"""LAB 29 (ruv): the afternoon loop, drawn (RC2 chapter 3, page 4).

Every time comes from the register, read here at build: C104 (the feedback round, given about 13:50, recorded 14:07), C028
(the player ported at 15:07) and C105 (the eight asks that carry his time in a commit subject, each with when it came back).
Two lanes: what he asked above, what came back below, one line between each pair. The axis is broken: the afternoon from 13:30
to 17:15 compressed, 17:15 to 18:45 opened out, so the eight asks can be told apart; the break is layout, not an event.
Labels as the researcher asks (researcher__012): "asked (as written)", "recorded" for the conductor's rows, "landed" for the
player's fixes. Writes loop.svg and pages.html.
Usage: python3 -B -I tools/draw.py
"""
import json, re
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
INK, MUTED, FILL, FILL2, ACCENT, PAPER = '#1f2933', '#5b6670', '#eef2f6', '#d5dce4', '#b0481a', '#ffffff'
SANS = 'Inter, Helvetica, Arial, sans-serif'
PT = 9 * 25.4 / 72
W, H = 164.0, 50.0
A0, A1, AX0, AX1 = 13.5, 17.25, 26.0, 62.0                      # hours and mm: the compressed afternoon
B0, B1, BX0, BX1 = 17.25, 18.75, 66.0, 161.0                     # the last ninety minutes, opened out
YA, YB = 12.0, 32.0                                              # the two lanes


def hours(t):
    h, m, *s = [int(x) for x in t.split(':')]
    return h + m / 60 + (s[0] if s else 0) / 3600


def x(t):
    h = hours(t) if isinstance(t, str) else t
    if h <= A1:
        return AX0 + (h - A0) / (A1 - A0) * (AX1 - AX0)
    return BX0 + (h - B0) / (B1 - B0) * (BX1 - BX0)


def t(xx, y, s, anchor='start', weight=400, fill=INK):
    return f'<text x="{xx:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{PT:.3f}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'


def main():
    reg = json.loads((ROOT / 'claims' / 'register.json').read_text())
    claims = {c['id']: c for c in (reg['claims'] if isinstance(reg, dict) else reg)}
    for cid in ('C028', 'C104', 'C105'):
        assert claims[cid]['state'] == 'checked', cid
    fb = claims['C104']['value']['feedback_round']
    given = re.search(r'(\d{1,2}:\d{2})', fb['given']).group(1)          # "about 13:50"
    recorded = re.search(r'(\d{1,2}:\d{2}:\d{2})', fb['recorded']).group(1)
    port = re.search(r'(\d{1,2}:\d{2}:\d{2})', claims['C028']['value']['port']).group(1)
    rows = claims['C105']['value']['rows']
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H:g}mm" viewBox="0 0 {W:g} {H:g}" role="img" '
         'aria-label="The afternoon loop: what the editor asked, above, and what came back, below, on one line of time.">']
    # lanes and their names
    for y, name in ((YA, 'he asked'), (YB, 'came back')):
        s.append(f'<line x1="{AX0:.2f}" y1="{y}" x2="{AX1:.2f}" y2="{y}" stroke="{FILL2}" stroke-width=".4"/>')
        s.append(f'<line x1="{BX0:.2f}" y1="{y}" x2="{BX1:.2f}" y2="{y}" stroke="{FILL2}" stroke-width=".4"/>')
        s.append(t(0.3, y + 1.1, name, weight=700))
    # the break: two short slashes on each lane, no label
    for y in (YA, YB):
        for dx in (0, 1.4):
            s.append(f'<line x1="{AX1 + 1 + dx:.2f}" y1="{y + 1.4}" x2="{AX1 + 2 + dx:.2f}" y2="{y - 1.4}" stroke="{MUTED}" stroke-width=".3"/>')
    # the axis
    ya = YB + 8
    for hh in (14, 15, 16, 17):
        s.append(f'<line x1="{x(hh):.2f}" y1="{YB + 2}" x2="{x(hh):.2f}" y2="{YB + 3.4}" stroke="{MUTED}" stroke-width=".3"/>')
        s.append(t(x(hh), ya, f'{hh}:00', 'middle', fill=MUTED))
    for hh in (17.5, 18.0, 18.5):
        s.append(f'<line x1="{x(hh):.2f}" y1="{YB + 2}" x2="{x(hh):.2f}" y2="{YB + 3.4}" stroke="{MUTED}" stroke-width=".3"/>')
        s.append(t(x(hh), ya, f'{int(hh)}:{int(round(hh % 1 * 60)):02d}', 'middle', fill=MUTED))
    # the afternoon, from C104 and C028: no per-ask marks
    s.append(f'<line x1="{x(given):.2f}" y1="{YA}" x2="{x(recorded):.2f}" y2="{YB}" stroke="{MUTED}" stroke-width=".4"/>')
    s.append(f'<circle cx="{x(given):.2f}" cy="{YA}" r="1.1" fill="{PAPER}" stroke="{INK}" stroke-width=".35"/>')
    s.append(f'<rect x="{x(recorded) - 1:.2f}" y="{YB - 1}" width="2" height="2" fill="{PAPER}" stroke="{INK}" stroke-width=".35"/>')
    s.append(f'<circle cx="{x(port):.2f}" cy="{YB}" r="1.1" fill="{INK}"/>')
    s.append(t(x(port) + 1.8, YB - 2.2, 'the player, ported', 'start', fill=INK))
    s.append(t(x(given) + 1.8, YA - 2.4, 'his first priority', 'start', fill=INK))
    # the eight asks of C105
    for asked, commit, back, kind in rows:
        landed = kind.startswith('player')
        s.append(f'<line x1="{x(asked):.2f}" y1="{YA + 1.1}" x2="{x(back):.2f}" y2="{YB - 1.1}" stroke="{ACCENT if landed else MUTED}" stroke-width=".4"/>')
        s.append(f'<circle cx="{x(asked):.2f}" cy="{YA}" r="1.1" fill="{PAPER}" stroke="{INK}" stroke-width=".35"/>')
        if landed:
            s.append(f'<circle cx="{x(back):.2f}" cy="{YB}" r="1.1" fill="{ACCENT}"/>')
        else:
            s.append(f'<rect x="{x(back) - 1:.2f}" y="{YB - 1}" width="2" height="2" fill="{PAPER}" stroke="{INK}" stroke-width=".35"/>')
    s.append(t(x('17:36'), YA - 2.4, 'routed by the conductor', 'middle', fill=MUTED))
    s.append(t(x('18:15'), YA - 2.4, 'the player', 'middle', fill=ACCENT))
    s.append('</svg>')
    (HERE / 'loop.svg').write_text('\n'.join(s) + '\n')
    key = (f'<span style="white-space:nowrap">&#9675; asked (as written)</span> &nbsp; '
           f'<span style="white-space:nowrap">&#9633; recorded: the conductor routes it</span> &nbsp; '
           f'<span style="white-space:nowrap;color:var(--accent)">&#9679; landed: a player fix</span>')
    (HERE / 'pages.html').write_text(
        '<section class="page" data-claims="C104 · C028 · C105">\n <figure class="fig span12">\n'
        '  <p class="fig-title">The afternoon loop: ask, and what came back</p>\n'
        '  <img src="{{dir}}/loop.svg" alt="The editor\'s afternoon asks above, what came back below, one line between each pair" style="width:100%;display:block">\n'
        f'  <p style="margin:2mm 0 0;font:400 9pt/12pt var(--sans);color:var(--muted)">{key}</p>\n'
        '  <figcaption><b>Read each line from top to bottom: an ask, then what came back. The afternoon from his first priority to the player\'s port is drawn without '
        'its asks, which carry no time in the record; the last ninety minutes are opened out, and the player\'s fixes come back within minutes.</b> '
        'A time asked is what a member wrote, not a clock: one fix landed before the time it names.'
        '<span class="src">The register: C104 (given about 13:50, recorded 14:07), C028 (the port, 15:07), C105 (the eight asks with his time in a commit subject, '
        'at 298be4e). The axis is broken at quarter past five: layout, not an event.</span></figcaption>\n </figure>\n</section>\n')
    print('loop.svg and pages.html written')


if __name__ == '__main__':
    main()
