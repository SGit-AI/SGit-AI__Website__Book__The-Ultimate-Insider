# A look at the full book's printed pages (conductor__036, the editor's note of 4 November: "a pass on pagination, and making
# sure that all pages look ok"). It builds the full book's PDF as release.yml builds it (publishing/build_book.py, run and never
# changed; see print_pages.build_pdf), in a temporary folder that is removed afterwards, reads each page with pdftotext and each
# image's printed size with pdfimages and each page's fill with pdftoppm (all inside that folder), and flags:
#   chapter_end_spill  a chapter's last page less than a quarter full (the tail of the chapter alone, as in the editor's screenshot);
#   gap_page           a page inside a chapter whose content stops well short of the foot of the text block (a figure or heading
#                      pushed to the next page, or a figure out of proportion to its page), measured on the rendered page, so a
#                      figure drawn as a vector counts too;
#   figure_apart       a raster figure whose introducing paragraph is on an earlier page (only where a chapter's figure lines and
#                      its raster images can be paired by count; most figures are vector drawings that pdfimages cannot see).
# What it cannot tell is written into the result, not guessed: whether a gap is meant (a divider, an opener), which figure is which
# in the chapters it cannot pair, and anything about how a page looks beyond how far its content reaches. It also reports, as
# information and not as a flag, the pages with a raster figure taller than 45% of the text block (the publisher's own warning). It writes only review/anchors/print-check.json: page numbers, chapter titles, counts
# and sizes; no text from the PDF and no path. Kept by developer@book.the-ultimate-insider.
# Run: python3 review/tools/print_check.py [--stats]    (after make_editions.py, so editions.json holds today's chapters)
#      python3 -I review/tools/print_check.py --pdf FILE  checks a PDF it is given (the release's own, downloaded by hand into a folder of
#      its own) instead of building one: this container's build was one page longer than CI's on 4 November (141 against 140, from the
#      same inputs), so page numbers from a local build can sit a page off the published file. The tool itself never fetches anything.

import json, os, re, shutil, subprocess, sys, tempfile
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from print_pages import ROOT, build_pdf, read_pdf, map_paragraphs, norm, chapters_hash, book_files   # noqa: E402

OUT = ROOT / 'review' / 'anchors' / 'print-check.json'
SLUG = 'rc2-150'                                                      # FB1: the full book only
TEXT_HEIGHT = 9.69 - 0.5 - 0.625                                      # inches: the Crown Quarto page less book.css's margins (publishing/build_book.py, line 68)
DPI = 30                                                              # pages are rendered small: only how far the content reaches is wanted
GAP_FILL = 0.70                                                       # content ending above this share of the text block, inside a chapter, is a gap
INK = 230                                                             # a pixel darker than this (of 255) is content
SPILL_FILL = 0.25                                                     # a chapter's last page less than a quarter full is a spill: the tail of the chapter alone
LARGE_SHARE = 0.45                                                    # the publisher's own "printed taller than 45% of the text block"
BIG_IMAGE_INCHES = 1.0                                                # an image at least this tall counts as a figure; smaller ones are marks and cast bars


def page_lines(pdf, n):
    """Each page's lines of text, without the running head (a line on at least 40% of the pages) and the page number."""
    raw = []
    for i in range(1, n + 1):
        t = subprocess.run(['pdftotext', '-layout', '-f', str(i), '-l', str(i), str(pdf), '-'], capture_output=True, text=True).stdout
        raw.append([ln.strip() for ln in t.splitlines() if ln.strip()])
    common = {ln for ln, k in Counter(ln for page in raw for ln in set(page)).items() if k >= 0.4 * n}
    return [[ln for ln in page if ln not in common and not re.fullmatch(r'\d{1,4}', ln)] for page in raw]


def page_images(pdf):
    """[(page, inches tall)] for each image, from pdfimages' own placement (the publisher's tall_images does the same)."""
    rows = subprocess.run(['pdfimages', '-list', str(pdf)], capture_output=True, text=True).stdout.splitlines()[2:]
    out = []
    for f in (r.split() for r in rows):
        if len(f) >= 14 and f[2] == 'image':
            h, yppi = int(f[4]), int(f[13])
            out.append((int(f[0]), h / yppi if yppi else 0.0))
    return out


def page_fill(pdf, n, tmp):
    """How far down the text block each page's content reaches (0 to 1; None for a page with nothing in the block), from the
    page rendered small (pdftoppm, into tmp). The running head and the page number sit outside the block and are skipped."""
    subprocess.run(['pdftoppm', '-r', str(DPI), '-gray', str(pdf), str(Path(tmp) / 'pg')], capture_output=True)
    y0, y1 = round(0.5 * DPI), round((9.69 - 0.625) * DPI)
    out = []
    for i in range(1, n + 1):
        f = next(Path(tmp).glob(f'pg-*{i}.pgm'.replace('*', '0' * (len(str(n)) - len(str(i))))), None)
        if not f:
            out.append(None)
            continue
        raw = f.read_bytes()
        m = re.match(rb'P5\s+(\d+)\s+(\d+)\s+255\s', raw)
        w, h = int(m.group(1)), int(m.group(2))
        px = raw[m.end():]
        last = None
        for row in range(min(y1, h - 1), y0 - 1, -1):
            if min(px[row * w:(row + 1) * w]) < INK:
                last = row
                break
        out.append(None if last is None else round((last - y0 + 1) / (y1 - y0 + 1), 2))
    return out


def chapter_starts(chapters, pages):
    """The page each chapter opens on: its title in the first lines of a page, searching on from the last one found."""
    starts, at = [], 1
    for c in chapters:
        t = norm(c['title'])
        hit = next((i + 1 for i in range(at - 1, len(pages)) if t and t in pages[i][:400]), None)
        starts.append(hit)
        if hit:
            at = hit
    return starts


def main(stats, given=None):
    data = next(e for e in json.loads((ROOT / 'review' / 'anchors' / 'editions.json').read_text())['editions'] if e['edition'] == SLUG)
    chapters = data['chapters']
    tmp = tempfile.mkdtemp(prefix='print_check_')
    try:
        if given:
            pdf = Path(given)
            if not pdf.is_file():
                sys.exit(f'{pdf}: no such file')
            created = next((l.split(':', 1)[1].strip() for l in subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True).stdout.splitlines()
                            if l.startswith('CreationDate')), 'unknown')
            source = f'a PDF given by hand ({pdf.name}, created {created}); its chapters are taken to be today\'s'
        else:
            pdf = build_pdf(SLUG, tmp, dict(os.environ, TMPDIR=tmp))
            source = 'built here as release.yml builds it (this container\'s build may differ from CI\'s by a page or so)'
        if not pdf:
            sys.exit('the full book did not build: nothing checked')
        n, words = read_pdf(pdf)
        lines = page_lines(pdf, n)
        images = page_images(pdf)
        fills = page_fill(pdf, n, tmp)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    where, found, _, findable = map_paragraphs(chapters, words)
    starts = chapter_starts(chapters, [' '.join(w.split()[:80]) for w in words])               # each page's first words
    big_on = {}
    for p, inch in images:
        if inch >= BIG_IMAGE_INCHES:
            big_on.setdefault(p, []).append(inch)
    if stats:
        for i in range(1, n + 1):
            print(f'page {i:3}: {len(lines[i - 1]):3} lines, fill {fills[i - 1]}, images {[round(x, 2) for p, x in images if p == i]}')
        print('chapter starts:', starts)
        return
    # chapter page ranges
    ranges = []
    for k, c in enumerate(chapters):
        if starts[k]:
            nxt = next((s for s in starts[k + 1:] if s), n + 1)
            ranges.append((c['title'], starts[k], nxt - 1))
    flags, cannot = [], []
    last_of = {end: title for title, start, end in ranges if end > start}
    first_ch = min((st for st in starts if st), default=1)
    for i in range(1, n + 1):
        nl, fill = len(lines[i - 1]), fills[i - 1]
        if i in last_of and fill is not None and fill < SPILL_FILL:
            flags.append({'kind': 'chapter_end_spill', 'page': i, 'chapter': last_of[i], 'lines': nl, 'fill': fill})
        elif i >= first_ch and i not in last_of and fill is not None and fill < GAP_FILL and not any(i == s for s in starts if s):
            flags.append({'kind': 'gap_page', 'page': i, 'chapter': next((t for t, st, e in ranges if st <= i <= e), None),
                          'fill': fill, 'lines': nl, 'raster_figure_here': i in big_on, 'borderline': fill >= GAP_FILL - 0.03})   # within three points of the line: a prompt to look, not a finding
    tall = sorted({p for p, inch in images if inch > LARGE_SHARE * TEXT_HEIGHT})
    # figures apart from their introducing paragraph, where a chapter's figure lines and large images can be paired in order
    unpaired = []
    for k, c in enumerate(chapters):
        if not starts[k]:
            cannot.append(f'chapter "{c["title"]}": its opening page was not found, so its figures are not checked')
            continue
        end = next((s for s in starts[k + 1:] if s), n + 1) - 1
        paras = [p for sc in c['scenes'] for p in sc['paragraphs']]
        figs = [(j, p) for j, p in enumerate(paras) if p['text'].startswith('Figure:') and j > 0]
        pics = sorted(p for p, inch in images if starts[k] <= p <= end and inch >= BIG_IMAGE_INCHES)
        if len(figs) != len(pics):
            if figs or pics:
                unpaired.append((c['title'], len(figs), len(pics)))
            continue
        for (j, _), page in zip(figs, pics):
            intro = where.get(paras[j - 1]['id'])
            if intro and page - intro >= 1:
                flags.append({'kind': 'figure_apart', 'page': page, 'chapter': c['title'], 'intro_page': intro, 'pages_apart': page - intro})
    if unpaired:
        cannot.append(f'{len(unpaired)} chapters have a different number of figure lines and large images, so their figures are not paired: '
                      + '; '.join(f'"{t}" ({a} lines, {b} images)' for t, a, b in unpaired))
    cannot += ['whether a gap or a short page is meant (a divider, an opener, a page left to a drawing): it measures how far the content reaches',
               'which figure is which in the chapters it could not pair, and the figures drawn as vectors, which pdfimages cannot see: those are judged only by the gaps they leave',
               'how a page looks beyond how far its content reaches']
    # the list in the order it is read: tails emptiest first, then gap pages emptiest first, then the low-confidence figure separations
    flags.sort(key=lambda f: ({'chapter_end_spill': 0, 'gap_page': 1, 'figure_apart': 2}[f['kind']], f.get('fill', f['page'])))   # emptiest first
    # what changed since the last run, by kind and chapter (page numbers move whenever the layout does, so they cannot be compared)
    since = None
    if OUT.exists():
        prev = json.loads(OUT.read_text())
        a, b = Counter((f['kind'], f['chapter']) for f in prev['flags']), Counter((f['kind'], f['chapter']) for f in flags)
        row = lambda k, c: {'kind': k, 'chapter': c, 'before': a.get((k, c), 0), 'now': b.get((k, c), 0)}
        since = {'previous_pdf_pages': prev['pdf_pages'], 'previous_counts': prev['counts'],
                 'fixed': [row(*key) for key in a if b.get(key, 0) < a[key]],
                 'new': [row(*key) for key in b if b[key] > a.get(key, 0)],
                 'remaining': [row(*key) for key in b if key in a and b[key] >= a[key]]}
    result = {'about': 'The full book\'s printed pages checked for pages that may not look right (conductor__036). Written by review/tools/print_check.py: page numbers, chapter titles, counts and sizes only.',
              'edition': SLUG, 'source': source, 'pdf_pages': n, 'chapters_hash': chapters_hash(book_files(SLUG)),
              'thresholds': {'spill_fill_below': SPILL_FILL, 'gap_fill_below': GAP_FILL, 'tall_figure_share': LARGE_SHARE, 'figure_inches_at_least': BIG_IMAGE_INCHES},
              'chapters_found': sum(1 for s in starts if s), 'chapters': len(chapters),
              'counts': dict(Counter(f['kind'] for f in flags)), 'flags': flags, 'raster_figures_over_45_percent_on_pages': tall, 'since_last': since, 'cannot_tell': cannot}
    if findable and found < 0.6 * findable:                             # the figure check leans on the paragraph pages: say so when they are not trustworthy
        result['cannot_tell'].insert(0, f'paragraph pages could not be matched well ({found} of {findable}), so the figure separations below are not reliable')
        result['flags'] = [f for f in result['flags'] if f['kind'] != 'figure_apart']
        result['counts'] = dict(Counter(f['kind'] for f in result['flags']))
    result['paragraphs_found_on_a_page'] = {'found': found, 'of': findable}
    OUT.write_text(json.dumps(result, indent=1, ensure_ascii=False) + '\n')
    print(f'{n} pages; {len(starts) - starts.count(None)} of {len(chapters)} chapters located; flags: {result["counts"] or "none"}')
    for f in flags:
        print(' ', {k: v for k, v in f.items()})
    if since:
        print(f'since the last run ({since["previous_pdf_pages"]} pages, {since["previous_counts"]}):')
        for name in ('fixed', 'new', 'remaining'):
            for x in since[name]:
                print(f'  {name}: {x["kind"]} in "{x["chapter"]}": {x["before"]} -> {x["now"]}')
    for c in cannot:
        print('  cannot tell:', c)


if __name__ == '__main__':
    args = sys.argv[1:]
    main('--stats' in args, args[args.index('--pdf') + 1] if '--pdf' in args else None)
