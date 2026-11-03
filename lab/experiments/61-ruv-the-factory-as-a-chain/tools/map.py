"""RC2 chapter 2's map (ruv; the conductor named the owner, conductor__016): the factory as a chain, a Wardley map.

Placed by the chapter's own figure brief and narrator (manuscript/rc2/30/02-the-factory-is-assembled.md, "The map, before its
name"): the editor at the top, wanting a talk the room understands; under it the slides, the site and the player; under those
the agents; at the bottom what the agents ran on, the agent tool, the build, the check and the brief at the ordinary end, and
the hold at the new end, made that night. Left to right by how settled each part already was, in the book's four stages and
its conventions (manuscript/00b-how-to-read-a-map.md): the user a dark dot, each line "needs". The talk and the slides near the
new edge and the site and the player in custom built follow 00b's map 2; the agents, which the brief does not place, sit where
the team was made that day, at genesis edging into custom built: our reading, said on the page. No number on the map.
Writes map.svg and pages.html.
Usage: python3 -B -I tools/map.py
"""
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
INK, MUTED, FILL, FILL2, ACCENT, PAPER = '#1f2933', '#5b6670', '#eef2f6', '#d5dce4', '#b0481a', '#ffffff'
SANS = 'Inter, Helvetica, Arial, sans-serif'
PT = 9 * 25.4 / 72
W, H = 164.0, 100.0
X0, X1, Y0, Y1 = 14.0, 162.0, 6.0, 88.0                          # the map's field

# evolution 0..1 across the four stages; rows top to bottom
NODES = {
    'editor':  (0.09, 0.00, 'the editor', 'user'),
    'talk':    (0.07, 0.17, 'a talk the room understands', 'need'),
    'slides':  (0.15, 0.38, 'the slides', None),
    'site':    (0.36, 0.38, 'the site', None),
    'player':  (0.40, 0.50, 'the player', None),
    'agents':  (0.24, 0.66, 'the agents', None),
    'hold':    (0.08, 0.95, 'the hold, made that night', 'new'),
    'brief':   (0.66, 0.95, 'the brief', None),
    'check':   (0.76, 0.86, 'the check', None),
    'build':   (0.82, 0.95, 'the build', None),
    'tool':    (0.70, 0.80, 'the agent tool', None),
}
LEFT = {'slides', 'agents'}
ABOVE = {'talk'}                                               # set above its dot, clear of the lines leaving it                                   # labels set to the left of their dot, clear of the lines
LINKS = [('editor', 'talk'), ('talk', 'slides'), ('talk', 'site'), ('talk', 'player'),
         ('slides', 'agents'), ('site', 'agents'), ('player', 'agents'),
         ('agents', 'tool'), ('agents', 'build'), ('agents', 'check'), ('agents', 'brief'), ('agents', 'hold')]
STAGES = ['new', 'custom built', 'product', 'ordinary']   # 00b's four stages, the ends in the chapter's own words


def xy(k):
    e, r = NODES[k][:2]
    return X0 + e * (X1 - X0), Y0 + r * (Y1 - Y0)


def t(x, y, s, weight=400, fill=INK, anchor='start'):
    return f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{PT:.3f}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'


def main():
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H:g}mm" viewBox="0 0 {W:g} {H:g}" role="img" '
         'aria-label="The factory as a chain, a Wardley map: the editor and his talk at the top, the slides, site and player, the agents, '
         'and at the bottom what they ran on: the agent tool, the build, the check and the brief at the ordinary end, the hold at the new end.">']
    # stage bands and the axis
    for i, name in enumerate(STAGES):
        xa = X0 + i * (X1 - X0) / 4
        if i:
            s.append(f'<line x1="{xa:.2f}" y1="{Y0 - 2}" x2="{xa:.2f}" y2="{Y1 + 3}" stroke="{FILL2}" stroke-width=".3" stroke-dasharray="1 1"/>')
        s.append(t(xa + (X1 - X0) / 8, H - 2.4, name, 400, MUTED, 'middle'))
    s.append(f'<line x1="{X0:.2f}" y1="{Y1 + 4:.2f}" x2="{X1:.2f}" y2="{Y1 + 4:.2f}" stroke="{MUTED}" stroke-width=".35"/>')
    s.append(f'<path d="M{X1 - 1.6:.2f} {Y1 + 3:.2f} L{X1:.2f} {Y1 + 4:.2f} L{X1 - 1.6:.2f} {Y1 + 5:.2f}" fill="none" stroke="{MUTED}" stroke-width=".35"/>')
    s.append(t(1, Y0 + 2, 'seen', 400, MUTED))
    s.append(t(1, Y1, 'unseen', 400, MUTED))
    for a, b in LINKS:
        (x1, y1), (x2, y2) = xy(a), xy(b)
        s.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{MUTED}" stroke-width=".3"/>')
    for k, (e, r, label, kind) in NODES.items():
        x, y = xy(k)
        if kind == 'user':
            s.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="1.6" fill="{INK}"/>')
        elif kind == 'new':
            s.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="1.5" fill="{ACCENT}"/>')
        else:
            s.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="1.3" fill="{PAPER}" stroke="{INK}" stroke-width=".4"/>')
        left = k in LEFT
        dy = -2.2 if k in ABOVE else 1.1
        s.append(t(x - 2.4 if left else x + 2.4, y + dy, label, 700 if kind in ('user', 'need', 'new') else 400,
                   ACCENT if kind == 'new' else INK, 'end' if left else 'start'))
    s.append('</svg>')
    (HERE / 'map.svg').write_text('\n'.join(s) + '\n')
    (HERE / 'pages.html').write_text(
        '<section class="page" data-claims="">\n <figure class="fig span12">\n'
        '  <p class="fig-title">The factory as a chain</p>\n'
        '  <img src="{{dir}}/map.svg" alt="A Wardley map of the factory: the editor and his talk at the top, what it needed below, and at the bottom the ordinary parts and one new one, the hold" style="width:100%;display:block">\n'
        '  <figcaption><b>Look at the bottom row first: almost all of it was already ordinary, so the top could be built in a day. '
        'The one new part at the bottom is the brake.</b> Read down for what each part needs; read across for how settled it already was.'
        '<span class="src">Placed by chapter 2\'s figure brief and narrator (manuscript/rc2/30/02-the-factory-is-assembled.md); the talk, slides, site and player '
        'as map 2 of "How to read a map" places them; the agents, which the brief does not place, at the new edge where the team was made that day: our reading.</span>'
        '</figcaption>\n </figure>\n</section>\n')
    print('map.svg and pages.html written')


if __name__ == '__main__':
    main()
