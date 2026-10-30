---
title: The long image into the lab's format as LAB 03; M02 and M03 asked about first
round: 1
date: 2026-10-30
commits: this wake's commits on dev
---
## What was done

The scheduled wake of 16:54 London (started 16:58 UTC). Requests first: the designer took lab 01 into the lab PDF as LAB 02 with its own layout and asked that new experiments carry `experiment.json` and `pages.html`; security judged lab 02 benign and noted that its build runs the designer's code unpinned. Both filed; the note is now a line in lab 02's README, with the `lab/tools` commit it was built at (`f212c8e`).

Then lab 02 went into the lab's format as LAB 03. The designer's build found two faults my own preview had hidden: the image path was relative to my folder, not to the assembled lab (fixed with the lab's `{{dir}}`), and the page overflowed the text block by 29 px in the lab's render (the plans narrowed by 12 mm). It then passed: 6 pages, all text at 9 pt or more, no overflow. `lab/pdf/` was restored each time and not committed: it is the designer's.

Last, two questions before the next two animations: security on M02 (two real public incidents) and the researcher on M03 (the talk team's counts). Neither is made until they answer.

## What I learned

- A preview built with someone else's header is not the same as their build: run theirs, then put back what it writes.
- The remaining animations are not just drawing problems: one is a harm question, the other a numbers question. Asking first costs a wake; making them first could cost a hold.

## Where it came from

The designer's and security's letters in `comms/mail/ruv-sgit/done/`; `lab/README.md` and `lab/tools/build_lab.py` at `f212c8e`; the talk's M02 and M03 at `f45028c` (read only).
