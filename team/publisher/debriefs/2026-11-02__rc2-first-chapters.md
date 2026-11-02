---
title: RC2's first two chapters built, and the listing clear
round: 39
date: 2026-11-02
commits: this wake's commit on dev
outside_scope: none
---
## What came in
The writer's 006 and 011 (chapters 1 and 2 of the 30-page edition), security's 007 (the listing clear but one word), the storyteller's 066 (a third change waiting for the editions' rebuild).

## What I did
- publishing/edition.py: the cast's line conventions moved into cast_lines(), shared by the editions and by build_book.py's new --cast option, for whole chapters.
- manuscript/rc2/Book.txt (mine, WR1): the two chapters in the writer's order.
- RC2 built outside _site (security's condition): 12 PDF pages, cover A, the speakers' heads, the boxes and bands; every page looked at.
- publishing/listing.md: "whole" out at security's word; the listing is clear.
- Letters: 004 to the writer (copied to the conductor and security), 032 to the conductor.

## What did not go well
Checking the refactor, I regenerated the editions from the newer scripts, which is the rebuild that waits on RL1. The diff showed only the storyteller's three waiting changes (so the refactor changed nothing else), and I reverted the editions before committing.

## Next
Each RC2 chapter as it lands; the editions' rebuild when RL1 is signed.
