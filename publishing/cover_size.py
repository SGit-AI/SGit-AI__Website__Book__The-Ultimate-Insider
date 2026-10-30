#!/usr/bin/env python3
"""The paperback's full cover size for the designer: back, spine and front as one image, with bleed.

KDP's rules (publishing/KDP.md, from KDP's help read 30 October 2026): spine width = page count x
0.002252 inch on white paper, 0.0025 inch on cream; 0.125 inch of bleed on every outside edge;
spine text only from about 79 pages up. The page count is the interior PDF's, so give the PDF:

    python3 publishing/cover_size.py --pdf _site/manuscript/the-ultimate-insider.pdf [--paper cream]
    python3 publishing/cover_size.py --pages 220 [--paper white] [--trim 6x9] [--dpi 300]
"""
import argparse
import re
import sys

PER_PAGE = {"white": 0.002252, "cream": 0.0025}  # inches of spine per page, by paper
BLEED = 0.125
SPINE_TEXT_FROM = 79


def pdf_pages(path):
    """The page count of a PDF, read from its page objects (no library needed for our own PDFs)."""
    try:
        with open(path, "rb") as f:
            data = f.read()
    except OSError as e:
        sys.exit(f"cover_size: cannot read {path}: {e.strerror} (build it first: python3 publishing/build_book.py)")
    n = len(re.findall(rb"/Type\s*/Page(?!s)", data))
    if not n:
        sys.exit(f"cover_size: no pages found in {path}")
    return n


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--pages", type=int)
    src.add_argument("--pdf")
    p.add_argument("--paper", choices=sorted(PER_PAGE), default="cream")
    p.add_argument("--trim", default="6x9", help="width x height in inches, e.g. 6x9")
    p.add_argument("--dpi", type=int, default=300)
    a = p.parse_args()
    w, h = (float(x) for x in a.trim.lower().split("x"))
    pages = a.pages or pdf_pages(a.pdf)
    if pages % 2:
        pages += 1  # a printed book has an even page count: KDP adds the blank last page
    spine = pages * PER_PAGE[a.paper]
    width = BLEED + w + spine + w + BLEED
    height = BLEED + h + BLEED
    px = lambda inches: round(inches * a.dpi)
    print(f"interior   {pages} pages, {a.paper} paper, trim {w:g} x {h:g} in")
    print(f"spine      {spine:.3f} in ({spine * 25.4:.1f} mm); spine text "
          f"{'allowed' if pages >= SPINE_TEXT_FROM else f'not allowed under {SPINE_TEXT_FROM} pages'}")
    print(f"full cover {width:.3f} x {height:.3f} in ({width * 25.4:.1f} x {height * 25.4:.1f} mm), "
          f"{px(width)} x {px(height)} px at {a.dpi} dpi")
    print(f"front      from {BLEED + w + spine:.3f} in to {width - BLEED:.3f} in across; back from {BLEED:.3f} in to {BLEED + w:.3f} in")


if __name__ == "__main__":
    main()
