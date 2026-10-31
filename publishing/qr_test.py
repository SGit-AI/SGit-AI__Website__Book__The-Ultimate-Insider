#!/usr/bin/env python3
"""A printable test sheet of QR codes at several sizes, to find the smallest a phone reads on the printed page (task A5).

The book promises QR codes from the paper to the record. How small one can print depends on how many modules (squares)
it has across, which depends on how long the address is: a GitHub commit address needs far more than a short address on
the book's own site. This sheet prints both kinds at 10 to 25 mm on a 6 by 9 inch page; print it at 100% and scan each
row with a phone at reading distance. Needs reportlab (its QR widget) and a Chromium, as build_book.py does; writes
_site/manuscript/qr-test.pdf (never committed). No code is downloaded.

    python3 publishing/qr_test.py [--chrome PATH]
"""
import argparse
import os
import subprocess
import sys
import tempfile

from reportlab.graphics import renderSVG
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_book import ROOT, find_chrome  # noqa: E402

ADDRESSES = [
    ("A GitHub commit page in the talk's repository", "https://github.com/SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider/commit/298be4e"),
    ("A short address on the book's site (illustrative: no such page yet)", "https://the-ultimate-insider.book.sgit.ai/r/C010"),
]
SIZES_MM = [10, 12, 15, 20, 25]


def qr_svg(text):
    """The code as SVG, error correction M, with its own four-module quiet zone; and its modules across."""
    w = QrCodeWidget(text)
    w.barLevel = "M"
    x0, y0, x1, y1 = w.getBounds()
    d = Drawing(x1 - x0, y1 - y0)
    d.add(w)
    svg = renderSVG.drawToString(d)
    return svg[svg.index("<svg"):], len(w.qr.modules)


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--chrome")
    a = p.parse_args()
    chrome = find_chrome(a.chrome)
    if not chrome:
        sys.exit("qr_test: no Chromium or Chrome found (give --chrome PATH)")
    rows = []
    for label, url in ADDRESSES:
        svg, modules = qr_svg(url)
        cells = "".join(f'<td><div class="q" style="width:{mm}mm;height:{mm}mm">{svg}</div>{mm} mm<br>'
                        f'{mm / (modules + 8):.2f} mm a module</td>' for mm in SIZES_MM)
        rows.append(f"<h2>{label}</h2><p><code>{url}</code> ({len(url)} characters, {modules} modules across)</p>"
                    f"<table><tr>{cells}</tr></table>")
    html = ("<!doctype html><meta charset=utf-8><style>@page{size:6in 9in;margin:0.6in}body{font:9pt Georgia,serif}"
            "h1{font-size:13pt}h2{font-size:10pt;margin:1.4em 0 0.2em}code{font-size:7pt;word-break:break-all}"
            "table{border-collapse:collapse}td{vertical-align:bottom;padding:0 6px 0 0;font-size:7pt;text-align:center}"
            ".q svg{width:100%;height:100%;display:block}</style>"
            "<h1>QR codes: the smallest a phone reads</h1><p>Print at 100% (no scaling) and scan each code with a phone "
            "at reading distance. Note the smallest that opens the page, for each address. Sizes include the code's "
            "quiet margin.</p>" + "".join(rows))
    out = os.path.join(ROOT, "_site", "manuscript")
    os.makedirs(out, exist_ok=True)
    pdf = os.path.join(out, "qr-test.pdf")
    with tempfile.TemporaryDirectory() as tmp:
        page = os.path.join(tmp, "qr-test.html")
        with open(page, "w", encoding="utf-8") as f:
            f.write(html)
        try:
            subprocess.run([chrome, "--headless", "--no-sandbox", "--disable-gpu", f"--user-data-dir={tmp}/p",
                            "--no-pdf-header-footer", f"--print-to-pdf={pdf}", "file://" + page],
                           timeout=90, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.TimeoutExpired:
            pass
    print(f"qr_test: {os.path.relpath(pdf, ROOT)}")


if __name__ == "__main__":
    main()
