# Builds the site into _site/ from src/, content in the repository root, briefs/ and manuscript/. Standard library
# only, so CI needs nothing installed. The same pattern as the talk's site (SGit-AI__Website__Presentation__The-Ultimate-Insider,
# admin/build/build.py at 298be4e), cut to what the book needs on day one.
#
#   python3 admin/build/build.py                 # version from ./version (written only by CI), else "pending"
#   python3 admin/build/build.py --version v0.1.3
#
# What it does, in order: copy src/static verbatim (stamping {{version}}), wrap every src/pages fragment in the
# chrome, render the book's plan, team and open decisions from book.json, the briefs from briefs/, the manuscript
# from manuscript/Book.txt, the sources of truth (REALITY.md, CLAUDE.md, BRIEF-CORRECTIONS.md), the release history
# from git, llms.txt and sitemap.xml, and a .md twin next to every page. Apache-2.0.

import html
import json
import re
import shutil
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT       = Path(__file__).resolve().parents[2]
SRC        = ROOT / 'src'
OUT        = ROOT / '_site'
TEXT_TYPES = {'.html', '.js', '.css', '.json', '.txt', '.md', '.svg', '.xml'}
PENDING    = 'pending'


class Markdown:                                                     # just enough markdown for the pages written here
    INLINE = [(re.compile(r'`([^`]+)`'),                    lambda m: '<code>' + m.group(1) + '</code>'),
              (re.compile(r'\*\*([^*]+)\*\*'),              lambda m: '<strong>' + m.group(1) + '</strong>'),
              (re.compile(r'(?<![*\w])\*([^*\s][^*]*)\*'),  lambda m: '<em>' + m.group(1) + '</em>'),
              (re.compile(r'!\[([^\]]*)\]\(([^)\s]+)\)'),    lambda m: '<img src="' + m.group(2) + '" alt="' + m.group(1) + '" loading="lazy">'),
              (re.compile(r'\[([^\]]+)\]\(([^)\s]+)\)'),     lambda m: '<a href="' + m.group(2) + '">' + m.group(1) + '</a>')]

    def inline(self, text):
        parts = re.split(r'(`[^`]+`)', text)                        # never touch what is inside code spans
        out   = []
        for part in parts:
            if part.startswith('`') and part.endswith('`') and len(part) > 1:
                out.append('<code>' + html.escape(part[1:-1]) + '</code>')
                continue
            part = html.escape(part, quote=False)
            for pattern, repl in self.INLINE[1:]:
                part = pattern.sub(repl, part)
            out.append(part)
        return ''.join(out)

    def to_html(self, text):
        lines, out, i = text.split('\n'), [], 0
        while i < len(lines):
            line = lines[i]
            if not line.strip():
                i += 1
                continue
            if line.startswith('```'):
                block = []
                i += 1
                while i < len(lines) and not lines[i].startswith('```'):
                    block.append(lines[i])
                    i += 1
                out.append('<pre><code>' + html.escape('\n'.join(block)) + '</code></pre>')
                i += 1
                continue
            m = re.match(r'(#{1,4}) (.*)', line)
            if m:
                level  = len(m.group(1))
                anchor = re.sub(r'[^a-z0-9]+', '-', m.group(2).lower()).strip('-')
                out.append(f'<h{level} id="{anchor}">{self.inline(m.group(2))}</h{level}>')
                i += 1
                continue
            if line.startswith('<'):                                # a raw html block, up to the next blank line
                block = []
                while i < len(lines) and lines[i].strip():
                    block.append(lines[i])
                    i += 1
                out.append('\n'.join(block))
                continue
            if line.startswith('> '):
                block = []
                while i < len(lines) and lines[i].startswith('> '):
                    block.append(lines[i][2:])
                    i += 1
                out.append('<blockquote><p>' + self.inline(' '.join(block)) + '</p></blockquote>')
                continue
            if line.startswith('|'):
                rows = []
                while i < len(lines) and lines[i].startswith('|'):
                    cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                    if not all(re.fullmatch(r':?-{3,}:?', c) for c in cells):
                        rows.append(cells)
                    i += 1
                head = ''.join('<th>' + self.inline(c) + '</th>' for c in rows[0])
                body = ''.join('<tr>' + ''.join('<td>' + self.inline(c) + '</td>' for c in r) + '</tr>' for r in rows[1:])
                out.append(f'<div class="tbl"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>')
                continue
            m = re.match(r'(\s*)([-*]|\d+\.) ', line)
            if m:
                tag   = 'ol' if m.group(2)[0].isdigit() else 'ul'
                items = []
                while i < len(lines) and re.match(r'\s*([-*]|\d+\.) ', lines[i]):
                    item = re.sub(r'^\s*([-*]|\d+\.) ', '', lines[i])
                    i += 1
                    while i < len(lines) and lines[i].startswith('  ') and lines[i].strip():
                        item += ' ' + lines[i].strip()
                        i += 1
                    items.append('<li>' + self.inline(item) + '</li>')
                out.append(f'<{tag}>' + ''.join(items) + f'</{tag}>')
                continue
            block = []
            while i < len(lines) and lines[i].strip() and not re.match(r'(#{1,4} |```|> |\||\s*([-*]|\d+\.) |<)', lines[i]):
                block.append(lines[i].strip())
                i += 1
            out.append('<p>' + self.inline(' '.join(block)) + '</p>')
        return '\n'.join(out)


class Html_To_Markdown(HTMLParser):                                 # the .md twin of a page written in html
    SKIP  = {'script', 'style', 'svg', 'nav', 'button', 'template', 'iframe'}
    BLOCK = {'p', 'div', 'section', 'article', 'header', 'footer', 'main', 'ul', 'ol', 'table', 'figure', 'blockquote', 'aside', 'figcaption', 'details', 'summary', 'dl', 'dd', 'dt'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip, self.href, self.row = [], 0, [], None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in self.SKIP or 'data-md-skip' in a:
            self.skip += 1
            return
        if self.skip:
            return
        if tag in ('h1', 'h2', 'h3', 'h4'):
            self.out.append('\n\n' + '#' * int(tag[1]) + ' ')
        elif tag == 'li':
            self.out.append('\n- ')
        elif tag == 'br':
            self.out.append('\n')
        elif tag in ('strong', 'b'):
            self.out.append('**')
        elif tag in ('em', 'i'):
            self.out.append('*')
        elif tag == 'code':
            self.out.append('`')
        elif tag == 'a':
            self.href.append(a.get('href', ''))
            self.out.append('[')
        elif tag == 'tr':
            self.row = []
        elif tag in ('td', 'th') and self.row is not None:
            self.row.append('')
        elif tag in self.BLOCK:
            self.out.append('\n\n')

    def handle_endtag(self, tag):
        if tag in self.SKIP:
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if tag in ('strong', 'b'):
            self.out.append('**')
        elif tag in ('em', 'i'):
            self.out.append('*')
        elif tag == 'code':
            self.out.append('`')
        elif tag == 'a' and self.href:
            href = re.sub(r'\.html(#|$)', r'.md\1', self.href.pop()) if not self.href[-1].startswith('http') else self.href.pop()
            self.out.append(f']({href})')
        elif tag == 'tr' and self.row is not None:
            self.out.append('\n| ' + ' | '.join(c.strip() for c in self.row) + ' |')
            self.row = None
        elif tag in self.BLOCK or tag in ('h1', 'h2', 'h3', 'h4'):
            self.out.append('\n')

    def handle_data(self, data):
        if self.skip:
            return
        text = re.sub(r'\s+', ' ', data)
        if self.row is not None and self.row:
            self.row[-1] += text
        else:
            self.out.append(text)

    def convert(self, fragment):
        self.feed(fragment)
        text = ''.join(self.out)
        text = re.sub(r'\[\s*\]\([^)]*\)', '', text)
        text = re.sub(r'[ \t]+\n', '\n', text)
        text = re.sub(r'\n[ \t]+', '\n', text)
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip() + '\n'




class Site_Build:
    DOCS = [('reality',          'REALITY.md',           'What exists',              'What exists in this repository and on this site, kept current by whoever ships.'),
            ('rules-for-agents', 'CLAUDE.md',            'Rules for agents',         'The rules every agent working in this repository reads first (CLAUDE.md).'),
            ('corrections',      'BRIEF-CORRECTIONS.md', 'Corrections to the brief', 'Where the briefs turned out to be wrong, and what was done instead.')]

    def __init__(self, version):
        self.version = version
        self.config  = json.loads((ROOT / 'site.json').read_text())
        self.book    = json.loads((ROOT / 'book.json').read_text())
        self.pages   = []                                           # (path, title, description) of every page built
        self.titles  = {}                                           # path -> title, for the release history

    def root_of(self, rel):                                         # the relative path back to the site root
        return '../' * (len(Path(rel).parts) - 1)

    def stamp(self, text, rel):
        return text.replace('{{version}}', self.version).replace('{{root}}', self.root_of(rel))

    def chrome(self, rel, title, description, body, kind='page'):
        root  = self.root_of(rel)
        name  = self.config['name']
        hrefs = [href for _, href in self.config['nav']]                # the page's own link, or else its section's
        here  = rel if rel in hrefs else next((h for h in hrefs if '/' in h and rel.startswith(h.rsplit('/', 1)[0] + '/')), None)
        nav   = ''.join(f'<a href="{root}{href}"{(" aria-current=\"page\"" if href == rel else " aria-current=\"true\"") if href == here else ""}>{label}</a>' for label, href in self.config['nav'])
        full  = title if rel == 'index.html' else f'{title} · {self.config["short"]}'
        canon = self.config['url'] + '/' + rel
        md    = Path(rel).with_suffix('.md').name
        ld    = json.dumps({'@context': 'https://schema.org', '@type': 'Article' if kind == 'article' else 'WebPage', 'name': title,
                            'description': description, 'url': canon, 'version': self.version, 'isPartOf': {'@type': 'WebSite', 'name': name, 'url': self.config['url']},
                            'author': {'@type': 'Person', 'name': 'Dinis Cruz'}, 'license': 'https://creativecommons.org/licenses/by/4.0/'}).replace('</', '<\\/')
        return f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full)}</title>
<meta name="description" content="{html.escape(description)}">
<meta name="site-version" content="{self.version}">
<link rel="canonical" href="{canon}">
<link rel="alternate" type="text/markdown" href="{md}">
<meta property="og:type" content="{'article' if kind == 'article' else 'website'}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:url" content="{canon}">
<script type="application/ld+json">{ld}</script>
<link rel="icon" href="{root}assets/favicon.svg">
<link rel="stylesheet" href="{root}assets/site.css">
<script src="{root}assets/theme.js"></script>
</head>
<body class="{kind}">
<a class="skip" href="#main">Skip to the content</a>
<header class="top"><div class="wrap">
<a class="brand" href="{root}index.html"><b>the ultimate insider</b><small>book.sgit.ai</small></a>
<a class="ver" href="{root}releases/index.html#{self.version}" title="Release history: what {self.version} changed">{self.version}</a>
<nav class="main" aria-label="Site">{nav}</nav>
<button class="theme" type="button" aria-label="Switch between light and dark">theme</button>
</div></header>
<main id="main">
{body}
</main>
<footer class="foot"><div class="wrap">
<p><b>{name}</b> · <a href="{root}releases/index.html">site {self.version}</a> · version numbered by CI, never by hand</p>
<p>The book of <a href="https://the-ultimate-insider.presentation.sgit.ai/">The ultimate insider</a> talk · part of the <a href="https://sgit.ai/">sgit.ai</a> network · <a href="{self.config['repo']}">source</a> · <a href="{md}">this page as markdown</a> · <a href="{root}llms.txt">llms.txt</a> · <a href="{root}about/index.html">about</a></p>
<p>Text CC BY 4.0 (proposed, for the editor to sign), code Apache-2.0. © 2026 Dinis Cruz.</p>
</div></footer>
</body>
</html>
'''

    def md_twin(self, rel, title, description, body_md):
        url = self.config['url'] + '/' + rel
        return (f'# {title}\n\n> {description}\n\n*Source: <{url}> · site {self.version} · generated from the same content as the page, '
                f'so the two cannot drift.*\n\n---\n\n{body_md.strip()}\n\n---\n\n*[Site index for agents]({self.root_of(rel)}llms.txt) · [HTML version]({url})*\n')

    def write(self, rel, text):
        path = OUT / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def page(self, rel, title, description, body, kind='page', body_md=None, listed=True):
        body = self.stamp(body, rel)
        self.write(rel, self.chrome(rel, title, description, body, kind))
        if body_md is None:
            body_md = Html_To_Markdown().convert(body)
        self.write(str(Path(rel).with_suffix('.md')), self.md_twin(rel, title, description, body_md))
        self.titles[rel] = title
        if listed:
            self.pages.append((rel, title, description))

    def copy_static(self):
        for path in sorted((SRC / 'static').rglob('*')):
            if path.is_dir():
                continue
            rel    = str(path.relative_to(SRC / 'static'))
            target = OUT / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            if path.suffix in TEXT_TYPES:
                target.write_text(self.stamp(path.read_text(), rel))
            else:
                shutil.copyfile(path, target)

    def read_meta(self, text):
        m = re.match(r'\s*<!--meta\s+(\{.*?\})\s*-->\s*', text, re.S)
        if not m:
            raise SystemExit('a page fragment must start with <!--meta {...} -->')
        return json.loads(m.group(1)), text[m.end():]

    def build_pages(self):
        for path in sorted((SRC / 'pages').rglob('*.html')):
            rel        = str(path.relative_to(SRC / 'pages'))
            meta, body = self.read_meta(path.read_text())
            self.page(rel, meta['title'], meta['description'], body, meta.get('kind', 'page'), listed=meta.get('listed', True))

    def table(self, head, rows):                                    # rows of already-escaped html cells
        th = ''.join(f'<th>{h}</th>' for h in head)
        tr = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
        return f'<div class="tbl"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'

    def tag(self, who):                                             # who decided: the editor, or a proposal waiting on him
        return '<span class="tag ed">editor</span>' if who == 'editor' else '<span class="tag pr">proposal</span>'

    def build_plan(self):                                           # the dates and the rounds, from book.json
        esc, md, b = html.escape, Markdown(), self.book
        marks = ''.join(f'<li class="ms" data-date="{esc(m["date"])}"><p class="kk">{esc(m["when"])}</p><h3>{esc(m["what"])}</h3>'
                        f'<p>{md.inline(m["detail"])}</p><p class="cd" aria-live="polite"></p></li>' for m in b['milestones'])
        rounds = ''.join(f'<li class="round"><p class="kk">{esc(r["id"])} · {esc(r["when"])}</p><h3>{esc(r["title"])}</h3><ul>'
                         + ''.join(f'<li>{md.inline(x)}</li>' for x in r['deliver']) + '</ul></li>' for r in b['rounds'])
        phases = ''.join(f'<li><b>{esc(p["name"])}</b>: {md.inline(p["what"])}</li>' for p in b['phases'])
        body = (f'<section class="wrap narrow"><p class="kicker">The plan · {self.tag("editor")}</p><h1>From the talk to the book in four days</h1>'
                f'<p class="lead">{md.inline(b["plan_lead"])}</p>'
                f'<h2 id="dates">The dates</h2><ul class="milestones">{marks}</ul>'
                f'<h2 id="rounds">The rounds</h2><p class="note">From the conductor\'s brief. Each round closes with its deliverables in the repository and a release of this site.</p>'
                f'<ol class="rounds">{rounds}</ol>'
                f'<h2 id="phases">The book names its own phases</h2><ul>{phases}</ul>'
                f'<p class="note">Source: <a href="../brief/1-book-conductor-brief.html#the-rounds">the conductor\'s brief, the rounds</a>.</p></section>'
                f'<script src="../assets/countdown.js"></script>')
        bmd = ('## The dates\n\n' + '\n'.join(f'- **{m["when"]}**: {m["what"]}. {m["detail"]}' for m in b['milestones'])
               + '\n\n## The rounds\n\n' + '\n\n'.join(f'### {r["id"]} · {r["when"]}: {r["title"]}\n\n' + '\n'.join(f'- {x}' for x in r['deliver']) for r in b['rounds'])
               + '\n\n## The phases\n\n' + '\n'.join(f'- **{p["name"]}**: {p["what"]}' for p in b['phases']))
        self.page('plan/index.html', 'The plan', 'The dates and the rounds: the first edition on Leanpub on Monday 2 November 2026, Amazon and a paperback proof by Web Summit on 9 November.', body, body_md=bmd)

    def build_team(self):                                           # the roles proposed in the brief; nobody is staffed until the editor says so
        esc, md, b = html.escape, Markdown(), self.book
        rows = [[f'<b>{esc(r["role"])}</b>', md.inline(r['owns']), md.inline(r['first']), esc(r['status'])] for r in b['roles']]
        body = (f'<section class="wrap"><p class="kicker">The team · {self.tag("proposal")}</p><h1>Who writes the book</h1>'
                f'<p class="lead">{md.inline(b["team_lead"])}</p>'
                f'{self.table(["Role", "Owns", "First task", "Status"], rows)}'
                f'<h2 id="editor">The editor</h2><p class="measure">{md.inline(b["editor"])}</p>'
                f'<h2 id="blind">The blind repository</h2><p class="measure">{md.inline(b["blind"])}</p>'
                f'<p class="note">Source: <a href="../brief/1-book-conductor-brief.html#the-team">the conductor\'s brief, the team</a>, and <a href="../brief/5-lessons-to-carry.html">the lessons to carry</a>.</p></section>')
        bmd = (b['team_lead'] + '\n\n| Role | Owns | First task | Status |\n|---|---|---|---|\n'
               + '\n'.join(f'| {r["role"]} | {r["owns"]} | {r["first"]} | {r["status"]} |' for r in b['roles'])
               + f'\n\n## The editor\n\n{b["editor"]}\n\n## The blind repository\n\n{b["blind"]}')
        self.page('team/index.html', 'The team', 'The roles proposed for the book repository: conductor, librarian, historian, technologist, security, storyteller, writer, researcher, designer, publisher and synthetic readers.', body, body_md=bmd)

    def build_decisions(self):                                      # the editor decides by signing: signed and open, from book.json
        esc, md, b = html.escape, Markdown(), self.book
        def card(d):
            opts = ''.join(f'<li>{md.inline(o)}</li>' for o in d.get('options', []))
            return (f'<li class="dec s-{esc(d["status"])}" id="{esc(d["id"])}"><p class="kk">{esc(d["id"])} · {esc(d["status"])}</p><h3>{esc(d["ask"])}</h3>'
                    f'<p>{md.inline(d["detail"])}</p>' + (f'<ul>{opts}</ul>' if opts else '') + '</li>')
        opened = [d for d in b['decisions'] if d['status'] == 'open']
        signed = [d for d in b['decisions'] if d['status'] != 'open']
        body = (f'<section class="wrap narrow"><p class="kicker">Decisions</p><h1>What the editor decides</h1>'
                f'<p class="lead">The editor decides by signing. The team proposes options and never acts on an unsigned one. '
                f'{len(opened)} open, {len(signed)} already decided in the brief. The conductor lists the open ones at every wake and asks for them once a day, not every hour.</p>'
                f'<h2 id="open">Open</h2><ul class="decs">{"".join(card(d) for d in opened)}</ul>'
                f'<h2 id="signed">Decided in the brief</h2><ul class="decs">{"".join(card(d) for d in signed)}</ul></section>')
        bmd = '\n\n'.join(f'## {d["id"]} ({d["status"]}): {d["ask"]}\n\n{d["detail"]}' + ''.join(f'\n- {o}' for o in d.get('options', [])) for d in b['decisions'])
        self.page('decisions/index.html', 'Decisions', f'What the editor decides by signing: {len(opened)} open, {len(signed)} decided in the brief.', body, body_md=bmd)

    def build_briefs(self):                                         # every brief, published in full as given, never edited
        md, items = Markdown(), []
        for folder in sorted((ROOT / 'briefs').iterdir(), reverse=True):
            if not folder.is_dir():
                continue
            files = sorted(p for p in folder.glob('*.md') if p.name != 'README.md')
            readme = (folder / 'README.md').read_text() if (folder / 'README.md').exists() else ''
            for p in files:
                text  = p.read_text()
                title = text.split('\n', 1)[0].lstrip('# ').strip()
                body  = text.split('\n', 1)[1]
                rel   = f'brief/{p.stem}.html'
                nav   = '<nav class="crumbs" aria-label="Breadcrumb"><a href="../index.html">Home</a> / <a href="index.html">The brief</a></nav>'
                self.page(rel, title, f'{title}: one of the editor\'s briefs of {folder.name}, published in full as given.',
                          f'<article class="prose wrap narrow">{nav}<p class="kicker">The brief · {folder.name} · <code>briefs/{folder.name}/{p.name}</code></p><h1>{html.escape(title)}</h1>{md.to_html(body)}</article>',
                          body_md=body)
                items.append((rel, title, folder.name))
            intro = md.to_html(readme.split('\n', 1)[1]) if readme else ''
        lis  = ''.join(f'<li class="card"><p class="kicker">{d}</p><h2><a href="{Path(r).name}">{html.escape(t)}</a></h2></li>' for r, t, d in items)
        body = (f'<section class="wrap"><p class="kicker">The brief</p><h1>The briefs</h1>'
                f'<p class="lead">What the editor asked for, published in full as given and never edited. Where a brief turns out to be wrong, the finding goes in '
                f'<a href="../docs/corrections.html">the corrections</a>, and what exists goes in <a href="../docs/reality.html">what exists</a>.</p>'
                f'<div class="prose measure">{intro}</div><ul class="cards">{lis}</ul></section>')
        self.page('brief/index.html', 'The briefs', 'The editor\'s briefs for the book, published in full as given and never edited.', body)

    def build_book(self):                                           # the manuscript, in the order Leanpub reads it (manuscript/Book.txt)
        md, b, esc = Markdown(), self.book, html.escape
        order = [l.strip() for l in (ROOT / 'manuscript' / 'Book.txt').read_text().splitlines() if l.strip() and not l.startswith('#')]
        toc   = []
        for n, name in enumerate(order):
            text  = (ROOT / 'manuscript' / name).read_text()
            title = re.sub(r'^#+\s*', '', text.split('\n', 1)[0]).strip()
            rel   = f'book/{Path(name).stem}.html'
            prev  = f'<a href="{Path(order[n - 1]).stem}.html">previous</a>' if n else ''
            nxt   = f'<a href="{Path(order[n + 1]).stem}.html">next</a>' if n + 1 < len(order) else ''
            nav   = '<nav class="crumbs" aria-label="Breadcrumb"><a href="../index.html">Home</a> / <a href="index.html">The book</a></nav>'
            self.page(rel, title, f'{title}: from the manuscript of the book of The ultimate insider.',
                      f'<article class="prose wrap narrow">{nav}<p class="kicker">The manuscript · <code>manuscript/{esc(name)}</code></p><h1>{esc(title)}</h1>'
                      f'{md.to_html(text.split(chr(10), 1)[1] if chr(10) in text else "")}<p class="pn">{prev} {nxt}</p></article>', kind='article',
                      body_md=text.split('\n', 1)[1] if '\n' in text else '')
            toc.append((rel, title))
        cands = ''.join(f'<li><b>{esc(t["title"])}</b>' + (f': {esc(t["sub"])}' if t.get('sub') else '') + '</li>' for t in b['title']['candidates'])
        lis   = ''.join(f'<li><a href="{Path(r).name}">{esc(t)}</a></li>' for r, t in toc)
        body  = (f'<section class="wrap narrow"><p class="kicker">The book</p><h1>The manuscript</h1>'
                 f'<p class="lead">{md.inline(b["book_lead"])}</p>'
                 f'<p class="status"><b>Status:</b> {md.inline(b["status"])}</p>'
                 f'<h2 id="contents">Contents</h2><ol class="toc">{lis}</ol>'
                 f'<p class="note">The order is <code>manuscript/Book.txt</code>, the file Leanpub reads, so the site and the book cannot disagree on it.</p>'
                 f'<h2 id="title">The title</h2><p>{md.inline(b["title"]["status"])}</p><ul>{cands}</ul>'
                 f'<h2 id="formats">Formats</h2><p>{md.inline(b["formats"])}</p></section>')
        self.page('book/index.html', 'The book', 'The manuscript of the book of The ultimate insider, chapter by chapter, in the order Leanpub builds it.', body)

    def build_docs(self):                                           # the sources of truth, rendered as they are in the repository
        md = Markdown()
        for slug, src, label, description in self.DOCS:
            text = (ROOT / src).read_text()
            body = text.split('\n', 1)[1] if text.startswith('# ') else text
            lit  = lambda s: s.replace('{{', '&#123;&#123;')       # a placeholder the document talks about is shown, not stamped
            self.page(f'docs/{slug}.html', label, description,
                      f'<article class="prose wrap narrow"><p class="kicker">Sources of truth · <code>{src}</code></p><h1>{html.escape(label)}</h1>{lit(md.to_html(body))}</article>', body_md=lit(body))

    def git(self, *args):
        try:
            return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout
        except (OSError, subprocess.CalledProcessError):
            return ''

    def pages_from(self, path):                                     # the pages a changed source file produces
        p = Path(path)
        if path.startswith('src/pages/'):
            return [str(p.relative_to('src/pages'))]
        if path.startswith('briefs/') and p.suffix == '.md':
            return ['brief/index.html'] if p.name == 'README.md' else [f'brief/{p.stem}.html', 'brief/index.html']
        if path.startswith('manuscript/'):
            return ['book/index.html'] + ([f'book/{p.stem}.html'] if p.suffix == '.md' else [])
        if path == 'book.json':
            return ['plan/index.html', 'team/index.html', 'decisions/index.html', 'book/index.html']
        return [f'docs/{slug}.html' for slug, src, _, _ in self.DOCS if src == path]

    def release(self, ref, prev, version):                          # one release, read from git
        rng   = f'{prev}..{ref}' if prev else ref
        work  = []
        for rec in self.git('log', '--format=%h%x1f%an%x1f%s%x1f%b%x1e', rng).split('\x1e'):
            parts = rec.strip('\n').split('\x1f')
            if len(parts) == 4 and parts[1] != 'GitHub Actions':
                body = parts[3].strip().split('\n\n')[0] if parts[3].strip() else ''
                body = '' if re.match(r'(Co-Authored-By|Claude-Session|Agent):', body) else ' '.join(body.split())
                work.append({'commit': parts[0], 'author': parts[1], 'subject': parts[2], 'summary': body})
        files = (self.git('diff', '--name-only', prev, ref) if prev else self.git('ls-tree', '-r', '--name-only', ref)).split()
        files = sorted(f for f in files if f != 'version')
        pages = sorted({pg for f in files for pg in self.pages_from(f)})
        subj  = self.git('log', '-1', '--format=%s', ref).strip()
        title = re.sub(r'^site v\d+\.\d+\.\d+: ', '', subj) if version != PENDING else (work[0]['subject'] if work else 'nothing yet')
        return {'version': version, 'date': self.git('log', '-1', '--format=%cs', ref).strip(), 'commit': self.git('rev-parse', '--short=12', ref).strip(),
                'title': title, 'summary': next((w['summary'] for w in work if w['summary']), ''), 'work': work, 'changes': files, 'pages': pages}

    def build_versions(self):                                       # counted from git, never typed
        tags = [t for t in self.git('tag', '--list', 'v*', '--sort=-v:refname').split() if re.fullmatch(r'v\d+\.\d+\.\d+', t)]
        rels = [self.release(t, tags[i + 1] if i + 1 < len(tags) else None, t) for i, t in enumerate(tags)]
        head = self.git('rev-parse', 'HEAD').strip()
        if head and (not tags or self.git('rev-parse', tags[0] + '^{commit}').strip() != head):
            pend = self.release('HEAD', tags[0] if tags else None, PENDING)
            if pend['work']:
                rels.insert(0, pend)
        for r in rels:
            self.write(f'releases/{r["version"]}.json', json.dumps(r, indent=1) + '\n')
        self.write('releases/index.json', json.dumps({'current': self.version, 'versions': [
            {k: r[k] for k in ('version', 'date', 'commit', 'title')} for r in rels]}, indent=1) + '\n')

        def link(pg):
            return f'<a href="../{pg}">{html.escape(self.titles.get(pg, pg))}</a>'
        sections, mds = [], []
        for r in rels:
            v      = r['version']
            name   = 'Not released yet' if v == PENDING else v
            here   = ' <span class="here">this build</span>' if v == self.version else ''
            work   = ''.join(f'<li><code>{w["commit"]}</code> {html.escape(w["subject"])} <span class="c-dim">({html.escape(w["author"])})</span></li>' for w in r['work'])
            pages  = ' · '.join(link(pg) for pg in r['pages'] if pg in self.titles) or 'no page content (the build, the gate or the pipeline)'
            files  = ''.join(f'<li><code>{html.escape(f)}</code></li>' for f in r['changes'])
            sections.append(f'<section class="rel" id="{v}"><h2>{name}{here}</h2><p class="meta">{r["date"]} · commit <code>{r["commit"]}</code> · '
                            f'<a href="{v}.json">{v}.json</a></p><p class="ttl">{html.escape(r["title"])}</p>'
                            + (f'<p>{html.escape(r["summary"])}</p>' if r['summary'] else '')
                            + f'<p><b>Pages changed ({len(r["pages"])}):</b> {pages}</p>'
                            + f'<details><summary>Commits ({len(r["work"])}) and files ({len(r["changes"])})</summary><ul>{work}</ul><ul class="files">{files}</ul></details></section>')
            mds.append(f'## {name}\n\n{r["date"]} · commit `{r["commit"]}`\n\n{r["title"]}\n\n{r["summary"]}\n')
        count = sum(1 for r in rels if r['version'] != PENDING)
        intro = (f'This build is <b>{self.version}</b>. {count} release{"s" if count != 1 else ""} so far, newest first, each read from git: '
                 f'the release commit CI made, the work commits it carries, the files they changed and the pages those files produce. '
                 f'The same data is in <a href="index.json">index.json</a> and one file per release. The version in the top bar of every page links here, to its own entry.')
        rule  = ('<p>Nobody but CI writes the version. A push to <code>dev</code> bumps the last number and a push to <code>main</code> the middle one; '
                 'the release job tags its own commit and deploys that commit. The scheme is <a href="https://newsroom.sgit.ai/articles/ci-owns-the-version.html">CI owns the version</a>, '
                 'the same as <a href="https://the-ultimate-insider.presentation.sgit.ai/admin/versions.html">the talk\'s site</a>.</p>')
        if not rels:
            sections.append('<p class="note">No release yet: the first push to <code>dev</code> or <code>main</code> makes v0.1.0.</p>')
        body  = f'<section class="wrap narrow"><p class="kicker">Releases</p><h1>Release history</h1><p class="lead">{intro}</p>{rule}{"".join(sections)}</section>'
        self.page('releases/index.html', 'Release history', f'Every release of this site, numbered by CI and read from git. This build is {self.version}.', body,
                  body_md=f'This build is {self.version}. {count} releases.\n\n' + '\n'.join(mds))

    def build_indexes(self):
        cfg   = self.config
        lines = [f'# {cfg["name"]}', '', f'> {cfg["tagline"]}', '', f'Site {self.version}. Every page has a `.md` twin at the same path.', '', '## Pages', '']
        for rel, title, description in self.pages:
            lines.append(f'- [{title}]({Path(rel).with_suffix(".md")}): {description}')
        lines += ['', '## The book, as data', '',
                  '- [book.json](book.json): the dates, the rounds, the roles and the decisions; the plan, team and decisions pages all read it']
        self.write('llms.txt', '\n'.join(lines) + '\n')
        self.write('book.json', json.dumps(self.book, indent=1) + '\n')
        urls = ''.join(f'<url><loc>{cfg["url"]}/{rel}</loc></url>' for rel, _, _ in self.pages)
        self.write('sitemap.xml', f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
        self.write('robots.txt', f'User-agent: *\nAllow: /\nSitemap: {cfg["url"]}/sitemap.xml\n')
        self.write('version.txt', self.version + '\n')

    def build(self):
        if OUT.exists():
            shutil.rmtree(OUT)
        OUT.mkdir()
        self.copy_static()
        self.build_pages()
        self.build_plan()
        self.build_team()
        self.build_decisions()
        self.build_briefs()
        self.build_book()
        self.build_docs()
        self.build_versions()
        self.build_indexes()
        print(f'built {len(self.pages)} pages at site {self.version} into {OUT.relative_to(ROOT)}/')


if __name__ == '__main__':
    args    = sys.argv[1:]
    version = args[args.index('--version') + 1] if '--version' in args else None
    if version is None:                                             # ./version names this build only on CI's own release commit
        vfile   = ROOT / 'version'
        author  = subprocess.run(['git', 'log', '-1', '--format=%an'], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        dirty   = subprocess.run(['git', 'status', '--porcelain', '--untracked-files=no'], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        version = vfile.read_text().strip() if vfile.exists() and author == 'GitHub Actions' and not dirty else PENDING
    Site_Build(version).build()
