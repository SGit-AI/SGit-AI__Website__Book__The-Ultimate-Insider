# Experiment LAB 14 (ruv): a dot that becomes the next map

By ruv.sgit@book.the-ultimate-insider, 31 October 2026 (the 10:54 UTC wake), for the editor's RC1 review, theme T10: show a fractal Wardley map, "a dot that becomes the next map", as frames or a sequence (routed by the conductor, `comms/mail/ruv-sgit/done/conductor__005-rc1-review-5-to-9.eml`).

## What it tries

Three frames. 1: RC1's map 5, the day as one value chain, with one dot ringed, "Tools written on the day". 2: the lens, the map faded and that dot opening into a large circle that holds map 6. 3: map 6, the plumbing under the day, whole: what the editor brought, what was written on the day, what was rented. The point a reader should leave with: every part on a map is a map of its own.

## Made from

The illustrator's RC1 map images (`team/conductor/rc1/resources/images/maps/05-the-day-as-a-value-chain.png` and `06-the-plumbing-under-the-day.png`, at `42f0b94`, read only; their sources are the JSON files in `team/conductor/rc1/maps/`). Nothing is added to the maps but the ring and the lens; every word and number on them is the maps' own, under the maps' own rules (`team/conductor/rc1/maps/README.md`).

## Build

`python3 -I tools/build.py` composes the three frames with Pillow and writes `pages.html`; the preview is `../03-ruv-could-have-been-worse-frames/tools/preview.py` then `tools/print.js`. Three pages in the lab's build, no text under 9 pt, no overflow. `lab/pdf` and `lab/tools/ids.json` (which the lab build updates) are the designer's and were restored, not committed.

## Questions for the editor

Does the zoom make a map within a map clear on paper? Three frames, or two (the dot, then the map)?

## 31 October, the 14:54 wake

Frame 1 is printed at 114 mm, the width map 5 was drawn for, so its labels keep their size (the designer's one change, designer__032).
