#!/usr/bin/env python3
"""LAB 27's sheets: the nine as personas, their moods, a scorecard each, and the 'on stage now' marker.

    python3 lab/experiments/27-designer-the-cast/make_sheets.py
Draws from lab/characters/make_cast.py (one construction for every figure) and reads the scorecards' values from the
researcher's claims/scorecard-values.md at build time: no value is typed here. Every sheet is at most 164 mm wide
(the Crown Quarto text block), one SVG unit a millimetre, its size stated; all text 9 pt (3.18 mm). Hashes and
commit ids stay off the page (NR1); claim ids are printed small under each card.
"""
import re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

F = 3.18  # 9 pt
SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'


def t(x, y, s, weight=400, fill=mc.INK, anchor="start", size=F):
    return f'<text x="{x:.2f}" y="{y:.2f}" {SANS} font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'


def fig(m, mood, x, y, s):
    return f'<g transform="translate({x:.2f} {y:.2f}) scale({s})">{mc.figure(m, mood)}</g>'


def cast_sheet():
    cw, ch = 164 / 3, 57.0
    out = []
    for i, (m, (col, look, job)) in enumerate(mc.CAST.items()):
        x, y = (i % 3) * cw, (i // 3) * ch
        out.append(f'<rect x="{x + .6:.2f}" y="{y + .6:.2f}" width="{cw - 1.2:.2f}" height="{ch - 1.2:.2f}" rx="1.6" fill="#fff" stroke="{mc.FILL2}" stroke-width=".35"/>')
        out.append(f'<rect x="{x + .6:.2f}" y="{y + .6:.2f}" width="{cw - 1.2:.2f}" height="1.6" fill="{col}"/>')
        out.append(fig(m, "happy", x + cw / 2 - 16, y + 2.2, .8))
        out.append(t(x + cw / 2, y + 46.4, m, 800, anchor="middle"))
        words, row, rows = look.split(), "", []
        for w in words:  # wrap the look at about 28 characters
            if len(row) + len(w) + 1 > 28:
                rows.append(row)
                row = w
            else:
                row = (row + " " + w).strip()
        rows.append(row)
        for j, r in enumerate(rows[:2]):
            out.append(t(x + cw / 2, y + 50.3 + j * 3.8, r, fill=mc.MUTED, anchor="middle"))
    return mc.svg(164, 3 * ch, "".join(out), "The talk's nine agents as personas, each with one colour, one thing on the head and one in the hand")


def mood_sheet():
    name_w, col_w, row_h, top = 26.0, 34.5, 18.6, 6.0
    out = [t(name_w + col_w * (k + .5), 3.6, mood, 800, anchor="middle") for k, mood in enumerate(mc.MOODS)]
    for i, m in enumerate(mc.CAST):
        y = top + i * row_h
        if i % 2 == 0:
            out.append(f'<rect x="0" y="{y:.2f}" width="164" height="{row_h:.2f}" fill="{mc.FILL}"/>')
        out.append(t(1.5, y + row_h / 2 + 1.1, m, 800))
        for k, mood in enumerate(mc.MOODS):
            out.append(fig(m, mood, name_w + col_w * (k + .5) - 7.2, y + .3, .36))
    return mc.svg(164, round(top + len(mc.CAST) * row_h, 2), "".join(out),
                  "Each of the nine in four moods: happy, worried, stressed, unhappy (the book's reading, not the record's)")


def scorecard_rows():
    """The researcher's table, read as it stands: member -> (first commit time, commits, wake records, slot, policy)."""
    rows = {}
    for line_ in (REPO / "claims" / "scorecard-values.md").read_text().splitlines():
        cells = [c.strip() for c in line_.strip().strip("|").split("|")]
        if len(cells) == 7 and cells[0] in mc.CAST:
            rows[cells[0]] = (cells[1].split()[0], cells[3], cells[4], cells[5], cells[6])
    missing = [m for m in mc.CAST if m not in rows]
    if missing:
        sys.exit(f"make_sheets: no register row for {missing}: a card is not drawn without its values")
    return rows


AT_PREFIX = {"conductor": "99", "dev": "52"}  # C095, as the researcher's note says to print which basis


def card(m, vals, x, y, w=52.0, h=53.0):
    col = mc.CAST[m][0]
    first, commits, wakes, slot, policy = vals
    out = [f'<rect x="{x:.2f}" y="{y:.2f}" width="{w}" height="{h}" rx="2.2" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>',
           f'<rect x="{x:.2f}" y="{y:.2f}" width="{w}" height="15" rx="2.2" fill="{col}"/>',
           f'<rect x="{x:.2f}" y="{y + 12:.2f}" width="{w}" height="3" fill="{col}"/>',
           f'<rect x="{x + 1.6:.2f}" y="{y + 1.4:.2f}" width="12.4" height="12.2" rx="1.6" fill="#fff"/>',
           f'<g transform="translate({x + 1.4:.2f} {y + 1.3:.2f}) scale(.32)">{mc.head(m)}</g>',
           t(x + 16, y + 9.4, m, 800, fill="#fff")]
    stats = [("first commit", first), ("commits", commits + ("*" if m in AT_PREFIX else "")), ("wake records", wakes),
             ("hourly slot", slot), ("policy at the end", policy)]
    for j, (k, v) in enumerate(stats):
        yy = y + 21.2 + j * 5.2
        out.append(t(x + 2.4, yy, k, fill=mc.MUTED))
        out.append(t(x + w - 2.4, yy, v, 800, anchor="end"))
        if j < len(stats) - 1:
            out.append(mc.line(x + 2.4, yy + 1.8, x + w - 2.4, yy + 1.8, mc.FILL2, .25))
    note = f"* by @ prefix: {AT_PREFIX[m]} (C095)" if m in AT_PREFIX else ""
    if note:
        out.append(t(x + 2.4, y + h - 6.6, note, fill=mc.MUTED))
    out.append(t(x + 2.4, y + h - 2.6, "C011 C014 C022 C071 C072", fill=mc.MUTED))
    return "".join(out)


def scorecards():
    rows = scorecard_rows()
    w, h, gap = 52.0, 53.0, 4.0
    out = [card(m, rows[m], (i % 3) * (w + gap), (i // 3) * (h + gap), w, h) for i, m in enumerate(mc.CAST)]
    return mc.svg(164, 3 * h + 2 * gap, "".join(out), "A scorecard for each of the nine, every value from the book's register")


def first_commits():
    rows = scorecard_rows()
    return {m: rows[m][0] for m in mc.CAST}


if __name__ == "__main__":
    (HERE / "sheet-cast.svg").write_text(cast_sheet())
    (HERE / "sheet-moods.svg").write_text(mood_sheet())
    (HERE / "sheet-scorecards.svg").write_text(scorecards())
    firsts = first_commits()
    for label, at in (("0050", "00:50"), ("0200", "02:00"), ("1200", "12:00"), ("1600", "16:00")):
        present = {m for m, f in firsts.items() if f <= at}  # on stage from its first commit (C011)
        (HERE / f"on-stage-{label}.svg").write_text(mc.on_stage(present, 9.0))
    print("written sheet-cast.svg, sheet-moods.svg, sheet-scorecards.svg, on-stage-*.svg")
