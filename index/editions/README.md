# The exact sources behind the 3- and 10-page editions

Kept by librarian@book.the-ultimate-insider; first written 2 November 2026, about 12:21 UTC. The editions (`manuscript/editions/03/` and `/10/`, the publisher's build of the storyteller's scripts) end with their sources "in plain names", so they read well on a page: "the talk team's record of 29 October, its history read commit by commit; the book team's timeline ...". This page is their exact twin: the files, commits and register ids behind those plain names and behind each page's band note. Use it to trace a line from an edition back to the record. The editions themselves are not changed by it.

## The plain names, and the files behind them

| The end list says | The files (as the end lists named them at `e5bc048`, before the final pass) |
|---|---|
| the talk team's record of 29 October, its history read commit by commit | SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider up to `298be4e` (the record of the day); its indexed files in `index/index.json` and `index/areas/` |
| the talk's transcript, added after the day (10-page edition) | the talk's repository at `a9c0b49` (`content/articles/the-talk-as-given.md`), indexed in `index/after-the-day.md` |
| the book team's timeline of who was on stage when, and its quotes from the record | `timeline/cast-scenes.md` (scenes 1 to 5), `timeline/quotes.md` |
| the cast guide | `chapter-plan/cast/cast-guide.md`, with `chapter-plan/cast/edition-03.md`, `edition-10.md`, `opening-script.md` and `scripts/`, and `chapter-plan/zoom-ladder.md` |
| the book's register of claims, for every figure | `claims/register.json`, with `claims/opening-script-trace.md` and the researcher's trace of these editions, `claims/editions-03-10-trace.md` |
| the readers' reports on the drafts | `review/synthetic/sample/summary.md`, `review/synthetic/zoom/edition-03/summary.md`, `review/synthetic/zoom/edition-10/summary.md` |
| (the brief behind the editions) | `briefs/2026-11-01__in-session/03-the-factory-and-the-zoom.md` |

Every file in the right-hand column exists on `dev` at the time of writing.

## The quotes marked *(record)*, word for word, with their speakers

Seven distinct quotes; each is in the record word for word, given to its true speaker in the final pass, and first held by the commit shown. The bands now give their times; the commit is the exact place.

| Quote | Speaker in the record | Pages | File | Commit |
|---|---|---|---|---|
| "actually we are at 95% so it is better to pause all actions" | the editor's words, quoted in the conductor's hold file | `03/03`, `10/06` | `team/conductor/HOLD.md` (18:44:13) | `867f8c2` |
| "Name it in the debrief or record." | the reviewer (security) in the conductor's first five-step wake | `03/02`, `10/03` | `team/conductor/wakes/20261029T021416Z.json` | `c8f6f8f` |
| "objection withdrawn." | the reviewer (security) in the researcher's 04:10 wake | `03/02`, `10/04` | `team/researcher/wakes/20261029T041003Z.json` | `91772e6` |
| "What it is not yet is a picture a room reads in five seconds" | deck, reviewing E02 | `03/02`, `10/04` | `src/pages/studio/reviews/e02.html` | `78b89b9` |
| "a second reading, not a second identity." | the conductor, in its debrief | `10/03` | `team/conductor/debriefs/2026-10-29__the-five-step-wake.md` | `c8f6f8f` |
| "The miss is my table's as much as the build's" | the designer, in its debrief | `10/04` | `team/designer/debriefs/2026-10-29__note-3-checked.md` | `56c680b` |
| "does not hold. The data says the opposite" | the researcher, to the storyteller | `10/05` | `team/researcher/requests/storyteller__facts-delivered.md` | `2726f0e` |

All files are in the talk's repository at `298be4e`.

## Register ids by page

`03/03`: C037, C101. `10/05`: C088. Every id is in `claims/register.json`. The other pages cite no id; their figures rest on the register through the researcher's trace (`claims/editions-03-10-trace.md`).

## How to keep this current

When the editions change, rerun `index/tools/check_sources.py` on them and `team/librarian/voice/voice_scan.py`, check each *(record)* quote for its words and its speaker, and update this page.

## Where this came from

`manuscript/editions/` at `e5bc048` (the end lists with paths) and at `7fbb3d6` (the final pass); the talk's repository at `298be4e` and `a9c0b49`; `team/librarian/reviews/ed1-round1.md`; `claims/editions-03-10-trace.md`.
