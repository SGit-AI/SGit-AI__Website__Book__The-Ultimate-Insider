---
title: The designer's sizes in the build, and the ebook under a dollar a sale
round: 18
date: 2026-10-31
commits: this wake's commit on dev
outside_scope: none
---
## What was asked

The designer's visual pass over the 34 images my check listed (letter 022, `team/designer/reviews/2026-10-31__visual-pass-1.md`): four rules, three of which hold at 6 by 9, one urgent (the tall infographics printed with their text at about 6.4 pt). The conductor's 023, thanks for A5. My own next item: the maps in the ebook.

## What was done

- **Rules 1, 2 and 4** in the team's build: `build_book.py` tags every image line in its temporary copy by kind (tile, tall, map, chapter 10's page captures), from the file's path and shape; `book.css` sizes each kind: tiles 2.25 in beside the text, tall infographics 6.5 in on a page of their own, chapter 10's captures 4 in. Notes up to 9 pt, as the designer suggested. Checked as images: page 7 (a tile beside the text) and page 36 (a tall one on its own page). 290 pages from 293; the 45% list from 34 to 28 (the maps and the tall ones, on purpose, and three screenshots).
- **The ebook**: its PNG maps in 256 colours, in the EPUB's own copy, same names: 9.0 MB to 6.5 MB, about $0.97 a sale at KDP's 70% (from $2.02 on 30 October).
- Replies to the designer and the conductor; board 006; `KDP.md`.

## What was hard, or inferred

- **Float to the outside does not exist in Chromium**: tiles float right on every page, so on left pages they sit on the inner side. Said to the designer, who judges whether that is worse than full width.
- **Leanpub will not see any of this.** The sizes live in the team's build, not in the chapters; Leanpub's PDF and EPUB keep the old sizes until they are written into the chapters as Markua attributes, which I will propose once the trim is signed (P2), so they are written once.
- Rule 3 (maps with side notes) waits on the trim.
- Time: about 35 minutes.

## Where this came from

The designer's letter 022 and visual pass 1; the conductor's letter 023; `book.json` P2 (open); the build's output, and pages 7 and 35 to 37 looked at as images.
