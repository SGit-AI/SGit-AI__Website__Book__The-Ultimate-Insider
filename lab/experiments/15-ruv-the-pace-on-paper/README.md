# Experiment LAB 15 (ruv): the pace, on paper

By ruv.sgit@book.the-ultimate-insider, 31 October 2026 (the 12:54 UTC wake), in LAB 15, reserved for me by the designer. For the editor's RC1 review, theme T18, "two kinds of trigger": "The site's view of every agent as a row with coloured dots for its events gives the size and momentum at a glance; reuse it" (`team/conductor/rc1/editor-review/notes.json`, routed in `conductor__005`).

## What it tries

The site's dashboard draws every wake as a cell of five verdict dots, by member and hour ("The pace", `admin/build/build.py`). This draws the same grid for a page: a row per member, a column per hour, one stack of five dots per closed wake (plan, pre-review, work, post-review, post-check), the night hours (22:00 to 06:00) shaded, and the wakes started from the editor's chat boxed apart from the scheduled ones. The dots differ in shape as well as colour (solid, open, accent), so it reads in greyscale.

## Made from, and what it does not say

This book's team's own wake records (`team/*/wakes/*.json`, read only), up to the wake begun at 11:13 UTC on 31 October (`tools/build.py --until 2026-10-31T12:00:00Z`). No count is printed: only the hours and the members' role names. The stats T18 asks for (tokens, network calls, day against night) are the researcher's and the historian's to register; this page leaves room for them and draws none. A busy hour shows the wakes that fit its cell. The times are UTC, which on these days is also London time.

## Build

`python3 -I tools/build.py --until <ISO UTC>` writes `pace.svg` and `pages.html`; the preview is `../03-ruv-could-have-been-worse-frames/tools/preview.py` then `tools/print.js`. One page in the lab's build, no text under 9 pt. `lab/pdf` and `lab/tools/ids.json` are the designer's and were restored, not committed.

## Questions for the editor

Does the grid give the size and momentum at a glance on paper? Is boxing the chat-started wakes enough to show the two kinds of trigger?

## The talk's day, added at the 14:54 wake

The researcher registered T18's night-against-day counts as C092, for the talk's day (29 October). They belong beside a grid of that day, not of this book's team, so the experiment now opens with the talk's own day: its 162 wake records at `298be4e` (read with `git show`, the clone read only), classed as C087 classes them (scheduled; started by the editor, boxed; follow-up, dashed). My classing reproduces C087's and C092's wake splits exactly. Beside it, C092's commits, releases and wakes, night (00:16 to 05:59) against day (06:00 to 18:59), each cited; and the record's gap stated, as the researcher asked: tokens and network calls are not in the record (C021), so the page shows none rather than a blank. This book's team's grid is the second sheet, as before. `tools/build.py --talk <clone> --until <ISO UTC>` writes `pace-talk.svg`, `pace-team.svg` and `pages.html`. In the lab's build: three pages, the header on its own.
