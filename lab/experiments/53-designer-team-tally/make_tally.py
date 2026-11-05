#!/usr/bin/env python3
"""LAB 53: the team's tally for chapter 16 ("the team's tally: every member's commits and sessions for the day, side by
side"; its brief: "drawn as a card each, the conductor's card first"; brief 13, the dashboard as the team's high five).

    python3 lab/experiments/53-designer-team-tally/make_tally.py

Nine cards, one per member of the talk's team: its head, its name, its commits and its sessions (wakes) for the day,
read from C119 at build (checked); the conductor first, then by commits. No id drawn (P28): the record line carries C119.
"""
import json, sys
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'


def t(x, y, s, weight=400, fill=mc.INK, anchor="start", size=3.18):
    return (f'<text x="{x:.2f}" y="{y:.2f}" {SANS} font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}">{escape(str(s), quote=False)}</text>')


def main():
    reg = {c["id"]: c for c in json.loads((REPO / "claims" / "register.json").read_text())["claims"]}
    c = reg["C119"]
    if c["state"] != "checked":
        sys.exit("make_tally: C119 is not checked")
    m = c["value"]["members"]
    if set(m) != set(mc.CAST):
        sys.exit("make_tally: C119's members are not the nine")
    order = ["conductor"] + sorted((k for k in m if k != "conductor"), key=lambda k: -m[k]["commits"])
    w, h, gx, gy, out = 51.6, 27.0, 1.3, 2.0, []
    for i, k in enumerate(order):
        x, y = (i % 3) * (w + gx) + .3, (i // 3) * (h + gy) + .3
        col = mc.CAST[k][0]
        out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w}" height="{h}" rx="1.8" fill="#fff" stroke="{mc.FILL2}" stroke-width=".45"/>'
                   f'<rect x="{x:.1f}" y="{y:.1f}" width="2.2" height="{h}" rx="1" fill="{col}"/>'
                   f'<g transform="translate({x + 1.6:.2f} {y + 1.2:.2f}) scale(.42)">{mc.head(k)}{mc.over_face(k, col)}{mc.neckwear(k, col) if k == "deck" else ""}</g>'
                   + t(x + 20, y + 8.4, k, 800)
                   + t(x + 20, y + 19.6, m[k]["commits"], 800, mc.INK, size=7.2)
                   + t(x + 20, y + 24.4, "commits", 400, mc.MUTED)
                   + t(x + w - 2.6, y + 19.6, m[k]["wakes"], 800, col, "end", 5.2)
                   + t(x + w - 2.6, y + 24.4, "sessions", 400, mc.MUTED, "end"))
    rows = (len(order) + 2) // 3
    svg = mc.svg(158, round(rows * (h + gy) - gy + .6, 1), "".join(out),
                 "The team's tally: nine cards, each member's commits and sessions for the day, the conductor's first")
    (HERE / "team-tally.svg").write_text(svg)
    print("written team-tally.svg: " + ", ".join(f"{k} {m[k]['commits']}/{m[k]['wakes']}" for k in order))


if __name__ == "__main__":
    main()
