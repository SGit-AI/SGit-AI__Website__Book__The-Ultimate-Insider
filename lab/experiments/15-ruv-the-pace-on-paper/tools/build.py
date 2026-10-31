"""LAB 15 (ruv): the site's pace grid, on paper (the editor's RC1 review, T18: "the site's view of every agent as a row with
coloured dots for its events gives the size and momentum at a glance; reuse it").

Two grids, drawn as the site's dashboard draws its pace (admin/build/build.py, "The pace"): a row per member, a column per
hour (UTC, which on these days is also London time), one stack of five dots per wake (plan, pre-review, work, post-review,
post-check). Night hours are shaded. A wake is classed as the researcher's C087 classes the talk's: its kind starts
"scheduled"; or it names a follow-up (or "tonight's rule"); else it was started by the editor (boxed in the accent; a
follow-up is boxed dashed).
  sheet 1  the talk's day, 29 October, from the talk repository's wake records at 298be4e (read only, via git show),
           with C092's registered night-against-day counts beside it
  sheet 2  this book's team, from its own wake records (team/*/wakes/*.json, read only); no count printed
Writes pace-talk.svg, pace-team.svg and pages.html.
Usage: python3 -I tools/build.py --talk <clone of the talk's repository> [--until <ISO UTC>]
"""
import glob, json, subprocess, sys
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
INK, MUTED, FILL, FILL2, ACCENT, PAPER = '#1f2933', '#5b6670', '#eef2f6', '#d5dce4', '#b0481a', '#ffffff'
SANS = 'Inter, Helvetica, Arial, sans-serif'
STEPS = ['plan', 'pre_review', 'work', 'post_review', 'post_check']
GOOD = {'go', 'done', 'clean', 'as-planned'}
AMBER = {'change', 'partial', 'finding', 'off-plan', 'none'}
W, LABEL, ROW, TOP = 164, 24, 8.2, 12
TALK_AT = '298be4e'


def t(x, y, s, size=3.3, weight=400, fill=INK, anchor='start'):
    return f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'


def dot(x, y, v):
    r = .5
    if v in GOOD:
        return f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="{INK}"/>'
    if v == 'stop':
        return f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r + .1}" fill="{ACCENT}"/>'
    if v in AMBER:
        return f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r - .08}" fill="{PAPER}" stroke="{INK}" stroke-width=".22"/>'
    return f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r - .1}" fill="{FILL2}"/>'


def trigger(w):
    """C087's classes: scheduled, follow-up, or started by the editor."""
    k = (w.get('kind') or '').lower()
    return 'scheduled' if k.startswith('scheduled') or 'scheduled' in k else 'follow-up' if ('follow' in k or 'tonight' in k) else 'editor'


def grid(ws, order, first, last, night):
    hours = [first + timedelta(hours=i) for i in range(int((last - first).total_seconds() // 3600) + 1)]
    col = (W - LABEL) / len(hours)
    members = [m for m in order if any(w['agent'] == m for w in ws)] + sorted({w['agent'] for w in ws} - set(order))
    H = TOP + ROW * len(members) + 10
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H:.1f}" role="img" aria-label="A pace grid: a row per member, '
         'a column per hour, a stack of five verdict dots per wake; night shaded; wakes started by the editor boxed.">']
    step = 3 if len(hours) <= 24 else 6
    for i, h in enumerate(hours):
        x = LABEL + i * col
        if night(h):
            s.append(f'<rect x="{x:.2f}" y="{TOP - 2}" width="{col:.3f}" height="{ROW * len(members) + 2}" fill="{FILL}"/>')
        if h.hour % step == 0:
            s.append(f'<line x1="{x:.2f}" y1="{TOP - 2}" x2="{x:.2f}" y2="{TOP + ROW * len(members):.2f}" stroke="{FILL2}" stroke-width=".25"/>')
            s.append(t(x + .4, TOP - 3.2, f'{h.hour:02d}:00', 3.2, 400, MUTED) if x < W - 10 else t(W, TOP - 3.2, f'{h.hour:02d}:00', 3.2, 400, MUTED, 'end'))
        if h.hour == 0 or i == 0:
            s.append(t(x + .4, TOP - 7.6, h.strftime('%d %b').lstrip('0'), 3.3, 700, INK))
    for r, m in enumerate(members):
        y0 = TOP + r * ROW
        s.append(t(0, y0 + ROW / 2 + 1.1, m, 3.3, 700))
        s.append(f'<line x1="{LABEL}" y1="{y0 + ROW:.2f}" x2="{W}" y2="{y0 + ROW:.2f}" stroke="{FILL2}" stroke-width=".2"/>')
        for i, h in enumerate(hours):
            inh = sorted((w for w in ws if w['agent'] == m and w['started'][:13] == h.strftime('%Y-%m-%dT%H')), key=lambda w: w['started'])
            for k, w in enumerate(inh):
                x = LABEL + i * col + .9 + k * 1.25
                if x > LABEL + (i + 1) * col - .4:
                    break                                            # a busy hour: the cell shows what fits
                for j, st in enumerate(STEPS):
                    s.append(dot(x, y0 + 1.6 + j * 1.2, w.get('steps', {}).get(st, {}).get('verdict', 'missing')))
                tr = trigger(w)
                if tr != 'scheduled':
                    dash = ' stroke-dasharray=".5 .35"' if tr == 'follow-up' else ''
                    s.append(f'<rect x="{x - .75:.2f}" y="{y0 + .7:.2f}" width="1.5" height="{5 * 1.2 + .4:.2f}" fill="none" stroke="{ACCENT}" stroke-width=".25"{dash}/>')
    ly = TOP + ROW * len(members) + 6
    s.append(dot(LABEL + 1, ly - 1.1, 'go') + t(LABEL + 2.6, ly, 'go, done, clean, as-planned', 3.2, 400, MUTED))
    s.append(dot(LABEL + 47, ly - 1.1, 'partial') + t(LABEL + 48.6, ly, 'change, partial, finding', 3.2, 400, MUTED))
    s.append(dot(LABEL + 86, ly - 1.1, 'stop') + t(LABEL + 87.6, ly, 'stop', 3.2, 400, MUTED))
    s.append(f'<rect x="{LABEL + 99:.2f}" y="{ly - 3.2:.2f}" width="1.5" height="3.6" fill="none" stroke="{ACCENT}" stroke-width=".25"/>'
             + t(LABEL + 101.8, ly, 'started by the editor', 3.2, 400, MUTED))
    s.append('</svg>')
    return '\n'.join(s) + '\n'


def talk_wakes(clone):
    files = subprocess.run(['git', '-C', clone, 'ls-tree', '-r', '--name-only', TALK_AT, '--', 'team'], capture_output=True, text=True, check=True).stdout.split()
    out = []
    for f in files:
        if '/wakes/' in f and f.endswith('.json'):
            out.append(json.loads(subprocess.run(['git', '-C', clone, 'show', f'{TALK_AT}:{f}'], capture_output=True, text=True, check=True).stdout))
    return out


def main():
    args = sys.argv[1:]
    clone = args[args.index('--talk') + 1]
    until = args[args.index('--until') + 1] if '--until' in args else None

    talk = talk_wakes(clone)
    day = datetime(2026, 10, 29)
    (HERE / 'pace-talk.svg').write_text(grid(talk, ['conductor', 'researcher', 'deck', 'storyteller', 'designer', 'motion', 'studio', 'ruv-sgit', 'dev'],
                                              day, day + timedelta(hours=18), lambda h: h.hour < 6))
    team = [json.load(open(f)) for f in glob.glob(str(ROOT / 'team' / '*' / 'wakes' / '*.json'))]
    team = [w for w in team if w.get('closed') and w.get('started') and (until is None or w['started'] <= until)]
    first = datetime.fromisoformat(min(w['started'] for w in team)[:13] + ':00:00')
    last = datetime.fromisoformat(max(w['started'] for w in team)[:13] + ':00:00')
    (HERE / 'pace-team.svg').write_text(grid(team, ['conductor', 'researcher', 'storyteller', 'historian', 'librarian', 'security', 'publisher',
                                                    'designer', 'ruv-sgit', 'developer', 'synthetic'],
                                             first, last, lambda h: h.hour >= 22 or h.hour < 6))
    stamp = max(w['started'] for w in team)[:16].replace('T', ' ')
    tiles = ''.join(f'<div class="tile" style="margin:0"><b>{a}</b>{b}<span class="cid">C092</span></div>'
                    for a, b in (('Commits', 'night 225 · day 589'), ('Releases', 'night 61 · day 149'),
                                 ('Wakes', 'night 35 · day 127')))
    (HERE / 'pages.html').write_text(
        '<section class="page" data-claims="C087 · C092 · C021">\n <figure class="fig span12">\n'
        '  <img src="{{dir}}/pace-talk.svg" alt="The talk team\'s pace on 29 October, every wake as a stack of five verdict dots" style="width:100%;display:block">\n'
        '  <figcaption><b>Read across for one member, down for one hour; each stack of five dots is one wake. Shaded is night, before 06:00. '
        'A boxed stack was started by the editor, a dashed box is a follow-up; the rest ran on the schedule (C087).</b>'
        '<span class="src">The talk repository\'s team/*/wakes/*.json at 298be4e (read only), the record\'s end; classed as C087. A busy hour shows the wakes that fit its cell.</span></figcaption>\n'
        ' </figure>\n'
        f'  <div class="rail" style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:4mm;margin-top:3mm">{tiles}</div>\n'
        '  <p style="font:400 9pt/12pt var(--sans);color:var(--muted);margin-top:3mm">Night is 00:16 to 05:59, day 06:00 to 18:59 (C092). '
        'Tokens and network calls are not in the record (C021): there is no usage page and no token count, so the page shows none rather than a blank.</p>\n'
        '</section>\n'
        '<section class="page" data-claims="">\n <figure class="fig span12">\n'
        '  <p class="fig-title">This book\'s team, the same view</p>\n'
        '  <img src="{{dir}}/pace-team.svg" alt="This book\'s team\'s pace, every closed wake as a stack of five verdict dots" style="width:100%;display:block">\n'
        '  <figcaption><b>The same grid for the team that writes this book: night (22:00 to 06:00) shaded, wakes started by the editor boxed.</b>'
        f'<span class="src">This book\'s team\'s own wake records (team/*/wakes/*.json) up to the wake begun {stamp} UTC. No count is printed.</span></figcaption>\n'
        ' </figure>\n</section>\n')


if __name__ == '__main__':
    main()
