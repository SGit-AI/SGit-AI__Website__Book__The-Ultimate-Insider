#!/usr/bin/env python3
"""LAB 81: the footer with the chapter's own bar (PEN1 note 9), shown on a real build.

    python3 lab/experiments/81-designer-footer/make_footer.py <built.pdf> <name-chapters.json> "<chapter title>"

Stamps the PDF with lab/tools/book/chapter_bar.py (into a temporary file), then crops the foot of every page of the
named chapter at 200 dpi, one strip under another, into footer-study.png. The PDF is read, never kept here.
"""
import json, subprocess, sys, tempfile
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
pdf, cj, title = sys.argv[1:4]
chs = sorted(json.load(open(cj))["chapters"], key=lambda c: c["page"])
i = next(k for k, c in enumerate(chs) if c["title"] == title)
first, last = chs[i]["page"], chs[i + 1]["page"] - 1
with tempfile.TemporaryDirectory() as tmp:
    out = f"{tmp}/bars.pdf"
    subprocess.run([sys.executable, str(REPO / "lab/tools/book/chapter_bar.py"), pdf, cj, out], check=True)
    strips = []
    for p in range(first, last + 1):
        subprocess.run(["pdftoppm", "-f", str(p), "-l", str(p), "-r", "200", "-png", "-singlefile", out, f"{tmp}/p{p}"],
                       check=True, stderr=subprocess.DEVNULL)
        im = Image.open(f"{tmp}/p{p}.png").convert("RGB")
        strips.append(im.crop((0, im.height - 115, im.width, im.height - 25)))
w = strips[0].width
sheet = Image.new("RGB", (w, sum(s.height + 16 for s in strips) - 16), "white")
y = 0
for s in strips:
    sheet.paste(s, (0, y)); y += s.height + 16
    if y < sheet.height:
        sheet.paste(Image.new("RGB", (w, 2), (213, 220, 228)), (0, y - 9))
sheet.save(HERE / "footer-study.png", optimize=True)
print(f"footer-study.png: pages {first} to {last}, {w} by {sheet.height} px")
