"""The full book's chapter 12 (and wherever a Figure line names it): a card of the editor's eight afternoon asks, redrawn at
the conductor's 025 (the editor, 4 November: show what each ask built, the major ones marked, and the time from his ask to the
work landing, "even if you add more time, it doesn't matter").

Every value is read at build from C118 (checked): per ask, the time he asked, what was built (C118's words), the time from his
ask to the work (C118's words, whole), whether it was major (the historian's rule, not the editor's, printed in the caption),
and where work was not placed in the talk before the hold; then the two larger asks of the feedback round, about 13:50. Each
row has a bar for the time from his ask to the first work, drawn from that time with no number of its own; the scale runs to
the longest. Row 5, "at his minute", has a tick and no bar. The time runs to the work, not to the conductor's routing (C118's
landed_vs_routed); the caption says so. No commit id is printed: they are cut from C118's text. Text is escaped; the drawing
is checked with publishing/edition.py's own unsafe_svg, and the tool refuses itself if it would be refused. Writes
edition/asks-card.svg only.
Usage: python3 -B -I tools/asks.py
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
TINY = 6.8 * 25.4 / 72
_spec = importlib.util.spec_from_file_location('edition', ROOT / 'publishing' / 'edition.py')
_edition = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_edition)
unsafe_svg = _edition.unsafe_svg
HASH = re.compile(r'\b[0-9a-f]{7}\b')
TIME = re.compile(r'(\d+) min (\d+) s')


def t(x, y, s, size=PT, weight=400, fill=INK, anchor='start', style=''):
    st = f' font-style="{style}"' if style else ''
    return (f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{size:.3f}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}"{st}>{escape(str(s), quote=False)}</text>')


def wrap(s, n):
    out, line = [], ''
    for w in s.split():
        if line and len(line) + 1 + len(w) > n:
            out.append(line)
            line = w
        else:
            line = f'{line} {w}'.strip()
    return out + [line]


def first_minutes(s):
    m = TIME.search(s)
    return int(m.group(1)) + int(m.group(2)) / 60 if m else 0.0


def main():
    reg = json.loads((ROOT / 'claims' / 'register.json').read_text())
    c = {x['id']: x for x in (reg['claims'] if isinstance(reg, dict) else reg)}['C118']
    assert c['state'] == 'checked'
    v = c['value']
    rows, larger = v['rows'], v['larger_asks']
    assert len(rows) == 8 and len(larger) == 2
    for r in rows + larger:
        assert not HASH.search(r['what']), r['what']                 # no commit id in what is printed
    scale = max(first_minutes(r['ask_to_work']) for r in rows + larger)
    W, x0 = 164.0, 3.0
    xt, xw, xb, bw = x0, x0 + 13.0, x0 + 13.0, 92.0                  # time asked; what; bar start and full width
    xr = W - x0                                                      # right edge: the major mark

    def row(r, y, asked):
        out = []
        major = str(r['major']).startswith(('yes', 'showcases yes'))
        what = wrap(r['what'], 86)
        out.append(t(xt, y, asked, PT, 700, ACCENT if major else INK))
        for j, ln in enumerate(what):
            out.append(t(xw, y + j * 3.7, ln, SMALL, 600 if major else 400, INK))
        if major:
            out.append(f'<rect x="{xr - 12.5:.2f}" y="{y - 3.0:.2f}" width="12.5" height="4.0" rx="2" fill="{ACCENT}"/>')
            out.append(t(xr - 6.25, y - .1, 'major', TINY, 700, PAPER, 'middle'))
        yb = y + len(what) * 3.7 + .6
        mins = first_minutes(r['ask_to_work'])
        if mins > 0:
            out.append(f'<rect x="{xb:.2f}" y="{yb - 1.9:.2f}" width="{bw * mins / scale:.2f}" height="1.9" fill="{ACCENT if major else MUTED}"/>')
        else:
            out.append(f'<line x1="{xb:.2f}" y1="{yb - 2.6:.2f}" x2="{xb:.2f}" y2="{yb + .6:.2f}" stroke="{MUTED}" stroke-width=".5"/>')
        tl = wrap(r['ask_to_work'], 92)
        tx = xb + (bw * mins / scale if mins > 0 else 0) + 1.5
        if tx + len(tl[0]) * 1.25 > xr:                              # long times go under the bar
            tx = xb
            yb += 3.4
        for j, ln in enumerate(tl):
            out.append(t(tx if j == 0 else xb, yb + j * 3.2, ln, TINY, 400, MUTED, 'start', 'italic'))
        yn = yb + (len(tl) - 1) * 3.2
        notes = []
        if 'showcases yes' in str(r['major']):
            notes.append(r['major'])
        work = r.get('work', '')
        if 'none of the three showcases placed' in work:
            notes.append('none of the three showcases placed in the talk before the hold')
        elif 'not placed' in work and r['n'] == 2:
            notes.append('the first page placed; the two later showcases not placed before the hold')
        for j, n in enumerate(notes):
            out.append(t(xb, yn + 3.4 + j * 3.2, n, TINY, 400, ACCENT, 'start', 'italic'))
        return out, yn + 3.4 + len(notes) * 3.2 + 2.6

    body, y = [], 16.0
    body.append(t(xt, y - 4.0, 'asked', TINY, 700, MUTED))
    body.append(t(xw, y - 4.0, 'what was built, and the time from his ask to the work', TINY, 700, MUTED))
    body.append(f'<line x1="{x0}" y1="{y - 2.6:.2f}" x2="{xr}" y2="{y - 2.6:.2f}" stroke="{FILL2}" stroke-width=".3"/>')
    for r in rows:
        out, y = row(r, y + 1.4, r['asked'])
        body += out
    y += 2.0
    body.append(t(xt, y, 'Two larger asks from the feedback round, about 13:50', SMALL, 700, INK))
    body.append(f'<line x1="{x0}" y1="{y + 1.4:.2f}" x2="{xr}" y2="{y + 1.4:.2f}" stroke="{FILL2}" stroke-width=".3"/>')
    y += 4.4
    for r in larger:
        out, y = row(r, y + 1.4, '13:50')
        body += out
    notes = ['The time runs from his ask to the work, not to the conductor\'s routing; each bar runs to the first work.',
             '"Major", the historian\'s rule, not the editor\'s: a new slide or page, or at least 100 lines of product files.',
             'Every value: the register, C118.']
    y += 1.0
    for j, n in enumerate(notes):
        body.append(t(x0, y + j * 3.5, n, TINY, 400, MUTED, 'start', 'italic' if j < 2 else ''))
    H = y + len(notes) * 3.5 + 1.5
    label = ('His afternoon asks: for each, what was built, the major ones marked, and the time from his ask to the work; '
             'then the two larger asks of the feedback round.')
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H:.1f}mm" viewBox="0 0 {W:g} {H:.1f}" role="img" '
         f'aria-label="{escape(label, quote=True)}">',
         t(x0, 6.2, 'His afternoon asks, and what each one built', PT * 1.15, 800, INK)]
    s += body
    s.append('</svg>')
    svg = '\n'.join(s) + '\n'
    assert not HASH.search(re.sub(r'#[0-9a-f]{6}', '', svg)), 'a commit id would print'
    why = unsafe_svg(svg)
    if why:
        sys.exit(f"refused by the build's rule: {why}")
    (HERE / 'edition' / 'asks-card.svg').write_text(svg)
    print('asks-card.svg written')


if __name__ == '__main__':
    main()
