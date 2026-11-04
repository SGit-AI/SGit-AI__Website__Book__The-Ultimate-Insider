"""The repository growing by the hour (the conductor's 026, for the editor's important concept on the repository, brief of
4 November 18): the talk's repository at the end of each clock hour of 29 October, its files by kind, one stacked bar per
hour, 00 to 18 (hours one to nineteen on the margin clock).

Every value is read at build from C124 (checked): each hour's files by kind (md, json, html, svg, js, css, other) and its
total, asserted to add up. Bytes are registered but not drawn. The caption carries C124's rule and its note: the bars follow
dev's first-parent line, so a late-merged branch makes an hour look quieter; hour 00 is the repository at its last commit of
that hour, hour 18 the day's last release, after the hold. No folder tree is drawn: C124 holds none. Text is escaped; the
drawing is checked with publishing/edition.py's own unsafe_svg, and the tool refuses itself if it would be refused.
Writes edition/repo-growth.svg only.
Usage: python3 -B -I tools/repo.py
"""
import importlib.util, json, sys
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
INK, MUTED, FILL2, PAPER = '#1f2933', '#5b6670', '#d5dce4', '#ffffff'
KINDS = [('html', '#b0481a'), ('md', '#1f2933'), ('json', '#5b6670'), ('js', '#8a6d1f'), ('css', '#c98b5e'),
         ('svg', '#7a93a8'), ('other', '#d5dce4')]
SANS = 'Inter, Helvetica, Arial, sans-serif'
PT = 9 * 25.4 / 72
SMALL = 7.5 * 25.4 / 72
TINY = 6.5 * 25.4 / 72
_spec = importlib.util.spec_from_file_location('edition', ROOT / 'publishing' / 'edition.py')
_edition = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_edition)
unsafe_svg = _edition.unsafe_svg


def t(x, y, s, size=PT, weight=400, fill=INK, anchor='start', style=''):
    st = f' font-style="{style}"' if style else ''
    return (f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{size:.3f}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}"{st}>{escape(str(s), quote=False)}</text>')


def main():
    reg = json.loads((ROOT / 'claims' / 'register.json').read_text())
    c = {x['id']: x for x in (reg['claims'] if isinstance(reg, dict) else reg)}['C124']
    assert c['state'] == 'checked'
    hours = c['value']['hours']
    assert [h['hour'] for h in hours] == [f'{i:02d}' for i in range(19)]
    for h in hours:
        assert sum(h['by_kind'].values()) == h['files'], h['hour']
        assert set(h['by_kind']) == {k for k, _ in KINDS}, h['hour']
    first, last = hours[0], hours[-1]
    peak = max(h['files'] for h in hours)
    W, H = 164.0, 92.0
    x0, x1, base, top = 6.0, 158.0, 66.0, 16.0
    step = (x1 - x0) / len(hours)
    bw = step * .7
    label = ('The talk\'s repository at the end of each hour of 29 October: its files by kind, stacked, '
             'one bar per hour from 00 to 18.')
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H:g}mm" viewBox="0 0 {W:g} {H:g}" role="img" '
         f'aria-label="{escape(label, quote=True)}">',
         t(x0, 6.0, 'The repository growing by the hour: its files by kind', PT * 1.1, 800, INK)]
    for i, h in enumerate(hours):
        x = x0 + i * step + (step - bw) / 2
        y = base
        for k, col in KINDS:
            n = h['by_kind'][k]
            hh = (base - top) * n / peak
            if hh > 0:
                s.append(f'<rect x="{x:.2f}" y="{y - hh:.2f}" width="{bw:.2f}" height="{hh:.2f}" fill="{col}"/>')
            y -= hh
        s.append(t(x + bw / 2, y - 1.2, h['files'], TINY, 700, INK, 'middle'))
        s.append(t(x + bw / 2, base + 3.6, h['hour'], TINY, 400, MUTED, 'middle'))
    s.append(f'<line x1="{x0:.2f}" y1="{base:.2f}" x2="{x1:.2f}" y2="{base:.2f}" stroke="{MUTED}" stroke-width=".3"/>')
    s.append(t((x0 + x1) / 2, base + 7.6, 'the clock hour of 29 October (hour one is 00:00 to 00:59); each bar the files at the hour\'s end', TINY, 400, MUTED, 'middle'))
    # the key
    kx, ky = x0, 11.0
    for k, col in KINDS:
        s.append(f'<rect x="{kx:.2f}" y="{ky - 2.2:.2f}" width="2.6" height="2.6" fill="{col}"/>')
        s.append(t(kx + 3.6, ky, k, TINY, 400, INK))
        kx += 4.0 + len(k) * 1.6 + 3.0
    s.append(t(kx + 1.0, ky, '(svg, js and css are a few files each: thin bands)', TINY, 400, MUTED, 'start', 'italic'))
    notes = [f'Hour 00 is the repository at its last commit of that hour, {first["commit_time"][:5]}; hour 18 is the day\'s last release, '
             f'{last["commit_time"][:5]}, after the hold.',
             'The bars follow dev\'s first-parent line: a branch merged late makes an hour look quieter than the work done in it.',
             '"Other" is everything else: images, text files, scripts, QR codes. Every value: the register, C124.']
    for j, n in enumerate(notes):
        s.append(t(x0, base + 13.0 + j * 3.4, n, TINY, 400, MUTED, 'start', 'italic' if j < 2 else ''))
    s.append('</svg>')
    svg = '\n'.join(s) + '\n'
    why = unsafe_svg(svg)
    if why:
        sys.exit(f"refused by the build's rule: {why}")
    (HERE / 'edition' / 'repo-growth.svg').write_text(svg)
    print('repo-growth.svg written')


if __name__ == '__main__':
    main()
