"""LAB (ruv, id to be named): the talk as given, by speaker, for chapter 10 (the editor's LK1: an infographic-driven book).

The talk's 102 passages as one strip across the page, each shaded by who spoke (the editor, the room, the host), the three
parts marked above it. From the talk repository's team/conductor/talk-record/transcript.json at a9c0b49 (material added
after the day, generated from the recording; read only): only each passage's start time and speaker class are read; no
words, no names. Passages that share a start time share its interval equally. The last passage's end is not stamped.
Printed numbers: C069's registered counts only, and minute ticks on the axis.
Usage: python3 -B -I tools/build.py --talk <clone of the talk's repository>
Writes passages.json (time and class only), strip.svg and pages.html.
"""
import json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
INK, MUTED, FILL, FILL2, ACCENT, PAPER = '#1f2933', '#5b6670', '#eef2f6', '#d5dce4', '#b0481a', '#ffffff'
SANS = 'Inter, Helvetica, Arial, sans-serif'
AT = 'a9c0b49'
COL = {'editor': INK, 'room': ACCENT, 'host': '#9aa5b1'}
W, X0, END = 164, 2, 88 * 60                                     # the axis runs to 88 minutes; the last passage starts at 1:27:10 (C069)


def secs(t):
    parts = [int(p) for p in t.split(':')]
    return parts[0] * 60 + parts[1] if len(parts) == 2 else parts[0] * 3600 + parts[1] * 60 + parts[2]


def t(x, y, s, size=3.3, weight=400, fill=INK, anchor='start'):
    return f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'


def read(clone):
    P = json.loads(subprocess.run(['git', '-C', clone, 'show', f'{AT}:team/conductor/talk-record/transcript.json'],
                                  capture_output=True, text=True, check=True).stdout)
    md = subprocess.run(['git', '-C', clone, 'show', f'{AT}:content/articles/the-talk-as-given.md'], capture_output=True, text=True, check=True).stdout
    import re
    parts = [secs(m) for m in re.findall(r'id="part-\d"[^\n]*?<p class="tr-t">([0-9:]+)', md.replace('\n', ' ', 0)) ]
    if not parts:                                                # the part heading and its first passage are on separate lines
        lines = md.splitlines()
        for i, l in enumerate(lines):
            if 'id="part-' in l:
                m = re.search(r'<p class="tr-t">([0-9:]+)', ' '.join(lines[i:i + 3]))
                parts.append(secs(m.group(1)))
    return [{'t': p['t'], 'who': p['who']} for p in P], parts


def main():
    clone = sys.argv[sys.argv.index('--talk') + 1]
    passages, parts = read(clone)
    (HERE / 'passages.json').write_text(json.dumps({'source': f'talk repository team/conductor/talk-record/transcript.json at {AT} (time and speaker class only)',
                                                    'passages': passages, 'part_starts_s': parts}, indent=1) + '\n')
    k = (W - 2 * X0) / END
    x = lambda s: X0 + s * k
    Y, HGT = 22, 20                                             # 20 mm: at 12 the strip read as a rule (the designer, designer__047)
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 65" role="img" aria-label="The talk as given, about 87 minutes, '
         'as a strip of its 102 passages shaded by speaker: the editor, the room, the host; three parts marked above.">']
    s.append(f'<rect x="{x(0):.2f}" y="{Y}" width="{x(END) - x(0):.2f}" height="{HGT}" fill="{FILL}"/>')
    starts = sorted({secs(p['t']) for p in passages})
    for i, st in enumerate(starts):
        en = starts[i + 1] if i + 1 < len(starts) else secs('1:27:10') + 50       # the last passage: a short block, its end not stamped
        group = [p for p in passages if secs(p['t']) == st]
        w = (x(en) - x(st)) / len(group)
        for j, p in enumerate(group):
            s.append(f'<rect x="{x(st) + j * w:.3f}" y="{Y}" width="{max(w - .12, .15):.3f}" height="{HGT}" fill="{COL[p["who"]]}"/>')
    s.append(t(W - X0, Y + HGT + 9.4, 'the last passage\'s end is not stamped', 3.18, 400, MUTED, 'end'))
    for m in range(0, 90, 15):                                   # minute ticks
        s.append(f'<line x1="{x(m * 60):.2f}" y1="{Y + HGT}" x2="{x(m * 60):.2f}" y2="{Y + HGT + 1.4}" stroke="{MUTED}" stroke-width=".3"/>')
        s.append(t(x(m * 60), Y + HGT + 4.6, f'{m} min' if m else '0', 3.18, 400, MUTED, 'middle' if m else 'start'))
    bounds = parts + [END]
    for i, (a, b) in enumerate(zip(bounds, bounds[1:])):         # the parts, above the strip
        s.append(f'<path d="M{x(a) + .4:.2f} {Y - 2} V{Y - 4} H{x(b) - .4:.2f} V{Y - 2}" fill="none" stroke="{INK}" stroke-width=".35"/>')
        s.append(t((x(a) + x(b)) / 2, Y - 5.6, ['Part one', 'Part two', 'Part three'][i], 3.3, 700, INK, 'middle'))
    ly = 60
    for i, (who, n, label) in enumerate((('editor', 83, 'the editor'), ('room', 18, 'the room'), ('host', 1, 'the host'))):
        lx = X0 + i * 46
        s.append(f'<rect x="{lx:.2f}" y="{ly - 2.8}" width="3.4" height="3.4" fill="{COL[who]}"/>' + t(lx + 5, ly, f'{label}: {n} passage' + ('s' if n != 1 else ''), 3.3))
    s.append('</svg>')
    (HERE / 'strip.svg').write_text('\n'.join(s) + '\n')
    (HERE / 'pages.html').write_text(
        '<section class="page" data-claims="C069">\n <figure class="fig span12">\n'
        '  <p class="fig-title">The talk as given: who spoke, minute by minute</p>\n'
        '  <img src="{{dir}}/strip.svg" alt="The talk\'s 102 passages as a strip shaded by speaker, with its three parts" style="width:100%;display:block">\n'
        '  <figcaption><b>About 87 minutes, 102 passages: 83 the editor\'s, 18 from the room, 1 the host\'s (C069). The room spoke during the talk as well as after it.</b>'
        f'<span class="src">The talk repository\'s team/conductor/talk-record/transcript.json at {AT}, added after the day and generated from the recording (C069); '
        'only each passage\'s start time and speaker class are read, no words and no names. Passages that share a start time share its interval.</span></figcaption>\n'
        ' </figure>\n</section>\n')


if __name__ == '__main__':
    main()
