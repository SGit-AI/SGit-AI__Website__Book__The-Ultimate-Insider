"""The seventy's chapter 1 and the full book's chapter 2 (the designer's 110 gave it to ruv): one ask's round trip drawn to
the clock, with the eight afternoon asks beside it as a small table.

Every time is read at build from the register: C105 (the asks, each with the time written in its commit subject and the
commit's own time) and C006 (the hold). Only 18:25, 18:37 and 18:44 are labelled on the line of time; its ticks are
unlabelled. The asked time is what a member wrote in the subject, not a clock (C105's note), and the four conductor rows are
the conductor routing the ask, not the work landing; the table says both. Pure vector: no image, href, script or handler;
the tool refuses itself if publishing/edition.py's rule would match. Writes edition/round-trip.svg only.
Usage: python3 -B -I tools/roundtrip.py
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
INK, MUTED, FILL, FILL2, ACCENT, PAPER, AMBER = '#1f2933', '#5b6670', '#eef2f6', '#d5dce4', '#b0481a', '#ffffff', '#8a6d1f'
SANS = 'Inter, Helvetica, Arial, sans-serif'
PT = 9 * 25.4 / 72
SMALL = 7.5 * 25.4 / 72
UNSAFE = re.compile(r"<script|<foreignObject|\bhref\s*=|\bon[a-z]+\s*=|@import", re.I)


def t(x, y, s, weight=400, fill=INK, anchor='start', size=PT, style=''):
    st = f' font-style="{style}"' if style else ''
    return (f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{size:.3f}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}"{st}>{s}</text>')


def mins(hhmm):
    h, m = hhmm.split(':')[:2]
    return int(h) * 60 + int(m)


def main():
    reg = json.loads((ROOT / 'claims' / 'register.json').read_text())
    c = {x['id']: x for x in (reg['claims'] if isinstance(reg, dict) else reg)}
    assert c['C105']['state'] == 'checked' and c['C006']['state'] == 'checked'
    rows = c['C105']['value']['rows']
    assert len(rows) == c['C105']['value']['asks']
    last = rows[-1]
    asked, commit, back = last[0], last[1], last[2][:5]                 # the round trip: the last ask
    hold = c['C006']['value'][:5]
    hold_commit = re.search(r'\b([0-9a-f]{7})\b', c['C006']['value']).group(1)
    W, H = 164.0, 62.0
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H:g}mm" viewBox="0 0 {W:g} {H:g}" role="img" '
         'aria-label="One ask\'s round trip drawn to the clock: the editor\'s ask, the commit that answered it, and the hold at '
         'the edge of the picture; beside it, his afternoon asks with the time each was asked and the time each came back.">']
    # the line of time, from a few minutes before the ask to the hold at the right edge
    x0, x1, ly = 4.0, 88.0, 34.0
    m0, m1 = mins(asked) - 5, mins(hold)
    X = lambda m: x0 + (x1 - x0) * (m - m0) / (m1 - m0)
    s.append(f'<line x1="{x0}" y1="{ly}" x2="{x1}" y2="{ly}" stroke="{MUTED}" stroke-width=".35"/>')
    for m in range(m0, m1 + 1):
        if m % 5 == 0 or m == m0:
            s.append(f'<line x1="{X(m):.2f}" y1="{ly - 1:.2f}" x2="{X(m):.2f}" y2="{ly + 1:.2f}" stroke="{MUTED}" stroke-width=".25"/>')
    xa, xb, xh = X(mins(asked)), X(mins(back)), X(mins(hold))
    s.append(f'<path d="M{xa:.2f} {ly:.2f} C{xa + 4:.2f} {ly - 17:.2f} {xb - 4:.2f} {ly - 17:.2f} {xb:.2f} {ly:.2f}" '
             f'fill="none" stroke="{ACCENT}" stroke-width=".5"/>')
    s.append(f'<path d="M{xb - 1.6:.2f} {ly - 2.6:.2f} L{xb:.2f} {ly:.2f} L{xb + .6:.2f} {ly - 3:.2f}" fill="none" stroke="{ACCENT}" stroke-width=".5"/>')
    for x in (xa, xb):
        s.append(f'<circle cx="{x:.2f}" cy="{ly:.2f}" r="1.3" fill="{ACCENT}"/>')
    s.append(t(xa, ly + 5.5, asked, 700, INK, 'middle'))
    s.append(t(xa, ly + 9.6, 'his ask', 400, MUTED, 'middle', SMALL))
    s.append(t(xb, ly + 5.5, back, 700, INK, 'middle'))
    s.append(t(xb, ly + 9.6, f'the commit that', 400, MUTED, 'middle', SMALL))
    s.append(t(xb, ly + 12.8, f'answered it ({commit})', 400, MUTED, 'middle', SMALL))
    s.append(t((xa + xb) / 2, ly - 15.5, 'the round trip', 400, ACCENT, 'middle', SMALL, 'italic'))
    s.append(f'<line x1="{xh:.2f}" y1="{ly - 22:.2f}" x2="{xh:.2f}" y2="{ly + 4:.2f}" stroke="{INK}" stroke-width=".6" stroke-dasharray="1.2 .8"/>')
    s.append(t(xh - 1.5, ly - 19.0, hold, 700, INK, 'end'))
    s.append(t(xh - 1.5, ly - 15.4, f'the hold ({hold_commit})', 400, MUTED, 'end', SMALL))
    s.append(t(x0, 7.0, 'One ask, drawn to the clock', 700, INK))
    # the table of asks
    tx, ty, rh = 97.0, 7.0, 4.4
    s.append(t(tx, ty, 'His afternoon asks', 700, INK))
    s.append(t(tx, ty + 5.0, 'asked', 400, MUTED, 'start', SMALL))
    s.append(t(tx + 13, ty + 5.0, 'back', 400, MUTED, 'start', SMALL))
    s.append(t(tx + 25, ty + 5.0, 'what came back', 400, MUTED, 'start', SMALL))
    s.append(f'<line x1="{tx}" y1="{ty + 6.6:.2f}" x2="{W - 1:.2f}" y2="{ty + 6.6:.2f}" stroke="{FILL2}" stroke-width=".3"/>')
    for i, (a, _, b, kind) in enumerate(rows):
        y = ty + 11.0 + i * rh
        lit = i == len(rows) - 1
        if lit:
            s.append(f'<rect x="{tx - 1:.2f}" y="{y - 3.4:.2f}" width="{W - tx:.2f}" height="4.2" fill="{FILL}"/>')
        col = ACCENT if lit else INK
        s.append(t(tx, y, a, 700 if lit else 400, col, 'start', SMALL))
        s.append(t(tx + 13, y, b[:5], 700 if lit else 400, col, 'start', SMALL))
        s.append(t(tx + 25, y, 'routed by the conductor' if kind == 'conductor routes' else 'a player fix', 400, MUTED, 'start', SMALL))
    ny = ty + 11.0 + len(rows) * rh + 1.0
    s.append(t(tx, ny, '"Asked" is the time written in the commit,', 400, MUTED, 'start', SMALL, 'italic'))
    s.append(t(tx, ny + 3.4, 'not a clock: one came back before it.', 400, MUTED, 'start', SMALL, 'italic'))
    s.append(t(x0, H - 2.4, 'Times: the register, C105 (the asks) and C006 (the hold).', 400, MUTED, 'start', SMALL))
    s.append('</svg>')
    svg = '\n'.join(s) + '\n'
    if UNSAFE.search(svg):
        sys.exit("refused by the build's rule")
    (HERE / 'edition').mkdir(exist_ok=True)
    (HERE / 'edition' / 'round-trip.svg').write_text(svg)
    print('round-trip.svg written')


if __name__ == '__main__':
    main()
