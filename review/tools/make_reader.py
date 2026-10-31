# The augmented reading view (A8, the editor's RC1 review, batch 5): every RC1 chapter as a page where what is dead text
# in print is a link online. A commit hash links to its commit, a file path to its file, a register id (C001...) to the
# claim at the chapter's foot (value, state, source, the command that reruns it, from claims/register.json); each
# paragraph says how many sources it carries. Same anchors as the review pages (make_review.py), so a comment and a source
# point at the same words. Only what is verified gets a link: a hash or path is looked up in this repository and in a
# read-only clone of the talk's repository (pass its path); one found in neither, or a path found in both with nothing in
# the paragraph to say which, stays plain text. The page makes no request to another host: links load nothing until clicked.
# Writes only src/pages/review/read/ and review/anchors/rc1-provenance.json (every anchor's sources, as data). Kept by developer@book.the-ultimate-insider.
# Run: python3 review/tools/make_reader.py <path to a clone of SGit-AI__Website__Presentation__The-Ultimate-Insider>

import html, json, re, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_review import ROOT, Markdown, anchored                    # noqa: E402

RC1    = ROOT / 'team' / 'conductor' / 'rc1'
OUT    = ROOT / 'src' / 'pages' / 'review' / 'read'
BOOK   = 'https://github.com/SGit-AI/SGit-AI__Website__Book__The-Ultimate-Insider'
TALK   = 'https://github.com/SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider'
TALK_AT = '298be4e'


class Repo:
    def __init__(self, path, ref, url, blob_ref):
        self.path, self.url, self.blob_ref = path, url, blob_ref
        names = subprocess.run(['git', 'ls-tree', '-r', '--name-only', ref], cwd=path, capture_output=True, text=True).stdout.split()
        self.files = set(names) | {str(Path(n).parent) for n in names} | {str(p) for n in names for p in Path(n).parents}
        self.seen = {}

    def has_commit(self, h):
        if h not in self.seen:
            self.seen[h] = subprocess.run(['git', 'cat-file', '-e', f'{h}^{{commit}}'], cwd=self.path, capture_output=True).returncode == 0
        return self.seen[h]

    def has_path(self, p):
        return p.rstrip('/') in self.files

    def commit_url(self, h):
        return f'{self.url}/commit/{h}'

    def path_url(self, p):
        return f'{self.url}/{"tree" if not Path(p).suffix else "blob"}/{self.blob_ref}/{p.rstrip("/")}'


def link(url, text, title):
    return f'<a class="pv" href="{html.escape(url)}" title="{html.escape(title)}" rel="noopener noreferrer">{text}</a>'


def augment(block, book, talk, claims, used, ch, srcs=None):
    count = 0
    srcs = [] if srcs is None else srcs                             # what this block rests on, for the provenance data
    commits = {}
    for h in re.findall(r'<code>([0-9a-f]{7,12})</code>', block):
        commits[h] = 'book' if book.has_commit(h) else 'talk' if talk.has_commit(h) else None
    sides = {s for s in commits.values() if s}
    words = re.sub(r'<[^>]+>', ' ', block)
    lean = (sides.pop() if len(sides) == 1 else
            'talk' if re.search(r"\btalk('s)?\b", words) and not re.search(r'\bThis repository\b', words) else
            'book' if re.search(r'\bThis repository\b', words) else None)

    def code(m):
        nonlocal count
        inner = m.group(1)
        if inner in commits:
            side = commits[inner]
            if not side:
                return m.group(0)
            count += 1
            srcs.append({'commit': inner, 'repository': side})
            repo = book if side == 'book' else talk
            return link(repo.commit_url(inner), m.group(0), f'commit {inner} in the {"book" if side == "book" else "talk"}\'s repository')
        p = html.unescape(inner).split(' ')[0].rstrip('.,;:)')
        if '/' not in p or p.startswith(('/', '~', 'http')) or re.search(r'[<>*{}]', p):
            return m.group(0)
        in_book, in_talk = book.has_path(p), talk.has_path(p)
        side = ('book' if in_book and not in_talk else 'talk' if in_talk and not in_book else lean if in_book and in_talk else None)
        if not side:
            return m.group(0)
        count += 1
        srcs.append({'path': p, 'repository': side})
        repo = book if side == 'book' else talk
        where = 'this book\'s repository' if side == 'book' else f'the talk\'s repository at {TALK_AT}'
        return link(repo.path_url(p), m.group(0), f'{p} in {where}')

    block = re.sub(r'<code>([^<]+)</code>', code, block)

    def claim(m):
        nonlocal count
        cid = m.group(0)
        if cid not in claims:
            return cid
        count += 1
        srcs.append({'claim': cid})
        used.setdefault(cid, None)
        return f'<a class="pv pv-claim" href="#claims-{ch}-{cid}" title="{html.escape(claims[cid]["claim"])}">{cid}</a>'

    parts = re.split(r'(<[^>]+>)', block)                           # register ids in text only, never inside a tag
    block = ''.join(p if p.startswith('<') else re.sub(r'\bC\d{3}\b', claim, p) for p in parts)
    return block, count


def value_html(v):                                                 # a register value: a number or text in bold, a dict or list as nested lines
    if isinstance(v, dict):
        return '<ul class="pv-val">' + ''.join(f'<li>{html.escape(str(k))}: {value_html(x)}</li>' for k, x in v.items()) + '</ul>'
    if isinstance(v, list):
        return '<ul class="pv-val">' + ''.join(f'<li>{value_html(x)}</li>' for x in v) + '</ul>'
    return f'<b>{html.escape(str(v))}</b>'


def claims_html(used, claims, ch):
    if not used:
        return ''
    rows = []
    for cid in sorted(used):
        c = claims[cid]
        src = c.get('source', {})
        rows.append(f'<li id="claims-{ch}-{cid}"><b>{cid}</b> {html.escape(c["claim"])}: {value_html(c.get("value", ""))} '
                    f'<span class="pv-state pv-{html.escape(c.get("state", ""))}">{html.escape(c.get("state", ""))}</span>'
                    f'<br><span class="c-dim">{html.escape(src.get("repository", ""))} at {html.escape(str(src.get("at", "")))}: {html.escape(str(src.get("evidence", "")))}</span>'
                    + (f'<br><code>{html.escape(c["command"])}</code>' if c.get('command') else '') + '</li>')
    return (f'<section class="pv-claims" aria-label="The claims in this chapter"><h2>The numbers in this chapter</h2>'
            f'<p class="note">From the researcher\'s register (<code>claims/register.json</code>): the only place a number in the book may come from. Each with the command that reruns it.</p>'
            f'<ol>{"".join(rows)}</ol></section>')


def main(talk_path):
    for where in (ROOT, Path(talk_path)):                           # a shallow clone would leave real commits unlinked
        if subprocess.run(['git', 'rev-parse', '--is-shallow-repository'], cwd=where, capture_output=True, text=True).stdout.strip() == 'true':
            sys.exit(f'{where} is a shallow clone: run git fetch --unshallow there first')
    book = Repo(ROOT, 'HEAD', BOOK, 'dev')
    talk = Repo(Path(talk_path), TALK_AT, TALK, TALK_AT)
    claims = {c['id']: c for c in json.loads((ROOT / 'claims' / 'register.json').read_text())['claims']}
    order = [l.strip() for l in (ROOT / 'manuscript' / 'Book.txt').read_text().splitlines() if l.strip() and not l.startswith('#')]
    files = [f for f in order if (RC1 / f).exists()]
    OUT.mkdir(parents=True, exist_ok=True)
    toc, total, provenance = [], 0, {}
    for i, f in enumerate(files):
        text = (RC1 / f).read_text()
        title = re.match(r'# (.*)', text).group(1)
        ch = f.split('-')[0]
        body = re.sub(r'\]\(resources/', '](../../book/resources/', text.split('\n', 1)[1])
        out, used, n_ch = [], {}, 0

        def keep(tag, srcs):                                        # the anchor's sources, as data
            aid = re.search(r'data-a="([^"]+)"', tag)
            if aid and srcs:
                provenance[aid.group(1)] = {'chapter': f, 'sources': srcs}
        for line in anchored(Markdown().to_html(body), ch, {}, [], f).split('\n'):
            m = re.match(r'(<(p|blockquote|li|div)[^>]*data-a="[^"]+"[^>]*>)(.*)$', line)
            if m or line.startswith(('<ul>', '<ol>')):
                if line.startswith(('<ul>', '<ol>')):              # list items one by one
                    def li(mm):
                        nonlocal n_ch
                        srcs = []
                        inner, k = augment(mm.group(2), book, talk, claims, used, ch, srcs)
                        keep(mm.group(1), srcs)
                        n_ch += k
                        return f'<li{mm.group(1)}{f" data-pv={chr(34)}{k}{chr(34)}" if k else ""}>{inner}</li>'
                    line = re.sub(r'<li([^>]*)>(.*?)</li>', li, line)
                else:
                    srcs = []
                    inner, k = augment(m.group(3), book, talk, claims, used, ch, srcs)
                    keep(m.group(1), srcs)
                    n_ch += k
                    line = m.group(1)[:-1] + (f' data-pv="{k}"' if k else '') + '>' + inner
            out.append(line)
        total += n_ch
        prev = f'<a href="{Path(files[i - 1]).stem}.html">Previous</a>' if i else ''
        nxt = f'<a href="{Path(files[i + 1]).stem}.html">Next</a>' if i + 1 < len(files) else ''
        meta = {'title': f'{title} (augmented)', 'description': f'RC1, {title}, with every commit, file and number linked to where it came from.'}
        page = f'''<!--meta {json.dumps(meta)} -->
<link rel="stylesheet" href="{{{{root}}}}review/pen.css">
<div class="rv wrap pv-page" data-no-third-party>
<p class="rv-proto">The augmented view of RC1 (A8), a first slice: commits, files and numbers link to where they came from; a number beside a paragraph counts its sources. Made by <code>review/tools/make_reader.py</code>.</p>
<nav class="pv-nav" aria-label="Chapters"><a href="index.html">All chapters</a>{prev}{nxt}</nav>
<article class="rv-ch pv-ch" data-ch="{ch}"><h1>{html.escape(title)}</h1>
{chr(10).join(out)}
{claims_html(used, claims, ch)}
</article>
<nav class="pv-nav" aria-label="Chapters"><a href="index.html">All chapters</a>{prev}{nxt}</nav>
</div>
'''
        (OUT / f'{Path(f).stem}.html').write_text(page)
        toc.append(f'<li><a href="{Path(f).stem}.html">{html.escape(title)}</a> <span class="c-dim">{n_ch} linked sources, {len(used)} numbers</span></li>')
        print(f'reader: {f}: {n_ch} sources, {len(used)} claims')
    index = f'''<!--meta {json.dumps({"title": "RC1, augmented", "description": "The book's first version online with what print cannot do: every commit, file and number linked to where it came from. A first slice of A8."})} -->
<section class="wrap narrow" data-no-third-party>
<p class="kicker">The reviewer experience · A8, a first slice</p>
<h1>RC1, augmented</h1>
<p class="lead">In print, a commit hash or a file path is dead text. Here each one is a link to the record, each number links to the register entry that checks it, and every paragraph keeps the same anchor as on the review pages.</p>
<p class="note">{total} sources linked across {len(files)} chapters. Only what was found is linked: a hash or path looked up in this repository and in the talk's at <code>{TALK_AT}</code>; anything found in neither stays plain text. Nothing loads from GitHub until you click.</p>
<ol>{"".join(toc)}</ol>
<p><a href="sources.html">What rests on what</a>: every number and commit, with the paragraphs that rest on it.</p>\n<p><a href="graph.html">Whose work each chapter rests on</a>: the commits each chapter cites, by the member who made them.</p>
<p class="note">Made by <code>review/tools/make_reader.py</code> from <code>team/conductor/rc1/</code> and <code>claims/register.json</code>. Not yet: the graph drawn, QR targets, and a page-by-page view like the PDF.</p>
</section>
'''
    (OUT / 'index.html').write_text(index)
    data = {'schema': 'the-ultimate-insider/provenance/v1', 'edition': 'RC1', 'source': 'team/conductor/rc1/',
            'repositories': {'book': BOOK, 'talk': f'{TALK} at {TALK_AT}'},
            'note': 'Every anchored paragraph of RC1 with what it rests on: commits and paths found in the book\'s or the talk\'s repository, and register ids (claims/register.json). Made by review/tools/make_reader.py; anchors as in review/anchors/rc1.json.',
            'anchors': dict(sorted(provenance.items()))}
    (ROOT / 'review' / 'anchors' / 'rc1-provenance.json').write_text(json.dumps(data, indent=1, ensure_ascii=False) + '\n')
    (OUT / 'sources.html').write_text(sources_page(provenance, claims, files))
    (OUT / 'graph.html').write_text(graph_page(provenance, files, talk))
    print(f'reader: {total} sources in {len(files)} chapters')


def member_of(talk, h, roles):                                     # whose commit, by role, from the talk's own record: never an author's name
    out = subprocess.run(['git', 'log', '-1', '--format=%P%x1f%s%x1f%b', h], cwd=talk.path, capture_output=True, text=True).stdout
    parents, subject, body = (out.split('\x1f') + ['', '', ''])[:3]
    m = re.search(r'^Agent: ([\w.-]+)@', body, re.M)
    if m and m.group(1).lower() in roles:
        return m.group(1).lower()
    m = re.match(r'(?:site v[\d.]+: )?@?([A-Za-z][\w.-]*)(?: joins)?:', subject)
    if m and m.group(1).lower() in roles:
        return m.group(1).lower()
    if not parents.strip():
        return 'editor'                                             # the root commit: the editor's, by the register (C001)
    return 'other'


def graph_page(provenance, files, talk):                            # the graph behind the book, first view: whose work on the day each chapter rests on
    roles = {Path(n).name for n in subprocess.run(['git', 'ls-tree', '--name-only', f'{TALK_AT}:team'], cwd=talk.path,
                                                  capture_output=True, text=True).stdout.split()}
    cells, members = {}, {}
    for v in provenance.values():
        for src in v['sources']:
            if src.get('repository') == 'talk' and 'commit' in src:
                who = members.setdefault(src['commit'], member_of(talk, src['commit'], roles))
                cells.setdefault((v['chapter'], who), set()).add(src['commit'])
    totals = {}
    for (f, who), hs in cells.items():
        totals[who] = totals.get(who, 0) + len(hs)
    order = sorted((w for w in totals if w not in ('editor', 'other')), key=lambda w: (-totals[w], w)) + [w for w in ('editor', 'other') if w in totals]
    top = max(len(hs) for hs in cells.values())
    titles = {f: re.match(r'# (.*)', (RC1 / f).read_text()).group(1) for f in files}
    head = ''.join(f'<th scope="col">{html.escape(w)}</th>' for w in order)
    rows = []
    for f in files:
        tds = []
        for w in order:
            n = len(cells.get((f, w), ()))
            step = 0 if not n else 1 + round(4 * (n - 1) / max(top - 1, 1))      # five steps of one hue, by count
            tip = f'{titles[f]}: {n} of {w}\'s commits cited' if n else f'{titles[f]}: none of {w}\'s'
            tds.append(f'<td class="gx gx{step}" title="{html.escape(tip)}">{n or ""}</td>')
        rows.append(f'<tr><th scope="row"><a href="{Path(f).stem}.html">{html.escape(titles[f])}</a></th>{"".join(tds)}</tr>')
    foot = ''.join(f'<td>{totals[w]}</td>' for w in order)
    meta = {'title': 'RC1, whose work it rests on', 'description': 'Which members of the talk team, and the editor, each chapter of RC1 rests on: the commits it cites, counted by who made them.'}
    return f'''<!--meta {json.dumps(meta)} -->
<link rel="stylesheet" href="{{{{root}}}}review/pen.css">
<section class="wrap pv-page" data-no-third-party>
<nav class="pv-nav" aria-label="Chapters"><a href="index.html">All chapters</a><a href="sources.html">What rests on what</a></nav>
<p class="kicker">RC1, augmented · A8</p>
<h1>Whose work each chapter rests on</h1>
<p class="lead">Each cell counts the commits of the day that a chapter cites, by the member of the talk team who made them. Darker means more. It shows where the book leans on one member's record, and where a member's work is told only second hand.</p>
<div class="gx-wrap"><table class="gx-table">
<caption>Commits from the talk's repository cited per chapter, by member ({len(members)} different commits; the last row adds the chapters up, so a commit cited in two chapters counts twice)</caption>
<thead><tr><th scope="col">Chapter</th>{head}</tr></thead>
<tbody>{"".join(rows)}</tbody>
<tfoot><tr><th scope="row">All chapters</th>{foot}</tr></tfoot>
</table></div>
<p class="note">Who made a commit is read from the talk's own record at <code>{TALK_AT}</code>: the <code>@member:</code> at the start of its subject, or its <code>Agent:</code> trailer. The first commit is the editor's (register C001); "other" is release merges and commits that name no member. Commits from this book's own repository are not counted here. Made by <code>review/tools/make_reader.py</code> from <code>review/anchors/rc1-provenance.json</code>.</p>
</section>
'''


def sources_page(provenance, claims, files):                        # the provenance turned round: each source, and the paragraphs resting on it
    titles = {f: re.match(r'# (.*)', (RC1 / f).read_text()).group(1) for f in files}
    by_claim, by_commit = {}, {}
    for aid, v in provenance.items():
        for src in v['sources']:
            if 'claim' in src:
                by_claim.setdefault(src['claim'], []).append((v['chapter'], aid))
            elif 'commit' in src:
                by_commit.setdefault((src['repository'], src['commit']), []).append((v['chapter'], aid))

    def places(refs):                                               # one label per chapter, then a number for each further paragraph
        groups = {}
        for f, aid in sorted(set(refs), key=lambda r: (files.index(r[0]), r[1])):
            groups.setdefault(f, []).append(aid)
        out = []
        for f, aids in groups.items():
            t = titles[f]
            label = f"ch. {t.split('.')[0]}" if t[:1].isdigit() else t.split('.')[0] if t.startswith('Appendix') else t
            more = ''.join(f' <a class="pv-more" href="{Path(f).stem}.html#{x}" title="paragraph {i} of those here">\u00b6{i}</a>' for i, x in enumerate(aids[1:], 2))
            out.append(f'<span class="pv-at"><a href="{Path(f).stem}.html#{aids[0]}" title="{html.escape(t)}">{html.escape(label)}</a>{more}</span>')
        return ' · '.join(out)

    rows = ''.join(f'<li id="{cid}"><b>{cid}</b> {html.escape(claims[cid]["claim"])} '
                   f'<span class="pv-state pv-{html.escape(claims[cid].get("state", ""))}">{html.escape(claims[cid].get("state", ""))}</span>'
                   f'<br><span class="c-dim">in</span> {places(refs)}</li>' for cid, refs in sorted(by_claim.items()))
    commits = []
    for side, name, repo_url in (('talk', f"the talk's repository at {TALK_AT}", TALK), ('book', "this book's repository", BOOK)):
        items = sorted((h, refs) for (s_, h), refs in by_commit.items() if s_ == side)
        commits.append(f'<h2>Commits in {name} ({len(items)})</h2><ul class="pv-src">'
                       + ''.join(f'<li>{link(f"{repo_url}/commit/{h}", f"<code>{h}</code>", f"commit {h}")} {places(refs)}</li>' for h, refs in items) + '</ul>')
    meta = {'title': 'RC1, what rests on what', 'description': 'Every number and every commit RC1 cites, with each paragraph that rests on it: the provenance of the book turned round.'}
    return f'''<!--meta {json.dumps(meta)} -->
<link rel="stylesheet" href="{{{{root}}}}review/pen.css">
<section class="wrap narrow pv-page" data-no-third-party>
<nav class="pv-nav" aria-label="Chapters"><a href="index.html">All chapters</a></nav>
<p class="kicker">RC1, augmented · A8</p>
<h1>What rests on what</h1>
<p class="lead">The same sources as the chapter pages, turned round: for each number in the register and each commit, the paragraphs of RC1 that rest on it. Change a number or doubt a commit, and this is the list of what to reread.</p>
<p class="note">From <code>review/anchors/rc1-provenance.json</code>, made by <code>review/tools/make_reader.py</code>. A link names the chapter; it lands on the paragraph.</p>
<h2>Numbers ({len(by_claim)})</h2>
<ol class="pv-src">{rows}</ol>
{''.join(commits)}
</section>
'''


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('usage: make_reader.py <path to a clone of the talk\'s repository>')
    main(sys.argv[1])
