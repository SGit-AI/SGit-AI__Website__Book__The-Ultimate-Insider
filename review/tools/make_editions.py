# RC2 online, with each scene's record under it: the book promises the reader "Online, under each scene, you can open
# the commits, times and files it rests on." The writer marks each scene with a `%% record: ...` line (a Markua comment,
# left out of the PDF); this renders the chapters of an edition as pages and shows each record line under its scene,
# every commit, path and register id in it a link where verified (the same lookup as make_reader.py: this repository,
# a read-only clone of the talk's at 298be4e, claims/register.json). Other `%%` lines are notes for the writers and stay
# hidden. Paragraph anchors as on the review pages. Also writes the zoom index: the editions from shortest to longest.
# Writes only src/pages/review/rc2/, rc2-70/, ed-03/, ed-10/ and src/pages/review/zoom.html. Kept by developer@book.the-ultimate-insider.
# Run: python3 review/tools/make_editions.py <path to a full clone of SGit-AI__Website__Presentation__The-Ultimate-Insider>

import html, json, re, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_review import ROOT, Markdown, anchored                    # noqa: E402
from make_reader import Repo, link, value_html, BOOK, TALK, TALK_AT  # noqa: E402

EDITIONS = [('rc2', 'RC2, the 30-page edition', ROOT / 'manuscript' / 'editions' / 'rc2' / 'Book.txt'),
            ('rc2-70', 'the 70-page edition, being written', ROOT / 'manuscript' / 'editions' / 'rc2-70' / 'Book.txt')]
PAGES = ROOT / 'src' / 'pages' / 'review'
SHORT = [('ed-03', 'the 3-page edition', ROOT / 'manuscript' / 'editions' / '03' / 'Book.txt', ROOT / 'chapter-plan' / 'cast' / 'edition-03.md'),
         ('ed-10', 'the 10-page edition', ROOT / 'manuscript' / 'editions' / '10' / 'Book.txt', ROOT / 'chapter-plan' / 'cast' / 'edition-10.md')]
NO_RECORD = {('ed-03', 'A book about you doing it')}            # pages the script gives no section: named here, so any other miss stops the build
TOKEN = re.compile(r'(?<![\w/.-])(C\d{3}|[0-9a-f]{7,12}|[\w.-]+(?:/[\w.-]+)+/?|[\w-]+\.md)(?![\w/-])')


def record_html(line, book, talk, claims, used):
    text = re.sub(r'^`?%%\s*record:\s*', '', line.strip()).rstrip('`').strip()
    out, last, n = [], 0, 0
    for m in TOKEN.finditer(text):
        tok, rendered = m.group(1), None
        if re.fullmatch(r'C\d{3}', tok) and tok in claims:
            used.setdefault(tok, None)
            rendered = f'<a class="pv pv-claim" href="#claim-{tok}" title="{html.escape(claims[tok]["claim"])}">{tok}</a>'
        elif re.fullmatch(r'[0-9a-f]{7,12}', tok):
            side = 'book' if book.has_commit(tok) else 'talk' if talk.has_commit(tok) else None
            if side:
                repo = book if side == 'book' else talk
                rendered = link(repo.commit_url(tok), f'<code>{tok}</code>', f'commit {tok} in the {side}\'s repository')
        else:
            p = tok.rstrip('/')
            side = 'book' if book.has_path(p) else 'talk' if talk.has_path(p) else None
            if side:
                repo = book if side == 'book' else talk
                rendered = link(repo.path_url(p), f'<code>{html.escape(tok)}</code>', f'{p} in the {side}\'s repository')
        out.append(html.escape(text[last:m.start()]))
        out.append(rendered if rendered else f'<code>{html.escape(tok)}</code>')
        n += 1 if rendered else 0
        last = m.end()
    out.append(html.escape(text[last:]))
    return ''.join(out), n


def norm(t):
    return re.sub(r'[^a-z0-9]+', ' ', t.lower()).strip()


def script_records(script):
    """The storyteller's script: each '## Page N. <title>' section's `%% record:` lines, and the 'Where this came from' ones."""
    pages, where, cur = [], [], None
    for line in script.read_text().splitlines():
        m = re.match(r'## (?:Page \d+\. |At the back\. )?(.*)', line)
        if m:
            cur = [] if not norm(m.group(1)).startswith('where this came from') else where
            if cur is not where:
                pages.append((norm(m.group(1)), cur))
        elif cur is not None and re.match(r'^`?%%\s*record:', line.strip()):
            cur.append(line.strip())
    return pages, where


def web_text(raw, name):
    """The publisher's Markua for the web: fences and marker images out, a figure's alt text kept, and nothing raw let through."""
    out = []
    for line in raw.splitlines():
        if line.startswith(':::'):
            continue
        line = re.sub(r'!\[[^\]]*\]\([^)]*marker[^)]*\)(\{[^}]*\})?\\?', '**On stage:** ', line)
        line = re.sub(r'^!\[([^\]]*)\]\([^)]*\)(\{[^}]*\})?\\?$', lambda m: '**Figure:** ' + m.group(1), line)
        line = re.sub(r'\{[.#][^}]*\}', '', line).rstrip('\\').rstrip()
        if line.lstrip().startswith('<') or '](' in line:
            sys.exit(f'{name}: raw HTML or a link the web page would pass unescaped: {line[:80]!r}')
        out.append(line)
    return '\n'.join(out)


def chapter_page(path, i, files, book, talk, claims, edition_title, foot=None):
    raw = path.read_text()
    if foot is not None:                                            # a short edition: the publisher's text, its page's record at the foot
        raw = web_text(raw, path) + '\n' + '\n'.join(foot)
    title = re.match(r'# (.*)', raw).group(1)
    ch = f'r{i + 1:02d}'
    used, blocks, scene, linked, seen = {}, [], 0, 0, {}                # seen: one per chapter, so a repeated line gets -2, not a twin id
    for part in re.split(r'(^`?%%[^\n]*$)', raw.split('\n', 1)[1], flags=re.M):
        if re.match(r'^`?%%\s*record:', part):
            scene += 1
            inner, k = record_html(part, book, talk, claims, used)
            linked += k
            blocks.append(f'<aside class="rc-rec" id="rec-{ch}-{scene}"><b>Rests on</b> {inner}</aside>')
        elif re.match(r'^`?%%', part):
            continue                                                # notes for the writers: not for readers
        elif part.strip():
            blocks.append(anchored(Markdown().to_html(part), ch, seen, [], path.name))
    claims_list = ''.join(f'<li id="claim-{c}"><b>{c}</b> {html.escape(claims[c]["claim"])}: {value_html(claims[c].get("value", ""))} '
                          f'<span class="pv-state pv-{html.escape(claims[c].get("state", ""))}">{html.escape(claims[c].get("state", ""))}</span></li>'
                          for c in sorted(used))
    prev = f'<a href="{files[i - 1].stem}.html">Previous</a>' if i else ''
    nxt = f'<a href="{files[i + 1].stem}.html">Next</a>' if i + 1 < len(files) else ''
    nav = f'<nav class="pv-nav" aria-label="Chapters"><a href="index.html">All chapters</a><a href="../zoom.html">The zoom</a>{prev}{nxt}</nav>'
    meta = {'title': f'{title} ({edition_title}, online)', 'description': f'{edition_title}: {title}, with the record each scene rests on.'}
    body = (f'<!--meta {json.dumps(meta)} -->\n<link rel="stylesheet" href="{{{{root}}}}review/pen.css">\n'
            f'<div class="rv wrap pv-page" data-no-third-party>\n'
            f'<p class="rv-proto">{html.escape(edition_title[0].upper() + edition_title[1:])}, online: {"at the foot, what this page rests on, from the storyteller" + chr(39) + "s script" if foot is not None else "under each scene, what it rests on"}. Made by <code>review/tools/make_editions.py</code> from the writer\'s chapters.</p>\n'
            f'{nav}\n<article class="rv-ch pv-ch"><h1>{html.escape(title)}</h1>\n' + '\n'.join(blocks) +
            (f'\n<section class="pv-claims"><h2>The numbers in this chapter</h2><p class="note">From the researcher\'s register (<code>claims/register.json</code>).</p><ol>{claims_list}</ol></section>' if used else '') +
            f'\n</article>\n{nav}\n</div>\n')
    return title, scene, linked, body


def main(talk_path):
    for where in (ROOT, Path(talk_path)):
        if subprocess.run(['git', 'rev-parse', '--is-shallow-repository'], cwd=where, capture_output=True, text=True).stdout.strip() == 'true':
            sys.exit(f'{where} is a shallow clone: run git fetch --unshallow there first')
    book, talk = Repo(ROOT, 'HEAD', BOOK, 'dev'), Repo(Path(talk_path), TALK_AT, TALK, TALK_AT)
    claims = {c['id']: c for c in json.loads((ROOT / 'claims' / 'register.json').read_text())['claims']}
    for slug, edition_title, booktxt in EDITIONS:
        OUT = PAGES / slug
        OUT.mkdir(parents=True, exist_ok=True)
        files = [(booktxt.parent / l.strip()).resolve() for l in booktxt.read_text().splitlines() if l.strip() and not l.startswith('#')]
        files = [f for f in files if f.exists()]
        toc, scenes, links = [], 0, 0
        for i, f in enumerate(files):
            title, n, k, body = chapter_page(f, i, files, book, talk, claims, edition_title)
            (OUT / f'{f.stem}.html').write_text(body)
            scenes, links = scenes + n, links + k
            toc.append(f'<li><a href="{f.stem}.html">{html.escape(title)}</a> <span class="c-dim">{n} scenes with their record, {k} links</span></li>')
        src = html.escape(str(files[0].parent.relative_to(ROOT))) if files else ''
        meta = {'title': f'{edition_title[0].upper() + edition_title[1:]} online, with its record', 'description': f'One Human, Nine Agents, Nineteen Hours, {edition_title}, online: under each scene, the commits, times and files it rests on.'}
        (OUT / 'index.html').write_text(
            f'<!--meta {json.dumps(meta)} -->\n<section class="wrap narrow" data-no-third-party>\n<p class="kicker">{html.escape(edition_title)} · a draft</p>\n'
            f'<h1>{html.escape(edition_title[0].upper() + edition_title[1:])}, online, with its record</h1>\n<p class="lead">The book says: "Online, under each scene, you can open the commits, times and files it rests on." Here they are: each scene with what it rests on, every commit, file and number a link where it could be verified.</p>\n'
            f'<p class="note">{len(files)} chapters, {scenes} scenes, {links} links, from the writer\'s chapters (<code>{src}/</code>) as they stand on dev; rebuilt with the site. The draft changes at every release.</p>\n'
            f'<ol>{"".join(toc)}</ol>\n<p><a href="../zoom.html">The zoom</a>: the same story at every length.</p>\n</section>\n')
        print(f'{slug}: {len(files)} chapters, {scenes} scenes, {links} links')
    for slug, edition_title, booktxt, script in SHORT:
        OUT = PAGES / slug
        OUT.mkdir(parents=True, exist_ok=True)
        files = [booktxt.parent / l.strip() for l in booktxt.read_text().splitlines() if l.strip() and not l.startswith('#')]
        pages, where = script_records(script)
        toc, links = [], 0
        for i, f in enumerate(files):
            title = re.match(r'# (.*)', f.read_text()).group(1)
            hit = [r for t, r in pages if t.startswith(norm(title))]
            if not hit and (slug, title) in NO_RECORD:
                hit = [['`%% record: (the storyteller' + chr(39) + 's script gives this page no record line)`']]
            if len(hit) != 1:
                sys.exit(f'{f}: "{title}" matches {len(hit)} pages of {script.name}, not one')
            title, n, k, body = chapter_page(f, i, files, book, talk, claims, edition_title, foot=hit[0])
            (OUT / f'{f.stem}.html').write_text(body)
            links += k
            toc.append(f'<li><a href="{f.stem}.html">{html.escape(title)}</a> <span class="c-dim">{k} links</span></li>')
        used, wh = {}, []
        for line in where:
            inner, k = record_html(line, book, talk, claims, used)
            wh.append(f'<aside class="rc-rec"><b>Rests on</b> {inner}</aside>')
            links += k
        meta = {'title': f'{edition_title[0].upper() + edition_title[1:]} online, with its record', 'description': f'One Human, Nine Agents, Nineteen Hours, {edition_title}, online: each page with the commits, files and numbers it rests on.'}
        rel = lambda p: html.escape(str(p.relative_to(ROOT)))
        (OUT / 'index.html').write_text(
            f'<!--meta {json.dumps(meta)} -->\n<section class="wrap narrow" data-no-third-party>\n<p class="kicker">{html.escape(edition_title)} · online</p>\n'
            f'<h1>{html.escape(edition_title[0].upper() + edition_title[1:])}, online, with its record</h1>\n'
            f'<p class="lead">The printed pages, each with what it rests on at its foot: the record lines the storyteller wrote under each page of its script, every commit, file and number a link where it could be verified.</p>\n'
            f'<p class="note">{len(files)} chapters, {links} links. The text is the publisher\'s (<code>{rel(booktxt.parent)}/</code>), the record the storyteller\'s (<code>{rel(script)}</code>), as they stand on dev.</p>\n'
            f'<ol>{"".join(toc)}</ol>\n<h2>Where the whole edition came from</h2>\n{"".join(wh)}\n<p><a href="../zoom.html">The zoom</a>: the same story at every length.</p>\n</section>\n')
        print(f'{slug}: {len(files)} chapters, {links} links')
    zmeta = {'title': 'The zoom: the book at every length', 'description': 'One Human, Nine Agents, Nineteen Hours from 3 pages to the full first version: start small, zoom in.'}
    (OUT.parent / 'zoom.html').write_text(
        f'<!--meta {json.dumps(zmeta)} -->\n<section class="wrap narrow" data-no-third-party>\n<p class="kicker">The book · ZM1</p>\n<h1>The zoom: the same story at every length</h1>\n'
        f'<p class="lead">Start small and zoom in. Each length is written from the one above it, and the longer ones keep the shorter ones\' lines.</p>\n<ol class="zoom">\n'
        f'<li><b>3 pages</b>: <a href="ed-03/index.html">online, with its record</a> · <a href="{{{{root}}}}manuscript/one-human-nine-agents-edition-03.pdf">the PDF</a></li>\n'
        f'<li><b>10 pages</b>: <a href="ed-10/index.html">online, with its record</a> · <a href="{{{{root}}}}manuscript/one-human-nine-agents-edition-10.pdf">the PDF</a></li>\n'
        f'<li><b>30 pages, RC2</b>: <a href="rc2/index.html">online, with the record under each scene</a> · <a href="{{{{root}}}}rc2.html">its page and PDF</a></li>\n'
        f'<li><b>70 pages, being written</b>: <a href="rc2-70/index.html">the chapters drafted so far, online, with their record</a></li>\n'
        f'<li><b>The full first version, RC1</b>: <a href="read/index.html">online, with every source linked</a></li>\n</ol>\n'
        f'<p class="note">The 70-page edition grows as the writer drafts it. Made by <code>review/tools/make_editions.py</code>.</p>\n</section>\n')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('usage: make_editions.py <path to a clone of the talk\'s repository>')
    main(sys.argv[1])
