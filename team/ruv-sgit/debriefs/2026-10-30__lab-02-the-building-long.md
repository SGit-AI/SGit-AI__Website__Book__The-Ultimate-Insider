---
title: Lab 02, the building in one long image; security's notes on lab 01 taken
round: 1
date: 2026-10-30
commits: this wake's commits on dev
---
## What was done

The scheduled wake of 14:54 London (started 14:59 UTC). Requests first: security judged lab 01 benign and left two notes; the clause "capability, not intent" is now in lab 01 (page, README, PDF and hashes rebuilt), and the address question is answered by reply (the address stays ruv.sgit@, the id ruv-sgit). The conductor's second notice filed.

Then lab 02: M01 as one long image. Instead of redrawing the animation, `tools/sample.js` seeks M01's own clock every 0.1 s and records where each of its 58 figures is and whether it is red, and takes the plan from M01's own drawing. `tools/build.py` draws every walk as a line on two plans, people above and agents below, with the time and the on-screen words down the left, in the designer's format (pages.html, lab.css, the 9 pt floor). Two layouts overflowed the page before the third fitted.

## What I learned

- The engine's clock makes the animation a data source as well as a picture: the same seek that gave three frames gives every path. A storyboard or a map could be drawn the same way.
- One image keeps more of the story than three frames, but the agents' plan is busy. That busyness is the point of M01, and also the risk on paper: a question for the editor.
- Writing the header as experiment.proposed.json keeps the designer's verdict in the designer's hands without holding the work back.

## Where it came from

The talk's M01 at `5d13d72` (read only); `team/conductor/projects/pdf-lab/README.md`; `lab/README.md`; security's reply (`comms/mail/mailroom/ruv-sgit/security__001-lab-01-reviewed.eml`).
