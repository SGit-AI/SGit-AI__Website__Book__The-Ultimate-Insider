# Brief for conductor@the-book (the informed repo)

## The project **[editor]**

A book about what was built on 29 October 2026: a ten-agent team, run by one person, that took a talk from nothing to on stage in one day, with the record to prove it. The first commit was at 00:16, the talk at 19:00, the merge to main at 23:19: nineteen hours, 816 commits (603 by Claude, 211 release commits by GitHub Actions, 2 by the editor), 211 site releases from v0.1.0 to v0.2.0.

The book is about two things, told as one story:

- **the workflow**: how the team was set up, briefed, scheduled, keyed, reviewed, held and released, and how to replicate it elsewhere; this is the main thread;
- **the argument**: the talk itself, The Ultimate Insider (agents as the insider that has none of the old attacker's limits, the perfect storm, Agent Behaviour Policies, SHarness, brakes so we can go faster). It runs through the book because every control the team used is an answer to that risk, and because the team that built the talk is itself the ultimate insider, held in check by its own policies.

The gap the book fills: the public conversation says agents cannot be made to work, are too risky, and do not pay back. Here is a counter-example with a timestamped record, and the controls that made it safe.

## The centre of gravity **[editor]**

The editor chose the third of three candidates: not the argument alone (the talk as a book), not the method alone (a playbook), but **the two as one story**: the team that built the talk is the ultimate insider, and the book shows the controls working on itself (the 18:44 hold when the editor's usage reached 95%, signed session keys, the pinned key tool, a review before and after every wake, decisions that only the editor can sign).

## Not raw content: analysis with hindsight **[editor]**

The book is not a dump of the record. It is analysis written with hindsight: what was achieved, in what order, why it worked, what it cost, what went wrong, and what it means. The record is quoted as evidence; the writing explains it. Every chapter ends with where it came from (the same rule as the Gen ZX book).

## The target and the dates **[editor]**

- **Monday 2 November 2026:** the first edition on sale on Leanpub.
- **Monday 9 November 2026:** Web Summit opens (9 to 12 November). By then: on Amazon too (KDP review takes up to 72 hours), and a paperback proof ordered. The paperback is the stretch goal.
- The book names its own phases: tonight was the explorer's build; this edition is the villager's; a publisher's edit later is the town planner's. (The editor's words: explorer, villager, town planner.)
- The pace: hourly wakes, as on the talk's team, round the clock at first; the editor may narrow the hours.

## Two repositories **[editor]**

1. **The book repo** (this one): the conductor knows the whole story from the start, owns the book, and drives the writing. It reads the talk's repository and the blind repo's findings.
2. **The blind repo**: its agents arrive knowing nothing but the talk's repository at v0.2.0, and write what they find. See `2-blind-repo-brief.md`.

**The one-way valve** (Claude's proposal, the editor agreed): the book repo reads the blind repo; nothing flows the other way, or the blind repo stops being blind. No brief, chapter, decision or chat from the book repo is ever copied into it. The blind repo's agents must not be given this file.

Both run in parallel. The source for both is the talk's repository pinned at tag/commit `298be4e` (site v0.2.0, main). Read-only: nobody on either team pushes to it.

## The team

Reuse the setup of the talk's team as it stands (start.py, five-step wakes, status.json, mailrooms, session keys and the pinned key tool, HOLD.md, REALITY.md and BRIEF-CORRECTIONS.md, the hourly slots fifteen minutes apart, a release on every merge). See `5-lessons-to-carry.md`. Roles proposed for the book repo:

| role | owns | first task |
|---|---|---|
| conductor | the schedule, routing, pace, the editor's decisions page, the two-repo valve | stand up both repos; fix the chapter plan with the editor by Friday night |
| librarian | the inventory of the source: every file, wake, debrief, decision, memo and chat, indexed | the index, before any chapter is written; `3-source-map.md` is the seed |
| historian | the timeline: the day minute by minute, from the git log and the wake records | the timeline of 29 October, with the ten or so turning points marked |
| technologist | how the setup works: tools, schedules, keys, vaults, builds, the player | the architecture of the team, as diagrams and prose, enough to rebuild it |
| security (GRC) | the controls: policies, holds, keys, reviews, what each one stopped, what it missed | the control register: every control in the record, with evidence of it firing |
| storyteller | the arc: chapter plan, voice, the two threads braided | the chapter plan, from the librarian's index and the historian's timeline |
| writer (deck's successor) | the chapters themselves | chapter 1 as soon as the plan is signed |
| researcher | claims register; every number in the book traced to the record or a source | the numbers in this brief, checked; then the talk's claims, as the talk's researcher left them |
| designer / illustrator | covers, the book's infographics, the talk's visuals re-drawn for print | the cover in three proposals; the list of talk visuals that survive on paper |
| publisher | Leanpub and KDP listings, PDF and EPUB from one source, the paperback proof | the Leanpub book created and the build producing a PDF on day one |
| readers (synthetic) | the market research: who buys this, what they call the problem, where they put it down | see the market stream below |

The editor is the editor: he decides, signs decisions, reads on paper, and is interviewed. Nobody else speaks for him.

## The rounds

- **Round 0 (Friday 30 Oct, daytime):** repos up, keys published, schedule running, Leanpub book created, build producing an empty PDF. Librarian index started. Blind repo's agents fired.
- **Round 1 (Friday night):** index, timeline, control register, chapter plan. The editor signs the plan and the title.
- **Round 2 (Saturday):** chapters drafted from the plan, each from the record, analysis first. Market stream reports: readers and positioning.
- **Round 3 (Sunday):** the editor reads on paper; synthetic readers read the draft; corrections; cover chosen; the blind repo's findings compared with the book's own, and the differences written up as a chapter.
- **Round 4 (Monday):** release candidate, the editor's sign-off, on sale on Leanpub. KDP submitted.
- **The week to the 9th:** Amazon live, paperback proof, the town-planner list started (what a publisher's edit would change).

## The market-research and positioning stream **[editor]**

Starts in the book repo at once, in parallel with the writing, so the positioning can be validated before Web Summit:

- synthetic readers, five to eight, built from real buyer types (a CISO, a head of platform engineering, a founder building with agents, a GRC lead, an investor, a sceptical senior developer, a conference-goer at Web Summit): each reads the brief and the chapter plan, says what they would pay, what they would call the problem, and where they would put the book down;
- the positioning: three candidate statements, tested against the readers; the title and subtitle chosen from `4-positioning-starter.md` or better ones;
- the comparison set: the books and reports a buyer would see beside it;
- the Web Summit plan: what to say in one sentence, what to show (the player, the record), and what the QR on the paperback's back points to.

## Rules

- The source is read-only and pinned. The blind repo is write-once from the book side: never.
- Analysis over raw. A chapter that is mostly quoted record is sent back.
- Every number traced. The researcher's register is the only place a number may come from.
- The failures stay in: the hold at 95%, the player port landing late, the researcher contradicting the editor's claims, anything the blind repo finds that the book repo missed.
- The editor's limits are a control: the conductor watches usage and pauses the team before the editor is cut off, as the talk's conductor did at 18:44.
- Nothing on either team builds or describes anything attack-shaped. The insider argument is made with this benign team.
- Open on every wake: HOLD.md first, vault_check first.

## What the conductor asks the editor now

1. The repository names and addresses (proposal: `SGit-AI__Book__The-Ultimate-Insider` and `SGit-AI__Book__The-Ultimate-Insider__Blind`, sites under sgit.ai).
2. Whether the hours are round the clock or 08:00 to 22:00.
3. The title: pick or strike from the starter list, or give his own.
4. Whether the editor's voice memos and the claude.ai session transcripts of 29 October go into the source (they are not in the repository; the editor holds them).
5. The licence: CC BY 4.0 for the text as for the Gen ZX book, or something else.
