"""LAB 09 (ruv): the talk's M03, 'Meet the team', drawn as one big picture and explained (the editor's RC1 review, note 8, T4).

Not a frame of the animation: a drawing made from the register only, so every number on it has a claim id.
  C071  each member's minute past the hour (the talk's schedule at 298be4e)
  C073  the six counts as at 17:02:26 on 29 October (the talk's team-in-numbers.json)
  C024  the day's one hold, 18:44
The short role words are M03's own (its SHORT map in src/static/motion/lab/meet-the-team/v1/index.html at f45028c).
Writes dial.svg and pages.html; the lab sets them (lab/README.md). Usage: python3 -I tools/build.py
"""
import json, math
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
REG = json.loads((HERE.parents[2] / 'claims' / 'register.json').read_text())
CLAIMS = {c['id']: c for c in (REG['claims'] if isinstance(REG, dict) and 'claims' in REG else REG)}
INK, MUTED, FILL, FILL2, ACCENT, PAPER = '#1f2933', '#5b6670', '#eef2f6', '#d5dce4', '#b0481a', '#ffffff'
SANS = 'Inter, Helvetica, Arial, sans-serif'
SHORT = {'conductor': 'routes and paces', 'deck': 'what the talk says', 'designer': 'how it looks', 'dev': 'build and release',
         'motion': 'story animations', 'researcher': 'the facts', 'ruv-sgit': 'animations in runs', 'storyteller': 'the story',
         'studio': 'ports'}                                         # M03's own words
SLOTS = {k: int(v.strip(':')) for k, v in CLAIMS['C071']['value'].items()}

W, H = 167, 78                                                      # mm, the text block's width
CX, CY, R = 83.5, 39, 26


def t(x, y, s, size=3.4, weight=400, fill=INK, anchor='start'):
    return (f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}">{s}</text>')


def pos(minute, r):
    a = minute / 60 * 2 * math.pi - math.pi / 2
    return CX + r * math.cos(a), CY + r * math.sin(a)


def badge(x, y, n):
    return f'<circle cx="{x:.2f}" cy="{y:.2f}" r="2.6" fill="{INK}"/>' + t(x, y + 1.2, str(n), 3.4, 700, PAPER, 'middle')


def dial():
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="An hour dial: nine agents around '
         'it at the minute past the hour each one wakes, the editor at the centre.">']
    s.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="{FILL2}" stroke-width="1.4"/>')
    for m in range(0, 60, 5):                                        # the minutes, every five
        a, b = pos(m, R - 1.6), pos(m, R + 1.6)
        s.append(f'<line x1="{a[0]:.2f}" y1="{a[1]:.2f}" x2="{b[0]:.2f}" y2="{b[1]:.2f}" stroke="{MUTED}" stroke-width=".4"/>')
    for m, lab in ((0, ':00'), (15, ':15'), (30, ':30'), (45, ':45')):
        x, y = pos(m, R - 6)
        s.append(t(x, y + 1.2, lab, 3.4, 400, MUTED, 'middle'))
    s.append(f'<circle cx="{CX}" cy="{CY}" r="11" fill="{PAPER}" stroke="{INK}" stroke-width=".8"/>')
    s.append(t(CX, CY + 1.2, 'the editor', 3.6, 700, INK, 'middle'))
    for name, m in sorted(SLOTS.items(), key=lambda kv: kv[1]):
        x, y = pos(m, R)
        s.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="2.4" fill="{ACCENT}" stroke="{PAPER}" stroke-width=".6"/>')
        lx, ly = pos(m, R + 6)
        anchor = 'start' if lx > CX + 2 else 'end' if lx < CX - 2 else 'middle'
        s.append(t(lx, ly, f'{name} <tspan font-weight="700" fill="{ACCENT}">:{m:02d}</tspan>', 3.6, 700, INK, anchor))
        s.append(t(lx, ly + 4, SHORT[name], 3.4, 400, MUTED, anchor))
    # the call-outs: 1 the ring is one hour, 2 a member at its minute, 3 the editor
    x, y = pos(43, R)                                                 # on the ring, between two members
    s.append(badge(x, y, 1))
    x, y = pos(SLOTS['conductor'] + 4, R - 5)                         # just inside, after the first member's dot
    s.append(badge(x, y, 2))
    s.append(badge(CX + 13, CY - 9, 3))
    s.append('</svg>')
    return '\n'.join(s)


def counts():
    v = CLAIMS['C073']['value']
    first = lambda k: v[k].split(' ')[0].rstrip(':,')
    rows = [(first('hours_since_first_commit') + ' h', 'since the first commit, at 00:16'),
            (first('commits'), 'commits, CI\'s releases among them'),
            (first('releases'), 'releases'),
            (first('wakes'), 'wakes, 119 of them ended ok'),
            (first('commits_overnight'), 'commits overnight, 00:16 to 05:59'),
            (first('holds'), 'holds at 17:02; the day\'s one came at 18:44 (C024)')]
    return rows


def main():
    (HERE / 'dial.svg').write_text(dial() + '\n')
    tiles = ''.join(f'<div class="tile" style="margin:0"><span style="display:block;font:800 28pt/30pt var(--sans)">{n}</span>{w}</div>'
                    for n, w in counts())
    chips = ''.join(f'<div style="border:.4mm solid var(--accent);border-radius:2mm;padding:2mm 3mm;font:400 9.5pt/13pt var(--sans)">'
                    f'<b>{a}</b><br><span style="color:var(--muted)">{b}</span></div>'
                    for a, b in (('The board', 'an SGit vault'), ('The mail', 'an SGit vault'), ('A key each', 'the PKI, pki.sgit.ai'),
                                 ('Five steps', 'every wake, with a gate')))
    how = ''.join(f'<li style="margin-bottom:2mm">{x}</li>' for x in (
        '<b>The ring is one hour.</b> Every member wakes once an hour, all day and all night.',
        '<b>Each dot is a member, at its own minute.</b> The conductor goes first, at :02, to route the hour\'s work; the storyteller last, at :54. No two share a minute.',
        '<b>The editor is at the centre.</b> Every member answers to one person, who decides by signing.',
        '<b>The counts are the talk\'s at 17:02 on 29 October,</b> about two hours before the record ends: what the team had done by then, from its own records.',
        '<b>Four things keep it in step:</b> a shared board, shared mail, a key for each member, and five steps at every wake.'))
    html = ('<section class="page" data-claims="C071">\n <figure class="fig span12">\n'
            '  <p class="fig-title">Nine agents, one editor: who wakes when</p>\n'
            '  <img src="{{dir}}/dial.svg" alt="An hour dial: nine agents around it at the minute each wakes, the editor at the centre" style="width:100%;display:block">\n'
            '  <figcaption><b>Read it like a clock: the dots are the minutes past each hour when each member wakes (C071).</b>'
            '<span class="src">Drawn from claims/register.json C071; role words M03\'s own (at f45028c). This "ruv-sgit" is the talk\'s member.</span></figcaption>\n'
            ' </figure>\n</section>\n'
            '<section class="page" data-claims="C071 · C073 · C024">\n'
            '  <h2>How to read it</h2>\n'
            f'  <ol style="margin:0 0 6mm;padding-left:5mm;font:400 10pt/14pt var(--sans)">{how}</ol>\n'
            '  <h2>One day\'s work, from the records, at 17:02</h2>\n'
            f'  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:5mm 6mm" class="rail">{tiles}</div>\n'
            '  <h2 style="margin-top:6mm">What keeps it in step</h2>\n'
            f'  <div style="display:grid;grid-template-columns:1fr 1fr;gap:3mm 4mm">{chips}</div>\n'
            '  <p style="margin-top:5mm;font:400 9pt/12pt var(--sans);color:var(--muted)">The talk\'s counts at 17:02:26 on 29 October (C073), not the day\'s; '
            'the board and the mail were SGit vaults on the talk\'s team (this book\'s team keeps them in git). The capability is the orchestration, not the model: M03\'s last line.</p>\n'
            '</section>\n')
    (HERE / 'pages.html').write_text(html)


if __name__ == '__main__':
    main()
