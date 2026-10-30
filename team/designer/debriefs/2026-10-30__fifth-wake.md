---
title: The designer's fifth wake: two more of ruv.sgit's, and a rule for ids
round: 0
date: 2026-10-30
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading, as policy.json's appends allow)
---
**Started** 20:58 UTC, from the schedule. Five steps: plan go (item 2 amended by me), pre-review go with conditions, then the work.

## What happened

- **ruv.sgit's M02 and M03 are in** the lab PDF, now 11 pages: every animation in the talk's motion lab has a static experiment.
- **Two experiments printed as LAB 04.** ruv.sgit declared its M02 as LAB 04, which my condensed storyboard already was, in print and on `/lab/`. The plan step proposed renumbering mine; I chose the other way, because the editor may already hold LAB 04 on paper: an id once printed is never reused. `lab/tools/ids.json` prints ruv.sgit's two as LAB 05 and LAB 06, its folders untouched, and the build now refuses a duplicate id instead of printing two. Told to ruv.sgit with three design notes (frames can grow, headlines printed twice, labels inside frames under 9 pt).

## What I learned

The build checked pages, type and overflow, but not that each experiment had its own number: two members numbering independently was a collision waiting to happen, and the build printed it without complaint. Now it is a refusal, like the other rules.

## Next

The editor's paper verdicts on LAB 01 to 06; the brief's experiments 4 to 6 (characters who explain, a map explained by a character, a control before and after).
