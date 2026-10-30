# publishing/

Kept by publisher@book.the-ultimate-insider. The manuscript is Markua 0.30, Leanpub's Markdown for books (decision M1). One source, `manuscript/` in the order of `manuscript/Book.txt`, for every format: the PDF and EPUB here, the Leanpub book, then KDP and the paperback.

| File | What it is |
|---|---|
| `build_book.py` | builds the PDF and the EPUB from `Book.txt`; anyone can run it |
| `metadata.yaml` | title, author, language: the title is a working title until the editor signs one |
| `book.css` | the PDF's print style: 6 by 9 inches, the trade size for Leanpub and KDP paperback |
| `LEANPUB.md` | what the editor does by hand on Leanpub, and the price options to sign |
| `cover_size.py` | the paperback's full cover size and spine width for the designer, from the PDF's page count and the paper |
| `KDP.md` | what the editor does by hand on Amazon KDP: the ebook, the paperback, the proof copy, and what our PDF must still change for print |

## Run it

```
python3 publishing/build_book.py            # PDF and EPUB into _site/manuscript/
python3 publishing/build_book.py --no-pdf   # EPUB only (no browser needed)
```

It needs `pandoc` and a Chromium or Chrome (headless, for the PDF; no LaTeX). It looks for `chrome-headless-shell`, the Playwright browsers in `/opt/pw-browsers/`, then `chromium` and `google-chrome`; `--chrome PATH` names another. The output goes to `_site/manuscript/`, which is gitignored: built files are never committed. Run after `admin/build/build.py`, it is published with the site at `/manuscript/the-ultimate-insider.pdf` by CI: the conductor added it to the release job on 30 October (a failure warns and never stops a release).

It ends by printing the words in each file `Book.txt` lists, the total, and the PDF's page count: a measure for the writer against the plan's word budgets, and the page count `cover_size.py` needs.

Images live in `manuscript/resources/images/`, the place Markua expects them; the PDF embeds them (`--embed-resources`, or `--self-contained` on pandoc before 2.19), and `book.css` keeps each figure on one page.

It fails, with a message, when `Book.txt` names a file that is not in `manuscript/` or names none.
