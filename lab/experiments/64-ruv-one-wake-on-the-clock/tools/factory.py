"""The full book's chapter 2, "What a factory is" (the conductor's 025, from the editor's brief of 4 November): the factory's
hour as a clock face, every member's turn at its own minute past the hour, the turn passing round the face.

The minutes are C071's (checked): the schedule as it stood at the end of the day. It records slots, not wakes run, and no
hand-over of work: work passed by request and mail, answered at the recipient's own slot. So the face carries one rotation
round the hour, the turn passing from slot to slot, and no arrow from member to member. The note says the schedule ran every
hour and that members joined it through the day, with no times. No number but C071's minutes. Text is escaped; the drawing is
checked with publishing/edition.py's own unsafe_svg, and the tool refuses itself if it would be refused. Writes
edition/factory-clock.svg only.
Usage: python3 -B -I tools/factory.py
"""
import importlib.util, json, math, sys
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


def pol(cx, cy, r, minute):
    a = 2 * math.pi * minute / 60 - math.pi / 2
    return cx + r * math.cos(a), cy + r * math.sin(a), a


def main():
    reg = json.loads((ROOT / 'claims' / 'register.json').read_text())
    c = {x['id']: x for x in (reg['claims'] if isinstance(reg, dict) else reg)}['C071']
    assert c['state'] == 'checked'
    slots = sorted(((int(v.strip(':')), m) for m, v in c['value'].items()))
    W, H = 164.0, 92.0
    SHIFT = 10.0
    cx, cy, R = 60.0, 47.0, 30.0
    label = ('The factory\'s hour as a clock face: each member\'s turn at its own minute past the hour, '
             'the turn passing round the face, every hour of the day.')
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H - SHIFT:g}mm" viewBox="0 0 {W:g} {H - SHIFT:g}" role="img" '
         f'aria-label="{escape(label, quote=True)}">',
         f'<g transform="translate(0,-{SHIFT})">',                   # no drawn title: the Figure line is the caption (26)
         f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{FILL}" stroke="{FILL2}" stroke-width=".4"/>']
    for m in range(60):
        x0, y0, _ = pol(cx, cy, R - (2.6 if m % 15 == 0 else 1.2), m)
        x1, y1, _ = pol(cx, cy, R, m)
        s.append(f'<line x1="{x0:.2f}" y1="{y0:.2f}" x2="{x1:.2f}" y2="{y1:.2f}" stroke="{MUTED}" '
                 f'stroke-width="{.35 if m % 15 == 0 else .18}"/>')
    # one rotation round the face, inside the dots: the turn passing round the hour
    rr = R - 8.0
    x0, y0, _ = pol(cx, cy, rr, 3)
    x1, y1, a1 = pol(cx, cy, rr, 55)
    s.append(f'<path d="M{x0:.2f} {y0:.2f} A{rr} {rr} 0 1 1 {x1:.2f} {y1:.2f}" fill="none" stroke="{ACCENT}" '
             f'stroke-width=".6" stroke-dasharray="1.6 1"/>')
    tx, ty = -math.sin(a1), math.cos(a1)                              # clockwise tangent at the arc's end
    nx, ny = math.cos(a1), math.sin(a1)
    s.append(f'<path d="M{x1 - 2.2 * tx + 1.2 * nx:.2f} {y1 - 2.2 * ty + 1.2 * ny:.2f} L{x1 + .4 * tx:.2f} {y1 + .4 * ty:.2f} '
             f'L{x1 - 2.2 * tx - 1.2 * nx:.2f} {y1 - 2.2 * ty - 1.2 * ny:.2f}" fill="none" stroke="{ACCENT}" stroke-width=".6"/>')
    s.append(t(cx, cy - 1.2, 'one hour,', 400, MUTED, 'middle', SMALL, 'italic'))
    s.append(t(cx, cy + 2.8, 'the turn going round', 400, MUTED, 'middle', SMALL, 'italic'))
    for minute, name in slots:
        x, y, a = pol(cx, cy, R - 4.0, minute)
        s.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="1.6" fill="{INK}"/>')
        lx, ly, _ = pol(cx, cy, R + 3.2, minute)
        anchor = 'start' if math.cos(a) > .2 else ('end' if math.cos(a) < -.2 else 'middle')
        if anchor == 'middle':
            ly += 2.2 if math.sin(a) > 0 else -.4
        else:
            ly += 1.1
        s.append(t(lx, ly, f'{name} :{minute:02d}', 400, INK, anchor, SMALL))
    # the words beside the face
    nx0 = 112.0
    lines = ['Every member had its own', 'minute past the hour, so', 'the hour went round the', 'team in turn, and then',
             'began again.']
    for i, ln in enumerate(lines):
        s.append(t(nx0, 30.0 + i * 4.6, ln, 400, INK, 'start', SMALL))
    s.append(t(nx0, 30.0 + len(lines) * 4.6 + 3.0, 'Work did not pass round the', 400, MUTED, 'start', SMALL, 'italic'))
    s.append(t(nx0, 30.0 + len(lines) * 4.6 + 6.6, 'face: it went by letter,', 400, MUTED, 'start', SMALL, 'italic'))
    s.append(t(nx0, 30.0 + len(lines) * 4.6 + 10.2, 'read at the next turn.', 400, MUTED, 'start', SMALL, 'italic'))
    s.append(t(2, H - 5.4, 'The schedule as it stood at the end of the day (C071); it ran every hour, and members joined it', 400, MUTED, 'start', SMALL))
    s.append(t(2, H - 1.8, 'through the day. Each dot is a slot on the schedule, not a wake that ran.', 400, MUTED, 'start', SMALL))
    s.append('</g>')
    s.append('</svg>')
    svg = '\n'.join(s) + '\n'
    why = unsafe_svg(svg)
    if why:
        sys.exit(f"refused by the build's rule: {why}")
    (HERE / 'edition' / 'factory-clock.svg').write_text(svg)
    print('factory-clock.svg written')


if __name__ == '__main__':
    main()
