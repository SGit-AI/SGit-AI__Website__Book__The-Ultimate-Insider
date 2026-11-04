---
title: The shrink found: the cover and the small type had one cause
round: 67
date: 2026-11-04
commits: this wake's commit on dev
outside_scope: none
---
## What came in
The conductor's 067 (the title page sits low), the designer's 121 (the schedule and chapter 11's two cards), security's 012 (Appendix B may go in), the researcher's 025 copied to me (two changes to 93 first). The conductor's 066 items 2 and 3 were still open.

## What I did
- Looked into the cover not filling page 1. A one-chapter build filled it; the full books did not. Measured word heights: every RC2 PDF was shrunk to about 0.85. Found the cause: the margin clock's note (.clock, mine, from 3 November) hung 26 mm into a 9.5 to 16 mm margin, and Chromium shrinks the whole document to fit overflow.
- Fixed: .clock inside the text column. The cover fills; the body prints at the signed 9.5 pt; the thirty 36, the seventy 72, the full book 133 pages.
- The title raised on the title page (067).
- rc2_map.py after the gate: the designer's three (57 lines drawn).
- 93 held: the researcher asked the writer for two changes first.
- The setup sheet's count-dependent figures updated (the interior 132 pages: $6.31 a copy, the floor at 60% about $10.51).
- Letters: conductor 048 (cc designer), designer 040, writer 031.

## What did not go well
The shrink went unseen for a day: I checked page counts and figures, never the size of a printed word. From now on each build is checked for scale, by word height. I also slipped a comment past a closing bracket in build_book.py, so the first rebuild did not run; caught before anything was committed.

## Next
The pagination pass on full-size pages (four chapter ends spill), with the developer's page map; the type options only if he still finds it small; 93 when the writer has made its changes.
