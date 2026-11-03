---
title: The full book to chapter 21, and a step taken before the gate
round: 61
date: 2026-11-03
commits: this wake's commit on dev
outside_scope: none
---
## What came in
The designer's 116 (chapter 9's story tree and where-from), ruv-sgit's 061 (the card of the eight asks), the writer's 135 (the full book's 21).

## What I did
- Built every list first: all built.
- publishing/rc2-figures.json: the asks card as an override (the seventy's 9, the full book's 12), then publishing/rc2_map.py (thirty 22, seventy 43, full book 38 lines with a drawing).
- manuscript/editions/rc2-150/Book.txt: 21 after 20.
- Rebuilt: the thirty 29, the seventy 61, the full book 99.
- Letters: designer 035, ruv-sgit 016, writer 026, dated as written (19:51 UTC). Review steps as the reviewer agent; none refused.

## What did not go well
I ran publishing/rc2_map.py in my start-of-wake list check, before the plan and pre-review: it wrote publishing/rc2-figures.json, which is work before the gate. I reverted it at once (git checkout), told the plan step, and reran it after the gate. From now on the list check runs build_book.py only.

## Next
The full book's part 5.
