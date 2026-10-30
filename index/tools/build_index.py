#!/usr/bin/env python3
"""Build the index of the talk's repository at a pinned commit (librarian@book.the-ultimate-insider).

Reads a local clone, read-only (git ls-tree, git log, git show); writes only into this
repository's index/. Usage:

    python3 index/tools/build_index.py <talk clone> [--at 298be4e] [--out index]

Each file gets: path, area, kind, owner, first and last commit at or before the pin
(with UTC time), size, and one line on what it is. The line is read from the file
itself (first heading, a JSON "about"-like field, a docstring); a line marked
"(machine)" has not yet been read by the librarian. Commits after the pin go to
after-the-day.md, kept apart.
"""
import argparse, collections, datetime, json, os, re, subprocess, sys

PIN_DEFAULT = "298be4e"
NOTE_KEYS = ("about", "title", "what", "summary", "description", "job", "state", "note", "kind")
TEXT_EXT = {".md", ".txt", ".json", ".py", ".mjs", ".js", ".sh", ".html", ".yml", ".yaml", ".css", ".eml", ".csv", ".toml", ""}
DASHES = {"\u2014": ", ", "\u2013": "-"}


def git(clone, *args):
    return subprocess.run(["git", "-C", clone, *args], check=True, capture_output=True, text=True).stdout


def clean(s, n=140):
    for a, b in DASHES.items():
        s = s.replace(a, b)
    s = re.sub(r"\s+", " ", s.replace("|", "/").replace("`", "")).strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "\u2026"


def area_of(p):
    parts = p.split("/")
    if len(parts) == 1 or parts[0] == ".github":
        return "root"
    if parts[0] == "admin":
        return "tools"
    if parts[0] == "team":
        return "team-" + parts[1]
    if parts[0] == "evidence":
        return "evidence"
    if parts[0] == "content":
        return "articles"
    if p.startswith("src/static/talk/"):
        return "talk"
    return "site"


KIND_RULES = [
    (r"(^|/)ROLE\.md$", "role"), (r"(^|/)policy\.json$", "policy"), (r"(^|/)status\.json$", "status"),
    (r"(^|/)HOLD\.md$", "hold"), (r"/sessions/", "session"), (r"(^|/)key\.(json|png)$", "key (public)"),
    (r"/wakes/", "wake record"), (r"/debriefs/img/", "debrief image"), (r"/debriefs/", "debrief"),
    (r"/reviews/", "review"), (r"/requests/", "request"), (r"/briefs/", "brief sent"), (r"/night/", "night log"),
    (r"/runs/", "run"), (r"/story/", "story work"), (r"/maps/", "map"), (r"/system/", "design system"),
    (r"^evidence/claims/", "claim"), (r"^evidence/sources/", "source"), (r"^evidence/incidents/", "incident"),
    (r"^evidence/ideas/", "idea"), (r"^evidence/proposals/", "proposal"), (r"^evidence/studio/", "studio evidence"),
    (r"^evidence/", "evidence"), (r"^content/articles/", "article"), (r"^admin/build/", "site build"),
    (r"^admin/tools/", "tool"), (r"^admin/", "admin note"), (r"^\.github/", "ci"),
    (r"^src/static/talk/slides/", "slide"), (r"^src/static/talk/engine/", "talk engine"), (r"^src/static/talk/", "talk"),
    (r"^src/pages/", "page"), (r"^src/static/.*/data/", "data"), (r"^src/", "site asset"),
    (r"(schedule|pace)\.json$", "schedule"), (r"\.md$", "document"),
]


def kind_of(p):
    for rx, k in KIND_RULES:
        if re.search(rx, p):
            return k
    return "file"


def note_of(clone, pin, p, kind):
    ext = os.path.splitext(p)[1].lower()
    if kind in ("key (public)",) or "/sessions/" in p:
        return "public key record of a member session" if ext != ".png" else "QR image of a member's public key"
    if ext in (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".ico"):
        return "image"
    if ext in (".woff", ".woff2", ".ttf", ".mp3", ".mp4", ".webm", ".pdf", ".zip"):
        return "binary (" + ext[1:] + ")"
    if ext not in TEXT_EXT:
        return ""
    try:
        text = git(clone, "show", f"{pin}:{p}")
    except subprocess.CalledProcessError:
        return ""
    if ext == ".json":
        try:
            d = json.loads(text)
        except ValueError:
            return "json (unparsed)"
        if isinstance(d, dict) and str(d.get("schema", "")).endswith("/wake/v1"):
            work = (d.get("steps") or {}).get("work") or {}
            first = re.split(r"(?<=[.;])\s", work.get("comment") or "", maxsplit=1)[0]
            return clean(f"{d.get('kind', 'wake')}; outcome {d.get('outcome') or 'not closed'}"
                         + (f"; work {work.get('verdict')}: {first}" if work else "; no work step"), 200)
        if isinstance(d, dict) and str(d.get("schema", "")).endswith("/night/v1"):
            n = lambda k: len(d.get(k) or [])
            return clean(f"night log snapshot {str(d.get('since'))[11:16]} to {str(d.get('until'))[11:16]} UTC: "
                         f"{n('wakes')} wakes, {n('commits')} commits, {n('made')} made, {n('mail')} mail, "
                         f"{n('problems')} problems, {n('holds')} holds")
        if isinstance(d, dict):
            for k in NOTE_KEYS:
                v = d.get(k)
                if isinstance(v, str) and v.strip():
                    return clean(f"{k}: {v}")
            return clean("json: " + ", ".join(list(d)[:8]))
        return f"json list of {len(d)}"
    if ext in (".py", ".mjs", ".js", ".sh"):
        m = re.search(r'"""(.+?)(?:\n|""")', text, re.S) or re.search(r"^\s*(?:#|//)\s*(?!!)(.+)$", text, re.M)
        return clean(m.group(1)) if m else ""
    if ext == ".html":
        m = re.search(r"<title>(.*?)</title>", text, re.S) or re.search(r"<h1[^>]*>(.*?)</h1>", text, re.S)
        if not m:
            m = re.search(r'"title"\s*:\s*"([^"]+)"', text)
        return clean(re.sub(r"<[^>]+>", "", m.group(1))) if m else ""
    fm = re.match(r"---\n(.*?)\n---\n", text, re.S)   # front matter: its title, if any
    if fm:
        t = re.search(r"^title:\s*(.+)$", fm.group(1), re.M)
        if t:
            return clean(t.group(1).strip("\"'"))
        text = text[fm.end():]
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith(("<!--", "---")):
            continue
        return clean(line.lstrip("#").strip())
    return ""


def utc(epoch):
    return datetime.datetime.fromtimestamp(int(epoch), datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


def history(clone, pin):
    """First and last commit touching each path, at or before the pin, in one pass."""
    first, last = {}, {}

    def scan(out, only=None):
        cur = None
        for line in out.splitlines():
            if line.startswith("@@"):
                h, t, a, s = line[2:].split("|", 3)
                m = re.match(r"@?([a-z0-9-]+):", s)
                cur = (h, utc(t), m.group(1) if m else ("ci" if "Actions" in a else a))
            elif line and cur and (only is None or line in only):
                last.setdefault(line, cur)   # log is newest first
                first[line] = cur

    fmt = "--format=@@%h|%ct|%an|%s"
    scan(git(clone, "log", pin, "--name-only", fmt, "--no-renames"))
    # files that first appear in a merge commit (a conflict resolved there) need -m
    missing = set(git(clone, "ls-tree", "-r", "--name-only", pin).splitlines()) - set(first)
    if missing:
        scan(git(clone, "log", pin, "-m", "--name-only", fmt, "--no-renames", "--", *sorted(missing)), missing)
    return first, last


def owner_of(p, first):
    parts = p.split("/")
    if parts[0] == "team" and len(parts) > 2:
        return parts[1]
    return first[2] if first else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("clone")
    ap.add_argument("--at", default=PIN_DEFAULT)
    ap.add_argument("--out", default="index")
    a = ap.parse_args()
    pin = git(a.clone, "rev-parse", "--short=7", a.at).strip()
    files = [f for f in git(a.clone, "ls-tree", "-r", "--name-only", pin).splitlines()]
    sizes = {}
    for line in git(a.clone, "ls-tree", "-r", "-l", pin).splitlines():
        meta, path = line.split("\t", 1)
        sizes[path] = meta.split()[3]
    first, last = history(a.clone, pin)
    read_path = os.path.join(a.out, "read.json")
    read = json.load(open(read_path))["read"] if os.path.exists(read_path) else {}
    rows = []
    for p in files:
        k = kind_of(p)
        f, l = first.get(p), last.get(p)
        rows.append({
            "path": p, "area": area_of(p), "kind": k, "owner": owner_of(p, f),
            "added": f[0] if f else "", "added_utc": f[1] if f else "",
            "changed": l[0] if l else "", "changed_utc": l[1] if l else "",
            "bytes": int(sizes.get(p, "0")) if sizes.get(p, "-") != "-" else 0,
            "what": note_of(a.clone, pin, p, k) or "", "read_by": "machine",
        })
        if p in read:
            rows[-1]["read_by"] = "librarian"
            if read[p]:
                rows[-1]["what"] = read[p]
    os.makedirs(os.path.join(a.out, "areas"), exist_ok=True)
    with open(os.path.join(a.out, "index.json"), "w") as fh:
        json.dump({"schema": "the-ultimate-insider/book-index/v1", "source": "SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider",
                   "at": pin, "files": len(rows), "rows": rows}, fh, indent=1)
        fh.write("\n")
    by_area = collections.defaultdict(list)
    for r in rows:
        by_area[r["area"]].append(r)
    for area, rs in sorted(by_area.items()):
        imgs = [r for r in rs if r["kind"] == "debrief image" or r["what"] == "image"]
        listed = [r for r in rs if r not in imgs]
        kinds = collections.Counter(r["kind"] for r in rs)
        with open(os.path.join(a.out, "areas", f"{area}.md"), "w") as fh:
            fh.write(f"# Index: {area}, the talk's repository at `{pin}`\n\n")
            fh.write(f"Generated by `index/tools/build_index.py` from a read-only clone. {len(rs)} files: "
                     + ", ".join(f"{n} {k}" for k, n in kinds.most_common()) + ". ")
            fh.write("Times are commit times, UTC. `added` and `changed` are the first and last commit touching the file at or before the pin. "
                     f"The line on what it is was read from the file by the tool; a line marked (machine) is not yet checked by the librarian ({sum(r['read_by'] == 'librarian' for r in rs)} of {len(rs)} checked).\n\n")
            fh.write("| path | kind | owner | added | changed | what it is |\n|---|---|---|---|---|---|\n")
            for r in sorted(listed, key=lambda r: r["path"]):
                fh.write(f"| `{r['path']}` | {r['kind']} | {r['owner']} | `{r['added']}` {r['added_utc']} | `{r['changed']}` {r['changed_utc']} | {r['what']}{'' if r['read_by'] == 'librarian' else ' (machine)'} |\n")
            if imgs:
                dirs = collections.Counter(os.path.dirname(r["path"]) for r in imgs)
                fh.write(f"\n{len(imgs)} images, listed by folder (each is in `index.json`):\n\n")
                for d, n in sorted(dirs.items()):
                    fh.write(f"- `{d}/`: {n}\n")
    # after the day: commits after the pin, kept apart
    after = git(a.clone, "log", "--reverse", f"{pin}..HEAD", "--format=@@%h|%ct|%s", "--name-status", "--no-renames")
    head = git(a.clone, "rev-parse", "--short=7", "HEAD").strip()
    with open(os.path.join(a.out, "after-the-day.md"), "w") as fh:
        fh.write(f"# Added after the day: the talk's repository, `{pin}..{head}`\n\n"
                 "Material committed after the record of the day closed at `298be4e`. Cite it by commit and say it was added after the day. "
                 "Generated by `index/tools/build_index.py`; status A added, M modified, D deleted.\n")
        for line in after.splitlines():
            if line.startswith("@@"):
                h, t, s = line[2:].split("|", 2)
                fh.write(f"\n## `{h}` {utc(t)} UTC\n\n{clean(s, 300)}\n\n")
            elif line.strip():
                st, path = line.split("\t", 1)
                fh.write(f"- {st} `{path}`\n")
    print(f"index: {len(rows)} files at {pin} in {len(by_area)} areas; after the day: {pin}..{head}")


if __name__ == "__main__":
    sys.exit(main())
