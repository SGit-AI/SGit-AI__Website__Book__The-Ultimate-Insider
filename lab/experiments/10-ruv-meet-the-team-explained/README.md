# Experiment LAB 10 (ruv): meet the team, explained

By ruv.sgit@book.the-ultimate-insider, 31 October 2026 (the 02:54 UTC wake), for the editor's RC1 paper review, note 8 (theme T4): page 8 of RC1 is "Motion's 'Meet the team' animation ... (one still)", and the editor wrote that it is "a super powerful slide and animation that needs explaining: more frames, and the format explained; perhaps a different infographic" (`team/conductor/rc1/editor-review/notes.json`; his words in `briefs/2026-10-31__rc1-paper-review/`).

## What it tries

The different infographic: not a frame of the animation but the animation's idea drawn again, big, as an hour dial. The nine members sit at the minute past the hour each one wakes, the editor at the centre, and three numbered call-outs point at what to read. The second page explains it in five points and gives the team's counts at 17:02 beside the four things that kept it in step. LAB 06 (three frames of M03) is the other way of telling it; the editor can compare the two.

## Made from, and every number

Drawn by `tools/build.py` from `claims/register.json` only: C071 (each member's minute), C073 (the six counts as at 17:02:26 on 29 October; "510 commits, CI's releases among them" and the 17:02 label as the researcher asked for LAB 06) and C024 (the day's one hold, 18:44). The role words and the four things that keep the team in step are M03's own (`src/static/motion/lab/meet-the-team/v1/index.html` at `f45028c`, read only). The "ruv-sgit" on the dial is the talk's member of that name.

## Build

`python3 -I tools/build.py` writes `dial.svg` and `pages.html`; the preview is `../03-ruv-could-have-been-worse-frames/tools/preview.py` then `tools/print.js`. In the lab's build it is two pages at Crown Quarto (the header and the dial on one, the explanation on the next) after two sizes that pushed the dial off the header's page; no text under 9 pt, no overflow. `lab/pdf` is the designer's and was not committed.

## Questions for the editor

Does the dial, explained, carry what the animation did? Should page 8 of the book use it instead of the still?

## Its id

First declared LAB 09; the designer's timeline (`lab/experiments/09-designer-timeline/`) took LAB 09 a minute later and was printed with it, and the lab build refuses two experiments with one id, so this folder became `10-ruv-meet-the-team-explained` and LAB 10 at the 04:54 wake on 31 October. The designer owns the numbering.
