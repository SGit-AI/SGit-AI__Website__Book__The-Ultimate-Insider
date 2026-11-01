#!/usr/bin/env python3
"""LAB 32's sheets: six options of the editor as the narrator (DR1), and his card.

    python3 lab/experiments/32-designer-the-narrator/make_sheets.py
The figures come from lab/characters/make_cast.py (editor_figure: the cast's construction, a neutral head, no likeness).
The card's values are read from claims/register.json when the sheet is built (C003, C087, C069): none typed here.
164 mm wide, one SVG unit a millimetre, size stated, text 9 pt.
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
sys.path.insert(0, str(REPO / "lab" / "experiments" / "27-designer-the-cast"))
import make_cast as mc  # noqa: E402
from make_sheets import t  # noqa: E402  (LAB 27's 9 pt text)


def wrap(s, n):
    rows, row = [], ""
    for w in s.split():
        if row and len(row) + len(w) + 1 > n:
            rows.append(row); row = w
        else:
            row = (row + " " + w).strip()
    return rows + [row]


def options_sheet():
    cw, ch = 164 / 3, 74.0
    out = []
    for i, (opt, (shows, src)) in enumerate(mc.EDITOR_OPTIONS.items()):
        x, y = (i % 3) * cw, (i // 3) * ch
        out.append(f'<rect x="{x + .6:.2f}" y="{y + .6:.2f}" width="{cw - 1.2:.2f}" height="{ch - 1.2:.2f}" rx="1.6" fill="#fff" stroke="{mc.FILL2}" stroke-width=".35"/>')
        out.append(f'<rect x="{x + .6:.2f}" y="{y + .6:.2f}" width="{cw - 1.2:.2f}" height="1.6" fill="{mc.EDITOR}"/>')
        out.append(f'<g transform="translate({x + cw / 2 - 16:.2f} {y + 3:.2f}) scale(.8)">{mc.editor_figure(opt)}</g>')
        out.append(t(x + cw / 2, y + 47.4, f"option {opt}", 800, anchor="middle"))
        for j, r in enumerate(wrap(shows, 27)[:2]):
            out.append(t(x + cw / 2, y + 51.6 + j * 3.9, r, anchor="middle"))
        for j, r in enumerate(wrap(src, 28)[:3]):
            out.append(t(x + cw / 2, y + 60 + j * 3.9, r, fill=mc.MUTED, anchor="middle"))
    return mc.svg(164, 2 * ch, "".join(out), "Six options of the editor as the narrator, in the cast's style, for him to pick one")


def card():
    reg = json.loads((REPO / "claims" / "register.json").read_text())
    c = {x["id"]: x["value"] for x in (reg["claims"] if isinstance(reg, dict) else reg)}
    rows = [("commits in the record", str(c["C003"]["Dinis Cruz"]), "C003"),
            ("wakes he started", str(c["C087"]["editor"]), "C087"),
            ("passages he spoke", f'{c["C069"]["by"]["editor"]} of {c["C069"]["passages"]}', "C069")]
    w, h = 52.0, 46.0
    out = [f'<rect x="0" y="0" width="{w}" height="{h}" rx="2.2" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>',
           f'<rect x="0" y="0" width="{w}" height="15" rx="2.2" fill="{mc.EDITOR}"/>', f'<rect x="0" y="12" width="{w}" height="3" fill="{mc.EDITOR}"/>',
           t(3, 9.4, "the editor, the narrator", 800, fill="#fff")]
    for j, (k, v, cid) in enumerate(rows):
        yy = 21.4 + j * 5.4
        out.append(t(2.4, yy, k, fill=mc.MUTED))
        out.append(t(w - 2.4, yy, v, 800, anchor="end"))
        out.append(mc.line(2.4, yy + 1.8, w - 2.4, yy + 1.8, mc.FILL2, .25))
    out.append(t(2.4, h - 7, "his head: the option he picks", fill=mc.MUTED))
    out.append(t(2.4, h - 2.6, " ".join(r[2] for r in rows), fill=mc.MUTED))
    return mc.svg(w, h, "".join(out), "The narrator's card: his values from the book's register")


if __name__ == "__main__":
    (HERE / "options.svg").write_text(options_sheet())
    (HERE / "card.svg").write_text(card())
    print("written options.svg, card.svg")
