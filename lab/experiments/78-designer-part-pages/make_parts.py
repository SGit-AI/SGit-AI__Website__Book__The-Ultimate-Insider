#!/usr/bin/env python3
"""LAB 78: the five part pages (PEN1 note 16; the storyteller's 169, the publisher's 064). Each opens its part as a
placed page the size of the text block (156 by 200 mm), as the opening spread is, and carries only what the storyteller
set: "Part one" to "Part five" in words (style sheet rule 13), the part's name, and the one line the spread's list
gives it. Nothing else: no cast bar, no figure, no id.

    python3 lab/experiments/78-designer-part-pages/make_parts.py

Every word is read at build from manuscript/rc2/150/00-start-here.md ("The story, in five parts"), never edited.
Writes part-1.svg to part-5.svg.
"""
import re, sys, textwrap
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'
SERIF = 'font-family="Georgia, \'DejaVu Serif\', serif"'
SRC = (REPO / "manuscript" / "rc2" / "150" / "00-start-here.md").read_text()
W, H, PT = 156.0, 200.0, 0.3528
WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}


def t(x, y, s, weight=400, fill=mc.INK, size=3.18, fam=SANS, spacing=0):
    ls = f' letter-spacing="{spacing}"' if spacing else ""
    return (f'<text x="{x:.2f}" y="{y:.2f}" {fam} font-size="{size:.2f}" font-weight="{weight}" fill="{fill}"{ls}>'
            f'{escape(str(s), quote=False)}</text>')


def parts():
    out = []
    for l in SRC.splitlines():
        m = re.match(r"^(\d)\. \*\*([^*]+)\*\* (.+)$", l)
        if m:
            out.append((int(m.group(1)), m.group(2).rstrip("."), m.group(3)))
    if [p[0] for p in out] != [1, 2, 3, 4, 5]:
        sys.exit("make_parts: 00 no longer lists the five parts as the part pages expect")
    return out


def page(n, name, line):
    y0 = 62.0  # a third of the way down, where a part opens
    out = [f'<rect x="0" y="{y0 - 14:.2f}" width="18" height="1.6" fill="{mc.ACCENT}"/>',
           t(0, y0, f"Part {WORDS[n]}", 700, mc.ACCENT, size=14 * PT, spacing=.3)]
    y = y0 + 13
    for r in textwrap.wrap(name, 26):
        out.append(t(0, y, r, 800, mc.INK, size=26 * PT)); y += 26 * PT * 1.15
    y += 4
    for r in textwrap.wrap(line, 62):
        out.append(t(0, y, r, 400, mc.MUTED, size=12 * PT, fam=SERIF)); y += 12 * PT * 1.45
    if y > H:
        sys.exit(f"make_parts: part {n} runs past the page")
    return mc.svg(W, H, "".join(out), f"Part {WORDS[n]}: {name}. {line}")


def main():
    for n, name, line in parts():
        svg = page(n, name, line)
        if re.search(r">[^<]*\b(C\d{3}|[0-9a-f]{7,})\b", svg) or "@" in re.sub(r"<[^>]+>", "", svg):
            sys.exit("make_parts: an id, a hash or an address is drawn")
        (HERE / f"part-{n}.svg").write_text(svg)
    print("written part-1.svg to part-5.svg")


if __name__ == "__main__":
    main()
