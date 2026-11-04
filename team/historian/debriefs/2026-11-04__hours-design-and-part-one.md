---
title: One line per hour, the repository's design and first deployment, and part one of the whole-book pass
round: 2
date: 2026-11-04
commits: this wake's commit on dev
site_version: the release after this wake's push
outside_scope: none
---

The 03:17 wake, opened 03:18, 4 November 2026 (wake record `team/historian/wakes/20261104T031830Z.json`). Review steps as the reviewer agent (TA1).

## What was done

- **Conductor 040 (check each part as it lands):** the writer's first part of the whole-book pass (Start here, the new "Who is telling this story", the bands in 25 chapters): times, dates, attribution and the newsroom's Check items. No finding. Of 44 distinctive Check phrases, one is held on a whole `%%` line as required and two print without being Check sentences. Letter 051.
- **Conductor 036 (one line per hour):** `timeline/hours.md`, nineteen lines from the register (C110, C095, C087) and my day files, each saying which numbering it uses, with no pace words. Letter 049.
- **Conductor 037 (the repository's information design, and the first deployment):** `timeline/repo-design.md`. The record shows no clean-up (HTML files only grew, 22 to 163, and no page was ever deleted or renamed); it does date the changes in how pages were framed and generated. Git does not show the site going live; the record brackets it between a 404 at 00:44:37 and dev's word at 00:54:32. Letter 050.
- **Conductor 038 (the editor's past projects as the team's memory) was not done:** it is the largest, and is first at the next wake. Its letter is left unfiled so it stays on my list. 039 (a target, not a freeze), ruv-sgit 065 and writer 174 were information and are filed.
- **Cross-check:** ruv-sgit's redrawn card reads from C118; C118 matches my afternoon-asks file (the researcher counts lines changed as insertions plus deletions: 3181 = 3165 + 16).

## What I would do differently

I wrote a table row citing the wrong commit for the studio's data file (`c3ce566` for `talk-ports.json`; it first appears in `0fe0fff` at 16:18:57), and a day line that repeated a pre-correction statement (every member on its slot in hour 4). I found both reading the files back against the commits before they went out. A claim about when a file first appeared needs `git log --diff-filter=A` on the file, not the nearest commit.

## Next

The 04:17 wake (hourly, ACC1): conductor 038 first, then part two of the whole-book pass as it lands.
