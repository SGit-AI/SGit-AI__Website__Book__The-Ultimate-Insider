#!/usr/bin/env python3
"""Count the sgit.ai pages named in the talk's history (the editor's past projects).

Read only and offline: it runs git against a clone of the talk's repository and reads files from it.

    python3 past_projects_scan.py <clone of the talk's repository> [end commit, default cb5b996] [--used]

The rule, stated once so a count can be rerun and diffed:
  PAGE      a host ending in sgit.ai (any number of labels before it) followed by a path of any number of
            segments; the scheme (http or https) is dropped, a fragment (#...) or query (?...) is dropped,
            trailing punctuation . , ) ; : ' " * ` > ] is stripped; a path of nothing is "/"; a trailing
            slash is NOT folded (so /x and /x/ are two pages); case is not folded.
  HISTORY   every added line (git log -p -U0 -G sgit.ai, oldest first, up to the end commit) is read; a page
            counts if it was ever added, even if a later commit removed it; a mention is one URL match.
  TREE      the same pattern over the files as they stand at the end commit (git grep).
  CATEGORY  of the file an added line sits in: editor_words (a quoted line, starting ">", in BRIEF.md or a
            file under team/conductor/briefs/), brief_text (any other line there), research (evidence/),
            slide (src/static/talk/), page (src/ and content/), member_note (anything else under team/),
            site_tool (index/, admin/, .github), other.
  USED      a page with at least one mention in editor_words, brief_text, member_note, page or slide
            (that is, not only in the researcher's evidence files).
  CAPTURES  entries of evidence/sources/manifest.json whose url contains sgit.ai.
"""
import collections, json, re, subprocess, sys

URL = re.compile(r'((?:https?://)?(?:[a-z0-9-]+\.)*sgit\.ai)((?:/[A-Za-z0-9_.%~#?=&+-]*)*)')
USE = ("editor_words", "brief_text", "member_note", "page", "slide")


def git(clone, *a):
    return subprocess.run(["git", "-C", clone, *a], capture_output=True, text=True, errors="replace").stdout


def page_of(m):
    host = m.group(1).replace("https://", "").replace("http://", "")
    path = re.sub(r"[#?].*$", "", m.group(2).rstrip(".,);:'\"*`>]")) or "/"
    return host, path


def category(f, quote):
    if f is None: return "other"
    if f == "BRIEF.md" or f.startswith("team/conductor/briefs/"): return "editor_words" if quote else "brief_text"
    if f.startswith("evidence/"): return "research"
    if f.startswith("src/static/talk/"): return "slide"
    if f.startswith("src/") or f.startswith("content/"): return "page"
    if f.startswith("team/"): return "member_note"
    if f.startswith(("index/", "admin/", ".github")): return "site_tool"
    return "other"


def main():
    clone = sys.argv[1]
    end = next((a for a in sys.argv[2:] if not a.startswith("--")), "cb5b996")
    tree = git(clone, "grep", "-h", "-I", r"sgit\.ai", end)
    tp = {page_of(m) for l in tree.split("\n") for m in URL.finditer(l)}
    print(f"TREE at {end}: lines naming sgit.ai {sum(1 for l in tree.split(chr(10)) if l)}, pages {len(tp)}, hosts {len({h for h, _ in tp})}")
    nr = git(clone, "grep", "-h", "-I", r"newsroom\.sgit\.ai", end)
    print(f"TREE at {end}: lines naming newsroom.sgit.ai {sum(1 for l in nr.split(chr(10)) if l)}, mentions {len(re.findall(r'newsroom[.]sgit[.]ai', nr))}")
    log = git(clone, "log", "-p", "--reverse", "--no-color", "-U0", "-G", r"sgit\.ai", "--format=@@C|%ad|%an|%s", "--date=format:%H:%M:%S", end)
    pages, cats, cur, f = {}, collections.Counter(), None, None
    for line in log.split("\n"):
        if line.startswith("@@C|"):
            _, t, an, subj = line.split("|", 3); cur = (t, re.sub(r"^@?([a-z][a-z0-9.-]*)[:@ ].*", r"\1", subj)); f = None; continue
        if line.startswith("+++ b/"): f = line[6:].strip(); continue
        if line.startswith("+") and not line.startswith("+++") and "sgit.ai" in line and cur:
            c = category(f, line[1:].strip().startswith(">"))
            for m in URL.finditer(line):
                k = page_of(m); cats[c] += 1
                e = pages.setdefault(k, {"first": {}, "cats": collections.Counter()})
                e["cats"][c] += 1; e["first"].setdefault(c, (cur[0], cur[1], f))
    print(f"HISTORY to {end}: pages {len(pages)}, hosts {len({h for h, _ in pages})}, mentions added {sum(cats.values())}")
    print("  mentions by category:", dict(cats))
    used = {k: e for k, e in pages.items() if any(c in e["cats"] for c in USE)}
    print(f"  used pages: {len(used)}")
    man = json.loads(git(clone, "show", f"{end}:evidence/sources/manifest.json"))["sources"]
    cap = [s for s in man if "sgit.ai" in (s.get("url") or "")]
    print(f"CAPTURES: sources {len(man)}, on sgit.ai {len(cap)}, status 200 {sum(1 for s in cap if s.get('http_status') == 200)}")
    host = lambda s: re.search(r"https?://([^/]+)", s["url"]).group(1)
    print("  articles on newsroom.sgit.ai itself:", sum(1 for s in cap if host(s) == "newsroom.sgit.ai" and "/articles/" in s["url"]))
    print("  articles on a sub-site of it:", sum(1 for s in cap if host(s).endswith(".newsroom.sgit.ai") and "/articles/" in s["url"]))
    if "--used" in sys.argv:
        for (h, p), e in sorted(used.items(), key=lambda kv: min(v[0] for c, v in kv[1]["first"].items() if c in USE)):
            c, v = min(((c, v) for c, v in e["first"].items() if c in USE), key=lambda cv: cv[1][0])
            print(f"{v[0]}\t{v[1]}\t{c}\t{h}{p}")


main()
