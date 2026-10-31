"""LAB 20 (ruv): the locks that never closed, for chapter 8 (the editor's RC1 review, note 9: experiments in each chapter).

The evening as one line, to scale, from checked claims only:
  C027  the lock tool landed at 17:54; locks planned for 18:30, 19:30 and 20:00; none closed
  C006  the hold, 18:44:13, at the editor's word (usage near its limit); every member's next wake stopped
  C005  the last release, 18:46: work already in flight still landed
Above the line, what happened; below it, the three planned locks as open padlocks. The axis is labelled on the hour only.
Writes locks.svg and pages.html. Usage: python3 -B -I tools/build.py
"""
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
INK, MUTED, FILL, FILL2, ACCENT, TINT, PAPER = '#1f2933', '#5b6670', '#eef2f6', '#d5dce4', '#b0481a', '#f6e1d4', '#ffffff'
SANS = 'Inter, Helvetica, Arial, sans-serif'
W, H, Y = 164, 104, 44                                           # mm; Y is the axis
T0, T1 = 17 * 60 + 45, 20 * 60 + 8                               # the axis runs a little either side of the events


def x(m):
    return 4 + (m - T0) / (T1 - T0) * (W - 8)


def hm(s):
    h, m = s.split(':'); return int(h) * 60 + int(m)


def t(xx, yy, s, size=3.3, weight=400, fill=INK, anchor='middle'):
    return f'<text x="{xx:.2f}" y="{yy:.2f}" font-family="{SANS}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'


def padlock(cx, cy, col):
    """An open padlock: the body, and the shackle lifted off one side."""
    return (f'<rect x="{cx - 3:.2f}" y="{cy:.2f}" width="6" height="5" rx=".8" fill="{PAPER}" stroke="{col}" stroke-width=".55"/>'
            f'<path d="M{cx - 1.8:.2f} {cy:.2f} V{cy - 2.6:.2f} A1.8 1.8 0 0 1 {cx + 1.8:.2f} {cy - 2.6:.2f} V{cy - 1.4:.2f}" fill="none" stroke="{col}" stroke-width=".55"/>')


def main():
    hold = hm('18:44')
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="The evening of 29 October to scale: '
         'the lock tool at 17:54, three locks planned for 18:30, 19:30 and 20:00 drawn as open padlocks, the hold at 18:44, the last release at 18:46; no lock closed.">']
    # after the hold: tinted, and said in words
    s.append(f'<rect x="{x(hold):.2f}" y="10" width="{x(T1) - x(hold):.2f}" height="{H - 18}" fill="{FILL}"/>')
    s.append(t(W - 5, H - 15, 'after the hold: work in flight still landed,', 3.2, 400, MUTED, 'end'))
    s.append(t(W - 5, H - 10.8, 'and no member\'s wake started again', 3.2, 400, MUTED, 'end'))
    # the axis, labelled on the hour
    s.append(f'<line x1="{x(T0):.2f}" y1="{Y}" x2="{x(T1):.2f}" y2="{Y}" stroke="{INK}" stroke-width=".5"/>')
    for h in (18, 19):
        s.append(f'<line x1="{x(h * 60):.2f}" y1="{Y - 1.2}" x2="{x(h * 60):.2f}" y2="{Y + 1.2}" stroke="{INK}" stroke-width=".4"/>')
        s.append(t(x(h * 60), Y + 5.2, f'{h}:00', 3.2, 400, MUTED))
    # above: what happened
    for tm, words, col, dy in (('17:54', 'the lock tool lands', INK, 0), ('18:44', 'the hold', ACCENT, -9), ('18:46', 'the last release', INK, -18)):
        xx = x(hm(tm))
        s.append(f'<line x1="{xx:.2f}" y1="{Y}" x2="{xx:.2f}" y2="{Y - 12 + dy:.2f}" stroke="{col}" stroke-width="{.9 if col == ACCENT else .35}"/>')
        s.append(f'<circle cx="{xx:.2f}" cy="{Y}" r="1.2" fill="{col}"/>')
        anchor = 'end' if tm == '18:44' else 'start'
        s.append(t(xx + (-1.2 if anchor == 'end' else 1.2), Y - 13.6 + dy, f'<tspan font-weight="700">{tm}</tspan> {words}', 3.3, 400, col, anchor))
    # below: what was planned, and never happened
    for tm, part in (('18:30', 'part 1'), ('19:30', 'part 2'), ('20:00', 'part 3')):
        xx = x(hm(tm))
        s.append(f'<line x1="{xx:.2f}" y1="{Y}" x2="{xx:.2f}" y2="{Y + 13:.2f}" stroke="{MUTED}" stroke-width=".35" stroke-dasharray="1 .7"/>')
        s.append(f'<circle cx="{xx:.2f}" cy="{Y}" r="1.1" fill="{PAPER}" stroke="{MUTED}" stroke-width=".4"/>')
        s.append(padlock(xx, Y + 16, MUTED))
        a = 'end' if tm == '20:00' else 'middle'
        xa = xx + 3 if tm == '20:00' else xx
        s.append(t(xa, Y + 27, f'<tspan font-weight="700">{tm}</tspan> {part}', 3.3, 400, INK, a))
        s.append(t(xa, Y + 31.4, 'never closed', 3.2, 400, MUTED, a))
    s.append(t(4, H - 2, 'Above the line: what happened. Below: what was planned. To scale.', 3.2, 400, MUTED, 'start'))
    s.append('</svg>')
    (HERE / 'locks.svg').write_text('\n'.join(s) + '\n')
    (HERE / 'pages.html').write_text(
        '<section class="page" data-claims="C027 · C006 · C005">\n <figure class="fig span12">\n'
        '  <p class="fig-title">Three locks planned, none closed</p>\n'
        '  <img src="{{dir}}/locks.svg" alt="The evening to scale: the lock tool, three planned locks drawn as open padlocks, the hold, the last release" style="width:100%;display:block">\n'
        '  <figcaption><b>The tool to lock each part landed at 17:54; the first lock was due at 18:30 and did not run; at 18:44 the hold stopped every member\'s next wake, '
        'the lock included. Two brakes met, and the stronger one stopped the other.</b>'
        '<span class="src">From claims/register.json C027 (the plan, the tool, none locked), C006 (the hold) and C005 (the last release); '
        'chapter 8, manuscript/08-the-locks-that-never-closed.md, tells it.</span></figcaption>\n'
        ' </figure>\n</section>\n')


if __name__ == '__main__':
    main()
