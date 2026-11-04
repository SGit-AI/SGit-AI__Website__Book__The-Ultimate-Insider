---
title: RV2, the reader tests on three sections of the full book
round: 0
date: 2026-11-04
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none
---

synthetic@book.the-ultimate-insider, the 05:42 scheduled wake, 4 November 2026, on Sonnet 5.5.

## What shipped

- conductor__036 (RV2): the three named readers each read 00-start-here, 00b and 10-talking-through-git of the full book at `f53c6e5a`, against principles 1, 6, 7 and 21. `review/synthetic/sections/`: each reader's file and the merged `findings.md`, every finding mapped to file and line with its principle and a severity (must, should, could).
- Every cited line and quote checked against the files by script: 46 of 47 matched where cited; one line number corrected (the newsroom builder's step 4 finding is at line 12, not 4).
- Requests to writer (synthetic__006) and writer2 (synthetic__001); a letter to the conductor with the grid (synthetic__018): none of the three passes yet.

## What it found

No section has a must open for two readers; the first-build finisher's three musts are the same three words used before they are explained (board and hold, repository, git), which the other two readers rate should. The recurring principle hits: 21 (a scene told in full twice, chapter 10), 7 (runs of short fragments, chapter 10), 6 (how-to-read directions in 00 and 00b). One reader holds a line another flags: "If you only read one page, read this one."

## What I did not do

The whole-book read (conductor__034) waits on the publisher. Nothing is called signed: that is the editor's (SO1).
