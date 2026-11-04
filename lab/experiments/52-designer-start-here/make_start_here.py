#!/usr/bin/env python3
"""LAB 52: Start here's three figures (manuscript/rc2/150/00-start-here.md, lines 17, 31 and 65; the editor's LY1, the
opening pages' visuals; the publisher's 045).

    python3 lab/experiments/52-designer-start-here/make_start_here.py

- start-stones.svg: the five steps as numbered stones on a path, from an empty project to a second agent: numbers only,
  the words stay in the text above (his note, brief 03).
- start-route.svg: the five parts as stops on one route, the chapters beneath each, two ways marked: the whole way, and
  the short way (this page, then part five, then back to the start), as the page's narrator says.
- start-strip.svg: the day as a thin strip, its stops placed at their times in the record (C001, C011's first commit, the
  first five-step wake C088, the editor away and back as chapter 9 tells it, the hold C006, the talk due C100), no time
  printed; one number on it, "nearly nineteen hours" (C010: the title's rounding of 18 h 44 min).
No register id inside a drawing (convention 8); no caption drawn in.
"""
import json, re, sys
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'
REG = {c["id"]: c for c in json.loads((REPO / "claims" / "register.json").read_text())["claims"]}
CH00 = (REPO / "manuscript" / "rc2" / "150" / "00-start-here.md").read_text()


def t(x, y, s, weight=400, fill=mc.INK, anchor="middle", size=3.18):
    return (f'<text x="{x:.2f}" y="{y:.2f}" {SANS} font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}">{escape(s, quote=False)}</text>')


def stones():
    if "numbered stones only" not in CH00:
        sys.exit("make_start_here: line 17 no longer asks for numbered stones only")
    out = [mc.path("M14 30 C40 6, 62 42, 86 20 S128 8, 140 22", "none", mc.FILL2, 3.2)]
    pts = [(28, 20.4), (50, 24.4), (72, 27), (98, 15.6), (120, 13.4)]
    for k, (x, y) in enumerate(pts):
        out.append(f'<circle cx="{x}" cy="{y}" r="5.6" fill="{mc.ACCENT}" stroke="#fff" stroke-width=".8"/>'
                   + t(x, y + 1.7, str(k + 1), 800, "#fff", size=4.8))
    # the start, an empty project (a folder, open, nothing in it); the end, a second agent beside the first
    out.append(mc.path("M2 25 h6 l1.5 2 h7.5 v10 h-15 z", "#fff", mc.INK, .5))
    out.append(f'<g transform="translate(130 11) scale(.3)">{mc.head("dev")}</g><g transform="translate(140 13) scale(.3)">{mc.head("conductor")}</g>')
    return mc.svg(155, 40, "".join(out), "The five steps as five numbered stones on a path, from an empty project to a second agent")


PARTS = [("1", "chapters 1 to 3"), ("2", "chapters 4 to 8"), ("3", "chapters 9 to 15"), ("4", "chapters 16 to 19"), ("5", "chapters 20 to 23")]


def route():
    for _, ch in PARTS:
        if f"({ch})" not in CH00:
            sys.exit(f"make_start_here: the page no longer gives '{ch}'")
    if "this page, then part five, then back to the start" not in CH00:
        sys.exit("make_start_here: the page no longer gives the short way as drawn")
    y, xs = 30.0, [32 + k * 26 for k in range(5)]
    out = [mc.line(12, y, 148, y, mc.INK, .9)]
    out.append(f'<circle cx="12" cy="{y}" r="2.2" fill="{mc.INK}"/>' + t(12, y + 8.2, "start", 700, mc.MUTED))
    for (n, ch), x in zip(PARTS, xs):
        out.append(f'<circle cx="{x}" cy="{y}" r="5.2" fill="#fff" stroke="{mc.INK}" stroke-width=".7"/>'
                   + t(x, y + 1.5, n, 800, mc.INK, size=4.4) + t(x, y + 10.4, "part " + n, 700) + t(x, y + 14.6, ch.replace("chapters ", "ch. "), 400, mc.MUTED))
    # the short way: from the start over the top to part five, then back to part one
    out.append(f'<path d="M12 {y - 3} C30 4, 118 4, {xs[4]} {y - 6}" fill="none" stroke="{mc.ACCENT}" stroke-width=".9" stroke-dasharray="2 1.4"/>'
               f'<path d="M{xs[4]} {y - 6} l-.6 -3 l2.8 1.6 z" fill="{mc.ACCENT}"/>'
               f'<path d="M{xs[4] - 4} {y - 6.5} C100 14, 60 14, {xs[0] + 3} {y - 5.4}" fill="none" stroke="{mc.ACCENT}" stroke-width=".7" stroke-dasharray="1.2 1.2"/>'
               f'<path d="M{xs[0] + 3} {y - 5.4} l2.9 -.9 l-1.2 2.7 z" fill="{mc.ACCENT}"/>')
    out.append(t(80, 3.4, "the short way: part five first, then back to the start", 700, mc.ACCENT))
    out.append(t(80, y + 21, "the whole way: one part after another", 700, mc.INK))
    return mc.svg(155, round(y + 23, 1), "".join(out), "The book's five parts as stops on one route, the chapters under each, the whole way along the line and the short way over the top to part five and back")


def hm(s):
    h, m = re.match(r"(\d{1,2}):(\d{2})", s).groups()
    return int(h) + int(m) / 60


def strip():
    first = REG["C001"]["value"]
    if "00:16" not in json.dumps(first):
        sys.exit("make_start_here: C001 no longer gives 00:16")
    if REG["C010"]["state"] not in ("checked", "corrected"):
        sys.exit("make_start_here: C010 is not checked")
    # each stop at its time in the record; no time is printed
    # name, hour, label tier (above, negative; below, positive) and anchor: placed by hand so no two labels meet
    stops = [("the empty project", 0 + 16 / 60, -1, "start"), ("the first agent", 40 / 60, 1, "start"),
             ("the five steps", 2 + 16 / 60, -2, "start"), ("the six alone", 4 + 5 / 60, 2, "start"),
             ("my return", 13 + 50 / 60, -1, "middle"), ("the hold", 18 + 44 / 60, 1, "end"), ("the talk", 19.0, -1, "end")]
    x0, x1, y = 6.0, 149.0, 20.0
    X = lambda h: x0 + (x1 - x0) * h / 19.0
    out = [f'<rect x="{X(4 + 5 / 60):.2f}" y="{y - 1.6}" width="{X(13 + 50 / 60) - X(4 + 5 / 60):.2f}" height="3.2" fill="{mc.FILL}"/>',
           mc.line(x0, y, x1, y, mc.INK, .7)]
    for k, (name, h, tier, anchor) in enumerate(stops):
        x = X(h)
        ly = y + (tier * 5.2 + (-1.2 if tier < 0 else 2.6))
        out.append(f'<circle cx="{x:.2f}" cy="{y}" r="1.6" fill="{mc.ACCENT if name in ("the hold", "the talk") else mc.INK}"/>'
                   + mc.line(x, y + (-2 if tier < 0 else 2), x, ly + (1 if tier < 0 else -3.2), mc.FILL2, .3)
                   + t(x - (1 if anchor == "start" else 0) + (1 if anchor == "end" else 0), ly, name,
                       700 if k in (0, 6) else 400, mc.INK, anchor))
    out.append(t(77.5, y + 21, "nearly nineteen hours", 800, mc.ACCENT, size=4.2))
    return mc.svg(155, round(y + 23, 1), "".join(out), "The day as a thin strip, from the empty project to the talk, nearly nineteen hours")


if __name__ == "__main__":
    for name, svg in (("start-stones.svg", stones()), ("start-route.svg", route()), ("start-strip.svg", strip())):
        if re.search(r">[^<]*\bC\d{3}\b", svg):
            sys.exit(f"make_start_here: {name} draws a register id")
        (HERE / name).write_text(svg)
    print("written start-stones.svg, start-route.svg, start-strip.svg")
