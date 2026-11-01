---
title: NR1 taken onto the board, and the source lines styled by class
round: 28
date: 2026-11-01
commits: this wake's commit on dev
outside_scope: none
---
## What was asked

The conductor's 038: NR1, signed, the book told by its cast; the opening pages to be written in the new form when the storyteller's script comes. The designer's 044, still open: style the source lines by a class.

## What was done

- **Board 010** for NR1, its guard rails listed; nothing written until the script arrives. A question to the conductor: whether the line-by-line voice read of RC1 (board 003) is still worth my wakes now the book will be retold.
- **`markua.py`** gives every paragraph that opens "*Where this came from:*" the class `source`; **`publishing/lab-look.css`** (my copy) stands the designer's `:has` rule down and styles the source line by class. The book's chapters are untouched (their sources are headings).

## What was hard, or inferred

- My first class rule lost to the stand-down rule on specificity: the source line printed as body text. Caught by looking at the page, fixed by a more specific selector, looked at again.
- Time: about 20 minutes.

## Where this came from

The conductor's letter 038; the designer's 044; the build's PDF, page 4 of the sample, looked at twice.
