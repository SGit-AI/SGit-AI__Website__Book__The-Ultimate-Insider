"""The cast in strips (the editor's CH1 and NR1): a script in, a strip of panels out, in the lab's format.

A script (scripts/<name>.json) names its moment and claims, and its panels: who speaks, the designer's drawing of them
(lab/characters/, read only, referenced in place), the pose, the line, and where the line comes from. The words are always
the storyteller's: this tool never writes a line, it only sets one. A line longer than the cast's rule (90 characters)
stops the build. A panel whose drawing does not exist yet is set as a dashed placeholder naming who it waits for.
Every strip carries a "dramatised" band with its moment and claim ids; no number goes in a bubble.
Usage: python3 -B -I tools/strip.py scripts/a.json [scripts/b.json ...]   (writes pages.html, one sheet per script)
"""
import html, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
CHAR = HERE.parents[1] / 'characters'
MAXLINE = 90


def panel(p):
    who = html.escape(p['who']); line = p['line']
    if len(line) > MAXLINE:
        sys.exit(f'line over {MAXLINE} characters for {who}: the cast\'s rule')
    if any(ch.isdigit() for ch in line):
        sys.exit(f'a number in a bubble ({who}): numbers go in the body with their claim id')
    if (CHAR / p['drawing']).exists():
        fig = f'<img src="{{{{dir}}}}/../../characters/{p["drawing"]}" alt="{who}{", " + html.escape(p["pose"]) if p.get("pose") else ""}" style="width:30mm;display:block;margin:0 auto">'
    else:
        fig = (f'<div style="width:30mm;height:37mm;margin:0 auto;border:.4mm dashed var(--muted);display:flex;align-items:center;justify-content:center;'
               f'text-align:center;font:400 9pt/12pt var(--sans);color:var(--muted)">{who}: the designer\'s drawing to come</div>')
    return (f'  <div style="border:.3mm solid var(--fill-2);border-radius:2mm;padding:3mm;display:flex;flex-direction:column;gap:2mm">{fig}'
            f'<p class="who" style="font:700 10pt/14pt var(--sans);font-variant:small-caps;letter-spacing:.04em;margin:1mm 0 0">{who}'
            + (f' <span style="font-weight:400;color:var(--muted)">· {html.escape(p["pose"])}</span>' if p.get('pose') else '')
            + f'</p><p class="bubble">{html.escape(line)}</p></div>\n')


def sheet(script):
    s = json.loads(script.read_text())
    n = len(s['panels'])
    srcs = '; '.join(sorted({p['from'] for p in s['panels']}))
    return (f'<section class="page" data-claims="{" · ".join(s["claims"])}">\n'
            f'  <p class="fig-title">{html.escape(s["title"])}</p>\n'
            f'  <div style="display:grid;grid-template-columns:repeat({n},1fr);gap:4mm">\n' + ''.join(panel(p) for p in s['panels']) + '  </div>\n'
            f'  <div class="callout concept" style="margin-top:5mm"><p class="kind">Dramatised</p>'
            f'<p class="co-text">{html.escape(s["moment"])} The scene is drawn from the record; the words are the storyteller\'s, the drawings the designer\'s.</p></div>\n'
            f'  <p style="font:400 9pt/12pt var(--sans);color:var(--muted)">Lines from: <span class="mono">{html.escape(srcs)}</span>. Drawings: <span class="mono">lab/characters/</span>.</p>\n'
            '</section>\n')


def main():
    scripts = [HERE / a for a in sys.argv[1:]] or sorted((HERE / 'scripts').glob('*.json'))
    (HERE / 'pages.html').write_text(''.join(sheet(s) for s in scripts))


if __name__ == '__main__':
    main()
