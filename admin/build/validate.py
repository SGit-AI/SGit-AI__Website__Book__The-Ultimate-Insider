# The gate. Fails the build (exit 1) on any finding; CI runs it before every release and on the built tree.
# The talk's gate (admin/build/validate.py at 298be4e), without the checks for its team, wakes and slides.
#
#   python3 admin/build/validate.py            # checks the sources and _site/ (build first)
#
# Checks, each one listed on /about/: links resolve, every page is reachable, has its .md twin and is in llms.txt,
# carries structured data and the version, no placeholder survives the build, no script or stylesheet loads from
# another host, every script parses, book.json and the manuscript hold together, no em-dashes in prose, and the
# leak tripwire over every tracked file. Apache-2.0.

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT  = ROOT / '_site'


class Gate:
    LEAKS = [('private key',       re.compile(r'-----BEGIN [A-Z ]*PRIVATE KEY-----')),
             ('AWS access key',    re.compile(r'\bAKIA[0-9A-Z]{16}\b')),
             ('GitHub token',      re.compile(r'\b(ghp|gho|ghs|ghu)_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}')),
             ('Anthropic key',     re.compile(r'\bsk-ant-[A-Za-z0-9_-]{20,}')),
             ('OpenAI-style key',  re.compile(r'\bsk-[A-Za-z0-9]{40,}')),
             ('OpenRouter key',    re.compile(r'\bsk-or-v1-[0-9a-f]{32,}')),
             ('Slack token',       re.compile(r'\bxox[abpr]-[A-Za-z0-9-]{20,}')),
             ('sgit vault key',    re.compile(r'\b[a-z0-9]{24}:[a-z0-9]{8}\b'))]

    def __init__(self):
        self.findings = []

    def fail(self, check, where, what):
        self.findings.append(f'[{check}] {where}: {what}')

    def html_files(self):
        return sorted(p for p in OUT.rglob('*.html'))

    def target(self, page, url):
        return ((OUT if url.startswith('/') else page.parent) / url.split('#')[0].split('?')[0].lstrip('/')).resolve()

    def check_links(self):
        attr = re.compile(r'(?:href|src)="([^"]+)"')
        for page in self.html_files():
            for url in attr.findall(page.read_text()):
                if re.match(r'(https?:|mailto:|data:|javascript:|#|\{)', url):
                    continue
                if url.split('#')[0].split('?')[0] and not self.target(page, url).exists():
                    self.fail('links', page.relative_to(OUT), f'{url} does not resolve')

    def check_reachable(self):                                      # a page nobody links to fails
        linked = set()
        for page in self.html_files():
            for url in re.findall(r'href="([^"#?]+)', page.read_text()):
                if not re.match(r'(https?:|mailto:|data:|javascript:)', url) and self.target(page, url) != page.resolve():
                    linked.add(self.target(page, url))
        for page in self.html_files():
            if page.resolve() not in linked and page.relative_to(OUT) != Path('index.html'):
                self.fail('reachable', page.relative_to(OUT), 'no other page links to it')

    def check_twins_and_index(self):
        llms = (OUT / 'llms.txt').read_text() if (OUT / 'llms.txt').exists() else ''
        if not llms:
            self.fail('llms.txt', 'llms.txt', 'missing')
        for page in self.html_files():
            rel = str(page.relative_to(OUT))
            if not page.with_suffix('.md').exists():
                self.fail('twins', rel, 'has no .md twin')
            if f'({Path(rel).with_suffix(".md")})' not in llms:
                self.fail('llms.txt', rel, 'is not listed in llms.txt')

    def check_chrome(self):                                         # structured data, and the version in the top bar
        version = (OUT / 'version.txt').read_text().strip() if (OUT / 'version.txt').exists() else None
        for page in self.html_files():
            text = page.read_text()
            rel  = page.relative_to(OUT)
            if '<script type="application/ld+json">' not in text:
                self.fail('structured data', rel, 'no JSON-LD')
            m = re.search(r'<a class="ver" href="[^"]*#([^"]+)"[^>]*>([^<]+)</a>', text)
            if not m:
                self.fail('version', rel, 'no version in the top bar')
            elif m.group(2) != version:
                self.fail('version', rel, f'top bar says {m.group(2)}, the build is {version}')

    def check_stamps(self):
        for path in OUT.rglob('*'):
            if path.is_file() and path.suffix in ('.html', '.md', '.js', '.css', '.json', '.txt'):
                text = path.read_text()
                for token in ('{{version}}', '{{root}}'):
                    if token in text:
                        self.fail('stamp', path.relative_to(OUT), f'{token} survived the build')

    def check_no_remote_code(self):
        remote = re.compile(r'<(?:script[^>]*\ssrc|link(?=[^>]*rel="(?:stylesheet|preload|modulepreload)")[^>]*\shref)="(https?:)?//')
        for page in self.html_files():
            if remote.search(page.read_text()):
                self.fail('self-contained', page.relative_to(OUT), 'loads a script or stylesheet from another host')

    def check_scripts_parse(self):
        node = shutil.which('node')
        if not node:
            print('note: node not found, script parse check skipped')
            return
        block = re.compile(r'<script(?![^>]*\bsrc=)(?![^>]*type="application/(?:ld\+)?json")[^>]*>(.*?)</script>', re.S)
        with tempfile.TemporaryDirectory() as tmp:
            jobs = [(p, p.read_text()) for p in OUT.rglob('*.js')]
            for page in self.html_files():
                for n, code in enumerate(block.findall(page.read_text())):
                    jobs.append((Path(f'{page}#script{n}'), code))
            for n, (where, code) in enumerate(jobs):
                f = Path(tmp) / f's{n}.js'
                f.write_text(code)
                r = subprocess.run([node, '--check', str(f)], capture_output=True, text=True)
                if r.returncode:
                    self.fail('scripts', str(where).replace(str(OUT) + '/', ''), r.stderr.strip().splitlines()[-1] if r.stderr.strip() else 'does not parse')

    def check_book(self):                                           # book.json has what the pages need; the manuscript list and its files agree
        book = json.loads((ROOT / 'book.json').read_text())
        for key in ('status', 'book_lead', 'formats', 'title', 'plan_lead', 'milestones', 'rounds', 'phases', 'team_lead', 'editor', 'blind', 'roles', 'decisions'):
            if key not in book:
                self.fail('book', 'book.json', f'has no {key}')
        ids = [d.get('id') for d in book.get('decisions', [])]
        for d in book.get('decisions', []):
            if d.get('status') not in ('open', 'decided'):
                self.fail('book', f'book.json decision {d.get("id")}', 'status is neither open nor decided')
        if len(ids) != len(set(ids)):
            self.fail('book', 'book.json', 'duplicate decision id')
        for m in book.get('milestones', []):
            if not re.fullmatch(r'\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ', m.get('date', '')):
                self.fail('book', f'book.json milestone {m.get("what")}', 'date is not an ISO UTC time')
        listed = [l.strip() for l in (ROOT / 'manuscript' / 'Book.txt').read_text().splitlines() if l.strip() and not l.startswith('#')]
        for name in listed:
            if not (ROOT / 'manuscript' / name).exists():
                self.fail('manuscript', 'manuscript/Book.txt', f'lists {name}, which does not exist')
        for path in (ROOT / 'manuscript').glob('*.md'):
            if path.name not in listed:
                self.fail('manuscript', f'manuscript/{path.name}', 'is not listed in manuscript/Book.txt')

    def tracked_files(self):
        r = subprocess.run(['git', 'ls-files', '-co', '--exclude-standard'], cwd=ROOT, capture_output=True, text=True)
        return [ROOT / f for f in r.stdout.splitlines() if (ROOT / f).is_file()]

    def check_prose(self):
        for path in self.tracked_files():
            if path.suffix not in ('.md', '.html', '.json', '.js', '.css', '.py', '.txt') or 'LICENSE' in path.name:
                continue
            for n, line in enumerate(path.read_text(errors='ignore').splitlines(), 1):
                if '\u2014' in line:
                    self.fail('prose', f'{path.relative_to(ROOT)}:{n}', 'em-dash')

    def check_leaks(self):
        for path in self.tracked_files() + [p for p in OUT.rglob('*') if p.is_file()]:
            try:
                text = path.read_text()
            except (UnicodeDecodeError, OSError):
                continue
            for name, pattern in self.LEAKS:
                if pattern.search(text):
                    self.fail('leaks', path.relative_to(ROOT), f'looks like a {name}')

    def run(self):
        if not OUT.exists():
            sys.exit('build first: python3 admin/build/build.py')
        for check in (self.check_links, self.check_reachable, self.check_twins_and_index, self.check_chrome, self.check_stamps,
                      self.check_no_remote_code, self.check_scripts_parse, self.check_book, self.check_prose, self.check_leaks):
            check()
        if self.findings:
            print('\n'.join(self.findings))
            sys.exit(f'gate: {len(self.findings)} finding(s)')
        print(f'gate: clean ({len(self.html_files())} html files)')


if __name__ == '__main__':
    Gate().run()
