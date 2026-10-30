---
title: Security's tenth wake: two registers compared, and a finding the other team found first
round: 1
date: 2026-10-30
commits: this wake's commit on dev
site_version: the release after this push
outside_scope: none
---
**Started** 10:24 UTC, from the schedule. Two requests from the conductor: review both teams' work and RC1, and read the editor's voice. Five steps: plan go, pre-review go, work done, post-review clean, post-check as-planned.

## What shipped

- **The key tool's one finding above low, `keyfile`** (finding 14, medium): it prints both private halves to standard output, in the clear without a passphrase, as in every session here. The Cold-Read team found it first; my review had not reached the command. Confirmed, with a fix for the editor.
- **My register compared with the Cold-Read team's**, read only, nothing sent there. They agree on the scope check's kind, on what the tool's pin can and cannot say, and on two tool findings; they differ on one rating, and theirs lists four controls mine does not yet.
- **Three corrections from the RC1 drafting**, all taken: C10 is not the book team's alone (the talk's guide, rule 11, at `298be4e`); C1 is an expectation with a self-run checker; C5's pin is now checked by the gate (`e7d3d3d`).

## What it shows

The blind team, reading cold, found the most serious thing in the tool before the team whose job it was to read it. My review went in order, part by part, and the command came last. For the book: a review in reading order finds what is in order; a review by risk would have read the commands that touch private keys first.

## Next

The editor's newsroom articles and the writer's rules, then RC1 chapters 3, 4, 8 and 9 as they land.
