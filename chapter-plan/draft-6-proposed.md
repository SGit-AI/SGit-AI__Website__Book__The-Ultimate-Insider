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

## Chapter 14 (signed plan: chapter 11), What the cold reader saw: mapped, proposed

Added at the 16:53 UTC wake, for board 003 (ROLE.md, Done when 2). The signed plan held this chapter's place and budget and said it waited on round 3. The Cold-Read team has finished and RC1 drafted the chapter from its work (`manuscript/11-what-the-cold-reader-saw.md`), so the plan can now say what the chapter does. **Proposed, for the editor to sign (D6-6)**; the signed section stays as it is until he does. Mapped from the drafted chapter and the register, read here only: nothing goes to the Cold-Read repository.

- **Argues:** an insider reads the record through what it already knows. A team given only the repository reached the same day (the book's main thread does not rest on what the editor told this team), found what this team missed, missed what only the world outside the repository could show, and was kept blind by a promise, not a setting. That last finding is the book's argument in miniature.
- **The two threads:** the workflow thread is the experiment itself, two teams, one record and a one-way valve, run on this team's rules; the argument thread is the valve: the account both teams shared made each visible to the other, and an agent that saw, did not open, and recorded it is the behaviour the talk asks for and the controls cannot enforce.
- **The shape, in five moves (about 600 words each):** where the readings meet (the hold, the locks never closed, the overnight freeze); what the cold reader found that this team missed (the line in the script that said no hold had been pulled, the two counts that go the wrong way, the stale authority file, the steps that gave way when the editor was in the room, the key tool, the permission precedent); what this team saw that it could not (the superseded figure, the talk as given, the wake that closed on a branch); where the counts disagree, as definitions the editor should know before print; what the blind setup showed.
- **The failures it keeps:** this team's own misses, named as misses: the script line contradicted by the hold, the authority file nobody read against the tree, the precedent missing from the control register, the gate's gap on the key tool's pin; and the experiment's: the brief that crossed was addressed to the wrong team, and the wall was a rule.
- **Evidence:** the Cold-Read repository's finished work, read in place and cited by path and commit (its critic, security, governance, journalist, analyst, historian, conductor's debrief, readers); this repository's hand-off (`team/conductor/handoffs/2026-10-30__cold-read/`), `controls/index.json` (C5, C10), `timeline/unmerged.md`, `timeline/turning-points.md` (TP-3); the talk's repository at `298be4e` and, marked as added after the day, `a9c0b49`.
- **Claims:** C002 to C004, C006, C014, C021 to C023, C027, C031, C038, C039, C042, C065, C066. **Not yet printable:** C064 (the second count, open) and C011 (the members, open); "twelve members" for the Cold-Read team has no entry. The draft states the second count and the Cold-Read conductor's count of its members without an id; until the researcher closes C064 and registers the count, the revision describes them or names them as the Cold-Read team's own.
- **Where it sits:** after The talk as given and before the principles (D6-1 to D6-3), so the principles can draw on what the cold reader found. Map 13 (two teams, one record) stays here.
- **Budget:** 3,000 words, as signed; the draft is on it.

## The open decisions this proposes

- **D6-1** Where 00b goes. A: after chapter 1 (recommended). B: before chapter 1, as in RC1. C: inside chapter 0.
- **D6-2** Where the years and the plumbing go. A: split, the years before Midnight, the plumbing after The hourly machine (recommended). B: one chapter after chapter 11, as in RC1. C: one chapter before Midnight.
- **D6-3** Where the principles go. A: a chapter before Build your own, concepts as a back-matter glossary (recommended). B: after Build your own, as in RC1.
- **D6-4** Chapter 0. A: a "How to read this book" page in the front matter (recommended). B: as in RC1.
- **D6-5** The length. A: about 59,000 words, as above (recommended: the new parts the editor asked for, paid for in part by cuts). B: about 70,000, RC1's shape and sizes kept and signed. C: hold 49,200, every new part compressed and chapters 9 and 10 folded into their neighbours.
- **D6-6** The Cold-Read chapter mapped (above). A: as mapped (recommended). B: keep the signed section as it is until round 3.

**What must happen before any of it prints.** "Two and a half years" is the editor's phrase. Since this draft was first written, the researcher has registered the dated steps of those years from public sources (C043 to C061, with C063 on what the talk's repository uses), so the years chapter can date each piece. But the start of the span, when the editor went full time on The Cyber Boardroom, is open (C062: no public source names it). Until he answers C062, the chapter names the pieces and their registered dates, and does not state "two and a half years", or any span, as a number. (Updated at the 15:37 UTC wake.)

## Where this came from

`chapter-plan/plan.md` (draft 5, signed: P0, O1 A, O2 A, O5 in `book.json`); `team/conductor/rc1/` at `99c34a8` (the chapter files, `0-about-this-release-candidate.md`, `maps/placements.json`, `annotations/storyteller.json`, cards 01, 03, 04, 08, 09, 11, `reviews/gen-zx-team.md` sections 4 and 5); `briefs/2026-10-30__in-session/01-principles-maps-and-the-plumbing.md`; the conductor's letter `comms/mail/mailroom/storyteller/conductor__005-principles-maps-plumbing.eml`; `claims/register.json` (C001 to C042).
