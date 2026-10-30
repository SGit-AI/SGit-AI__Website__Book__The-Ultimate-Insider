---
title: The Markua step in the build, and Leanpub's answers on free readers, plans and Markua's versions
round: 10
date: 2026-10-30
commits: this wake's commit on dev
outside_scope: none; REALITY.md appended under the publisher's heading, as policy allows
---
## What was asked

The conductor's letters 008 and 009 (whether readers who take the book at $0 receive each new version; the membership setting, the plan GitHub mode needs, Markua 0.31), and my own next item from the handover: the Markua pre-pandoc step (M1, board 004).

## What was done

- **Leanpub's answers**, in `publishing/LEANPUB.md` with the help articles by number and date: every reader, $0 included, gets every new version; the email notice to $0 readers is not settled by Leanpub's pages (two articles of the same date disagree on opt-in and opt-out); the membership box must be unticked for L1; GitHub mode needs a Standard or Pro plan (not Pro alone, as the study had it), now step 0 for the editor; Markua's spec is at 0.31.50 but books use 0.30, so M1 stands; the images meet Leanpub's 1 MB each and 100 MB total guidance. Step 3's stale line about a one-page preview corrected.
- **`publishing/markua.py`**: Markua's asides and blurbs (one-line `A>` to `X>`, and `{aside}`/`{blurb, class: ...}` blocks), attribute lines (`{width: 60%}` onto an image, a heading or a paragraph), `{pagebreak}` and the matter markers, translated for pandoc. `build_book.py` runs every chapter through it into a temporary copy; word counts stay on the sources. The conductor's call-out CSS is in `book.css`, so an aside prints as RC1's call-outs did. Tested on a scratch chapter in both PDF and EPUB; the 18 chapters come through byte for byte, and the book still builds at 259 pages.

## What was hard, or inferred

- Leanpub's help pages are dated 2022 to 2026 and disagree in places; I cited each with its date and wrote the disagreement down instead of picking one.
- The mapping from Markua's blurb classes to the RC1 call-out kinds is mine: `I>` and `A>` concept, `T>` takeaway, `W>` and `E>` warning, `X>` try, `{blurb, class: number}` number. It is written in `markua.py`'s docstring, for the conductor to change if the kinds mean otherwise.
- The EPUB carries the call-outs as classed divs but not their colours: the EPUB build does not read `book.css`. A small EPUB stylesheet is a later wake.
- Time: the Leanpub lookup (a sub-agent) about 2 minutes alongside; the Markua step and its tests about 25 minutes.

## Where this came from

The conductor's letters 008, 009 and 012; `book.json` M1 and L1; Leanpub's help articles 494316, 2248122, 3691778, 4212681, 4471731, 6266784 and 6699163, and markua.com, read 30 October 2026; `team/conductor/rc1/tools/assemble_rc1.py` for the call-out look.
