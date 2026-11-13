# The quotes lane at 20:11 on 13 November: the editor's pen on pages 2 to 4, landed in 00 and 00b

By librarian@book.the-ultimate-insider, 13 November 2026, about 20:30 UTC. Read: `git diff acc59a81..HEAD -- manuscript` with the file headers kept; `--name-only` lists exactly two files: `00-start-here.md` and `00b-who-is-telling-this-story.md` (the writer's 19:38 commit, PEN1 round 1 notes 1, 2, 4 to 6, 14, 17 to 19, 21 to 23, 25 to 30). dev's head `eeb7f5fe`; the talk's clone. Edited nothing of anyone's.

## Findings

None. The changes are the editor's own rewrites and cuts, each with its note number on a record line. Where a claim of record entered the reading text it holds: "the talk was given at hack::soho, in IOActive's London office, on 29 October 2026" (C100, with the venue sourced to the talk as given, added after the day, `a9c0b49`); "every agent that built it left a record of what it did" (C022: all nine members have wake records, 162 in all); "Sixteen minutes before the talk was due, I stopped them all" is the figure the book uses everywhere (C100); the empty chair "was more coincidence than decision, and the project did not need it" is C132, the editor's reading, printed at his word; the companion site's address is the one `book.json` records as signed by the editor (30 October) and chapter 00 prints; the Black Hat Europe keynote of 9 December 2025 and the 15 October demo are C116's, unchanged. No new quotation, number or commit id. `claims/final-pass.py` in the talk's clone: FAILS 0. Sources: one tool note at 10 line 92; voice and logistics as before. Every chapter of the 150 and the back matter passes in the quotes lane with nothing open.

## Where this came from

`manuscript/rc2/150/00`, `00b`; `team/conductor/print-review/round-01.json`; `claims/final-pass.py`; `claims/register.json` C022, C100, C116, C132; `book.json`; the writer's 19:38 commit.
