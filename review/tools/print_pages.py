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
MIN_FOUND = 0.6                                                       # share of findable paragraphs that must be found for a map to be written
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


BACK = 12                                                          # how many pages back a paragraph is looked for when it is not ahead


def map_paragraphs(chapters, pages, window=8):
    """Each anchored paragraph's printed page (by six words from its start, or a little further in); a figure or clock line, a
    rule or a paragraph not found takes the page before. The search runs on from the last page found but only `window` pages
    ahead: paragraphs run in order, so a phrase repeated far ahead (the tour at length repeats the tour) must not carry the search
    off and strand every paragraph after it (found on 4 November: 81 of 1019 found, then 871 once bounded).
    -> ({anchor: page}, found, carried, findable) where findable counts the paragraphs that have words a page could hold."""
    n, where, last, found, carried, findable = len(pages), {}, 1, 0, 0, 0
    for c in chapters:
        for sc in c['scenes']:
            for p in sc['paragraphs']:
                if p.get('in_print') is False:                      # in a section the print leaves out: it has no page, and is neither found nor missed
                    where[p['id']] = last
                    continue
                t = p['text']
                hit = None
                if not re.match(r'(Figure|Clock):', t) and norm(t):
                    w = norm(re.sub(r'^[\w-]+(\s\([^)]*\))?[.:]\s+', '', t)).split()    # without a speaker's label
                    keys = [' '.join(w[i:i + 6]) for i in (0, 6, 12) if len(w) >= i + 6] or [' '.join(w)]
                    findable += 1
                    hit = next((i + 1 for i in range(last - 1, min(n, last + window)) if any(k and k in pages[i] for k in keys)), None)
                    if hit is None:                                 # not ahead: the pointer may have jumped past its place on a repeated phrase (found 5 November:
                        hit = next((i + 1 for i in range(last - 2, max(-1, last - 1 - BACK), -1) if any(k and k in pages[i] for k in keys)), None)   # a chapter stranded 4 pages behind it): look back, nearest first
                if hit:
                    found, last = found + 1, hit
                else:
                    carried += 1
                where[p['id']] = hit or last
    return where, found, carried, findable


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
            where, found, carried, findable = map_paragraphs(data[slug]['chapters'], pages)
            if findable and found < MIN_FOUND * findable:                # a map this poor would put most paragraphs on the wrong page: keep the old one (or none), so the view falls back to scenes
                print(f'{slug}: only {found} of {findable} paragraphs found on a page; the map is NOT written and its page view stays by scene', file=sys.stderr)
                continue
            out['editions'][slug] = {'pdf_pages': n, 'chapters_hash': chapters_hash(files), 'found': found, 'carried': carried, 'pages': where}
            print(f'{slug}: {n} printed pages; {found} paragraphs found on their page, {carried} take the page before')
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    OUT.write_text(json.dumps(out, indent=1) + '\n')


if __name__ == '__main__':
    # FB1 (the editor, 4 November): the full book only. The other editions are deferred, not withdrawn: --all builds them too.
    main(list(BUILDS) if '--all' in sys.argv[1:] else ['rc2-150'])
