# The first ten pages: the outline traced

researcher@book.the-ultimate-insider, 31 October 2026, the 18:32 wake. The storyteller's outline (`chapter-plan/first-ten-pages-outline.md`, the 17:40 wake) checked page by page against `claims/register.json` and `claims/first-ten-pages-numbers.md`, before the publisher writes it (T10). The written pages get the same trace, line by line, when they land in `manuscript/sample/`.

| Page | Ids it cites | Verdict | Note |
|---|---|---|---|
| 1. A team of agents made a talk in a day | C001, C011, C015, C004, C069 | holds | "nine agents and one person" is the record's count; C011 is open only for the brief's "ten". "After midnight": 00:16 (C001). "Gave it on stage": about 87 minutes (C069, the transcript, added after the day) |
| 2. What they made | none | holds | no number |
| 3. How you can see everything | C004, C003, C009 | holds | "every release": 210 on the day (C009) if a number is wanted |
| 4. Meet the team | C011 | holds | the order (conductor first, storyteller later) matches the join times (C011, C012) |
| 5. How a day runs | C092, C073, C087 | holds | if the timeline prints counts, night against day is C092; scheduled against editor-started is C087 |
| 6. The rule that let them go fast | C006, C024, C089 | holds, one caution | "minutes before the talk" is 16 minutes (18:44 to 19:00, C006, C010): say "sixteen minutes" or keep "minutes". The reason goes to the footnote as two accounts (C089) |
| 7. What did not work | C029, C030 | holds, one caution | the before-and-after visual: 320 claims, of which 52 were not checked, 210 held whole, 3 did not hold (C029); none of the three reached the stage (C030), but a figure the register had found out of date did (C031). "Claims checked" is not 320 |
| 8. Why this matters to you | C091 | holds | "sold out" only; no participant named; Algarve Evolution's figures only as its own |
| 9. Start tomorrow | none | holds | no number |
| 10. Where this book goes next | none | holds | no number |

**What to keep out**, as the sheet says: tokens, money, a usage total, "ten agents".

## Where this came from

`chapter-plan/first-ten-pages-outline.md` at dev on 31 October 2026, 18:33 UTC (read only); `claims/register.json`; `claims/first-ten-pages-numbers.md`.

## The written pages, traced line by line (31 October 2026, 20:40 UTC)

`manuscript/sample/first-ten-pages.md` at dev, read only. Every line with a number or a time was matched to its id, and quotations to their source.

| Line | What it says | Verdict |
|---|---|---|
| 3 | 00:16; nine agents and one person; 58 beats; 814 commits by 18:46, 603 by the agents; about 87 minutes with questions | holds (C001, C011, C015, C004, C003, C069) |
| 38 | 18:39, the conductor's "part 1 not yet locked, unchanged since 18:30; dev asked to lock it now" and "run lock.py --part 1 now" (`2ed6427`) | holds: the commit is 18:39:16, its subject and its To-dev trailer say so |
| 42 | 814 commits and 210 releases by 18:46 | holds (C004, C009) |
| 68 | nine agents | holds (C011) |
| 79 | 182 commits before six; 162 wakes: 105, 47, 10; from five to two every wake on its schedule | holds (C092, C073, C087) |
| 95 | "sixteen minutes before the talk ... every wake after it stopped" | holds: no wake opened after 18:44:13 (C087) |
| 95 | "and nothing went wrong after it, because nothing more happened" | **does not hold**: a wake already open went on. The designer committed at 18:45:35 (`88b8f00`), its merge at 18:45:36, and v0.1.209 was released at 18:46:22 (C005, C065). Say instead: "no new wake started after it; one already running finished its commit eighty-two seconds later, and the last release followed" |
| 99 | the footnote's two accounts, "two days later" | holds (C089), and a third now joins them: on 31 October at about 19:00 the editor said the 95% "was the tokens usage" (C089). The footnote can add it; the record holds the percentage, not the unit (C021) |
| 113, 120 | 320; 52 not checked; 210 held whole; 3 did not hold, none on stage; one out-of-date figure did reach a slide | holds (C029, C030, C031) |
| 129 | Faro, 31 October, the Vibathon, sold out; "build something that somebody else can use ... That's literally the loop." | holds: the quotation is in the newsroom article word for word (C091) |
| 139 to 143 | the five steps | no number |

One line to change (95), and one footnote that may grow (99). Nothing else needs an id it does not carry.
