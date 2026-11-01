"""LAB 24 (ruv): the talk's day by member and hour, for chapter 2 (the editor's LK1: the member-by-hour chart "tells the story").

Read straight from the researcher's table, claims/talk-commits-by-member-hour.md (C095): every cell printed as it is written
there, nothing re-derived or rounded. One hue, light to dark, for a count; an empty hour is the paper's grey. Night, 00:00 to
05:59, is marked as C092 has it. The "no @member prefix" row and the totals stay, so the columns agree with C092 (182, 468).
Drawn in the manner of the conductor's team/conductor/tools/day_heatmap.py (read, not imported).
Writes heatmap.svg and pages.html. Usage: python3 -B -I tools/build.py
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
TABLE = HERE.parents[2] / 'claims' / 'talk-commits-by-member-hour.md'
RAMP = ['#f3e8e2', '#e8c9b8', '#d9a487', '#c77d58', '#b0481a', '#7d3212']   # the lab's accent, light to dark
INK, MUTED, FILL, FILL2, PAPER = '#1f2933', '#5b6670', '#eef2f6', '#d5dce4', '#ffffff'
SANS = 'Inter, Helvetica, Arial, sans-serif'


def table():
    rows = []
    for line in TABLE.read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) == 21 and cells[0] not in ('Member', '---') and not cells[0].startswith('-'):
            rows.append((cells[0].replace('**', ''), [c.replace('**', '') for c in cells[1:20]], cells[20].replace('**', '')))
    return rows


def t(x, y, s, size=3.2, weight=400, fill=INK, anchor='middle'):
    return f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'


def main():
    rows = table()
    body = [r for r in rows if r[0] != 'all']
    allr = [r for r in rows if r[0] == 'all'][0]
    peak = max(int(v) for _, vs, _ in body for v in vs)
    W, LAB, TOT = 164, 30, 10
    cw = (W - LAB - TOT) / 19
    rh, top = 6.2, 9
    H = top + rh * (len(rows)) + 14
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H:.1f}" role="img" aria-label="The talk\'s commits by member and hour, 29 October, 00:00 to 18:59: every cell counted, one hue light to dark.">']
    s.append(f'<rect x="{LAB:.2f}" y="{top - 6.5}" width="{6 * cw:.2f}" height="{rh * len(rows) + 6.5:.2f}" fill="none" stroke="{MUTED}" stroke-width=".3" stroke-dasharray="1 .7"/>')
    s.append(t(LAB + 3 * cw, top - 2.6 - 4.2, 'night', 3.2, 700, MUTED))
    for h in range(19):
        s.append(t(LAB + (h + .5) * cw, top - 1.6, f'{h:02d}', 3.2, 400, MUTED))
    s.append(t(LAB + 19 * cw + TOT / 2, top - 1.6, 'total', 3.2, 700, MUTED))
    for r, (name, vals, total) in enumerate(rows):
        y = top + r * rh
        label = 'no @member' if name.startswith('other') else name
        bold = 700 if name == 'all' else 400
        s.append(t(LAB - 1.5, y + rh / 2 + 1.1, label, 3.3, 700 if name != 'all' else 800, INK, 'end'))
        for h, v in enumerate(vals):
            n = int(v); x = LAB + h * cw
            if name == 'all':
                fill, txt = PAPER, INK
            elif n == 0:
                fill, txt = FILL, None
            else:
                k = min(len(RAMP) - 1, int((n / peak) * (len(RAMP) - 1) + .5))
                fill, txt = RAMP[k], (PAPER if k >= 3 else INK)
            s.append(f'<rect x="{x + .15:.2f}" y="{y + .15:.2f}" width="{cw - .3:.2f}" height="{rh - .3:.2f}" fill="{fill}"/>')
            if txt:
                s.append(t(x + cw / 2, y + rh / 2 + 1.1, v, 3.18, bold, txt))
        s.append(t(LAB + 19 * cw + TOT / 2, y + rh / 2 + 1.1, total, 3.3, 700, INK))
        if name == 'other (no @member prefix)':
            s.append(f'<line x1="{LAB}" y1="{y + rh:.2f}" x2="{W}" y2="{y + rh:.2f}" stroke="{INK}" stroke-width=".35"/>')
    s.append('</svg>')
    (HERE / 'heatmap.svg').write_text('\n'.join(s) + '\n')
    (HERE / 'pages.html').write_text(
        '<section class="page" data-claims="C095 · C092 · C021">\n <figure class="fig span12">\n'
        '  <p class="fig-title">The talk\'s day, by member and by hour</p>\n'
        '  <img src="{{dir}}/heatmap.svg" alt="The talk\'s commits by member and hour on 29 October, every cell counted" style="width:100%;display:block">\n'
        '  <figcaption><b>Who committed when, 00:00 to 18:59 on 29 October: the night\'s first rush, the steady working morning, and the busy afternoon (C095).</b>'
        '<span class="src">Commits whose subject names a member with @, by commit hour (UTC, also London time that day), at 298be4e; releases and commits with no @member prefix '
        'on their own rows, so the columns add to C092\'s night (182) and day (468). Every number is the researcher\'s table, claims/talk-commits-by-member-hour.md. '
        'Tokens and network calls are not in the record (C021).</span></figcaption>\n'
        ' </figure>\n</section>\n')


if __name__ == '__main__':
    main()
