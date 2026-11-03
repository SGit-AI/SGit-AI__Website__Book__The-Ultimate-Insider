# The wakes behind each chapter of RC1 (A8, "the graph's next views"): for every commit of the talk's repository a chapter
# cites (review/anchors/rc1-provenance.json), the wake of the talk team's member that made it: the member read from the
# commit's "@member:" subject (or its Agent: trailer, as the graph reads it), the wake the one whose started-to-closed window holds the commit's time. Only the member,
# the time, the five step verdicts and a link to the wake file are shown; no comment text is copied. What cannot be traced
# is counted, not guessed. Writes only src/pages/review/read/wakes.html. Kept by developer@book.the-ultimate-insider.
# Run: python3 review/tools/make_wakes.py <path to a full clone of SGit-AI__Website__Presentation__The-Ultimate-Insider>
import collections, html, json, re, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_review import ROOT                                        # noqa: E402
from make_reader import TALK, TALK_AT                               # noqa: E402

STEPS = ['plan', 'pre_review', 'work', 'post_review', 'post_check']
OUT = ROOT / 'src' / 'pages' / 'review' / 'read' / 'wakes.html'


def main(talk):
    git = lambda *a: subprocess.run(['git', '-C', str(talk), *a], capture_output=True, text=True, check=True).stdout
    if git('rev-parse', '--is-shallow-repository').strip() == 'true':
        sys.exit(f'{talk} is a shallow clone: run git fetch --unshallow there first')
    prov = json.loads((ROOT / 'review' / 'anchors' / 'rc1-provenance.json').read_text())['anchors']
    by_ch = collections.defaultdict(set)
    for a in prov.values():
        for s in a['sources']:
            if s.get('repository') == 'talk' and 'commit' in s:
                by_ch[a['chapter']].add(s['commit'])
    wakes = collections.defaultdict(list)                           # member -> [(started, closed, file, verdicts)]
    for f in git('ls-tree', '-r', '--name-only', TALK_AT, 'team').split():
        if re.fullmatch(r'team/[\w-]+/wakes/\d{8}T\d{6}Z\.json', f):
            w = json.loads(git('show', f'{TALK_AT}:{f}'))
            v = {k: str((w.get('steps', {}).get(k) or {}).get('verdict') or '') for k in STEPS}
            wakes[f.split('/')[1]].append((w.get('started') or '', w.get('closed') or '', f, v))
    commit_wake, untraced = {}, collections.Counter()
    for c in sorted({c for cs in by_ch.values() for c in cs}):
        subj, when, body = git('show', '-s', '--format=%s%x00%cI%x00%b', c).split('\x00', 2)
        when = re.sub(r'\+00:00$', 'Z', when.strip())
        m = re.match(r'@([\w-]+):', subj) or re.search(r'^Agent: ([\w-]+)@', body, re.M)   # as the graph reads it: the subject, else the trailer
        if not m:
            untraced['with no "@member:" subject or Agent: trailer'] += 1
            continue
        hits = [w for w in wakes.get(m.group(1), []) if w[0] and w[0] <= when <= (w[1] or '9')]
        if not hits:
            untraced['outside any wake of its member'] += 1
            continue
        commit_wake[c] = (m.group(1), hits[-1])
    files = sorted(by_ch, key=lambda n: [int(x) if x.isdigit() else x for x in re.split(r'(\d+)', n)])
    secs, total = [], 0
    for ch in files:
        per = collections.defaultdict(list)
        for c in sorted(by_ch[ch]):
            if c in commit_wake:
                per[commit_wake[c][1][2]].append((c, commit_wake[c]))
        rows = []
        for f, items in sorted(per.items(), key=lambda kv: kv[1][0][1][1][0]):
            member, (started, _, _, v) = items[0][1]
            verdicts = ' · '.join(f'<span class="pv-state">{html.escape(v[k] or "none")}</span>' for k in STEPS)
            commits = ' '.join(f'<a class="pv" href="{TALK}/commit/{c}" rel="noopener noreferrer"><code>{c}</code></a>' for c, _ in items)
            rows.append(f'<li><b>{html.escape(member)}</b> <span class="pv-at">{html.escape(started[:16].replace("T", " "))} UTC</span> '
                        f'<a class="pv" href="{TALK}/blob/{TALK_AT}/{f}" rel="noopener noreferrer">the wake record</a> {verdicts}<br><span class="c-dim">cites</span> {commits}</li>')
        total += len(rows)
        n_t = sum(1 for c in by_ch[ch] if c in commit_wake)
        secs.append(f'<section><h2><a href="{html.escape(Path(ch).stem)}.html">{html.escape(ch)}</a></h2>'
                    f'<p class="note">{len(by_ch[ch])} talk commits cited; {n_t} traced to {len(rows)} wakes.</p><ul class="pv-src">{"".join(rows)}</ul></section>')
    n_all, n_tr = len({c for cs in by_ch.values() for c in cs}), len(commit_wake)
    gaps = '; '.join(f'{n} {why}' for why, n in untraced.items())
    meta = {'title': 'The wakes behind each chapter', 'description': 'For each chapter of RC1, the talk team\'s wakes that made the commits it cites: member, time, the five step verdicts.'}
    OUT.write_text(f'<!--meta {json.dumps(meta)} -->\n<link rel="stylesheet" href="{{{{root}}}}review/pen.css">\n<section class="wrap narrow" data-no-third-party>\n'
                   f'<p class="kicker">RC1, augmented · A8</p>\n<h1>The wakes behind each chapter</h1>\n'
                   f'<p class="lead">Every commit of the talk a chapter cites was made in some member\'s hourly wake. Here are those wakes, chapter by chapter: who, when, and how each of its five steps ended (plan, pre-review, work, post-review, post-check).</p>\n'
                   f'<p class="note">How: a commit\'s member is read from its "@member:" subject or its Agent: trailer, as on the graph, and its wake is that member\'s wake record whose start-to-close window holds the commit\'s time, in the talk\'s repository at <code>{TALK_AT}</code>. '
                   f'{n_tr} of the {n_all} cited commits are traced this way; not traced: {html.escape(gaps) or "none"}. Only member, time, verdicts and links are shown. The decisions behind a page come in a later view. '
                   f'Made by <code>review/tools/make_wakes.py</code>.</p>\n<p><a href="index.html">RC1 online</a> · <a href="graph.html">whose work each chapter rests on</a></p>\n'
                   + '\n'.join(secs) + '\n</section>\n')
    print(f'wakes.html: {n_tr} of {n_all} cited commits traced, {total} chapter-wake rows; untraced: {gaps}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('usage: make_wakes.py <path to a clone of the talk\'s repository>')
    main(Path(sys.argv[1]))
