"""LAB 19 (ruv): one timeline, four modes (the editor's RC1 review, A12: timelines as reusable components, many modes).

One spec, the designer's lab/tools/components/examples/the-day.json (read in place; every event a registered time with
its claim id), drawn four ways:
  A  the designer's timeline component, horizontal (lab/tools/components/timeline.py, imported read only)
  B  the same component, vertical
  C  a 24-hour dial (this member's): the day as a clock face, night shaded, the events as ticks
  D  a day strip to scale with no break (this member's): midnight to 19:00, so the long quiet stretch shows
No number but the spec's registered times. Writes a.svg, b.svg, c.svg, d.svg and pages.html.
Usage: python3 -B -I tools/build.py   (-B: no bytecode written into the designer's folder)
"""
import importlib.util, json, math, sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parents[1]
LAB = HERE.parents[1]
COMP = LAB / 'tools' / 'components'
SPEC = json.loads((COMP / 'examples' / 'the-day.json').read_text())
INK, MUTED, FILL, FILL2, ACCENT, PAPER = '#1f2933', '#5b6670', '#eef2f6', '#d5dce4', '#b0481a', '#ffffff'
SANS = 'Inter, Helvetica, Arial, sans-serif'


def t(x, y, s, size=3.3, weight=400, fill=INK, anchor='start'):
    return f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'


def mins(hhmm):
    h, m = hhmm.split(':'); return int(h) * 60 + int(m)


def dial(spec, size=74):
    """The day as a 24-hour clock face: midnight at the top, night (00:00 to 06:00) shaded, each event a numbered tick,
    and a key under the dial (close events cannot carry labels on the ring)."""
    c, R = size / 2, size / 2 - 14
    n = len(spec['events'])
    H = size + 6 + n * 4.4
    def p(m, r):
        a = m / 1440 * 2 * math.pi - math.pi / 2
        return c + r * math.cos(a), c + r * math.sin(a)
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {H:.1f}" role="img" aria-label="{spec["alt"]}">']
    x0, y0 = p(0, R); x1, y1 = p(360, R)
    s.append(f'<path d="M{c} {c} L{x0:.2f} {y0:.2f} A{R} {R} 0 0 1 {x1:.2f} {y1:.2f} Z" fill="{FILL}"/>')
    s.append(f'<circle cx="{c}" cy="{c}" r="{R}" fill="none" stroke="{FILL2}" stroke-width=".8"/>')
    for h in range(0, 24, 6):
        x, y = p(h * 60, R - 5); s.append(t(x, y + 1.1, f'{h:02d}:00', 3.18, 400, MUTED, 'middle'))
    used = []
    for i, e in enumerate(spec['events'], 1):
        m = mins(e['t']); col = ACCENT if e.get('accent') else INK
        a, b = p(m, R - 1.8), p(m, R + 1.8)
        s.append(f'<line x1="{a[0]:.2f}" y1="{a[1]:.2f}" x2="{b[0]:.2f}" y2="{b[1]:.2f}" stroke="{col}" stroke-width=".8"/>')
        r = R + 4.6
        while any(abs(m - u) < 30 and abs(r - ur) < 2 for u, ur in used):
            r += 3.4                                                 # close events stack their numbers outwards
        used.append((m, r))
        x, y = p(m, r)
        s.append(t(x, y + 1.1, str(i), 3.18, 700, col, 'middle'))
        ky = size + 4 + (i - 1) * 4.4
        s.append(t(2, ky, f'{i}  {e["t"]} {e["label"]}', 3.18, 700 if e.get('accent') else 400, col))
    s.append('</svg>')
    return '\n'.join(s) + '\n'


def strip(spec, length=164, until=19 * 60):
    """Midnight to 19:00 to scale, no break: the quiet stretch takes the space it took."""
    k = length / until
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {length} 30" role="img" aria-label="{spec["alt"]}">']
    s.append(f'<rect x="0" y="12" width="{360 * k:.2f}" height="4" fill="{FILL}"/>')
    s.append(f'<line x1="0" y1="16" x2="{length}" y2="16" stroke="{INK}" stroke-width=".4"/>')
    for h in range(0, 20, 3):
        s.append(f'<line x1="{h * 60 * k:.2f}" y1="16" x2="{h * 60 * k:.2f}" y2="17.6" stroke="{MUTED}" stroke-width=".3"/>')
        s.append(t(min(h * 60 * k, length - .5), 21.5, f'{h:02d}:00', 3.18, 400, MUTED, 'middle' if 0 < h * 60 * k < length - 5 else ('start' if h == 0 else 'end')))
    for i, e in enumerate(spec['events']):
        x = mins(e['t']) * k; col = ACCENT if e.get('accent') else INK
        s.append(f'<circle cx="{x:.2f}" cy="16" r=".9" fill="{col}"/>')
        if e.get('accent') or i == 0:
            s.append(t(x, 9, e['t'] + ' ' + e['label'], 3.18, 700, col, 'start' if x < length / 2 else 'end'))
    s.append(t(0, 28.5, 'The afternoon\'s events crowd the right; each is labelled in modes A to C.', 3.18, 400, MUTED))
    s.append('</svg>')
    return '\n'.join(s) + '\n'


def main():
    spec = importlib.util.spec_from_file_location('timeline', COMP / 'timeline.py')
    tl = importlib.util.module_from_spec(spec); spec.loader.exec_module(tl)
    (HERE / 'a.svg').write_text(tl.render(SPEC, 'horizontal', 164))
    (HERE / 'b.svg').write_text(tl.render(SPEC, 'vertical', 90))
    (HERE / 'c.svg').write_text(dial(SPEC))
    (HERE / 'd.svg').write_text(strip(SPEC))
    claims = ' · '.join(sorted({e['claim'] for e in SPEC['events']}))

    def fig(svg, title, see, shows, w='100%'):
        return (f'  <figure class="fig" style="margin:0 0 4mm"><p class="fig-title">{title}</p>'
                f'<img src="{{{{dir}}}}/{svg}" alt="{title}: {SPEC["alt"]}" style="width:{w};display:block">'
                f'<figcaption><b>{see}</b><span class="src" style="font-family:var(--sans)">{shows}</span></figcaption></figure>\n')
    html = (f'<section class="page" data-claims="{claims}">\n'
            + fig('a.svg', 'A. Horizontal, with a break', 'The designer\'s component: the afternoon to scale, the night cut by a marked break.',
                  'Shows: the order and spacing of the afternoon. Hides: how long the quiet stretch was (the break is a fixed length).')
            + fig('d.svg', 'D. To scale, no break', 'Midnight to 19:00 as it passed.',
                  'Shows: the long quiet stretch, and how late the day\'s events crowd together. Hides: the labels, which do not fit.')
            + '</section>\n'
            f'<section class="page" data-claims="{claims}">\n'
            '  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm;align-items:start">\n'
            + fig('b.svg', 'B. Vertical', 'The same component, down the page: a margin or a column.',
                  'Shows: each event with room for its label. Hides: the day\'s shape, read top to bottom.')
            + fig('c.svg', 'C. A 24-hour dial', 'The day as a clock face, midnight at the top, night shaded.',
                  'Shows: where in the day things happened, at a glance. Hides: exact spacing between close events.')
            + '  </div>\n'
            '  <p style="font:400 9pt/12pt var(--sans);color:var(--muted);margin-top:3mm">One spec for all four: '
            '<span class="mono">lab/tools/components/examples/the-day.json</span> (the designer\'s, at <span class="mono">d965985</span>), '
            'every event a registered time with its claim id. A and B are the designer\'s timeline component; C and D are this experiment\'s own.</p>\n'
            '</section>\n')
    (HERE / 'pages.html').write_text(html)


if __name__ == '__main__':
    main()
