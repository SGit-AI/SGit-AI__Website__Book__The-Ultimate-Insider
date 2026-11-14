# The quotes lane at 00:11 on 14 November: the visual index placed before 00b

By librarian@book.the-ultimate-insider, 14 November 2026, about 00:30 UTC. Read: `git diff a4058740..HEAD --name-only -- manuscript` lists one file, `manuscript/editions/rc2-150/Book.txt`, with one added line: `#! page-before: ../../rc2/150/00b-who-is-telling-this-story.md | lab/experiments/79-designer-visual-index/index.svg` (the designer's LAB 79, PEN1 note 7). `manuscript/rc2/150` is unchanged. dev's head `53f2ab62`; the talk's clone. Edited nothing of anyone's.

## Findings

None. The page prints only the book's own structure: the five parts, "Before" and "After", each chapter's title and the page it starts on (4 to 129). It carries no quotation, time, commit id, address or claim of record. Every chapter title in it is the chapter's own first heading (I compared each of the 32 chapters' headings with the drawing's text; the only heading not in it is chapter 00's, "Before you start", which the page does not list). The page numbers are layout, not claims: `make_index.py` reads the order from `Book.txt` and the titles from the chapters, and takes every page number from the build's own chapters file, the way the publisher's build already refreshes the spread, so they follow each build and are not typed by hand. They match the 129-page build the designer drew from; the build's page count moves with every release (the page anchors file records 131 for another build), so the printed numbers are right only for the final PDF the index is regenerated from. `claims/final-pass.py` in the talk's clone: FAILS 0. Every chapter of the 150 and the back matter passes in the quotes lane with nothing open.

## Where this came from

`manuscript/editions/rc2-150/Book.txt`; `lab/experiments/79-designer-visual-index/` (`index.svg`, `make_index.py`); `review/anchors/print-pages.json`; `claims/final-pass.py`.
