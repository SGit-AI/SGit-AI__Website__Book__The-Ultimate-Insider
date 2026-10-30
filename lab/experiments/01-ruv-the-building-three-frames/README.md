# Experiment 01 (ruv): the building, in three frames

By ruv.sgit@book.the-ultimate-insider, 30 October 2026, the first run of the PDF lab (`team/conductor/projects/pdf-lab/README.md`, experiment 1: "An animation as three frames").

## What it tries

The talk's animation M01, "the building", told on paper in three stills, with the time in the beat and the words that were on screen under each. Nothing is redrawn: each still is the animation itself, frozen on its own clock, so the page shows exactly what the room saw at that second.

## What it is made from

- M01 v1: `src/static/motion/lab/the-building/v1/index.html` in SGit-AI__Website__Presentation__The-Ultimate-Insider, read-only, cloned into the session's scratchpad. Last changed at `5d13d72` (29 October 2026, 18:29 UTC, "people sometimes find the gold, agents keep going"); identical at `298be4e`, the end of the record, and at `424b67a`, the clone's head.
- The talk's slide engine (`src/static/talk/engine/slide.js`, `slide.css`, unchanged since `23739cc` and `5a91607`), whose `?t=` freezes a slide at a time and `?theme=light` gives the print colours.

## How it was made

`tools/make.sh <talk clone>` runs `tools/capture.js` (Chromium, 1280 by 720 at twice the pixels, `?t=22.5`, `?t=30`, `?t=43`, light theme) and then `tools/print.js` (A4, the page's own margins) on `page.html`. `SHA256SUMS` holds the hashes of the PDF and the frames.

Why these three times: the animation has four stops (`RUV_STEPS`: 0, 5, 23 and 37 seconds) and four headlines. Frame 1 is the last moment of the people's headline, when they have all stopped; frame 2 is the agents' headline while they are still arriving; frame 3 is the end, with the footnote. The opening (the empty plan and the split) is the one stop left out: frame 1 already shows the plan.

## The numbers on the page

Only the animation's own clock (its `data-end="43"` and the three seek times) and none from the day. The animation says of its figures: "A pattern, not a count", and the page keeps that line. After security's review (30 October, 14:40 UTC) the legend adds "Red shows capability, not intent: the talk's agents were a benign team", so a reader without the talk does not take red for the agents' intent.

## Questions for the editor, on paper

1. Does the story survive without the motion? Keep, change, or drop.
2. The words are printed twice (in the frame, and beside it in larger type). Keep both, or crop the headline out of the frames?
3. Is the opening (one way in, the corridor that splits) missed? A fourth, small frame would fit.

## What is next

The same animation as one long image (lab experiment 2), and the other two animations (`could-have-been-worse`, `meet-the-team`) as three frames. The page's type and grid are a placeholder until the designer's.
