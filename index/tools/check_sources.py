#!/usr/bin/env python3
"""Check a chapter's sources (librarian@book.the-ultimate-insider).

Reads each chapter's `## Where this came from` section, and every register id anywhere in it,
and checks that each path, commit and register id it names exists. Read only: it writes
nothing but its report to stdout. Usage:

    python3 index/tools/check_sources.py --talk <talk clone> [--cold-read <clone>] <chapter.md> ...

A path is found if it exists in this repository, in the talk's repository at 298be4e or at
its latest commit (said so: added after the day), or in the Cold-Read clone; a bare file name
is found if exactly one file anywhere has that name. A commit is found in any of the three.
A register id is found in claims/register.json.
"""
import argparse, json, os, re, subprocess, sys

PIN = "298be4e"
TICK = re.compile(r"`([^`\n]+)`")
HEX = re.compile(r"^[0-9a-f]{7,40}$")
REG = re.compile(r"\bC\d{3}\b")


def git(clone, *args):
    r = subprocess.run(["git", "-C", clone, *args], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def tree(clone, ref):
    out = git(clone, "ls-tree", "-r", "--name-only", ref) if clone else None
    return set(out.splitlines()) if out else set()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--talk", required=True)
    ap.add_argument("--cold-read")
    ap.add_argument("chapters", nargs="+")
    a = ap.parse_args()
    here = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sources = {
        "here": set((git(here, "ls-files") or "").splitlines()),
        f"talk@{PIN}": tree(a.talk, PIN),
        "talk, added after the day": tree(a.talk, "HEAD") - tree(a.talk, PIN),
        "cold-read": tree(a.cold_read, "HEAD"),
    }
    dirs = {k: {p.rsplit("/", i)[0] for p in v for i in range(1, p.count("/") + 1)} for k, v in sources.items()}
    names = {}
    for k, v in sources.items():
        for p in v:
            names.setdefault(os.path.basename(p), set()).add((k, p))
    reg = {c["id"] for c in json.load(open(os.path.join(here, "claims/register.json")))["claims"]}
    clones = [here, a.talk] + ([a.cold_read] if a.cold_read else [])
    problems = 0
    for ch in a.chapters:
        lines = open(ch).read().splitlines()
        start = next((i for i, l in enumerate(lines) if l.strip().lower().startswith("## where this came from")), None)
        report = []
        if start is None:
            report.append(("-", "no `## Where this came from` section"))
        for i, line in enumerate(lines):
            for cid in REG.findall(line):
                if cid not in reg:
                    report.append((i + 1, f"register id {cid} is not in claims/register.json"))
            if start is None or i < start:
                continue
            for tok in TICK.findall(line):
                t = tok.strip().rstrip("/").split(":")[-1] if tok.count(":") == 1 and "/" in tok.split(":")[-1] else tok.strip().rstrip("/")
                if HEX.match(t):
                    if not any(git(c, "cat-file", "-e", f"{t}^{{commit}}") is not None for c in clones):
                        report.append((i + 1, f"commit {t} not found in this repository, the talk's or the Cold-Read's"))
                    continue
                if " " in t or ("/" not in t and "." not in t):
                    continue   # prose in backticks, a command, an id: not a path
                where = [k for k in sources if t in sources[k] or t in dirs[k]]
                if not where and "/" not in t:
                    hits = names.get(t, set())
                    if len(hits) == 1:
                        where = [f"{next(iter(hits))[0]} as {next(iter(hits))[1]}"]
                    elif len(hits) > 1:
                        report.append((i + 1, f"`{t}` is ambiguous: {len(hits)} files have that name; give the path"))
                        continue
                if not where:
                    report.append((i + 1, f"path `{t}` not found in this repository, the talk's or the Cold-Read's"))
                elif where == ["talk, added after the day"]:
                    report.append((i + 1, f"`{t}` was added after the day: check the chapter says so"))
        problems += len(report)
        print(f"{ch}: {'clean' if not report else str(len(report)) + ' finding(s)'}")
        for ln, msg in report:
            print(f"  line {ln}: {msg}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
