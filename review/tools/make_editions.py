# RC2 online, with each scene's record under it: the book promises the reader "Online, under each scene, you can open
# the commits, times and files it rests on." The writer marks each scene with a `%% record: ...` line (a Markua comment,
# left out of the PDF); this renders the chapters of an edition as pages and shows each record line under its scene,
# every commit, path and register id in it a link where verified (the same lookup as make_reader.py: this repository,
# a read-only clone of the talk's at 298be4e, claims/register.json). Other `%%` lines are notes for the writers and stay
# hidden. Paragraph anchors as on the review pages. Also writes the zoom index: the editions from shortest to longest.
# Writes only each edition's pages.html (rc2, rc2-70, rc2-150, ed-03, ed-10), review/anchors/qr-targets.json, editions.json (and its copy in src/static/review/), src/pages/review/rc2/, rc2-70/, rc2-150/, ed-03/, ed-10/ and src/pages/review/zoom.html. Kept by developer@book.the-ultimate-insider.
# Run: python3 review/tools/make_editions.py <path to a full clone of SGit-AI__Website__Presentation__The-Ultimate-Insider>

import atexit, html, json, re, shutil, subprocess, sys, tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_review import ROOT, Markdown, anchored, plain                   # noqa: E402
from make_reader import Repo, link, value_html, BOOK, TALK, TALK_AT  # noqa: E402
from print_pages import chapters_hash, book_files, OUT as PRINT     # noqa: E402

EDITIONS = [('rc2', 'RC2, the 30-page edition', ROOT / 'manuscript' / 'editions' / 'rc2' / 'Book.txt'),
            ('rc2-70', 'the 70-page edition, being written', ROOT / 'manuscript' / 'editions' / 'rc2-70' / 'Book.txt'),
            ('rc2-150', 'the full book, being written', ROOT / 'manuscript' / 'editions' / 'rc2-150' / 'Book.txt')]
PAGES = ROOT / 'src' / 'pages' / 'review'
SITE = json.loads((ROOT / 'site.json').read_text())['url'].rstrip('/')   # the book's own domain: the only host a printed code may point at
QR = ROOT / 'review' / 'anchors' / 'qr-targets.json'
DATA = [ROOT / 'review' / 'anchors' / 'editions.json', ROOT / 'src' / 'static' / 'review' / 'editions.json']   # the editions as data; the second is published
SHORT = [('ed-03', 'the 3-page edition', ROOT / 'manuscript' / 'editions' / '03' / 'Book.txt', ROOT / 'chapter-plan' / 'cast' / 'edition-03.md'),
         ('ed-10', 'the 10-page edition', ROOT / 'manuscript' / 'editions' / '10' / 'Book.txt', ROOT / 'chapter-plan' / 'cast' / 'edition-10.md')]
NO_RECORD = {('ed-03', 'A book about you doing it')}            # pages the script gives no section: named here, so any other miss stops the build
ADDR = re.compile(r'https?://[^\s"<>\'`()\\]+')                  # an address, as the guards read it on both sides
HOSTS = re.compile(r'https://(github\.com/SGit-AI/|the-ultimate-insider\.book\.sgit\.ai/)')


def addresses(text):
    return {a.rstrip('.,;:!?') for a in ADDR.findall(text)}


TOKEN = re.compile(r'(?<![\w/.-])(C\d{3}|[0-9a-f]{7,12}|[\w.-]+(?:/[\w.-]+)+/?|[\w-]+\.md)(?![\w/-])')


def record_html(line, book, talk, claims, used, toks=None):
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
        if toks is not None:
            kind = 'claim' if re.fullmatch(r'C\d{3}', tok) else 'commit' if re.fullmatch(r'[0-9a-f]{7,12}', tok) else 'path'
            href = re.search(r'href="([^"]+)"', rendered).group(1) if rendered and kind != 'claim' else None
            toks.append({'token': tok, 'kind': kind, 'verified': bool(rendered),
                         **({'repository': 'book' if BOOK in href else 'talk', 'url': html.unescape(href)} if href else {}),
                         **({'claim': claims[tok]['claim'], 'value': claims[tok].get('value'), 'state': claims[tok].get('state')} if kind == 'claim' and rendered else {})})
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


def qr(slug, f, rid, words):
    return {'id': f'{slug}/{f.stem}#{rid}', 'edition': slug, 'chapter': f.name, 'url': f'{SITE}/review/{slug}/{f.stem}.html#{rid}', 'starts': words}


def printed_view(ed, name, pp):  # run print_pages.py after make_editions.py has written editions.json, then this again
    """The long editions by printed page (print_pages.py): each page its paragraphs, and the record of each scene ending on it."""
    pages, last, left_out = {}, 1, 0                                              # a paragraph the map does not know takes the page before, across scenes
    for c in ed['chapters']:
        for sc in c['scenes']:
            for p in sc['paragraphs']:
                if p.get('in_print') is False:                      # a section the print leaves out: not shown on a printed page
                    left_out += 1
                    continue
                last = pp['pages'].get(p['id'], last)
                pages.setdefault(last, {'chapters': [], 'paras': [], 'recs': []})
                if c['title'] not in pages[last]['chapters']:
                    pages[last]['chapters'].append(c['title'])
                pages[last]['paras'].append(p['text'])
            if sc['record'] and sc['paragraphs']:
                pages[last]['recs'].append(sc)
    secs = []
    for n in sorted(pages):
        pg = pages[n]
        body = ''.join(f'<p>{html.escape(t)}</p>' for t in pg['paras'])
        recs = ''.join(record_aside(sc) for sc in pg['recs'])
        secs.append(f'<section class="pg" id="p-{n}" data-pg aria-label="Printed page {n}"><h2>{html.escape(" · ".join(pg["chapters"]))} · printed page {n}</h2>{body}{recs}</section>')
    what = (f'Each page here is a printed page of the PDF ({pp["pdf_pages"]} pages, built here as the release builds it; on 4 November this build was a page longer than the published file, so near the end a page number may sit one off). {pp["found"]} paragraphs were found on their page; '
            f'{pp["carried"]} (figures, clock lines, rules) take the page of the one before. Pages with only a cover or a picture are not shown.')
    if left_out:
        heads = ' and '.join(f'"{h}"' for h in ed.get('left_out_of_print', []))
        what += f' {left_out} paragraphs in sections the print leaves out ({heads}) are not shown here: they are on the edition\'s chapter pages online.'
    write_pages(ed, name, secs, what)
    print(f'{ed["edition"]}/pages.html: {len(secs)} printed pages')


def record_aside(sc):
    opens = ' · '.join(f'<a class="pv" href="{html.escape(t["url"])}" rel="noopener noreferrer"><code>{html.escape(t["token"])}</code></a>'
                       for t in sc['tokens'] if t.get('url'))
    return f'<aside class="rc-rec"><b>Rests on</b> {html.escape(sc["record"])}' + (f'<br>Open: {opens}' if opens else '') + '</aside>'


def write_pages(ed, name, secs, what):
    bar = ('<div class="pg-bar"><button type="button" data-pg-prev>Previous</button> <span data-pg-at></span> '
           '<button type="button" data-pg-next>Next</button> <span class="c-dim">or the arrow keys</span></div>')
    meta = {'title': f'{name}, page by page', 'description': f'One Human, Nine Agents, Nineteen Hours, {ed["title"]}, one page at a time, with what each rests on.'}
    (PAGES / ed['edition'] / 'pages.html').write_text(
        f'<!--meta {json.dumps(meta)} -->\n<link rel="stylesheet" href="{{{{root}}}}review/pen.css">\n<section class="wrap narrow" data-no-third-party>\n'
        f'<p class="kicker">{html.escape(ed["title"])} · page by page</p>\n<h1>{html.escape(name)}, page by page</h1>\n'
        f'<p class="lead">The draft one page at a time, as on a tablet, with what each page rests on beneath it.</p>\n'
        f'<p class="note">{what} {len(secs)} pages, from <a href="{{{{root}}}}review/editions.json">editions.json</a>; the same chapters with their links are in <a href="index.html">the edition online</a>.</p>\n'
        f'{bar}\n' + '\n'.join(secs) + f'\n{bar}\n</section>\n<script src="{{{{root}}}}review/pages.js" defer></script>\n')


def pages_view(ed):
    """An edition one page at a time, as a reader turns them: the same filtered text as editions.json, the record under each.
    In the 3- and 10-page editions a chapter is one printed page (publishing/edition.py); in the longer ones a page here is a scene."""
    printed = ed['edition'].startswith('ed-')
    name = ed['title'][0].upper() + ed['title'][1:]
    pp = (json.loads(PRINT.read_text())['editions'].get(ed['edition']) if PRINT.exists() else None) if not printed else None
    if pp and pp['chapters_hash'] != chapters_hash(book_files(ed['edition'])):
        pp = None                                                    # the chapters changed since the PDF was read: scenes, until print_pages.py runs again
    if pp and any(p['id'] not in pp['pages'] for c in ed['chapters'] for sc in c['scenes'] for p in sc['paragraphs']):
        print(f'{ed["edition"]}: the page map lacks some of today\'s paragraphs (print_pages.py ran before editions.json was rebuilt); by scene until it is rerun', file=sys.stderr)
        pp = None
    if pp:
        return printed_view(ed, name, pp)
    secs, n = [], 0
    for c in ed['chapters']:
        for sc in c['scenes']:
            n += 1
            body = ''.join(f'<p>{html.escape(p["text"])}</p>' for p in sc['paragraphs'])
            rec = ''
            if sc['record']:
                opens = ' · '.join(f'<a class="pv" href="{html.escape(t["url"])}" rel="noopener noreferrer"><code>{html.escape(t["token"])}</code></a>'
                                   for t in sc['tokens'] if t.get('url'))
                rec = (f'<aside class="rc-rec"><b>Rests on</b> {html.escape(sc["record"])}'
                       + (f'<br>Open: {opens}' if opens else '') + '</aside>')
            secs.append(f'<section class="pg" id="p-{n}" data-pg aria-label="Page {n}"><h2>{html.escape(c["title"])} · page {n}</h2>{body}{rec}</section>')
    bar = ('<div class="pg-bar"><button type="button" data-pg-prev>Previous</button> <span data-pg-at></span> '
           '<button type="button" data-pg-next>Next</button> <span class="c-dim">or the arrow keys</span></div>')
    meta = {'title': f'{name}, page by page', 'description': f'One Human, Nine Agents, Nineteen Hours, {ed["title"]}, one page at a time, with what each rests on.'}
    what = ('Each page here is a printed page of this edition.' if printed else
            'A "page" here is a scene: the printed page breaks are not yet read from the PDF, so a printed page and a page here may differ.')
    (PAGES / ed['edition'] / 'pages.html').write_text(
        f'<!--meta {json.dumps(meta)} -->\n<link rel="stylesheet" href="{{{{root}}}}review/pen.css">\n<section class="wrap narrow" data-no-third-party>\n'
        f'<p class="kicker">{html.escape(ed["title"])} · page by page</p>\n<h1>{html.escape(name)}, page by page</h1>\n'
        f'<p class="lead">The draft one page at a time, as on a tablet, with what each page rests on beneath it.</p>\n'
        f'<p class="note">{what} {n} pages, from <a href="{{{{root}}}}review/editions.json">editions.json</a>; the same chapters with their links are in <a href="index.html">the edition online</a>.</p>\n'
        f'{bar}\n' + '\n'.join(secs) + f'\n{bar}\n</section>\n<script src="{{{{root}}}}review/pages.js" defer></script>\n')
    print(f'{ed["edition"]}/pages.html: {n} pages')


def drop_headings(booktxt):
    """The headings the build leaves out of the print: the "#! drop-section:" lines of the edition's list (publishing/build_book.py)."""
    return [m.group(1) for l in booktxt.read_text().splitlines() for m in [re.match(r'\s*#!\s*drop-section:\s*(.+?)\s*$', l)] if m]


def drop_sections(text, headings):
    """As publishing/build_book.py does: each named "## " section goes, from its heading to the next "# " or "## " heading, or the end."""
    for h in headings:
        text = re.sub(r"(?ms)^## " + re.escape(h) + r"[ \t]*\n.*?(?=^#{1,2} |\Z)", "", text)
    return text


def printed_ids(raw, drop, ch, name):
    """The anchors of the paragraphs that print: the chapter with the build's rule applied, run through the same anchoring.
    -> (set of ids, how many paragraphs that is)"""
    text, ids, seen, n = drop_sections(raw, drop), set(), {}, 0
    for part in re.split(r'(^`?%%[^\n]*$)', text.split('\n', 1)[1], flags=re.M):
        if re.match(r'^`?%%', part) or not part.strip():
            continue
        done = anchored(Markdown().to_html(re.sub(r'\s*`%%[^`]*`', '', part)), ch, seen, [], name)
        found = re.findall(r' id="([^"]+)" data-a="[^"]+" tabindex="0">', done)
        ids, n = ids | set(found), n + len(found)
    return ids, n


SCRIPTS_OK = ('{{root}}review/pages.js', '{{root}}review/pen.js')   # the only scripts a review page may load (the site's own, by the page templates in make_review.py)
URL_ATTRS = ('href', 'src', 'srcset', 'action', 'formaction', 'poster', 'data', 'cite', 'background', 'ping', 'xlink:href', 'longdesc', 'manifest')


def url_ok(v):
    """An allow-list for a url on a review page (security's findings on 8cc02c05 and on the parser commit): relative, a fragment, the
    book's own site, or the SGit-AI repositories on GitHub; nothing else. The value is read as a browser reads it: entities resolved,
    leading and trailing control characters and spaces trimmed, tabs and line breaks removed wherever they sit, a backslash taken as a
    slash. Any other scheme (javascript:, data:, mailto:, http:), a scheme-relative '//host' or the same in other letters is refused."""
    v = html.unescape(html.unescape(v))                              # twice: a value escaped twice is refused if either reading is an address
    v = re.sub(r'[\t\n\r]', '', v.strip(''.join(chr(c) for c in range(0x21))))
    v = v.replace('\\', '/')
    low = v.lower()
    if not v:
        return True
    if low.startswith('//'):
        return False
    if re.match(r'^[a-z][a-z0-9+.-]*:', low):
        return low.startswith(SITE.lower() + '/') or bool(re.match(r'https://(github\.com/sgit-ai/|the-ultimate-insider\.book\.sgit\.ai/)', low))
    return True                                                     # a fragment, a root-relative or a relative path


from html.parser import HTMLParser

RAW_ADDR = re.compile(r'(?i)(?:[a-z][a-z0-9+.-]*:)?[/\\]{2}[^\s"\'<>`]+')   # an address in any letters, with or without a scheme, as the tag's own text carries it


class _Tags(HTMLParser):
    """Every start tag of a page: its parsed attributes (double-quoted, single-quoted or unquoted, entities resolved) and its raw text."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags, self.css, self._in_style = [], [], False

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, attrs, self.get_starttag_text() or ''))
        self._in_style = tag == 'style'

    def handle_endtag(self, tag):
        self._in_style = False

    def handle_data(self, data):
        if self._in_style:
            self.css.append(data)

    handle_startendtag = handle_starttag


def page_attribute_problem(page):
    """The first thing on the page that breaks the rule, or None if the page is clean. Tags are read with a parser, so quoting does not
    matter (security__007): a url attribute the allow-list refuses; any attribute value, or the tag's own raw text, carrying an address
    off the two hosts (a '//host', or one in other letters, included); a css url() the allow-list refuses, or css with @import, image-set or
    escapes; a script other than the site's own two (SCRIPTS_OK), an inline script, or an on* attribute; a tag the parser cannot read."""
    t = _Tags()
    try:
        t.feed(page)
        t.close()
    except Exception as e:                                           # a page the parser cannot read is refused, not guessed at
        return f'unreadable markup: {e}'
    for tag, attrs, raw in t.tags:
        if tag.lower() in ('iframe', 'frame', 'base', 'object', 'embed'):   # post-review: nothing on a review page frames, embeds or re-bases a page
            return f'<{tag}>: not allowed on a review page'
        if tag.lower() == 'script':                                  # security__008: only the site's own two scripts, by their source; no inline script
            src = next((v for n, v in attrs if n.lower() == 'src'), None)
            if src not in SCRIPTS_OK:
                return f'<script> that is not one of the site\'s own: {(src or "inline")[:80]}'
        for name, v in attrs:
            n = name.lower()
            v = v or ''
            if n == 'srcdoc':
                return f'<{tag} srcdoc=...>: not allowed'
            if n.startswith('on'):                                   # an event handler, in any letters
                return f'<{tag} {name}=...>: an event handler'
            urls = [x.split()[0] for x in v.split(',') if x.strip()] if n == 'srcset' else [v]
            if n in URL_ATTRS and not all(url_ok(x) for x in urls):
                return f'<{tag} {name}="{v[:80]}">'
            for a_ in addresses(v):
                if not (a_ == SITE or HOSTS.match(a_)):
                    return f'<{tag} {name}="{v[:80]}">'
        for m in RAW_ADDR.findall(raw):                              # the raw text of the tag, whatever the quoting
            if not url_ok(m.rstrip('.,;:!?)')):
                return f'<{tag}> carries {m[:80]}'
    styles = ["".join(t.css)] + [v or '' for _, attrs, _ in t.tags for n, v in attrs if n.lower() == 'style']
    for css in styles:                                               # css the pages may carry is plain: no @import, image-set(), or escapes that hide a url
        if re.search(r'@import|image-set|image\(|\\', css, re.I):
            return f'css: {css[:80]}'
    for v in re.findall(r'url\(([^)]*)\)', page, re.I):
        if not url_ok(v.strip('\'" ')):
            return f'url({v[:80]})'
    return None


CLAIM_HEAD = re.compile(r'^#{1,6}\s+(C\d{3})\b')


def text_address_gate(raw, claims, path):
    """Security's answer (security__060 and 006): an address off the two hosts may be printed in the online view as escaped text only
    when it stands under its own claim, that is, in a section whose heading names the claim id (Appendix A's '## C101: ...') and the
    address is in that claim's own register entry. An address anywhere else, or under a claim whose entry does not list it, stops the
    build (fail closed). Lines of writers' notes ('%%') are not printed and not read here. -> [{'address', 'claim'}] for this chapter."""
    found, claim, in_code = [], None, False
    for n, line in enumerate(raw.split('\n'), 1):
        if line.lstrip().startswith(('```', '~~~')) and not re.match(r'^`?%%', line):
            in_code = not in_code                                   # a '#' line inside a fenced block is a comment, not a heading
        m = CLAIM_HEAD.match(line) if not in_code else None
        if m:
            claim = m.group(1)
        elif not in_code and re.match(r'^#{1,6}\s', line):
            claim = None                                            # any other heading ends the claim's section
        if re.match(r'^`?%%', line):
            continue
        for a in sorted(addresses(line)):
            if a == SITE or HOSTS.match(a):
                continue
            if claim is None or claim not in claims or a not in addresses(json.dumps(claims[claim], ensure_ascii=False)):
                sys.exit(f'{path.name}:{n}: an address off the two hosts that is not under a claim whose register entry lists it: {a}')
            if {'address': a, 'claim': claim} not in found:
                found.append({'address': a, 'claim': claim})
    return found


def chapter_page(path, i, files, book, talk, claims, edition_title, foot=None, drop=()):
    raw = path.read_text()
    if foot is not None:                                            # a short edition: the publisher's text, its page's record at the foot
        raw = web_text(raw, path) + '\n' + '\n'.join(foot)
    title = re.match(r'# (.*)', raw).group(1)
    ch = f'r{i + 1:02d}'
    text_addresses = text_address_gate(raw, claims, path)          # security's answer to developer__047: a register address may print as text under its own claim, nothing else off the two hosts
    used, blocks, scene, linked, seen, recs, first = {}, [], 0, 0, {}, [], ''
    kept, kept_n = printed_ids(raw, drop, ch, path.name) if drop else (None, 0)             # which paragraphs print (build_book.py's drop-section rule)
    after_heading = False                                           # set by a heading, taken by the next block (a figure under a heading is introduced by it)
    scenes, paras = [], []                                          # the chapter as data: the same filtered text as the page, never a writers' note                # seen: one per chapter, so a repeated line gets -2, not a twin id
    for part in re.split(r'(^`?%%[^\n]*$)', raw.split('\n', 1)[1], flags=re.M):
        if re.match(r'^`?%%\s*record:', part):
            scene += 1
            toks = []
            inner, k = record_html(part, book, talk, claims, used, toks)
            scenes.append({'record_id': f'rec-{ch}-{scene}', 'paragraphs': paras, 'record': re.sub(r'^`?%%\s*record:\s*', '', part.strip()).rstrip('`').strip(), 'tokens': toks})
            paras = []
            linked += k
            blocks.append(f'<aside class="rc-rec" id="rec-{ch}-{scene}"><b>Rests on</b> {inner}</aside>')
            recs.append((f'rec-{ch}-{scene}', first[:80] or (recs[-1][1] if recs else '')))   # two records in a row: the scene's words are the one before
            first = ''
        elif re.match(r'^`?%%', part):
            continue                                                # notes for the writers: not for readers
        elif part.strip():
            part = re.sub(r'\s*`%%[^`]*`', '', part)                   # a writers' note inside a paragraph: also not for readers
            done = anchored(Markdown().to_html(part), ch, seen, [], path.name)
            blocks.append(done)
            for m in re.finditer(r'<(?:p|li|blockquote|div)[^>]* id="([^"]+)" data-a="[^"]+" tabindex="0">(.*?)</(?:p|li|blockquote|div)>|<h[1-6] id="[^"]*">(.*?)</h[1-6]>', done):
                if m.group(1) is None:                                  # a heading: the next block opens a section
                    after_heading = plain(m.group(3)) if m.group(3) else True
                    continue
                a, t = m.group(1), m.group(2)
                paras.append({'id': a, 'text': plain(t), **({'after_heading': True, 'heading': after_heading} if after_heading else {}),
                              **({'in_print': False} if kept is not None and a not in kept else {})})
                after_heading = False
            first = first or ' '.join(plain(done).split()[:14])
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
    if kept is not None:                                              # a duplicate whose first copy is in a dropped section would be numbered differently: say so
        every = [p for sc in scenes for p in sc['paragraphs']] + paras
        if sum(1 for p in every if p.get('in_print') is False) != len(every) - kept_n:
            print(f'warning: {path.name}: the paragraphs that print do not add up ({len(every) - kept_n} expected left out, {sum(1 for p in every if p.get("in_print") is False)} marked)', file=sys.stderr)
    if paras:
        scenes.append({'record_id': None, 'paragraphs': paras, 'record': None, 'tokens': []})
    return title, scene, linked, body, recs, {'file': str(path.relative_to(ROOT)), 'title': title, 'page': f'{ch}', **({'text_addresses': text_addresses} if text_addresses else {}), 'scenes': scenes}


def main(talk_path):
    for where in (ROOT, Path(talk_path)):
        if subprocess.run(['git', 'rev-parse', '--is-shallow-repository'], cwd=where, capture_output=True, text=True).stdout.strip() == 'true':
            sys.exit(f'{where} is a shallow clone: run git fetch --unshallow there first')
    book, talk = Repo(ROOT, 'HEAD', BOOK, 'dev'), Repo(Path(talk_path), TALK_AT, TALK, TALK_AT)
    claims = {c['id']: c for c in json.loads((ROOT / 'claims' / 'register.json').read_text())['claims']}
    targets, editions = [], []
    global PAGES
    REAL_PAGES, PAGES = PAGES, Path(tempfile.mkdtemp())
    atexit.register(shutil.rmtree, PAGES, True)                     # a refusal leaves nothing behind, in the repository or in /tmp             # the pages are built aside and put in place only after every guard below has passed: a refusal leaves no page behind
    for slug, edition_title, booktxt in EDITIONS:
        OUT = PAGES / slug
        OUT.mkdir(parents=True, exist_ok=True)
        files = [(booktxt.parent / l.strip()).resolve() for l in booktxt.read_text().splitlines() if l.strip() and not l.startswith('#')]
        files = [f for f in files if f.exists()]
        chapters, dropped = [], drop_headings(booktxt)
        editions.append({'edition': slug, 'title': edition_title, 'online': f'{SITE}/review/{slug}/index.html', **({'left_out_of_print': dropped} if dropped else {}), 'chapters': chapters})
        toc, scenes, links = [], 0, 0
        for i, f in enumerate(files):
            title, n, k, body, recs, data = chapter_page(f, i, files, book, talk, claims, edition_title, drop=dropped)
            chapters.append(data)
            targets += [qr(slug, f, rid, words) for rid, words in recs]
            (OUT / f'{f.stem}.html').write_text(body)
            scenes, links = scenes + n, links + k
            toc.append(f'<li><a href="{f.stem}.html">{html.escape(title)}</a> <span class="c-dim">{n} scenes with their record, {k} links</span></li>')
        src = html.escape(str(files[0].parent.relative_to(ROOT))) if files else ''
        meta = {'title': f'{edition_title[0].upper() + edition_title[1:]} online, with its record', 'description': f'One Human, Nine Agents, Nineteen Hours, {edition_title}, online: under each scene, the commits, times and files it rests on.'}
        (OUT / 'index.html').write_text(
            f'<!--meta {json.dumps(meta)} -->\n<section class="wrap narrow" data-no-third-party>\n<p class="kicker">{html.escape(edition_title)} · a draft</p>\n'
            f'<h1>{html.escape(edition_title[0].upper() + edition_title[1:])}, online, with its record</h1>\n<p class="lead">The book says: "Online, under each scene, you can open the commits, times and files it rests on." Here they are: each scene with what it rests on, every commit, file and number a link where it could be verified.</p>\n'
            f'<p class="note">{len(files)} chapters, {scenes} scenes, {links} links, from the writer\'s chapters (<code>{src}/</code>) as they stand on dev; rebuilt with the site. The draft changes at every release.</p>\n'
            f'<ol>{"".join(toc)}</ol>\n<p class="note">As data: <a href="{{{{root}}}}review/editions.json">editions.json</a>, every edition\'s chapters, paragraphs and record.' + ' <a href="pages.html">Page by page</a>: one scene at a time.</p>\n<p><a href="../zoom.html">The zoom</a>: the same story at every length.</p>\n</section>\n')
        print(f'{slug}: {len(files)} chapters, {scenes} scenes, {links} links')
    for slug, edition_title, booktxt, script in SHORT:
        OUT = PAGES / slug
        OUT.mkdir(parents=True, exist_ok=True)
        files = [booktxt.parent / l.strip() for l in booktxt.read_text().splitlines() if l.strip() and not l.startswith('#')]
        pages, where = script_records(script)
        chapters = []
        editions.append({'edition': slug, 'title': edition_title, 'online': f'{SITE}/review/{slug}/index.html', 'record_from': str(script.relative_to(ROOT)), 'chapters': chapters})
        toc, links = [], 0
        for i, f in enumerate(files):
            title = re.match(r'# (.*)', f.read_text()).group(1)
            hit = [r for t, r in pages if t.startswith(norm(title))]
            if not hit and (slug, title) in NO_RECORD:
                hit = [['`%% record: (the storyteller' + chr(39) + 's script gives this page no record line)`']]
            if len(hit) != 1:
                sys.exit(f'{f}: "{title}" matches {len(hit)} pages of {script.name}, not one')
            title, n, k, body, recs, data = chapter_page(f, i, files, book, talk, claims, edition_title, foot=hit[0])
            chapters.append(data)
            targets += [qr(slug, f, rid, words) for rid, words in recs]
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
            f'<ol>{"".join(toc)}</ol>\n<p class="note">As data: <a href="{{{{root}}}}review/editions.json">editions.json</a>, every edition\'s chapters, paragraphs and record. <a href="pages.html">Page by page</a>: one printed page at a time.</p>\n<h2>Where the whole edition came from</h2>\n{"".join(wh)}\n<p><a href="../zoom.html">The zoom</a>: the same story at every length.</p>\n</section>\n')
        print(f'{slug}: {len(files)} chapters, {links} links')
    for t in targets:                                                # printed codes: https, the book's own host, no query, no tracking
        if not re.fullmatch(r'https://the-ultimate-insider\.book\.sgit\.ai/review/[\w-]+/[\w-]+\.html#rec-r\d\d-\d+', t['url']):
            sys.exit(f'qr target refused: {t["url"]}')
    for e in editions:
        pages_view(e)
    for t in targets:
        for a in addresses(json.dumps(t, ensure_ascii=False)):     # no exception for print: every address in a target on the book's domain
            if not a.startswith(SITE + '/'):
                sys.exit(f'qr target carries an outside address: {a}')
    outside = []                                                     # addresses the register itself cites, under the claim that cites them: kept as text, never a link
    for e in editions:
        for c in e['chapters']:
            for sc in c['scenes']:
                for t in sc['tokens']:
                    if t['kind'] != 'claim' or not t['verified']:
                        continue
                    own = addresses(json.dumps(claims[t['token']], ensure_ascii=False))
                    for a in sorted(addresses(json.dumps({k: t.get(k) for k in ('claim', 'value')}, ensure_ascii=False))):
                        if HOSTS.match(a):
                            continue
                        if a not in own:
                            sys.exit(f'editions.json: {a} under {t["token"]} is not in the register entry for it')
                        if {'address': a, 'claim': t['token']} not in outside:
                            outside.append({'address': a, 'claim': t['token']})
    for e in editions:                                               # the gate in chapter_page has passed for these: listed with their claim, as text, never a link
        for c in e['chapters']:
            for x in c.get('text_addresses', []):
                if x not in outside:
                    outside.append(x)
    blob = json.dumps({'about': 'The online editions as data: each chapter, its scenes, their paragraphs (with the review pages\' anchors) and the record each rests on, '
                                'every token resolved to its repository and address, or marked unverified. Writers\' notes are left out, as on the pages. '
                                'outside_citations: addresses on other hosts that the researcher\'s register cites as sources, under the claim that cites them; text, not links. '
                                'Written by review/tools/make_editions.py from manuscript/ as it stands on dev. RC1, the first version, is in rc1-book.json beside this file.', 'site': SITE,
                       'outside_citations': outside, 'editions': editions}, indent=1, ensure_ascii=False) + '\n'
    if '%%' in blob:
        sys.exit('editions.json would carry a %% line: refused')
    for u in re.findall(r'"url": "([^"]+)"', blob):
        if not HOSTS.match(u):
            sys.exit(f'editions.json: a url off the two public hosts: {u}')
    allowed = {o['address'] for o in outside}
    bare = json.loads(blob)                                          # the data with the claims' own register text taken out, and the list itself:
    bare.pop('outside_citations')                                    # outside it, every address must be on the two hosts (a citation passes only under its claim, checked above)
    for e in bare['editions']:
        for c in e['chapters']:
            ok = [x['address'] for x in c.pop('text_addresses', [])]  # passed the gate in chapter_page, under their claim: out of the scan, in this chapter's paragraphs only
            for sc in c['scenes']:
                for p_ in sc['paragraphs']:
                    if ok:                                           # whole addresses only, never a piece of a longer one
                        p_['text'] = ADDR.sub(lambda m_: '[address]' if m_.group(0).rstrip('.,;:!?') in ok else m_.group(0), p_['text'])
                for t in sc['tokens']:
                    if t['kind'] == 'claim':
                        t.pop('claim', None), t.pop('value', None)
    for a in addresses(json.dumps(bare, ensure_ascii=False)):
        if not (a == SITE or HOSTS.match(a)):
            sys.exit(f'editions.json: an address off the two hosts outside its claim\'s register text: {a}')
    for f in sorted(list(PAGES.glob('*/*.html')) + list(REAL_PAGES.glob('*.html'))):   # and never a link on the pages: the persona pages too (security__009), not only the editions'
        page = f.read_text()
        for h in re.findall(r'href="([^"]+)"', page):
            if html.unescape(h).rstrip('.,;:!?') in allowed:
                sys.exit(f'{f}: links an outside citation: {h}')
        bad = page_attribute_problem(page)                           # security: every attribute and css url(), as an allow-list, not a pattern
        if bad:
            sys.exit(f'{f}: an attribute or url() the review pages may not carry: {bad}')
    if '--dry' in sys.argv:                                          # every guard passed; nothing is put in place (for a diff to be reviewed before a release)
        out = next((sys.argv[k + 1] for k, a_ in enumerate(sys.argv) if a_ == '--data-out' and k + 1 < len(sys.argv)), None)
        if out:                                                      # the data, for a check that needs today's chapters (print_check.py --chapters); to a file the caller names, never into the repository's places
            Path(out).write_text(blob)
        print('dry run: every guard passed; nothing put in place' + (f'; the data written to {out}' if out else '')); shutil.rmtree(PAGES); return
    QR.write_text(json.dumps({'about': 'One target per scene (RC2, the 70-page draft) or page (the 3- and 10-page editions): the public URL of the record under it, '
                                       'for a QR code in print. Written by review/tools/make_editions.py; an id holds while the chapter keeps its place and scenes.',
                              'site': SITE, 'targets': targets}, indent=1, ensure_ascii=False) + '\n')
    print(f'qr targets: {len(targets)} -> {QR.relative_to(ROOT)}')
    shutil.copytree(PAGES, REAL_PAGES, dirs_exist_ok=True)           # every guard has passed
    shutil.rmtree(PAGES)
    PAGES, OUT = REAL_PAGES, REAL_PAGES / OUT.name
    print(f'outside citations: ' + (', '.join(f"{o['address']} ({o['claim']})" for o in outside) or 'none'))
    for d in DATA:
        d.write_text(blob)
    print(f'editions.json: {len(editions)} editions, {sum(len(e["chapters"]) for e in editions)} chapters, {len(blob) // 1024} KB')
    built = {Path(b).parent.name for _, _, b in EDITIONS} | {Path(b).parent.name for _, _, b, _ in SHORT}
    unbuilt = sorted(d.name for d in (ROOT / 'manuscript' / 'editions').iterdir() if d.is_dir() and (d / 'Book.txt').exists() and d.name not in built)
    for u in unbuilt:                                                # a new edition is seen at the next run, not when someone happens to notice
        print(f'warning: manuscript/editions/{u}/ is an edition this tool does not build', file=sys.stderr)
    unbuilt_note = (f' Not yet online: {", ".join(f"<code>manuscript/editions/{html.escape(u)}/</code>" for u in unbuilt)}, a newer edition this page does not build yet.' if unbuilt else '')
    zmeta = {'title': 'The zoom: the book at every length', 'description': 'One Human, Nine Agents, Nineteen Hours from 3 pages to the full first version: start small, zoom in.'}
    zoom_old = (OUT.parent / 'zoom.html').read_text() if (OUT.parent / 'zoom.html').exists() else None
    (OUT.parent / 'zoom.html').write_text(
        f'<!--meta {json.dumps(zmeta)} -->\n<section class="wrap narrow" data-no-third-party>\n<p class="kicker">The book · ZM1</p>\n<h1>The zoom: the same story at every length</h1>\n'
        f'<p class="lead">Start small and zoom in. Each length is written from the one above it, and the longer ones keep the shorter ones\' lines.</p>\n<ol class="zoom">\n'
        f'<li><b>3 pages</b>: <a href="ed-03/index.html">online, with its record</a> · <a href="ed-03/pages.html">page by page</a> · <a href="{{{{root}}}}manuscript/one-human-nine-agents-edition-03.pdf">the PDF</a></li>\n'
        f'<li><b>10 pages</b>: <a href="ed-10/index.html">online, with its record</a> · <a href="ed-10/pages.html">page by page</a> · <a href="{{{{root}}}}manuscript/one-human-nine-agents-edition-10.pdf">the PDF</a></li>\n'
        f'<li><b>30 pages, RC2</b>: <a href="rc2/index.html">online, with the record under each scene</a> · <a href="rc2/pages.html">page by page</a> · <a href="{{{{root}}}}rc2.html">its page and PDF</a></li>\n'
        f'<li><b>70 pages, being written</b>: <a href="rc2-70/index.html">the chapters drafted so far, online, with their record</a> · <a href="rc2-70/pages.html">page by page</a></li>\n'
        f'<li><b>The full book, being written</b>: <a href="rc2-150/index.html">online, with the record under each scene</a> · <a href="rc2-150/pages.html">page by page</a></li>\n'
        f'<li><b>The full first version, RC1</b>: <a href="read/index.html">online, with every source linked</a> · <a href="{{{{root}}}}review/rc1-book.json">as data</a></li>\n</ol>\n'
        f'<p class="note">The 70-page edition and the full book grow as the writer drafts them.{unbuilt_note} Made by <code>review/tools/make_editions.py</code>.</p>\n</section>\n')
    bad = page_attribute_problem((OUT.parent / 'zoom.html').read_text())   # the zoom page is written last, so it is read last (post-review): a refusal puts the old page back
    if bad:
        if zoom_old is not None:
            (OUT.parent / 'zoom.html').write_text(zoom_old)
        sys.exit(f'zoom.html: an attribute or url() the review pages may not carry: {bad}')


if __name__ == '__main__':
    argv = sys.argv[1:]                                              # --dry: run every guard, write nothing into place; --dry --data-out FILE also writes the editions data to FILE
    if '--data-out' in argv and '--dry' not in argv:
        sys.exit('--data-out is for a dry run only (--dry --data-out FILE): refused')
    args = [a for k, a in enumerate(argv) if a != '--dry' and a != '--data-out' and not (k and argv[k - 1] == '--data-out')]
    if len(args) != 1:
        sys.exit('usage: make_editions.py <path to a clone of the talk\'s repository> [--dry [--data-out FILE]]')
    main(args[0])
