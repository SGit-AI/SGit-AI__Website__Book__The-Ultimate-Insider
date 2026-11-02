"""The reviewer card (ruv), for RC2's chapter 3, page 2: the clipboard and the researcher, in two panels.

The words are the writer's (card.json, copied exactly from writer__020); the drawings are the designer's, made by
lab/characters/make_cast.py (imported read only: figure() and reviewer_figure(), the reviewer as the researcher's own figure
with a clipboard, designer__086). One SVG, 164 mm wide, about 60 mm tall, text at 9 pt, no number in any text. A line the writer
marks as the record's carries "(record)" beside it. Writes card.svg and pages.html.
Usage: python3 -B -I tools/card.py
"""
import html, importlib.util, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
LAB = HERE.parents[1]
spec = importlib.util.spec_from_file_location('make_cast', LAB / 'characters' / 'make_cast.py')
mc = importlib.util.module_from_spec(spec); spec.loader.exec_module(mc)           # definitions only; its __main__ never runs
sys.path.insert(0, str(LAB / 'experiments' / '25-ruv-the-cast-strips' / 'tools'))
import strip                                                                        # the number rule

W, H, GAP = 164.0, 58.0, 4.0
PT = 9 * 25.4 / 72
LEAD = PT * 1.25
CHARW = PT * 0.53
INK, MUTED, FILL, FILL2, ACCENT = '#1f2933', '#5b6670', '#eef2f6', '#d5dce4', '#b0481a'
SANS = 'Inter, Helvetica, Arial, sans-serif'


def wrap(line, width):
    out, cur = [], ''
    for w in line.split():
        trial = (cur + ' ' + w).strip()
        if len(trial) * CHARW <= width: cur = trial
        else: out.append(cur); cur = w
    return out + ([cur] if cur else [])


def fig(elements, x, y, h):
    return f'<svg x="{x:.2f}" y="{y:.2f}" width="{h * .8:.2f}" height="{h:.2f}" viewBox="0 0 40 50">{elements}</svg>'


def bubble(x, y, w, text, extra=''):
    lines = wrap(text, w - 3)
    out = [f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{len(lines) * LEAD + 2.2:.2f}" rx="1.4" fill="{FILL}"/>']
    for j, ln in enumerate(lines):
        out.append(f'<text x="{x + 1.4:.2f}" y="{y + 1.1 + PT + j * LEAD:.2f}" font-family="{SANS}" font-size="{PT:.3f}" fill="{INK}">{html.escape(ln)}</text>')
    if extra:
        out.append(f'<text x="{x + w:.2f}" y="{y + len(lines) * LEAD + 2.2 + PT + .6:.2f}" font-family="{SANS}" font-size="{PT:.3f}" font-style="italic" fill="{MUTED}" text-anchor="end">{extra}</text>')
    return out, len(lines) * LEAD + 2.2


def main():
    d = json.loads((HERE / 'card.json').read_text())
    reg = json.loads((LAB.parent / 'claims' / 'register.json').read_text())
    c107 = {c['id']: c for c in (reg['claims'] if isinstance(reg, dict) else reg)}['C107']
    assert c107['state'] == 'checked'
    t = re.search(r'(\d{2}:\d{2}):\d{2}', c107['value']['researcher_dispute']['pre_review_first']).group(1)   # 04:11
    for p in d['panels']:
        p['small'] = p['small'].replace('{C107}', t)
    pw = (W - GAP) / 2
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H:g}mm" viewBox="0 0 {W:g} {H:g}" role="img" '
         'aria-label="A card of panels: the reviewer with a clipboard and the researcher; first the objection, then the objection withdrawn. Dramatised: the words are the writer\'s, the drawings the designer\'s.">']
    for i, p in enumerate(d['panels']):
        x0 = i * (pw + GAP)
        s.append(f'<rect x="{x0 + .2:.2f}" y=".2" width="{pw - .4:.2f}" height="{H - .4:.2f}" rx="1.6" fill="none" stroke="{FILL2}" stroke-width=".3"/>')
        r, q = p['reviewer'], p['researcher']
        for text in (r['line'], q['line'], re.sub(r'\b[0-9a-f]{7}\b|\b\d{2}:\d{2}\b', '', p['small'])):   # the hash and C107's time are traced   # a commit hash names the record; it is not a number
            strip.nonum(text, 'the card')
        # the clipboard, left; the researcher, right
        s.append(fig(mc.reviewer_figure('researcher', r['mood']), x0 + 3, 3, 20))
        s.append(fig(mc.figure('researcher', q['mood']), x0 + pw - 19, 3, 20))
        s.append(f'<text x="{x0 + 3:.2f}" y="{27.4:.2f}" font-family="{SANS}" font-size="{PT:.3f}" font-weight="700" fill="{INK}">the reviewer</text>')
        s.append(f'<text x="{x0 + pw - 3:.2f}" y="{27.4:.2f}" font-family="{SANS}" font-size="{PT:.3f}" font-weight="700" fill="{INK}" text-anchor="end">the researcher</text>')
        b1, h1 = bubble(x0 + 2, 29.5, pw * .42, r['line'], '(record)' if r['record'] else '')
        b2, h2 = bubble(x0 + pw * .46, 29.5, pw * .54 - 2, q['line'])
        s += b1 + b2
        if 29.5 + max(h1 + (LEAD if r['record'] else 0), h2) > H - 7:
            sys.exit(f'panel {i + 1}: the lines do not fit at 9 pt')
        s.append(f'<text x="{x0 + 2:.2f}" y="{H - 2.2:.2f}" font-family="{SANS}" font-size="{PT:.3f}" fill="{MUTED}">{html.escape(p["small"])}</text>')
    s.append('</svg>')
    svg = '\n'.join(s) + '\n'
    strip.nonum(re.search(r'aria-label="([^"]*)"', svg).group(1), 'the card\'s label')
    (HERE / 'card.svg').write_text(svg)
    (HERE / 'pages.html').write_text(
        '<section class="page" data-claims="C107">\n <figure class="fig span12">\n'
        '  <p class="fig-title">The argument with a reviewer</p>\n'
        '  <img src="{{dir}}/card.svg" alt="The reviewer with a clipboard and the researcher: the objection, then the objection withdrawn" style="width:100%;display:block">\n'
        '  <figcaption><b>Left, the reviewer calls a file out of scope; right, it withdraws the objection, and the dispute goes into the record.</b> '
        'Dramatised: the words are the writer\'s, and "objection withdrawn." is the record\'s; both readings came at 04:11 (C107).'
        '<span class="src">The writer\'s lines (writer__020, chapter 3 of the thirty); the record, af0010b and the researcher\'s wake record; the drawings, '
        'lab/characters/make_cast.py (the reviewer as the researcher\'s own figure with a clipboard).</span></figcaption>\n </figure>\n</section>\n')
    print('card.svg and pages.html written')


if __name__ == '__main__':
    main()
