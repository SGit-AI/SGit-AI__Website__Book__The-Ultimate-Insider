# LAB 29 (ruv), proposed: the afternoon loop

By ruv.sgit@book.the-ultimate-insider, 2 November 2026 (the wake of 18:05 UTC), for RC2's chapter 3 page 4, where the signed outline asks: "the loop drawn over the afternoon: each of his asks, and what came back, on one line of time; for ruv-sgit, from the commits that carry his time in their subject" (`chapter-plan/edition-30-outline.md`, RP1).

## What exists so far

`tools/extract.py` reads the talk repository at `298be4e` (read only) and keeps every commit whose subject carries the editor's time. `data/asks.json` holds what it found: eight commits, from 17:27 to 18:37, four of them the conductor recording his words and four the player's fixes. Nothing is drawn yet: every number on a page comes from the register, so the times wait for the researcher.

## What the extraction cannot see, said now

- The outline's loop starts at about 13:50 (the player as his first priority). No commit before 17:27 carries his time in its subject, so the earlier asks are not in this data; they would need another source (the wake records, or the historian's timeline).
- A time in a subject is the time a member wrote down, not a clock: the player fix stamped "(the editor, 18:05)" landed at 18:04:48, before the time it names.
