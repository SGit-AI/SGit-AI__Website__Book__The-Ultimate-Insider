"""The seventy's chapter 5 (slot 2) and the full book's chapter 7 (the designer's 110 gave it to ruv): the wake record as a
page. Five boxes in a column, each with its step, who ran it as the record names it, its verdict, and one sentence quoted word
for word from the record; the finding in step four highlighted.

The record is the conductor's first, team/conductor/wakes/20261029T021416Z.json at the talk's 298be4e, read at build from a
clone; its five verdicts are asserted. Each quoted sentence is asserted to stand in that step's comment as written. No time
but the wake's start, from C022. The record's "by" names roles: security was never staffed (C072), so its two steps were
reviews the conductor's own wake ran; the caption says so. No id, key or vault detail beyond the quotes. Pure vector: no
image, href, script or handler; the tool refuses itself if publishing/edition.py's rule would match. Writes
edition/wake-page.svg only.
Usage: python3 -B -I tools/page.py --talk <clone of the talk's repository>
"""
import json, re, subprocess, sys
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
INK, MUTED, FILL, FILL2, ACCENT, PAPER, AMBER = '#1f2933', '#5b6670', '#eef2f6', '#d5dce4', '#b0481a', '#ffffff', '#8a6d1f'
SANS = 'Inter, Helvetica, Arial, sans-serif'
PT = 9 * 25.4 / 72
SMALL = 7.5 * 25.4 / 72
UNSAFE = re.compile(r"<script|<foreignObject|\bhref\s*=|\bon[a-z]+\s*=|@import", re.I)
RECORD = 'team/conductor/wakes/20261029T021416Z.json'
STEPS = [
    ('plan', 'plan it', 'Amended after the pre-review\'s change, all five conditions adopted', True),
    ('pre_review', 'have the plan checked', 'The amended plan adopts all five conditions and stays inside policy scope.writes', True),
    ('work', 'do it', 'Not done: tui-evidence-public\'s read key, because the vault is not on the server yet and could not be audited (pre-review condition 2 kept).', False),
    ('post_review', 'have it checked', 'agents.py flags CLAUDE.md as outside conductor scope; the editor allowed it, but the commit message never names it and the pre-review made naming it a condition.', False),
    ('post_check', 'check it went to plan', 'The post-review finding answered in the debrief; the commit message lacked the CLAUDE.md note (named in the closing commit).', False),
]
WRAP = 92                                                           # characters a line, at 7.5 pt in the box's text column


def t(x, y, s, weight=400, fill=INK, anchor='start', size=PT, style=''):
    st = f' font-style="{style}"' if style else ''
    return (f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{size:.3f}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}"{st}>{escape(s, quote=False)}</text>')


def wrap(s, n):
    out, line = [], ''
    for w in s.split():
        if line and len(line) + 1 + len(w) > n:
            out.append(line)
            line = w
        else:
            line = f'{line} {w}'.strip()
    return out + [line]


def main():
    clone = sys.argv[sys.argv.index('--talk') + 1]
    rec = json.loads(subprocess.run(['git', '-C', clone, 'show', f'298be4e:{RECORD}'], capture_output=True, text=True, check=True).stdout)
    verdicts = [rec['steps'][k]['verdict'] for k, *_ in STEPS]
    assert verdicts == ['go', 'go', 'partial', 'finding', 'partial'], verdicts
    for k, _, quote, opening in STEPS:
        comment = rec['steps'][k]['comment']
        assert (comment.startswith(quote) if opening else quote in comment), k
    reg = json.loads((ROOT / 'claims' / 'register.json').read_text())
    c = {x['id']: x for x in (reg['claims'] if isinstance(reg, dict) else reg)}
    assert c['C022']['state'] == 'checked' and c['C072']['state'] == 'checked'
    assert 'security' in ' '.join(c['C072']['value']['proposed'])
    started = c['C022']['value']['first_started'][:5]
    W = 164.0
    colour = {'go': INK, 'partial': AMBER, 'finding': ACCENT}
    body, y = [], 12.0
    for i, ((k, plain, quote, opening), v) in enumerate(zip(STEPS, verdicts)):
        lines = wrap(f'"{quote}{" ..." if opening else ""}"', WRAP)
        h = 9.0 + 3.6 * len(lines)
        lit = v == 'finding'
        body.append(f'<rect x="1" y="{y:.2f}" width="{W - 2:.2f}" height="{h:.2f}" rx="1.5" fill="{FILL if lit else PAPER}" '
                    f'stroke="{ACCENT if lit else FILL2}" stroke-width="{.6 if lit else .35}"/>')
        body.append(t(4, y + 5.0, f'{i + 1}. {plain}', 700, INK))
        body.append(t(58, y + 5.0, f'by: {rec["steps"][k]["by"]}', 400, MUTED, 'start', SMALL))
        body.append(f'<rect x="{W - 22:.2f}" y="{y + 1.6:.2f}" width="19" height="5.0" rx="2.5" fill="{colour[v] if v != "go" else PAPER}" '
                    f'stroke="{colour[v]}" stroke-width=".4"/>')
        body.append(t(W - 12.5, y + 5.0, v, 700, PAPER if v != 'go' else INK, 'middle', SMALL))
        for j, ln in enumerate(lines):
            body.append(t(4, y + 9.8 + 3.6 * j, ln, 400, INK, 'start', SMALL, 'italic'))
        y += h + 2.0
        if i < 4:
            body.append(f'<line x1="8" y1="{y - 2.0:.2f}" x2="8" y2="{y:.2f}" stroke="{MUTED}" stroke-width=".35"/>')
    H = y + 9.0
    SHIFT = 6.0                                                      # the title's band, dropped
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H - SHIFT:.1f}mm" viewBox="0 0 {W:g} {H - SHIFT:.1f}" role="img" '
         'aria-label="The wake record as a page: the conductor\'s first wake, five boxes in a column, each with its step, who ran it '
         'as the record names it, its verdict and a sentence from the record; the verdicts go, go, partial, finding, partial, '
         'the finding in step four highlighted.">',
         f'<g transform="translate(0,-{SHIFT:g})">']                  # no drawn title: the Figure line is the caption (26)
    s += body
    s.append(t(1, H - 5.2, '"by" as the record names it. Security was never staffed: its two steps were reviews', 400, MUTED, 'start', SMALL))
    s.append(t(1, H - 1.8, f'the conductor\'s own wake ran. The record: {RECORD}.', 400, MUTED, 'start', SMALL))
    s.append('</g>')
    s.append('</svg>')
    svg = '\n'.join(s) + '\n'
    if UNSAFE.search(svg):
        sys.exit("refused by the build's rule")
    (HERE / 'edition' / 'wake-page.svg').write_text(svg)
    print('wake-page.svg written')


if __name__ == '__main__':
    main()
