"""The cast strips for the editions (ED1): one script in, one sized SVG out, for the publisher to place on an edition page.

The designer's brief (designer__069): one SVG per strip that states its size, at most 164 mm wide and about 60 mm tall so the
scene's words share the page, text at most 9.5 pt (and, as everywhere in the lab, at least 9 pt). Six panels in a row: the
designer's drawing (lab/characters, read only, inlined here so the file stands alone, its own label removed), who speaks,
and the line, word for word from the storyteller's script. The band stays on the edition page, not in the strip.
The tool refuses a line that does not fit its bubble, any number in a bubble (digits or words), and any size outside the brief.
Usage: python3 -B -I tools/edition.py scripts/<script>.json edition/<name>.svg
"""
import html, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
CHAR = HERE.parents[1] / 'characters'
sys.path.insert(0, str(HERE / 'tools'))
import strip                                                         # the lab tool: its pose table and its number rule

W, H, GAP = 164.0, 60.0, 1.6
PT = 9.0 * 25.4 / 72                                                 # 9 pt in mm
LEAD = PT * 1.25
CHARW = PT * 0.53                                                    # an average glyph in the sans, for wrapping; checked by rendering
INK, MUTED, FILL, FILL2 = '#1f2933', '#5b6670', '#eef2f6', '#d5dce4'
SANS = 'Inter, Helvetica, Arial, sans-serif'


def drawing(name, x, y, w, h):
    """The designer's drawing, inlined: its outer svg kept for the viewBox, its label and role removed."""
    src = (CHAR / name).read_text()
    m = re.search(r'<svg\b([^>]*)>(.*)</svg>', src, re.S)
    vb = re.search(r'viewBox="([^"]+)"', m.group(1)).group(1)
    return (f'<svg x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" viewBox="{vb}" preserveAspectRatio="xMidYMid meet">'
            f'{m.group(2).strip()}</svg>')


def wrap(line, width):
    out, cur = [], ''
    for word in line.split():
        trial = (cur + ' ' + word).strip()
        if len(trial) * CHARW <= width:
            cur = trial
        else:
            out.append(cur); cur = word
    return out + ([cur] if cur else [])


def main():
    script, outp = HERE / sys.argv[1], HERE / sys.argv[2]
    s = strip.from_storyteller(json.loads(script.read_text()), script)
    panels = s['panels']
    pw = (W - GAP * (len(panels) - 1)) / len(panels)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H:g}mm" viewBox="0 0 {W:g} {H:g}" role="img" '
           f'aria-label="{html.escape(s["title"])}, a strip of panels. Dramatised: the words are the storyteller\'s, the drawings the designer\'s.">']
    for i, p in enumerate(panels):
        x = i * (pw + GAP)
        strip.nonum(p['line'], f'a bubble ({p["who"]})')
        out.append(f'<rect x="{x:.2f}" y="0.2" width="{pw:.2f}" height="{H - .4:.2f}" rx="1.6" fill="none" stroke="{FILL2}" stroke-width=".3"/>')
        if p.get('empty'):
            out.append(f'<rect x="{x + pw / 2 - 6.5:.2f}" y="2.5" width="13" height="16" fill="none" stroke="{MUTED}" stroke-width=".35" stroke-dasharray="1 .8"/>')
        else:
            out.append(drawing(p['drawing'], x + pw / 2 - 7, 2, 14, 17.5))
        who = p['who'].replace('the ', '', 1) if p['who'].startswith('the ') else p['who']
        names = wrap(who, (pw - 3.6) / 1.08)                          # bold runs wider
        for j, nm in enumerate(names):
            out.append(f'<text x="{x + 1.8:.2f}" y="{22.6 + j * LEAD:.2f}" font-family="{SANS}" font-size="{PT:.3f}" font-weight="700" fill="{INK}">{html.escape(nm)}</text>')
        if p['line']:
            lines = wrap(p['line'], pw - 4.4)
            top = 25.0 + (len(names) - 1) * LEAD
            bh = len(lines) * LEAD + 2.2
            if top + bh > H - 1.2:
                sys.exit(f'the line for {p["who"]} does not fit its bubble at 9 pt: the brief is about 60 mm tall')
            out.append(f'<rect x="{x + 1:.2f}" y="{top:.2f}" width="{pw - 2:.2f}" height="{bh:.2f}" rx="1.4" fill="{FILL}"/>')
            for j, ln in enumerate(lines):
                out.append(f'<text x="{x + 2.2:.2f}" y="{top + 1.1 + PT + j * LEAD:.2f}" font-family="{SANS}" font-size="{PT:.3f}" fill="{INK}">{html.escape(ln)}</text>')
    out.append('</svg>')
    svg = '\n'.join(out) + '\n'
    strip.nonum(re.search(r'aria-label="([^"]*)"', svg).group(1), 'the strip\'s label')
    assert W <= 164 and H <= 62 and 'font-size="3.1' in svg
    outp.parent.mkdir(exist_ok=True)
    outp.write_text(svg)
    print(f'{outp.relative_to(HERE)}: {len(panels)} panels, {W:g} x {H:g} mm')


if __name__ == '__main__':
    main()
