"""LAB 15 (ruv): the site's pace grid, on paper (the editor's RC1 review, T18: "the site's view of every agent as a row with
coloured dots for its events gives the size and momentum at a glance; reuse it").

Drawn from this book team's own wake records (team/*/wakes/*.json, read only), as the dashboard draws them
(admin/build/build.py, "The pace"): a row per member, a column per hour (UTC, which on these days is also London time),
one stack of five dots per closed wake (plan, pre-review, work, post-review, post-check). Night hours (22:00 to 06:00) are
shaded; a wake started from the editor's chat is boxed, apart from scheduled ones (T18's two kinds of trigger).
No count is printed: only the hours and the members' role names. Writes pace.svg and pages.html.
Usage: python3 -I tools/build.py [--until <ISO UTC>]   (default: every closed wake on disk)
"""
import glob, json, sys
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


def main():
    until = sys.argv[sys.argv.index('--until') + 1] if '--until' in sys.argv else None
    ws = [json.load(open(f)) for f in glob.glob(str(ROOT / 'team' / '*' / 'wakes' / '*.json'))]
    ws = [w for w in ws if w.get('closed') and w.get('started') and (until is None or w['started'] <= until)]
    first = datetime.fromisoformat(min(w['started'] for w in ws)[:13] + ':00:00')
    last = datetime.fromisoformat(max(w['started'] for w in ws)[:13] + ':00:00')
    hours = [first + timedelta(hours=i) for i in range(int((last - first).total_seconds() // 3600) + 1)]
    col = (W - LABEL) / len(hours)
    order = ['conductor', 'researcher', 'storyteller', 'historian', 'librarian', 'security', 'publisher', 'designer', 'ruv-sgit',
             'developer', 'synthetic']
    members = [m for m in order if any(w['agent'] == m for w in ws)] + sorted({w['agent'] for w in ws} - set(order))
    H = TOP + ROW * len(members) + 10
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H:.1f}" role="img" aria-label="The team\'s pace: a row per member, '
         'a column per hour, a stack of five verdict dots per wake; night hours shaded; wakes started from the editor\'s chat boxed.">']
    for i, h in enumerate(hours):                                    # night shading and the hour labels
        x = LABEL + i * col
        if h.hour >= 22 or h.hour < 6:
            s.append(f'<rect x="{x:.2f}" y="{TOP - 2}" width="{col:.3f}" height="{ROW * len(members) + 2}" fill="{FILL}"/>')
        if h.hour % 6 == 0:
            s.append(f'<line x1="{x:.2f}" y1="{TOP - 2}" x2="{x:.2f}" y2="{TOP + ROW * len(members):.2f}" stroke="{FILL2}" stroke-width=".25"/>')
            s.append(t(x + .4, TOP - 3.2, f'{h.hour:02d}:00', 3.2, 400, MUTED))
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
                for j, step in enumerate(STEPS):
                    s.append(dot(x, y0 + 1.6 + j * 1.2, w.get('steps', {}).get(step, {}).get('verdict', 'missing')))
                if 'scheduled' not in (w.get('kind') or ''):
                    s.append(f'<rect x="{x - .75:.2f}" y="{y0 + .7:.2f}" width="1.5" height="{5 * 1.2 + .4:.2f}" fill="none" stroke="{ACCENT}" stroke-width=".25"/>')
    # the legend
    ly = TOP + ROW * len(members) + 6
    s.append(dot(LABEL + 1, ly - 1.1, 'go') + t(LABEL + 2.6, ly, 'go, done, clean, as-planned', 3.2, 400, MUTED))
    s.append(dot(LABEL + 47, ly - 1.1, 'partial') + t(LABEL + 48.6, ly, 'change, partial, finding', 3.2, 400, MUTED))
    s.append(dot(LABEL + 86, ly - 1.1, 'stop') + t(LABEL + 87.6, ly, 'stop', 3.2, 400, MUTED))
    s.append(f'<rect x="{LABEL + 99:.2f}" y="{ly - 3.2:.2f}" width="1.5" height="3.6" fill="none" stroke="{ACCENT}" stroke-width=".25"/>'
             + t(LABEL + 101.8, ly, 'started from the chat', 3.2, 400, MUTED))
    s.append('</svg>')
    (HERE / 'pace.svg').write_text('\n'.join(s) + '\n')
    stamp = max(w['started'] for w in ws)[:16].replace('T', ' ')
    (HERE / 'pages.html').write_text(
        '<section class="page" data-claims="">\n <figure class="fig span12">\n'
        '  <img src="{{dir}}/pace.svg" alt="The team\'s pace, every closed wake as a stack of five verdict dots" style="width:100%;display:block">\n'
        '  <figcaption><b>Read across for one member, down for one hour: each stack of five dots is one wake, top to bottom plan, pre-review, '
        'work, post-review, post-check. The shaded columns are night; a boxed stack was started from the editor\'s chat, the rest by the schedule.</b>'
        f'<span class="src">This book\'s team, from its own wake records (team/*/wakes/*.json) up to the wake begun {stamp} UTC, drawn as the site\'s '
        'dashboard draws its pace grid (admin/build/build.py). A busy hour shows the wakes that fit its cell. No count is printed; the stats are the researcher\'s.</span></figcaption>\n'
        ' </figure>\n</section>\n')


if __name__ == '__main__':
    main()
