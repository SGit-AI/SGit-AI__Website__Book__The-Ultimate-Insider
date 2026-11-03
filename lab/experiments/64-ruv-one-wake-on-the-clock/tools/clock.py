"""The seventy, chapter 5 (ruv; the conductor named the owner, conductor__019): the five-step wake on the clock, with one real
wake's verdicts filled in.

The clock face is the day's schedule, each member's minute past the hour (C071, as the slots stood for the day, not as they
stood at 02:14). The real wake is the conductor's first, the only record at the talk's 298be4e whose five verdicts are go, go,
partial, finding, partial, as the chapter tells it (team/conductor/wakes/20261029T021416Z.json, started 02:14, C022's first).
Its verdicts are read from that record at build. No other number. Pure vector: no image, href, script or handler; the tool
refuses itself if publishing/edition.py's rule would match. Writes edition/one-wake.svg and pages.html.
Usage: python3 -B -I tools/clock.py --talk <clone of the talk's repository>
"""
import json, math, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
INK, MUTED, FILL, FILL2, ACCENT, PAPER, AMBER = '#1f2933', '#5b6670', '#eef2f6', '#d5dce4', '#b0481a', '#ffffff', '#8a6d1f'
SANS = 'Inter, Helvetica, Arial, sans-serif'
PT = 9 * 25.4 / 72
UNSAFE = re.compile(r"<script|<foreignObject|\bhref\s*=|\bon[a-z]+\s*=|@import", re.I)
RECORD = 'team/conductor/wakes/20261029T021416Z.json'
STEPS = [('plan', 'plan it'), ('pre_review', 'have the plan checked'), ('work', 'do it'),
         ('post_review', 'have it checked'), ('post_check', 'check it went to plan')]


def t(x, y, s, weight=400, fill=INK, anchor='start', size=PT):
    return f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{size:.3f}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'


def main():
    clone = sys.argv[sys.argv.index('--talk') + 1]
    rec = json.loads(subprocess.run(['git', '-C', clone, 'show', f'298be4e:{RECORD}'], capture_output=True, text=True, check=True).stdout)
    verdicts = [rec['steps'][k]['verdict'] for k, _ in STEPS]
    assert verdicts == ['go', 'go', 'partial', 'finding', 'partial'], verdicts
    reg = json.loads((ROOT / 'claims' / 'register.json').read_text())
    c = {x['id']: x for x in (reg['claims'] if isinstance(reg, dict) else reg)}
    assert c['C071']['state'] == 'checked' and c['C022']['state'] == 'checked'
    slots = {m: int(v.strip(':')) for m, v in c['C071']['value'].items()}
    started = c['C022']['value']['first_started'][:5]                  # 02:14
    W, H = 164.0, 76.0
    cx, cy, R = 46.0, 38.0, 20.0
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H:g}mm" viewBox="0 0 {W:g} {H:g}" role="img" '
         'aria-label="The five-step wake on the clock: each member\'s minute past the hour, the conductor\'s lit, and the conductor\'s first wake '
         'with its five verdicts: go, go, partial, finding, partial.">',
         f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{FILL}" stroke="{FILL2}" stroke-width=".4"/>']
    for m in range(60):
        a = 2 * math.pi * m / 60 - math.pi / 2
        r0 = R - (2.2 if m % 15 == 0 else 1.1)
        s.append(f'<line x1="{cx + r0 * math.cos(a):.2f}" y1="{cy + r0 * math.sin(a):.2f}" x2="{cx + R * math.cos(a):.2f}" y2="{cy + R * math.sin(a):.2f}" stroke="{MUTED}" stroke-width="{.35 if m % 15 == 0 else .2}"/>')
    for name, minute in slots.items():
        a = 2 * math.pi * minute / 60 - math.pi / 2
        lit = name == 'conductor'
        x, y = cx + (R - 3.2) * math.cos(a), cy + (R - 3.2) * math.sin(a)
        s.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{1.5 if lit else 1.1}" fill="{ACCENT if lit else INK}"/>')
        lx, ly = cx + (R + 2.6) * math.cos(a), cy + (R + 2.6) * math.sin(a) + 1.1
        anchor = 'start' if math.cos(a) > .15 else ('end' if math.cos(a) < -.15 else 'middle')
        if anchor == 'middle':
            ly += 1.6 if math.sin(a) > 0 else -.6
        if lit:                                                    # the lit label inside the face, so the line to the steps leaves clear
            anchor, lx, ly = 'middle', x - 2.5, y + 8.4
        s.append(t(lx, ly, f'{name} :{minute:02d}', 700 if lit else 400, ACCENT if lit else INK, anchor, PT))
    s.append(t(cx, cy + 1.1, 'the hour', 400, MUTED, 'middle'))
    # the five steps, as a path to the right, with the wake's verdicts
    x0, y0 = 100.0, 14.0
    s.append(t(x0, 6.5, f'the conductor\'s first wake, {started}', 700, INK))
    colour = {'go': INK, 'partial': AMBER, 'finding': ACCENT}
    for i, ((key, plain), v) in enumerate(zip(STEPS, verdicts)):
        y = y0 + i * 11.5
        s.append(f'<circle cx="{x0 + 3:.2f}" cy="{y + 3:.2f}" r="3" fill="{PAPER}" stroke="{INK}" stroke-width=".4"/>')
        s.append(t(x0 + 3, y + 4.1, str(i + 1) if False else '', 700))
        s.append(t(x0 + 8.5, y + 4.1, plain))
        s.append(f'<rect x="{W - 20:.2f}" y="{y + .2:.2f}" width="19" height="5.6" rx="2.8" fill="{colour[v] if v != "go" else PAPER}" stroke="{colour[v]}" stroke-width=".4"/>')
        s.append(t(W - 10.5, y + 4.1, v, 700, PAPER if v != 'go' else INK, 'middle'))
        if i < 4:
            s.append(f'<line x1="{x0 + 3:.2f}" y1="{y + 6:.2f}" x2="{x0 + 3:.2f}" y2="{y + 11.5:.2f}" stroke="{MUTED}" stroke-width=".35"/>')
    am = 2 * math.pi * slots['conductor'] / 60 - math.pi / 2       # from the conductor's own dot, over the top, to the first step
    dx, dy = cx + (R - 3.2) * math.cos(am), cy + (R - 3.2) * math.sin(am)
    s.append(f'<path d="M{dx + 1.6:.2f} {dy - .6:.2f} C{dx + 14:.2f} {dy - 16:.2f} {x0 - 14:.2f} {y0 + 3:.2f} {x0 - .4:.2f} {y0 + 3:.2f}" fill="none" stroke="{ACCENT}" stroke-width=".4"/>')
    s.append(t(x0, H - 2.4, 'the clock face: the day\'s schedule (C071)', 400, MUTED))
    s.append('</svg>')
    svg = '\n'.join(s) + '\n'
    if UNSAFE.search(svg):
        sys.exit('refused by the build\'s rule')
    (HERE / 'edition' / 'one-wake.svg').write_text(svg)
    (HERE / 'pages.html').write_text(
        '<section class="page" data-claims="C071 · C022">\n <figure class="fig span12">\n'
        '  <p class="fig-title">One wake on the clock</p>\n'
        '  <img src="{{dir}}/edition/one-wake.svg" alt="The five-step wake on the clock, with the conductor\'s first wake\'s verdicts" style="width:100%;display:block">\n'
        '  <figcaption><b>Each member woke at its own minute; at its minute, the conductor\'s first wake went through the five steps: '
        'two checks said go, the work was partial, the check after it found something, and the plan was only partly done.</b>'
        '<span class="src">The clock face: the day\'s schedule, C071. The wake: team/conductor/wakes/20261029T021416Z.json at 298be4e, started 02:14 (C022), '
        'its verdicts read from the record at build.</span></figcaption>\n </figure>\n</section>\n')
    print('one-wake.svg written')


if __name__ == '__main__':
    main()
