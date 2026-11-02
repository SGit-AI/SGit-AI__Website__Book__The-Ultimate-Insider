# The 3- and 10-page editions, traced

researcher@book.the-ultimate-insider, 2 November 2026, the 09:32 London wake. This traces `manuscript/editions/03/` and `manuscript/editions/10/` as built by the publisher (letter `publisher__004`, from the storyteller's scripts at 04:42), against `claims/register.json` and the talk's record at `298be4e`. It covers the storyteller's new lines on pages 1, 6 and 9 of the script (`storyteller__036`; edition pages 5 and 8 in the build). It is ED1's number lane before round 1; the full trace follows round 2.

**In short:**
- Every *(record)* quote is in the record word for word, but one is given to the wrong speaker.
- One line says "the team's own data" where the data was published reports.
- Two small ordering and time fixes.
- Everything else holds, including the title's numbers and the price line (C101).

## What needs a change

| Edition, page | The edition says | The record says | Change to |
|---|---|---|---|
| 3 p2; 10 p4 | Researcher: "My reviewer said a file was not mine to change. (I showed) It was. 'objection withdrawn.' *(record)*" | "objection withdrawn" is the **reviewer's** words, in security's second pre-review of the researcher's 04:10 wake: "editor-decisions.json is in scope (evidence/**): objection withdrawn" (`team/researcher/wakes/20261029T041003Z.json`, 04:11:55; committed in `91772e6`, 04:12:20) | give the quote to the reviewer (the clipboard), e.g. *Reviewer:* "objection withdrawn." *(record)* and the researcher's line without quote marks |
| 10 p4, band | the researcher's dispute (04:11) | 04:11:55 in the wake record; 04:12 in the commit | keep 04:11 (the wake record) or say 04:12; either holds |
| 3 p2; 10 p5 | "The researcher checked one of my lines against the team's own data" / "against the team's own data and found the opposite" | R5 rests on published reports: DBIR 2025 and 2026, M-Trends 2026 (`team/researcher/requests/storyteller__facts-delivered.md`, `2726f0e`) | "against the published breach data" |
| 3 p2 | "Later the researcher joined" after the conductor's first review | the researcher's first commit was 01:52 (C011); the conductor's first review was 02:19 (`c8f6f8f`) | "The researcher had joined by then" or move the line before the conductor's |

## What holds

- **The title:**
  - **Nine Agents:** nine staffed (C011). Security was proposed and never staffed; "ten" stays open.
  - **Nineteen Hours:** 00:16 to the talk due at 19:00 is 18 h 44 min (C010, C100). As a title it is a rounding. Say it exactly once inside, as the storyteller's 042 already plans.
- **"The first four within the hour"** (3 p1, 10 p2): from the repository at 00:16:23 (C001), dev 00:40, the conductor 00:44, deck 00:51 and ruv-sgit 01:08 (C011). All four came within 52 minutes.
- **"Six agents. The editor's chair is empty from five in the morning to two in the afternoon"; "For nine hours I started nothing"** (3 p2, 10 p4): six on stage by 05:00 (C011); from 05:00 to 13:59 every wake was started by the schedule (C087). "Started nothing" holds for wakes.
- **"Security's chair, planned at midnight"** (3 p3, 10 p6): the conductor's roster at 00:44 (`97b98d9`) maps "conductor, security, researcher, deck, dev". Security was never staffed (C011).
- **The hold** (3 p3, 10 p6): 18:44 (C006). The quote "actually we are at 95% so it is better to pause all actions" is the editor's, as `team/conductor/HOLD.md` gives it. "Sixteen minutes before the talk was due" holds (C100). "What was already in flight still landed": C005, C065.
- **The three accounts of why** (10 p6): C089, dated as written.
- **"Name it in the debrief or record"; "a second reading, not a second identity"** (10 p3): `c8f6f8f`, 02:19. The band's "between 01:39 and 02:19" holds.
- **Deck's review and the designer's note** (10 p4): 06:21 (`78b89b9`) and 10:49 (`56c680b`). The conductor's note at 10:05 (`09317d9`): "again" holds, as it was the second note.
- **The player** (10 p5):
  - "My first priority" holds: "the main priority", in the editor's brief of about 13:50 (`team/conductor/briefs/2026-10-29__editor/README.md`).
  - It was ported at 15:07 (`3314ffe`).
  - Fixes "in the last hour before the talk": the editor asked for player changes at 18:05, 18:10, 18:15 and 18:25, all landed by 18:37 (`23739cc`, `12e93db`, `013d97e`, `dbd75ad`).
  - C088 for the unclosed wake.
- **"I kept the line in the talk"** (3 p2, 10 p5): the beat "The outside is mature, the inside is not" is in `src/static/talk/talk.json` at `298be4e`.
- **Studio's refusal** (10 p5): 17:47, "made by the session's own check". Taken from the earlier trace.
- **What did not work** (10 p7):
  - The lock tool was never run (C027).
  - Only part one was final (C027).
  - The freeze at 02:47 and the correction at 02:52 (C031); the out-of-date figure reached the stage (C031).
- **The second factory "the next day"** (3 p3, 10 p8): this repository's record begins on 30 October, with the conductor, librarian, historian, researcher, storyteller and publisher there that day. Web Summit as "the technology conference in Lisbon": the newsroom's article of 16 October gives Lisbon, 9 to 12 November (`claims/ps1-sources.md`, section 5). "Several people": the editor's brief of 1 November. The Web Summit team article of 31 October says seven, which the edition rightly leaves out.
- **The price line** (3 p3, 10 p9): C101 as written, with its date and C037 beside it.
- **The talk of 58 beats, given on the evening of 29 October** (10 p1): C015, C100.
- **"Within the hour"** (10 p1): members woke hourly on the day (C071), so a change asked at one slot could land by the next. It holds as "within the hour" for the afternoon loop. The player fixes above landed within minutes: the last, asked at 18:25, at 18:37.

## The final build (ED1, after round 2): traced

At the 12:32 wake on 2 November, against the final build (`05ee698`, the publisher's letter 005), as a diff from the version traced above.

**In short:**
- All four fixes are in: the reviewer's quote, the published breach data, "by then the researcher had joined", and the times.
- Every number in the final build traces.
- One caption promises more than its figure shows.

- **New line: "By twenty to one it held a brief and one page of rules"** (3 p1, 10 p2). This holds. Dev's first commit (`1f7c633`, 00:40:50) adds `BRIEF.md`, `CLAUDE.md` and `team/dev/ROLE.md`; the conductor's `CLAUDE.md` follows at 00:44 (`97b98d9`).
- **New line: "That it was given that evening rests on its transcript, added to the record after the day"** (10 p1). This holds (C069, C100).
- **New line: "the out-of-date figure reached a slide in the talk"** (10 p7). This holds (C031: $17.4M on the definition slide, never changed).
- **The scorecards** (10 p2, `figure-10-02.svg`):
  - On stage from: dev 00:40, the conductor 00:44, deck 00:51, ruv-sgit 01:08 (C011).
  - Commits: 64, 106, 59 and 84 (C014: commits whose subject names the member, merges not counted). Each card carries its ids. All hold.
  - **Caption:** it says the cards show "on stage from, commits, wakes, slot". The cards show only the first two. The caption should match: "on stage from and commits".
- **The two strips** (10 p6 and p7): no number. The lines rest on these entries:
  - "Nobody lifted it that day": C024.
  - "The designer pushed after it": C065.
  - "One out-of-date figure ... on the definition slide": C031.
  - "None of them reached the stage": C030.
  All hold as dramatised.
- **The bands:** "my own words in the hold file" (`team/conductor/HOLD.md`) and "my later two accounts, given after the day" (C089) hold. So does "Dramatised (the conductor's line)".

## Not traced here

- The shop owner and the team of three (3 p2, 10 p9): examples, not claims.
- Deck's "If a room cannot read one at a glance, it goes back" and the other unquoted scene lines: dramatised, and the cast guide's.
- The series page: G1, signed.

## Where this came from

`manuscript/editions/03/` and `10/` as on dev at the 09:32 wake; the talk's repository at `298be4e` (read-only clone): each commit and file named above; `claims/register.json` C001 to C101. Checked on 2 November 2026, about 09:40 UTC.
