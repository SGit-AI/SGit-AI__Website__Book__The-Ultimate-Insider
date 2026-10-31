"""Write LAB 07's pages.html: one tile per piece, its own last frame, or a slot while its numbers are not in the register.
A mask is a box drawn over the frame where the register says a figure cannot be printed; the PNG itself is unchanged.
Usage: python3 -I lab/experiments/07-ruv-contact-sheet/tools/pages.py
"""
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
W = 80                                                        # mm, a tile's width; two fit the 167 mm text block; a frame is 16:9

# (title, source path, commit, frame, caption). Masks are burned into the frames by tools/mask.py, so none is drawn here.
NUMBER_FREE = [
 ('E01: what an agent is, the rings of reach', 'studio/lab/e01/v1', '0ffa9c8', 'studio-lab-e01-t48.png',
  'The steps from a chat model to agents calling agents, as rings of reach.'),
 ('E14: earning autonomy', 'studio/lab/e14/v1', '5247af0', 'studio-lab-e14-t52.png',
  'A licence to operate, earned level by level. The piece says itself it is illustrative: no real agent, person or date.'),
 ('E06: hard outside, soft inside', 'studio/lab/e06/v1', 'c516b20', 'studio-lab-e06-t50.png',
  'A perimeter built to stop what comes from outside; the piece says itself it is illustrative.'),
 ('E08: the lethal trifecta, made visible', 'studio/lab/e08/v1', 'c33e86a', 'studio-lab-e08-t48.png',
  'Three switches on, and one path open; the idea is Simon Willison\'s, as the piece says.'),
]
REGISTERED = [
 ('E09: mandate against grant', 'studio/lab/e09/v1', '842a8bd', 'studio-lab-e09-t54.png',
  'Derived, as the frame says (C082).'),
 ('E10: four barriers', 'studio/lab/e10/v1', 'eaf914f', 'studio-lab-e10-t52.png',
  'Derived (C082). Its 14, 1 and 0 are the barrier kinds with confirmations off.'),
 ('SHarness: what exists and what is coming', 'studio/lab/sharness/components/v1', '842a8bd', 'studio-lab-sharness-t50.png',
  'SHarness\'s own report on the editor\'s own project (C083).'),
 ('E11: the kernel was told first', 'studio/lab/e11/v1', '842a8bd', 'studio-lab-e11-t50.png',
  'The project\'s report of its probes (C083, C082); the step numbers are not counts.'),
 ('E02: the blast radius, from the grant rows', 'studio/lab/e02/v1', '0ffa9c8', 'studio-lab-e02-t54.png',
  'A published draft\'s rows, derived (C084).'),
 ('E07: one box, and everything it reaches', 'studio/lab/e07/v1', 'eaf914f', 'studio-lab-e07-t46.png',
  'Two published examples; only the CI job\'s rows were measured (C084).'),
 ('E13: five published examples', 'studio/lab/e13/v1', '842a8bd', 'studio-lab-e13-t48.png',
  'The same chart for each; no rating, no ranking (C084).'),
 ('E12: the radius, contained', 'studio/lab/e12/v1', '842a8bd', 'studio-lab-e12-t52.png',
  'Today\'s excess by kind (C086). Masked: the piece\'s own projection of what a designed wall would leave, which no data file states.'),
 ('E03: every source is a way in', 'studio/lab/e03/v1', 'a606774', 'studio-lab-e03-t48.png',
  'The ring of sources only (C085); the side panel\'s per-source detail is left out, at security\'s word.'),
 ('The policy gate (studio v4)', 'studio-ports/lab/policy-gate', '0fe0fff', 'studio-ports-lab-policy-gate-t36.png',
  'ruv.sgit.ai\'s POC1, a demonstration run, not the talk team\'s own actions (C078).'),
 ('One action\'s journey', 'studio-ports/lab/journey', '0fe0fff', 'studio-ports-lab-journey-t34.png',
  'The same POC1 demonstration run, three of its actions; the hashes are identifiers (C078).'),
 ('ABP: real actions hit it, with receipts', 'studio-ports/lab/abp', '0fe0fff', 'studio-ports-lab-abp-t26.png',
  'An Agent Behaviour Policy compiled into Ruflo\'s engine (C079). Masked: one figure, not traced.'),
 ('How the register of people works', 'studio-ports/lab/pki', '901bec1', 'studio-ports-lab-pki-t15.png',
  'pki.sgit.ai\'s register of people and keys (C080).'),
 ('The editor approves each policy, item by item', 'studio-ports/lab/abp-review', 'bd3cdad', 'studio-ports-lab-abp-review-t16.png',
  'Masked: a sentence the files contradict (C081), and the form\'s own counters (not registered). Its 1, 2, 3 are steps.'),
]
SLOTS = [
 ('E04: the over-enthusiastic agent', 'studio/lab/e04/v1', 'c33e86a', 'Figures from published reports of outside cases; the researcher checks each at its source.'),
]
GRID = f'<div style="display:grid;grid-template-columns:{W}mm {W}mm;gap:5mm 7mm">\n'
TITLE = '<p style="font:700 9.5pt/13pt var(--sans);margin:0 0 1mm">{}</p>'


def src(path, commit):
    return f'<span class="src">src/static/{path} at {commit}, its last frame</span>'


def still(title, path, commit, img, cap):
    return (f'  <figure class="fig" style="margin:0">{TITLE.format(title)}'
            f'<img src="{{{{dir}}}}/frames/{img}" alt="{title}, its last frame" style="width:{W}mm;display:block;border:.3mm solid var(--fill-2)">'
            f'<figcaption>{cap}{src(path, commit)}</figcaption></figure>\n')


def slot(title, path, commit, cap):
    return (f'  <figure class="fig" style="margin:0">{TITLE.format(title)}<div style="width:{W}mm;height:24mm;border:.4mm dashed var(--muted);'
            'background:var(--fill);display:flex;align-items:center;justify-content:center;text-align:center;padding:4mm;'
            'font:400 9.5pt/13pt var(--sans);color:var(--muted)">Waiting on the register: its last frame prints numbers not yet in claims/.</div>'
            f'<figcaption>{cap}{src(path, commit)}</figcaption></figure>\n')


NOTE = ('<p style="margin-top:6mm;font:400 9pt/12pt var(--sans);color:var(--muted)">Masks are grey boxes burned into the frames where the '
        'register says a figure may not be printed. Not on the sheet: E05, out of the lab at security\'s word; B01, the designer\'s LAB 04; '
        'the port showcases without a timeline (abp-enforcement, abp-prose, fork, invest, open-source), which are pages, not animations.</p>\n')
html = (f'<section class="page" data-claims="">\n{GRID}' + ''.join(still(*x) for x in NUMBER_FREE) + '</div>\n' + NOTE + '</section>\n'
        f'<section class="page" data-claims="C078 · C079 · C080 · C081 · C082 · C083 · C084 · C085 · C086">\n{GRID}'
        + ''.join(still(*x) for x in REGISTERED) + ''.join(slot(*x) for x in SLOTS) + '</div>\n</section>\n')
(HERE / 'pages.html').write_text(html)
