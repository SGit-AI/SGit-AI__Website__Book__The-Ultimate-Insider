# LAB 41 (ruv): the clock in the margin

By ruv.sgit@book.the-ultimate-insider, 3 November 2026 (the wake of 01:56 UTC), at the editor's word relayed by the conductor (`conductor__015`): "a clock on the right ... maybe hour one, hour two, hour three ... some stats that you can show to give a sense of time passing", with the storyteller's numbering (`storyteller__074`; `chapter-plan/edition-30-outline.md`, "The clock in the margin, and what to show"): hour one is 00:00 to 00:59 on 29 October, and the hold at 18:44 falls in hour nineteen.

## Two forms, for the designer and the publisher to choose

- **Float box** (`edition/clock-01.svg` to `clock-19.svg`, 38 by 30 mm): the hour in words, its clock span, the day's commits hour by hour as nineteen bars with this hour lit, and this hour's commits. The book's outer margin is 9.5 mm, too narrow for stats at 9 pt, so this sits in the text column beside a scene.
- **Edge ladder** (`edition/edge-01.svg` to `edge-19.svg`, 8 by 120 mm): nineteen ticks down the outer margin, this hour lit and named along the edge. It fits the margin and carries no stats.

## What it carries, and what it leaves out

One stat: commits that hour, read at build from C095's "all" row (`claims/talk-commits-by-member-hour.md`); the tool checks the row sums to C095's total and stops if C095 is not checked. Wakes by trigger (C087) are left out because the register gives 05 to 13 UTC (hours six to fourteen) as a range. The cast on stage is left out because C095 counts only commits whose subject starts with a member's name (it would put the conductor's arrival in hour two, where C011 has 00:44) and C011 is open. Both can come in when the register gives them by the hour.

## Chosen, and spans (3 November 2026, the wake of 03:55 UTC)

The designer chose the float box and gave the folder LAB 41 (`designer__098`); the publisher places a writer's "**Clock:** Hour N." line as `clock-NN.svg`, floated right in the column, on clock hours (CK1, `conductor__017`). For the spans the chapters use, `clock-SS-EE.svg` lights the span's hours together and names them in words, with no commit count, since a sum is not in the register.

## The repository growing by the hour (4 November 2026)

At the conductor's 026, for the editor's important concept on the repository (brief 2026-11-04 18), `tools/repo.py` writes `edition/repo-growth.svg`: the talk's repository at the end of each clock hour of 29 October, 00 to 18 (hours one to nineteen on this clock), its files by kind stacked, each bar's total above it. Every value is read from C124 at build, its kinds asserted to add up to its totals. Bytes are registered and not drawn. The caption keeps C124's rule and note: the bars follow dev's first-parent line, so a late-merged branch makes an hour look quieter; hour 00 is the repository at its last commit of that hour, hour 18 the day's last release, after the hold. The strip of folder trees the conductor asked for "if you can" is not drawn: C124 holds no tree.
