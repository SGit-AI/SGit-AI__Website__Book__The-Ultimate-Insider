"""LAB 02's three frames of M01 for the 150-page edition's chapter 1 (its Figure line: "the same idea as three frames of the
animation: users wandering and stopping; agents arriving in numbers; the agents not stopping").

The frames are the animation itself frozen on its own clock (frames/, unchanged), embedded as PNG data images on security's
terms (security__016: data:image/png;base64 only, a PNG signature, a still of a piece security allowed; M01 was cleared by
security__001, 30 October). Under each frame, the Figure line's own words; beside the last, security's line from that review,
"Red shows capability, not intent". No number. Writes edition/three-frames.svg; the layout is the designer's to change.
Usage: python3 -B -I tools/edition.py
"""
import base64, html, io, re, sys
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parents[1]
FRAMES = [('m01-light-t22_5.png', 'users wandering and stopping'), ('m01-light-t30.png', 'agents arriving in numbers'),
          ('m01-light-t43.png', 'the agents not stopping')]
INK, MUTED, FILL2 = '#1f2933', '#5b6670', '#d5dce4'
SANS = 'Inter, Helvetica, Arial, sans-serif'
PT = 9 * 25.4 / 72
W, GAP = 164.0, 4.0
PW = (W - 2 * GAP) / 3
ALLOWED = re.compile(r'\bhref\s*=\s*"data:image/png;base64,[A-Za-z0-9+/=]+"')


def main():
    parts, H = [], 0
    for i, (name, words) in enumerate(FRAMES):
        im = Image.open(HERE / 'frames' / name).convert('RGB')
        ih = PW * im.size[1] / im.size[0]
        im = im.resize((960, round(960 * im.size[1] / im.size[0])), Image.LANCZOS)
        buf = io.BytesIO(); im.save(buf, 'PNG', optimize=True)
        data = buf.getvalue()
        assert data[:8] == b'\x89PNG\r\n\x1a\n'
        x = i * (PW + GAP)
        parts.append(f'<image x="{x:.2f}" y="0" width="{PW:.2f}" height="{ih:.2f}" href="data:image/png;base64,{base64.b64encode(data).decode()}"/>')
        parts.append(f'<rect x="{x:.2f}" y="0" width="{PW:.2f}" height="{ih:.2f}" fill="none" stroke="{FILL2}" stroke-width=".3"/>')
        parts.append(f'<text x="{x:.2f}" y="{ih + 2 + PT:.2f}" font-family="{SANS}" font-size="{PT:.3f}" font-weight="700" fill="{INK}">{html.escape(words)}</text>')
        H = max(H, ih + 2 + PT)
    x3 = 2 * (PW + GAP)
    parts.append(f'<text x="{x3:.2f}" y="{H + PT * 1.3:.2f}" font-family="{SANS}" font-size="{PT:.3f}" fill="{MUTED}">Red shows capability, not intent.</text>')
    H = round(H + PT * 1.3 + 1.2, 1)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H:g}mm" viewBox="0 0 {W:g} {H:g}" role="img" '
           'aria-label="The building, three frames of the animation: users wandering and stopping; agents arriving in numbers; the agents not stopping.">\n'
           + '\n'.join(parts) + '\n</svg>\n')
    rest = ALLOWED.sub('', svg)                                    # security__016: no href but PNG data; nothing else of the old rule
    if re.search(r"<script|<foreignObject|\bhref\s*=|\bon[a-z]+\s*=|@import|data:image/svg", rest, re.I):
        sys.exit('outside security__016\'s terms')
    (HERE / 'edition').mkdir(exist_ok=True)
    (HERE / 'edition' / 'three-frames.svg').write_text(svg)
    print('edition/three-frames.svg', f'{W:g} x {H:g} mm')


if __name__ == '__main__':
    main()
