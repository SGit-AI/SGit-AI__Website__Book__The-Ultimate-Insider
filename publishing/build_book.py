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


def pandoc(args):
    subprocess.run(["pandoc", "--from", "markdown", "--metadata-file", os.path.join(HERE, "metadata.yaml")] + args,
                   check=True, cwd=MANUSCRIPT)


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--out", default=os.path.join(ROOT, "_site", "manuscript"))
    p.add_argument("--chrome", help="path to a Chromium or Chrome binary")
    p.add_argument("--no-pdf", action="store_true")
    p.add_argument("--no-epub", action="store_true")
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
            text = markua.translate(f.read())
        files.append(os.path.join(marked, os.path.basename(src)))
        with open(files[-1], "w", encoding="utf-8") as f:
            f.write(text)

    if not a.no_epub:
        epub = os.path.join(a.out, f"{NAME}.epub")
        pandoc(["--to", "epub3", "--toc", "--toc-depth=1", "--output", epub] + files)
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
        args = ["--to", "html5", "--standalone", "--toc", "--toc-depth=1", "--section-divs",
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
    counts = [(os.path.basename(f), words(f)) for f in sources]
    for name, n in counts:
        print(f"build_book:   {n:>7,} words  {name}")
    total = sum(n for _, n in counts)
    pages = ""
    if not a.no_pdf:
        with open(pdf, "rb") as f:
            pages = f", {len(re.findall(rb'/Type\s*/Page(?!s)', f.read()))} PDF pages at 6 x 9 in"
    print(f"build_book:   {total:>7,} words in all{pages}")


if __name__ == "__main__":
    main()
