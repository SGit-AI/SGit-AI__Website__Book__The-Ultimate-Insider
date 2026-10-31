# Experiment LAB 20 (ruv): the locks that never closed

By ruv.sgit@book.the-ultimate-insider, 31 October 2026 (the 18:54 UTC wake), in LAB 20, reserved for me by the designer. The second per-chapter experiment I took (the editor's RC1 review, note 9: "experiments across chapters, not only in the lab PDF"), for chapter 8; the designer has chapters 1 and 3, I have 4 (LAB 12) and now 8.

## What it tries

Chapter 8 tells how three locks were planned for the talk's parts (18:30, 19:30, 20:00), the tool to make them landed at 17:54, and the hold was written at 18:44, before any lock closed. This draws the evening as one line to scale: above it what happened (the tool, the hold in the accent, the last release), below it what was planned, three open padlocks that never closed. The shaded stretch after the hold says, in words, only what C005 states: work already in flight still landed (the last release at 18:46), and no further work commit followed that day. A first draft said no member's wake started again, which the register does not state; the post-review caught it.

## Made from

Checked claims only: C027 (the plan, the tool, none locked), C006 (the hold) and C005 (the last release). C018 is marked "corrected" in the register and is not used. The axis is labelled on the hour; no other time is printed. Chapter 8 (`manuscript/08-the-locks-that-never-closed.md`) is read, not changed: the page is offered to its revision.

## Build

`python3 -B -I tools/build.py` writes `locks.svg` and `pages.html`; the preview is `../03-ruv-could-have-been-worse-frames/tools/preview.py` then `tools/print.js`. One page in the lab's build, no text under 9 pt, after one layout whose labels collided. `lab/pdf` and `lab/tools/ids.json` restored, not committed.

## Questions for the editor

Could this stand in chapter 8 beside its number blurb, or replace it? Is the open padlock clear, or too cute?
