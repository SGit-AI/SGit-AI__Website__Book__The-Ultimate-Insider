---
title: The drawn cast bars; placements restored from the figure briefs; 03b in
round: 75
date: 2026-11-04
commits: this wake's commit on dev
outside_scope: none
---
## What came in
The designer's 135 (the cast bar drawn for 24 chapters; the loops); the developer's 042; ruv-sgit's 069 (a must on 12); writer2's 022, writer4's 007 (92 re-set, 94 narrated) and the writer's 206 (03b; three key QR codes in 03).

## What I did
- "#! cast-bars": the designer's map read from lab/tools/book/ (realpath, .json, directly there), each drawing through lab_drawing; the bar above each chapter's cast-bar line.
- 03b after 03; 92 still held for the researcher's trace.
- Overrides: 12 "the player, first", 03b's heatmap.
- Unplanned, told to the post-check: rc2_map.py reads a blank slot's path from its own "%% figure brief" line (never one already placed or named by two briefs). The writers had moved paths there, and eight placements had silently gone back to boxes, chapter 1's two screenshots among them; seven are back (the eighth was a wrong pick, refused by the new rule).
- Letters: conductor 056, designer 048, ruv-sgit 020, writer 036, writer2 005, writer4 005.

## What did not go well
Moving the paths off the Figure lines dropped drawings without any warning from the build. The map should have warned when a placed drawing disappeared; for now the briefs carry them.

## Next
The three key QRs, 03b's and 94's figures when drawn; 92 when traced; RV2 part two.

Post-check notes: the brief fill takes the first path a brief names, so a brief that names a path to reject it would place it (writers to keep rejected paths off brief lines, or the designer's list to fill the slot); two letters said "the build" where rc2_map.py reads the briefs.
