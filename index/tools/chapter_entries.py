#!/usr/bin/env python3
"""The index entries each chapter draws on (librarian@book.the-ultimate-insider).

Reads each chapter's `## Where this came from` section and, for every path it names, finds the
row in the index: the talk's (`index/index.json`, at 298be4e), the Cold-Read's
(`index/cold-read/index.json`), or this repository's own files. Paths are resolved as
`check_sources.py` resolves them: a path is also tried under the folders of the paths found
earlier on its line, and a bare name among the files in those folders. Writes
`index/chapters/<chapter>.md` and `index/chapters/README.md`; reads nothing else. Usage:

    python3 index/tools/chapter_entries.py [--talk <talk clone>] manuscript/*.md

With --talk, a file added to the talk's repository after 298be4e (`index/after-the-day.md`) is
placed too, marked as added after the day. A folder a chapter names is placed as a folder.
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TICK = re.compile(r"`([^`\n]+)`")
HEX = re.compile(r"^[0-9a-f]{7,40}$")


def rows(path):
    return {r["path"]: r for r in json.load(open(os.path.join(HERE, path)))["rows"]}


def main():
    talk, cold = rows("index/index.json"), rows("index/cold-read/index.json")
    args = sys.argv[1:]
    after = {}
    if args[:1] == ["--talk"]:
        clone, args = args[1], args[2:]
        tree = lambda ref: set(subprocess.run(["git", "-C", clone, "ls-tree", "-r", "--name-only", ref], capture_output=True, text=True).stdout.split())
        after = {p: None for p in tree("HEAD") - tree("298be4e")}
    here = set(subprocess.run(["git", "-C", HERE, "ls-files"], capture_output=True, text=True).stdout.split())
    sources = [("talk at 298be4e", talk), ("Cold-Read", cold), ("this repository", {p: None for p in here}), ("talk, added after the day", after)]
    dirs = {name: {p.rsplit("/", j)[0] for p in s for j in range(1, p.count("/") + 1)} for name, s in sources}
    out_dir = os.path.join(HERE, "index/chapters")
    os.makedirs(out_dir, exist_ok=True)
    summary = []
    for ch in sorted(args):
        lines = open(ch).read().splitlines()
        start = next((i for i, l in enumerate(lines) if l.strip().lower().startswith("## where this came from")), None)
        found, commits, unresolved = {}, [], []
        for line in lines[start + 1:] if start is not None else []:
            ctx = []
            for tok in TICK.findall(line):
                t = tok.strip().rstrip("/")
                if HEX.match(t):
                    commits.append(t)
                    continue
                if " " in t or "/" not in t and "." not in t or "<" in t or "*" in t:
                    continue
                hit = None
                for cand in [t] + [d + "/" + t for d in ctx]:
                    hit = next(((name, cand) for name, s in sources if cand in s or cand in dirs[name]), None)
                    if hit:
                        break
                if not hit and "/" not in t:
                    near = [(name, p) for name, s in sources for p in s if os.path.basename(p) == t and os.path.dirname(p) in ctx]
                    hit = near[0] if len(near) == 1 else None
                if hit:
                    found.setdefault(hit, None)
                    ctx = [hit[1].rsplit("/", j)[0] for j in range(1, hit[1].count("/") + 1)] + ctx
                elif "/" in t or t.endswith((".md", ".json", ".py", ".html")):
                    unresolved.append(t)
        name = os.path.basename(ch)
        L = [f"# The index entries `{name}` draws on", "",
             f"From the chapter's `## Where this came from` in `manuscript/{name}`, resolved by `index/tools/chapter_entries.py`. "
             "Each row is the index's own entry for the file: kind, owner, when it was added and last changed, and what it is.", ""]
        for src, table in sources:
            hits = [p for (s, p) in found if s == src]
            if not hits:
                continue
            L += [f"## {src} ({len(hits)})", ""]
            if src in ("talk at 298be4e", "Cold-Read"):
                L += ["| Path | Kind | Owner | Added | Last changed | What it is |", "|---|---|---|---|---|---|"]
                for p in hits:
                    r = table.get(p) or {"kind": "folder"}
                    L.append("| `%s` | %s | %s | `%s` %s | `%s` %s | %s |" % (p, r.get("kind", ""), r.get("owner", ""), r.get("added", ""),
                             r.get("added_utc", ""), r.get("changed", ""), r.get("changed_utc", ""), (r.get("what") or "").replace("|", "/")))
            else:
                L += [f"- `{p}`" for p in hits]
            L.append("")
        if commits:
            L += [f"## Commits named ({len(dict.fromkeys(commits))})", "", ", ".join(f"`{c}`" for c in dict.fromkeys(commits)), ""]
        if unresolved:
            L += ["## Not in any index", "", "Paths the tool could not place (outside the three repositories, or a web address): " +
                  ", ".join(f"`{u}`" for u in dict.fromkeys(unresolved)), ""]
        open(os.path.join(out_dir, name), "w").write("\n".join(L).rstrip() + "\n")
        counts = {src: sum(1 for (s, _) in found if s == src) for src, _ in sources}
        summary.append((name, counts, len(dict.fromkeys(commits)), len(dict.fromkeys(unresolved))))
    R = ["# The index entries each chapter draws on", "",
         "One file per chapter of the manuscript, built by `index/tools/chapter_entries.py` from each chapter's `## Where this came from`: "
         "the index's entry for every file the chapter cites, by repository, and the commits it names. ROLE.md, Done when 3. "
         "Rebuild after each revision: `python3 index/tools/chapter_entries.py manuscript/*.md`.", "",
         "| Chapter | Talk files | Cold-Read files | This repository's files | Talk, after the day | Commits | Not placed |", "|---|---|---|---|---|---|---|"]
    for name, c, n, u in summary:
        R.append(f"| [`{name}`]({name}) | {c['talk at 298be4e']} | {c['Cold-Read']} | {c['this repository']} | {c['talk, added after the day']} | {n} | {u} |")
    open(os.path.join(out_dir, "README.md"), "w").write("\n".join(R) + "\n")


if __name__ == "__main__":
    main()
