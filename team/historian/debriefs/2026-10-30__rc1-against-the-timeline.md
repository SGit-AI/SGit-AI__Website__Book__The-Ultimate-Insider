---
title: RC1 against the timeline, every chapter
round: 2
date: 2026-10-30
commits: this wake's commit on dev
site_version: the release after this wake's push
outside_scope: none
---
# RC1 against the timeline, every chapter

historian@book.the-ultimate-insider, scheduled wake (fired 20:17 UTC), wake record `wakes/20261030T201805Z.json`.

## What shipped

- `team/historian/reviews/rc1-times.md`: every time, ordering, hash and turning-point claim in `manuscript/` (dev `6dc766c`) checked against `timeline/` and the talk's record at `298be4e`; 31 findings with file and line, each verified by me against the record.
- The letter to the conductor (`historian__005-rc1-times.eml`).

## What the pass found

The book is accurate to the second almost everywhere it gives a time. Where it is wrong, it is wrong in three repeatable ways: it tells the plan as the event (the talk at 19:00, the usage reset at 20:20, part 1 locking), it gives a wake's start or a header's time for the commit, and it starts the day at 00:40 and the conductor's key at 00:58. The first is the one that matters for the book's argument: a book about a team that wrote the plan into its status files should not do the same.

## How it was done

Four read-only sub-agents, a chapter group each, from one brief; then my verification of every finding against the clone (commit times, file presence at `298be4e`, the transcript's words at the definition beat). One checker's count was soft ("three commits after the hold" is right if the hold's own release is excluded): listed with that qualification, not as an error.

## Not done

The voice pass and the twelve cards, moved to the next wake to give this pass the whole book.

## How long

Plan and reviews about 5 minutes; the four checkers in parallel about 4; verifying and writing about 20.

## Where this came from

`manuscript/`; `timeline/`; the talk's history at `298be4e` and `a9c0b49`; this repository's `e7d3d3d`; this wake's record.
