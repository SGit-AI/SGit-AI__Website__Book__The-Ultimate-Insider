"""LAB 12 (ruv): chapter 4's five-step wake as one vertical strip (the editor's RC1 review, note 9: experiments per chapter).

Drawn from team/conductor/WAKE.md (this repository; ported from the talk's at 298be4e) and chapter 4's own concept box
(manuscript/04-the-hourly-machine.md). No number but the step order. Writes strip.svg and pages.html.
Usage: python3 -I tools/build.py
"""
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
INK, MUTED, FILL, FILL2, ACCENT, TINT, PAPER = '#1f2933', '#5b6670', '#eef2f6', '#d5dce4', '#b0481a', '#f6e1d4', '#ffffff'
SANS = 'Inter, Helvetica, Arial, sans-serif'
W, BX, BW, GAP = 164, 0, 108, 3.6                             # mm: strip width; the spine's boxes on the left
SX, SW = 118, 46                                              # the side: where a stop goes

# (badge or '', title, who, what it sees or does, verdicts, height, kind)
STEPS = [
 ('', 'Start', 'the member', 'start.py pulls dev, prints the start banner. A hold on the team: no work, end banner, stop.', '', 15, 'edge'),
 ('1', 'Plan', 'a conductor sub-agent', 'reads the member\'s mail, board, requests and role; writes one to three items, requests first.', 'go · stop', 21, 'step'),
 ('2', 'Pre-review', 'a security sub-agent', 'sees the plan and the rules, never the raw messages: policy, secrets, harm to other members.', 'go · change · stop', 21, 'step'),
 ('', 'Gate', 'wake.py gate', 'refuses the work until steps 1 and 2 both say go.', '', 13, 'gate'),
 ('3', 'Work', 'the member', 'only inside its own policy\'s paths, and only after the gate.', 'done · partial · none', 17, 'work'),
 ('4', 'Post-review', 'a security sub-agent', 'reads the diff and runs the gate: secrets, writes outside policy, harm to other members.', 'clean · finding · stop', 21, 'step'),
 ('5', 'Post-check', 'a conductor sub-agent', 'did it go according to plan, item by item?', 'as-planned · partial · off-plan · stop', 19, 'step'),
 ('', 'Close', 'wake.py close', 'refuses a wake that skipped a step. Then the release, the debrief, and the end banner, last.', '', 15, 'edge'),
]
FS, LH = 3.3, 4.05                                             # 9.4 pt text, its leading


def t(x, y, s, size=FS, weight=400, fill=INK, anchor='start'):
    return f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'


def wrap(s, n):
    out, line = [], ''
    for w in s.split():
        if len(line) + len(w) + 1 > n:
            out.append(line); line = w
        else:
            line = (line + ' ' + w).strip()
    return out + [line]


def boxes():
    """Each step's lines, and the box height they need."""
    out = []
    for badge, title, who, what, verdicts, _, kind in STEPS:
        lines = wrap(what, 58)
        if title == 'Pre-review':
            lines += ['A change sends the plan back: amend it, review it again.']
        h = 8.5 + LH * len(lines) + (LH + .6 if verdicts else 0) + 1.6
        out.append((badge, title, who, lines, verdicts, h, kind))
    return out


def strip():
    bx = boxes()
    total = sum(b[5] for b in bx) + GAP * (len(bx) - 1) + 2
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {total:.1f}" role="img" aria-label="The five-step wake as one '
         'vertical strip: start, plan, pre-review, the gate, the work, post-review, post-check, close; a stop from any step writes HOLD.md and every wake stops.">']
    y, mids = 1, {}
    for badge, title, who, lines, verdicts, h, kind in bx:
        fill = {'edge': FILL, 'gate': PAPER, 'work': TINT, 'step': PAPER}[kind]
        stroke = ACCENT if kind == 'gate' else INK if kind != 'edge' else MUTED
        dash = ' stroke-dasharray="1.6 1"' if kind == 'gate' else ''
        s.append(f'<rect x="{BX}" y="{y:.2f}" width="{BW}" height="{h:.2f}" rx="1.6" fill="{fill}" stroke="{stroke}" stroke-width=".5"{dash}/>')
        x0 = BX + 4
        if badge:
            s.append(f'<circle cx="{BX + 5.5}" cy="{y + 5.2:.2f}" r="3.1" fill="{INK}"/>' + t(BX + 5.5, y + 6.4, badge, 3.6, 700, PAPER, 'middle'))
            x0 = BX + 11
        s.append(t(x0, y + 6.3, f'{title} <tspan font-weight="400" fill="{MUTED}">· {who}</tspan>', 3.7, 700))
        yy = y + 11
        for ln in lines:
            s.append(t(BX + 4, yy, ln)); yy += LH
        if verdicts:
            parts = [f'<tspan fill="{ACCENT}" font-weight="700">stop</tspan>' if v == 'stop' else f'<tspan font-weight="700">{v}</tspan>' for v in verdicts.split(' · ')]
            s.append(t(BX + 4, yy + .6, f'<tspan fill="{MUTED}">verdicts: </tspan>' + ' · '.join(parts)))
        mids[title] = (y, h)
        y += h
        if title != 'Close':
            s.append(f'<line x1="{BW / 2}" y1="{y:.2f}" x2="{BW / 2}" y2="{y + GAP - .6:.2f}" stroke="{INK}" stroke-width=".5"/>'
                     f'<path d="M{BW / 2 - 1.3:.2f} {y + GAP - 1.8:.2f} L{BW / 2:.2f} {y + GAP - .2:.2f} L{BW / 2 + 1.3:.2f} {y + GAP - 1.8:.2f}" fill="none" stroke="{INK}" stroke-width=".5"/>')
        y += GAP
    # the side: every stop goes to one place
    lines = wrap('writes the member\'s HOLD.md and pushes it to dev. From then on every member\'s start.py stops the wake, and only the editor lifts the hold.', 24)
    sh = 10 + LH * len(lines) + 2
    hm = (mids['Pre-review'][0] + mids['Post-check'][0] + mids['Post-check'][1]) / 2
    s.append(f'<rect x="{SX}" y="{hm - sh / 2:.2f}" width="{SW}" height="{sh:.2f}" rx="1.6" fill="{TINT}" stroke="{ACCENT}" stroke-width=".6"/>')
    s.append(t(SX + 3, hm - sh / 2 + 6.3, 'A stop, from any step', 3.7, 700, ACCENT))
    for i, ln in enumerate(lines):
        s.append(t(SX + 3, hm - sh / 2 + 11 + i * LH, ln))
    for name in ('Plan', 'Pre-review', 'Post-review', 'Post-check'):
        yy, hh = mids[name]
        ym = yy + 5.2
        s.append(f'<path d="M{BW:.2f} {ym:.2f} C{BW + 6:.2f} {ym:.2f} {SX - 6:.2f} {hm:.2f} {SX:.2f} {hm:.2f}" fill="none" stroke="{ACCENT}" stroke-width=".45" stroke-dasharray="1.4 .9"/>')
    s.append('</svg>')
    return '\n'.join(s)


def main():
    (HERE / 'strip.svg').write_text(strip() + '\n')
    (HERE / 'pages.html').write_text(
        '<section class="page" data-claims="">\n <figure class="fig span12">\n'
        '  <img src="{{dir}}/strip.svg" alt="The five-step wake as one vertical strip, with where a stop goes" style="width:100%;display:block">\n'
        '  <figcaption><b>Read down the left for one wake; every stop on the right goes to the same place, and stops every member.</b>'
        '<span class="src">From team/conductor/WAKE.md (this book\'s team; ported rule for rule from the talk\'s at 298be4e) and chapter 4\'s concept box '
        '(manuscript/04-the-hourly-machine.md). Chapter 4 tells when the talk\'s team began to run it.</span></figcaption>\n'
        ' </figure>\n</section>\n')


if __name__ == '__main__':
    main()
