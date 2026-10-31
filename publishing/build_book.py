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
import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile

import markua

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANUSCRIPT = os.path.join(ROOT, "manuscript")
HERE = os.path.join(ROOT, "publishing")
NAME = "the-ultimate-insider"
CHROMES = (["chrome-headless-shell"] + sorted(glob.glob("/opt/pw-browsers/chromium_headless_shell-*/*/chrome-headless-shell"))
           + ["chromium", "chromium-browser", "google-chrome", "google-chrome-stable", "/opt/pw-browsers/chromium"])


def chapters():
    """The files Book.txt lists, in its order; blank lines and # comments skipped."""
    with open(os.path.join(MANUSCRIPT, "Book.txt"), encoding="utf-8") as f:
        names = [line.strip() for line in f if line.strip() and not line.lstrip().startswith("#")]
    missing = [n for n in names if not os.path.isfile(os.path.join(MANUSCRIPT, n))]
    if missing:
        sys.exit(f"build_book: Book.txt lists files not in manuscript/: {', '.join(missing)}")
    if not names:
        sys.exit("build_book: Book.txt lists no files")
    return [os.path.join(MANUSCRIPT, n) for n in names]


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


TEXT_HEIGHT = 9 - 0.55 - 0.65  # inches: the 6 by 9 page less book.css's top and bottom margins


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


def pandoc(args):
    subprocess.run(["pandoc", "--from", "markdown", "--metadata-file", os.path.join(HERE, "metadata.yaml")] + args,
                   check=True, cwd=MANUSCRIPT)


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--out", default=os.path.join(ROOT, "_site", "manuscript"))
    p.add_argument("--chrome", help="path to a Chromium or Chrome binary")
    p.add_argument("--no-pdf", action="store_true")
    p.add_argument("--no-epub", action="store_true")
    p.add_argument("--epub-image-width", type=int, default=1000,
                   help="the EPUB's images at most this many pixels wide (default 1000; 0 keeps them as they are)")
    p.add_argument("--max-image-share", type=float, default=0.45,
                   help="report every image printed taller than this share of the text block (default 0.45)")
    a = p.parse_args()
    if not shutil.which("pandoc"):
        sys.exit("build_book: pandoc is not installed")
    sources = chapters()
    os.makedirs(a.out, exist_ok=True)
    made = []
    marked = tempfile.mkdtemp(prefix="build_book_markua_")  # Markua-only syntax translated for pandoc (M1); images still resolve from manuscript/
    files = []
    for src in sources:
        with open(src, encoding="utf-8") as f:
            text = figure_kinds(markua.translate(f.read()))
        files.append(os.path.join(marked, os.path.basename(src)))
        with open(files[-1], "w", encoding="utf-8") as f:
            f.write(text)

    if not a.no_epub:
        epub = os.path.join(a.out, f"{NAME}.epub")
        css = os.path.join(marked, "epub.css")  # pandoc's own EPUB styles, then ours: --css replaces pandoc's, it does not add
        default = subprocess.run(["pandoc", "--print-default-data-file", "epub.css"], capture_output=True, text=True).stdout
        with open(os.path.join(HERE, "epub.css"), encoding="utf-8") as f, open(css, "w", encoding="utf-8") as out:
            out.write(default + "\n" + f.read())
        smaller = epub_images(marked, a.epub_image_width)
        pandoc(["--to", "epub3", "--toc", "--toc-depth=1", "--reference-location=section", "--css", css,
                "--resource-path", os.pathsep.join([smaller, MANUSCRIPT]), "--output", epub] + files)
        made.append(epub)

    if not a.no_pdf:
        chrome = find_chrome(a.chrome)
        if not chrome:
            sys.exit("build_book: no Chromium or Chrome found for the PDF (give --chrome PATH)")
        work = tempfile.mkdtemp(prefix="build_book_")  # the HTML stays out of _site/: the site gate would read it as a page
        html = os.path.join(work, f"{NAME}.html")
        with open(os.path.join(HERE, "book.css"), encoding="utf-8") as f:
            css = f.read()
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as head:
            head.write(f"<style>\n{css}</style>\n")
        args = ["--to", "html5", "--standalone", "--toc", "--toc-depth=1", "--section-divs", "--reference-location=section",
                "--include-in-header", head.name, "--variable", "document-css=false", "--output", html]
        try:  # images inside the HTML: it is written to a temporary folder, where manuscript/'s relative paths break
            try:
                pandoc(args + ["--embed-resources"] + files)
            except subprocess.CalledProcessError:  # pandoc before 2.19 has --self-contained instead
                pandoc(args + ["--self-contained"] + files)
        finally:
            os.unlink(head.name)
        pdf = os.path.join(a.out, f"{NAME}.pdf")
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
        made.append(pdf)
    shutil.rmtree(marked, ignore_errors=True)

    for m in made:
        print(f"build_book: {os.path.relpath(m, ROOT)} ({os.path.getsize(m)} bytes) from {len(files)} file(s) in Book.txt")
        if m.endswith(".epub"):  # KDP, 70% royalty: US $0.15 a megabyte on every Amazon.com sale (publishing/KDP.md)
            print(f"build_book:   EPUB {os.path.getsize(m) / 1e6:.1f} MB: KDP delivery about US ${os.path.getsize(m) / 1e6 * 0.15:.2f} a sale at 70%")
    counts = [(os.path.basename(f), words(f)) for f in sources]
    for name, n in counts:
        print(f"build_book:   {n:>7,} words  {name}")
    total = sum(n for _, n in counts)
    pages = ""
    if not a.no_pdf:
        with open(pdf, "rb") as f:
            pages = f", {len(re.findall(rb'/Type\s*/Page(?!s)', f.read()))} PDF pages at 6 x 9 in"
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
