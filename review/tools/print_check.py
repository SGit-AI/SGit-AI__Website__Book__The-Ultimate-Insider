# A look at the full book's printed pages (conductor__036, the editor's note of 4 November: "a pass on pagination, and making
# sure that all pages look ok"). It builds the full book's PDF as release.yml builds it (publishing/build_book.py, run and never
# changed; see print_pages.build_pdf), in a temporary folder that is removed afterwards, reads each page with pdftotext and each
# image's printed size with pdfimages and each page's fill with pdftoppm (all inside that folder), and flags:
#   chapter_end_spill  a chapter's last page less than a quarter full (the tail of the chapter alone, as in the editor's screenshot);
#   gap_page           a page inside a chapter whose content stops well short of the foot of the text block (a figure or heading
#                      pushed to the next page, or a figure out of proportion to its page), measured on the rendered page, so a
#                      figure drawn as a vector counts too;
#   figure_apart       a figure whose printed caption begins on a later page than the one its introducing paragraph ends on. Each
#                      figure is found by its caption (the "Figure:" lines of review/anchors/editions.json are the printed captions),
#                      so vector drawings count as much as images; the comparison is made in memory and no caption text is kept.
# What it cannot tell is written into the result, not guessed: whether a gap is meant (a divider, an opener), whether the drawing
# under a caption is on the caption's page, and anything about how a page looks beyond how far its content reaches. It also
# reports, as information and not as a flag, the pages with a raster figure taller than 45% of the text block (the publisher's
# own warning). It writes only review/anchors/print-check.json: page numbers, chapter titles, counts
# and sizes; no text from the PDF and no path. Kept by developer@book.the-ultimate-insider.
# Run: python3 review/tools/print_check.py [--stats]    (after make_editions.py, so editions.json holds today's chapters)
#      python3 -I review/tools/print_check.py --pdf FILE  checks a PDF it is given (the release's own, downloaded by hand into a folder of
#      its own) instead of building one: this container's build was one page longer than CI's on 4 November (141 against 140, from the
#      same inputs), so page numbers from a local build can sit a page off the published file. The tool itself never fetches anything.
#      python3 -I review/tools/print_check.py --pdf FILE --chapters-json FILE  also reads the chapters file the build writes beside the PDF
#      (publisher__007: each chapter's first page), downloaded by hand into the same folder as the PDF. It is untrusted data: read as JSON
#      only, checked for shape and size, used for page numbers only, and ignored (with a line in cannot_tell) if any check fails; no title,
#      file name or other text from it is kept. A chapter it does not name keeps the title finder's page.

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


def tidy(words):
    """Each page's tokens without the running head and the page number, so that words broken across a page break read on."""
    toks = [w.split() for w in words]
    heads = Counter(tuple(t[:13]) for t in toks if len(t) >= 13)
    head = list(heads.most_common(1)[0][0]) if heads else []
    out = []
    for t in toks:
        if head and t[:len(head)] == head:
            t = t[len(head):]
        if t and t[-1].isdigit() and len(t[-1]) <= 3:
            t = t[:-1]
        out.append(t)
    return out


def locate(tokens, key, first, last):
    """(page of the first word, page of the last word) of the first place, from page `first` to `last`, where the key words run
    on, even across a page break; or None. A run that begins at the foot of a page and ends on the next is seen as such."""
    k = len(key)
    for p in range(first, last + 1):
        t = tokens[p - 1] + (tokens[p][:k + 4] if p < len(tokens) else [])
        for i in range(len(tokens[p - 1])):
            if t[i:i + k] == key:
                return p, (p if i + k <= len(tokens[p - 1]) else p + 1)
    return None


def figure_placements(chapters, words, where):
    """Each Figure line found by its printed caption. For the nearest prose paragraph before it: the page it ends on (its last six
    words, from the page it begins on, at most three pages on); then the page the caption begins on (the first six words after
    "Figure:", from there, at most three pages on). A figure with a heading between it and that paragraph (a figure straight
    under a heading, which introduces it) is not checked: a section opening on a new page is not a separation.
    -> ([(chapter, intro_end_page, caption_page)], not_found, total, under_a_heading)"""
    n, out, missing, total, under_heading = len(words), [], 0, 0, 0
    by_heading, unplaced, note_rule = [], 0, 0
    tok = tidy(words)
    for c in chapters:
        paras = [p for sc in c['scenes'] for p in sc['paragraphs']]
        for j, p in enumerate(paras):
            if not p['text'].startswith('Figure:'):
                continue
            total += 1
            k = j - 1
            while k >= 0 and (paras[k]['text'].startswith(('Figure:', 'Clock:')) or paras[k].get('in_print') is False):
                k -= 1                                                  # past another figure, a clock line or a paragraph the print leaves out
            h = next((m for m in range(k + 1, j + 1) if paras[m].get('after_heading')), None)
            if h is not None:
                under_heading += 1                                      # a heading opens the section the figure is in: the heading introduces it (publisher__004)
                hs = next((where[paras[m]['id']] for m in range(h, len(paras)) if paras[m]['id'] in where and not paras[m]['text'].startswith(('Figure:', 'Clock:'))), None)   # the first printed paragraph at or after the heading's section
                hk = norm(paras[h].get('heading') or '').split()[:6] if isinstance(paras[h].get('heading'), str) else []
                hit = locate(tok, hk, max(1, hs - 2), hs) if hs and hk else None
                if hit:
                    capkey = norm(p['text'][len('Figure:'):]).split()[:6]
                    cp = locate(tok, capkey, hit[1], min(n, hit[1] + 3)) if capkey else None
                    if cp:
                        by_heading.append((c['title'], hit[1], cp[0]))
                    else:
                        missing += 1
                else:
                    unplaced += 1                                       # the heading's page could not be found: not checked
                continue
            if k >= 0 and paras[k]['text'].strip() == 'Dramatised.':
                # publisher__005: the one-line "Dramatised." note directly before a figure is the figure's introduction, and the build
                # keeps the two together. Only this exact note counts; any other figure is checked as before.
                before = next((where[paras[m]['id']] for m in range(k - 1, -1, -1) if paras[m]['id'] in where), None)
                capkey = norm(p['text'][len('Figure:'):]).split()[:6]
                hit = locate(tok, capkey, before, min(n, before + 4)) if before and capkey else None   # the caption (a "Figure to come:" box may print in front of it)
                if hit:
                    cp = hit[0]
                    line = tok[cp - 1]
                    at = next((i for i in range(len(line) - len(capkey) + 1) if line[i:i + len(capkey)] == capkey), 0)
                    near = line[max(0, at - 6):at]                      # the few words just before the caption on its page
                    prev = tok[cp - 2][-3:] if cp >= 2 and at < 6 else []   # or the last words of the page before, when the caption opens its page
                    if 'dramatised' in near:
                        note = cp
                    elif 'dramatised' in prev:
                        note = cp - 1
                    else:                                               # the note is not beside the caption (a drawing's own text may sit between): judge by the paragraph before the note, as for any figure
                        k2 = next((m for m in range(k - 1, -1, -1) if paras[m]['id'] in where), None)
                        w2 = norm(re.sub(r'^[\w-]+(\s\([^)]*\))?[.:]\s+', '', paras[k2]['text'])).split() if k2 is not None else []
                        h2 = locate(tok, w2[-6:], before, min(n, before + 3)) if w2 else None
                        note = h2[1] if h2 else before
                    out.append((c['title'], note, cp))
                    note_rule += 1
                else:
                    missing += 1
                continue
            start = where.get(paras[k]['id']) if k >= 0 else None
            if not start:
                continue                                                # a figure with no paragraph before it in its chapter
            w = norm(re.sub(r'^[\w-]+(\s\([^)]*\))?[.:]\s+', '', paras[k]['text'])).split()
            hit = locate(tok, w[-6:], start, min(n, start + 3)) if w else None
            end = hit[1] if hit else start                              # the page the paragraph's LAST word is on
            capkey = norm(p['text'][len('Figure:'):]).split()[:6]
            hit = locate(tok, capkey, end, min(n, end + 3)) if capkey else None
            cap = hit[0] if hit else None                               # the page the caption's FIRST word is on
            if cap is None:
                missing += 1
                continue
            out.append((c['title'], end, cap))
    return out, missing, total, under_heading, by_heading, unplaced, note_rule


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


def chapters_json_starts(path, n_pages, chapters, found_by_title):
    """The chapters file the build writes beside its PDF, as untrusted data: returns (starts, counts, problem). starts is the title finder's list with
    the file's page for every chapter the file names (matched by the base name of the file); counts holds integers only. On any fault: (None, None, why)
    with a fixed sentence that quotes nothing from the file."""
    try:
        p = Path(path)
        if not p.is_file() or p.stat().st_size > 1_000_000:
            return None, None, 'the chapters file is missing or larger than 1 MB: ignored'
        d = json.loads(p.read_text(encoding='utf-8'))
        rows = d['chapters'] if isinstance(d, dict) else None
        if not isinstance(rows, list) or not rows or len(rows) > 200:
            return None, None, 'the chapters file has no usable list of chapters: ignored'
        pages, by_name = [], {}
        for r in rows:
            f, pg = (r.get('file'), r.get('page')) if isinstance(r, dict) else (None, None)
            if not isinstance(f, str) or len(f) > 200 or type(pg) is not int or not 1 <= pg <= n_pages:
                return None, None, 'the chapters file has an entry of the wrong shape or a page outside the PDF: ignored'
            if pages and pg <= pages[-1]:
                return None, None, 'the chapters file has pages that do not increase: ignored'
            pages.append(pg)
            by_name.setdefault(os.path.basename(f.replace('\\', '/')), pg)
        starts, matched, disagree = [], 0, 0
        for c, by_title in zip(chapters, found_by_title):
            pg = by_name.get(os.path.basename(str(c.get('file', '')).replace('\\', '/')))
            if pg is None:
                starts.append(by_title)
                continue
            matched += 1
            disagree += by_title != pg
            starts.append(pg)
        seen = [s for s in starts if s]
        if seen != sorted(set(seen)):
            return None, None, 'the chapters file does not fit the book\'s chapters in order: ignored'
        return starts, {'in_file': len(rows), 'matched': matched, 'disagree_with_the_title_finder': disagree}, None
    except (OSError, ValueError, UnicodeError, AttributeError, TypeError, KeyError, RecursionError, MemoryError):
        return None, None, 'the chapters file could not be read as JSON: ignored'


def main(stats, given=None):
    chap_file = Path(sys.argv[sys.argv.index('--chapters') + 1]) if '--chapters' in sys.argv else ROOT / 'review' / 'anchors' / 'editions.json'   # --chapters FILE: today's chapters from make_editions.py --dry --data-out
    data = next(e for e in json.loads(chap_file.read_text())['editions'] if e['edition'] == SLUG)
    chapters = data['chapters']
    tmp = tempfile.mkdtemp(prefix='print_check_')
    try:
        if given:
            pdf = Path(given)
            if not pdf.is_file():
                sys.exit(f'{pdf}: no such file')
            created = next((l.split(':', 1)[1].strip() for l in subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True).stdout.splitlines()
                            if l.startswith('CreationDate')), 'unknown')
            source = f'a PDF given by hand ({pdf.name}, created {created}); its chapters are {"a data file given by hand (--chapters)" if "--chapters" in sys.argv else "those of the online view, review/anchors/editions.json, as last built"}'
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
    chap_json = None
    chap_json_note = None
    if '--chapters-json' in sys.argv:
        got, chap_json, chap_json_note = chapters_json_starts(sys.argv[sys.argv.index('--chapters-json') + 1], n, chapters, starts)
        if got:
            starts = got
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
    # figures apart from the paragraph that introduces them, found by their printed captions
    placed, not_found, fig_total, under_heading, by_heading, unplaced, note_rule = figure_placements(chapters, words, where)
    for title, intro_end, cap in placed:
        if cap > intro_end:
            flags.append({'kind': 'figure_apart', 'page': cap, 'chapter': title, 'intro_page': intro_end, 'pages_apart': cap - intro_end})
    for title, head, cap in by_heading:
        if cap > head:
            flags.append({'kind': 'figure_apart', 'page': cap, 'chapter': title, 'intro_page': head, 'pages_apart': cap - head, 'introduced_by': 'a heading'})
    figures = {'figure_lines': fig_total, 'introduced_by_a_heading': under_heading, 'heading_checked': len(by_heading), 'heading_page_not_found': unplaced, 'introduced_by_the_dramatised_note': note_rule,
               'begin_on_a_later_page_than_their_heading': sum(1 for _, e, cp in by_heading if cp > e),
               'with_a_paragraph_before_them_in_the_section': len(placed), 'not_found': not_found,
               'begin_on_a_later_page_than_that_paragraph_ends': sum(1 for _, e, cp in placed if cp > e)}
    cannot += ['whether a gap or a short page is meant (a divider, an opener, a page left to a drawing): it measures how far the content reaches',
               f'{not_found} of {fig_total} figure lines could not be found by their printed caption; {under_heading} sit straight under a heading ({unplaced} of them with the page of the heading not found, not checked), which counts as what introduces them; for the rest it finds where the caption begins, not whether the drawing under it is on the same page',
               'how a page looks beyond how far its content reaches']
    if chap_json_note:
        cannot.insert(0, chap_json_note)
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
              'chapters_found': sum(1 for s in starts if s), 'chapters': len(chapters), 'chapters_file': chap_json,
              'counts': dict(Counter(f['kind'] for f in flags)), 'flags': flags, 'raster_figures_over_45_percent_on_pages': tall, 'figures': figures, 'since_last': since, 'cannot_tell': cannot}
    if findable and found < 0.6 * findable:                             # the figure check leans on the paragraph pages: say so when they are not trustworthy
        result['cannot_tell'].insert(0, f'paragraph pages could not be matched well ({found} of {findable}), so the figure separations below are not reliable')
        result['flags'] = [f for f in result['flags'] if f['kind'] != 'figure_apart']
        result['counts'] = dict(Counter(f['kind'] for f in result['flags']))
    result['paragraphs_found_on_a_page'] = {'found': found, 'of': findable}
    OUT.write_text(json.dumps(result, indent=1, ensure_ascii=False) + '\n')
    print(f'{n} pages; {len(starts) - starts.count(None)} of {len(chapters)} chapters located; flags: {result["counts"] or "none"}; figures: {figures}')
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
