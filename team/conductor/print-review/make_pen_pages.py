#!/usr/bin/env python3
"""The editor's pen, drawn: each photographed page with its notes boxed and numbered, and beside it a card per note
with his words and what they mean (PEN1, the editor, 13 November 2026, after the newsroom's "143 notes in a day").

    python3 team/conductor/print-review/make_pen_pages.py 01

Reads team/conductor/print-review/round-NN.json (the notes, and each note's box on its photograph, in the photograph's
own pixels as it was sent, 1500 x 2000) and writes src/static/assets/print-review/round-N-pXX-pen.jpg. A correction to
a reading or a box is one line in the JSON."""
import json, sys, textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[3]
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
OBL = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
COL = {"writer": (200, 40, 48), "designer": (124, 58, 237), "publisher": (37, 99, 235),
       "storyteller": (5, 150, 105), "researcher": (217, 119, 6)}


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, f, width):
    out = []
    for para in text.split("\n"):
        words, line = para.split(), ""
        for w in words:
            t = (line + " " + w).strip()
            if draw.textlength(t, font=f) <= width:
                line = t
            else:
                out.append(line); line = w
        out.append(line)
    return out


def page(rnd, pg, notes, photo):
    im = Image.open(ROOT / photo).convert("RGB")
    s = im.width / 1500                                        # boxes are in the photograph's own 1500 x 2000 pixels
    ov = Image.new("RGBA", im.size, (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
    d = ImageDraw.Draw(im)
    fnum = font(BOLD, 22)
    for n in notes:
        c = COL[n["who"][0]]
        x0, y0, x1, y1 = [v * s for v in n["box"]]
        od.rectangle([x0, y0, x1, y1], fill=c + (38,), outline=c + (230,), width=4)
    im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB"); d = ImageDraw.Draw(im)
    for n in notes:
        c = COL[n["who"][0]]
        x0, y0 = n["box"][0] * s, n["box"][1] * s
        d.ellipse([x0 - 20, y0 - 20, x0 + 20, y0 + 20], fill=c, outline="white", width=3)
        t = str(n["n"]); d.text((x0 - d.textlength(t, font=fnum) / 2, y0 - 13), t, font=fnum, fill="white")
    # the panel: a card per note
    W = 900; pad = 26; inner = W - 2 * pad - 40
    fh, fl, fq, fm = font(BOLD, 30), font(BOLD, 17), font(OBL, 26), font(FONT, 20)
    probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    cards = []
    for n in notes:
        q = wrap(probe, "“" + n["his_words"] + "”", fq, inner)
        m = wrap(probe, n["reading"] or ("The line: " + n["on_the_page"]), fm, inner)
        h = 18 + 26 + len(q) * 33 + 8 + len(m) * 27 + 18
        cards.append((n, q, m, h))
    H = max(im.height, 110 + sum(h + 14 for *_, h in cards) + pad)
    out = Image.new("RGB", (im.width + W, H), (250, 250, 248)); out.paste(im, (0, 0))
    d = ImageDraw.Draw(out); X = im.width + pad
    d.text((X, 28), f"Page {pg}", font=fh, fill=(20, 20, 20))
    d.text((X, 68), "What the pen says, word for word, and what it means", font=font(FONT, 19), fill=(110, 110, 110))
    y = 110
    for n, q, m, h in cards:
        c = COL[n["who"][0]]
        d.rounded_rectangle([X, y, X + W - 2 * pad, y + h], radius=10, fill="white", outline=c, width=3)
        d.rectangle([X, y + 4, X + 6, y + h - 4], fill=c)
        cx, cy = X + 30, y + 30
        d.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill=c)
        t = str(n["n"]); d.text((cx - d.textlength(t, font=fl) / 2, cy - 11), t, font=fl, fill="white")
        d.text((X + 56, y + 20), ", ".join(n["who"]).upper() + ("  ·  " + n["state"].upper() if n["state"] != "open" else ""),
               font=fl, fill=c)
        yy = y + 18 + 26
        for line in q:
            d.text((X + 20, yy), line, font=fq, fill=(25, 35, 90)); yy += 33
        yy += 8
        for line in m:
            d.text((X + 20, yy), line, font=fm, fill=(55, 55, 55)); yy += 27
        # a dashed leader from the card to its box
        bx, by = n["box"][2] * s, (n["box"][1] + n["box"][3]) / 2 * s
        ex, ey = X, y + 30
        steps = 40
        for i in range(0, steps, 2):
            a, b = i / steps, (i + 1) / steps
            d.line([bx + (ex - bx) * a, by + (ey - by) * a, bx + (ex - bx) * b, by + (ey - by) * b], fill=c + (0,) if False else c, width=1)
        y += h + 14
    return out


def main():
    rnd = sys.argv[1]
    data = json.loads((ROOT / f"team/conductor/print-review/round-{rnd}.json").read_text())
    for pg in data["pages"]:
        notes = [n for n in data["notes"] if n["page"] == pg]
        photo = f"src/static/assets/print-review/round-{int(rnd)}-p{pg:02d}.jpg"
        img = page(int(rnd), pg, notes, photo)
        dst = ROOT / f"src/static/assets/print-review/round-{int(rnd)}-p{pg:02d}-pen.jpg"
        img.save(dst, quality=84, optimize=True)
        print("written", dst.relative_to(ROOT), img.size)


if __name__ == "__main__":
    main()
