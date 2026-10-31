---
title: The editor's layout notes at 6 by 9: 10 pt type, nothing under 9, fuller margins, 255 pages
round: 19
date: 2026-10-31
commits: this wake's commit on dev
outside_scope: none
---
## What was asked

The editor's paper review (the conductor's letter 018, point 1): the type is too big, there is too much white space, use more of the page with normal margins, decide what the footer carries. The designer's 024 (pages 7 and 36 judged right; tiles stay floating right) and the conductor's 024 (thanks; P2 still open) were notices.

## What was done

- **Type**: body 10 pt from 10.5, the size the designer proposed; and the designer's floor, nothing under 9 pt: captions, call-outs and their labels (the label was 7 pt), code, notes and the page number all raised to 9.
- **Margins**: top 0.55, bottom 0.65 with the folio, outside 0.45 in, all still above KDP's minimums; **the gutter stays 0.75 in**, because the gutter is part of P2, open. The build's text height for the 45% check follows.
- **The footer**: the page number, outside corner. A running chapter title needs CSS string-set, which Chromium does not print; said to the designer and the conductor.
- **The result**: 290 pages to 255; the 45% list 28 to 23; pages 40 and 41 looked at as a spread. `KDP.md`: the page count, the spine at 255 pages (0.640 in on cream) and the margins.
- Letters to the designer (a request to judge it) and the conductor; board 006.

## What was hard, or inferred

- Where the line runs between "the editor asked for it" and "the editor has not signed it": he asked for smaller type and fuller margins in his review, so they are made, in one file, reversible; the trim and gutter he has been asked to sign (P2), so they wait.
- "Normal margins" is my reading, checked against KDP's minimums, not a measured norm: the designer judges it.
- Time: about 25 minutes.

## Where this came from

The conductor's letters 018 and 024; the designer's 013 (point 3) and 024; `book.json` P2 (open); the build's output; `cover_size.py --pages 255`.
