#!/usr/bin/env python3
"""LAB 77: the full cover at A4 for a London print shop (the editor, 5 November 2026, brief 52).

    python3 lab/experiments/77-a4-print/make_a4_cover.py --pages 116 [--spine-mm 6.5]

The same cover as LAB 44 (cover A on the front, the description and the nine on the back, the title and the author on the
spine), laid flat at A4: back + spine + front, 210 x 297 mm each side, 3 mm bleed on every outside edge. The front is
cover A drawn taller (cover_signed(height)) to A4's shape and enlarged by 210/189, so nothing is stretched; the back is
the same back enlarged, its author line at the foot; the spine is drawn at its real width. No barcode, no price, no
contact detail. The spine width is the shop's to give for its paper: by default KDP's white-paper rule per page.
"""
import argparse, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "experiments" / "44-designer-print-cover"))
import make_print_cover as mp  # noqa: E402

IN = 25.4
A4W, A4H = 210.0, 297.0
B = 3.0                                   # mm of bleed, the shops' usual
S = A4W / mp.W                            # 210 / 189: the Crown Quarto drawing enlarged to A4's width
DH = A4H / S                              # the drawing's height in its own units at A4's shape (267.3)


def a4_cover(pages, spine_mm):
    sw = spine_mm if spine_mm else pages * mp.cover_size.PER_PAGE["white"] * IN
    TW, TH = 2 * B + 2 * A4W + sw, 2 * B + A4H
    W0, H0 = mp.W, mp.H
    try:
        mp.H = DH                          # the back's author line at the A4 foot, the stripes to the A4 corner
        back = mp.back()
        inner = mp.cov.cover_signed(height=DH)
        inner = inner[inner.index(">") + 1:inner.rindex("</svg>")]
        stripes = mp.stripes_into_bleed(0, 0)
        mp.H = A4H                         # the spine is drawn at its real size, in mm
        sp, size = mp.spine(sw)
    finally:
        mp.W, mp.H = W0, H0
    front_x = B + A4W + sw
    out = [f'<rect width="{TW:.3f}" height="{TH:.3f}" fill="{mp.GROUND}"/>',
           f'<g transform="translate({B:.3f} {B:.3f}) scale({S:.5f})">{back}</g>',
           f'<g transform="translate({B + A4W:.3f} {B:.3f})">{"".join(sp)}</g>',
           f'<g transform="translate({front_x:.3f} {B:.3f}) scale({S:.5f})">'
           f'<svg x="0" y="0" width="{mp.W}" height="{DH:.3f}" viewBox="0 0 {mp.W} {DH:.3f}" overflow="visible">{inner}</svg>'
           f'{stripes}</g>']
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{TW:.3f}mm" height="{TH:.3f}mm" viewBox="0 0 {TW:.3f} {TH:.3f}" '
           f'role="img" aria-label="The A4 paperback cover laid flat: the back with the book\'s description, the spine with '
           f'the title and the author, and cover A on the front">' + "".join(out) + "</svg>\n")
    return svg, sw, TW, TH, size


def main():
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--pages", type=int, required=True)
    a.add_argument("--spine-mm", type=float, default=0, help="the shop's spine width for its paper; default KDP white")
    o = a.parse_args()
    svg, sw, TW, TH, size = a4_cover(o.pages, o.spine_mm)
    (HERE / "a4-full-cover.svg").write_text(svg)
    w_in, h_in = TW / IN, TH / IN
    mp.render(HERE / "a4-full-cover.svg", w_in, h_in, pdf=HERE / "a4-full-cover.pdf")
    mp.exact_box(HERE / "a4-full-cover.pdf", w_in, h_in)
    mp.render(HERE / "a4-full-cover.svg", w_in, h_in, png=HERE / "a4-full-cover-preview.png", png_px=1600)
    print(f"written a4-full-cover.pdf ({TW:.1f} x {TH:.1f} mm; spine {sw:.2f} mm for {o.pages} pages; spine text {size:.2f} mm)")


if __name__ == "__main__":
    main()
