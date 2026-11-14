"""PEN1 note 9: the chapter's own progress bar, under the book's bar in the running footer.

Release code, brought from the designer's lab/tools/book/chapter_bar.py at security's word (security 026): Chromium's
page CSS has no per-chapter page counter, so once the PDF is laid out, each page's place in its chapter is read from
the build's own <name>-chapters.json and a thin bar is stamped under the book's bar. Two filled rectangles per page,
no text, so every text check on the PDF reads the same before and after. A page in a chapter's range is stamped only
if its footer (its last two lines of text) names that chapter or its part, as running_footer sets them (the chapter's
title on right pages, the part's name on left pages): placed pages, part pages, the index and blank pages are left
alone. No network; pdftotext is called with a list of arguments, never a shell.

    stamp_pdf(pdf, chapters) -> (pages stamped, pages in the PDF)   # rewrites pdf through a temp file
"""
import io
import os
import subprocess
import tempfile

from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas

IN = 72.0
BAR_W = 1.1 * IN          # the book bar's width (build_book.running_footer: width 1.1in)
BOOK_Y = 0.3125 * IN      # the book bar's centre: the middle of the 0.625 in bottom margin (publishing/book.css)
GAP, H = 3.2, 1.6         # pt: the chapter bar sits 3.2 pt under the book bar, as thick (1.6 pt)
MARGINS = {"right": (0.65 * IN, 0.5 * IN), "left": (0.5 * IN, 0.65 * IN)}  # publishing/full-book.css
TRACK, FILL = (0xEC / 255, 0xC6 / 255, 0xB3 / 255), (0xB0 / 255, 0x48 / 255, 0x1A / 255)  # the designer's accent tints


def footers(pdf):
    """Each page's last two lines of text, whitespace folded: the running footer's label and the page number."""
    out = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True, check=True).stdout
    pages = []
    for page in out.split("\f"):
        lines = [" ".join(l.split()) for l in page.split("\n") if l.strip()]
        pages.append(" ".join(lines[-2:]))
    return pages


def plan(pdf, chapters, total):
    """{page: fraction of its chapter} for every page whose footer names its chapter or its part."""
    chs = sorted((c for c in chapters if c.get("page")), key=lambda c: c["page"])
    feet = footers(pdf)
    out = {}
    for i, c in enumerate(chs):
        first = c["page"]
        last = (chs[i + 1]["page"] - 1) if i + 1 < len(chs) else total
        n = last - first + 1
        keys = {" ".join(s.split())[:18] for s in (c["title"], c.get("part") or "") if s and s.strip()}
        for p in range(first, last + 1):
            if p <= len(feet) and any(k in feet[p - 1] for k in keys):
                out[p] = (p - first + 1) / n
    return out


def bar(w, h, page_no, frac):
    side = "right" if page_no % 2 else "left"
    ml, mr = MARGINS[side]
    cx = ml + (w - ml - mr) / 2
    x, y = cx - BAR_W / 2, BOOK_Y - H / 2 - GAP - H
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(w, h))
    c.setFillColorRGB(*TRACK)
    c.rect(x, y, BAR_W, H, stroke=0, fill=1)
    c.setFillColorRGB(*FILL)
    c.rect(x, y, BAR_W * frac, H, stroke=0, fill=1)
    c.save()
    return PdfReader(io.BytesIO(buf.getvalue())).pages[0]


def stamp_pdf(pdf, chapters):
    """Stamp the chapter bars into pdf, through a temp file in the same folder replaced only once it is written."""
    reader = PdfReader(pdf)
    todo = plan(pdf, chapters, len(reader.pages))
    writer = PdfWriter()
    for i, page in enumerate(reader.pages, 1):
        if i in todo:
            box = page.mediabox
            page.merge_page(bar(float(box.width), float(box.height), i, todo[i]))
        writer.add_page(page)
    fd, tmp = tempfile.mkstemp(suffix=".pdf", dir=os.path.dirname(os.path.abspath(pdf)))
    try:
        with os.fdopen(fd, "wb") as f:
            writer.write(f)
        os.replace(tmp, pdf)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)
    return len(todo), len(reader.pages)
