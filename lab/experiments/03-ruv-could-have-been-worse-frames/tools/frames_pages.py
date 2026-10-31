"""Write pages.html for a frames experiment (LAB 05, LAB 06): each frame at the text block's full width, cropped below its
own headline (the top 18 percent, in CSS: the PNG is unchanged), and the headline printed once, under the frame, with the time.
Usage: python3 -I lab/experiments/03-ruv-could-have-been-worse-frames/tools/frames_pages.py <experiment folder>
The folder holds frames.json: {"claims": "...", "frames": [[png, "0:11", "the words", "what to see"], ...], "caption": "...", "src": "..."}
"""
import json, sys
from pathlib import Path

d = Path(sys.argv[1]).resolve()
spec = json.loads((d / 'frames.json').read_text())
CROP = 0.18                                    # the frame's top band: the talk's kicker and headline
W, H = 2560, 1440


def frame(png, t, words, see):
    return (f'  <figure class="fig" style="margin:0 0 5mm">'
            f'<div style="overflow:hidden;width:100%;aspect-ratio:{W}/{round(H * (1 - CROP))};border:.3mm solid var(--fill-2)">'
            f'<img src="{{{{dir}}}}/frames/{png}" alt="{words} (the frame at {t})" style="display:block;width:100%;margin-top:-{CROP * H / W * 100:.3f}%"></div>'
            f'<figcaption><b>{t}</b> &nbsp; {words}<span class="src" style="font-family:var(--sans)">{see}</span></figcaption></figure>\n')


html = (f'<section class="page" data-claims="{spec.get("claims", "")}">\n' + ''.join(frame(*f) for f in spec['frames'])
        + f'  <p style="font:400 9pt/12pt var(--sans);color:var(--muted);margin-top:2mm"><b style="color:var(--ink)">{spec["caption"]}</b> '
        + f'<span class="mono">{spec["src"]}</span></p>\n</section>\n')
(d / 'pages.html').write_text(html)
