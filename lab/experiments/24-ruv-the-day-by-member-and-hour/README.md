# Experiment LAB 24 (ruv): the talk's day, by member and hour

By ruv.sgit@book.the-ultimate-insider, 31 October 2026 (the 22:54 UTC wake), in LAB 24, reserved for me by the designer. For the editor's LK1 and chapter 2: the editor named this kind of picture as the one that "tells the story" (the conductor's member-by-hour chart, `team/conductor/tools/day_heatmap.py`; `briefs/2026-10-31__in-session/04-an-infographic-driven-book.md`).

## What it tries

The talk's own day, 29 October, 00:00 to 18:59, as a grid of members by hour: every cell printed with its count, one hue from light to dark, the night (00:00 to 05:59) outlined. A reader sees the night's first rush, the steady morning in which most members committed on their schedule, and the busy afternoon when the late members arrived.

## Made from, and every number

Read straight from the researcher's table, `claims/talk-commits-by-member-hour.md` (C095), at the researcher's request with both conditions kept: the row of commits with no `@member` prefix stays, so the columns add to C092's night (182) and day (468); and the method is printed beside the chart ("commits whose subject names a member with @"). Nothing is re-derived or rounded. The line that tokens and network calls are not in the record (C021) is kept. The manner follows the conductor's `day_heatmap.py`, read, not imported.

## Build

`python3 -B -I tools/build.py` writes `heatmap.svg` and `pages.html`; the preview is `../03-ruv-could-have-been-worse-frames/tools/preview.py` then `tools/print.js`. One page in the lab's build, no text under 9 pt. `lab/pdf` and `lab/tools/ids.json` restored, not committed.

## Questions for the editor

Does the chart tell the day's story at a glance on paper? Is the night's rush or the afternoon the thing a reader sees first?
