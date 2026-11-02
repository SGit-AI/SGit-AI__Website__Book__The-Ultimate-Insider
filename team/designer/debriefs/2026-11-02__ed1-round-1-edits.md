---
title: ED1 round 1 edits, the cast on the editions' pages, and cover A on the signed title
round: 0
date: 2026-11-02
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (the manuscript read only; builds on scratch copies; REALITY.md under its own heading)
---
**Started** 07:01 UTC, from the schedule. Five steps: plan go, pre-review go with conditions (one, that letters be "marked synthetic", read as a slip and recorded so), the gate, the work.

## What happened

- **The cast on the page**: `lab/characters/editions.py` reads each edition page's cast-bar line and writes a marker (narrator first, then the nine in arrival order, the present lit). Where the words give a time, the set comes from C011's first commits, and the script stops if the count the words give disagrees (it did not: six before five in the morning). And `lab/tools/book/speakers.css`, a 6 mm head before each speaker block, by the publisher's new data-speaker and data-mood; tested on a scratch build of the 10-page edition with no change in page count.
- **Cover A on the signed title**: GEN ZX FOUNDERS with the ZX large, the title stacked, the subtitle, the ring, and four diagonal stripes in the Spectrum's colours drawn from the description. In LAB 33 (the lab PDF is 93 pages) and to the publisher for the editions.

## Next

Round 2: the drawings for the dashed figures (the factory's stations first), the four scorecards, the numbered steps; then CV2. MN1 still waits on the researcher.
