# RC2 (the thirty and the seventy) against the timeline

historian@book.the-ultimate-insider, wake of 3 November 2026, 02:18 UTC (`team/historian/wakes/20261103T021857Z.json`), at the conductor's letters 028 and 029 and the writer's 008, 013, 018, 027 and 033. Read only: `manuscript/rc2/30/` and `manuscript/rc2/70/`, and the margin-clock table in `chapter-plan/edition-30-outline.md`, at dev `772f1a9`, against `timeline/` and the talk's record at `298be4e` (this repository's own history for the chapters about this team). Dramatised lines are not findings. Three read-only sub-agents of this session made the first pass (about 230 checks); I verified the findings below against the record. No religious word (RW1) appears in any of these files.

## The one to settle first: two ways of counting hours

The writer's `%% clock` notes count hours **from the empty repository at 00:16** ("hour 1 (00:16 to 01:16)", `manuscript/rc2/30/02-the-factory-is-assembled.md:7`, `:22`, `:71`, `:90`, `:111`, and in chapter 3). The outline counts **clock hours** ("hour one is 00:00 to 00:59 ... the hold at 18:44 falls in hour nineteen", `chapter-plan/edition-30-outline.md:19`), which is how the register's hourly tables are built (C087, C095). The two disagree for most beats: 04:11 is hour 4 in the notes and hour five in the outline; 15:02 is 15 and sixteen; 01:08 is 1 and two; 02:16 is 2 and three. The margin must use one; the outline's clock hours match the register, so the notes should follow it. The outline's own table is right throughout on its own scheme (hours checked row by row).

## Findings

| Where | The text says | The record says | Evidence |
|---|---|---|---|
| `manuscript/rc2/30/01-the-creators-problem.md:46`; `manuscript/rc2/70/01-slides-as-a-compromise.md:54` | "My last request in the record has my own time on it, 18:25" | 18:25 is his last **player** request (the time in `dbd75ad`'s subject); later on the record: 18:26 in motion's session (`5d13d72`, which these chapters themselves tell) and the hold at 18:44:13 | `dbd75ad`, `5d13d72`, `867f8c2` |
| `manuscript/rc2/30/01-the-creators-problem.md:53` | "the last fixes made at his word, the last at 18:25" | 18:25 is his time in the subject; the fix landed at 18:37:02 (chapter 3's band says so) | `dbd75ad` |
| `manuscript/rc2/30/02-the-factory-is-assembled.md:32` (band `:55`) | the conductor arrives at 00:44 saying "anyone can pull the hold" | At 00:44 there was a roster and a proposed schedule; the hold any member can pull, and the schedule that ran, came at 01:39 | `97b98d9`, `09f13d5` |
| `manuscript/rc2/30/02-the-factory-is-assembled.md:104` | the first wake's card: "plan go, pre-review go, work partial ..." | The pre-review said change, then go ("pre-review change then go"); the card should show both | `c8f6f8f`; `team/conductor/wakes/20261029T021416Z.json` |
| `manuscript/rc2/30/02-the-factory-is-assembled.md:111`, `:122` | "My last request of the night was at 04:03" | At 04:03 he agreed the designer's policy (my letter 018): his last act, not a request. "My last word of the night" | `f448345` |
| `manuscript/rc2/30/03-the-factory-runs.md:55` (band `:74`) | "First" deck's review at 06:21, "Second" deck holding back its request at 04:19 | Reversed: the hold-back came at 04:19, two hours before the review at 06:21:41 | `team/deck/wakes/20261029T041822Z.json`; `aeffbf9`; `78b89b9` |
| `manuscript/rc2/30/03-the-factory-runs.md:113` | "It came to me. I kept the line in the talk, my own call", after R5 reached him at 15:02 | **Corrected 3 November, 04:40: my first reading of this row was wrong.** His decisions file does answer R5, under "The editor's answers to the researcher's pushback": "The outside is in balance: he keeps the claim." It is headed "about 15:00" but was committed at 15:16:37, after the storyteller's pass at 15:02:48; so "he had already kept it at 15:00" rests only on the file's own heading. Safest: "He kept the line, in his answers of that afternoon" | `team/conductor/briefs/2026-10-29__editor/1-editor-decisions-1500.md` (`78d517d`, 15:16:37); `b208a16`; `2726f0e` |
| `manuscript/rc2/30/03-the-factory-runs.md:133`; `chapter-plan/edition-30-outline.md:37` | studio's wake "from 17:41 to 17:47" | 17:41:15 to 17:48:21; 17:47 is its work step and `bd3cdad` | `team/studio/wakes/20261029T174115Z.json` |
| `manuscript/rc2/30/04-the-stop.md:15` | "Part 1 was final at half past six." | 18:30 was the planned lock and the time `HOLD.md` counts "unchanged since"; part 1 was last marked final at 18:20, and he moved its cut-off to 19:00 at 18:26. "Unchanged since half past six" | `team/conductor/HOLD.md`; `0ecddca`; `5d13d72` |
| `manuscript/rc2/30/04-the-stop.md:21` | "At the same moment [as the request to lock], dev was in the middle of my last fixes ... The fix landed." | Wrong order: the last fix landed at 18:37:02, before the request at 18:39:16; the conductor's plan at 18:38 notes "dev is live, last commit 18:37" | `dbd75ad`; `2ed6427`; `team/conductor/wakes/20261029T183647Z.json` |
| `manuscript/rc2/30/04-the-stop.md:90` | "the out-of-date figure reached a slide in the talk" when the freeze lifted | It did not reach the slide then: it was on the definition slide from 00:40 and never changed; the freeze lifted at 14:07 for the framing only. "Stayed on a slide" | C031; `1f7c633`; `c9ced4e` |
| `manuscript/rc2/30/05-the-factory-rebuilt-and-yours.md:65`, `:143` (band `:74`) | the limit "on the evening of 1 November"; the conductor's words "the next morning" | This team, after the day: the conductor's brief dates the limit "from about 16:30" on 1 November; the quoted words are in its brief of 2 November 00:15 and commit `9395328` at 00:06:38, the same night (`:69` says so). The editor's answer, UL1, came about 00:35 | this repository: `team/conductor/editor-briefs/2026-11-02T0015Z.json`; `9395328`; `book.json` UL1 |
| `manuscript/rc2/70/01-slides-as-a-compromise.md:54` | "My last request in the record has my own time on it, 18:25" | 18:25 is the last time in a player commit's subject (`dbd75ad`, 18:37:02); the record has a later request in his own time: 18:26 in motion's session (`5d13d72`), which the chapter itself tells at `:41`. "My last player request" | `dbd75ad`, `5d13d72` |
| `manuscript/rc2/70/02-the-tour.md:57` | "it still shows the last hold of that night" | There was one hold: `867f8c2` (18:44:13) is the only commit that adds a `HOLD.md` before `298be4e`; chapter 3 of this edition says "It was used once, at 18:44". "The hold of that night" | `git log 298be4e -- '**/HOLD.md'` |
| `manuscript/rc2/70/05-the-clock-and-one-wake.md:38` | "the conductor had changed a file outside its own page of rules" | The file was `CLAUDE.md`, the page of rules itself; it was outside the conductor's **scope** (its policy), and the commit did not name it: "agents.py flags CLAUDE.md as outside conductor scope; the editor allowed it, but the commit message never names it" | `team/conductor/wakes/20261029T021416Z.json` at `298be4e` (post_review, 02:19:05) |
| `manuscript/rc2/70/05-the-clock-and-one-wake.md:57` | "Its debrief says it in its own words" (read as the reviewer's) | The line is the conductor's debrief's ("What this does not prove"); the reviewer sub-agents wrote none. The band at `:64` has it right | `team/conductor/debriefs/2026-10-29__the-five-step-wake.md`; `c8f6f8f` |
| `manuscript/rc2/70/05-the-clock-and-one-wake.md:28` and the figure at `:46` | the reviewer "had already sent the plan back once" before its go | A caution: the order is the debrief's ("change, then go"), but the record's own timestamps run the other way: the go at 02:16:07, the change kept in its history at 02:17:00. If the figure prints the step times word for word, they will look out of order: say so beside it | `team/conductor/wakes/20261029T021416Z.json` (`steps.pre_review` 02:16:07; `history[0].pre_review` 02:17:00) |
| `chapter-plan/edition-30-outline.md:26` | "the talk, from 19:00" | 19:00 is the plan; the start is in no record (the hour label "after hour nineteen" holds) | `timeline/after-1900.md` |

## What holds

Chapter 3 of the seventy (the first files of `1f7c633`, quoted word for word; the hold from `09f13d5`); chapter 5's walk through the first wake record, every step time and verdict exact; the hold, the designer's commit 82 seconds after it, the last release; the freeze and its correction; the afternoon arrivals; the refusal scene of 2 November in this team's own record; the margin table's hours on the outline's scheme.

## Where this came from

`manuscript/rc2/`, `chapter-plan/edition-30-outline.md` at dev `772f1a9`; `timeline/`; the talk's history at `298be4e`; this repository's history for 1 and 2 November; the register (C027, C031, C087, C095).

## The seventy, part 3 (chapters 6 to 9), checked 3 November 04:19 UTC

At the writer's letter 046. Same method; one read-only checker, every finding verified by me.

| Where | The text says | The record says | Evidence |
|---|---|---|---|
| `manuscript/rc2/70/06-talking-through-git.md:30` | deck "learned to not ask", holding E02 by its own choice, and "left itself a note" | Deck's plan sent E02 at once; the pre-review asked for the change (one request in flight); deck amended and held it. The note is a `To-conductor:` trailer, not to itself. The band at `:37` is right | `team/deck/wakes/20261029T041822Z.json`; `team/deck/debriefs/2026-10-29__e01-review.md`; `aeffbf9` |
| `manuscript/rc2/70/06-talking-through-git.md:70` (band `:84`, "in full where shown") | the conductor's note to ruv-sgit | Cut short unmarked: the trailer goes on "(WAKE.md step 6: '@ruv-sgit:' or 'Agent: ruv.sgit@the-ultimate-insider')." Mark the cut | `09317d9` (10:05:48) |
| `manuscript/rc2/70/06-talking-through-git.md:76` | ruv-sgit: "Noted. Again." | Dramatised, but the record contradicts it: ruv-sgit read both notes at its 10:34 wake and its next commits still lacked the `@` and the trailer, through 13:41 | `team/ruv-sgit/wakes/20261029T103411Z.json`; `a31bd6f`, `57d24d3`, `41d4757` |
| `manuscript/rc2/70/07-the-rhythm.md:42` | "Two hours later the second version came in, and deck kept it" | v2 came in at 07:43:45, about 80 minutes after the 06:21 review; deck kept it at 08:21:46 | `cf52cda`; `eefc1d3` |
| `manuscript/rc2/70/07-the-rhythm.md:42` | "The third version came back just before I did" | v3 was delivered at 12:53:00, about an hour before he came back; deck's review of it is the one at 13:48:52, "just before". "Deck passed the third version just before I came back" | `8012b00`; `19e7f2d` |
| `manuscript/rc2/70/07-the-rhythm.md:44` | ruv-sgit: "Numbered dots, plain words, named rings. Readable, this time." | Deck's words, about v2 ("Numbered dots, plain words and named rings make it readable"), given here to ruv-sgit after v3 | `team/deck/debriefs/2026-10-29__e02-v2-review.md` |
| `manuscript/rc2/70/09-the-loop-and-the-port.md:59` | "the record has no answer of mine to the objection itself"; "I had already kept the line, two minutes before" | He answered R5 in his decisions file ("he keeps the claim"); its 15:00 is the heading, its commit 15:16:37, after 15:02:48. This came from my own wrong row above, now corrected | `78d517d`; `b208a16` |
| `manuscript/rc2/70/09-the-loop-and-the-port.md:51` | the outside "is more mature than its inside" | R5's claim compares the surface with itself over time ("smaller and more mature than it was"), not with the inside; the storyteller's line was "the outside is in balance" | `2726f0e` (story-r5-surface-smaller-more-mature); `b208a16` |

`08-the-plumbing.md`: no findings; its corrections file did say "None yet." at `298be4e` (touched only by `1f7c633`), while `REALITY.md` changed all day, last at 17:42:40 (`70d4981`). For its open "to trace": the gate refused a release in the night, at 01:19: dev "added the banner rule ... because the gate the conductor added at the editor's rule refused the release without it" (`24da366`; `team/dev/debriefs/2026-10-29__the-board.md`); the banners check came at 00:53:45 (`a3a4807`). "Creator" (the heading of chapter 9) is the editor's own word in PS1, not one of RW1's.

## The seventy, part 4 (chapters 10 to 12), checked 3 November 05:19 UTC

At the writer's letter 051. Every quoted word of the hold file and of the designer's commit in chapter 10 matches the record; the order of 18:36, 18:37, 18:39 and 18:44 holds. Chapter 11: no findings.

| Where | The text says | The record says | Evidence |
|---|---|---|---|
| `manuscript/rc2/70/12-how-do-we-contain-this.md:39` (band `:50`) | "The conductor said so at two in the morning, in its first debrief" | The words and the time are right, but it is not the conductor's first debrief: four came before (00:59, 01:09, 01:27, 01:35). "In its debrief of the first five-step wake" | `b3ee324`, `31b0f86`, `02cbd86`, `ecc048e`, `c8f6f8f` |
| `manuscript/rc2/70/12-how-do-we-contain-this.md:5` | "My talk that evening ... I gave it with a factory of agents behind me" | That it was given rests on the talk as given, `a9c0b49`, added after the day; the chapter and its sources should say so | `timeline/after-1900.md`; `timeline/after-the-day.md`; C100 |
| `manuscript/rc2/70/10-the-last-ten-minutes.md:3` | "Security's chair, planned at midnight" | Minor: its page was written at 00:51:12, in the first hour (chapter 12 says so) | `17b287b` |
| `manuscript/rc2/70/10-the-last-ten-minutes.md:19` | "unchanged since half past six, the time planned for its lock" | Holds, but incomplete: at 18:26 he moved part 1's cut-off to 19:00 (motion's `5d13d72`, 18:29), before the conductor's 18:36 wake still worked to 18:30. Worth a clause | `5d13d72`; `3342cff` |

## The seventy, part 5 (chapters 13 to 16), checked 3 November 06:18 UTC

At the writer's letter 057. Chapters 13 to 16 tell mostly this book's own team; they are checked against this repository's files and history (my clone's history starts on 30 October about 10:28 UTC). The quoted lines of the storyteller's handover are word for word. Chapter 16: no findings.

| Where | The text says | The record says | Evidence |
|---|---|---|---|
| `manuscript/rc2/70/13-sessions-end.md:9` | "That night the factory was taken apart. The sessions went" | To `298be4e` the record shows the hold at 18:44:13, never lifted that day, and no commit from 18:48 to the merge at 23:19; nothing records sessions ended or the team taken apart that night. Told as an event the record does not hold | `867f8c2`; `team/conductor/HOLD.md`; `timeline/after-1900.md`; C024 |
| `manuscript/rc2/70/13-sessions-end.md:22` | the 95% "was just a footnote" | His words: "it's an interesting point, but it's just a footnote"; "was" is inside the quote marks but not his | `briefs/2026-10-31__rc1-paper-review/batch-07-pages-22-to-32.md` (`49c701e`); C089 |
| `manuscript/rc2/70/13-sessions-end.md:31` | the handover written "at about 11:45 UTC" | The quote matches the file, but the file was committed at 11:03:47, so it was not written at 11:45; mark the time as the handover's own, or drop it (my own handover carries the same line) | `cfcc2951` |
| `manuscript/rc2/70/13-sessions-end.md:39` | the new storyteller session calls the old one's letters "yesterday's" | Same day: the old session ran 30 October from 01:41 to 13:02 UTC, the new began at 13:02 | `team/storyteller/sessions/*/SESSION.json`; `444d5323` |
| `manuscript/rc2/70/14-the-second-factory-and-the-third.md:117` | "The line you read in chapter 1 is the corrected one" | In this edition chapter 1 has no such line; it is the thirty's chapter 1 (`manuscript/rc2/30/01-the-creators-problem.md:82`); here the subject is chapter 3, "The brake, made that night" | `fde3fea`; `58322a27` |
| `manuscript/rc2/70/15-principles.md:21` | the hold "was used once, sixteen minutes before the talk" | The plan as the event again: "before the talk was due" | C100; `timeline/after-1900.md` |
| `manuscript/rc2/70/15-principles.md:9` | "Before any agent did anything, there was a brief and a page of rules" | Both arrived in dev's own first commit at 00:40, with the site and the talk; the empty repository held neither. "With the first agent came a brief and a page of rules" | `1f7c633`; `2e4b1f4` |

## The full book (150), chapters 2 and 3: one ask followed in full, and the tour's stops, 3 November 09:18 UTC

At the writer's letter 070.

### One afternoon ask, from his words to the commit

**"When in doubt, add it" (17:27).**

| Step | When (UTC) | Who | The record |
|---|---|---|---|
| He says it | 17:27 | the editor, in the conductor's session | "since we don't have a lot of time, can you ask the deck agent put those new materials created by the other agents in the deck, apart from the ones that I then chose not to include. So when in doubt add it." (`team/conductor/briefs/2026-10-29__editor/7-when-in-doubt-add-it-1727.md`) |
| Routed | 17:29:41 | conductor | Brief 7 and mail 066 to deck, with the first gap list (the studio ports, the SHarness pieces, six explainer pages); the conductor to rerun the sweep at every follow-up and mail only what is new: "Deck places; it does not search" (`a618b29`) |
| Done | 17:52:15 | deck | "part 1 final for its lock ... every other new piece into parts 2 and 3"; part 2 gains the B01 overlap, the journey, the team's own policies, the PKI showcase; part 3 the SHarness series; the commit quotes him: "The editor, 17:27: when in doubt, add it." (`b1c9bab`). No deck wake record covers this commit: deck's last closed at 17:27:22 and its next opened at 18:20:09 |
| Checked | 18:15:31 | storyteller | Parts 2 and 3 checked before their locks: "the blast-radius piece the editor named is in no beat" (`e8c0fbb`): one piece still missing, sent to deck |
| Seen again | (no record) | the editor | The record does not show him looking at the placements; from 18:04 he was fixing the player in dev's session, and part 1 was the part he played. Say "the record does not show when I saw it" |

From word to commit: 25 minutes, through two agents, and the check found one gap. It is a good case for chapter 2 because each hand-off is on the record, and so is the one place it fell short.

### The tour's stops (150/03)

| Where | The text says | The record says | Evidence |
|---|---|---|---|
| `manuscript/rc2/150/03-the-tour-at-length.md:112` | the home page given to dev, `5a91607` (16:06) | Dev made the home page in its first pass at 00:40 (`1f7c633`); `5a91607` at 16:06:50 changed its words ("the home page says the perfect storm"). Cite both, or say "dev's home page, its words of 16:06" | `1f7c633`; `5a91607` |
| `manuscript/rc2/150/03-the-tour-at-length.md:167` | the policy review page given to studio, `bd3cdad` | Right: the page first appears in `bd3cdad` at 17:47:28 | `bd3cdad` |
| `manuscript/rc2/150/03-the-tour-at-length.md:211` | the night's brief given to the conductor, `648feee` (03:10) | The conductor's, but first written at 02:57:23 (`c531560`), then edited at 03:05 and 03:10 (`648feee`, "dev's two new asks scheduled") | `c531560`, `8543269`, `648feee` |
