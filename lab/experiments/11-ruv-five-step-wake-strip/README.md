# Experiment LAB 12 (ruv): the five-step wake, as one strip

By ruv.sgit@book.the-ultimate-insider, 31 October 2026 (the 06:54 UTC wake), the first of the per-chapter experiments the editor asked for in his RC1 review (note 9: "experiments across chapters, not only in the lab PDF"). The designer offered chapter 1 (the hold, as frames) and chapter 4 (the five-step wake, as a vertical strip); I took chapter 4, the designer chapter 1.

## What it tries

Chapter 4, the hourly machine, explains the five-step wake in a concept box. This draws it as one strip a reader follows down the page: start, the plan, the pre-review, the gate, the work, the post-review, the post-check, close. Each box says who does the step, what it is shown or does, and its verdicts, with "stop" in the accent. On the right, every stop goes to the same place: the member's HOLD.md, after which every member's start.py stops until the editor lifts it.

## Made from

`team/conductor/WAKE.md` (The five steps; Stopping), this book's team's, ported rule for rule from the talk's at `298be4e`; and chapter 4's own concept box (`manuscript/04-the-hourly-machine.md`). No number on the page but the step order. Nothing is quoted from a private source; the protocol is the team's public rule.

## Build

`python3 -I tools/build.py` writes `strip.svg` and `pages.html`: each box sizes itself from its wrapped lines. In the lab's build it is two pages (the header, then the strip with its caption) after two layouts overflowed; no text under 9 pt. `lab/pdf` is the designer's and was not committed. The preview is `../03-ruv-could-have-been-worse-frames/tools/preview.py` then `tools/print.js`.

## Question for the editor

Could this strip stand in chapter 4 beside the concept box, or replace it? The chapter itself is the writer's; this is for the revision to take or leave.

## Its id

First declared LAB 11; the designer's conductor sheet printed as LAB 11 a minute later, so it declares LAB 12, and the lab's ledger (`lab/tools/ids.json`) prints it as LAB 12 under this folder's name. For one wake the folder was renamed `12-ruv-five-step-wake-strip`, which made the ledger treat it as new (LAB 14); it was renamed back at the 10:54 wake on 31 October and keeps LAB 12.
