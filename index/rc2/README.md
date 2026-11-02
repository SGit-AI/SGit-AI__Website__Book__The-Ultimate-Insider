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

## How to keep this current

For each new RC2 chapter: `index/tools/check_sources.py`, `team/librarian/voice/voice_scan.py`, `index/tools/chapter_entries.py`, then each quote by hand for its words and its speaker, and a row here.
