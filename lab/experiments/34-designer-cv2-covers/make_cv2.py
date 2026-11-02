#!/usr/bin/env python3
"""LAB 34: CV2, six front covers on the signed title, and the 10-page edition's two drawings that are the designer's.

    python3 lab/experiments/34-designer-cv2-covers/make_cv2.py
Every cover carries the same signed parts (NS1, G1): GEN ZX FOUNDERS with the ZX large, the title, the subtitle, the
author, and four diagonal stripes in the Spectrum's colours drawn here. Only the art differs. The art of B, C and D
is LAB 33's studies, scaled into the space under the title. Numbers on E are read from claims/register.json at
build, each printed with its id. Nothing is chosen for the editor: CV1 A stands until he signs another.
"""
import json, math, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
for p in ("lab/characters", "lab/experiments/33-designer-cover-studies", "lab/experiments/27-designer-the-cast"):
    sys.path.insert(0, str(REPO / p))
import make_cast as mc  # noqa: E402
import make_covers as cv  # noqa: E402
import make_sheets as ms  # noqa: E402  (LAB 27: the cards)

W, H, t = cv.W, cv.H, cv.t
REG = {c["id"]: c["value"] for c in json.loads((REPO / "claims" / "register.json").read_text())["claims"]}


def signed(art, label):
    stripes = "".join(f'<path d="M{W - 58 + i * 9} {H} L{W - 51 + i * 9} {H} L{W} {H - (51 - i * 9)} L{W} {H - (58 - i * 9)} z" fill="{c}"/>'
                      for i, c in enumerate(cv.SPECTRUM))
    text = (t(14, 22, "GEN", 11, 800, cv.MUTED_D, spacing=2.4) + t(43, 26, "ZX", 26, 800, cv.PAPERY, spacing=1)
            + t(86, 22, "FOUNDERS", 11, 800, cv.MUTED_D, spacing=2.4)
            + t(14, 56, "ONE HUMAN,", 15.5, 800, spacing=1.5) + t(14, 76, "NINE AGENTS,", 15.5, 800, spacing=1.5)
            + t(14, 96, "NINETEEN HOURS", 15.5, 800, cv.ACCENT, spacing=1.5)
            + t(14, 110, "How a factory of AI agents built a presentation", 6.2, 400) + t(14, 118, "in a day, and how to build yours", 6.2, 400)
            + t(14, H - 12, "DINIS CRUZ", 9, 700, spacing=2.4))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}" role="img" aria-label="{label}">'
            f'<rect width="{W}" height="{H}" fill="{cv.GROUND}"/>{art}{stripes}{text}</svg>\n')


def under_title(art):  # LAB 33's art (drawn for y 86 to 225) scaled into y 124 to 221
    return f'<g transform="translate(28 64) scale(.7)">{art}</g>'


def art_a():
    svg = cv.cover_signed()  # LAB 33's signed cover: its art only, between the ground and the first text
    start = svg.index(f'fill="{cv.GROUND}"/>') + len(f'fill="{cv.GROUND}"/>')
    return svg[start:svg.index("<text")]


def art_numbers():
    nine = REG["C011"]["staffed"]
    commits = REG["C004"]["total"]
    span = REG["C037"]["span"].split(",")[1].split("(")[0].strip()  # '18 h 44 min'
    rows = [(str(nine), "agents", "C011"), (span, "first commit to 19:00", "C037"), (str(commits), "commits, releases included", "C004")]
    out = []
    for i, (big, words, cid) in enumerate(rows):
        y = 150 + i * 28
        out.append(t(14, y, big, 22 if len(big) < 5 else 15, 800, cv.ACCENT if i == 0 else cv.PAPERY))
        out.append(t(14, y + 8, f"{words} ({cid})", 6, 400, cv.MUTED_D))
    for i, m in enumerate(mc.CAST):  # the nine, small, down the right
        out.append(cv.fig(m, 132 + (i % 3) * 16, 132 + (i // 3) * 22, .36))
    return "".join(out)


def art_cards():
    """Three cards as they arrived, cut to what reads on a cover: the head, the name, the time on stage (C011)."""
    rows = ms.scorecard_rows()
    order = sorted(mc.CAST, key=lambda m: rows[m][0])[:3]
    out = []
    for i, m in enumerate(order):
        x, y, w, h = 14 + i * 56, 132, 50, 70
        col = mc.CAST[m][0]
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2.5" fill="#f3ede1"/>'
                   f'<rect x="{x}" y="{y}" width="{w}" height="18" rx="2.5" fill="{col}"/><rect x="{x}" y="{y + 14}" width="{w}" height="4" fill="{col}"/>')
        out.append(f'<g transform="translate({x + 9} {y + 18}) scale(.8)">{mc.figure(m)}</g>')
        out.append(t(x + 4, y + 12, m, 7, 800, "#fff"))
        out.append(t(x + 4, y + h - 5, f"on stage {rows[m][0]}", 5.6, 700, mc.INK))
    out.append(t(14, 210, "the first three on stage (C011)", 5, 400, cv.MUTED_D))
    return "".join(out)


COVERS = {
    "A": ("the factory (CV1, signed)", art_a, "the signed study: a creator inside a ring of agents, the talk a small screen leaving it"),
    "B": ("the festival set-up", lambda: under_title(cv.festival()), "the book is the setting-up, not the band: the stage small, the team building in front"),
    "C": ("the map", lambda: under_title(cv.mapped()), "for readers who know maps: the nine moving from genesis to commodity, the creator as the need"),
    "D": ("the zoom", lambda: under_title(cv.zoom()), "the editions as frames closing in on the factory: the cover explains the zoom"),
    "E": ("the numbers", art_numbers, "the editor's idea: the day's numbers big, each with its claim id, the nine small beside them"),
    "F": ("the cast's cards", art_cards, "the first three on stage, as cards: the book is told by its cast, and the cover says so"),
}
PICK = "A"


def sheet_pages():
    """pages.html: the six side by side (thumbnails as one image, the cases in 9 pt text), then one per page."""
    import subprocess, tempfile
    html = "<html><body style='margin:0;background:#fff;display:flex;gap:4mm'>" + "".join(
        f"<div style='width:60mm'><img style='width:60mm' src='file://{HERE}/cover-{k}.svg'></div>" for k in COVERS) + "</body></html>"
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(html)
    js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1500,height:300},deviceScaleFactor:1.6});"
          f"await p.goto('file://{f.name}');await p.screenshot({{path:'{HERE}/sheet.png',fullPage:true}});await b.close()}})()")
    subprocess.run(["node", "-e", js], check=True, cwd=tempfile.gettempdir())
    rows = "".join(f"<p class='t-cap'><b>{k}, {name}{' (my pick)' if k == PICK else ''}:</b> {case}.</p>" for k, (name, _, case) in COVERS.items())
    pages = [f"""<section class="page" data-claims="C004 · C011 · C037">
 <figure class="fig"><p class="fig-title">Six covers on the signed title, side by side</p>
  <img src="../experiments/34-designer-cv2-covers/sheet.png" style="width:164mm" alt="The six covers A to F side by side">
  <figcaption><b>Choose with a word: A to F.</b> <span class="src">thumbnails only; each cover is printed full size on the pages after, its text at 9 pt or more</span></figcaption></figure>
 {rows}
 <p class="t-cap"><b>Signed: A</b> (CV2, the editor, 2 November 2026: "I like that first cover"). The other five rest.</p>
</section>"""]
    for k, (name, _, case) in COVERS.items():
        pages.append(f"""<section class="page" data-claims="{'C004 · C011 · C037' if k == 'E' else ('C011' if k == 'F' else '')}">
 <figure class="fig"><p class="fig-title">Cover {k}: {name}</p>
  <div style="width:140mm;margin:0 auto">{{{{file:experiments/34-designer-cv2-covers/cover-{k}.svg}}}}</div>
  <figcaption><b>{case[0].upper() + case[1:]}.</b> <span class="src">the signed title, subtitle and series line (NS1, G1); the stripes drawn here{'; the numbers read from claims/register.json at build' if k in ('E', 'F') else ''}</span></figcaption></figure>
</section>""")
    (HERE / "pages.html").write_text("\n".join(pages) + "\n")


def lectern():
    """10-page edition, page 1: the narrator at a lectern with a play button; behind him the factory's nine stations."""
    out = []
    for i, m in enumerate(mc.ARRIVAL if hasattr(mc, "ARRIVAL") else mc.CAST):
        x = 8 + i * 16.6
        out.append(f'<rect x="{x - 1:.1f}" y="2" width="15" height="22" rx="1.5" fill="{mc.FILL}" stroke="{mc.FILL2}" stroke-width=".35"/>')
        out.append(f'<g transform="translate({x - 1.2:.1f} 3) scale(.38)">{mc.figure(m)}</g>')
    out.append(f'<rect x="58" y="34" width="48" height="27" rx="1.6" fill="#fff" stroke="{mc.INK}" stroke-width=".5"/>'
               f'<circle cx="82" cy="47.5" r="7" fill="{mc.ACCENT}"/><path d="M79.6 43.6 l6.6 3.9 l-6.6 3.9 z" fill="#fff"/>')
    out.append(f'<path d="M100 92 l6 -24 h18 l6 24 z" fill="{mc.FILL2}" stroke="{mc.INK}" stroke-width=".5"/>')
    out.append(f'<g transform="translate(102 46) scale(.62)">{mc.editor_figure("A")}</g>')
    out.append(f'<path d="M100 92 l6 -24 h18 l6 24 z" fill="{mc.FILL2}" stroke="{mc.INK}" stroke-width=".5" opacity=".92"/>')
    return mc.svg(164, 94, "".join(out), "The narrator at a lectern beside a play button; behind, the factory's nine stations, one member at each")


def four_cards():
    """The first four on stage as compact cards in one row (publisher__013: page 2 on one sheet): head, name, two values."""
    rows = ms.scorecard_rows()
    order = sorted(mc.CAST, key=lambda m: rows[m][0])[:4]
    out = []
    for i, m in enumerate(order):
        x, y, w, h = i * 40.8 + .5, .5, 39.6, 33
        col = mc.CAST[m][0]
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>'
                   f'<rect x="{x}" y="{y}" width="{w}" height="12" rx="2" fill="{col}"/><rect x="{x}" y="{y + 9}" width="{w}" height="3" fill="{col}"/>'
                   f'<rect x="{x + 1.4}" y="{y + 1.2}" width="10" height="9.6" rx="1.2" fill="#fff"/>'
                   f'<g transform="translate({x + 1.1} {y + 1}) scale(.26)">{mc.head(m)}</g>')
        out.append(ms.t(x + 13.5, y + 7.6, m, 800, fill="#fff"))
        out.append(ms.t(x + 2.4, y + 18.2, "on stage from", fill=mc.MUTED) + ms.t(x + w - 2.4, y + 18.2, rows[m][0], 800, anchor="end"))
        out.append(ms.t(x + 2.4, y + 23.6, "commits", fill=mc.MUTED) + ms.t(x + w - 2.4, y + 23.6, rows[m][1], 800, anchor="end"))
        out.append(ms.t(x + 2.4, y + 29.6, "C011 C014", fill=mc.MUTED))
    return mc.svg(164, 34, "".join(out), "The cards of the first four on stage: " + ", ".join(order))


if __name__ == "__main__":
    for k, (name, art, case) in COVERS.items():
        (HERE / f"cover-{k}.svg").write_text(signed(art(), f"Cover {k}, {name}: One Human, Nine Agents, Nineteen Hours"))
    sheet_pages()
    ed = REPO / "lab" / "characters" / "editions"
    (ed / "figure-10-01.svg").write_text(lectern())
    (ed / "figure-10-02.svg").write_text(four_cards())
    print("written six covers and the two edition figures")
