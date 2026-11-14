#!/usr/bin/env python3
"""PEN1 note 9: the chapter's own progress bar, under the book's bar in the footer.

The build's running footer (publishing/build_book.py, running_footer) draws the book's bar in CSS and says progress
within a chapter cannot be drawn: Chromium has no per-chapter page counter. Once the PDF is laid out, though, every
page's place in its chapter is known. This tool stamps that second bar after layout, from the build's own
<name>-chapters.json (each chapter's exact first page), so nothing is guessed from titles.

    python3 lab/tools/book/chapter_bar.py <built.pdf> <name-chapters.json> <out.pdf> [--check]

It draws only two thin rectangles per page (a track and its fill), no text, so every text check on the PDF reads
the same before and after. A page is stamped only if it already prints that chapter's title (the running footer's
label, or the chapter's own heading on its first page), so placed pages, part pages, the index and blank pages are left alone. The bar sits under the
book's bar, at its width, centred on the text block of a right or a left page as the CSS centres it.
--check prints the pages it would stamp and writes nothing.
"""
import io, json, subprocess, sys

from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas

IN = 72.0
BAR_W = 1.1 * IN          # the book bar's width (running_footer: width 1.1in)
BOOK_Y = 0.3125 * IN      # the book bar's centre: the middle of the 0.625in bottom margin (publishing/book.css)
GAP, H = 3.2, 1.6         # pt: the chapter bar sits 3.2 pt under the book bar, as thick (1.6 pt)
MARGINS = {"right": (0.65 * IN, 0.5 * IN), "left": (0.5 * IN, 0.65 * IN)}  # publishing/full-book.css
TRACK, FILL = (0xEC / 255, 0xC6 / 255, 0xB3 / 255), (0xB0 / 255, 0x48 / 255, 0x1A / 255)  # the lab's accent tints


def page_texts(pdf):
    """Each page's text, whitespace folded (pdftotext, one call for the whole PDF)."""
    out = subprocess.run(["pdftotext", pdf, "-"], capture_output=True, text=True).stdout
    return [" ".join(p.split()) for p in out.split("\f")]


def plan(pdf, chapters, total):
    """{page: fraction} for every page whose footer names its chapter."""
    chs = sorted(chapters, key=lambda c: c["page"])
    texts = page_texts(pdf)
    out = {}
    for i, c in enumerate(chs):
        first = c["page"]
        last = (chs[i + 1]["page"] - 1) if i + 1 < len(chs) else total
        n = last - first + 1
        key = " ".join(c["title"].split())[:18]  # the footer label may wrap after this; 18 characters stay on its first line
        for p in range(first, last + 1):
            if key and p <= len(texts) and key in texts[p - 1]:
                out[p] = (p - first + 1) / n
    return out


def stamp(w, h, page_no, frac):
    side = "right" if page_no % 2 else "left"
    ml, mr = MARGINS[side]
    cx = ml + (w - ml - mr) / 2
    x, y = cx - BAR_W / 2, BOOK_Y - H / 2 - GAP - H
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(w, h))
    c.setFillColorRGB(*TRACK); c.rect(x, y, BAR_W, H, stroke=0, fill=1)
    c.setFillColorRGB(*FILL); c.rect(x, y, BAR_W * frac, H, stroke=0, fill=1)
    c.save()
    return PdfReader(io.BytesIO(buf.getvalue())).pages[0]


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    src, cj, dst = sys.argv[1:4]
    chapters = json.load(open(cj, encoding="utf-8"))["chapters"]
    reader = PdfReader(src)
    todo = plan(src, chapters, len(reader.pages))
    if "--check" in sys.argv:
        print(f"chapter_bar: {len(todo)} of {len(reader.pages)} pages would carry the chapter bar")
        return
    writer = PdfWriter()
    for i, page in enumerate(reader.pages, 1):
        if i in todo:
            box = page.mediabox
            page.merge_page(stamp(float(box.width), float(box.height), i, todo[i]))
        writer.add_page(page)
    with open(dst, "wb") as f:
        writer.write(f)
    print(f"chapter_bar: {len(todo)} of {len(reader.pages)} pages stamped, written {dst}")


if __name__ == "__main__":
    main()
