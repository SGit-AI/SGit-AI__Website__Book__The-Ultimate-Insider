"""The full book's chapter 2 (the conductor's 028, from the editor's brief of 4 November): the round trip's clock half alone,
the last afternoon ask drawn to the clock, without the old table of asks. The asks are carried by the asks card (asks.py).

Written to its own file, edition/round-trip-clock.svg, so round-trip.svg (placed elsewhere with its table) is left as it is.
Every time is read at build from the register: C105 (the ask and the commit that answered it) and C006 (the hold). Only
18:25, 18:37 and 18:44 are labelled; the ticks are unlabelled. Text is escaped; the drawing is checked with
publishing/edition.py's own unsafe_svg, and the tool refuses itself if it would be refused.
Usage: python3 -B -I tools/roundclock.py
"""
import importlib.util, json, re, sys
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
INK, MUTED, FILL, FILL2, ACCENT, PAPER = '#1f2933', '#5b6670', '#eef2f6', '#d5dce4', '#b0481a', '#ffffff'
SANS = 'Inter, Helvetica, Arial, sans-serif'
PT = 9 * 25.4 / 72
SMALL = 7.5 * 25.4 / 72
_spec = importlib.util.spec_from_file_location('edition', ROOT / 'publishing' / 'edition.py')
_edition = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_edition)
unsafe_svg = _edition.unsafe_svg


def t(x, y, s, weight=400, fill=INK, anchor='start', size=PT, style=''):
    st = f' font-style="{style}"' if style else ''
    return (f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{size:.3f}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}"{st}>{escape(str(s), quote=False)}</text>')


def mins(hhmm):
    h, m = hhmm.split(':')[:2]
    return int(h) * 60 + int(m)


def main():
    reg = json.loads((ROOT / 'claims' / 'register.json').read_text())
    c = {x['id']: x for x in (reg['claims'] if isinstance(reg, dict) else reg)}
    assert c['C105']['state'] == 'checked' and c['C006']['state'] == 'checked'
    last = c['C105']['value']['rows'][-1]
    asked, commit, back = last[0], last[1], last[2][:5]
    hold = c['C006']['value'][:5]
    hold_commit = re.search(r'\b([0-9a-f]{7})\b', c['C006']['value']).group(1)
    W, H = 164.0, 50.0
    label = ('One ask\'s round trip drawn to the clock: the editor\'s ask, the commit that answered it, '
             'and the hold at the edge of the picture.')
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H:g}mm" viewBox="0 0 {W:g} {H:g}" role="img" '
         f'aria-label="{escape(label, quote=True)}">',
         t(4, 7.0, 'One ask, drawn to the clock', 700, INK)]
    x0, x1, ly = 8.0, 150.0, 30.0
    m0, m1 = mins(asked) - 5, mins(hold)
    X = lambda m: x0 + (x1 - x0) * (m - m0) / (m1 - m0)
    s.append(f'<line x1="{x0}" y1="{ly}" x2="{x1}" y2="{ly}" stroke="{MUTED}" stroke-width=".35"/>')
    for m in range(m0, m1 + 1):
        if m % 5 == 0 or m == m0:
            s.append(f'<line x1="{X(m):.2f}" y1="{ly - 1:.2f}" x2="{X(m):.2f}" y2="{ly + 1:.2f}" stroke="{MUTED}" stroke-width=".25"/>')
    xa, xb, xh = X(mins(asked)), X(mins(back)), X(mins(hold))
    s.append(f'<path d="M{xa:.2f} {ly:.2f} C{xa + 8:.2f} {ly - 20:.2f} {xb - 8:.2f} {ly - 20:.2f} {xb:.2f} {ly:.2f}" '
             f'fill="none" stroke="{ACCENT}" stroke-width=".6"/>')
    s.append(f'<path d="M{xb - 2.2:.2f} {ly - 2.8:.2f} L{xb:.2f} {ly:.2f} L{xb + .4:.2f} {ly - 3.4:.2f}" fill="none" stroke="{ACCENT}" stroke-width=".6"/>')
    for x in (xa, xb):
        s.append(f'<circle cx="{x:.2f}" cy="{ly:.2f}" r="1.5" fill="{ACCENT}"/>')
    s.append(t(xa, ly + 6.0, asked, 700, INK, 'middle'))
    s.append(t(xa, ly + 10.2, 'his ask', 400, MUTED, 'middle', SMALL))
    s.append(t(xb, ly + 6.0, back, 700, INK, 'middle'))
    s.append(t(xb, ly + 10.2, f'the commit that answered it ({commit})', 400, MUTED, 'middle', SMALL))
    s.append(t((xa + xb) / 2, ly - 17.0, 'the round trip', 400, ACCENT, 'middle', SMALL, 'italic'))
    s.append(f'<line x1="{xh:.2f}" y1="{ly - 22:.2f}" x2="{xh:.2f}" y2="{ly + 4:.2f}" stroke="{INK}" stroke-width=".6" stroke-dasharray="1.2 .8"/>')
    s.append(t(xh - 1.5, ly - 19.0, hold, 700, INK, 'end'))
    s.append(t(xh - 1.5, ly - 15.4, f'the hold ({hold_commit})', 400, MUTED, 'end', SMALL))
    s.append(t(4, H - 2.4, 'Times: the register, C105 (the ask) and C006 (the hold).', 400, MUTED, 'start', SMALL))
    s.append('</svg>')
    svg = '\n'.join(s) + '\n'
    why = unsafe_svg(svg)
    if why:
        sys.exit(f"refused by the build's rule: {why}")
    (HERE / 'edition' / 'round-trip-clock.svg').write_text(svg)
    print('round-trip-clock.svg written')


if __name__ == '__main__':
    main()
