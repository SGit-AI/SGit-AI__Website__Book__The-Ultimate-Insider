#!/usr/bin/env python3
"""LAB 57: the day at a glance (manuscript/rc2/150/03b-the-day-at-a-glance.md, line 7): the talk's day as one picture,
each hour's work marked on it, and the chapters of this book beneath the hours they tell.

    python3 lab/experiments/57-designer-day-at-a-glance/make_day.py

The nineteen clock hours of 29 October, 00 to 18, printed as the book's hours one to nineteen (hour N is clock hour N-1,
the conductor's CK1). Each hour's work is its commits, the "all" row of claims/talk-commits-by-member-hour.md (C095,
checked), its sum checked at build. The four phases and their hour ranges as the chapter's own words give them, checked
at build; the chapters beneath, as its figure brief lists them. Counts on the picture only; no register id drawn.
"""
import json, re, sys
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'
CH = (REPO / "manuscript" / "rc2" / "150" / "03b-the-day-at-a-glance.md").read_text()
PHASES = [("the setup", 1, 5, "The setup, hours one to five"), ("the flow", 6, 13, "The flow, hours six to thirteen"),
          ("the acceleration", 14, 18, "The acceleration, hours fourteen to eighteen"), ("the crunch and the stop", 19, 19, "the crunch and the stop, hour nineteen")]
CHAPTERS = [("4", 1, 1), ("5", 2, 2), ("7", 3, 3), ("8", 4, 5), ("9", 6, 14), ("12", 14, 15), ("14", 16, 17), ("15", 18, 18), ("16", 19, 19)]


def t(x, y, s, weight=400, fill=mc.INK, anchor="middle", size=3.18):
    return (f'<text x="{x:.2f}" y="{y:.2f}" {SANS} font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}">{escape(str(s), quote=False)}</text>')


def commits():
    reg = {c["id"]: c for c in json.loads((REPO / "claims" / "register.json").read_text())["claims"]}
    if reg["C095"]["state"] != "checked":
        sys.exit("make_day: C095 is not checked")
    table = (REPO / "claims" / "talk-commits-by-member-hour.md").read_text()
    row = next(l for l in table.splitlines() if l.startswith("| **all**"))
    cells = [c.strip().strip("*") for c in row.strip("|").split("|")][1:]
    n = [int(c) for c in cells[:19]]
    if sum(n) != int(cells[19]) or sum(n) != reg["C095"]["value"]["non_merge_commits"]:
        sys.exit("make_day: the hours do not add up to C095's total")
    return n


def table():
    """Every row of C095's table, checked: each row adds to its total, the columns to the all row."""
    rows = {}
    for l in (REPO / "claims" / "talk-commits-by-member-hour.md").read_text().splitlines():
        if l.startswith("| ") and not l.startswith("| Member") and not l.startswith("|---"):
            cells = [c.strip().strip("*") for c in l.strip("|").split("|")]
            n = [int(c) for c in cells[1:21]]
            if sum(n[:19]) != n[19]:
                sys.exit(f"make_day: row {cells[0]} does not add up")
            rows[cells[0]] = n[:19]
    allrow = rows.pop("all")
    if [sum(r[h] for r in rows.values()) for h in range(19)] != allrow:
        sys.exit("make_day: the columns do not add up to the all row")
    return rows


def heat():
    rows = table()
    names = list(rows)
    lw, cw, ch, y0 = 26.0, 6.8, 5.6, 6.0
    big = max(max(r) for k, r in rows.items() if k not in ("releases", "other (no @member prefix)"))
    out = [t(lw + 19 * cw / 2, 3.4, "hours of the day, one to nineteen", 400, mc.MUTED)]
    for h in range(19):
        out.append(t(lw + h * cw + cw / 2, y0 + 3.6, h + 1, 700 if h in (0, 18) else 400))
    y = y0 + 5.6
    for i, k in enumerate(names):
        if k == "releases":
            y += 3.0  # a gap: below it, rows that are not one member
        label = {"other (no @member prefix)": "unnamed"}.get(k, k)
        out.append(t(lw - 1.6, y + ch / 2 + 1.1, label, 700 if k not in ("releases", "other (no @member prefix)") else 400,
                     mc.INK if k not in ("releases", "other (no @member prefix)") else mc.MUTED, "end"))
        for h, v in enumerate(rows[k]):
            x = lw + h * cw
            f = min(1.0, v / big)
            if v:
                out.append(f'<rect x="{x + .25:.2f}" y="{y + .25:.2f}" width="{cw - .5:.2f}" height="{ch - .5:.2f}" rx=".6" fill="{mc.INK}" fill-opacity="{.10 + .85 * f:.2f}"/>')
                out.append(t(x + cw / 2, y + ch / 2 + 1.1, v, 700, "#fff" if f > .45 else mc.INK, size=3.18))
            else:
                out.append(f'<rect x="{x + .25:.2f}" y="{y + .25:.2f}" width="{cw - .5:.2f}" height="{ch - .5:.2f}" rx=".6" fill="none" stroke="{mc.FILL2}" stroke-width=".3"/>')
        y += ch
    out.append(t(2, y + 5, "a member's row counts the commits that open with its name; below, releases and the rest", 400, mc.MUTED, "start"))
    svg = mc.svg(156, round(y + 7, 1), "".join(out), "The same day by member: each agent a row, each hour a column, darker where it did more")
    if re.search(r">[^<]*\bC\d{3}\b", svg):
        sys.exit("make_day: an id is drawn")
    (HERE / "day-by-member.svg").write_text(svg)
    print("written day-by-member.svg")


def main():
    for _, _, _, words in PHASES:
        if words not in CH:
            sys.exit(f"make_day: the chapter no longer says '{words}'")
    if "4 and 5 (hours one and two), 7 (three), 8 (four and five), 9 (six to thirteen" not in CH:
        sys.exit("make_day: the chapter's list of chapters beneath has changed")
    n = commits()
    x0, cw, base, top = 2.0, 8.0, 46.0, 28.0
    big = max(n)
    out = []
    for k, (name, a, b, _) in enumerate(PHASES):  # the phases, as bands over their hours
        x = x0 + (a - 1) * cw
        w = (b - a + 1) * cw
        out.append(f'<rect x="{x + .3:.2f}" y="2" width="{w - .6:.2f}" height="{base - 2:.2f}" rx="1.4" fill="{mc.FILL if k % 2 == 0 else "#fff"}" stroke="{mc.FILL2}" stroke-width=".35"/>'
                   + (t(x + w - 1, 12.5, name, 800, mc.ACCENT, "end") if k == 3 else t(x + w / 2, 7, name, 800)))
    for h in range(19):  # each hour's commits
        v = n[h]
        bh = top * v / big
        x = x0 + h * cw
        out.append(f'<rect x="{x + 1.6:.2f}" y="{base - bh:.2f}" width="{cw - 3.2:.2f}" height="{bh:.2f}" rx=".6" fill="{mc.ACCENT if h == 18 else mc.INK}"/>'
                   + t(x + cw / 2, base - bh - 1.2, v, 700, mc.MUTED))
        out.append(t(x + cw / 2, base + 4.4, h + 1, 700 if h in (0, 18) else 400))
    out.append(mc.line(x0, base, x0 + 19 * cw, base, mc.INK, .5))
    # the chapters beneath the hours they tell
    y = base + 9
    for c, a, b in CHAPTERS:
        x1, x2 = x0 + (a - 1) * cw + 1, x0 + b * cw - 1
        row = 1 if c in ("5", "12", "15") else 0
        yy = y + row * 6
        out.append(f'<path d="M{x1:.2f} {yy} h{x2 - x1:.2f}" stroke="{mc.FILL2}" stroke-width="1.6" stroke-linecap="round"/>'
                   + t((x1 + x2) / 2, yy + 4.4, f"ch. {c}", 700))
    out.append(t(x0, base + 25, "hours of the day, one to nineteen; above each, its commits; beneath, the chapter that tells it", 400, mc.MUTED, "start"))
    svg = mc.svg(156, round(base + 27, 1), "".join(out), "The talk's day at a glance: nineteen hours in four phases, each hour's commits, and the chapters of this book beneath the hours they tell")
    if re.search(r">[^<]*\bC\d{3}\b", svg):
        sys.exit("make_day: an id is drawn")
    (HERE / "day-at-a-glance.svg").write_text(svg)
    print("written day-at-a-glance.svg")
    heat()


if __name__ == "__main__":
    main()
