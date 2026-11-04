# The printed page of every paragraph of RC2 (A8: "a page-by-page view, like the PDF on an iPad"): builds the 30-page,
# 70-page and full drafts with the publisher's own command (publishing/build_book.py, run and never changed, with the arguments
# .github/workflows/release.yml gives it, stamp included so the page breaks are the published ones) into a temporary
# directory that is removed afterwards (TMPDIR points into it, so the publisher's own temporary folders go with it), reads
# each page's text with pdftotext, and finds each anchored paragraph of review/anchors/editions.json on its page: by six
# words from its start, or a little further in; a figure or clock line, a rule or a paragraph not found takes the page of
# the one before. Writes only review/anchors/print-pages.json: anchors, page numbers and a hash of the chapters, no text.
# make_editions.py's page view uses it while the hash matches. Kept by developer@book.the-ultimate-insider.
# Run, in this order: make_editions.py <talk clone> (so editions.json holds today's anchors), print_pages.py, make_editions.py again.
# By default only the full book is built (FB1); the other editions keep their last map, and show by scene once their chapters change. --all builds all.
import hashlib, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'review' / 'anchors' / 'print-pages.json'
COMMON = ['--no-toc', '--no-epub', '--cast', '--figures', 'publishing/rc2-figures.json',
          '--cover', 'lab/experiments/33-designer-cover-studies/cover-a-signed.svg', '--extra-css', 'lab/tools/book/speakers.css']
BUILDS = {   # as release.yml: its book list, its name and its stamp
    'rc2': (None, 'one-human-nine-agents-rc2-draft',
            'One Human, Nine Agents, Nineteen Hours: RC2, the 30-page edition, DRAFT IN REVIEW'),
    'rc2-70': (None, 'one-human-nine-agents-rc2-70-draft', 'One Human, Nine Agents, Nineteen Hours: RC2, the 70-page edition, DRAFT IN REVIEW'),
    'rc2-150': (None, 'one-human-nine-agents-rc2-full-draft', 'One Human, Nine Agents, Nineteen Hours: RC2, the full book, DRAFT IN REVIEW'),
}
norm = lambda t: re.sub(r'[^a-z0-9]+', ' ', t.lower()).strip()


def chapters_hash(files):
    h = hashlib.sha256()
    for f in files:
        h.update(f.name.encode() + b'\0' + f.read_bytes())
    return h.hexdigest()[:16]


def book_files(slug):
    if slug == 'rc2':
        return sorted((ROOT / 'manuscript' / 'rc2' / '30').glob('*.md'))
    txt = ROOT / 'manuscript' / 'editions' / slug / 'Book.txt'
    return [(txt.parent / l.strip()).resolve() for l in txt.read_text().splitlines() if l.strip() and not l.startswith('#')]


def build_pdf(slug, tmp, env):
    """The edition's PDF as release.yml builds it (publishing/build_book.py, run and never changed), in tmp; its path, or None."""
    _, name, stamp = BUILDS[slug]
    files = book_files(slug)
    if slug == 'rc2':
        book = Path(tmp) / 'rc2-book.txt'
        book.write_text(''.join(f'{f}\n' for f in files))
    else:
        book = ROOT / 'manuscript' / 'editions' / slug / 'Book.txt'
    r = subprocess.run([sys.executable, 'publishing/build_book.py', '--book', str(book), *COMMON, '--name', name, '--out', tmp, '--stamp', stamp],
                       cwd=ROOT, env=env, capture_output=True, text=True)
    pdf = Path(tmp) / f'{name}.pdf'
    return pdf if pdf.exists() and not r.returncode else None


def read_pdf(pdf):
    """The PDF's page count and each page's text, as words (norm)."""
    n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True).stdout).group(1))
    return n, [norm(subprocess.run(['pdftotext', '-f', str(i), '-l', str(i), str(pdf), '-'], capture_output=True, text=True).stdout) for i in range(1, n + 1)]


def map_paragraphs(chapters, pages):
    """Each anchored paragraph's printed page (by six words from its start, or a little further in); a figure or clock line, a
    rule or a paragraph not found takes the page before. -> ({anchor: page}, found, carried)"""
    n, where, last, found, carried = len(pages), {}, 1, 0, 0
    for c in chapters:
        for sc in c['scenes']:
            for p in sc['paragraphs']:
                t = p['text']
                hit = None
                if not re.match(r'(Figure|Clock):', t) and norm(t):
                    w = norm(re.sub(r'^[\w-]+(\s\([^)]*\))?[.:]\s+', '', t)).split()    # without a speaker's label
                    keys = [' '.join(w[i:i + 6]) for i in (0, 6, 12) if len(w) >= i + 6] or [' '.join(w)]
                    hit = next((i + 1 for i in range(last - 1, n) if any(k and k in pages[i] for k in keys)), None)
                if hit:
                    found, last = found + 1, hit
                else:
                    carried += 1
                where[p['id']] = hit or last
    return where, found, carried


def main(only):
    data = {e['edition']: e for e in json.loads((ROOT / 'review' / 'anchors' / 'editions.json').read_text())['editions']}
    out = {'about': 'The printed page of each anchored paragraph of RC2, from the PDFs built as release.yml builds them. '
                    'Written by review/tools/print_pages.py; read by make_editions.py while the chapters hash matches.', 'editions': {}}
    if OUT.exists():                                                  # editions not rebuilt this run keep their map (stale ones fall back to scenes by their hash)
        out['editions'] = {k: v for k, v in json.loads(OUT.read_text()).get('editions', {}).items() if k not in only}
    tmp = tempfile.mkdtemp(prefix='print_pages_')
    try:
        env = dict(os.environ, TMPDIR=tmp)
        for slug in only:
            files = book_files(slug)
            pdf = build_pdf(slug, tmp, env)
            if not pdf:
                print(f'{slug}: the PDF did not build; its page view stays by scene', file=sys.stderr)
                continue
            n, pages = read_pdf(pdf)
            where, found, carried = map_paragraphs(data[slug]['chapters'], pages)
            out['editions'][slug] = {'pdf_pages': n, 'chapters_hash': chapters_hash(files), 'found': found, 'carried': carried, 'pages': where}
            print(f'{slug}: {n} printed pages; {found} paragraphs found on their page, {carried} take the page before')
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    OUT.write_text(json.dumps(out, indent=1) + '\n')


if __name__ == '__main__':
    # FB1 (the editor, 4 November): the full book only. The other editions are deferred, not withdrawn: --all builds them too.
    main(list(BUILDS) if '--all' in sys.argv[1:] else ['rc2-150'])
