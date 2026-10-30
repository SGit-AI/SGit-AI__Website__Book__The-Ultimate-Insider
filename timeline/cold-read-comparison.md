# This timeline against the Cold-Read historian's

Kept by historian@book.the-ultimate-insider. Written 30 October 2026, 10:30 UTC, at the editor's request (relayed by the conductor, `team/conductor/requests/historian__review-and-rc1.md`) to review both teams' work. Read only: the Cold-Read team's `team/historian/timeline.md`, in a clone in this session's scratchpad. **Nothing here goes to the Cold-Read repository** (the one-way valve); this file is for this team and the RC1 chapters.

Both timelines read the talk's history at `298be4e`. The Cold-Read one read it with every later ref removed, so it cannot see what was added after the day or what never merged; this one reads all refs and keeps those apart (`after-the-day.md`, `unmerged.md`).

## Where they agree

Every time and commit both cite agrees to the second, from `2e4b1f4` (00:16:23) to `298be4e` (23:19:51). Both read the hold the same way (`867f8c2`, 18:44:13; part 1 final, not locked; C027), the conductor's tasks for others disabled before they fired (`d8f3300`, `b620234`), the first five-step wake closing partial (`c8f6f8f`), the 14:07 briefs, the 15:21 step limit, the 16:59 three parts, and the editor's chat run of 17:16 to 17:48. Two readers who never compared notes reached the same sequence: the strongest check this timeline has had.

## What the Cold-Read timeline has that this one lacks (to apply here)

1. **Who wrote the unnamed commits.** The "Player:" commits and the lock tool carry the `Claude-Session` trailer of dev's session, the session whose folder dev published at 01:53 (`56cbe55`); checked here on `28fe01d`, `dbd75ad`, `4a2481b`, `3314ffe`. My `16.md`, `17.md` and `18.md` call them unattributed and say the timeline does not guess. The trailer is evidence, not a guess: they can be marked "dev (*inferred* from the session trailer)". For the researcher: C014 counts these 13 as unattributed; the trailer would attribute some of them.
2. **A second wake open at the hold.** Deck's scheduled wake of 18:20:09 (fired 18:19) has only its plan recorded and never closes (`team/deck/wakes/20261029T182009Z.json` at `298be4e`; `89afb77`). My `18.md` names only dev's open wake (17:48:50).
3. **The designer's status contradicts the record.** At 18:45:35 (`88b8f00`), after the hold, the designer's `status.json` says part 1 was "locked at 18:30 after its check"; the conductor at 18:39 and `HOLD.md` say it was not, and no locked copy exists at `298be4e` (`admin/build/lock.py`'s output folder is absent). My `18.md` cites `88b8f00` without this. It belongs there: the last member write of the day records something that did not happen.
4. **A brief whose heading time is later than its commit.** Brief 5 (`5-parts-2-and-3-1715.md`) is headed about 17:10 and committed at 17:08 (`e86b0aa`). My `17.md` should say the record does not settle which is right.
5. **ruv-sgit's first vault deleted at the editor's go**, 02:07:52 (`f21265b`). Missing from my `02.md`.
6. **Whether the talk was given at 19:00**: the Cold-Read timeline says the record (to `298be4e`) does not say. My `after-1900.md` states it as an event citing the brief and `1f7c633`. Stricter and right: before `298be4e` the record holds the plan for 19:00, not the event. The evidence that it was given is the talk as given, `a9c0b49`, added after the day; `after-1900.md` should cite that and say so.

## What this timeline has that the Cold-Read one lacks (recorded here only)

- The editor's freeze of the talk at 02:47, recorded only in deck's reply file (turning point 3, C031). The Cold-Read timeline reads `a082c52` as the researcher's policy agreed, not as the exact-text corrections it also carries.
- The two commits of 18:48 that never reached `dev` (`unmerged.md`), invisible with later refs removed.
- The feedback round dated "about 13:50" by its own brief, before its commit at 14:07.
- The post-review findings about other sites' data (C025) as events, and the pre-review changes of 14:03 and 17:21 to 17:45.

These stay here. The Cold-Read team is finished, and the valve is one-way.

## Numbers

The Cold-Read timeline counts commits per hour, wakes per member and outcomes. None of its counts is used here; where they matter the register holds them (C022, C023, C014). Its per-member wake counts agree with C022.
