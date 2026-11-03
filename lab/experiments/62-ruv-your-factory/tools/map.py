"""RC2 chapter 5's map (ruv; left to ruv-sgit by the designer, designer__098): "your factory", chapter 2's map carried forward.

Placed by chapter 5's Map line and narrator (manuscript/rc2/30/05-the-factory-rebuilt-and-yours.md, "Your factory"): "one
project's parts becoming the next one's: the talk team's parts on the left, custom and built that night; this book's team in
the middle, ported; yours on the right, the same parts as ordinary, ready to use", and the four parts the narrator names, "a
tool, a page of rules, a brief and a hold". Each part is drawn three times along the book's evolution axis, joined by the
dashed arrows a Wardley map uses for movement (manuscript/00b-how-to-read-a-map.md). No number. Writes map.svg and pages.html.
Usage: python3 -B -I tools/map.py
"""
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
INK, MUTED, FILL, FILL2, ACCENT, PAPER = '#1f2933', '#5b6670', '#eef2f6', '#d5dce4', '#b0481a', '#ffffff'
SANS = 'Inter, Helvetica, Arial, sans-serif'
PT = 9 * 25.4 / 72
W, H = 164.0, 66.0
X0, X1 = 30.0, 162.0
PARTS = ['a tool', 'a page of rules', 'a brief', 'a hold']
WHO = [(0.36, "the talk's team,", 'built that night'), (0.62, "this book's team,", 'ported'), (0.88, 'yours,', 'ready to use')]
STAGES = ['new', 'custom built', 'product', 'ordinary']
TOP, ROW = 22.0, 9.5


def t(x, y, s, weight=400, fill=INK, anchor='start'):
    return f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{PT:.3f}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'


def main():
    X = lambda e: X0 + e * (X1 - X0)
    yb = TOP + ROW * (len(PARTS) - 1) + 8
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H:g}mm" viewBox="0 0 {W:g} {H:g}" role="img" '
         'aria-label="Your factory, a Wardley map: a tool, a page of rules, a brief and a hold, each moving right: built by the talk\'s team '
         'that night, ported by this book\'s team, and ready to use for you.">',
         '<defs><marker id="ar" markerWidth="4" markerHeight="4" refX="3.4" refY="2" orient="auto"><path d="M0 0 L4 2 L0 4 z" fill="#5b6670"/></marker></defs>']
    for i, name in enumerate(STAGES):
        xa = X0 + i * (X1 - X0) / 4
        if i:
            s.append(f'<line x1="{xa:.2f}" y1="{TOP - 16}" x2="{xa:.2f}" y2="{yb:.2f}" stroke="{FILL2}" stroke-width=".3" stroke-dasharray="1 1"/>')
        s.append(t(xa + (X1 - X0) / 8, H - 2.4, name, 400, MUTED, 'middle'))
    s.append(f'<line x1="{X0:.2f}" y1="{yb + 1:.2f}" x2="{X1:.2f}" y2="{yb + 1:.2f}" stroke="{MUTED}" stroke-width=".35" marker-end="url(#ar)"/>')
    for e, a, b in WHO:
        s.append(t(X(e), 6.4, a, 700, ACCENT if a == 'yours,' else INK, 'middle'))
        s.append(t(X(e), 10.6, b, 400, MUTED, 'middle'))
    for r, part in enumerate(PARTS):
        y = TOP + r * ROW
        s.append(t(0, y + 1.1, part, 700))
        for k in range(len(WHO) - 1):
            xa, xb = X(WHO[k][0]) + 2, X(WHO[k + 1][0]) - 2.2
            s.append(f'<line x1="{xa:.2f}" y1="{y}" x2="{xb:.2f}" y2="{y}" stroke="{MUTED}" stroke-width=".35" stroke-dasharray="1.2 .8" marker-end="url(#ar)"/>')
        for k, (e, a, b) in enumerate(WHO):
            last = k == len(WHO) - 1
            s.append(f'<circle cx="{X(e):.2f}" cy="{y}" r="1.4" fill="{ACCENT if last else PAPER}" stroke="{ACCENT if last else INK}" stroke-width=".4"/>')
    s.append('</svg>')
    (HERE / 'map.svg').write_text('\n'.join(s) + '\n')
    (HERE / 'pages.html').write_text(
        '<section class="page" data-claims="">\n <figure class="fig span12">\n'
        '  <p class="fig-title">Your factory</p>\n'
        '  <img src="{{dir}}/map.svg" alt="Your factory: a tool, a page of rules, a brief and a hold, each moving right, from built that night, to ported, to ready to use" style="width:100%;display:block">\n'
        '  <figcaption><b>Every part I had to invent, or carry over by hand, is already on the right for you: a tool, a page of rules, a brief and a hold.</b> '
        'Chapter 2\'s map carried forward: read each row left to right, as one project\'s part becomes the next one\'s.'
        '<span class="src">Placed by chapter 5\'s Map line and narrator (manuscript/rc2/30/05-the-factory-rebuilt-and-yours.md), in the conventions of "How to read a map"; '
        'the dashed arrows are a Wardley map\'s marks for movement.</span></figcaption>\n </figure>\n</section>\n')
    print('map.svg and pages.html written')


if __name__ == '__main__':
    main()
