# The chapter plan, draft 6: proposed, not signed

storyteller@book.the-ultimate-insider, 30 October 2026, the 13:02 UTC wake (the second account's first). **Draft 5 (`plan.md`) is the signed plan and stays so.** This file proposes how the plan follows RC1 as it now stands (`team/conductor/rc1/`, read at `99c34a8`) and the editor's principles of about 10:30 UTC (`briefs/2026-10-30__in-session/01-principles-maps-and-the-plumbing.md`). Nothing here is acted on until the editor signs it: the choices are offered to the conductor as open decisions D6-1 to D6-5 for `book.json` (`comms/mail/mailroom/conductor/storyteller__004-principles-answered.eml`). It answers the conductor's letter 005.

## What changed since the signature

RC1 added three parts the signed plan does not have, at the editor's word: **00b How to read a map** (after chapter 0, maps 1 to 5), **11b What was already there** (after chapter 11: the plumbing, then the years before the day, maps 6 and 7) and **13 Concepts and principles** (after chapter 12). It placed eleven more maps in the chapters (`team/conductor/rc1/maps/placements.json`). The Gen ZX Founders team's review (`team/conductor/rc1/reviews/gen-zx-team.md`, section 5) asks that the new material be paid for with cuts.

**The length.** The drafts total about 69,300 words (`wc -w` on the seventeen chapter files and the note "About this release candidate", `Where this came from` sections included, at `99c34a8`) against the signed 49,200. The three new parts are about 17,200 of it; the rest is the signed chapters running over: chapter 0 by about a quarter, chapter 10 by about a fifth, chapters 2 and 4 by about an eighth. Word counts here are working measures of drafts, not claims about the record.

## Three placements I would change in RC1

1. **00b goes after chapter 1, not before it.** The signed decision O2 A opens the book on the 18:44 hold. With 00b after chapter 0, a reader meets over 3,000 words on maps before the hold. 00b already ends on the usage dot and says "Chapter 1 opens on that moment": after chapter 1 it reads better still, as the map of a moment the reader has just lived. Chapter 0 becomes a short "How to read this book" in the front matter (the storyteller card 11, B), so the hold is the first page.
2. **11b splits in two.** The years before the day go before chapter 2 (they are why midnight was not empty); the plumbing goes after chapter 4, once the reader has watched the gate, the releases and the wake fire. After chapter 11, both arrive after the reader needed them. (Card 03, B.)
3. **The principles come before chapter 12, the concepts go to the back.** Chapter 12 ends on "The brakes are what let you go faster", the talk's own close and the book's strongest last line. A principles chapter after it ends the book on a summary. The concepts become a short glossary in the back matter (each entry pointing to where the book shows it), because Gen ZX change 2 explains each concept where it first appears, so the long concept entries repeat the chapters. (Card 04, B.)

## The order, with a map and the concepts for each chapter

Budgets are option A of D6-5 below. "Concepts" are those first explained there (from the Gen ZX review's table 4.1, moved to where each should be explained once the order changes).

| # | Chapter | Budget | Maps | Concepts first explained here |
|---|---|---|---|---|
| front | How to read this book (was chapter 0) | 600 | none | the record pinned at a commit; register ids as the fact marker; explorer, villager, town planner (credited) |
| 1 | Pause all actions | 3,000 | none (the turning points as a drawn timeline) | the hold; the usage limit as a resource; wake, banner (one sentence each) |
| 2 | How to read a map (was 00b) | 2,500 | 1 to 5 | Wardley map: user need, value chain, evolution, inertia; the day as a value chain |
| 3 | What was already there: the years (from 11b) | 3,000 | 7 | sgit, SHarness, The Cyber Boardroom, Issues-FS, Memory-FS, Type_Safe, the newsroom (what each made possible on the day, not a product list) |
| 4 | Midnight, an empty repository | 3,800 | none | `CLAUDE.md`, the brief and its corrections, `REALITY.md`; agent, session; two branches, `dev` and `main` |
| 5 | A mandate you can read | 4,200 | 8 | reach, mandate, the gap; setting, expectation, boundary; role, policy, scope; session keys; a pinned tool |
| 6 | The hourly machine | 4,000 | none (the schedule as a clock, the wake as a cycle) | scheduled task, slot, the five-step wake, sub-agent; requests as files; the board and the mailroom |
| 7 | The plumbing (from 11b) | 2,500 | 6 | CI owns the version; the gate and its tripwire; Markdown twins; non-functional requirements |
| 8 | The story before the slides | 4,000 | 9 | the talk as data, beats; the claims register; a record is not a gate |
| 9 | The editor signs | 3,500 | none | signing; the morning review |
| 10 | Building the talk | 4,000 | 10 | ports |
| 11 | The locks that never closed | 3,000 | 11 | the lock; two brakes |
| 12 | The team was the insider | 3,000 | 12 | the session's own permission check (C10); the ladder of controls |
| 13 | The talk as given | 3,000 | none | (none new) |
| 14 | What the cold reader saw | 3,000 | 13 | the Cold-Read team and the one-way valve |
| 15 | Principles (from 13) | 3,000 | none | the principles, each pointing back to its chapter |
| 16 | Build your own | 4,500 | 14, 15, 16 | (none new: it puts them to work) |
| back | Appendix A. Every number rerun | 2,000 | | |
| back | Appendix B. The control register (from chapter 12, was 9) | 1,000 | | |
| back | Concepts, a glossary (from 13) | 1,500 | | |
| | **Total** | **59,100** | 16 | |

Every chapter keeps what the signed plan gave it: its argument, its two threads, its failures and its claims line. Only the order, the budgets and the three new parts change.

## Where the cuts come from (option A)

From RC1 as it stands, about 10,200 words:

- Chapter 0 to a front-matter page, "The claim this book answers" moved to the end of chapter 1 (card 11): about 900.
- The hold told once: chapter 1 keeps the scene, the locks chapter owns the analysis (card 08): about 900.
- The control chapter argues with four controls; the full walk moves to Appendix B as a table (card 09): about 1,000 net.
- The talk as given back to 3,000: about 1,200.
- The record thinned out of the prose into each chapter's sources (Gen ZX change 8), chapters 2 to 4 of RC1: about 1,100.
- 00b to 2,500 (the four steps kept; "The maps still to come" becomes one paragraph, since each map now introduces itself): about 850.
- 11b from 6,800 to two chapters of 5,500, by cutting what the public record does not say to one paragraph: about 1,300.
- Concepts and principles from 7,050 to 4,500 (glossary and principles), because each concept is now explained where it appears: about 2,550.
- The rest from chapters a little over their budgets (A mandate you can read, Building the talk): about 400.

## The open decisions this proposes

- **D6-1** Where 00b goes. A: after chapter 1 (recommended). B: before chapter 1, as in RC1. C: inside chapter 0.
- **D6-2** Where the years and the plumbing go. A: split, the years before Midnight, the plumbing after The hourly machine (recommended). B: one chapter after chapter 11, as in RC1. C: one chapter before Midnight.
- **D6-3** Where the principles go. A: a chapter before Build your own, concepts as a back-matter glossary (recommended). B: after Build your own, as in RC1.
- **D6-4** Chapter 0. A: a "How to read this book" page in the front matter (recommended). B: as in RC1.
- **D6-5** The length. A: about 59,000 words, as above (recommended: the new parts the editor asked for, paid for in part by cuts). B: about 70,000, RC1's shape and sizes kept and signed. C: hold 49,200, every new part compressed and chapters 9 and 10 folded into their neighbours.

**What must happen before any of it prints.** "Two and a half years" is the editor's phrase and has no register entry yet (the register runs to C042). Chapter 3 above may not state it, or any date in it, until the researcher registers it from his public articles.

## Where this came from

`chapter-plan/plan.md` (draft 5, signed: P0, O1 A, O2 A, O5 in `book.json`); `team/conductor/rc1/` at `99c34a8` (the chapter files, `0-about-this-release-candidate.md`, `maps/placements.json`, `annotations/storyteller.json`, cards 01, 03, 04, 08, 09, 11, `reviews/gen-zx-team.md` sections 4 and 5); `briefs/2026-10-30__in-session/01-principles-maps-and-the-plumbing.md`; the conductor's letter `comms/mail/mailroom/storyteller/conductor__005-principles-maps-plumbing.eml`; `claims/register.json` (C001 to C042).
