"""Write LAB 07's pages.html: one tile per piece, its own last frame, or a slot while its numbers are not in the register.
A mask is a box drawn over the frame where the register says a figure cannot be printed; the PNG itself is unchanged.
Usage: python3 -I lab/experiments/07-ruv-contact-sheet/tools/pages.py
"""
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
W = 85                                                        # mm, a tile's width; a frame is 16:9

# (title, source path, commit, frame or None, caption, masks as (left, top, width, height) in % of the frame)
STILLS_1 = [
 ('E01: what an agent is, the rings of reach', 'studio/lab/e01/v1', '0ffa9c8', 'studio-lab-e01-t48.png',
  'The steps from a chat model to agents calling agents, as rings of reach.', []),
 ('E14: earning autonomy', 'studio/lab/e14/v1', '5247af0', 'studio-lab-e14-t52.png',
  'A licence to operate, earned level by level. The piece says itself it is illustrative: no real agent, person or date.', []),
]
STILLS_2 = [
 ('The policy gate (studio v4)', 'studio-ports/lab/policy-gate', '0fe0fff', 'studio-ports-lab-policy-gate-t36.png',
  'ruv.sgit.ai\'s POC1, a demonstration run, not the talk team\'s own actions (C078).', []),
 ('One action\'s journey', 'studio-ports/lab/journey', '0fe0fff', 'studio-ports-lab-journey-t34.png',
  'The same POC1 demonstration run, three of its actions; the hashes are identifiers (C078).', []),
 ('ABP: real actions hit it, with receipts', 'studio-ports/lab/abp', '0fe0fff', 'studio-ports-lab-abp-t26.png',
  'An Agent Behaviour Policy compiled into Ruflo\'s engine (C079). One figure masked: not traced.', [(35.0, 27.2, 2.4, 3.4)]),
 ('How the register of people works', 'studio-ports/lab/pki', '901bec1', 'studio-ports-lab-pki-t15.png',
  'pki.sgit.ai\'s register of people and keys (C080).', []),
 ('The editor approves each policy, item by item', 'studio-ports/lab/abp-review', 'bd3cdad', 'studio-ports-lab-abp-review-t16.png',
  'Masked: a sentence the files contradict (C081), and the form\'s own counters (not registered). Its 1, 2, 3 are steps, not counts.',
  [(80.4, 21.0, 15.2, 3.6), (69.3, 24.4, 15.4, 4.1), (10.0, 73.4, 23.5, 15.0)]),
]
SLOTS = [
 ('E09: mandate against grant', 'studio/lab/e09/v1', '842a8bd', 'Counts of a policy\'s rows (mandate, grant, excess).'),
 ('E10: four barriers', 'studio/lab/e10/v1', 'eaf914f', 'Counts of rows behind each barrier.'),
 ('SHarness: what exists and what is coming', 'studio/lab/sharness/components/v1', '842a8bd', 'A test count and dates.'),
]
GRID = f'<div style="display:grid;grid-template-columns:{W}mm {W}mm;gap:5mm 8mm">\n'
TITLE = '<p style="font:700 9.5pt/13pt var(--sans);margin:0 0 1mm">{}</p>'


def src(path, commit):
    return f'<span class="src">src/static/{path} at {commit}, its last frame</span>'


def still(title, path, commit, img, cap, masks):
    boxes = ''.join(f'<div style="position:absolute;left:{l}%;top:{t}%;width:{w}%;height:{h}%;background:var(--fill-2);'
                    f'outline:.3mm solid var(--muted)"></div>' for l, t, w, h in masks)
    return (f'  <figure class="fig" style="margin:0">{TITLE.format(title)}<div style="position:relative;width:{W}mm">'
            f'<img src="{{{{dir}}}}/frames/{img}" alt="{title}, its last frame" style="width:{W}mm;display:block;border:.3mm solid var(--fill-2)">'
            f'{boxes}</div><figcaption>{cap}{src(path, commit)}</figcaption></figure>\n')


def slot(title, path, commit, cap):
    return (f'  <figure class="fig" style="margin:0">{TITLE.format(title)}<div style="width:{W}mm;height:24mm;border:.4mm dashed var(--muted);'
            'background:var(--fill);display:flex;align-items:center;justify-content:center;text-align:center;padding:4mm;'
            'font:400 9.5pt/13pt var(--sans);color:var(--muted)">Waiting on the register: its last frame prints numbers not yet in claims/.</div>'
            f'<figcaption>{cap}{src(path, commit)}</figcaption></figure>\n')


NOTE = ('<p style="margin-top:6mm;font:400 9pt/12pt var(--sans);color:var(--muted)">Not on the sheet yet: the talk\'s studio pieces that security '
        'cleared (e02 to e04, e06 to e08, e11 to e13) wait to be sorted; e05 stays out of the lab at security\'s word; B01 is the designer\'s '
        'LAB 04; the port showcases without a timeline (abp-enforcement, abp-prose, fork, invest, open-source) are pages, not animations.</p>\n')
html = (f'<section class="page" data-claims="">\n{GRID}' + ''.join(still(*s) for s in STILLS_1) + '</div>\n' + NOTE + '</section>\n'
        f'<section class="page" data-claims="C078 · C079 · C080 · C081">\n{GRID}' + ''.join(still(*s) for s in STILLS_2)
        + slot(*SLOTS[0]) + '</div>\n</section>\n'
        f'<section class="page" data-claims="">\n{GRID}' + ''.join(slot(*s) for s in SLOTS[1:]) + '</div>\n</section>\n')
(HERE / 'pages.html').write_text(html)
