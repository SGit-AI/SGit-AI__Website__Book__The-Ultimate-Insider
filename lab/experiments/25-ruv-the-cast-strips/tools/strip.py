"""The cast in strips (the editor's CH1 and NR1): a script in, a strip of panels out, in the lab's format.

A script (scripts/<name>.json) names its moment and claims, and its panels: who speaks, the designer's drawing of them
(lab/characters/, read only, referenced in place), the pose, the line, and where the line comes from. The words are always
the storyteller's: this tool never writes a line, it only sets one. A line longer than the cast's rule (90 characters)
stops the build. A panel whose drawing does not exist yet is set as a dashed placeholder naming who it waits for.
Every strip carries a "dramatised" band with its moment and claim ids; no number goes in a bubble, as digits or as words,
and the alt text is checked the same way. Two script formats are read: this tool's own (title, moment, claims, panels of
who, drawing, pose, line, from) and the storyteller's (name, form, band, cast, panels of speaker, drawing, pose, line,
source; chapter-plan/cast/scripts/), whose drawings are found in the designer's cast (lab/characters/cast/<member>-<mood>.svg)
by the mood table MOOD below. Pose names are never printed: a pose is a direction to the artist, and some carry numbers.
Usage: python3 -B -I tools/strip.py scripts/a.json [scripts/b.json ...]   (writes pages.html, one sheet per script)
"""
import html, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
CHAR = HERE.parents[1] / 'characters'
MAXLINE = 90
NUMWORDS = re.compile(r'\b(two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|'
                      r'eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion)\b', re.I)
# the storyteller's poses, to the drawings that exist: the designer's four moods, and the conductor's own poses
MOOD = {'worried': 'worried', 'stressed': 'stressed', 'unhappy': 'unhappy', 'happy': 'happy', 'proud': 'happy', 'pacing': 'stressed'}
OWN = {('conductor', 'at ninety-five'): ('conductor-alarmed.svg', 'alarmed'), ('conductor', 'on the minute'): ('conductor-calm.svg', 'calm')}
TITLE = {'interview': 'An interview: {a} and {b}', 'therapy session': 'A therapy session: {a}, after the hold'}


def nonum(text, where):
    if any(ch.isdigit() for ch in text) or NUMWORDS.search(text):
        sys.exit(f'a number in {where}: numbers go in the band with their claim id')


def from_storyteller(s, path):
    """The storyteller's format, set as this tool's own; every word of every line kept."""
    panels = []
    for p in s['panels']:
        if p['speaker'] is None:                                 # the empty chair
            who = next((c.replace(':', ',') for c in s['cast'] if c.startswith('empty chair')), p['drawing'])
            panels.append({'who': 'the ' + who, 'drawing': None, 'mood': 'empty', 'line': p['line'], 'from': p['source'], 'empty': True})
            continue
        m = p['speaker']
        if (m, p['pose']) in OWN:
            drawing, mood = OWN[(m, p['pose'])]
        else:
            mood = MOOD.get(p['pose'], 'worried')
            drawing = f'cast/{m}-{mood}.svg'
        panels.append({'who': 'the ' + m, 'drawing': drawing, 'mood': mood, 'line': p['line'], 'from': p['source']})
    cast = [c for c in s['cast'] if ':' not in c]
    title = TITLE.get(s['form'], s['form']).format(a='the ' + cast[0], b='the ' + (cast[1] if len(cast) > 1 else ''))
    return {'title': title, 'moment': re.sub(r'^Dramatised\.\s*', '', s['band']), 'claims': list(dict.fromkeys(re.findall(r'C\d{3}', s['band']))),
            'panels': panels, 'srcs': f'{path.name}, copied word for word from chapter-plan/cast/scripts/ at 6452450'}


def panel(p):
    who = html.escape(p['who']); line = p['line']
    if len(line) > MAXLINE:
        sys.exit(f'line over {MAXLINE} characters for {who}: the cast\'s rule')
    nonum(line, f'a bubble ({who})')
    mood = p.get('mood') or (Path(p['drawing']).stem.split('-', 1)[1] if p.get('drawing') and Path(p['drawing']).stem.startswith('conductor-') else '')
    alt = who + (', ' + mood if mood else '')
    nonum(alt, f'the alt text ({who})')
    if p.get('empty'):
        fig = (f'<div style="width:19mm;height:24mm;margin:0 auto;border:.4mm dashed var(--muted);display:flex;align-items:center;justify-content:center;'
               f'text-align:center;font:400 9pt/12pt var(--sans);color:var(--muted)">empty</div>')
    elif (CHAR / p['drawing']).exists():
        fig = f'<img src="{{{{dir}}}}/../../characters/{p["drawing"]}" alt="{html.escape(alt)}" style="width:19mm;display:block;margin:0 auto">'
    else:
        fig = (f'<div style="width:19mm;height:24mm;margin:0 auto;border:.4mm dashed var(--muted);display:flex;align-items:center;justify-content:center;'
               f'text-align:center;font:400 9pt/12pt var(--sans);color:var(--muted)">{who}: the designer\'s drawing to come</div>')
    bubble = f'<p class="bubble">{html.escape(line)}</p>' if line else ''
    return (f'  <div style="border:.3mm solid var(--fill-2);border-radius:2mm;padding:2mm 3mm;display:flex;flex-direction:column;gap:1.5mm">{fig}'
            f'<p class="who" style="font:700 10pt/14pt var(--sans);font-variant:small-caps;letter-spacing:.04em;margin:1mm 0 0">{who}</p>{bubble}</div>\n')


def sheet(script):
    s = json.loads(script.read_text())
    if 'speaker' in json.dumps(s.get('panels', [{}])[0]):
        s = from_storyteller(s, script)
    n = min(len(s['panels']), 3)
    froms = sorted({p['from'] for p in s['panels']})
    dirs = {f.split(' (')[0].rsplit('/', 1)[0] for f in froms}
    if s.get('srcs'):
        srcs = s['srcs']
    elif len(dirs) == 1:                                           # one folder: name it once, each letter by its number
        short = sorted({f.split(' (')[0].rsplit('/', 1)[1].split('-')[0] for f in froms})   # each line's place is in the script
        srcs = ', '.join(short) + ', in ' + dirs.pop() + '/'
    else:
        srcs = '; '.join(froms)
    return (f'<section class="page" data-claims="{" · ".join(s["claims"])}">\n'
            f'  <p class="fig-title">{html.escape(s["title"])}</p>\n'
            f'  <div style="display:grid;grid-template-columns:repeat({n},1fr);gap:4mm">\n' + ''.join(panel(p) for p in s['panels']) + '  </div>\n'
            f'  <div class="callout concept" style="margin-top:3mm"><p class="kind">Dramatised</p>'
            f'<p class="co-text">{html.escape(s["moment"])} The scene is drawn from the record; the words are the storyteller\'s ({html.escape(srcs)}), the drawings the designer\'s (lab/characters/).</p></div>\n'
            '</section>\n')


def main():
    scripts = [HERE / a for a in sys.argv[1:]] or sorted((HERE / 'scripts').glob('*.json'))
    (HERE / 'pages.html').write_text(''.join(sheet(s) for s in scripts))


if __name__ == '__main__':
    main()
