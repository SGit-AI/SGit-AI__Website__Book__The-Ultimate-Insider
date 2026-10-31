"""Burn LAB 07's masks into the frames, so no committed file shows what the register says may not be printed.
Reads the raw captures (2560 x 1440, made by capture_http.js, kept outside the repository) and writes frames/ here.
A mask is a box in the lab's fill-2 grey with a muted outline; a blank is the frame's own background (a panel left out).
Usage: python3 -I lab/experiments/07-ruv-contact-sheet/tools/mask.py <raw captures folder>
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw

RAW, OUT = Path(sys.argv[1]), Path(__file__).resolve().parents[1] / 'frames'
FILL, LINE = (213, 220, 228), (91, 102, 112)

# frame: [(kind, (x0, y0, x1, y1), why)] in the raw frame's pixels
EDITS = {
 'studio-ports-lab-abp-t26.png': [('mask', (896, 393, 958, 442), 'C079: the figure beside verb.object.reach is not traced')],
 'studio-ports-lab-abp-review-t16.png': [
   ('mask', (2058, 300, 2448, 352), 'C081: the files contradict the sentence'),
   ('mask', (1766, 351, 2201, 410), 'C081: the files contradict the sentence'),
   ('mask', (256, 1057, 858, 1269), 'the form\'s own counters are not in the register')],
 'studio-lab-e12-t52.png': [
   ('mask', (1900, 356, 2482, 602), 'C086: "8 of 12 still bounded by nothing" is the piece\'s projection, in no data file'),
   ('mask', (1268, 1228, 2262, 1394), 'the same projection, "(8 of 12)", and the eight still-lit rows that count it (security__007)'),
   ('mask', (56, 1326, 1184, 1414), 'the same projection, "4 rows go dark, 8 stay lit"')],
 'studio-lab-e04-t50.png': [
   ('mask', (1976, 662, 2526, 1026), 'C090: the losses of four cases the talk team did not check at source (Antigravity, Codex, OpenClaw, Meta)'),
   ('mask', (48, 1304, 2330, 1361), 'the frame\'s own count of its cases, not in the register')],
 'studio-lab-e03-t48.png': [('blank', (1520, 360, 2560, 1400), 'security: the ring only, not the side panel\'s per-source detail')],
}
KEEP = ['studio-lab-e01-t48.png', 'studio-lab-e14-t52.png', 'studio-lab-e06-t50.png', 'studio-lab-e08-t48.png',
        'studio-lab-e09-t54.png', 'studio-lab-e10-t52.png', 'studio-lab-sharness-t50.png', 'studio-lab-e02-t54.png',
        'studio-lab-e07-t46.png', 'studio-lab-e11-t50.png', 'studio-lab-e13-t48.png',
        'studio-ports-lab-policy-gate-t36.png', 'studio-ports-lab-journey-t34.png', 'studio-ports-lab-pki-t15.png']

for name in KEEP + list(EDITS):
    im = Image.open(RAW / name).convert('RGB')
    d = ImageDraw.Draw(im)
    bg = im.getpixel((8, 700))
    for kind, box, _ in EDITS.get(name, []):
        if kind == 'mask':
            d.rectangle(box, fill=FILL, outline=LINE, width=4)
        else:
            d.rectangle(box, fill=bg)
    im.save(OUT / name, optimize=True)
print('frames written:', len(KEEP) + len(EDITS))
