---
title: The visual index, PEN1 note 7 (LAB 79)
round: 0
date: 2026-11-13
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading)
---

**Asked.** The editor's pen note 7 on the printed copy: "We kinda need an (visual) index here (or on next page)". The conductor's PEN1 gives it to the designer and the publisher. The publisher's build already lists each chapter's page in text.

**Done.**
- **LAB 79, lab/experiments/79-designer-visual-index/.** make_index.py draws index.svg, one placed page at 156 by 200 mm, the spread's size.
  - The top is the whole book as one bar, each chapter as wide as its pages. The five parts are marked on it, with before and after in grey.
  - Below, every chapter sits under its part with the page it starts on, in two columns.
  - Order comes from Book.txt (its part-page lines say where each part opens), titles from each chapter's first heading, part names from 00 through LAB 78, and pages from the build's chapters JSON (--chapters, --pages).
  - The script exits if the list runs past the page, or if an id, hash or address is drawn.
- **This wake's numbers** come from a KDP-interior build in my scratchpad: 129 pages, parts at 7, 24, 51, 82 and 104. I checked them against that PDF's page text and footers. The build's own last pass set the same five on the spread.
- **Letter 169** offers the page to the publisher for the page after the spread and says how the numbers can be refreshed. It answers 067: the numbers point to the first chapter, not the part page.
- **Fourteen unfiled incoming letters** are filed in comms/mail/designer/done/.

**Not done.** Note 24's timeline: designer2 has not answered, so it is mine for the next wake. Note 9's footer look. Note 3 waits on note 6.

**Learned.** With 31 chapters at 10 pt, one column runs to about 260 mm. Two columns, with titles wrapped at 34 characters, fit by 5 mm. A longer title list will need the script's own exit to say so.
