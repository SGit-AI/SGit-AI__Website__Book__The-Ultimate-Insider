#!/usr/bin/env python3
"""LAB 51: this book's team arriving, drawn like the talk's cast bar but over four days (chapter 94's line; the
newsroom's picture idea 3, "the book's own factory").

    python3 lab/experiments/51-designer-book-team-arriving/make_arriving.py

The twelve members whose first commit falls before 4 November, from C131 (claims/register.json, read at build): one head
each, in the order they arrived, and a leader from each to its moment on a line of four days, 30 October to 2 November.
Synthetic and the developer have no cast drawing yet, so they take the cast's plain head, no headgear. Names only: no
key, session, task or count. No caption drawn in (convention 8).
"""
import json, sys
from datetime import datetime
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'
START = datetime(2026, 10, 30)
DAYS = ["30 October", "31 October", "1 November", "2 November"]


def t(x, y, s, weight=400, fill=mc.INK, anchor="middle"):
    return (f'<text x="{x:.2f}" y="{y:.2f}" {SANS} font-size="3.18" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}">{escape(s, quote=False)}</text>')


def arrivals():
    reg = {c["id"]: c for c in json.loads((REPO / "claims" / "register.json").read_text())["claims"]}
    if reg["C131"]["state"] != "checked":
        sys.exit("make_arriving: C131 is not checked")
    out = []
    for m, v in reg["C131"]["value"]["members"].items():
        when = datetime.strptime("2026 " + v["first_commit"], "%Y %d %b %H:%M:%S")
        if when < datetime(2026, 11, 4):
            out.append((when, m))
    out.sort()
    if len(out) != 12:
        sys.exit(f"make_arriving: C131 gives {len(out)} members before 4 November, the line says twelve")
    return out


def plain_head():
    return (f'<rect x="10" y="10" width="20" height="16" rx="3.2" fill="{mc.FILL}" stroke="{mc.INK}" stroke-width="{mc.SW * 1.6}"/>'
            + mc.face("happy"))


def main():
    team = arrivals()
    W, step, s = 155.0, 12.4, .4
    x0, axis_y, ax0, ax1 = 9.0, 40.0, 4.0, 151.0  # the first name centred clear of the edge
    out = []
    span = 4 * 24 * 3600
    for k, (when, m) in enumerate(team):
        cx = x0 + k * step
        head = mc.head(m, True) if m in mc.COLOUR else plain_head()
        out.append(f'<g transform="translate({cx - 20 * s:.2f} {-3.2 * s:.2f}) scale({s})">{head}</g>')
        out.append(t(cx, 13.4 if k % 2 == 0 else 17.6, m, 700))
        ax = ax0 + (ax1 - ax0) * (when - START).total_seconds() / span
        out.append(mc.line(cx, 19 if k % 2 == 0 else 19.6, ax, axis_y - 1.4, mc.FILL2, .35)
                   + f'<circle cx="{ax:.2f}" cy="{axis_y:.2f}" r="1" fill="{mc.ACCENT}"/>')
    # the four days
    out.append(mc.line(ax0, axis_y, ax1, axis_y, mc.INK, .5))
    for d in range(5):
        x = ax0 + (ax1 - ax0) * d / 4
        out.append(mc.line(x, axis_y - 1.6, x, axis_y + 1.6, mc.INK, .4))
    for d, name in enumerate(DAYS):
        out.append(t(ax0 + (ax1 - ax0) * (d + .5) / 4, axis_y + 6, name, 400, mc.MUTED))
    svg = mc.svg(W, axis_y + 8, "".join(out), "This book's team arriving: twelve members, one head each in the order they came, over four days from 30 October to 2 November")
    (HERE / "book-team-arriving.svg").write_text(svg)
    print("written book-team-arriving.svg: " + ", ".join(m for _, m in team))


if __name__ == "__main__":
    main()
