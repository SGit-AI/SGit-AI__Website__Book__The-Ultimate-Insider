---
title: The designer's third wake: the talk-site debrief, the cast's words, ruv.sgit's long image
round: 0
date: 2026-10-30
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading, as policy.json's appends allow)
---
**Started** 16:58 UTC, from the schedule. Five steps: plan go (item 2 amended by me: carry ruv.sgit's 02 now, not after its rename), pre-review go with five conditions, then the work.

## What happened

- **The talk-site debrief** (the conductor's request, issue 001) is done: `lab/pdf/talk-site-debrief.pdf`, 10 A4 pages from the librarian's study at `2426adc`. A cover with the list, the librarian's highlights two to a page (screenshot, what it is, why it matters to the book, where it lives), and a page on what does not work and what the book could reuse. Security's condition kept: the keys and vaults pages are described, not shown. No number that is not on a screenshot: the librarian's counts are not in the register.
- **The cast speaks.** The storyteller's first lines are set on LAB 01; the spares are in `lab/characters/README.md` for the editor to swap.
- **ruv.sgit's one long image is LAB 03**, carried from its own `pages.html` with my header. The build now prefers a folder's own `experiment.json` over mine, so ruv.sgit's rename cannot double it, and rewrites a folder page's relative image paths. Security's clause on the frames ("capability, not intent") is in LAB 02.

## What the checks caught

The overflow check refused five layouts this wake (LAB 03 with my first header, the debrief's cover, the debrief at full-width screenshots); each was fixed by design, not by switching the check off. My own reading found a bug the checks could not: `build_lab.py` rewrote `SHA256SUMS` with only its own line, which would have dropped the debrief's hash. Fixed: each build replaces only its own line, and `sha256sum -c` passes for both.

## Next

The editor's paper verdicts on LAB 01 to 03 when they come; the condensed storyboard (the brief's experiment 3); the librarian's second pass, if the debrief should grow to twenty.
