"""The three rounds drawn (ruv): the fallback for publisher__007, with no image, href, script or handler in it.

Each round's shape is drawn after the talk's own still, not copied: v1 the mandate's four dots inside a ring, the twelve of the
excess outside it, and the list as bars set apart, not touching (deck: a table beside a diagram); v2 the twelve at two distances,
two unstated inside and ten refused outside, the list's bars now marked like the dots; v3 the twelve grouped in five arcs, four,
three, two, two and one. The counts match the stills and the register (C084: mandate four granted, excess twelve, unstated two,
refused ten; C086: the excess by kind). No word or id from the stills. Under each, the same outcome and deck's verdict word for
word as in three-rounds.svg. Writes edition/three-rounds-drawn.svg; refuses itself if publishing/edition.py's UNSAFE_SVG matches.
Usage: python3 -B -I tools/drawn.py
"""
import html, math, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE / 'tools'))
from rounds import ROUNDS, wrap, W, GAP, PW, PT, LEAD, INK, MUTED, FILL2, ACCENT, SANS     # the same words, the same frame

DARK, PANEL, WHITE, RED, RING = '#0d1117', '#1a1f26', '#f5f7fa', '#ff4f6d', '#3a4350'
UNSAFE = re.compile(r"<script|<foreignObject|\bhref\s*=|\bon[a-z]+\s*=|@import", re.I)   # publishing/edition.py's rule
IH = PW * 9 / 16


def dot(x, y, r, fill):
    return f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="{fill}"/>'


def panel(i, x):
    cx, cy, R = x + PW * .3, IH * .56, IH * .4
    s = [f'<rect x="{x:.2f}" y="0" width="{PW:.2f}" height="{IH:.2f}" rx="1" fill="{DARK}"/>',
         f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{R:.2f}" fill="{PANEL}"/>',
         f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{R * .38:.2f}" fill="none" stroke="{WHITE}" stroke-width=".35"/>']
    for k in range(4):                                             # the mandate, four granted (C084)
        a = math.pi / 2 * k + math.pi / 4
        s.append(dot(cx + R * .2 * math.cos(a), cy + R * .2 * math.sin(a), .55, WHITE))
    if i == 0:                                                     # v1: twelve evenly round, the list apart
        for k in range(12):
            a = 2 * math.pi * k / 12
            s.append(dot(cx + R * .82 * math.cos(a), cy + R * .82 * math.sin(a), .6, RED))
        bx = x + PW * .62
        for k in range(12):
            s.append(f'<rect x="{bx:.2f}" y="{IH * .14 + k * IH * .065:.2f}" width="{PW * .32:.2f}" height="{IH * .032:.2f}" fill="{RED}" opacity=".7"/>')
    else:
        for rr in (.62, .88):
            s.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{R * rr:.2f}" fill="none" stroke="{RING}" stroke-width=".25"/>')
        if i == 1:                                                 # v2: two unstated inside, ten refused outside (C084)
            angs = [(2 * math.pi * k / 10 + .3, .88) for k in range(10)] + [(1.2, .62), (3.9, .62)]
            for a, rr in angs:
                s.append(dot(cx + R * rr * math.cos(a), cy + R * rr * math.sin(a), .6, RED))
        else:                                                      # v3: five arcs of four, three, two, two and one (C086)
            groups, start = [4, 3, 2, 2, 1], -math.pi / 2 - .9
            for g, n in enumerate(groups):
                a0 = start + g * 2 * math.pi / 5
                span = .22 * (n - 1)
                rr = .62 if g >= 3 else .88                        # records and schedule held the two unstated in v3's still
                s.append(f'<path d="M{cx + R * .98 * math.cos(a0 - .12):.2f} {cy + R * .98 * math.sin(a0 - .12):.2f} '
                         f'A{R * .98:.2f} {R * .98:.2f} 0 0 1 {cx + R * .98 * math.cos(a0 + span + .12):.2f} {cy + R * .98 * math.sin(a0 + span + .12):.2f}" '
                         f'fill="none" stroke="{RED}" stroke-width=".35"/>')
                for k in range(n):
                    a = a0 + k * .22
                    s.append(dot(cx + R * (rr if k == 0 and g >= 3 else .88) * math.cos(a),
                                 cy + R * (rr if k == 0 and g >= 3 else .88) * math.sin(a), .6, RED))
        bx = x + PW * .62
        for k in range(12):
            y = IH * .14 + k * IH * .065
            s.append(dot(bx + .6, y + IH * .016, .5, RED))
            s.append(f'<rect x="{bx + 1.6:.2f}" y="{y:.2f}" width="{PW * .28:.2f}" height="{IH * .032:.2f}" fill="{WHITE}" opacity=".55"/>')
    return s


def main():
    rows, hmax = [], 0
    for i, (v, stem, outcome, quote, commit) in enumerate(ROUNDS):
        x = i * (PW + GAP)
        rows += panel(i, x)
        y = IH + 2.2 + PT
        for ln in wrap(outcome, PW, PT * .56):
            rows.append(f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{PT:.3f}" font-weight="700" fill="{ACCENT if i == 0 else INK}">{html.escape(ln)}</text>'); y += LEAD
        y += .8
        for ln in wrap('“' + quote + '”', PW, PT * .6):
            rows.append(f'<text x="{x + .6:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{PT:.3f}" font-style="italic" fill="{INK}">{html.escape(ln)}</text>'); y += LEAD
        rows.append(f'<text x="{x:.2f}" y="{y + .6:.2f}" font-family="{SANS}" font-size="{PT:.3f}" fill="{MUTED}">deck, {commit}</text>')
        hmax = max(hmax, y + 2)
    H = round(hmax + 1, 1)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H:g}mm" viewBox="0 0 {W:g} {H:g}" role="img" '
           'aria-label="One picture\'s three rounds, drawn after the talk\'s stills: a ring and a list apart, then dots at two distances, then dots grouped in arcs; '
           'deck\'s verdict under each in its own words.">\n' + '\n'.join(rows) + '\n</svg>\n')
    if UNSAFE.search(svg):
        sys.exit('the drawing would be refused by the build: a script, link or handler in it')
    (HERE / 'edition' / 'three-rounds-drawn.svg').write_text(svg)
    print('three-rounds-drawn.svg', f'{W:g} x {H:g} mm, no href')


if __name__ == '__main__':
    main()
