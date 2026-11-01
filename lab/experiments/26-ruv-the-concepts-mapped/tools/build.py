"""LAB 26 (ruv): chapter 13's concepts, mapped to the chapters that show them (the editor's LK1; ruv.sgit's visual plan).

Reads manuscript/13-concepts-and-principles.md (read only): every concept under "## The concepts", in its group, and the chapters
its entry names before "Where it is thin" (where the book shows it; the thin part is left out, so a line means "shown here").
Draws one picture: the concepts down the left in their five groups, the chapters down the right in the book's order, a line
from each concept to each chapter it names. No count is printed. Writes concepts.json, map.svg and pages.html.
Usage: python3 -B -I tools/build.py
"""
import json, re
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
INK, MUTED, FILL, FILL2, ACCENT, PAPER = '#1f2933', '#5b6670', '#eef2f6', '#d5dce4', '#b0481a', '#ffffff'
SANS = 'Inter, Helvetica, Arial, sans-serif'
W, ROW, GAP, PT9 = 164, 4.15, 1.6, 3.18
TONES = ['#2f6f8f', '#b0481a', '#5b6670', '#7a5c99', '#3d7a4f']   # one tone per concept group (the designer's note, designer__056)
LX, RX = 64, 108                                   # where the concept labels end and the chapter labels start (mm)


SHORT = {'The brief, the reality file and the corrections file': 'The brief, reality and corrections'}   # the one label too long for the column


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def t(x, y, s, size=PT9, weight=400, fill=INK, anchor='start'):
    return f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{esc(s)}</text>'


def read():
    man = ROOT / 'manuscript'
    chapters = []
    for f in (man / 'Book.txt').read_text().split():
        title = (man / f).read_text().splitlines()[0].lstrip('# ').strip()
        m = re.match(r'(\d+b?|Appendix A)\.? (.*)', title)
        key = f.split('-')[0]                                         # 0, 00, 00b, 01 ... 11b, 13, 99
        num = {'0': 'about', '00': '0', '00b': 'map', '11b': '11b', '13': '13', '99': 'A'}.get(key, str(int(key)) if key.isdigit() else key)
        chapters.append({'key': num, 'title': title})
    text = (man / '13-concepts-and-principles.md').read_text().split('## The concepts')[1].split('## The principles')[0]
    groups, cur = [], None
    for l in text.splitlines():
        if l.startswith('### '):
            cur = {'group': l[4:].strip(), 'concepts': []}
            groups.append(cur)
        m = re.match(r'\*\*(.+?)\*\*', l)
        if m and cur:
            shows = l.split('Where it is thin')[0]
            keys = []
            if 'page before chapter 0' in shows:
                keys.append('about')
                shows = shows.replace('page before chapter 0', '')
            for run in re.findall(r'[Cc]hapters? ([0-9]+b?(?:(?:, | and | to |, and )[0-9]+b?)*)', shows):
                keys += re.findall(r'[0-9]+b?', run)
            if 'Appendix A' in shows:
                keys.append('A')
            name = re.sub(r'\s*\(.*\)$', '', m.group(1).rstrip('.'))
            name = SHORT.get(name, name)
            cur['concepts'].append({'name': name, 'chapters': list(dict.fromkeys(keys))})
    return chapters, groups


def draw(chapters, groups):
    used = {k for g in groups for c in g['concepts'] for k in c['chapters']}
    chs = [c for c in chapters if c['key'] in used]
    y, rows, s_left = 4, {}, []
    for gi, g in enumerate(groups):
        s_left.append(t(0, y + 1.1, g['group'].upper(), PT9, 700, TONES[gi % len(TONES)]))
        y += ROW
        for c in g['concepts']:
            rows[c['name']] = y
            s_left.append(t(LX - 2, y + 1.1, c['name'], PT9, 400 if c['chapters'] else 400, INK if c['chapters'] else MUTED, 'end'))
            y += ROW
        y += GAP
    H = y + 2
    step = (H - 8) / max(len(chs) - 1, 1)
    cy = {c['key']: 4 + i * step for i, c in enumerate(chs)}
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H:.1f}" role="img" aria-label="Chapter 13\'s concepts down the left '
         'in their five groups, the book\'s chapters down the right, a line from each concept to each chapter that shows it.">']
    for gi, g in enumerate(groups):
        tone = TONES[gi % len(TONES)]
        for c in g['concepts']:
            y0 = rows[c['name']]
            for k in c['chapters']:
                y1 = cy[k]
                s.append(f'<path d="M{LX:.2f} {y0:.2f} C{(LX + RX) / 2:.2f} {y0:.2f} {(LX + RX) / 2:.2f} {y1:.2f} {RX - 2:.2f} {y1:.2f}" '
                         f'fill="none" stroke="{tone}" stroke-width=".3" opacity=".75"/>')
            s.append(f'<circle cx="{LX:.2f}" cy="{y0:.2f}" r=".7" fill="{tone if c["chapters"] else PAPER}" stroke="{tone}" stroke-width=".25"/>')
    for c in chs:
        y1 = cy[c['key']]
        s.append(f'<circle cx="{RX - 2:.2f}" cy="{y1:.2f}" r=".9" fill="{ACCENT}"/>')
        s.append(t(RX, y1 + 1.1, c['title'], PT9))
    s += s_left
    s.append('</svg>')
    return '\n'.join(s) + '\n', H


def main():
    chapters, groups = read()
    (HERE / 'concepts.json').write_text(json.dumps({'source': 'manuscript/13-concepts-and-principles.md and manuscript/Book.txt (read only)',
                                                    'chapters': chapters, 'groups': groups}, indent=1, ensure_ascii=False) + '\n')
    svg, H = draw(chapters, groups)
    (HERE / 'map.svg').write_text(svg)
    alone = [c['name'] for g in groups for c in g['concepts'] if not c['chapters']]
    note = (f' An open dot ({", ".join(alone)}) is explained only in chapter 13 itself.' if alone else '')
    (HERE / 'pages.html').write_text(
        '<section class="page" data-claims="">\n <figure class="fig span12">\n'
        '  <p class="fig-title">Where each idea lives in the book</p>\n'
        '  <img src="{{dir}}/map.svg" alt="Chapter 13\'s concepts in five groups, each joined to the chapters that show it" style="width:100%;display:block">\n'
        '  <figcaption><b>Find a word on the left; follow its lines, in its group\'s tone, to the chapters that show it at work. The chapters with the most lines are '
        'where the book\'s ideas meet.</b>' + note +
        '<span class="src">manuscript/13-concepts-and-principles.md: each concept\'s entry, the chapters it names before "Where it is thin" '
        '(where the day was thin is left out, so a line means "shown here"); chapter titles from manuscript/Book.txt. Built by tools/build.py; '
        'it changes as the chapter does.</span></figcaption>\n </figure>\n</section>\n')


if __name__ == '__main__':
    main()
