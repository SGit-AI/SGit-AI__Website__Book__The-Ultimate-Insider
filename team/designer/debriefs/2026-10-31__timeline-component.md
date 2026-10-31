---
title: The RC1 review taken; the first component, the timeline
round: 0
date: 2026-10-31
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading, as policy.json's appends allow)
---
**Started** 02:57 UTC, from the schedule. Five steps: plan go, pre-review go with conditions, then the work.

## What happened

- **The editor's RC1 review, relayed by the conductor**, is all on my board: issues 010 to 016 (visuals big and in the chapters, a visual pass over every printed page, footnotes and QR codes, the component toolkit, the conductor in detail, images that belong, the tour's visuals). Pace: my task already runs every two hours round the clock, which is Q6 as amended; nothing changed. I missed four of the letters at first because I listed only the newest; the plan step's sub-agent named them.
- **A12's first component**: `lab/tools/components/timeline.py`, JSON in, SVG out, horizontal and vertical, to scale with gaps over a threshold drawn as a marked break, labels stacked where they would collide, one accent. Example page LAB 09, from seven registered times. The lab build places it with one line.
- **LAB 07**: filled now, but held again: my own gutter change (167 mm to 164 mm) came after ruv.sgit's layout, and its fixed grid runs 3.4 mm past. Said so, and how to fit any width.

## What I caught by eye

The first horizontal timeline had a second break where the afternoon should be to scale (the threshold was too low), and labels pushed off the right edge pulled their leaders across other labels. Fixed: a six-hour threshold, labels to the left of their point near the edge, leaders always vertical.

## Next

The visual pass over the publisher's 34 oversized images (issue 011); the conductor in detail (014); the next components (013).
