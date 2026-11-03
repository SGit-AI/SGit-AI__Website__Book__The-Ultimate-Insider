"""The full book's chapter 12 and the seventy's chapter 9, slot 3 (the designer's 115 gave it to ruv): a card of the
editor's eight afternoon asks, each with the time he asked and the time it was recorded.

Every time is read at build from C105 (checked): the asked time is the one written in the commit subject, the recorded time
is the commit's own, to the second, as the register holds it. The times on the card only, as the brief asks; no commit
hashes. The rows are worded as round-trip.svg words them, so the two figures of these asks agree. The 18:05 row was recorded
before the time in its subject; both are printed as the record has them, and a note says why. For the four conductor rows
the recorded time is the conductor recording and routing the ask, not the work landing (C105's note); the caption says so.
Text is escaped; the drawing is checked with publishing/edition.py's own unsafe_svg, and the tool refuses itself if it
would be refused. Writes edition/asks-card.svg only.
Usage: python3 -B -I tools/asks.py
"""
import importlib.util, json, sys
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


def t(x, y, s, size=PT, weight=400, fill=INK, anchor='start', style=''):
    st = f' font-style="{style}"' if style else ''
    return (f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{size:.3f}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}"{st}>{escape(str(s), quote=False)}</text>')


def main():
    reg = json.loads((ROOT / 'claims' / 'register.json').read_text())
    c = {x['id']: x for x in (reg['claims'] if isinstance(reg, dict) else reg)}['C105']
    assert c['state'] == 'checked'
    rows = c['value']['rows']
    assert len(rows) == c['value']['asks']
    early = [r for r in rows if r[2][:5] < r[0]]                     # recorded before the time in its subject
    W, x0, ty, rh = 164.0, 4.0, 18.0, 6.2
    cols = (x0, x0 + 30, x0 + 66)
    H = ty + 6 + rh * len(rows) + 11
    label = 'His eight afternoon asks: each with the time he asked and the time it was recorded.'
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H:.1f}mm" viewBox="0 0 {W:g} {H:.1f}" role="img" '
         f'aria-label="{escape(label, quote=True)}">',
         f'<rect x=".2" y=".2" width="{W - .4:.2f}" height="{H - .4:.2f}" rx="1.8" fill="{PAPER}" stroke="{FILL2}" stroke-width=".35"/>',
         t(x0, 8.0, 'His eight afternoon asks', PT * 1.15, 800, INK),
         t(cols[0], ty - 3.0, 'asked', SMALL, 700, MUTED),
         t(cols[1], ty - 3.0, 'recorded', SMALL, 700, MUTED),
         t(cols[2], ty - 3.0, 'what came back', SMALL, 700, MUTED),
         f'<line x1="{x0}" y1="{ty - 1.6:.2f}" x2="{W - x0}" y2="{ty - 1.6:.2f}" stroke="{FILL2}" stroke-width=".3"/>']
    for i, (asked, _, recorded, kind) in enumerate(rows):
        y = ty + 3.4 + i * rh
        mark = (asked, recorded) in [(e[0], e[2]) for e in early]
        if mark:
            s.append(f'<rect x="{x0 - 1.4:.2f}" y="{y - 4.2:.2f}" width="{W - 2 * x0 + 2.8:.2f}" height="{rh - .6:.2f}" fill="{FILL}"/>')
        s.append(t(cols[0], y, asked, PT, 700, ACCENT if mark else INK))
        s.append(t(cols[1], y, recorded, PT, 400, ACCENT if mark else INK))
        s.append(t(cols[2], y, 'routed by the conductor' if kind == 'conductor routes' else 'a player fix', PT, 400, MUTED))
        if mark:
            s.append(t(W - x0, y, 'recorded before its subject\'s time', SMALL, 400, ACCENT, 'end', 'italic'))
    ny = ty + 3.4 + len(rows) * rh + 1.6
    s.append(t(x0, ny, '"Asked" is the time written in the commit\'s subject, not a clock; "recorded" is the commit\'s own time.', SMALL, 400, MUTED, 'start', 'italic'))
    s.append(t(x0, ny + 3.6, 'For the conductor\'s rows, the recorded time is the conductor routing the ask, not the work landing.', SMALL, 400, MUTED, 'start', 'italic'))
    s.append(t(x0, ny + 7.2, 'Every time: the register, C105.', SMALL, 400, MUTED))
    s.append('</svg>')
    svg = '\n'.join(s) + '\n'
    why = unsafe_svg(svg)
    if why:
        sys.exit(f"refused by the build's rule: {why}")
    (HERE / 'edition' / 'asks-card.svg').write_text(svg)
    print('asks-card.svg written')


if __name__ == '__main__':
    main()
