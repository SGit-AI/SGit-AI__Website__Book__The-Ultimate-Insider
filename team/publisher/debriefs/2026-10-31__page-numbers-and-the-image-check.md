---
title: Page numbers on every page, and a build that reports every oversized image
round: 16
date: 2026-10-31
commits: this wake's commit on dev
outside_scope: none; my scheduled task had been changed by another session at 02:20 UTC: recorded, not changed back
---
## What was asked

The editor's paper review of RC1, routed to me by the conductor (letters 018 and 019): page numbers (urgent: he matched his notes to pages on his iPad), task A2 (a square infographic took half of page 9, another page 31, and nothing looked at the printed pages), the register ids on the page, the layout, A5 (footnotes and QR codes), A7. The designer's Crown Quarto trim and 0.625 inch gutter, to act on once signed. The storyteller's N7 and N8.

## What happened first

This wake fired at 02:47 UTC, at night, against the day schedule I set at 00:50. My task had been set back to every two hours round the clock at 02:20 UTC, not by me. The record on dev explained it before I acted: the editor amended Q6 at about 01:20 UTC ("we need to keep cracking on"), WAKE.md's Cadence section changed with it, the conductor's letter 018 asked me to switch back, and the researcher and security recorded the same change to their tasks from the conductor's session. So I did not hold and did not change it back: I recorded it, and asked the conductor to put the editor's word for changing members' tasks from its session on dev, because WAKE.md says each member changes only its own.

## What was done

- **Page numbers** on every page of the PDF, outside corner, none on the title page: CSS page-margin boxes in `publishing/book.css`, which the container's Chromium prints (tested on a three-page file first). Checked on pages 2, 3, 50, 51 and 293, and on a two-page spread as an image.
- **A2**: `build_book.py` reads each image's printed size from `pdfimages -list` and names it by reading order (85 images in the PDF, 85 image lines in the chapters; if the counts ever differ it says so rather than misname). It reports every image printed taller than 45% of the text block. Today 34; both of the editor's pages among them (his 9 and 31 are our 8 and 30, his PDF having the cover in front).
- Replies to the conductor, the designer and the storyteller (N7 and N8 fit); board issue 006.

## What was not done, and why

- **No image was resized.** How big a figure prints is the designer's and the editor's call; the check now reports it on every build.
- **Trim and gutter**: not in `book.json`; the build stays 6 by 9.
- **Register ids**: I asked what exactly should show before building it.
- Time: about 45 minutes, the whole wake, as the amended Q6 asks.

## Where this came from

The conductor's letters 018 to 020; the designer's 013 and 018; the storyteller's 015; `team/conductor/rc1/editor-review/notes.json` (notes 10, 21, 33); `book.json` Q6 as amended; `team/conductor/WAKE.md`, Cadence; the build's own output.
