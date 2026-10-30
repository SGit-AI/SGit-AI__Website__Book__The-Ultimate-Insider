# Experiment 02 (ruv): the building, in one long image

By ruv.sgit@book.the-ultimate-insider, 30 October 2026, the lab's experiment 2 ("An animation as one long image", `team/conductor/projects/pdf-lab/README.md`), on the same animation as experiment 01 so the editor can compare the two on paper.

## What it tries

The talk's M01 as one image the eye travels down. Experiment 01 froze the animation three times; this one keeps all of it: every person's and every agent's walk is drawn as a line on the building's plan, the people's on the upper plan and the agents' on the lower, with the time and the words that were on screen down a spine on the left. A line turns red where the animation turns its figure red.

## What it is made from

- M01 v1, `src/static/motion/lab/the-building/v1/index.html` in the talk's repository at `5d13d72` (unchanged at `298be4e`), read only from a scratchpad clone.
- Nothing is redrawn by hand. `tools/sample.js` opens M01 in headless Chromium, takes the plan, its labels and the split arrow as M01 draws them at 3 seconds, and then seeks the animation's own clock every 0.1 s from 0 to 43 s, reading each of the 58 figures' place and colour (22 people, then 36 agents, in M01's own order). That is `paths.json`. `tools/build.py` draws `long.svg` from it in the lab's palette, `pages.html` in the lab's format, and a preview `page.html` (the designer's `lab/tools/lab.css` and header, read only) printed to `page.pdf`.
- The counts of figures are the animation's, not the day's: M01's footnote says "A pattern, not a count", and the page keeps it, with security's clause from experiment 01 ("capability, not intent").

## Into the lab PDF

The header is in `experiment.proposed.json`, not `experiment.json`, so `lab/tools/build_lab.py` leaves this experiment out until the designer's verdict; renaming the file is all it needs (one page, `pages.html` in the lab's format, the 9 pt floor kept).

## Questions for the editor, on paper

1. Does one image carry the story that took 43 seconds?
2. Is the lower plan too busy? A version with only the agents' red parts, or with fewer agents drawn, would be calmer.
3. Three frames (01) or one long image (02): which tells it better, or both?

`tools/make.sh <talk clone>` rebuilds everything; `SHA256SUMS` holds the hashes.
