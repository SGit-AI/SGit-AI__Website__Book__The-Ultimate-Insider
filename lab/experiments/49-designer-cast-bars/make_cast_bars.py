#!/usr/bin/env python3
"""LAB 49: the cast bar drawn, one row per chapter of the full book (principle 17; the storyteller's convention 6; the
critics' notes routed by the conductor, 075 and 076; the publisher places them, its 046 and 054).

    python3 lab/experiments/49-designer-cast-bars/make_cast_bars.py

Each row: the editor (the narrator's round head, the book's neutral figure), the nine in the order they arrived (C011, the
researcher's table, as LAB 37 reads it), and security's empty chair, dashed. Lit or greyed as the chapter's own
"**Cast bar:**" line says: that line was read by hand into STATE below, and the build checks every chapter in the full
book's list has a line and an entry. 19 to 23 draw what their lines describe: this book's team, the second team in
outline, three people in outline, the reader's own empty row. No caption drawn in (convention 8): the line stays the
words. Writes cast-bar-<chapter>.svg here and the map lab/tools/book/cast-bars.json for the publisher.
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

BOOK = REPO / "manuscript" / "editions" / "rc2-150" / "Book.txt"
ALL9 = set(mc.CAST)
FIRST6 = {"dev", "conductor", "deck", "ruv-sgit", "researcher", "designer"}
# chapter: (the editor: "lit", "grey" or None; the agents lit; the chair: True when drawn), from each chapter's line
STATE = {
    "01": ("lit", set(), False), "02": ("lit", set(), False), "03": (None, set(), False),
    "04": ("lit", {"dev", "conductor", "deck"}, True),
    "05": ("lit", {"dev", "conductor", "deck", "ruv-sgit", "researcher"}, True),
    "06": (None, FIRST6 - {"designer"}, True),  # the designer greyed, arriving in chapter 8 (storyteller 138, writer 213)
    "07": ("lit", {"dev", "conductor", "deck", "ruv-sgit", "researcher"}, True),
    "08": ("lit", FIRST6, True), "09": ("grey", FIRST6, True), "10": ("grey", FIRST6, True),
    "11": ("lit", ALL9, True), "12": ("lit", FIRST6 | {"storyteller"}, True), "13": ("lit", FIRST6 | {"storyteller"}, True),
    "14": ("lit", ALL9, True), "15": ("lit", ALL9, True), "16": ("lit", ALL9, True), "17": ("lit", ALL9, True),
    "18": ("lit", ALL9, True), "90": (None, set(), False),
}
SPECIAL = {"19", "20", "21", "22", "23"}


def order():
    out = {}
    for line in (REPO / "claims" / "scorecard-values.md").read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 7 and cells[0] in mc.CAST:
            out[cells[0]] = cells[1].split()[0]
    if set(out) != ALL9:
        sys.exit("make_cast_bars: the researcher's table does not give all nine first commits")
    return sorted(out, key=lambda m: out[m])


S, STEP = .42, 10.4  # a head 8.4 mm wide; one slot


def grey(body):
    return f'<g filter="url(#cb-grey)" opacity=".42">{body}</g>'


def editor_head(lit):
    body = (f'<circle cx="20" cy="17" r="8.6" fill="{mc.FILL}" stroke="{mc.INK}" stroke-width="{mc.SW * 1.6}"/>'
            + (f'<g transform="translate(0 -.8)">{mc.face("happy")}</g>' if lit else ""))
    return body if lit else body.replace(f'stroke="{mc.INK}"', f'stroke="{mc.FILL2}"')


def slot(i, body):
    return f'<g transform="translate({i * STEP - 10 * S:.2f} {-4 * S:.2f}) scale({S})">{body}</g>'


def chair(x):
    return (f'<g transform="translate({x:.2f} .6) scale(.5)" fill="none" stroke="{mc.MUTED}" stroke-width="1.1" '
            f'stroke-dasharray="1.8 1.2"><path d="M4 2 V18 M4 11 H14 V18 M4 2 H7"/></g>')


def outline(i):
    return slot(i, f'<rect x="10" y="10" width="20" height="16" rx="3.2" fill="none" stroke="{mc.FILL2}" stroke-width="1" stroke-dasharray="2 1.4"/>')


def row(ch, seq):
    defs = '<defs><filter id="cb-grey"><feColorMatrix type="saturate" values="0"/></filter></defs>'
    out, i = [], 0
    if ch in STATE:
        ed, lit, ch_ = STATE[ch]
        if ed:
            out.append(slot(0, editor_head(ed == "lit")))
            i = 1.35
        for k, m in enumerate(seq):
            body = mc.head(m, True)
            out.append(slot(i + k, body if m in lit else grey(body)))
        i += len(seq)
        if ch_:
            out.append(chair((i + .15) * STEP - 10 * S + 1.2))
            i += 1
        label = f"chapter {ch}: " + (", ".join(m for m in seq if m in lit) or "nobody lit yet")
    elif ch in ("19", "20", "21"):
        team = list(mc.BOOK_TEAM)
        out.append(slot(0, editor_head(True)))
        for k, m in enumerate(team):
            out.append(slot(1.35 + k, mc.head(m, True)))
        i = 1.35 + len(team)
        if ch == "19":  # one arrow, then the second team in outline
            x = i * STEP
            out.append(f'<path d="M{x - 2:.2f} 4.6 h7" stroke="{mc.INK}" stroke-width=".5"/><path d="M{x + 5.4:.2f} 4.6 l-2 -1.3 v2.6 z" fill="{mc.INK}"/>')
            i += 1
            for k in range(5):
                out.append(outline(i + k))
            i += 5
        label = f"chapter {ch}: this book's team, security at the table" + (", and the second team in outline" if ch == "19" else "")
    elif ch == "22":
        for k in range(3):
            out.append(slot(k * 1.4, editor_head(False)))
        i = 3 * 1.4
        label = "chapter 22: three people in outline, nothing lit"
    else:  # 23
        out.append(outline(0))
        i = 1
        label = "chapter 23: yours, empty for now"
    w = round(max(i, 1) * STEP, 2)
    return mc.svg(w, round(23 * S, 2), defs + "".join(out), "Cast bar, " + label)


def main():
    seq = order()
    chapters = [Path(l.strip()).name for l in BOOK.read_text().splitlines() if l.strip() and not l.startswith("#")]
    mapping = {}
    for name in chapters:
        text = (BOOK.parent / "../../rc2/150" / name).resolve().read_text()
        if not re.search(r"^\*\*Cast bar:\*\*", text, re.M):
            continue
        ch = name[:2]
        if ch not in STATE and ch not in SPECIAL:
            sys.exit(f"make_cast_bars: {name} has a cast bar line and no entry in STATE")
        out = HERE / f"cast-bar-{name[:-3]}.svg"
        out.write_text(row(ch, seq))
        mapping[f"rc2/150/{name}"] = str(out.relative_to(REPO))
    (REPO / "lab" / "tools" / "book" / "cast-bars.json").write_text(json.dumps(
        {"about": "The drawn cast bar per chapter of the full book, by the designer (LAB 49): the publisher places each in place of the chapter's '**Cast bar:**' line or beside it; the line stays the words. Built by lab/experiments/49-designer-cast-bars/make_cast_bars.py.",
         "bars": mapping}, indent=1) + "\n")
    print(f"written {len(mapping)} cast bars and lab/tools/book/cast-bars.json")


if __name__ == "__main__":
    main()
