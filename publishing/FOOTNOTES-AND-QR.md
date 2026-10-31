# Footnotes and QR codes: in Markua, in the team's build, on paper (task A5)

Kept by publisher@book.the-ultimate-insider, 31 October 2026, about 05:10 UTC, for the designer and the conductor (the editor's paper review of RC1, task A5). It says what works today; how the book uses either is the editor's and the designer's call.

## Footnotes and endnotes

**In Markua** (markua.com, section 11.20): a footnote is `text[^name]` with its definition `[^name]: The note.` anywhere later in the chapter; an endnote has two carets, `text[^^name]` and `[^^name]: The note.` A note's further paragraphs are indented four spaces. Each note is referenced once. Markua leaves where notes appear to the processor: "Markua does not specify how footnotes are output". Leanpub's own build decides for the official PDF and EPUB; the first Leanpub preview will show where.

**In the team's build** (`publishing/build_book.py`), since this wake: pandoc reads both forms as they are, and `--reference-location=section` prints every note at the end of its chapter, in the PDF and the EPUB, numbered through the book. Smaller type and a short rule above them (`book.css`). **A note cannot sit at the foot of its own page in our PDF**: Chromium, which prints it, has no footnote placement. If the editor wants true page-foot notes, that is Leanpub's PDF or a different print engine, not a CSS change.

**For the book**: the editor's review moves the provenance ("Where this came from") toward the augmented online version (note 14). Notes at chapter end suit short asides; a source the reader should be able to open belongs in a QR code or a link, below.

## QR codes

**Making them**: reportlab, already installed, has a QR generator; nothing is downloaded. `python3 publishing/qr_test.py` prints a test sheet (`_site/manuscript/qr-test.pdf`, 6 by 9 inches) with two addresses at 10, 12, 15, 20 and 25 mm, each including its quiet margin:

| Address | Characters | Modules across | Module at 15 mm | at 20 mm |
|---|---|---|---|---|
| A commit page on GitHub (`github.com/SGit-AI/.../commit/298be4e`) | 94 | 37 | 0.33 mm | 0.44 mm |
| A short address on the book's site (`the-ultimate-insider.book.sgit.ai/r/C010`, illustrative) | 48 | 29 | 0.41 mm | 0.54 mm |

The shorter the address, the fewer modules, the larger each one at the same printed size, and the easier the code reads. **A short address on the book's own site is the better target**: smaller codes, and it can be redirected if the record ever moves (the question in card 11, `team/publisher/rc1-cards.md`).

**The smallest a phone reads: not measured yet.** The container has no QR reader and no camera; Chromium here has no barcode detector. The sheet has to be printed at 100% and scanned with a phone: the smallest size in each row that opens the page is the answer. That is a two-minute test for the editor or the designer on any printer, and the proof copy settles it for KDP's paper.

**In Markua**: a QR code is an image like any other, `![what it opens](resources/images/qr/C010.svg)` or a PNG; Markua needs nothing special. Generated codes would be made by a build step from a list of addresses, never by hand, so each one is checked against its address on every build.
