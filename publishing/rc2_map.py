#!/usr/bin/env python3
"""RC2's figure map, rebuilt: publishing/rc2-figures.json, read by build_book.py --cast --figures.

The routine the publisher ran by hand each wake from 3 November 2026, as one script. It reads the designer's list
(lab/tools/book/rc2-70-figures.json, read only) and the writer's chapters (manuscript/rc2/, read only), and writes
only publishing/rc2-figures.json:

1. the designer's slots for every chapter that exists (the seventy), by Figure order;
2. the publisher's own placements from the file's "overrides" key (chapter: {opening words of a Figure line:
   drawing}), so a fresh copy of the designer's list cannot drop them;
3. the full book (manuscript/rc2/150/) recomputed: from 3 November 22:50 UTC it starts from the designer's own list for
   it (lab/tools/book/rc2-150-figures.json, read only), for each chapter whose slot count matches its Figure lines; each
   line still blank takes the drawing already placed in the thirty or the seventy whose line has the same first 40
   characters, or the three frames; then its overrides;
4. keys for chapters that no longer exist dropped;
5. every chapter's count and every drawing checked with the build's own rules (edition.figure_count,
   edition.unsafe_svg, the screenshot kinds): a mismatch stops it, and the file is not written.

    python3 publishing/rc2_map.py
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "publishing"))
import edition  # noqa: E402

MAP = os.path.join(ROOT, "publishing", "rc2-figures.json")
DESIGNER = os.path.join(ROOT, "lab", "tools", "book", "rc2-70-figures.json")
DESIGNER_150 = os.path.join(ROOT, "lab", "tools", "book", "rc2-150-figures.json")
MANUSCRIPT = os.path.join(ROOT, "manuscript")
FRAMES = "lab/experiments/01-ruv-the-building-three-frames/edition/three-frames.svg"
META = ("about", "overrides")


def briefs(chapter):
    """For each Figure and Map line, the first drawing path named on a "%% figure brief" line after it and before the
    next Figure line (the writers moved the paths there, conductor__033), or None."""
    with open(os.path.join(MANUSCRIPT, chapter), encoding="utf-8") as f:
        rows = [x.strip() for x in f.read().split("\n")]
    out, cur = [], None
    for x in rows:
        if x.startswith(("**Figure:**", "**Map:**")):
            out.append(None)
            cur = len(out) - 1
        elif cur is not None and out[cur] is None and re.match(r"`?%%\s*figure brief", x):
            m = edition.LAB_SVG.search(x)
            if m:
                out[cur] = m.group(0)
    return out


def lines(chapter):
    """A chapter's Figure and Map lines, their words only."""
    with open(os.path.join(MANUSCRIPT, chapter), encoding="utf-8") as f:
        return [re.sub(r"^\*\*(Figure|Map):\*\*\s*", "", x.strip()) for x in f.read().split("\n")
                if x.strip().startswith(("**Figure:**", "**Map:**"))]


def exists(chapter):
    return os.path.isfile(os.path.join(MANUSCRIPT, chapter))


HELD = set()  # (chapter, slot) an override holds blank with "": the box prints, and no brief fills it


def apply_overrides(d, chapters):
    n = 0
    for k in chapters:
        if not exists(k):
            continue
        for i, line in enumerate(lines(k)):
            for words, drawing in d["overrides"][k].items():
                if line.lower().startswith(words.lower()):
                    d[k][i] = drawing or None
                    if drawing == "":
                        HELD.add((k, i))
                    n += 1
    return n


def main():
    with open(MAP, encoding="utf-8") as f:
        d = json.load(f)
    d.setdefault("overrides", {})
    with open(DESIGNER, encoding="utf-8") as f:
        slots = json.load(f)["slots"]
    for k, v in slots.items():
        if exists(k):
            d[k] = list(v)
    a1 = apply_overrides(d, [k for k in d["overrides"] if not k.startswith("rc2/150/")])
    known = {}
    for k, v in d.items():
        if k in META or k.startswith("rc2/150/") or not exists(k):
            continue
        for line, drawing in zip(lines(k), v):
            if drawing:
                known.setdefault(line[:40], drawing)
    slots150 = {}
    if os.path.isfile(DESIGNER_150):
        with open(DESIGNER_150, encoding="utf-8") as f:
            slots150 = json.load(f).get("slots", {})
    from_designer = 0
    for path in sorted(glob.glob(os.path.join(MANUSCRIPT, "rc2", "150", "*.md"))):
        k = os.path.relpath(path, MANUSCRIPT)
        ls = lines(k)
        base = slots150.get(k)
        if base is None or len(base) != len(ls):
            base = [None] * len(ls)
        else:
            from_designer += 1
        d[k] = [b or (FRAMES if "three frames of the animation" in line.lower() else known.get(line[:40]))
                for b, line in zip(base, ls)]
    a2 = apply_overrides(d, [k for k in d["overrides"] if k.startswith("rc2/150/")])
    b = 0
    for path in sorted(glob.glob(os.path.join(MANUSCRIPT, "rc2", "150", "*.md"))):  # a blank slot takes its brief's path
        k = os.path.relpath(path, MANUSCRIPT)
        bs = briefs(k)
        for i, named in enumerate(bs):  # never a drawing the chapter already places, or one another line's brief names
            if i < len(d[k]) and not d[k][i] and named and named not in d[k] and (k, i) not in HELD \
                    and sum(1 for x in bs if x == named) == 1:
                d[k][i] = named
                b += 1
    for k in list(d):
        if k not in META and not exists(k):
            del d[k]
    problems = []
    for k, v in d.items():
        if k in META:
            continue
        with open(os.path.join(MANUSCRIPT, k), encoding="utf-8") as f:
            count = edition.figure_count(f.read())
        if count != len(v):
            problems.append(f"{k}: {len(v)} slot(s) for {count} Figure line(s)")
        for drawing in v:
            if not drawing:
                continue
            full = os.path.join(ROOT, drawing)
            if not os.path.isfile(full):
                problems.append(f"{k}: no such drawing {drawing}")
            elif drawing.endswith(".svg"):
                with open(full, encoding="utf-8", errors="replace") as f:
                    why = edition.unsafe_svg(f.read())
                if why:
                    problems.append(f"{k}: {drawing} has {why}")
            elif not drawing.startswith(edition.SHOTS) or not edition.shot_allowed(drawing[len(edition.SHOTS):]):
                problems.append(f"{k}: {drawing} is not a cleared screenshot")
    if problems:
        sys.exit("rc2_map: not written:\n  " + "\n  ".join(problems))
    with open(MAP, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=1)
        f.write("\n")
    drawn = {ed: sum(1 for k, v in d.items() if k.startswith(f"rc2/{ed}/") for x in v if x) for ed in ("30", "70", "150")}
    print(f"rc2_map: full-book chapters from the designer's list {from_designer}; overrides applied {a1} + {a2}; from briefs {b}; lines with a drawing: thirty {drawn['30']}, seventy {drawn['70']}, "
          f"full book {drawn['150']}")


if __name__ == "__main__":
    main()
