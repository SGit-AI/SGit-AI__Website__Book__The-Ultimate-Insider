#!/usr/bin/env python3
"""LAB 44: the covers for upload (the conductor's 059, the editor's brief 2026-11-04 09).

    python3 lab/experiments/44-designer-print-cover/make_print_cover.py [--pages 142] [--paper white]

KDP's full cover: back, spine and front as one PDF with 0.125 in bleed on every outside edge, its size worked out from
the page count with the publisher's own rule (publishing/cover_size.py, read only: KDP's spine per page, the bleed, spine
text from 79 pages). The front is cover A as signed (LAB 33's cover_signed), its four stripes carried into the bleed so a
trim that wanders shows no edge. The spine carries the title and the author inside KDP's spine margin (0.0625 in each
side). The back carries the book's description from publishing/listing.md (read only; traced by the researcher, cleared
by security), the series line and the nine heads, and leaves KDP's barcode area (2 x 1.2 in, 0.25 in from the spine and
the foot) empty: KDP prints its own white box there. No price, no contact detail, no number but the title's own.

Leanpub's cover: one 1800 x 2700 px image (2:3), cover A drawn taller (cover_signed(height)), nothing else changed.

The page count is today's (publishing/SETUP-SHEET.md: 141 interior pages, 142 printed, at 4 November, about 02:50 UTC; not final). At the
final count, run it again with --pages: only the spine's width and the cover's width move.
"""
import argparse, re, sys, textwrap
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
sys.path.insert(0, str(REPO / "lab" / "experiments" / "33-designer-cover-studies"))
sys.path.insert(0, str(REPO / "publishing"))
import make_cast as mc  # noqa: E402
import make_covers as cov  # noqa: E402
import cover_size  # noqa: E402

IN = 25.4
W, H = cov.W, cov.H                       # the trim, Crown Quarto, in mm
B = cover_size.BLEED * IN                 # 3.175 mm
TW_IN, TH_IN = 7.44, 9.69                 # the trim in inches, as cover_size.py takes it (Crown Quarto, P2)
TRW, TRH = TW_IN * IN, TH_IN * IN         # 188.976 x 246.126 mm; the art is drawn at 189 x 246.1 and fitted to it
SANS = cov.SANS
PAPERY, MUTED_D, ACCENT, GROUND = cov.PAPERY, cov.MUTED_D, cov.ACCENT, cov.GROUND


def tt(x, y, s, size, weight=700, fill=PAPERY, anchor="start", spacing=0, extra=""):
    return (f'<text x="{x:.2f}" y="{y:.2f}" {SANS} font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}" letter-spacing="{spacing}"{extra}>{escape(s, quote=False)}</text>')


def description():
    text = (REPO / "publishing" / "listing.md").read_text()
    m = re.search(r"^## Description\n\n(.+?)\n\n## ", text, re.S | re.M)
    if not m:
        sys.exit("make_print_cover: listing.md has no Description section")
    paras = [p.strip() for p in m.group(1).split("\n\n") if p.strip()]
    if not paras[0].startswith("For anyone with an idea") or not paras[-1].startswith("Part of the Gen ZX Founders"):
        sys.exit("make_print_cover: the description does not open and close as the back expects")
    for p in paras:
        if re.search(r"\$|@|https?:", p):
            sys.exit("make_print_cover: the description carries a price, an address or a link")
    return paras


def back():
    paras = description()
    out = [tt(14, 18, "GEN", 5.8, 800, MUTED_D, spacing=1.8), tt(32.8, 20.6, "ZX", 12, 800, PAPERY, spacing=.5),
           tt(52.6, 18, "FOUNDERS", 5.8, 800, MUTED_D, spacing=1.8)]
    y = 40.0
    for r in textwrap.wrap(paras[0], 34):
        out.append(tt(14, y, r, 8.2, 800, ACCENT))
        y += 10
    y += 3
    for p in paras[1:-1]:
        for r in textwrap.wrap(p, 74):
            out.append(tt(14, y, r, 4.3, 400))
            y += 6.1
        y += 3.4
    for r in textwrap.wrap(paras[-1], 74):
        out.append(tt(14, y, r, 4.3, 700, MUTED_D))
        y += 6.1
    if y > 196:
        sys.exit(f"make_print_cover: the description runs to {y:.0f} mm, into the heads")
    # the nine, heads only, left of the barcode area
    for k, m in enumerate(mc.CAST):
        out.append(f'<g transform="translate({14 + k * 12.4:.1f} 205) scale(.42)">{cov.dark(mc.head(m))}</g>')
    out.append(tt(14, 228, "the nine agents of the day", 4.3, 500, MUTED_D))
    out.append(tt(14, H - 8, "DINIS CRUZ", 6, 700, spacing=2))
    return "".join(out)


def barcode_box():
    """KDP's barcode area on the back, in back coordinates: 2 x 1.2 in, 0.25 in from the spine side and the foot."""
    w, h, m = 2 * IN, 1.2 * IN, .25 * IN
    return W - m - w, H - m - h, w, h


def spine(sw):
    margin = .0625 * IN
    size = min(3.6, (sw - 2 * margin) * .95)
    cx = sw / 2
    rot = f' transform="rotate(90 {cx:.2f} {{y}})"'
    title = "ONE HUMAN, NINE AGENTS, NINETEEN HOURS"
    y1, y2 = 16.0, H - 16.0
    out = [tt(cx, y1, title, size, 800, PAPERY, "start", .6, rot.replace("{y}", f"{y1:.2f}")).replace(
               f'y="{y1:.2f}"', f'y="{y1 + size * .36:.2f}"'),
           tt(cx, y2, "DINIS CRUZ", size, 700, MUTED_D, "end", .8, rot.replace("{y}", f"{y2:.2f}")).replace(
               f'y="{y2:.2f}"', f'y="{y2 + size * .36:.2f}"')]
    return out, size


def stripes_into_bleed(x0, y0):
    """Cover A's four stripes at the front's foot corner, continued into the bleed (same bands, x + y constant)."""
    out = []
    for i, c in enumerate(cov.SPECTRUM):
        c1, c2 = W - 46 + i * 7 + H, W - 40.5 + i * 7 + H
        pts = [(c1 - (H + B), H + B), (c2 - (H + B), H + B), (W + B, c2 - (W + B)), (W + B, c1 - (W + B))]
        out.append('<path d="M' + " L".join(f"{x0 + x:.2f} {y0 + y:.2f}" for x, y in pts) + f' z" fill="{c}"/>')
    return "".join(out)


def full_cover(pages, paper):
    if pages % 2:
        pages += 1
    sw = pages * cover_size.PER_PAGE[paper] * IN
    if pages < cover_size.SPINE_TEXT_FROM:
        sys.exit("make_print_cover: under 79 pages KDP allows no spine text; this cover carries some")
    TW, TH = 2 * B + 2 * TRW + sw, 2 * B + TRH
    front_x = B + TRW + sw
    inner = cov.cover_signed()
    inner = inner[inner.index(">") + 1:inner.rindex("</svg>")]
    sp, size = spine(sw)
    out = [f'<rect width="{TW:.3f}" height="{TH:.3f}" fill="{GROUND}"/>',
           f'<g transform="translate({B:.3f} {B:.3f})">{back()}</g>',
           f'<g transform="translate({B + TRW:.3f} {B:.3f})">{"".join(sp)}</g>',
           f'<svg x="{front_x:.3f}" y="{B:.3f}" width="{TRW:.3f}" height="{TRH:.3f}" viewBox="0 0 {W} {H}" preserveAspectRatio="none">{inner}</svg>',
           stripes_into_bleed(front_x, B)]
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{TW / IN:.3f}in" height="{TH / IN:.3f}in" '
           f'viewBox="0 0 {TW:.3f} {TH:.3f}" role="img" aria-label="The paperback cover laid flat: the back with the '
           f'book\'s description, the spine with the title and the author, and cover A on the front">' + "".join(out) + "</svg>\n")
    return svg, pages, sw, TW, TH, size


def guides(svg, sw, TW, TH):
    """The same cover with the trim, the spine folds, the safe area and the barcode area drawn on: for checking only."""
    bx, by, bw, bh = barcode_box()
    safe = .125 * IN
    g = (f'<g fill="none" stroke="#00b5e2" stroke-width=".35">'
         f'<rect x="{B}" y="{B}" width="{TW - 2 * B:.3f}" height="{TRH:.3f}"/>'
         f'<path d="M{B + TRW:.3f} 0 V{TH:.3f} M{B + TRW + sw:.3f} 0 V{TH:.3f}"/></g>'
         f'<g fill="none" stroke="#e2007a" stroke-width=".3" stroke-dasharray="2 1.5">'
         f'<rect x="{B + safe:.3f}" y="{B + safe:.3f}" width="{TRW - 2 * safe:.3f}" height="{TRH - 2 * safe:.3f}"/>'
         f'<rect x="{B + TRW + sw + safe:.3f}" y="{B + safe:.3f}" width="{TRW - 2 * safe:.3f}" height="{TRH - 2 * safe:.3f}"/></g>'
         f'<rect x="{B + bx:.3f}" y="{B + by:.3f}" width="{bw:.3f}" height="{bh:.3f}" fill="#fff" fill-opacity=".85"/>'
         f'<text x="{B + bx + bw / 2:.2f}" y="{B + by + bh / 2 + 1.5:.2f}" {SANS} font-size="4.3" font-weight="700" '
         f'fill="#15171c" text-anchor="middle">KDP barcode area</text>')
    return svg.replace("</svg>\n", g + "</svg>\n")


NODE = r"""
const { chromium } = require('playwright');
const [html, w, h, pdf, png, scale] = process.argv.slice(1);
(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: Math.round(w * 96), height: Math.round(h * 96) }, deviceScaleFactor: Number(scale) });
  await pg.goto('file://' + html);
  await pg.waitForTimeout(300);
  if (pdf !== '-') await pg.pdf({ path: pdf, preferCSSPageSize: true, printBackground: true,
                                  margin: { top: '0', right: '0', bottom: '0', left: '0' } });
  if (png !== '-') await pg.screenshot({ path: png, clip: { x: 0, y: 0, width: Math.round(w * 96), height: Math.round(h * 96) } });
  await b.close();
})();
"""


def render(svg_path, w_in, h_in, pdf=None, png=None, png_px=None):
    """Chromium through node's playwright (the lab's own renderer is node too): a PDF at the exact size, or a PNG."""
    import subprocess, tempfile
    html = (f'<!doctype html><html><head><meta charset="utf-8"><style>@page {{ size: {w_in:.3f}in {h_in:.3f}in; margin: 0 }}'
            f' html, body {{ margin: 0; padding: 0 }} svg {{ display: block; width: {w_in:.3f}in; height: {h_in:.3f}in }}</style>'
            f'</head><body>' + Path(svg_path).read_text() + "</body></html>")
    with tempfile.TemporaryDirectory() as d:
        hp = Path(d) / "cover.html"
        hp.write_text(html)
        scale = png_px / round(w_in * 96) if png_px else 1
        subprocess.run(["node", "-e", NODE, str(hp), f"{w_in:.3f}", f"{h_in:.3f}", str(pdf or "-"), str(png or "-"), f"{scale:.6f}"],
                       check=True)


def exact_box(pdf, w_in, h_in):
    """Chromium rounds a PDF's page to its own grid (here 15.430 x 9.943 in for 15.427 x 9.940); the art is drawn from
    the page's top left at the exact size, so the page box is set to the exact size over it: KDP checks the size."""
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import RectangleObject
    r = PdfReader(str(pdf))
    w = PdfWriter()
    for page in r.pages:
        top = float(page.mediabox.top)
        box = RectangleObject([0, round(top - h_in * 72, 3), round(w_in * 72, 3), top])
        page.mediabox = box
        page.cropbox = box
        page.trimbox = box
        page.bleedbox = box
        w.add_page(page)
    with open(pdf, "wb") as f:
        w.write(f)
    got = PdfReader(str(pdf)).pages[0].mediabox
    if abs(float(got.width) / 72 - w_in) > .0005 or abs(float(got.height) / 72 - h_in) > .0005:
        sys.exit(f"make_print_cover: the PDF is {float(got.width) / 72:.4f} x {float(got.height) / 72:.4f} in")


def main():
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--pages", type=int, default=142)
    a.add_argument("--paper", choices=sorted(cover_size.PER_PAGE), default="white")
    o = a.parse_args()
    svg, pages, sw, TW, TH, size = full_cover(o.pages, o.paper)
    name = f"kdp-full-cover-{pages}-{o.paper}"
    (HERE / f"{name}.svg").write_text(svg)
    (HERE / f"{name}-guides.svg").write_text(guides(svg, sw, TW, TH))
    w_in, h_in = TW / IN, TH / IN
    render(HERE / f"{name}.svg", w_in, h_in, pdf=HERE / f"{name}.pdf")
    exact_box(HERE / f"{name}.pdf", w_in, h_in)
    render(HERE / f"{name}-guides.svg", w_in, h_in, png=HERE / f"{name}-guides-preview.png", png_px=1800)
    tall = W * 1.5
    lean = cov.cover_signed(height=tall)
    (HERE / "leanpub-cover.svg").write_text(lean)
    render(HERE / "leanpub-cover.svg", W / IN, tall / IN, png=HERE / "leanpub-cover-1800x2700.png", png_px=1800)
    print(f"written {name}.pdf ({w_in:.3f} x {h_in:.3f} in; spine {sw / IN:.3f} in, text {size:.2f} mm), "
          f"{name}-guides-preview.png, leanpub-cover-1800x2700.png")


if __name__ == "__main__":
    main()
