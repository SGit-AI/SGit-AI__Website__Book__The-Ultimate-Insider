"""LAB 14 (ruv): a fractal Wardley map, as three frames (the editor's RC1 review, T10: "a dot that becomes the next map").

Composed from the illustrator's RC1 map images (team/conductor/rc1/resources/images/maps/, read only, at 42f0b94):
  frame 1  map 05, the day as a value chain, with one dot ringed: "Tools written on the day"
  frame 2  the lens: that dot opening into map 06, the plumbing under the day
  frame 3  map 06, whole
No label is added to the maps but the ring; every word and number on them is the maps' own.
Writes frames/*.png and pages.html. Usage: python3 -I tools/build.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

HERE = Path(__file__).resolve().parents[1]
MAPS = HERE.parents[2] / 'team' / 'conductor' / 'rc1' / 'resources' / 'images' / 'maps'
ACCENT, MUTED = (176, 72, 26), (91, 102, 112)
DOT = (422, 1068)                                                # "Tools written on the day" on map 05, in its own pixels
RING = 46


def ring(d, c, r, w=8, fill=ACCENT):
    d.ellipse((c[0] - r, c[1] - r, c[0] + r, c[1] + r), outline=fill, width=w)


def main():
    m5 = Image.open(MAPS / '05-the-day-as-a-value-chain.png').convert('RGB')
    m6 = Image.open(MAPS / '06-the-plumbing-under-the-day.png').convert('RGB')
    f1 = m5.copy(); ring(ImageDraw.Draw(f1), DOT, RING)
    f1.save(HERE / 'frames' / 'f1-map05-dot.png', optimize=True)

    # the lens: map 05 faded, the ringed dot, and a large circle holding map 06, joined by two tangent lines
    f2 = Image.blend(m5, Image.new('RGB', m5.size, 'white'), .72)
    R, C = 600, (m5.width - 640, m5.height // 2 + 80)            # the lens, right of the dot
    side = 2 * R
    m6s = m6.resize((round(m6.width * side / m6.height), side), Image.LANCZOS)
    tile = Image.new('RGB', (side, side), 'white')
    tile.paste(m6s, ((side - m6s.width) // 2, 0))
    mask = Image.new('L', (side, side), 0); ImageDraw.Draw(mask).ellipse((0, 0, side - 1, side - 1), fill=255)
    f2.paste(tile, (C[0] - R, C[1] - R), mask)
    d = ImageDraw.Draw(f2)
    for sgn in (-1, 1):                                          # lines from the small ring's edge to the lens's edge
        d.line((DOT[0], DOT[1] + sgn * RING, C[0] - R * .2, C[1] + sgn * R * .98), fill=MUTED, width=4)
    ring(d, DOT, RING); ring(d, C, R, 10)
    f2.save(HERE / 'frames' / 'f2-lens.png', optimize=True)

    m6.save(HERE / 'frames' / 'f3-map06.png', optimize=True)

    def fig(img, w, t, words, see):
        return (f'  <figure class="fig" style="margin:0 0 5mm"><img src="{{{{dir}}}}/frames/{img}" alt="{words}" '
                f'style="width:{w}mm;display:block;border:.3mm solid var(--fill-2)">'
                f'<figcaption><b>{t}</b> &nbsp; {words}<span class="src" style="font-family:var(--sans)">{see}</span></figcaption></figure>\n')
    src = ('<p style="font:400 9pt/12pt var(--sans);color:var(--muted);margin-top:2mm">The maps are the illustrator\'s for RC1, unchanged but '
           'for the ring and the lens: <span class="mono">team/conductor/rc1/maps/05-the-day-as-a-value-chain.json</span> and '
           '<span class="mono">06-the-plumbing-under-the-day.json</span>, images at <span class="mono">42f0b94</span>. '
           'Positions are readings of the record, not measurements, as the maps themselves say.</p>\n')
    html = ('<section class="page" data-claims="">\n'
            + fig('f1-map05-dot.png', 114, '1', 'The day, as one value chain. Pick one dot: the tools written on the day.',
                  'Every dot on a map is a whole map of its own, if you look closely enough.')
            + '</section>\n<section class="page" data-claims="">\n'
            + fig('f2-lens.png', 140, '2', 'Look into the dot.',
                  'The dot opens into the plumbing under the day: what the editor brought, what was written on the day, and what was rented.')
            + '</section>\n<section class="page" data-claims="">\n'
            + fig('f3-map06.png', 120, '3', 'The dot was a map all along.',
                  'Map 6: the plumbing under the day. Each of its dots could open again.')
            + src + '</section>\n')
    (HERE / 'pages.html').write_text(html)


if __name__ == '__main__':
    main()
