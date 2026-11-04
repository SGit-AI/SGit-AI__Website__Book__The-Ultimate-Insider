#!/usr/bin/env python3
"""LAB 33: four front-cover studies on PS1, and a look for the editions (ZM1).

    python3 lab/experiments/33-designer-cover-studies/make_covers.py
Each cover is drawn at Crown Quarto, 189 x 246.1 mm (7.44 x 9.69 in), one unit a millimetre, and states the size it is
shown at in the lab (DISPLAY_W mm wide), so every text on it prints at 9 pt or more there. LAB 18's system: a near-black
ground, stacked capitals, an accent prompt line. The series line is the editor's own (G1). The title is a visible
placeholder until NS1. The creator is a neutral figure, anyone (PS1: "it could be anyone"), not the editor's look (DR1
is open). The cast from lab/characters/make_cast.py. The only numbers are the editions' sizes, from the editor's memo.
"""
import math, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

W, H = 189.0, 246.1
DISPLAY_W = 140.0                      # shown at 140 mm wide in the lab: scale 0.74
MIN_TEXT = 3.18 / (DISPLAY_W / W)      # the smallest text, in cover units, that prints at 9 pt there (about 4.3)
GROUND, PAPERY, MUTED_D, ACCENT = "#15171c", "#f3ede1", "#9aa3ad", "#b0481a"
SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'
MONO = 'font-family="DejaVu Sans Mono, monospace"'
EDITIONS = (1, 3, 10, 30, 70, 150)     # ZM1, the editor's memo of 1 November 2026, 13:00


def t(x, y, s, size, weight=700, fill=PAPERY, anchor="start", font=SANS, spacing=0):
    assert size >= MIN_TEXT, f"{s!r} at {size} would print under 9 pt"
    return (f'<text x="{x:.1f}" y="{y:.1f}" {font} font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}" letter-spacing="{spacing}">{s}</text>')


def dark(svg_elements):
    """The cast on a dark ground: their ink outlines turned light so the figures hold together."""
    return svg_elements.replace(f'stroke="{mc.INK}"', 'stroke="#d8d2c4"')


def fig(m, x, y, s, mood="happy"):
    return f'<g transform="translate({x:.1f} {y:.1f}) scale({s})">{dark(mc.figure(m, mood))}</g>'


def creator(x, y, s):
    """Anyone: the narrator's construction (option A's round head), in a neutral grey, holding nothing."""
    body = mc.editor_figure("A").replace(mc.EDITOR, "#6b7280")
    body = body.split('<rect x="2.2"')[0]  # the round head and jacket only: no brief, no pen
    return f'<g transform="translate({x:.1f} {y:.1f}) scale({s})">{dark(body)}</g>'


def frame(art, label):
    """The cover's fixed parts: ground, series line, the title placeholder, prompt line, author."""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{DISPLAY_W}mm" height="{DISPLAY_W * H / W:.1f}mm" '
            f'viewBox="0 0 {W} {H}" role="img" aria-label="{label}">'
            f'<rect width="{W}" height="{H}" fill="{GROUND}"/>'
            + art
            + t(14, 24, "GEN ZX FOUNDERS", 11, 700, MUTED_D, spacing=3.2)
            + f'<rect x="12" y="32" width="165" height="40" rx="2" fill="none" stroke="{PAPERY}" stroke-width=".7" stroke-dasharray="3 2"/>'
            + t(94.5, 50, "THE TITLE", 15, 800, anchor="middle", spacing=3)
            + t(94.5, 62, "open: NS1", 7, 400, MUTED_D, anchor="middle", font=MONO)
            + t(14, 84, "&gt; a factory of agents, one creator", 7.4, 700, ACCENT, font=MONO)
            + t(14, H - 12, "DINIS CRUZ", 9, 700, PAPERY, spacing=2.4)
            + "</svg>\n")


def ring():
    cx, cy, r = W / 2, 160, 52
    out = [f'<circle cx="{cx}" cy="{cy}" r="{r + 6}" fill="none" stroke="#2a2e36" stroke-width="10"/>']
    for k in range(12):  # the loop's direction, round the ring
        a = math.radians(k * 30 + 15)
        out.append(f'<circle cx="{cx + (r + 6) * math.cos(a):.1f}" cy="{cy + (r + 6) * math.sin(a):.1f}" r=".9" fill="{ACCENT}"/>')
    for i, m in enumerate(mc.CAST):
        a = math.radians(-90 + i * 40)
        out.append(fig(m, cx + r * math.cos(a) - 9, cy + r * math.sin(a) - 11, .45))
    out.append(creator(cx - 14, cy - 18, .7))
    # the talk, a by-product: a small screen leaving the ring at the lower right
    out.append(f'<rect x="{W - 34}" y="{H - 44}" width="16" height="10" rx="1" fill="#2a2e36" stroke="{MUTED_D}" stroke-width=".5"/>'
               f'<path d="M{W - 28} {H - 41} l4 2 l-4 2 z" fill="{ACCENT}"/>'
               f'<path d="M{cx + r + 4} {cy + 30} q 18 20 {W - 34 - cx - r - 6} {H - 39 - cy - 30}" fill="none" stroke="{MUTED_D}" stroke-width=".5" stroke-dasharray="1.5 1.5"/>')
    return "".join(out)


def festival():
    out = [f'<rect x="64" y="96" width="61" height="26" fill="none" stroke="{MUTED_D}" stroke-width=".6"/>',
           f'<path d="M64 96 l30.5 -10 l30.5 10" fill="none" stroke="{MUTED_D}" stroke-width=".6"/>',
           f'<circle cx="94.5" cy="112" r="2" fill="{ACCENT}"/>']
    for x in range(20, 175, 14):  # scaffolding
        out.append(f'<line x1="{x}" y1="128" x2="{x}" y2="196" stroke="#2f343d" stroke-width="1"/>')
    for y in (140, 168, 196):
        out.append(f'<line x1="16" y1="{y}" x2="173" y2="{y}" stroke="#2f343d" stroke-width="1"/>')
    for i, m in enumerate(mc.CAST):
        out.append(fig(m, 12 + (i % 5) * 34 + (17 if i >= 5 else 0), 142 + (i // 5) * 40, .62))
    out.append(creator(150, 186, .6))
    return "".join(out)


def mapped():
    x0, x1, y0, y1 = 22, 176, 100, 214
    out = [f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="{MUTED_D}" stroke-width=".6"/>',
           f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="{MUTED_D}" stroke-width=".6"/>',
           t(x0, y1 + 8, "genesis", 6.4, 400, MUTED_D), t(x1, y1 + 8, "commodity", 6.4, 400, MUTED_D, anchor="end")]
    pts = []
    for i, m in enumerate(mc.CAST):
        f = i / (len(mc.CAST) - 1)
        x, y = x0 + 12 + f * (x1 - x0 - 30), y0 + 30 + (1 - (1 - f) ** 2) * 60
        pts.append((x + 6, y + 6))
        out.append(fig(m, x, y, .3))
    out.append(f'<path d="M{" L".join(f"{a:.1f} {b:.1f}" for a, b in pts)}" fill="none" stroke="{ACCENT}" stroke-width=".5" stroke-dasharray="2 1.5"/>')
    out.append(creator(x0 + 4, y0 - 6, .5))
    return "".join(out)


def zoom():
    cx, cy = W / 2, 156
    out = []
    for k, n in enumerate(reversed(EDITIONS)):
        f = 1 - k * 0.15
        w, h = 160 * f, 110 * f
        out.append(f'<rect x="{cx - w / 2:.1f}" y="{cy - h / 2:.1f}" width="{w:.1f}" height="{h:.1f}" fill="none" stroke="{ACCENT if n == 3 else "#3a3f49"}" stroke-width="{1 if n == 3 else .6}"/>')
        out.append(t(cx - w / 2 + 2, cy - h / 2 + 7, f"{n}", 6.4, 700, ACCENT if n == 3 else MUTED_D, font=MONO))
    for i, m in enumerate(mc.CAST):
        a = math.radians(-90 + i * 40)
        out.append(fig(m, cx + 12 * math.cos(a) - 3, cy + 9 * math.sin(a) - 3.6, .15))
    return "".join(out)


SPECTRUM = ("#d7262e", "#f5c518", "#2fa84f", "#2b6cb0")  # red, yellow, green, blue: the series' stripes (G1), drawn here


# the six on the official cover, each with a fragment of its temperament from chapter-plan/cast/cast-guide.md
COVER_SIX = [("dev", "the builder in the hard hat:", "fast, practical"),
             ("conductor", "a stage manager with", "a stopwatch: calm"),
             ("deck", "the slide editor:", "exacting, honest"),
             ("ruv-sgit", "the night-shift", "experimenter: tireless"),
             ("researcher", "the fact-checker:", "polite, unbudging"),
             ("designer", "the beret and the pencil:", "precise, polite")]


def cover_signed(height=H):
    """The book's official cover (the editor, 3 November 2026, about 00:40 UTC: "great, can you make this the official
    cover design"), after two rounds on CV1 A in his chat: GEN ZX FOUNDERS small on the left margin with the ZX larger;
    the signed title (NS1) and subtitle; six cast cards, each with its temperament abridged from the cast guide
    (every piece checked here); RC2, NOV 2026 (the editor, CV3, 4 November) and the text's licence (CC BY 4.0, Q5); the four stripes drawn from his description."""
    guide = (Path(__file__).resolve().parents[2].parent / "chapter-plan" / "cast" / "cast-guide.md").read_text()
    low = guide.lower()
    for m, a, b in COVER_SIX:  # abridged from the member's temperament: every piece must be in the guide's words
        for piece in [p.strip() for p in (a + " " + b).replace(":", ",").split(",") if p.strip()]:
            if piece.lower() not in low:
                sys.exit(f"make_covers: {piece!r} ({m}) is not in the cast guide")

    def tt(x, y, s, size, weight=700, fill=PAPERY, anchor="start", spacing=0):
        return (f'<text x="{x:.1f}" y="{y:.1f}" {SANS} font-size="{size}" font-weight="{weight}" fill="{fill}" '
                f'text-anchor="{anchor}" letter-spacing="{spacing}">{s}</text>')

    def card(m, l1, l2, x, y, w=51, h=46):
        col = mc.CAST[m][0]
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" fill="#f3ede1"/>'
                f'<rect x="{x}" y="{y}" width="{w}" height="10" rx="2" fill="{col}"/><rect x="{x}" y="{y + 7}" width="{w}" height="3" fill="{col}"/>'
                + tt(x + 2.4, y + 7, m, 5.2, 800, "#fff")
                + f'<g transform="translate({x + w / 2 - 9} {y + 10.5}) scale(.45)">{mc.figure(m)}</g>'
                + tt(x + 3, y + h - 7.6, l1, 3.6, 500, mc.INK) + tt(x + 3, y + h - 3.2, l2, 3.6, 500, mc.MUTED))

    b = [tt(14, 18, "GEN", 5.8, 800, MUTED_D, "start", 1.8), tt(32.8, 20.6, "ZX", 12, 800, PAPERY, "start", .5),
         tt(52.6, 18, "FOUNDERS", 5.8, 800, MUTED_D, "start", 1.8),
         tt(14, 40, "ONE HUMAN,", 12.5, 800, spacing=1.2), tt(14, 55.5, "NINE AGENTS,", 12.5, 800, spacing=1.2),
         tt(14, 71, "NINETEEN HOURS", 12.5, 800, ACCENT, spacing=1.2),
         tt(14, 90, "How a factory of AI agents built", 7.6, 400), tt(14, 99.5, "a presentation in a day,", 7.6, 400),
         tt(14, 109, "and how to build yours", 7.6, 400)]
    for i, (m, l1, l2) in enumerate(COVER_SIX):
        b.append(card(m, l1, l2, 14 + (i % 3) * 54.5, 117 + (i // 3) * 50))
    # a taller cover (Leanpub's 2:3, LAB 44) keeps the series line at the top and the author at the foot, and centres
    # the title and the cards in the extra height; at the default height nothing moves
    dy = (height - H) / 2
    if dy:
        b = b[:3] + [f'<g transform="translate(0 {dy:.2f})">'] + b[3:] + ["</g>"]
    Hc = height
    b += [f'<path d="M{W - 46 + i * 7} {Hc} L{W - 40.5 + i * 7} {Hc} L{W} {Hc - (40.5 - i * 7)} L{W} {Hc - (46 - i * 7)} z" fill="{c}"/>'
          for i, c in enumerate(SPECTRUM)]
    b += [tt(14, Hc - 15, "DINIS CRUZ", 8, 700, spacing=2.2),
          tt(14, Hc - 8, "RC2  \u00b7  NOV 2026  \u00b7  CC BY 4.0", 4.4, 500, MUTED_D, spacing=1)]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{Hc:g}mm" viewBox="0 0 {W} {Hc:g}" role="img" '
            f'aria-label="Cover: Gen ZX Founders. One Human, Nine Agents, Nineteen Hours. How a factory of AI agents built a presentation in a day, and how to build yours. Six of the cast: dev, conductor, deck, ruv-sgit, researcher, designer. Dinis Cruz. RC2, Nov 2026, CC BY 4.0.">'
            f'<rect width="{W}" height="{Hc:g}" fill="{GROUND}"/>' + "".join(b) + "</svg>\n")


def ladder(current, unit=4.0, label=True):
    """The editions' look: six squares, small to large, the one the reader holds filled; its size beside it."""
    out, x = [], 0.0
    for n in EDITIONS:
        s = unit * (1 + EDITIONS.index(n) * 0.35)
        on = n == current
        out.append(f'<rect x="{x:.2f}" y="{unit * 2.75 - s:.2f}" width="{s:.2f}" height="{s:.2f}" rx=".4" fill="{ACCENT if on else "none"}" stroke="{ACCENT if on else "#9aa3ad"}" stroke-width=".4"/>')
        x += s + 1.4
    if label:
        out.append(f'<text x="{x + 2:.2f}" y="{unit * 2.75 - .4:.2f}" {SANS} font-size="3.18" font-weight="800" fill="{ACCENT}">the {current}-page edition</text>')
    return out, x


def editions_sheet():
    out = []
    for row, n in enumerate((1, 3, 10, 30)):
        g, wdt = ladder(n)
        out.append(f'<g transform="translate(0 {row * 16})">' + "".join(g) + "</g>")
    # a page head carrying it
    y = 72
    out.append(f'<rect x="0" y="{y}" width="164" height="20" rx="1.5" fill="#fff" stroke="#d5dce4" stroke-width=".35"/>')
    g, _ = ladder(3, unit=2.6, label=False)
    out.append(f'<g transform="translate(4 {y + 4})">' + "".join(g) + "</g>")
    out.append(f'<text x="160" y="{y + 9}" {SANS} font-size="3.18" fill="#5b6670" text-anchor="end">the 3-page edition, page 2 of 3</text>')
    out.append(f'<line x1="4" y1="{y + 14}" x2="160" y2="{y + 14}" stroke="#d5dce4" stroke-width=".3"/>')
    return mc.svg(164, y + 22, "".join(out), "The editions' look: six squares from 1 to 150 pages, the one the reader holds filled, on a page head")


STUDIES = {
    "a-factory": (ring, "A ring of the nine agents turning round one creator; the talk a small screen leaving the ring"),
    "b-festival": (festival, "The stage small at the back; the team building the scaffolding in front, the creator with them"),
    "c-map": (mapped, "The nine along an evolution axis from genesis to commodity, the creator above as the need"),
    "d-zoom": (zoom, "Nested frames, one per edition, closing in on the factory; the 3-page frame marked"),
}

if __name__ == "__main__":
    for name, (art, label) in STUDIES.items():
        (HERE / f"cover-{name}.svg").write_text(frame(art(), f"Cover study: {label}. The title is a placeholder."))
    (HERE / "editions.svg").write_text(editions_sheet())
    (HERE / "cover-a-signed.svg").write_text(cover_signed())
    print("written four cover studies and editions.svg")
