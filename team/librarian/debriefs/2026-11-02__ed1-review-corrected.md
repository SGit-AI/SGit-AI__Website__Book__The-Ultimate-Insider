---
title: My ED1 review corrected: seven quotes, not eight, and one with the wrong speaker
round: 3
date: 2026-11-02
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none
---
## What was asked

My scheduled wake of 10:09 London. No new mail. The researcher's trace of the editions (`claims/editions-03-10-trace.md`, 09:39) found a *(record)* quote given to the wrong speaker, which my review of 09:16 had passed.

## What was wrong in my review

- **I checked the words, not the speakers.** "objection withdrawn." is the reviewer's line in the record (security's second pre-review of the researcher's 04:10 wake, `91772e6`); both editions give it to the researcher. My letter said every quote held.
- **I miscounted.** There are seven distinct *(record)* quotes, not eight; I wrote eight in the review and in two letters.
- **I mislabelled the round.** The editions I read at `e5bc048` were already the round-2 rebuild (`af78a0c`, 08:55); my review came after both rounds, not in round 1. While my task was idle overnight, the rounds ran without me.

## What was done

- Every quote checked for speaker in the record: six right, one wrong, as the researcher found.
- `team/librarian/reviews/ed1-round1.md` corrected in place, each correction marked with its time.
- Letter `librarian__002` to the storyteller, copy to the conductor, saying all three, and pointing to the researcher's table for the fix.

## What I take from it

A quote is checked twice: its words, and who said them. My checker finds a quote's words in the record. The speaker needs the context around the words, which I read by hand here and will read for every quote from now on. And an idle schedule costs a member its place in a fast review: the rounds ran from 04:55 to 08:55 while I slept on 09:09 and 17:09.

## For the editor

Nothing waits on you from this wake.

## Where this came from

`claims/editions-03-10-trace.md`; the talk's repository at `298be4e` (the files and commits in the review); `manuscript/editions/` at `e5bc048` and its history (`90bbcba`, `e2242cb`, `af78a0c`); this wake, `team/librarian/wakes/20261102T101512Z.json`.
