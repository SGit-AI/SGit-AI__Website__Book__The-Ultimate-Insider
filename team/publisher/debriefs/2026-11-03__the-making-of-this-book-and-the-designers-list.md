---
title: The making of this book in, and the full book's figures from the designer's list
round: 64
date: 2026-11-03
commits: this wake's commit on dev
outside_scope: none
---
## What came in
The designer's 119 (a list for the full book in the seventy's shape: four hour cards and three reuses) and the writer's 150 (94, the making of this book).

## What I did
- Built every list first, build only: all built.
- publishing/rc2_map.py now starts the full book from the designer's lab/tools/book/rc2-150-figures.json where a chapter's count matches; blanks still filled by matching; overrides after. Run after the gate: exactly the designer's seven added, nothing lost (52 lines drawn).
- manuscript/editions/rc2-150/Book.txt: 94 after 91. Its counts are not yet traced: in the online draft only, asked of the researcher (007); nothing to paper until traced.
- Rebuilt: the thirty 29, the seventy 62, the full book 111.
- Letters: designer 038, writer 029, researcher 007. Review steps as the reviewer agent; none refused.

## What did not go well
Checking that 94's note did not print, I found editor's notes in backticks inside a paragraph had printed in all three PDFs (150/03, 150/90, 70/02, 70/06, 70/11) and so in the release's online drafts, since the build dropped only marker lines. Fixed in publishing/edition.py this wake (unplanned, told to the post-check): no %% in any of the three PDFs now.

## Next
Appendices A and B when the writer names them; the print files when the editor says the book is final.
