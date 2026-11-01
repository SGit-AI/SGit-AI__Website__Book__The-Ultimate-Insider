---
title: Crown Quarto A and B, the page 7 note, LAB 23 and 24 in
round: 0
date: 2026-11-01
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (the publisher's build run on scratch copies; REALITY.md under its own heading)
---
**Started** 00:57 UTC, from the schedule. Five steps: plan (amended to three items), pre-review go with conditions, the gate, the work.

## What happened

- **A and B for the editor** (P2 signed): `lab/tools/book/compare_types.py` runs the publisher's own build with `--type A` and `--type B` on a scratch copy; `lab/pdf/sample-lab-look-A.pdf` and `-B.pdf`, 13 pages each at Crown Quarto. A body line runs about 95 characters in A, 100 in B: both long for the 164 mm block.
- **Page 7** (text in drawings bigger than the body): the cause was mine. The drawings were made at 120 mm with 9 pt labels; my fragment's `figure img { width: 100% }` stretched them to 164 mm, so the labels printed near 12 pt. And my `.svg` selector never matched, because the build embeds images as `data:` URIs. Fixed at the root: the SVGs state their size, the fragment leaves a sized SVG at its size, and the loop's words came down from 13 pt to 9. Checked on page 7: the labels print at about the body's size. A rule in `lab/README.md`. The comparison PDFs carry the fix on the copy until the publisher takes it (`designer__046`).
- **LAB 23 and 24 in**, both kept, with notes to ruv-sgit; LAB 25 and 26 reserved for it. The lab PDF is 63 pages.
- **CH1 and NR1**: issue 020 opened; the personalities and scorecard categories asked of the storyteller. The model-sheet plan, a stretch item, did not fit this wake.

## Lesson

A preview I built with my own fragment showed the bug and I did not see it: I checked the tile, not the drawings' text size. Next time measure text in drawings on the printed page (pdftotext -bbox), not only in the SVG.

## Next

The model sheets, starting with the conductor; mapnotes for chapters 11 and 11b; judge the publisher's next build.
