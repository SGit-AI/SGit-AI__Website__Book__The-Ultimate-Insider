"""LAB 02's three frames of M01 for the full book's chapter 1 (its Figure line: "the same idea as three frames of the
animation: users wandering and stopping; agents arriving in numbers; the agents not stopping").

The frames are the animation itself frozen on its own clock (frames/, unchanged), embedded as PNG data images on security's
terms (security__016). No caption is drawn under the frames: the Figure line is the caption (principle 26). Under them, the
red legend in full as security gives it (security__019, from its 001): "Red: doing damage" and "Red shows capability, not
intent: the talk's agents were a benign team." No number. The drawing is checked with publishing/edition.py's own
unsafe_svg, loaded by its file path. Writes edition/three-frames.svg; the layout is the designer's to change.
Usage: python3 -B -I tools/edition.py
"""
import base64, html, importlib.util, io, re, sys
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
_spec = importlib.util.spec_from_file_location('edition', ROOT / 'publishing' / 'edition.py')
_edition = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_edition)
LEGEND = ['Red: doing damage', 'Red shows capability, not intent: the talk\'s agents were a benign team.']
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
        H = max(H, ih)
    for j, ln in enumerate(LEGEND):                                 # the legend in full, from the left, across the width
        parts.append(f'<text x="0" y="{H + 2 + PT * (1 + 1.3 * j):.2f}" font-family="{SANS}" font-size="{PT:.3f}" '
                     f'font-weight="{700 if j == 0 else 400}" fill="{INK if j == 0 else MUTED}">{html.escape(ln)}</text>')
    H = round(H + 2 + PT * (1 + 1.3 * (len(LEGEND) - 1)) + 1.6, 1)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H:g}mm" viewBox="0 0 {W:g} {H:g}" role="img" '
           'aria-label="The building, three frames of the animation: users wandering and stopping; agents arriving in numbers; the agents not stopping.">\n'
           + '\n'.join(parts) + '\n</svg>\n')
    why = _edition.unsafe_svg(svg)                                 # the build's own rule: PNG data with its signature only
    if why:
        sys.exit(f"refused by the build's rule: {why}")
    (HERE / 'edition').mkdir(exist_ok=True)
    (HERE / 'edition' / 'three-frames.svg').write_text(svg)
    print('edition/three-frames.svg', f'{W:g} x {H:g} mm')


if __name__ == '__main__':
    main()
