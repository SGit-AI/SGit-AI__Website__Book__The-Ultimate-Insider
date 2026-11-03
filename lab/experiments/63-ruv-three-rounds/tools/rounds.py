"""RC2 seventy, chapter 7 (ruv; the conductor named the owner, conductor__018): one picture's three rounds side by side.

The talk's E02 (the blast radius) in its three versions, each the talk's own end-state still at 298be4e
(team/ruv-sgit/debriefs/img/2026-10-29__e02__end-dark.png, __e02-v2__..., __e02-v3__...; read only), copied in unchanged and
downscaled. Under each, the round's outcome (no count in it) and deck's verdict in its own words, word for word:
  v1  src/pages/studio/reviews/e02.html          "What it is not yet is a picture a room reads in five seconds."
  v2  team/deck/debriefs/2026-10-29__e02-v2-review.md   "Numbered dots, plain words and named rings make it readable."
  v3  src/pages/studio/reviews/e02-v3.html        "Three passes, and every note is in."
The stills' numbers are C084's (grant, mandate, excess, rows measured) and, on v2 and v3, C086's by-kind counts; the dot
numbers are labels, not counts. No mask: LAB 07 kept E02 unmasked (security__005). No time is printed: the review times are
not in the register. Writes stills/*.png, edition/three-rounds.svg (164 mm wide, the stills embedded) and pages.html.
Usage: python3 -B -I tools/rounds.py --talk <clone of the talk's repository>
"""
import base64, html, io, subprocess, sys
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parents[1]
AT = '298be4e'
INK, MUTED, FILL2, ACCENT = '#1f2933', '#5b6670', '#d5dce4', '#b0481a'
SANS = 'Inter, Helvetica, Arial, sans-serif'
PT = 9 * 25.4 / 72
LEAD = PT * 1.25
ROUNDS = [
    ('v1', 'e02', 'The first round: sent back', 'What it is not yet is a picture a room reads in five seconds.', '78b89b9'),
    ('v2', 'e02-v2', 'The second: kept, with notes for the next', 'Numbered dots, plain words and named rings make it readable.', 'eefc1d3'),
    ('v3', 'e02-v3', 'The third: kept, ready for the editor', 'Three passes, and every note is in.', '19e7f2d'),
]
W, GAP = 164.0, 4.0
PW = (W - 2 * GAP) / 3
IH = PW * 720 / 1280


def wrap(s, width, cw):
    out, cur = [], ''
    for w in s.split():
        tr = (cur + ' ' + w).strip()
        if len(tr) * cw <= width: cur = tr
        else: out.append(cur); cur = w
    return out + ([cur] if cur else [])


def main():
    clone = sys.argv[sys.argv.index('--talk') + 1]
    imgs = []
    for v, stem, *_ in ROUNDS:
        raw = subprocess.run(['git', '-C', clone, 'show', f'{AT}:team/ruv-sgit/debriefs/img/2026-10-29__{stem}__end-dark.png'],
                             capture_output=True, check=True).stdout
        im = Image.open(io.BytesIO(raw)).convert('RGB').resize((960, 540), Image.LANCZOS)
        im.save(HERE / 'stills' / f'e02-{v}.png', optimize=True)
        buf = io.BytesIO(); im.save(buf, 'PNG', optimize=True)
        imgs.append(base64.b64encode(buf.getvalue()).decode())
    rows = []
    hmax = 0
    for i, (v, stem, outcome, quote, commit) in enumerate(ROUNDS):
        x = i * (PW + GAP)
        ol = wrap(outcome, PW, PT * .56)
        ql = wrap('“' + quote + '”', PW, PT * .6)
        y = IH + 2.2 + PT
        parts = [f'<image x="{x:.2f}" y="0" width="{PW:.2f}" height="{IH:.2f}" href="data:image/png;base64,{imgs[i]}"/>',
                 f'<rect x="{x:.2f}" y="0" width="{PW:.2f}" height="{IH:.2f}" fill="none" stroke="{FILL2}" stroke-width=".3"/>']
        for ln in ol:
            parts.append(f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{PT:.3f}" font-weight="700" fill="{ACCENT if i == 0 else INK}">{html.escape(ln)}</text>'); y += LEAD
        y += .8
        for ln in ql:
            parts.append(f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{PT:.3f}" font-style="italic" fill="{INK}">{html.escape(ln)}</text>'); y += LEAD
        parts.append(f'<text x="{x:.2f}" y="{y + .6:.2f}" font-family="{SANS}" font-size="{PT:.3f}" fill="{MUTED}">deck, {commit}</text>')
        hmax = max(hmax, y + 2)
        rows += parts
    H = round(hmax + 1, 1)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H:g}mm" viewBox="0 0 {W:g} {H:g}" role="img" '
           'aria-label="One picture\'s three rounds side by side: the talk\'s blast radius picture, sent back, kept with notes, and kept for the editor, '
           'with deck\'s verdict under each in its own words.">\n' + '\n'.join(rows) + '\n</svg>\n')
    (HERE / 'edition' / 'three-rounds.svg').write_text(svg)
    figs = ''.join(f'<figure style="margin:0;flex:1"><img src="{{{{dir}}}}/stills/e02-{v}.png" alt="E02 {v}, its last frame" style="width:100%;display:block;border:.3mm solid var(--fill-2)">'
                   f'<p style="font:700 9pt/12pt var(--sans);margin:1.5mm 0 .5mm">{html.escape(o)}</p>'
                   f'<p style="font:italic 9pt/12pt var(--sans);margin:0">“{html.escape(q)}”</p>'
                   f'<p style="font:400 9pt/12pt var(--sans);color:var(--muted);margin:.5mm 0 0">deck, {c}</p></figure>'
                   for v, s, o, q, c in ROUNDS)
    (HERE / 'pages.html').write_text(
        '<section class="page" data-claims="C084 · C086">\n <figure class="fig span12">\n'
        '  <p class="fig-title">One picture\'s three rounds</p>\n'
        f'  <div style="display:flex;gap:4mm">{figs}</div>\n'
        '  <figcaption><b>The same data three times: a table beside a diagram, then numbered dots in named rings, then the dots grouped by what is at risk. '
        'Nobody was watching, and the picture was sent back, kept with notes, and kept for the editor.</b> '
        'The dot numbers are labels, not counts.'
        '<span class="src">The talk\'s own stills at 298be4e (team/ruv-sgit/debriefs/img/); deck\'s words from its review pages and debrief there. '
        'The stills\' numbers: C084 (grant, mandate, excess, rows measured) and C086 (the excess by kind).</span></figcaption>\n </figure>\n</section>\n')
    print('three-rounds.svg', f'{W:g} x {H:g} mm', 'and pages.html')


if __name__ == '__main__':
    main()
