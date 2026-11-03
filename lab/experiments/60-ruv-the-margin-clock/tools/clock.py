"""The margin clock (ruv), for RC2 (the editor, 3 November: "a clock on the right ... hour one, hour two, hour three ... some
stats that you can show to give a sense of time passing"; the storyteller's outline, "The clock in the margin, and what to show").

Hours are the clock hours of 29 October: hour one is 00:00 to 00:59, the hold at 18:44 falls in hour nineteen. The only stat is
commits that hour, read at build from C095's "all" row (claims/talk-commits-by-member-hour.md, checked). Wakes (C087) are left
out because the register gives 05 to 13 UTC (hours six to fourteen) as a range; the cast on stage is left out because C095
counts only "@member" subjects and C011 is open.

Two forms, for the designer and the publisher to choose:
  float  one box per hour inside the text column (the outer margin is 9.5 mm, too narrow for 9 pt stats): the hour in words,
         its clock span, a nineteen-bar line of commits per hour with this hour lit, and this hour's commits
  edge   a thin ladder for the margin itself: nineteen ticks down the page edge, this hour lit, its name turned along the edge
Writes edition/clock-HH.svg and edition/edge-HH.svg for hours one to nineteen, and pages.html (the lab sheet).
Usage: python3 -B -I tools/clock.py
"""
import json, re
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
INK, MUTED, FILL, FILL2, ACCENT, PAPER = '#1f2933', '#5b6670', '#eef2f6', '#d5dce4', '#b0481a', '#ffffff'
SANS = 'Inter, Helvetica, Arial, sans-serif'
PT9 = 9 * 25.4 / 72
WORDS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
         'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']


def commits_by_hour():
    reg = json.loads((ROOT / 'claims' / 'register.json').read_text())
    c = {x['id']: x for x in (reg['claims'] if isinstance(reg, dict) else reg)}['C095']
    assert c['state'] == 'checked'
    row = next(l for l in (ROOT / 'claims' / 'talk-commits-by-member-hour.md').read_text().splitlines() if l.startswith('| **all**'))
    cells = [x.strip() for x in row.strip('|').split('|')][1:]
    vals = [int(x) for x in cells[:19]]
    assert sum(vals) == int(cells[19]) == c['value']['non_merge_commits']
    return vals


def t(x, y, s, size=PT9, weight=400, fill=INK, anchor='start', extra=''):
    return f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{size:.3f}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{extra}>{s}</text>'


def float_box(h, vals):
    W, H = 38.0, 30.0
    peak = max(vals)
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H:g}mm" viewBox="0 0 {W:g} {H:g}" role="img" '
         f'aria-label="The clock: hour {WORDS[h]} of the day, and the commits each hour, this hour lit.">',
         f'<rect x=".2" y=".2" width="{W - .4:.2f}" height="{H - .4:.2f}" rx="1.6" fill="{PAPER}" stroke="{FILL2}" stroke-width=".3"/>',
         t(2, 5.2, 'HOUR', PT9, 700, MUTED, extra=' letter-spacing=".4"'),
         t(2, 10.6, WORDS[h], 13 * 25.4 / 72, 800, ACCENT),
         t(W - 2, 5.2, f'{h:02d}:00 to {h:02d}:59', PT9, 400, MUTED, 'end')]
    bw, x0, base, top = (W - 4) / 19, 2.0, 21.0, 12.6
    for i, v in enumerate(vals):
        bh = (base - top) * v / peak
        s.append(f'<rect x="{x0 + i * bw + .15:.2f}" y="{base - bh:.2f}" width="{bw - .3:.2f}" height="{bh:.2f}" fill="{ACCENT if i == h else FILL2}"/>')
    s.append(f'<line x1="{x0:.2f}" y1="{base:.2f}" x2="{W - 2:.2f}" y2="{base:.2f}" stroke="{MUTED}" stroke-width=".25"/>')
    s.append(t(2, 26.6, f'{vals[h]} commits this hour', PT9, 700, INK))
    s.append('</svg>')
    return '\n'.join(s) + '\n'


SPANS = [(1, 2), (2, 3), (2, 5), (5, 11), (5, 14), (14, 19), (15, 16)]   # every span the thirty's Clock lines use (publisher__005)


def span_box(a, b, vals):
    """A span: its hours lit together and named in words; no commit count, since a sum is not in the register."""
    W, H = 38.0, 30.0
    peak = max(vals)
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H:g}mm" viewBox="0 0 {W:g} {H:g}" role="img" '
         f'aria-label="The clock: hours {WORDS[a - 1]} to {WORDS[b - 1]} of the day, and the commits each hour, those hours lit.">',
         f'<rect x=".2" y=".2" width="{W - .4:.2f}" height="{H - .4:.2f}" rx="1.6" fill="{PAPER}" stroke="{FILL2}" stroke-width=".3"/>',
         t(2, 5.2, f'{a - 1:02d}:00 to {b - 1:02d}:59', PT9, 400, MUTED),
         t(2, 10.6, f'{WORDS[a - 1]} to {WORDS[b - 1]}', PT9 * 1.08, 800, ACCENT)]
    bw, x0, base, top = (W - 4) / 19, 2.0, 21.0, 12.6
    for i, v in enumerate(vals):
        bh = (base - top) * v / peak
        s.append(f'<rect x="{x0 + i * bw + .15:.2f}" y="{base - bh:.2f}" width="{bw - .3:.2f}" height="{bh:.2f}" fill="{ACCENT if a - 1 <= i <= b - 1 else FILL2}"/>')
    s.append(f'<line x1="{x0:.2f}" y1="{base:.2f}" x2="{W - 2:.2f}" y2="{base:.2f}" stroke="{MUTED}" stroke-width=".25"/>')
    s.append(t(2, 26.6, 'these hours lit', PT9, 400, MUTED))
    s.append('</svg>')
    return '\n'.join(s) + '\n'


def edge(h):
    W, H = 8.0, 120.0
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H:g}mm" viewBox="0 0 {W:g} {H:g}" role="img" '
         f'aria-label="The clock along the page edge: hour {WORDS[h]} of the day.">']
    step = (H - 40) / 18
    for i in range(19):
        y = 4 + i * step
        s.append(f'<line x1="{W - (5 if i == h else 2.2):.2f}" y1="{y:.2f}" x2="{W:.2f}" y2="{y:.2f}" stroke="{ACCENT if i == h else FILL2}" stroke-width="{.9 if i == h else .35}"/>')
    yl = 4 + 18 * step + 6
    s.append(t(W - 2.6, yl, f'hour {WORDS[h]}', PT9, 700, ACCENT, 'start', f' transform="rotate(90 {W - 2.6:.2f} {yl:.2f})"'))
    s.append('</svg>')
    return '\n'.join(s) + '\n'


def main():
    vals = commits_by_hour()
    for h in range(19):
        (HERE / 'edition' / f'clock-{h + 1:02d}.svg').write_text(float_box(h, vals))
        (HERE / 'edition' / f'edge-{h + 1:02d}.svg').write_text(edge(h))
    for a, b in SPANS:
        (HERE / 'edition' / f'clock-{a:02d}-{b:02d}.svg').write_text(span_box(a, b, vals))
    show = [0, 4, 15, 18]                                          # hours one, five, sixteen, nineteen: the outline's scenes
    boxes = ''.join(f'<img src="{{{{dir}}}}/edition/clock-{h + 1:02d}.svg" alt="The clock at hour {WORDS[h]}" style="width:38mm;display:block">' for h in show)
    edges = ''.join(f'<img src="{{{{dir}}}}/edition/edge-{h + 1:02d}.svg" alt="The edge clock at hour {WORDS[h]}" style="width:8mm;height:120mm;display:block">' for h in show)
    (HERE / 'pages.html').write_text(
        '<section class="page" data-claims="C095">\n <figure class="fig span12">\n'
        '  <p class="fig-title">The clock: a float box in the column</p>\n'
        f'  <div style="display:flex;justify-content:space-between">{boxes}</div>\n'
        '  <figcaption><b>Hour one, five, sixteen and nineteen: the empty project, the argument with a reviewer, the player arriving, the hold. '
        'The bars are the day\'s commits hour by hour, this hour lit; the reader feels the pace without a sentence about it.</b>'
        '<span class="src">Commits that hour: C095, the "all" row of claims/talk-commits-by-member-hour.md, read at build. Wakes (C087) and the cast on stage '
        '(C011) are left out until the register gives them by the hour.</span></figcaption>\n </figure>\n</section>\n'
        '<section class="page" data-claims="">\n <figure class="fig span12">\n  <p class="fig-title">Or the clock along the page edge</p>\n'
        f'  <div style="display:flex;gap:16mm;justify-content:center">{edges}</div>\n'
        '  <figcaption><b>The same hours as a thin ladder for the outer margin itself: nineteen ticks, this hour lit and named along the edge. '
        'It fits the 9.5 mm margin; it carries no stats.</b><span class="src">Files for every hour in edition/: clock-01.svg to clock-19.svg, '
        'edge-01.svg to edge-19.svg.</span></figcaption>\n </figure>\n</section>\n')
    print('nineteen hours written in both forms; pages.html')


if __name__ == '__main__':
    main()
