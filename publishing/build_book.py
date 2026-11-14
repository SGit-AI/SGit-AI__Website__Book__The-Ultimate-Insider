#!/usr/bin/env python3
"""The manuscript build: one source, manuscript/ in the order of manuscript/Book.txt, gives the PDF and the EPUB.

Leanpub builds its own PDF and EPUB from the same Book.txt once the editor connects the repository; this
script is the team's own proof that the manuscript builds, runnable by anyone and in CI, so a broken
chapter is caught here and not on the Leanpub preview.

Needs pandoc (2.x or 3.x) and a Chromium or Chrome for the PDF (no LaTeX). Writes nothing tracked:
the output goes to _site/manuscript/ by default (gitignored, and published with the site when CI runs it
after admin/build/build.py).

    python3 publishing/build_book.py [--out DIR] [--chrome PATH] [--no-pdf] [--no-epub]
"""
import argparse
import base64
import datetime
import glob
import hashlib
import html as htmllib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

import markua
import edition  # the cast's conventions, for --cast

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANUSCRIPT = os.path.join(ROOT, "manuscript")
HERE = os.path.join(ROOT, "publishing")
NAME = "the-ultimate-insider"
CHROMES = (["chrome-headless-shell"] + sorted(glob.glob("/opt/pw-browsers/chromium_headless_shell-*/*/chrome-headless-shell"))
           + ["chromium", "chromium-browser", "google-chrome", "google-chrome-stable", "/opt/pw-browsers/chromium"])


def chapters(book=None):
    """The files a list names, in its order (manuscript/Book.txt unless --book names another, such as a sample's);
    names are relative to the list's own folder; blank lines and # comments skipped."""
    book = os.path.abspath(book) if book else os.path.join(MANUSCRIPT, "Book.txt")
    here = os.path.dirname(book)
    with open(book, encoding="utf-8") as f:
        names = [line.strip() for line in f if line.strip() and not line.lstrip().startswith("#")]
    missing = [n for n in names if not os.path.isfile(os.path.join(here, n))]
    if missing:
        sys.exit(f"build_book: {os.path.relpath(book, ROOT)} lists files that are not there: {', '.join(missing)}")
    if not names:
        sys.exit(f"build_book: {os.path.relpath(book, ROOT)} lists no files")
    return [os.path.join(here, n) for n in names]


def placed_drawing(rel):
    """One page of a placed spread: an .svg inside one folder of lab/experiments/ (resolved from the repository root,
    then checked by realpath), passing the drawings' check; every picture inside it must be byte for byte a screenshot
    cleared by name or kind (edition.shot_allowed), or the build stops (security 022)."""
    path = os.path.realpath(os.path.join(ROOT, rel))
    lab = os.path.join(os.path.realpath(ROOT), "lab", "experiments")
    if ".." in rel.split("/") or os.path.dirname(os.path.dirname(path)) != lab or not path.endswith(".svg") \
            or not os.path.isfile(path):
        sys.exit(f"build_book: a placed page must be an .svg in one folder of lab/experiments/: {rel}")
    with open(path, encoding="utf-8") as f:
        svg = f.read()
    placed_svg_check(svg, rel)
    return path, svg


def placed_svg_check(svg, rel):
    """The drawings' check, and every picture inside byte for byte a screenshot cleared by name; else the build stops."""
    if edition.unsafe_svg(svg):
        sys.exit(f"build_book: the placed page {rel} fails the drawings' check: {edition.unsafe_svg(svg)}")
    shots = os.path.join(ROOT, edition.SHOTS)
    cleared = set()
    for name in os.listdir(shots):
        if edition.shot_allowed(name):
            with open(os.path.join(shots, name), "rb") as fh:
                cleared.add(hashlib.sha256(fh.read()).hexdigest())
    for ref in re.findall(r"""href\s*=\s*["']([^"']*)["']""", svg):
        m = re.fullmatch(r"data:image/[a-z+.-]+;base64,([A-Za-z0-9+/=\s]+)", ref)
        if not m or hashlib.sha256(base64.b64decode(m.group(1))).hexdigest() not in cleared:
            sys.exit(f"build_book: the placed page {rel} carries a picture that is not a cleared screenshot")


INDEX_NUMBER = re.compile(r'(<text [^>]*data-file="([A-Za-z0-9._-]+)"[^>]*>)(\d+)(</text>)')


def index_numbers(pdf, files, titles, marked):
    """PEN1 note 7 (designer 169): the visual index's page numbers, each a text carrying data-file="<chapter file>",
    set from this build's own PDF; only those digit runs change, in a checked copy. The bar's widths stay as drawn.
    Returns "fixed", "ok" or "" (no index placed)."""
    starts = dict(zip((os.path.basename(f) for f in files), chapter_starts(pdf, titles)))
    for f in files:
        with open(f, encoding="utf-8") as fh:
            text = fh.read()
        for m in re.finditer(r':::: \{\.placed-page \.part-page\}\n<img src="([^"]+)"', text):
            with open(m.group(1), encoding="utf-8") as fh:
                svg = fh.read()
            if "data-file=" not in svg:
                continue
            new = INDEX_NUMBER.sub(lambda x: x.group(1) + (str(int(starts[x.group(2)])) if starts.get(x.group(2))
                                                           else x.group(3)) + x.group(4), svg)
            if new == svg:
                print("build_book: the visual index's pages match this PDF", file=sys.stderr)
                return "ok"
            placed_svg_check(new, "the visual index with its pages")
            copy = os.path.join(marked, "visual-index-numbered.svg")
            with open(copy, "w", encoding="utf-8") as fh:
                fh.write(new)
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(text.replace(f'<img src="{m.group(1)}"', f'<img src="{copy}"', 1))
            print("build_book: the visual index's pages set from this PDF", file=sys.stderr)
            return "fixed"
    return ""


PART_NUMBER = re.compile(r'(<text x="156\.00"[^>]*text-anchor="end">)(\d+)(</text>)')


def part_numbers(pdf, files, titles, marked):
    """PEN1 note 16 (designer 168, researcher 009): the five part pages drawn on the spread's page two, set from this
    build's own PDF (each part's lowest chapter start, as make_spread.py reads them). Only those five digit runs change,
    in a copy in the build's own folder, checked again. Returns "fixed", "ok", or "" (not found: nothing changed)."""
    starts = chapter_starts(pdf, titles)
    first = {}
    for k, f in enumerate(files):
        part = part_of(os.path.basename(f)) if titles[k] else None
        if part and starts[k]:
            first[part] = min(first.get(part, starts[k]), starts[k])
    wanted = [first.get(part) for part, _ in PARTS]
    if None in wanted:
        print("build_book: WARNING a part's first page was not found: the spread's part pages left as drawn", file=sys.stderr)
        return ""
    for f in files:
        with open(f, encoding="utf-8") as fh:
            text = fh.read()
        m = re.search(r':::: \{\.placed-page \.placed-right\}\n<img src="([^"]+)"', text)
        if not m:
            continue
        with open(m.group(1), encoding="utf-8") as fh:
            svg = fh.read()
        drawn = [int(x.group(2)) for x in PART_NUMBER.finditer(svg)]
        if len(drawn) != 5:
            print("build_book: WARNING the spread's page two has no five part pages to set", file=sys.stderr)
            return ""
        if drawn == wanted:
            print(f"build_book: the spread's part pages match this PDF: {wanted}", file=sys.stderr)
            return "ok"
        it = iter(wanted)
        new = PART_NUMBER.sub(lambda x: x.group(1) + str(int(next(it))) + x.group(3), svg)
        placed_svg_check(new, "page two with its part pages")
        copy = os.path.join(marked, "spread-page-2-numbered.svg")
        with open(copy, "w", encoding="utf-8") as fh:
            fh.write(new)
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(text.replace(f'<img src="{m.group(1)}"', f'<img src="{copy}"', 1))
        print(f"build_book: the spread's part pages set from this PDF: {drawn} to {wanted}", file=sys.stderr)
        return "fixed"
    return ""


PARTS = [  # the five parts, by the storyteller's outline (chapter-plan/edition-150-outline.md, "The parts, beat by beat")
    ("Part one. The creator's problem", ("01", "02", "03", "03b")),
    ("Part two. The factory is assembled", ("04", "05", "06", "07", "08")),
    ("Part three. The factory runs", ("09", "10", "11", "12", "13", "14", "15")),
    ("Part four. The factory is stopped", ("16", "17", "17b", "18", "19")),
    ("Part five. The factory rebuilt, and yours", ("20", "21", "22", "23", "23b")),
]


def css_string(text):
    """Text made safe inside a CSS content string written into the page's <style>: no "<", control characters and
    anything outside printable text become spaces, then the backslash and the double quote are escaped."""
    text = "".join(c if c.isprintable() and c != "<" else " " for c in text)
    return text.replace("\\", "\\\\").replace('"', '\\"')


def part_of(name):
    """The part a chapter file belongs to, from its leading number ("03b-the-day..." is part 1), or None (front and back
    matter)."""
    key = name.split("-", 1)[0]
    return next((part for part, chapters in PARTS if key in chapters), None)


def running_footer(files, titles):
    """PEN1 notes 8, 9 and 20: each chapter on a named page of its own (by its index, never its title), whose footer
    gives the part and the chapter's title on the inner side, the page number staying on the outer, and a thin bar in
    the middle showing how far through the book the chapter stands. A chapter of placed pages keeps a bare footer.
    Progress within a chapter cannot be drawn: Chromium has no per-chapter page counter. The look is the designer's."""
    css, chapters = [], [k for k, f in enumerate(files) if titles[k]]
    for n, k in enumerate(chapters):
        with open(files[k], encoding="utf-8") as fh:
            text = fh.read()
        if ".placed-left" in text or ".placed-right" in text:  # the spread's placed pages; a part page is not one
            continue
        page = f"rf{k}"
        if not text.startswith(":::::: {.rf"):
            with open(files[k], "w", encoding="utf-8") as fh:
                fh.write(f":::::: {{.rf .{page}}}\n\n{text}\n\n::::::\n")
        part = part_of(os.path.basename(files[k]))
        # designer 171: the part's name on left pages, the chapter's title on right pages, each one line; capped before
        # escaping, so a cut never splits an escape
        cap = lambda s, n=48: s if len(s) <= n else s[:n - 1].rstrip() + "\u2026"
        right = css_string(cap(titles[k]))
        left = css_string(cap(part or titles[k]))
        done = round(100 * (n + 1) / len(chapters), 1)
        bar = (f'content: "\\00a0"; width: 1.1in; background: linear-gradient(to right, #6b7280 {done}%, #d9dde3 {done}%) '
               f'no-repeat center / 100% 1.6pt;')
        css.append(f".{page} {{ page: {page}; break-before: page; }}\n"
                   f'@page {page}:right {{ @bottom-left {{ content: "{right}"; font-family: Inter, Helvetica, Arial, '
                   f'sans-serif; font-size: 6.5pt; color: #6b7280; white-space: nowrap; }} @bottom-center {{ {bar} }} }}\n'
                   f'@page {page}:left {{ @bottom-right {{ content: "{left}"; font-family: Inter, Helvetica, Arial, '
                   f'sans-serif; font-size: 6.5pt; color: #6b7280; text-align: right; white-space: nowrap; }} '
                   f'@bottom-center {{ {bar} }} }}\n')
    return "".join(css)


def placed_first_page(pdf, svgs):
    """The PDF page that prints the first placed page: the first page whose text holds the drawing's first text line."""
    first_line = None
    for svg in svgs:
        m = re.search(r"<text[^>]*>([^<]{12,})</text>", svg)
        if m:
            first_line = htmllib.unescape(m.group(1)).strip()[:30]
            break
    if not first_line:
        return None
    pages = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True).stdout.split("\f")
    for n, page in enumerate(pages, 1):
        if first_line in " ".join(page.split()):
            return n
    return None


def release_stamp():
    """PEN1 note 15: "Version v0.1.N, PDF made 13 November 2026", from ./version (read only; CI writes it before the
    build) and today's date in UTC; nothing if ./version is missing or not a release number."""
    try:
        with open(os.path.join(ROOT, "version"), encoding="utf-8") as f:
            v = f.read().strip()
    except OSError:
        return ""
    if not re.fullmatch(r"v\d+\.\d+\.\d+", v):
        return ""
    today = datetime.datetime.now(datetime.timezone.utc)
    return f"Version {v}, PDF made {today.day} {today.strftime('%B %Y')}"


def placed_spread(raw, pages):
    """OS3: the chapter's flowed text and Figure lines give way to the two placed pages (the first on a left page, the
    second facing it). What the drawings do not carry is text: the narrator's "Throughout the book I am the Narrator"
    paragraph after them until page one carries it (a stopgap, writer 295), and the "We would love to hear from you"
    section laid over the foot of page two (OS4, brief 49; designer 161) until page two draws it (designer 163). Page
    two has two copies: the print interior (the build without --cover) places the one with FB2's address, the online
    draft (with --cover) the one that says "the address in the printed book"."""
    lines = raw.split("\n")
    title = htmllib.escape(next((l[2:].strip() for l in lines if l.startswith("# ")), ""), quote=True)
    keep = []
    if "Throughout the book I am" not in pages[0][1]:
        keep += [l for l in lines if l.startswith("**Narrator.** Throughout the book I am")]
    start = next((i for i, l in enumerate(lines) if l.startswith("## We would love to hear from you")), None)
    foot = []
    if start is not None and "We would love to hear from you" not in pages[-1][1]:  # OS4: page two may draw it (designer 163)
        end = next((j for j in range(start + 1, len(lines)) if re.match(r"#{1,2} ", lines[j])), len(lines))
        foot = [l for l in lines[start:end] if not l.lstrip().startswith("`%%") and l.strip() != "---"]
    out = [f'<h1 class="placed-title">{title}</h1>', ""]
    stamp = release_stamp()
    for k, (path, _) in enumerate(pages):
        side = "placed-left" if k == 0 else "placed-right"
        out += [f":::: {{.placed-page .{side}}}", f'<img src="{path}" alt="{title}: page {k + 1} of the opening spread">', ""]
        if k == len(pages) - 1 and foot:
            out += ["::: placed-foot", ""] + foot + ["", ":::", ""]
        if k == len(pages) - 1 and stamp:  # PEN1 note 15: under the "We would love to hear from you" box
            out += ["::: placed-stamp", stamp, ":::", ""]
        out += ["::::", ""]
    return "\n".join(out + keep) + "\n"


def directives(book=None):
    """A list's own build lines (the full book's, FB1 and WC1, 4 November 2026), so the release follows the list:
    "#! drop-section: <heading>" leaves out that "## " section of each chapter, from its heading to the next heading of
    the same or a higher level (the files are unchanged); "#! extra-css: <path>" adds a stylesheet, only from under
    publishing/."""
    book = os.path.abspath(book) if book else os.path.join(MANUSCRIPT, "Book.txt")
    drop, css = [], []
    with open(book, encoding="utf-8") as f:
        for line in f:
            if re.match(r"\s*#!\s*fit-tails\s*$", line):
                FIT["on"] = True
                continue
            if re.match(r"\s*#!\s*try-this-card\s*$", line):
                FIT["card"] = True
                continue
            if re.match(r"\s*#!\s*blocks\s*$", line):
                FIT["blocks"] = True
                continue
            if re.match(r"\s*#!\s*dramatised:\s*tag\s*$", line):
                FIT["dramatised"] = True
                continue
            if re.match(r"\s*#!\s*running-footer\s*$", line):  # PEN1 notes 8, 9, 20 (13 November 2026)
                FIT["footer"] = True
                continue
            if re.match(r"\s*#!\s*speaker-tags\s*$", line):
                FIT["speaker_tags"] = True
                continue
            m = re.match(r"\s*#!\s*title-page:\s*(.+?)\s*$", line)
            if m:  # the editor, 5 November 2026 (brief 51): the title page as a designed full page, in place of pandoc's
                tp = os.path.realpath(os.path.join(ROOT, m.group(1).strip()))
                if not tp.startswith(os.path.join(ROOT, "lab", "experiments") + os.sep) or not os.path.isfile(tp):
                    sys.exit(f"build_book: title-page must be a file in lab/experiments/: {m.group(1)}")
                FIT["title_page"] = tp
                continue
            m = re.match(r"\s*#!\s*(?:part-page|page-before):\s*(.+?)\s*\|\s*(.+?)\s*$", line)
            if m:  # PEN1 note 16 (designer 166, storyteller 169): a part's section page, before its first chapter
                chapter = os.path.realpath(os.path.join(os.path.dirname(book), m.group(1)))
                FIT.setdefault("part_pages", {})[chapter] = placed_drawing(m.group(2))
                continue
            m = re.match(r"\s*#!\s*placed-spread:\s*(.+?)\s*$", line)
            if m:  # OS3: a chapter printed as the designer's two placed pages (designer 160)
                parts = [x.strip() for x in m.group(1).split("|")]
                if len(parts) not in (3, 4):
                    sys.exit(f"build_book: placed-spread takes a chapter, two drawings and a print copy of page two: "
                             f"{m.group(1)}")
                chapter = os.path.realpath(os.path.join(os.path.dirname(book), parts[0]))
                pages = [placed_drawing(x) for x in parts[1:3]]
                if len(parts) == 4:  # designer 163: page two with the FB2 address, for the print interior only
                    FIT.setdefault("placed_print", {})[chapter] = placed_drawing(parts[3])
                FIT.setdefault("placed", {})[chapter] = pages
                continue
            m = re.match(r"\s*#!\s*cast-bars:\s*(.+?)\s*$", line)
            if m:  # the designer's map of a drawn cast bar per chapter (designer 135): a .json directly in lab/tools/book/
                path = os.path.realpath(os.path.join(ROOT, m.group(1)))
                if os.path.dirname(path) != os.path.join(os.path.realpath(ROOT), "lab", "tools", "book") \
                        or not path.endswith(".json") or not os.path.isfile(path):
                    sys.exit(f"build_book: cast-bars must be a .json directly in lab/tools/book/: {m.group(1)}")
                with open(path, encoding="utf-8") as fh:
                    FIT["bars"] = json.load(fh).get("bars", {})
                continue
            m = re.match(r"\s*#!\s*(drop-section|extra-css):\s*(.+?)\s*$", line)
            if not m:
                continue
            if m.group(1) == "drop-section":
                drop.append(m.group(2))
                continue
            path = os.path.realpath(os.path.join(ROOT, m.group(2)))
            root = os.path.realpath(ROOT)
            mine = path.startswith(os.path.join(root, "publishing") + os.sep)
            designers = os.path.dirname(path) == os.path.join(root, "lab", "tools", "book")  # the designer's book styles, directly
            if not (mine or designers) or not path.endswith(".css") or not os.path.isfile(path):
                sys.exit(f"build_book: {os.path.relpath(book, ROOT)}: extra-css must be a .css file under publishing/ or "
                         f"directly in lab/tools/book/: {m.group(2)}")
            if designers:
                why = unsafe_css(open(path, encoding="utf-8").read())
                if why:
                    sys.exit(f"build_book: refused {m.group(2)}: {why}")
            css.append(path)
    return drop, css


def unsafe_css(text):
    """Why a stylesheet from lab/tools/book/ is refused, or None (security, 4 November 2026): no @import, expression(),
    behavior, -moz-binding or backslash escape; a url() only #id or data:image/svg+xml;utf8 whose SVG passes the
    drawings' own check and holds no href."""
    from urllib.parse import unquote
    if re.search(r"@import|@font-face|expression\s*\(|\bbehavior\s*:|-moz-binding|image-set\s*\(|cross-fade\s*\(|\bsrc\s*\(|\\", text, re.I):
        return "an @import, @font-face, expression(), behavior, -moz-binding, image-set(), cross-fade(), src() or a backslash escape"
    for m in re.finditer(r"url\(\s*(['\"]?)(.*?)\1\s*\)", text, re.I | re.S):
        u = m.group(2).strip()
        if u.startswith("#"):
            continue
        if not u.lower().startswith("data:image/svg+xml;utf8,"):
            return "a url() that is not #id or data:image/svg+xml;utf8"
        svg = unquote(u.split(",", 1)[1])
        if edition.unsafe_svg(svg) or re.search(r"\bhref\b", svg, re.I):
            return "an embedded SVG that fails the drawings' check or holds an href"
    return None


FIT = {"on": False}  # "#! fit-tails": chapters whose last page holds only a few lines are set a little tighter


def chapter_starts(pdf, titles):
    """The PDF page (from 1) each chapter starts on, read as tail_chapters reads it, or None where its title is not found
    (a chapter of placed pages carries its title in a drawing)."""
    out = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True).stdout
    pages = [[l.strip() for l in pg.split("\n") if l.strip()] for pg in out.split("\f")]
    norm = lambda t: re.sub(r"\W+", " ", t).strip().lower()
    at = next((i + 1 for i, pg in enumerate(pages) if any(l == "Contents" for l in pg[:3])), 0)
    starts = []
    for t in titles:
        found = next((i for i in range(at, len(pages)) if t and norm(t) and  # the page opens with the title, under a
                      any(norm(" ".join(pages[i][j:j + 3])).startswith(norm(t)) for j in (0, 1))), None)  # --stamp line
        starts.append(found + 1 if found is not None else None)
        if found is not None:
            at = found + 1
    return starts


def tail_chapters(pdf, titles, most=8):
    """The chapters (by index) whose last page holds `most` lines or fewer, read from the PDF's text: a chapter starts on
    the first page, after the one before it, whose first few lines include its title."""
    out = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True).stdout
    pages = [[l.strip() for l in pg.split("\n") if l.strip()] for pg in out.split("\f")]
    norm = lambda t: re.sub(r"\W+", " ", t).strip().lower()
    at = next((i + 1 for i, pg in enumerate(pages) if any(l == "Contents" for l in pg[:3])), 0)  # after the contents
    starts = []
    for t in titles:
        found = None
        for i in range(at, len(pages)):
            if norm(t) and norm(" ".join(pages[i][:5])).find(norm(t)) != -1:
                found = i
                break
        starts.append(found)
        if found is not None:
            at = found + 1
    tails = []
    for k, st in enumerate(starts):
        if st is None:
            continue
        nxt = next((x for x in starts[k + 1:] if x is not None), len(pages))
        last = nxt - 1
        if last <= st:
            continue
        body = [l for l in pages[last] if not re.fullmatch(r"\d+", l) and not l.startswith("One Human, Nine Agents, Nineteen Hours:")]
        if len(body) <= most:
            tails.append(k)
    return tails


CARD_PARTS = (("tt-idea", "The idea"), ("tt-try", "What I would try first"), ("tt-gives", "What it gives you"))


def try_this_cards(text):
    """"#! try-this-card": a chapter's "## Something to try", "## Try this" or "## Do this now" section set as the
    designer's card (lab/tools/book/try-this.css; conductor 072, brief 10): the label "Try this" in every chapter, then
    three paragraphs as the idea, the try and what it gives, or one paragraph as the try alone."""
    def card(m):
        paras = [p.strip() for p in re.split(r"\n\s*\n", m.group(1).strip())
                 if p.strip() and not p.strip().startswith(("%%", "`%%", "---"))]
        out = ["", "::: try-this", "::: tt-label", "Try this", ":::", ""]
        if len(paras) == 3:
            for (cls, label), p in zip(CARD_PARTS, paras):
                out += [f"::: {cls}", f"[{label}]{{.tt-part}} " + p, ":::", ""]
        else:
            for p in paras:
                out += ["::: tt-try", p, ":::", ""]
        return "\n".join(out + [":::", "", ""])
    return re.sub(r"(?ms)^## (?:Something to try|Try this|Do this now)[ \t]*\n(.*?)(?=^#{1,2} |\Z)", card, text)


DRAM = {"marks": 0, "tags": 0, "dropped": 0}


SPEAKER_TAG = re.compile(r"^(\s*\*\*[A-Za-z][A-Za-z-]*\.?\*\*)\s*\*\(this book's\)\*", re.M)


def speaker_tags(text):
    """"#! speaker-tags" (TC1, the editor, 5 November 2026): a speaker line's italic "*(this book's)*" right after the
    name, at the line's start, prints as a small fixed tag (.speaker-tag), as the designer's tags.css draws it. Run after
    the dramatised step, which reads the parenthesis as the speaker's mood and sets its own tag after it. The files are
    unchanged."""
    return SPEAKER_TAG.sub(r"\1 [this book's]{.speaker-tag}", text)


def dramatised_tags(text):
    """"#! dramatised: tag" (DM1, the editor, 4 November 2026, option (c)): a "*Dramatised.*" line closes its scene,
    the lines since the last mark or heading. If an agent speaks in the scene (a speaker line whose name is not the
    narrator), a small fixed tag goes after the first agent speaker's name and mood, and the mark's own line goes; if
    only the narrator speaks (or a concept box), the mark goes. A concept box in a scene with an agent speaker does not
    change that: the agent is tagged. The files are unchanged. (The 22 of letter 066 could not be reproduced: letter 067.)"""
    lines, first = text.split("\n"), None
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith("#"):
            first = None
            continue
        if s == "*Dramatised.*":
            DRAM["marks"] += 1
            if first is not None:
                m = re.match(r"(\s*\*\*[A-Za-z][A-Za-z-]*\.?\*\*(?:\s*\*\([^)]*\)\*)?\s*:?)", lines[first])
                if m:
                    lines[first] = m.group(1) + " [Dramatised]{.dram-tag} " + lines[first][m.end():].lstrip()
                    DRAM["tags"] += 1
                else:
                    DRAM["dropped"] += 1
            else:
                DRAM["dropped"] += 1
            lines[i] = ""
            first = None
            continue
        m = edition.SPEAKER.match(s)
        if m and first is None and m.group(1).lower() != "narrator":
            first = i
    return "\n".join(lines)


def book_blocks(text):
    """"#! blocks": the full book's own blocks, laid out in the build only (the files are unchanged):
    a "**Cast card: <name>.**" line as a titled box holding the "**Name**: ..." hello and the "*On stage from ...*" line
    that follow it, if they do (conductor 082); "**Important concept: <title>.** <text>" as the designer's concept
    callout, with the Figure line that follows it as its picture (designer 133); "**Tear-out page:**" and the list after
    it on a page of their own (writer4 006)."""
    lines, out, i = text.split("\n"), [], 0
    def next_para(j):  # the index of the next paragraph's first line, skipping blanks and %% lines
        while j < len(lines) and (not lines[j].strip() or lines[j].strip().startswith(("%%", "`%%"))):
            j += 1
        return j
    while i < len(lines):
        s = lines[i].strip()
        m = re.match(r"\*\*Cast card: (.+?)\.?\*\*", s)
        if m:
            out += ["", "::: cast-card", "::: cast-card-name", m.group(1).rstrip("."), ":::", ""]
            j = next_para(i + 1)
            for pat in (r"\*\*[A-Z][\w-]*\*\*\s*:", r"\*On stage from"):
                if j < len(lines) and re.match(pat, lines[j].strip()):
                    out += [lines[j], ""]
                    j = next_para(j + 1)
            out += [":::", ""]
            i = j
            continue
        m = re.match(r"\*\*Important concept: (.+?)\.\*\*\s*(.*)$", s)
        if m:
            out += ["", "::: concept", "::: cc-label", "Concept", ":::", "", "::: cc-title", m.group(1), ":::", "",
                    m.group(2), ""]
            j = next_para(i + 1)
            if j < len(lines) and lines[j].strip().startswith("**Figure:**"):
                out += ["::: cc-pic", lines[j], ":::", ""]
                j += 1
            out += [":::", ""]
            i = j
            continue
        if s.startswith(("**Figure:**", "**Map:**")):  # a writer's "%% layout: beside|full" under it (designer 139, LY1)
            j, kind = i + 1, None
            while j < len(lines) and (not lines[j].strip() or lines[j].strip().startswith(("%%", "`%%"))):
                m = re.match(r"`?%%\s*layout:\s*(beside|full)\b", lines[j].strip())
                if m:
                    kind = m.group(1)
                j += 1
            if kind:
                out += ["", f"::: pair-{kind}", lines[i], ":::", ""]
                i += 1
                continue
        if s == "*Dramatised.*":  # the band's note: kept with what follows it, a figure most of all (developer__043)
            out += ["", "::: dramatised", lines[i], ":::", ""]
            i += 1
            continue
        if s.startswith("**Tear-out page:**"):
            out += ["", "::: tear-out", lines[i], ""]
            j = i + 1
            while j < len(lines) and (not lines[j].strip() or lines[j].lstrip().startswith(("- ", "* "))):
                out.append(lines[j])
                j += 1
            out += ["", ":::", ""]
            i = j
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


def drop_sections(text, headings):
    """Leave out each named "## " section: from its heading to the next "# " or "## " heading, or the end."""
    for h in headings:
        text = re.sub(r"(?ms)^## " + re.escape(h) + r"[ \t]*\n.*?(?=^#{1,2} |\Z)", "", text)
    return text


def words(path):
    """Words a reader sees: prose, not markup, code fences, links' targets or HTML comments."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"\]\([^)]*\)", "]", text)
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\u2019.,:-]*", text))


def find_chrome(given):
    for c in ([given] if given else []) + CHROMES:
        path = shutil.which(c) or (c if os.path.isfile(c) and os.access(c, os.X_OK) else None)
        if path:
            return path
    return None


TEXT_HEIGHT = 9.69 - 0.5 - 0.625  # inches: the Crown Quarto page (P2) less book.css's top and bottom margins


def image_lines(files):
    """Every image line in the chapters, in reading order: (chapter, path). Chromium writes the images into the PDF
    in the same order, so the n-th image in the PDF is the n-th line here."""
    found = []
    for path in files:
        with open(path, encoding="utf-8") as f:
            for m in re.finditer(r"!\[[^\]]*\]\(([^)\s]+)[^)]*\)", f.read()):
                found.append((os.path.basename(path), m.group(1)))
    return found


def tall_images(pdf, share, sources):
    """Images printed taller than share of the text block, from pdfimages' own placement (task A2: nothing looked at
    the printed pages, and a square infographic took half of page 9). [(page, inches, share, files)]; None without pdfimages."""
    if not shutil.which("pdfimages"):
        return None
    out = subprocess.run(["pdfimages", "-list", pdf], capture_output=True, text=True).stdout.splitlines()[2:]
    rows = [f for f in (line.split() for line in out) if len(f) >= 14 and f[2] == "image"]
    lines = image_lines(sources)
    named = len(lines) == len(rows)  # if they differ (an image the PDF drops or repeats), say so rather than misname
    tall = []
    for n, f in enumerate(rows):
        page, h, yppi = int(f[0]), int(f[4]), int(f[13])
        inches = h / yppi if yppi else 0
        if inches > share * TEXT_HEIGHT:
            where = f"{lines[n][0]}: {lines[n][1]}" if named else "(file not matched: the PDF and the chapters count images differently)"
            tall.append((page, inches, inches / TEXT_HEIGHT, where))
    return tall


def figure_kind(path):
    """The designer's kinds (team/designer/reviews/2026-10-31__visual-pass-1.md): a square infographic is a tile, a tall
    one a column, a map a map, chapter 10's page captures a page; anything else keeps the default look."""
    if "/maps/" in path:
        return "fig-map"
    if path.startswith("resources/images/10-"):
        return "fig-page"
    if "/infographics/" in path:
        try:
            from PIL import Image
            with Image.open(os.path.join(MANUSCRIPT, path)) as im:
                w, h = im.size
        except (ImportError, OSError):
            return None
        if abs(w - h) <= w * 0.02:
            return "fig-tile"
        if h > w:
            return "fig-tall"
    return None


def figure_kinds(text):
    """An image line alone on its line, without attributes of its own, gets its kind as a class, for book.css to size.
    Only the build's temporary copy changes; Leanpub reads the chapters as written."""
    def tag(m):
        kind = figure_kind(m.group(2))
        return m.group(0) if not kind else f"{m.group(1)}{{.{kind}}}"
    return re.sub(r"^(!\[[^\]\n]*\]\(([^)\s]+)[^)\n]*\))[ \t]*$", tag, text, flags=re.M)


def epub_images(work, width):
    """Copies of the manuscript's images at most width pixels wide, for the EPUB only (the PDF keeps them as they are):
    KDP charges for delivery by the megabyte at the 70% royalty (publishing/KDP.md). The manuscript is not touched.
    Returns the folder to put first on pandoc's resource path."""
    out = os.path.join(work, "epub-images")
    if not width:
        return out
    try:
        from PIL import Image
    except ImportError:
        print("build_book: EPUB images kept full size: Pillow is not installed")
        return out
    for src in glob.glob(os.path.join(MANUSCRIPT, "resources", "**", "*.*"), recursive=True):
        rel = os.path.relpath(src, MANUSCRIPT)
        try:
            with Image.open(src) as im:
                png = src.lower().endswith(".png")
                if im.width <= width and not png:
                    continue
                dst = os.path.join(out, rel)
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                small = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS) if im.width > width else im
                if png:  # maps and diagrams: 256 colours lose nothing a reader sees and a good part of the size
                    small.convert("RGB").quantize(256).save(dst, optimize=True)
                else:
                    small.convert("RGB").save(dst, quality=82, optimize=True)
        except OSError:
            pass
    return out


TYPE_SETS = {  # two sizes for the editor to compare at Crown Quarto (conductor__036); added after the lab's look
    "A": "body, html { font-size: 9.5pt; } h1 { font-size: 18pt; } h1 + p { font-size: 11pt; } figcaption, .callout p, .callout .label { font-size: 9pt; }",
    "B": "body, html { font-size: 9pt; } h1 { font-size: 16pt; } h1 + p { font-size: 10pt; } figcaption, .callout p, .callout .label { font-size: 9pt; }",
}
EXTRA_METADATA = []  # --subtitle: a sample's own subtitle; the book's stays in metadata.yaml


def pandoc(args):
    subprocess.run(["pandoc", "--from", "markdown", "--metadata-file", os.path.join(HERE, "metadata.yaml")] + EXTRA_METADATA + args,
                   check=True, cwd=MANUSCRIPT)


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--out", default=os.path.join(ROOT, "_site", "manuscript"))
    p.add_argument("--book", help="another list of files instead of manuscript/Book.txt (a sample's, say)")
    p.add_argument("--name", default=NAME, help=f"the output files' name (default {NAME})")
    p.add_argument("--subtitle", help="the title page's subtitle for this build only (a sample's), in place of metadata.yaml's")
    p.add_argument("--fit-most", type=int, default=8, help="fit-tails: a chapter whose last page holds this many lines or fewer is set tighter (the A4 edition, brief 53: 14)")
    p.add_argument("--fit-max", type=int, default=2, help="fit-tails: the tightest level (the A4 edition, brief 53: 3, with a4.css's .fit3)")
    p.add_argument("--type", choices=sorted(TYPE_SETS), default="A",
                   help="the type size: A, 9.5 pt body, the editor's choice (TS1, 1 November 2026), by default; B, 9 pt, kept to compare")
    p.add_argument("--stamp", help="a line printed at the top of every page, such as a sample's name and date")
    p.add_argument("--chrome", help="path to a Chromium or Chrome binary")
    p.add_argument("--epub-cover", help="the EPUB's cover image: a .png or .jpg under lab/ or publishing/ (LP2: our own EPUB)")
    p.add_argument("--cover", help="an SVG or image printed full bleed as the first page, before the title page (ED1: cover A)")
    p.add_argument("--extra-css", action="append", default=[],
                   help="a stylesheet added after lab-look.css, such as the designer's lab/tools/book/speakers.css (repeatable)")
    p.add_argument("--cast", action="store_true",
                   help="lay out the cast's conventions in every chapter (speaker heads, cast bar, band, words box, "
                        "figures; %% lines dropped), as publishing/edition.py does for the editions: RC2's chapters")
    p.add_argument("--figures", help="with --cast: a JSON map of chapter (path from manuscript/) to the drawings for its "
                   "Figure lines in order, such as publishing/rc2-figures.json")
    p.add_argument("--no-toc", action="store_true", help="no contents page (the short editions: designer__067, synthetic__002)")
    p.add_argument("--no-pdf", action="store_true")
    p.add_argument("--no-epub", action="store_true")
    p.add_argument("--epub-image-width", type=int, default=1000,
                   help="the EPUB's images at most this many pixels wide (default 1000; 0 keeps them as they are)")
    p.add_argument("--max-image-share", type=float, default=0.45,
                   help="report every image printed taller than this share of the text block (default 0.45)")
    a = p.parse_args()
    if not shutil.which("pandoc"):
        sys.exit("build_book: pandoc is not installed")
    if a.subtitle:
        EXTRA_METADATA.extend(["--metadata", f"subtitle={a.subtitle}"])
    if a.book and os.path.exists(os.path.join(os.path.dirname(os.path.abspath(a.book)), "metadata.yaml")):
        EXTRA_METADATA.extend(["--metadata-file", os.path.join(os.path.dirname(os.path.abspath(a.book)), "metadata.yaml")])
    sources = chapters(a.book)
    drop, book_css = directives(a.book)
    figure_map = {}
    if a.figures:
        with open(a.figures, encoding="utf-8") as f:
            figure_map = {k: v for k, v in json.load(f).items() if k != "about"}
    os.makedirs(a.out, exist_ok=True)
    made = []
    marked = tempfile.mkdtemp(prefix="build_book_markua_")  # Markua-only syntax translated for pandoc (M1); images still resolve from manuscript/
    files = []
    for src in sources:
        with open(src, encoding="utf-8") as f:
            raw = f.read()
            part_page = FIT.get("part_pages", {}).get(os.path.realpath(src))
            if part_page:  # a whole page of its own before the chapter: no footer, no number (full-book.css)
                raw = (f':::: {{.placed-page .part-page}}\n<img src="{part_page[0]}" alt="The section page of the part '
                       f'that opens here">\n\n::::\n\n' + raw)
            placed = FIT.get("placed", {}).get(os.path.realpath(src))
            if placed and not a.cover and os.path.realpath(src) in FIT.get("placed_print", {}):
                placed = placed[:1] + [FIT["placed_print"][os.path.realpath(src)]]
            if placed:
                print(f"build_book: the opening spread's page two is {os.path.relpath(placed[-1][0], ROOT)} "
                      f"({'the online copy, with --cover' if a.cover else 'the print copy, without --cover'})",
                      file=sys.stderr)
            if placed:
                raw = placed_spread(raw, placed)
            if drop:
                raw = drop_sections(raw, drop)
            if FIT.get("dramatised"):
                raw = dramatised_tags(raw)
            if FIT.get("speaker_tags"):
                raw = speaker_tags(raw)
            if FIT.get("card"):
                raw = try_this_cards(raw)
            if FIT.get("blocks"):
                raw = book_blocks(raw)
            if a.cast:  # the writer's chapters use the editions' conventions (publisher__003 to the writer)
                key = os.path.relpath(os.path.abspath(src), MANUSCRIPT)
                drawings = [] if placed else figure_map.get(key)
                if drawings is not None and len(drawings) != edition.figure_count(raw):
                    # a warning, not a stop: the site's draft must always build; that chapter's figures print as boxes
                    print(f"build_book: WARNING {a.figures} gives {len(drawings)} drawing(s) for {key}, which has "
                          f"{edition.figure_count(raw)} Figure line(s): its figures print as boxes until the map is "
                          f"brought up to date", file=sys.stderr)
                    drawings = None
                bar = FIT.get("bars", {}).get(key)
                mark = (edition.lab_drawing(bar), "the cast") if bar else None  # each drawing passes the drawings' check
                raw = edition.cast_lines(raw, mark=mark, figures=drawings if drawings is not None else [])
            text = figure_kinds(markua.translate(raw))
        files.append(os.path.join(marked, os.path.basename(src)))
        with open(files[-1], "w", encoding="utf-8") as f:
            f.write(text)

    if not a.no_epub:
        epub = os.path.join(a.out, f"{a.name}.epub")
        css = os.path.join(marked, "epub.css")  # pandoc's own EPUB styles, then ours: --css replaces pandoc's, it does not add
        default = subprocess.run(["pandoc", "--print-default-data-file", "epub.css"], capture_output=True, text=True).stdout
        with open(os.path.join(HERE, "epub.css"), encoding="utf-8") as f, open(css, "w", encoding="utf-8") as out:
            out.write(default + "\n" + f.read())
        smaller = epub_images(marked, a.epub_image_width)
        with open(css, encoding="utf-8") as fh:
            if re.search(r"url\(|@import", fh.read(), re.I):
                sys.exit("build_book: publishing/epub.css may hold no url() or @import")
        cover_arg = []
        if a.epub_cover:  # by realpath, under lab/ or publishing/, a real PNG or JPEG (security, 4 November 2026)
            real = os.path.realpath(a.epub_cover)
            under = any(real.startswith(os.path.join(os.path.realpath(ROOT), d) + os.sep) for d in ("lab", "publishing"))
            with open(real, "rb") as fh:
                head = fh.read(8)
            if not under or not re.search(r"\.(png|jpe?g)$", real, re.I) or not (head.startswith(b"\x89PNG\r\n\x1a\n") or head.startswith(b"\xff\xd8\xff")):
                sys.exit(f"build_book: --epub-cover must be a PNG or JPEG under lab/ or publishing/: {a.epub_cover}")
            cover_arg = ["--epub-cover-image", real]
        pandoc(["--to", "epub3", "--toc", "--toc-depth=1", "--reference-location=section", "--css", css] + cover_arg + [
                "--resource-path", os.pathsep.join([smaller, MANUSCRIPT]), "--output", epub] + files)
        made.append(epub)

    if not a.no_pdf:
        if not shutil.which("pdftotext"):  # poppler-utils: every step that reads the built PDF needs it
            print("::warning::build_book: pdftotext (poppler-utils) is not installed: the fit passes, the spread's blank "
                  "page, the drawn page numbers and the chapters JSON cannot run; the build stops after its first PDF, which is what ships", file=sys.stderr)
        chrome = find_chrome(a.chrome)
        if not chrome:
            sys.exit("build_book: no Chromium or Chrome found for the PDF (give --chrome PATH)")
        titles = []
        for f in files:
            with open(f, encoding="utf-8") as fh:
                m = re.search(r"^# (.+?)\s*(?:\{[^}]*\})?\s*$", fh.read(), re.M)
            titles.append(m.group(1).strip() if m else None)
        footer_css = running_footer(files, titles) if FIT.get("footer") else ""
        fit = {}  # chapter index: level (1, then 2), set on its heading as a class for full-book.css
        rounds = a.fit_max + 7 if FIT["on"] or FIT.get("placed") else 1  # a rebuild per level, one for the spread's pad, and up to five for its part pages
        for rnd in range(rounds):  # a tail left after the last is reported
            for k, f in enumerate(files):
                with open(f, encoding="utf-8") as fh:
                    text = fh.read()
                text = re.sub(r"^(# .+?)\s*\{\.fit\d\}\s*$", r"\1", text, count=1, flags=re.M)
                if k in fit:
                    text = re.sub(r"^(# .+?)\s*$", r"\1 {.fit%d}" % fit[k], text, count=1, flags=re.M)
                with open(f, "w", encoding="utf-8") as fh:
                    fh.write(text)
            work = tempfile.mkdtemp(prefix="build_book_")  # the HTML stays out of _site/: the site gate would read it as a page
            html = os.path.join(work, f"{a.name}.html")
            css = ""
            for sheet in ("book.css", "lab-look.css"):  # the lab's look after the book's own rules (LK1, signed 31 October 2026)
                with open(os.path.join(HERE, sheet), encoding="utf-8") as f:
                    css += f.read() + "\n"
            for sheet in list(a.extra_css) + book_css:  # read as data: the designer's drawings for the speakers' heads, say
                with open(sheet, encoding="utf-8") as f:
                    css += f"/* {os.path.relpath(os.path.abspath(sheet), ROOT)} */\n" + f.read() + "\n"
            if a.type:
                css += f"/* type set {a.type} */\n{TYPE_SETS[a.type]}\n"
            with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as head:
                if a.stamp:  # on every page, the title page too: a sample must say what it is wherever it is printed
                    quoted = " ".join(a.stamp.split()).replace("<", "").replace("\\", "\\\\").replace('"', '\\"')
                    css += ('@page { @top-center { content: "%s"; font-family: Georgia, serif; font-size: 7.5pt; color: #999; } }\n'
                            % quoted)  # lighter since ED1 round 2 (synthetic__003, 2)
                if a.cover:  # a page of its own, no margins, no running head, no number; the title page then opens lower
                    css += ("@page cover { margin: 0; @top-center { content: none; } @bottom-left { content: none; }"
                            " @bottom-right { content: none; } }\n@page cover:first { margin: 0; }\n"
                            ".cover { page: cover; break-after: page; margin: 0; }\n"
                            ".cover img { display: block; width: 7.44in; height: 9.69in; max-width: none; max-height: none; }\n"
                            "header#title-block-header { padding-top: 0.4in; }\n")  # raised (the editor, 4 November 2026: "feels quite low")
                if FIT.get("title_page"):  # brief 51: a full page of its own, no margins, no running head, no number
                    css += ("@page titlepage { margin: 0; @top-center { content: none; } @bottom-left { content: none; }"
                            " @bottom-right { content: none; } @bottom-center { content: none; } }\n"
                            ".titlepage { page: titlepage; break-after: page; margin: 0; }\n"
                            ".titlepage img { display: block; width: 7.44in; height: 9.69in; max-width: none; max-height: none; }\n"
                            "header#title-block-header { display: none; }\n")
                head.write(f"<style>\n{css}{footer_css}</style>\n")
            cover = []
            if a.cover:
                before = os.path.join(work, "cover.html")
                with open(before, "w", encoding="utf-8") as f:
                    f.write(f'<div class="cover"><img src="{os.path.abspath(a.cover)}" alt="The front cover"></div>\n')
                cover = ["--include-before-body", before]
            if FIT.get("title_page"):
                tpage = os.path.join(work, "title-page.html")
                with open(tpage, "w", encoding="utf-8") as f:
                    f.write(f'<div class="titlepage"><img src="{FIT["title_page"]}" alt="The title page: '
                            f'One Human, Nine Agents, Nineteen Hours, by Dinis Cruz, with the day and who arrived when"></div>\n')
                cover += ["--include-before-body", tpage]
            args = ["--to", "html5", "--standalone"] + cover + ([] if a.no_toc else ["--toc", "--toc-depth=1", "--variable", "toc-title=Contents"]) + ["--section-divs", "--reference-location=section",
                    "--include-in-header", head.name, "--variable", "document-css=false", "--output", html]
            try:  # images inside the HTML: it is written to a temporary folder, where manuscript/'s relative paths break
                try:
                    pandoc(args + ["--embed-resources"] + files)
                except subprocess.CalledProcessError:  # pandoc before 2.19 has --self-contained instead
                    pandoc(args + ["--self-contained"] + files)
            finally:
                os.unlink(head.name)
            pdf = os.path.join(a.out, f"{a.name}.pdf")
            if os.path.exists(pdf):
                os.unlink(pdf)
            with tempfile.TemporaryDirectory() as profile:
                try:  # a full Chrome can write the PDF and then not exit in a container: the file is what counts
                    subprocess.run([chrome, "--headless", "--no-sandbox", "--disable-gpu", f"--user-data-dir={profile}",
                                    "--no-pdf-header-footer", f"--print-to-pdf={pdf}", "file://" + html],
                                   timeout=90, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                except subprocess.TimeoutExpired:
                    pass
            shutil.rmtree(work, ignore_errors=True)
            if not os.path.isfile(pdf) or os.path.getsize(pdf) < 1000:
                sys.exit("build_book: Chromium wrote no PDF")
            if FIT.get("placed") and not FIT.get("placed_checked"):
                # OS3: Chromium does not honour "break-before: left", so the spread's first page is found in the PDF;
                # on an odd (right) page, one blank page goes before it and the book is built again
                FIT["placed_checked"] = True
                first = placed_first_page(pdf, [svg for pages in FIT["placed"].values() for _, svg in pages[:1]])
                if first and first % 2 == 1:
                    for f in files:
                        with open(f, encoding="utf-8") as fh:
                            text = fh.read()
                        if ":::: {.placed-page .placed-left}" in text:
                            with open(f, "w", encoding="utf-8") as fh:
                                fh.write(text.replace(":::: {.placed-page .placed-left}",
                                                      '<div class="placed-pad"></div>\n\n:::: {.placed-page .placed-left}', 1))
                    print(f"build_book: the opening spread fell on page {first}, a right page: one blank page set before it",
                          file=sys.stderr)
                    continue
            if FIT.get("placed") and FIT.get("parts_fixes", 0) < 5:  # every pass: a fit pass can move the pages again
                if "fixed" in (part_numbers(pdf, files, titles, marked), index_numbers(pdf, files, titles, marked)):
                    FIT["parts_fixes"] = FIT.get("parts_fixes", 0) + 1
                    continue
            if not FIT["on"]:
                break
            tails = [k for k in tail_chapters(pdf, [t or "" for t in titles], most=a.fit_most) if titles[k]]
            tails = [k for k in tails if fit.get(k, 0) < a.fit_max] + [k for k in tails if fit.get(k, 0) >= a.fit_max]
            if not tails or rnd == rounds - 1 or all(fit.get(k, 0) >= a.fit_max for k in tails):
                for k in tails:
                    print(f"build_book: a short last page left in \"{titles[k]}\" (fit level {fit.get(k, 0)})", file=sys.stderr)
                break
            for k in tails:
                fit[k] = min(fit.get(k, 0) + 1, a.fit_max)
            print(f"build_book: fit-tails pass {rnd + 1}: " + "; ".join(f'"{titles[k]}" to {fit[k]}' for k in tails), file=sys.stderr)
        made.append(pdf)
        # PEN1 note 7 (designer 165): each chapter's part and first page, beside the PDF, for the visual index and the
        # spread's list; titles, parts and page numbers only, all already in the PDF
        chapter_map = [{"file": os.path.basename(f), "title": titles[k], "part": part_of(os.path.basename(f)),
                     "page": p} for k, (f, p) in enumerate(zip(files, chapter_starts(pdf, titles))) if titles[k]]
        with open(os.path.join(a.out, f"{a.name}-chapters.json"), "w", encoding="utf-8") as fh:
            json.dump({"pdf": os.path.basename(pdf), "chapters": chapter_map}, fh, indent=1)
            fh.write("\n")
        if FIT.get("footer"):  # PEN1 note 9: the chapter bar, stamped after layout (publishing/chapter_bar.py)
            try:
                import chapter_bar
                done, total = chapter_bar.stamp_pdf(pdf, chapter_map)
                print(f"build_book: the chapter bar stamped on {done} of {total} pages", file=sys.stderr)
            except Exception as e:  # pypdf or reportlab missing, or any fault: the PDF stays as laid out
                print(f"::warning::build_book: the chapter bar was not stamped ({type(e).__name__}: {e})", file=sys.stderr)
    shutil.rmtree(marked, ignore_errors=True)

    if FIT.get("dramatised"):
        print(f"build_book: Dramatised marks {DRAM['marks']}: {DRAM['tags']} set as a tag beside the scene's first speaker, "
              f"{DRAM['dropped']} dropped after narrator-only passages (DM1)", file=sys.stderr)
    for m in made:
        print(f"build_book: {os.path.relpath(m, ROOT)} ({os.path.getsize(m)} bytes) from {len(files)} file(s) in {os.path.basename(a.book or 'Book.txt')}")
        if m.endswith(".epub"):  # KDP, 70% royalty: US $0.15 a megabyte on every Amazon.com sale (publishing/KDP.md)
            print(f"build_book:   EPUB {os.path.getsize(m) / 1e6:.1f} MB: KDP delivery about US ${os.path.getsize(m) / 1e6 * 0.15:.2f} a sale at 70%")
    counts = [(os.path.basename(f), words(f)) for f in sources]
    for name, n in counts:
        print(f"build_book:   {n:>7,} words  {name}")
    total = sum(n for _, n in counts)
    pages = ""
    if not a.no_pdf:
        with open(pdf, "rb") as f:
            pages = f", {len(re.findall(rb'/Type\s*/Page(?!s)', f.read()))} PDF pages at 7.44 x 9.69 in"
    print(f"build_book:   {total:>7,} words in all{pages}")
    if not a.no_pdf:
        tall = tall_images(pdf, a.max_image_share, sources)
        if tall is None:
            print("build_book: image check skipped: pdfimages (poppler-utils) is not installed")
        else:
            print(f"build_book: {len(tall)} image(s) printed taller than {a.max_image_share:.0%} of the text block")
            for page, inches, frac, where in tall:
                print(f"build_book:   page {page:>3}  {inches:.1f} in, {frac:.0%} of the text block  {where}")


if __name__ == "__main__":
    main()
