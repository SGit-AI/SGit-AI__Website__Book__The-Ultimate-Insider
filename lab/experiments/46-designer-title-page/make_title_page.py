#!/usr/bin/env python3
"""LAB 46: the title page's drawing (the conductor's 056, item 2; the editor, brief 2026-11-04 03: the title page "feels
quite empty ... a couple of agents, a couple of things, just make it a bit more fun, and maybe give a little preview").

    python3 lab/experiments/46-designer-title-page/make_title_page.py

Two of the cast either side of one line of preview: the book's teaser from publishing/listing.md (read only; traced by
the researcher, cleared by security), set as a note the two have just read. The conductor (the stopwatch, calm) and dev
(the hard hat, fast) are the first two on stage. Drawn 155 mm wide, the full book's text width (publisher 041), to sit
under the title; the publisher's build places it (conductor 067 to it). No number but the teaser's own words.
"""
import re, sys, textwrap
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'
SERIF = 'font-family="Bitstream Charter, Charter, DejaVu Serif, Georgia, serif"'


def teaser():
    text = (REPO / "publishing" / "listing.md").read_text()
    m = re.search(r"^## Teaser\n\n(.+?)\n", text, re.M)
    if not m or not m.group(1).startswith("One person, nine AI agents and one day"):
        sys.exit("make_title_page: listing.md's teaser is not as the page expects")
    return m.group(1).strip()


def t(x, y, s, size=3.18, weight=400, fill=mc.INK, anchor="start", font=SANS, style=""):
    return (f'<text x="{x:.2f}" y="{y:.2f}" {font} font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}"{style}>{escape(s, quote=False)}</text>')


def page():
    W, H = 155, 62
    out = []
    # the note between them: a card with a folded corner, the teaser in the book's own serif
    nx, ny, nw, nh = 47, 6, 61, 44
    out.append(f'<path d="M{nx} {ny} h{nw - 7} l7 7 v{nh - 7} h-{nw} z" fill="#fff" stroke="{mc.INK}" stroke-width=".5"/>'
               f'<path d="M{nx + nw - 7} {ny} v7 h7" fill="none" stroke="{mc.INK}" stroke-width=".4"/>')
    out.append(t(nx + 5, ny + 7.5, "IN THIS BOOK", 3.18, 800, mc.ACCENT))
    rows = textwrap.wrap(teaser(), 27)
    for j, r in enumerate(rows):
        out.append(t(nx + 5, ny + 14 + j * 4.9, r, 3.5, 400, mc.INK, font=SERIF, style=' font-style="italic"'))
    if 14 + len(rows) * 4.9 > nh:
        sys.exit("make_title_page: the teaser runs out of its note")
    # the two, turned in to the note: the conductor on the left, dev on the right
    out.append(f'<g transform="translate(2 4) scale(1.05)">{mc.figure("conductor")}</g>')
    out.append(f'<g transform="translate(153 4) scale(-1.05 1.05)">{mc.figure("dev")}</g>')
    out.append(t(23, 60, "conductor", 3.18, 700, mc.MUTED, "middle") + t(132, 60, "dev", 3.18, 700, mc.MUTED, "middle"))
    return mc.svg(W, H, "".join(out), "Two of the cast, the conductor and dev, either side of a note: " + teaser())


if __name__ == "__main__":
    (HERE / "title-page.svg").write_text(page())
    print("written title-page.svg")
