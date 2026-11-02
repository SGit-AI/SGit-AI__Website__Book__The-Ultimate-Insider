# The exact sources behind RC2

Kept by librarian@book.the-ultimate-insider, from 2 November 2026 (about 17:55 UTC), at the conductor's letter 018: as RC2's chapters land, each quote is checked word for word and for its true speaker, and its exact place is written here. RC2 is written from the 30-page edition up, then the 70 and the 150 (`book.json` RP1, `chapter-plan/zoom-ladder.md`). Each chapter's files are listed by `index/tools/chapter_entries.py` in `index/chapters/<chapter>.md`; this page adds what that cannot: the quotes.

## The 30-page edition

### Chapter 1, the creator's problem (`manuscript/rc2/30/01-the-creators-problem.md`)

| Line | Quote (opening words) | Speaker | Where it is | Checked |
|---|---|---|---|---|
| 9 | "I had to speak a lot because in a way I had to provide the animation ..." | the editor, voice note of 1 November 2026 | `briefs/2026-11-01__in-session/03-the-factory-and-the-zoom.md` | word for word |
| 23 | "This is a really cool animation of what happens. ..." | the editor, on stage, 15:50 on the recording's clock | the talk's `content/articles/the-talk-as-given.md`, section `#building`, added after the day at `a9c0b49` | word for word; the "..." stands for one sentence left out ("It's a fairly benign environment, and the amount of damage that actually happens is reasonably limited.") |
| 51 | "Creators need an immediate connection to what they create. That's my principle." | Bret Victor, "Inventing on Principle", CUSEC 2012 | outside the book's sources; the register's C103 (checked by the researcher) | through the register |

The band's "commit at 18:29" (line 32) is motion's `5d13d72`, 18:29:28, "M01 the building, the editor's changes".

### Chapter 2, the factory is assembled (`manuscript/rc2/30/02-the-factory-is-assembled.md`)

| Line | Quote | Speaker | Where it is | Checked |
|---|---|---|---|---|
| 7 | "Initial commit" | the editor, the first commit's subject, 00:16:23 | the talk's commit `2e4b1f4` | word for word |
| 86 | "Name it in the debrief or record." | the reviewer (security), in the conductor's first five-step wake | `team/conductor/wakes/20261029T021416Z.json`, `c8f6f8f` | word for word, right speaker |
| 88 | "a second reading, not a second identity." | the conductor, in its debrief | `team/conductor/debriefs/2026-10-29__the-five-step-wake.md`, `c8f6f8f` | word for word, right speaker |

### Chapter 3, the factory runs (`manuscript/rc2/30/03-the-factory-runs.md`)

| Line | Quote | Speaker | Where it is | Checked |
|---|---|---|---|---|
| 24, 30 | "objection withdrawn." | the reviewer (security), in the researcher's 04:10 wake | `team/researcher/wakes/20261029T041003Z.json`, `91772e6` | word for word, given to the reviewer |
| 30 (figure) | "out of scope" | the reviewer, its first objection in the same wake | the same file | the words are in the record |
| 41 | "What it is not yet is a picture a room reads in five seconds." | deck, reviewing E02 | `src/pages/studio/reviews/e02.html`, `78b89b9` | word for word, right speaker |
| 53 | "The miss is my table's as much as the build's" | the designer | `team/designer/debriefs/2026-10-29__note-3-checked.md`, `56c680b` | word for word, right speaker |
| 72 | "This is the main priority." | the editor, his feedback round, as the conductor wrote it down | `team/conductor/briefs/2026-10-29__editor/feedback-briefs.md`, `c9ced4e` | word for word |
| 93 | "does not hold. The data says the opposite" | the researcher, to the storyteller | `team/researcher/requests/storyteller__facts-delivered.md`, `2726f0e` | word for word, right speaker |
| 61 | "That is the part of the record I find hardest to believe, and easiest to check." | the narrator (the editor), kept from the 10-page edition | not a quote from the record | no check needed |

## How to keep this current

For each new RC2 chapter: `index/tools/check_sources.py`, `team/librarian/voice/voice_scan.py`, `index/tools/chapter_entries.py`, then each quote by hand for its words and its speaker, and a row here.
