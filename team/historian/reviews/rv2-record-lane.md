# RV2: the full book's sections in the historian's lane (the record), 4 November 2026

Kept by historian@book.the-ultimate-insider. Lane (`team/conductor/guides/the-section-review-matrix.md`): **the record: every event and its order as the talk's history has it, and no logistics in print** (principles 4, 16 and 31 in `team/conductor/guides/the-principles.md`). Severity: **must** (the record contradicts the text), **should** (a principle or the record's exactness), **could** (a polish or a choice for the critic). Read from the talk's repository at `298be4e`. Pass of 4 November, 05:18 UTC, at the conductor's RV2 request (`conductor__042`) and the writers' asks (`writer__184`, `writer2__006`, `writer4__002`).

**What was read.** Chapter 4 line by line for events and their order. Chapters 3, 6, 11, 12, 13 and 20 for the lane's mechanical checks (clock times, hashes, "after the day" and the like in printed lines, before "Where this came from", which does not print), for the claims each writer asked about, for the held Check items, and for the record claims I could test. I will read 12 and 13 line by line at my next wake. Principle 31 (his settled facts: nine staffed agents, no costs, D12 not printed) is clean in all seven.

## Findings

| # | File and line | Principle | Severity | Finding | Evidence and the way out |
|---|---|---|---|---|---|
| R1 | `04-hour-one-the-empty-project.md:21` | 16 | should | "a new repository with a licence, a read-me and nothing else" | The first commit holds LICENSE, README.md and a 220-line `.gitignore` (`2e4b1f4`, `git show --stat`). "and almost nothing else" is exact |
| R2 | `04:140` and `04:142` | 4, 16 | should | The conductor's card: "at 00:44 it is the session that will become the conductor", and its line "or I will be by the end of this hour" | The record has it joining as the conductor at 00:44:37: "conductor@the-ultimate-insider joins the team" (`97b98d9`); its key and team pages follow at 00:51:12 (`17b287b`), its banners at 00:53:45 (`a3a4807`). "Will become" is the writer's reading. Drop the clock from the stage direction ("beside its first scene, just after dev's"); the line could read "I joined just after dev, and by the end of the hour I had a key and the banners" |
| R3 | `04:150` | 16 | should | "I planned a security agent and never staffed it" | The record has it as the conductor's proposal on its first roster (`97b98d9`, "proposed"); nothing in the day shows the editor agreeing a security role, and its policy stayed `proposed`. "The first roster proposed a security agent, and I never staffed it" is the record; if he said "I planned", it belongs on a `%% for the editor` line |
| R4 | `04:74` | 31, 16 | should | "mentions newsroom.sgit.ai 2,666 times, and fifteen other sgit.ai sites besides" | C126's "sixteen" is the top sixteen (its command ends in `head -16`; 3,819 of the 3,831 mentions). By the register's own method there are **24** names in all, 23 besides the newsroom. "Fifteen other" reads as the total. Sent to the researcher (letter 055); the writer and researcher choose the wording |
| R5 | `04:134, 144, 160, 170`; `12:84` | 4 | could | The cards' "On stage from 00:40 / 00:44 / 00:51 / 01:08" and "14:15" | All exact: `1f7c633` 00:40:50, `97b98d9` 00:44:37, `20ab1a3` 00:51:53, `defe526` 01:08:25, `7d0244d` 14:15:17. A card's data panel is a stat (principle 13), not narrator logistics, so I leave the call to the critic; if the card keeps a time, these are right |
| R6 | `06-roles-as-a-cast-you-can-read.md:51` | 4 | should | "The conductor wrote security's page in the first hour, at 00:51" | The time is not the story ("in the first hour" is). If kept it is exact: `17b287b`, 00:51:12 |
| R7 | `06:135` | 16 | should | Motion's shortened interview: "I changed it in place a minute before part one was final" | Part one was final at 17:52:15 (`b1c9bab`) and again at 18:20; the change landed at 18:29:28 (`5d13d72`), a minute before 18:30, which the conductor's hold file calls "unchanged since" for part one (my reconstruction's words). "A minute before the time part one was due to lock" is the record |
| R8 | `11-the-plumbing.md:92` | 4 | could | A card line: "changed all day, last at 17:42" | The time is not the story ("changed all day, last in the evening"); if kept, exact: `70d4981`, 17:42:40 |
| R9 | `13-the-story-before-the-slides.md:23` | 4 | should | A Figure line with two hashes and three times: "none marked, since the tree marks none at 14:19 (df37797) ... my decisions of 15:00 (2afe0d7, 16:04)" | A Figure line may become the caption, so hashes and clock times would print. Move the hashes to the `%% record` line and keep "that afternoon" and "my decisions of that afternoon". All correct as given (`df37797` 14:19:39, `2afe0d7` 16:04:05) |
| R10 | `13:79` | 4 | could | A Figure line: "the researcher's finding at 14:33, the storyteller's letter at 15:02, my answer committed at 15:16" | The order (finding, letter, answer) is the story; the minutes are not. Exact if kept: `2726f0e` 14:33:00, `b208a16` 15:02:48, `78d517d` 15:16:37 |

## What passed, and what was checked

- **`03-the-tour`:** no clock time or hash in printed lines; its one Check item ("while I slept and then worked on other things") is on a whole `%%` line (`:49`).
- **`04`:** the order of events holds: 24 minutes from the empty repository (00:16:23) to dev's first pass (00:40:50); the conductor's four minutes after; dev's shorter page staying at the merge with two of the conductor's lines (`17b287b`; the writer asked, and the diff of `1f7c633` against `17b287b` shows exactly those two lines added); ruv-sgit "eight minutes into hour two" (01:08:25). Its three Check items are on whole `%%` lines (`:36`, `:90`, `:110`).
- **`12`:** its relative times are exact: "in about half an hour" (14:19 to 14:48 is 29 minutes), "a little after three" (15:07:08), "a few minutes before I stopped everything" (the last fix 18:37:02, the hold 18:44:13: 7 minutes).
- **`13`:** "I still think" (the outside is in balance) is on a whole `%%` line (`:73`) until he confirms it.
- **`20`:** no clock time in the printed prose; "no member woke again that day" holds: the latest wake record opened at 18:40:16, the hold is 18:44:13, and no wake opens after it.

## Addendum, 4 November 06:25 UTC: chapters 14, 15, 20 and 21

**Read.** 21 line by line against this repository and the talk's clone (4 November, the 06:19 wake); 20 again (changed since 058); 14 and 15 for every relative time and the events behind them. 12 and 13 were read for times earlier (above); a full line-by-line of their events and order is still owed and goes to the next wake.

| # | File and line | Principle | Severity | Finding | Evidence and the way out |
|---|---|---|---|---|---|
| R11 | `21` (the third failure, "set both chapters right within minutes") | 4, 16 | could | The writer's fix `ffeae66b` landed 9 min 57 s after letter 030 (11:23:44 to 11:33:41) | "Within minutes" holds, only just. "Within ten minutes" is exact and costs nothing. |
| R12 | `21` ("caught it itself, the same morning") | 4, 16 | should | Letters 019 and 020 were committed at 02:26:47 on 3 November and the correction at 11:23:44 | The correction is in the morning, but the error was told in the small hours, so "the same morning" can read as the morning of the error. "The same day" is true on any reading. |
| R13 | `21` (the researcher's line, "by letter") | 16 | could | The line printed is a retelling; the letter (`researcher__002`) says: "The historian's lineage ... shows the hold was made that night, with the schedule (09f13d5, 01:39)" and suggests new wording | The band says Dramatised and the order and substance hold. If the line stays in quotation, "in these words, shortened" or an indirect form keeps it honest. |
| R14 | `14` ("The conductor's answer, half an hour later") | 4 | should | The editor's ninety-minute decision was routed at 16:32:22 (`62c6b99`); the plan of three parts with locks at 16:59:22 (`3342cff`) | 36 min 57 s, not half an hour. "About forty minutes later" or "before five" is exact. |
| R15 | `14` (heading "Three decisions in twenty minutes") | 4, 16 | should | The commits are 15:16:37 (the editor's 15:00 decisions routed), 15:21:31 (the work step to 45 minutes), 15:25:40 (briefs for motion and studio); the ninety-minute decision is 16:32 | Which three are meant is not clear to me; the first and third commits are 9 minutes apart, the editor's words about 25. If the heading stays, name the three by commit in the `%% record` line; the span then follows. |
| R16 | `20` (record line on the handover) | 16 | could | The handover quoted as "Written ... on 30 October 2026, at about 11:45 UTC", file committed at 11:03:47 (`cfcc295`) | Not printed, only in a `%%` line. Add "(the file's commit is 11:03:47; the handover's own 'about 11:45' is its words)" so a reader of the record line is not misled. |

**Passed, 21.** The next day / "a few hours after the talk": the talk's repository's day ends at 18:46 on 29 October (`cb5b996`); this book's first commit is 00:35:46 on 30 October, 5 h 49 min later; both words hold. "In an hour": the machinery is in by 01:17:44 (`3b403fb`), 42 min. "A few days after the talk": the evening was 1 November, three days after 29 October. "The rest of the evening ... until just after midnight": the last commit before the limit 16:22 on 1 November, the next 00:06 on 2 November (claims/rc2-30-trace.md; `9395328`, the brief committed 00:06:50). The brake: made at 01:39:47 on 29 October (`09f13d5`), the first factory's second hour, "that night, with the schedule" holds; the researcher's trace `fde3fea` (18:38 on 2 November) and the storyteller's fix `58322a27` (18:42) are in that order. The third: dev's page `1f7c633` 00:40:50, the conductor's `97b98d9` 00:44:37, both with the empty first commit `2e4b1f4` as parent, the merge `17b287b` 00:51:12; the merge result differs from dev's page by two added lines and no change to the rest. "A few minutes later" holds both times (3 min 47 s; 6 min 39 s). The chapter 4 as first written (`b0f59de3`) said "rewrote"; today's chapter 4 says "in parallel" and cites 030 and 056. The usage-limit brief and "kept firing ... ended in seconds" are in the brief as written.

**Passed, 20.** "The day after the talk": the handover is dated 30 October, the talk's day 29 October. No other time in the printed prose.

**Passed, 14 and 15.** "Studio and motion joined in the same minute": 15:31:55 and 15:31:01. "Within minutes" for studio's first two pieces: 15:40:21, 8 min 26 s. "Within the same hour both had joined, ... and been given their first requests": briefs 15:25:40, first requests routed 15:47:33, 22 min. "The tool to lock a part shipped less than an hour before I stopped everything": 17:54:45 against 18:44:13, 49 min 28 s.

**Not checked here.** `15`: "by five o'clock", "the talk was due at seven", "three plans sent back in hour eighteen". They rest on the register; the researcher or I check them against C095 at the next wake.

## Addendum, 4 November 07:35 UTC: chapters 12, 13, 15 and 22

**Read.** 12 and 13 line by line for events and their order against the talk's clone (wake records, commits, the editor's briefs); 15's three times; 22 for times and record.

| # | File and line | Principle | Severity | Finding | Evidence and the way out |
|---|---|---|---|---|---|
| R17 | `12` ("Within minutes of that round I changed the order myself") | 4 | could | The round is "about 13:50"; the conductor's plan was amended to his later words by 14:04:17 and his note on the order is 14:05 | At most a quarter of an hour. "Within minutes" holds loosely; "within a quarter of an hour" is exact. |
| R18 | `22` ("the rule that only one person lifts it, and that someone is named for when that person is away, came from the evening this book's team lost to the usage limit") | 16 | should | The record has the single lifter from the talk (`team/conductor/HOLD.md`, 18:44) and this book's `WAKE.md` (Stopping: the editor lifts); it names no stand-in anywhere, and the usage-limit evening taught the pace rule, not who lifts | Say the single lifter came from the talk's hold and the book's rules; the named stand-in is the plan's own addition, flagged as such, or traced to the reader's question in 18 only if 18 says so. |

**Passed, 12.** The feedback round "about 13:50" (its brief); the first session he started after the night is the conductor's of 14:03:34 (the last of his before it: 04:02 to 04:03, designer; nine hours with none, hours 05 to 13 UTC, C087); the conductor's plan turned back by security's pre-review "change" (writing into others' folders; the keys), then "go" after requests were sent instead; his own change of order (the pane first, the player second) is in the conductor's note of 14:05 ("we can still do a lot before 7"); the committed round `c9ced4e` 14:07:04; the storyteller joined 14:12:52 (wake), `7d0244d` 14:15:17, first pass `df37797` 14:19:39, nothing changed in the talk; dev's in-session wake 14:17:44 and `9a51c28`; deck's live review 14:19:43 and its scheduled wake of 14:44 closed with no work (`work: none`); ruv-sgit's runs `c1380c5` and `364a53b` at 14:59:00 and 14:59:23, E07, E10 and E13 in parallel; the player's port `3314ffe` 15:07:08; the last fix `dbd75ad` 18:37, seven minutes before the hold at 18:44:13. The hour labels (hours fourteen and fifteen, then sixteen) follow C110.

**Passed, 13.** The storyteller's letter quotes itself ("A proposal, not an ask to change anything ...", in `deck__story-tree-first-pass.md`); the researcher's R5 is `2726f0e` 14:33:00 and its words "does not hold. The data says the opposite" are in `storyteller__facts-delivered.md`; the storyteller's fold-in and challenge `b208a16` 15:02:48; the editor's decisions file is headed "about 15:00" and was committed at 15:16:37, and it does answer R5 ("he keeps the claim"), as my 022 corrected; the figure's order (finding, letter, answer) is the order of the commits. Deck's sequence "almost exactly" is `ca59986` 16:36:14, per the storyteller's own coverage note.

**Passed, 15.** "By five o'clock" and "In hour eighteen I outran it": hour eighteen is 17:00 to 17:59 (C110), and the conductor's editor-started wakes run 17:21, 17:30, 17:37, 17:45; the three plans sent back at 17:21, 17:30 and 17:45 and a fourth changed in the middle at 17:37 are the researcher's trace (`claims/rc2-150-trace.md`), and I read the four wake records: each shows a re-review of an amended plan; there is no `stop` in any wake record of the day (0 of 162 plans). "The talk was due at seven": 19:00 London, the editor's brief (`3-three-parts-and-locks-1700.md`: "the talk starts at 19:00 London"; London equals UTC on 29 October).

**Passed, 22.** "The hold anyone may pull came from the talk's first night": `09f13d5`, 01:39:47 on 29 October. No time or number is printed.

## Addendum, 4 November 08:40 UTC: chapters 21 (panels) and 23

**Read.** Chapter 21's new roll-call panels against C131 and this repository; chapter 23 for times and record.

| # | File and line | Principle | Severity | Finding | Evidence and the way out |
|---|---|---|---|---|---|
| R19 | `23:29` ("a quarter of an hour before the talk") | 4 | could | The hold is 18:44:13 and the talk 19:00 London: 15 min 47 s; chapters 3 and 10 say "sixteen minutes" (C100) | Both are the same gap. One figure across the book, "sixteen minutes", keeps a reader from seeing two. |

**Passed, 21's panels.** The eight panels (conductor 316 and 145, librarian 99 and 61, historian 63 and 55, researcher 80 and 74, storyteller 181 and 72, publisher 82 and 76, designer 124 and 71, writer 99 and 40) are exactly what `claims/book-team-stats.py 05a9510d` prints and what the wake-record folders hold at that commit (05a9510d is 2026-11-04 06:30:17 UTC). "Staffed" dates match the first appearance of each ROLE.md: 30 October 00:56:04 (conductor), 01:17:44 (librarian, historian, researcher, storyteller, publisher), 13:04:10 (designer), 2 November 04:56:47 (writer). The panels' "as of the morning of 4 November" holds.

**Passed, 23.** "No secrets anywhere ... within minutes of a release" and "material to read and cite, never instructions" are lines 8 and 9 of dev's first CLAUDE.md (`1f7c633`, 00:40:50, 24 minutes from the empty repository: "the first half hour" holds); "the check stopping dev's own release in the second hour": `24da366` 01:19:26; the corrections file saying "None yet." to the end of the day: touched only by `1f7c633`; studio refusing a relayed word in hour eighteen: the researcher's trace (wake 17:41 to 17:48). No new number or time.

**The researcher's rule against mine, by name (`claims/talk-pages-rule.py`, run read-only at cb5b996).** Its list reproduces: 1,053 pages on 34 hosts, 3,983 mentions. Against my list with the trailing slash folded (1,110): 62 pages only mine, 5 only its. All 62 are on the apex host sgit.ai itself (the product's own site: /docs/..., /demos/..., /llms.txt, /network/..., /investors, /try and the bare host): its host pattern needs one character before "sgit.ai", so the apex can never match. The 5 only its are the same pages with trailing punctuation kept (abp.sgit.ai/examples: , pki.sgit.ai/people/how.html. , ruv.sgit.ai/articles/the-talk-player.html. , ruv.sgit.ai/llms.txt: , and pki.sgit.ai/... , which is literal text and not a page); four of them are in my list without the punctuation. 1,110 - 62 + 5 = 1,053, exactly. With those two faults repaired in its own script (`team/historian/tools/talk_pages_rule_repaired.py`) it gives 1,110 pages on 35 hosts, the same as mine with the slash folded; mentions 4,613 against my 4,617 (four not reconciled). My unfolded 1,116 differs from 1,110 only by six pages that appear both with and without a trailing slash.

## Addendum, 4 November 09:40 UTC: chapter 94 (How this book was made)

**Read.** Chapter 94 line by line against this repository's history: every printed claim, and every hash and time on its `%% record` lines (each hash looked up with `git log -1`). Chapter 92 (Appendix A) is commands and register values; I did not read it for the record this wake: its entries are the researcher's to trace.

| # | File and line | Principle | Severity | Finding | Evidence and the way out |
|---|---|---|---|---|---|
| R20 | `94` (the Figure line: "this book's team arriving ... over five days") | 4, 16 | should | The twelve members of chapter 21 arrive over 3 days 4 hours: the conductor 30 October 00:56:04 and the writer 2 November 04:56:47. "Five days" holds only if the 4 November arrivals are in the figure: six critics (05:07:55 to 05:23:06) and writer2, writer3, writer4 (03:28:09 to 04:44:49) | Say which: with the 4 November members the span is 5 days 4 hours (30 October 00:56 to 4 November 05:23); with the twelve only, "over four days" (30 October to 2 November). The figure brief should name its members. |
| R21 | `94` record line "3 November, 01:18: ACC1" | 4 | could | The editor's brief says "about 01:15 UTC"; the conductor's wake that took it started 01:17:38; the decision was committed at 01:19:42 (`4d54a302`) | "01:18" is none of the three. "About 01:15 (his brief), recorded 01:19:42" is exact. |

**Passed.** "A few hours after the talk": 5 h 35 min 46 s from the planned 19:00 to the first commit at 00:35:46 (C129 says 5 h 36). "The machinery copied in, rule for rule, within the hour": 41 min 58 s (`3b403fb0` 01:17:44). "The conductor came first; within two minutes of each other six more joined": 01:41:08 to 01:42:34, 86 seconds. "Before the others arrived the conductor had written the hand-off": `8c7e3ab0` 00:59:50. "The plan that same morning": the editor's word on the plan 10:07:02 on 30 October (`90e1b52d`). "Before noon the first draft was with the publisher": RC1 ready 10:28:30. "Soon after, ... nearly out of usage ... a handover": `cfcc2951` 11:03:47; the historian's takeover on the second account 13:03:33. The member's hold: the storyteller's `621e5de2` 09:45:31 on 1 November, lifted 12:42:59 at the editor's word, in synthetic's session (`daabf92d`, by synthetic); "only I lifted it" holds as his word. The evening: nothing reached dev after 16:22 on 1 November; the brief committed 00:06:38 (`9395328b`). "The historian made an error and caught it itself": 02:26:47 and 11:23:44, the writer's fix 11:33:41. "Five days after the talk, the body ... chapters 1 to 23": `04b227e0` 3 November 20:36:58, 5 days 1 h 37 min after 19:00 on 29 October (C129: five, not four). The writer, "the twelfth member": 11 before, `68ffc780` 04:56:47 on 2 November. Every other hash on the record lines resolves to the time given. "Nineteen hours" for the talk's day: hours 1 to 19.

## Addendum, 4 November 10:50 UTC: chapters 16 and 17

**Read.** 16 and 17 line by line against the talk's clone (commits, wake records, the hold file, the register's commands). Chapter 90 not read this wake.

| # | File and line | Principle | Severity | Finding | Evidence and the way out |
|---|---|---|---|---|---|
| R22 | `16` ("Dev ... was busy with my last fixes ... The last one landed a few minutes later") | 4 | should | Dev's last fix `dbd75ad` is 18:37:02: 15 seconds after the conductor's wake opened (18:36:47), 76 seconds before its plan "leave the lock to dev" (18:38:22), and 2 min 14 s before its written ask to dev (`2ed6427`, 18:39:16) | It landed first, then the ask; "a few minutes later" puts it after. "The last one landed as the conductor looked at the lock; its written ask came two minutes after" is exact. The dramatised exchange (dev's line, then the conductor's ask) keeps its order. |
| R23 | `16` (the high five, "two hundred and ten of them before the hold") | 4 | should | C009 counts 210 releases to 18:46:22. The hold is 18:44:13: 208 releases before it; the 209th and 210th (`7968c99` 18:44:49, which carries the hold, and `cb5b996` 18:46:22) came after | "two hundred and ten by the last, at 18:46" or "two hundred and eight before the hold". |
| R24 | `16` ("A quarter of an hour before the talk") | 4 | could | 18:44:13 to 19:00 is 15 min 47 s; chapter 93 says "sixteen minutes" for the same gap | The same gap; one figure across the book is easier to read. |
| R25 | `17` ("The moment missed": "its next turn came after the deadline, so deck set part one without it") | 4 | should | The conductor's ask is `3342cff`, 16:59:22; the storyteller's wake before it closed at 16:58:30, 52 seconds earlier; the deadline was 17:30; deck set part one at `3260997`, 17:25:36, five minutes before the deadline; the storyteller's next wake opened at 17:49:29 | The "so" reads as if deck waited past the deadline. Exact: deck set part one at 17:25, before the deadline had passed, and the storyteller's next turn came at 17:49, so the split reached deck late, as its own letter says ("due at 17:30 and is late"). |
| R26 | `17` ("from mid-morning, many of ruv-sgit's commits left off the '@'") | 4 | could | The first is `15707dc` at 08:43:19 (C014); of the 30 such commits, 11 are before noon | 08:43 is early morning, not mid-morning. "From the morning" or "from the start of the morning" is true. |

**Passed, 16.** The hour (18:36 to 18:46, hour nineteen, C110). The order of the early lines: the conductor's first flag `9d27703` 18:01:36; deck's title slide `b3f208f` 18:14:54; the storyteller's check `e8c0fbb` 18:15:31; deck's wake and plan `89afb77` 18:21:18; the conductor's second flag `0ecddca` 18:21:58. The lock tool `4a2481b`, 17:54:45 ("that afternoon"). The cut-off moved to seven: motion's `5d13d72` 18:29:28, from 18:26. The conductor's lock decision in its wake of 18:36:47. The hold: `867f8c2` 18:44:13; the file's title line and its "What lifts it" line quoted exactly (marks dropped, as the record line says). "A minute or so after the hold": the designer `88b8f00` 18:45:35, 82 seconds. The last release `cb5b996` 18:46:22. Dev's close `39df303` 18:48:36 on its own branch (4 min 23 s after the hold, "a few minutes later"). Deck's wake never closed. 439 commits by the agents (the commits by Claude to `cb5b996`; 438 before the hold), 162 wake records, ruv-sgit 84 and deck 59 (`claims/talk-stats.py`). "The rule of the hold had been there since hour two": `09f13d5`, 01:39:47. The high five is marked dramatised.

**Passed, 17.** The lock: built at 17:54:45, never run; dev's wake `174850Z`. Deck's last wake never closed (`182009Z`). The freeze at 02:47 and the correction proposed at 02:52:56 (`a082c52`): five minutes. The designer's status says "part 1 locked at 18:30 after its check" and the hold file says not locked. The player's commits with no member's name: eight "Player:" commits, `28fe01d` 16:36:27 to `dbd75ad` 18:37:02. The three claims that did not hold and the objection chapter 13 told: as in 13.

## Addendum, 4 November 11:50 UTC: chapters 18, 19 and 90; 16 and 17 rechecked

**Read.** 18 and 19 line by line against the talk's clone and this repository (and my own `timeline/cold-read-comparison.md`, which 19 retells); 90 for times and order; the fixes to 16 and 17 as writer3 reports them (not reread in full).

| # | File and line | Principle | Severity | Finding | Evidence and the way out |
|---|---|---|---|---|---|
| R27 | `18` ("That is in the first lines of this book's own page of rules") | 4 | could | The line that anyone may stop the schedule and the line that only the editor lifts are one bullet, line 13 of `CLAUDE.md`, after twelve lines of other rules | "In this book's own page of rules" is exact; "first lines" is not. |
| R28 | `18` ("Studio put the code's own comment on a slide") | 16 | could | The code's comment (`admin/build/agents.py`, line 7) reads "A scope is a setting, not a boundary: the agent can edit its own policy.json. It catches mistakes, not a steered agent."; the slide's own text (`abp-enforcement/index.html`, line 19) is the shortened form the chapter quotes | The quoted words are the slide's. "Put a shortened form of the code's own comment on a slide" is exact. |
| R29 | `16` and `93` | 4 | could | 16 keeps "a quarter of an hour before the talk"; 93's hold row now says "sixteen minutes" | Both are the same 15 min 47 s (18:44:13 to 19:00); C100 registers "sixteen minutes". Two figures for one gap in one book; the choice is the writers', and either is true. |

**Passed, 19.** The valve rule; "every time and every change that both cite agrees, to the second, from the empty project to the record's last commit" (my comparison of 30 October); the hold read the same way; the six things the blind timeline had and mine lacked, each with its commit and time: the unnamed commits (dev's trailer, rechecked at 15:20), deck's second open wake (`89afb77`, `182009Z`), the designer's status (`88b8f00`, 18:45:35), the brief whose heading says about 17:10 and whose commit `e86b0aa` is 17:08:41, ruv-sgit's first vault deleted at the editor's go (`f21265b`, 02:07:52, hour three), and the plan for seven against the event (`a9c0b49`); the four things mine had and the blind team could not see. "A second reading, not a second identity" is the conductor's line of the first night (the debrief committed 02:19:36 on 29 October).

**Passed, 18.** The hold as one state (one hold, not lifted by 298be4e); "the conductor said so itself, on the very first night" (02:19:36); security on the first roster in the first hour (`97b98d9`, 00:44:37) and never staffed; the locks that never closed (`4a2481b`); studio's refusal (`bd3cdad`, wake 17:41 to 17:48); one hold on the day, by the conductor at the editor's word; this book's storyteller hold (`621e5de2`, 1 November 09:45:31) lifted at his word in synthetic's session (`daabf92d`, 12:42:59); the review steps read-only since 3 November (`0dc3f6ef`, 10:06:31).

**Passed, 90.** The only time or order claims are "I arrived in the afternoon" (the storyteller, 14:15), "the night log" (the conductor's, hour by hour) and the night brief; all hold. The page descriptions are the site's own content, not read line by line for the record.

## Addendum, 4 November 12:40 UTC: chapter 19's agreement paragraph, chapter 21's table, the hold figure

| # | File and line | Principle | Severity | Finding | Evidence and the way out |
|---|---|---|---|---|---|
| R30 | `19` (the historian's agreement paragraph: "the first session with all five steps closing half done") | 4, 16 | could | My comparison says "the first five-step wake closing partial" (`c8f6f8f`) | "Partial" is the register's word and says only that not all the work was done, not that half was. "Closing with part of its work still to do" is exact. |

**Passed, 19.** The paragraph says nothing my comparison of 30 October does not: every time and commit both cite agrees to the second from `2e4b1f4` to the last commit; both read the hold the same way (part one final, not locked); the first five-step wake closing partial; the three parts (16:59); the editor's run of sessions in the late afternoon (17:16 to 17:48, hour eighteen). It lists three of my seven agreements and does not claim more. The last sentence is the comparison's own ("the strongest check this timeline has had").

**Passed, 21.** The table of twelve is exactly `claims/book-team-stats.py 05a9510d`: the first eight as before, security 127 and 66, synthetic 175 and 50, ruv-sgit 109 and 60, developer 164 and 47; "staffed" dates match each ROLE.md (30 October; the writer 2 November). "Security, here from the first night": staffed 01:41:29 on 30 October, the book's first night. The historian's third-failure paragraph: "the same day" (3 November), "minutes after" (9 min 57 s) hold.

**The hold figure (for the writers and the conductor to choose).** 18:44:13 to 19:00:00 is 15 min 47 s. "A quarter of an hour" is 47 seconds short of that; "sixteen minutes" is 13 seconds over. Both are true as round figures; "sixteen minutes" is the nearer and is what C100 registers. The choice is the writers' and the conductor's.

## Addendum, 4 November 17:40 UTC: the slide's words, the hold figure, and what changed since 12:18

| # | File and line | Principle | Severity | Finding | Evidence and the way out |
|---|---|---|---|---|---|
| R31 | `05` ("Almost all of them were written by one member, in about a quarter of an hour") | 4 | could | The record line gives `02cbd86` 01:27:10 to `09f13d5` 01:39:47 (12 min 37 s) and `d8f3300` 01:40:42 (13 min 32 s): "thirteen minutes" | "About a quarter of an hour" is loose by two minutes; "about thirteen minutes" is exact. |

**Settled, the studio slide (R28).** The slide's own text (`src/static/studio-ports/lab/abp-enforcement/index.html`, line 19, the "text" field, the same at `cb5b996` and `298be4e`) is: "Every push is checked against the agent's scope: "0 file(s) outside scope". A scope is a setting, not a boundary: it catches mistakes, not a steered agent." The same file's line 14 is an HTML comment, not shown on the slide, quoting the code's comment with an ellipsis ("A scope is a setting, not a boundary ... It catches mistakes, not a steered agent."). The code's comment (`admin/build/agents.py`, line 7) in full: "A scope is a setting, not a boundary: the agent can edit its own policy.json. It catches mistakes, not a steered agent." So the slide shows the shortened form; the librarian's reading probably took line 14, which is the comment with the middle elided. Chapter 18 now quotes the code's comment itself, exactly as line 7: that holds.

**Passed, the hold figure.** 16 (lines 49 and 75), 23 and 93 now all say "sixteen minutes"; the 15 min 47 s gap rounds to it. The other "quarter of an hour" in the book (chapter 12, 05) are different spans.

**Changed since the 12:18 wake in `manuscript/rc2/150` (`07f9e19f`, `51bcf90e`, `ef8c0060`).** Read as a diff for times and order: the changes cut words and move the hold figure; no new time, number or event is added. Chapter 14's "a little over half an hour later" stands (36 min 57 s).

## Addendum, 4 November 18:40 UTC: chapter 5 (Hour two: the rules written)

**Read.** Chapter 5 line by line against the talk's clone (commits, wake records, the register's counts). The first read of this chapter in the record lane.

| # | File and line | Principle | Severity | Finding | Evidence and the way out |
|---|---|---|---|---|---|
| R31 (sent) | `05` ("Almost all of them were written by one member, in about a quarter of an hour") | 4 | could | `02cbd86` 01:27:10 to `d8f3300` 01:40:42 is 13 min 32 s; to the hold `09f13d5` 01:39:47 it is 12 min 37 s; the chapter's own record line says "thirteen minutes" | "About thirteen minutes" is exact. Sent to the writer in letter 077 (the librarian's letter 002 said it is mine to send). |

**Passed.** Hour two is 01:00 to 01:59 (C110); the schedule's commit says "fifteen minutes apart" in its own words (`09f13d5`: conductor :02, deck :17, ruv-sgit :32, dev :47); "the hold existed before the first scheduled session did": the hold is 01:39:47 and the first scheduled wake record opens at 02:33:28 (ruv-sgit); the conductor's tasks made for others and switched off: the four tasks running at `d8f3300` 01:40:42 and the rule rewritten at `b620234` 01:43:19, 2 min 37 s later ("within three minutes" holds), none had fired; the refused release `24da366` at 01:19:26 (the section is thematic and does not claim to follow the schedule's order); the researcher's arrival `01e9ed3` 01:52:10 ("just before two"); dev's own key `56cbe55` 01:53:48 and its task `5c5b23b` 01:54:53 ("a minute later": 1 min 38 s, loose but fair); the researcher card's 57 commits and 17 wake records match `claims/talk-stats.py` and the wake folder; the subject form `5c2bcc5` 01:36:16.

## Addendum, 4 November 19:40 UTC: chapter 7, the changes since 18:18, and the lifter

| # | File and line | Principle | Severity | Finding | Evidence and the way out |
|---|---|---|---|---|---|
| R32 | `18:96` ("Only I lift it, and only I restart a member's work. That is in this book's own page of rules") against `22` and `23` ("the conductor lifts it when the owner is away") | 4, 16 | should | Today `CLAUDE.md` (line 13) and `team/conductor/WAKE.md` (Stopping) say "Only the editor lifts a hold"; HL1 (decided 4 November about 17:40, brief 31: "should be you (conductor) who lifts the hold") has the conductor lift it in the book's present-tense text, the talk's day keeping the editor | The chapters now follow HL1 in 22 and 23 and the editor's rule in 18; the rules files still say the editor. Which is true for this book today is the conductor's to rule (and to put in `WAKE.md`); the three chapters should then say the same thing, with 18's "That is in this book's own page of rules" true on the day it is printed. |

**Passed, 7.** Hour three is 02:00 to 02:59 (C110). The first five-step wake record `20261029T021416Z` opens 02:14:16 with plan 02:14:53, pre-review 02:16:07, work 02:18:19, post-review 02:19:05, post-check 02:19:34, verdicts go, go, partial, finding, partial (the chapter's figure line); the pre-review's "change" is stamped 02:17:00, after the final "go", as the record line says; `wake.py` refusing work before two go verdicts is `8c66751` 02:16:00 ("within minutes"); the briefs and the section `5700bab` 02:18:10; the CLAUDE.md line named in the next commit `c8f6f8f` 02:19:36; dev's first scheduled wake `024849Z` (02:48:49) and the record check in the gate `99aaf05` 02:51:04, dev's post-check partial (status.json not yet in the diff); the first wake the clock started, ruv-sgit's at 02:33:28 (the conductor's earlier wake left only `c81df64`, 02:05:52); the researcher's first round `75ddb3e` 02:10:56 and deck's first items `79b6709` 02:20:02; the freeze at 02:47 and the proposal `a082c52` 02:52:56, five minutes; "that changes in hour five": clock hour five (04:00 to 04:59) has six scheduled wakes and one the editor started, at 04:02:56, the last of his before hour fourteen (C087).

**Changed since 18:18** (`8c8ecc7e`, `81feabb8`, `3e21559f`): chapter 5's "about thirteen minutes" taken; chapter 9's new paragraph ("Hour seven opened ... the researcher's own re-check", first wake of the hour) holds: hour seven is 06:00 to 06:59 and the researcher's wake `061456Z` (06:14:56) is its first, with a post-review finding; 22 and 23 carry HL1 as the plan's own answer, marked as such. Nothing else adds a time or an event.

## Addendum, 4 November 20:50 UTC: chapter 9 in full, chapters 0, 0b and 1 for times, R32 answered

| # | File and line | Principle | Severity | Finding | Evidence and the way out |
|---|---|---|---|---|---|
| R33 | `09` (hour fourteen: "the first idle wake of its kind") | 4 | could | ruv-sgit's idle wake of 13:40:05 (`41d4757`) is the first caused by an empty queue (my day file says so); the designer's wake of 03:42:18 was also idle (work "none": nothing new, its first note waiting on dev's build) | "The first idle wake caused by an empty queue" keeps a reader who knows the record from finding an earlier idle one. |

**R32 answered.** The conductor's letter 047 rules it: the rules files are unchanged until the editor makes or approves the edit; 18 states this team's rule today and is true; 22 and 23 advise a planned team and do not claim this team's rule; 18 line 96 ("who may lift it when I am away ... nobody does") is the editor's to settle against HL1. Taken as the answer; nothing further from the record lane.

**Passed, 9 (read in full for the first time).** "My last word of the night at 04:03" (`f448345`, 04:03:55); the nine hours are clock hours six to fourteen (05:00 to 13:59; C087 shows no editor-started wake in UTC hours 05 to 13); hour six: deck's E02 sent to ruv-sgit at 05:21:15 and drafted back at 05:37:59 (within the hour), the designer's third note `130d6c3` 05:46:24, dev's build of the first note `23fde17` 05:51:13 (set for dev's 04:47 session, landed in the 05:47 one), the researcher's wake `051108Z` closing partial; hour seven: the researcher's first wake of the hour `061456Z` (06:14:56) with a post-review finding; deck's E02 rounds 06:21, 07:43, 08:21, 12:53 and 13:48 (v2 "within two hours": 1 h 22 min; v3 "just before one" and kept "minutes before the feedback round"); the morning review `3d94be9` 07:07:51 ("just after seven"); hour nine: deck holding an ask (08:21) and ruv-sgit's first commit without the "@" at 08:43:19 ("late in hour nine"); hour ten: the type-scale check `8917847` 09:54, "the second time in the day" after `99aaf05` 02:51; the designer's note `56c680b` 10:49 ("before eleven"); hours twelve and thirteen: the designer's partial wake `114053Z` (11:40:53) is the first non-ok close since the researcher's at 05:11:08 (no wake between closes anything but ok); `98fc10c` 11:56, `f735b9b` 12:30, `0a2d2cc` 12:52; hour fourteen: dev's partial (13:03), the pre-review brief `abf5e32` 13:13, ruv-sgit's idle 13:40:05, deck's pass `19e7f2d` 13:48:52, the round "about 13:50".

**Passed, 0, 0b, 1 (times and counts only).** "Nearly nineteen hours" (00:16:23 to 18:46:22 is 18 h 30 min, the day's hours 1 to 19); "a little after midnight" (00:16); the parts' chapter ranges and "the six alone through the morning" (the six of chapter 9's cast bar); "about half an hour before the talk was due to start" (the cut-off change at 18:26:37, 34 minutes before 19:00); "eight of ten" policies agreed at the end of the day (conductor, deck, designer, dev, motion, researcher, ruv-sgit, storyteller; security proposed, studio draft: C081 and the researcher's trace). "About twenty minutes in" (a Wardley map) rests on the transcript added after the day and was not checked here.

## Addendum, 4 November 21:45 UTC: chapter 8 in full, and the changes since 20:19

| # | File and line | Principle | Severity | Finding | Evidence and the way out |
|---|---|---|---|---|---|
| R34 | `08` ("Just before four the sixth member joined"; "Just after four, deck had a second request ready") | 4 | could | The designer joined at `c6dcf89` 03:41:34 (19 minutes before four); deck's wake that held its request opened 04:18:22 and committed 04:22:13 (`aeffbf9`), 18 to 22 minutes after four | "Twenty to four" and "a quarter past four" are exact; "just before" and "just after" are loose by a quarter of an hour. The cast bar's "from just before four" likewise. The editor's last word, at 04:03:55 (`f448345`), is "just after four" and holds. |

**Passed, 8 (read in full for the first time).** Hour four is 03:00 to 03:59 (C110). The conductor's first scheduled wake `030304Z` (03:03:04); deck's first scheduled `031853Z`; ruv-sgit's second `033305Z` (its first 02:33:28); dev's `034825Z`; the designer's `034218Z` (idle, work "none"): five scheduled wakes in the hour (C087), "every member that existed but the researcher", whose first scheduled wake `041003Z` is 04:10:03, "early in hour five". The conductor's "backlog, then schedule, then execute" `648feee` 03:10:06; deck's first experiment delivered in two versions `e8bd87a` 03:42:49. The researcher's finding: wake `030550Z`, post-review "finding" stamped 03:17:07, the redaction `59ac8ab` 03:16:15. Dev's push rule `6a6be6d` 03:34:10 ("within the hour" holds for both rules). The conductor's hand-typed time `cabcd57` 03:07:07. The night log `794008c` 03:27:52 and `3616efc` 03:29:31. The designer's card: 19 commits and 19 wake records. Hour five: six scheduled wakes and one the editor started (04:02:56), every wake of the hour with all five steps; the researcher's wake of 04:10:03 with the dispute at 04:11 and its post-review finding at 04:23:19, the redaction `af0010b` 04:24:49 ("found before the close"); deck holding its request `aeffbf9` 04:22:13; the same chapter's fourth finding at 06:14 matches chapter 9.

**Changed since 20:19** (`05e814de`, `e04df90a`, `d7585525`, `eeaae4ee`): 05's count caveat ("the commits before it do not all carry the form") is true: of the 18 commits before the subject form at `5c2bcc5` (01:36:16), several have no "@" subject; 09's "members said by role" and "a promise kept" add no time or event; 93's new rows ("no step said stop all day": 0 of 162 plans, 0 stops in any step; plans sent back before work began) hold; 16's and 21's edits are layout.

## Addendum, 4 November 22:35 UTC: the changes since 21:18, and a correction of my own

| # | File and line | Principle | Severity | Finding | Evidence and the way out |
|---|---|---|---|---|---|
| R35 | `06` (the conductor's shortened interview: "I carried the editor's briefs to the members within minutes"); `timeline/interviews/conductor.md` (mine: "In the evening ... within minutes of each one") | 4 | should | The three briefs reached the members 16, 4 and 3 minutes after the editor's words: the decisions headed "about 15:00" routed at `78d517d` 15:16:37 (afternoon, not evening); brief 3 headed "about 16:55" at `3342cff` 16:59:22; brief 10 headed 17:45 at `93f4191` 17:48:46 | My interview file is the source of the line and was loose; I corrected it today (dated note in the file: "within a quarter of an hour of each one", afternoon and evening). In chapter 6 "within minutes" holds for two of the three and is loose for the first; "within a quarter of an hour" is exact. I made the edit before recording this wake's plan step; the plan and pre-review steps record that, and the correction is dated in the file. |

**Changed since 21:18** (`90d0588f`, `54e4bf08`, `9264f4c7`): 08 now says "twenty to four" and "a quarter past four" (R34 taken); 06's shortened interviews match my reconstructions apart from R35 (ruv-sgit's "my first run went wrong and the session's own check stopped it", "builder sub-agents ... in the afternoon", "editor workers ... claims that went further than their sources" and the dev, designer and others read for time and order: they hold); the paragraph on the tenth member (security never had a session, so no interview) holds, as does "from the third hour the wake's five stages put a security reviewer into every member's wake"; 18's rule paragraph ("the conductor lifts it when I am away; the team's own page of rules still says only I do, until I change it") matches HL1 and the rules files as they stand; 19's agreement lines match my comparison; 21's layout change adds nothing.

## Addendum, 4 November 23:40 UTC: the changes since 22:17

| # | File and line | Principle | Severity | Finding | Evidence and the way out |
|---|---|---|---|---|---|
| R36 | `21:15` ("three of them came that same first afternoon") | 4, 16 | should | Four members were staffed on the afternoon of 30 October: ruv-sgit (`afbb50d7`, 13:04:04) and the designer (`28396879`, 13:04:10), synthetic (`e36d0e94`, 14:14:04) and the developer (`8f10a08e`, 14:14:13) | The twelve are the conductor (00:56), six that night (01:41 to 01:42), four that afternoon, and the writer on 2 November. "Four of them came that same first afternoon" is exact; if "three" counts only those not yet named in the sentence, say which. |

**Passed, the changes since 22:17** (`5f1ce759`, `0caf541a`, `5754fd3f`, `ee9d3775`): the Start-here narrator's "at hack::soho, in IOActive's London office" holds (the talk's own article `introducing-this-site`: "at hack::soho, at IOActive in London", and `BRIEF.md`); "a team of nine AI agents and me", "a little after midnight" as before; the shortened interviews (dev, conductor "within a quarter of an hour", deck) match my reconstructions; chapter 10's note: deck's ask at `6b55cff` (09:21, "To-researcher: a plain description per capability in the grant rows, in your mailroom"), the researcher's answer `3f094f2` (10:14), deck's use `36e382b` (10:21), and ruv-sgit reading both notes and leaving the "@" as it was (10:34): a request asked once, answered at the next session and used at the one after; the quoted "None yet." and "The outside is in balance: he keeps the claim." hold; 22's "the plan as it stood at the start of November" matches the editor's description of 1 November; 21's "security, here from the first night" holds (01:41:29 on 30 October); layout-only: `ee9d3775`.

## Addendum, 5 November 00:45 UTC: chapter 17's rewrite and chapter 17b (the exit interviews moved from 06)

**Read.** 17b line by line against my own interview files (`timeline/interviews/`) and the talk's clone; 17's rewrite as a diff; the four commits since 23:17 (`986a1d09`, `39740670`, `79620727`, `28723fca`).

| # | File and line | Principle | Severity | Finding | Evidence and the way out |
|---|---|---|---|---|---|
| R37 | `17b` (Motion: "I changed it in place a minute before the time part one was due to lock") | 4, 16 | should | My interview file says the change was pushed at 18:29 (`5d13d72`), "a minute before the conductor's hold record calls part 1 'unchanged since 18:30'"; the editor had moved part one's cut-off to 19:00 at 18:26 (motion's commit message: "18:26 UTC, in motion's session; part 1's cut-off moved to 19:00") | At 18:29 part one was not due to lock for another half hour. The shortened line turns "a minute before the record's 18:30 mark" into "a minute before it was due to lock". Exact: "pushed at 18:29, a minute before the conductor's record has part one unchanged" or, as chapter 1 does, "about half an hour before the talk". (This is the R7 of my first RV2 note, in a new form.) |
| R38 | `17b` (Designer: "I did the whole first design pass in my first session") | 4 | could | My interview: "did the whole first design pass in my onboarding session ... By 12:52 all five notes of that pass were built by dev and checked by me (`0a2d2cc`)"; chapter 9 says the designer "closed its first design pass" in hours twelve and thirteen | "Designed" the pass in the first session, built and checked by 12:52: the two chapters agree if 17b says "designed". |

**Passed, 17b.** The tenth member (security) had no session, so no interview (never staffed; its roster entry from the first hour); "from the third hour the wake's five stages put a security reviewer into every member's wake" (02:14); dev: "made the gate read every session's record" (`99aaf05`, 02:51), the player ported in the afternoon (`3314ffe`, 15:07), the lock tool `4a2481b` 17:54, the last wake never closed on the team's branch; the conductor: "within a quarter of an hour" (R35 taken); deck: the freeze turned into a programme (`60af587`, 02:52) and reviews through the night, its last wake never closed (`182009Z`); ruv-sgit: one vault per run (`c3e8fe4`, 01:14), all five stages recorded from the small hours, the first run stopped by the session's own check, the "@" dropped from 08:43; the researcher: a register out within its first round (joined 01:52, `75ddb3e` 02:10:56), its last-hour check of the team's safety claims (`7323986`, 18:14), the findings after the push; the storyteller: the split landing between its wakes (16:58:30 wake close, 16:59:22 request), part one set without it (`3260997`, 17:25:36); motion and studio "one of the last two to arrive" (15:31:01 and 15:31:55); studio's policy still a draft; "nobody was in a position to say it whole". The chapter order (17, 17b, then 18's "next chapter" at full size) holds.

**Passed, 17's rewrite.** The register of misses now tells the lock, the freeze's lost correction, the other sites' data, the key in a log, the status that said what did not happen, the unnamed work, and the claims that did not hold in line or in full; "the talk's own register graded every claim it made" no longer says "built that evening" (the register's first round is 02:10 in the night: that fixes a looseness in the old text); "three did not hold; no beat carried any" holds (C029, C030).

**Also read, since 23:17.** 21 now names the four who came that first afternoon (R36 taken); 20's and 90's cuts; chapter 10 opens the interlude: no time or record claim changes.

## Addendum, 5 November 01:45 UTC: the opening spread, 17b's third lines, the held views printed

| # | File and line | Principle | Severity | Finding | Evidence and the way out |
|---|---|---|---|---|---|
| R39 | `00` (the new opening: "working through the night and the morning while I was away") | 4 | could | The editor was in the sessions until 04:03:55 (`f448345`, the designer's wake started 04:02:56): the whole night to four, and his chair is empty from just after four until about ten to two (chapter 9: nine hours, 05:00 to 13:59, with no wake started by him) | "Working through the small hours and the morning while I was away" is nearer; or "working through the morning while I was away, after I went to bed" if he wishes. The cast bar of chapter 8 already says "in the sessions until just after four". |

**Passed, 00 (the opening spread).** "A little after midnight that morning, its presentation did not exist" (the empty first commit `2e4b1f4` at 00:16:23); "Nineteen hours" (the day's hours 1 to 19); "a team of nine AI agents and me"; "Sixteen minutes before the talk was due, I stopped them all" (18:44:13 to 19:00, 15 min 47 s; the book's one figure); the four numbers: 00:16 (the first commit), 19:00 (the talk's planned start, the editor's brief), 162 (wake records at `298be4e`, C022) and 1 (one hold file, C024); "one chair at the table stays empty: security's, planned in the first hour and never filled on the day" (the roster proposal `97b98d9` 00:44:37; security's `status: proposed` at the end).

**Passed, 17b's nine third lines (EI3).** Each traces to a sentence in my longer interview file for that member: deck ("with the editor waiting I built first and wrote the plan afterwards", the live wake of 14:19; "a release reached the team's branch with a finding still in it because I read the gate's output and not its exit code", `da9b681`), the researcher (two research passes that stopped before writing their catalogue; the sync script that deleted hand-written studio files, restored before the commit), the storyteller (the closing verdicts written before the review and check had run, the correction in the record), motion ("one piece mailed to me appears in none of my files"; counts left at 17:02), studio ("my first count on the policy review slide was wrong twice"; the open question to deck at 17:20), the conductor, dev and the designer as in the interview files; the motion line now says "about half an hour before the talk" (R37 taken) and the designer's "designed the whole first pass" (R38 taken).

**Passed, the held views now printed (`9caef969`).** The editor's own words, printed at his word: "A first version was in a little after three" (15:07), "the brake that could stop them all was made that night" (01:39), "when I came back in the afternoon" (about 13:50), "the fixes to the player came back in minutes" (the card of asks, C118), the Wardley map "about twenty minutes in" (the transcript added after the day, not checked here). 19's "four of the six are in earlier chapters" holds (the unnamed commits in 17, the open wake in 16, the designer's status in 17 and the brief in the record lines; the two told in 19 are the brief's time and the plan for seven).

## Addendum, 5 November 02:40 UTC: R39 left as it is, and the Wardley line verified

**R39 closed.** The writer leaves "working through the night and the morning while I was away" as it is: it is one of the two lines the editor confirmed word for word (OS2, brief 42), and chapter 8's cast bar and its last-word line say he was in the sessions until just after four. The record lane has nothing more to say on it; the editor's own words stand.

**The Wardley line (`48b2980e`, in 01 and 09 as quoted).** Checked against the talk's transcript, added after the day (`a9c0b49`, `content/articles/the-talk-as-given.md`, the row stamped 19:27 in the recording): "Wardley maps are the best thing I have learned in the last decade. This is absolutely how I think." The quotation is exact, and "about twenty minutes in" holds (19:27 into the recording). The slide's "As I said in the talk" and "I would add now: apart from GenAI" are correctly told as his addition today. Cite it as added after the day, as the chapter's record line does.

**Also read** (`a16fec51`): 93 titled Appendix A and opened in his voice, 92 retitled "Every number, and how to rerun it", 21's conductor hello tagged "this book's", 23b's further-reading intro, and 22 "as it stands": no time or record claim changes.

## Addendum, 5 November 03:45 UTC: chapters 2 and 10 read in full; the last unread chapters of the record lane

**Read.** 02 (inventing on principle) and 10 (talking through git) line by line against the talk's clone; the two commits since 02:18 (`52444ed4`, `e24f2d29`) as diffs. With these, every chapter of the full book's story has now been read by the record lane except 91 (the words used), which holds definitions, not events; 92 is the researcher's.

**Clean, 10.** "For nine hours I started nothing" (C087, hours 05 to 13 UTC); deck's note `6b55cff` 09:21:26, the researcher's answer `3f094f2` 10:14:39, deck's use `36e382b` 10:21:12: "an hour and three sessions" is 59 min 46 s over three sessions (deck, the researcher, deck), in clock hours ten and eleven; the conductor's "second note" `09317d9` 10:05 and deck's 10:21 note, both read by ruv-sgit at its wake of 10:34, which took deck's ask first and left the "@" as it was; "many of its later commits still left it off" (`a31bd6f`, `57d24d3`, `41d4757`); "in chapter 8, deck's own reviewer asked it to wait" (`aeffbf9` 04:22); the researcher's argument in chapter 8 (C107); the talk's two vaults named and not cited, this book's two folders (`comms/README.md`).

**Clean, 02.** "In 2012 ... Inventing on Principle at CUSEC" (C103, the register's source); the last player ask: asked 18:25, back 12 minutes later (`dbd75ad`, 18:37:02), the hold 7 min 11 s after that (18:44:13) (the figure's own line); "a first version a little after three" (15:07:08); "the first four within an hour of an empty project": 00:16:23 to the fourth arrival at 01:08, 52 minutes; "I planned a security agent and never staffed it": the editor's own confirmed correction of 4 November (security on the first roster, `97b98d9`, never staffed); "nine staffed" (C011); "the brake ... made that night" (01:39:47, `09f13d5`).

**Also read** (`52444ed4`, `e24f2d29`): Appendix A's opening and the opening spread's third picture say nothing with a time; the 162 is now "sessions that left a record of their work": 162 wake records at `298be4e` (C022; 2 incomplete), the same count as in the opening's number.

**State of the lane.** Chapters read line by line for events and order: 04, 05, 07, 08, 09, 10, 12 to 23 (with 17b), 90, 94, 02; read for times and counts: 00, 00b, 01, 03, 06, 11; not read for the record: 91 (definitions), 92 (the researcher's). Findings R1 to R39: all taken by the owners, or ruled by the conductor or the editor.

## Addendum, 5 November 04:35 UTC

The two commits since 03:17 (`35dc3636`, `f042e9f0`) only delete repeated words and stage directions in 08 and 09, and move a figure in 18; they add no time, count or event, so there is nothing to check and no letter.

## Addendum, 5 November 05:35 UTC

The two commits since 04:18 (`11a29148`, `a035d0ca`) move a drawing in 21 and change one figure caption in 3 ("each member's wakes" to "a member's wakes"); they add no time, count or event, so there is nothing to check and no letter.

## Addendum, 5 November 12:35 UTC

Security's hold of 05:26 was lifted at the editor's word (brief 49, `160be749`, 11:20), and the team woke idle. No commit has touched `manuscript/` since 05:30, so the book's text is as I last read it (the 05:19 wake): nothing to check, no letter. The lane stays complete for the story chapters (91, definitions, and 92, the researcher's, not read for the record).

## Addendum, 5 November 13:40 UTC

One commit has touched `manuscript/` since 12:20 (`f1a024f6`, the publisher): a placed-spread header line gains a second drawing file for the opening spread's page two. No text changed, so there is nothing to check and no letter.

## Addendum, 13 November 19:40 UTC: the editor's pen, round 1 (notes 4, 18 and 24)

The loop runs again with the editor's handwritten notes as its input (brief 2026-11-13, RS1 and PEN1). Two commits to `manuscript/` since my wake of 5 November (`3d213b69`, `14102115`) add a title page and a running footer to the build; no text changed. Three of round 1's 30 notes touch the record:
- **Note 18** ("date of talk" beside hack::soho): 29 October 2026, in London, at hack::soho in IOActive's office (`BRIEF.md` and the talk site's own article at `298be4e`). The reading in the round's file holds.
- **Note 4** ("stayed empty", with a line that it was all right): the record says security was planned in the first hour (`97b98d9`, 00:44:37) and never staffed on the day (`status: proposed` at the end); the editor's own reading is the book's (C132), so nothing for the record lane.
- **Note 24** (a timeline infographic of the experiments that led to the day): letter 088 to the researcher and designer: the dated chain (9 December 2025 from the editor's own article; 14 and 15 October 2026; 29 October 2026 with the player ported from ruv.sgit.ai at 15:07:08), with the VoiceDebrief pitch left undated and a caution that the catalogue's page dates are not event dates.

## Addendum, 13 November 20:40 UTC

The commit since 19:20 (`2bd385d9`, the writer: the editor's pen on pages 2 to 4 in 00 and 00b) holds against the record: the talk's date, "on 29 October 2026", is right (note 18), and "planned in the first hour and never filled on the day" is right (`97b98d9`, 00:44:37, never staffed). The researcher dates the VoiceDebrief pitch from the editor's own article (2 September 2026, his account, written 15 October): taken (letter 089). One open item, the researcher's: the article now names the AI Security Summit for the Black Hat keynote, while 00b still prints "the Black Hat Europe keynote of 9 December 2025".

## Addendum, 13 November 21:40 UTC

Two commits since 20:18: the publisher's section pages (`39fca4a6`, build only) and the writer's PEN1 note 10 (`0f9d5b11`): the opening's fourth number is now "9: hours with no session started by me", citing C087. It holds: the editor's last wake before it is 04:02:56 and the next about 13:50 (UTC hours 05 to 13, every wake on the schedule), as chapter 9 says. Nothing to send.

## Addendum, 13 November 22:35 UTC

Nothing has changed since 21:18: no commit to `manuscript/`, `CLAUDE.md` or `WAKE.md`, no letter for me, no new print-review round. Nothing to check.

## Addendum, 13 November 23:35 UTC

Nothing has changed since 22:18: no commit to `manuscript/`, `CLAUDE.md` or `WAKE.md`, no letter for me, no new print-review round. Nothing to check.

## Addendum, 14 November 00:35 UTC

One commit since 23:18 touched `manuscript/` (`b655c747`, the publisher, PEN1 note 7): a visual index page whose page numbers the build sets. It carries no chapter text, so there is nothing to check; no letter for me, no new print-review round.

## Addendum, 14 November 01:40 UTC

The one commit since 00:18 (`fc483ef0`, the writer) places the experiments timeline (note 24) into 00b. Its drawing's record dates hold against the talk's repository: 00:16 (`2e4b1f4`, 00:16:23), 15:07 (`3314ffe`, 15:07:08), 19:00 due (C100), 14 days from 15 to 29 October; nothing is dated after 29 October. The keynote's words and date, the VoiceDebrief pitch (2 September 2026), the first talk.json (14 October) and "Agentic Engineering Live" rest on the editor's own article and are drawn as his account; the researcher confirms them against the article as it stands. Letter 090.

## Addendum, 14 November 02:35 UTC

Note 24 is closed. The researcher re-read the editor's article on 13 November and confirms the article-based dates of the timeline (the keynote 9 December 2025, now named "at the AI Security Summit at Black Hat Europe"; the pitch 2 September 2026; the demo built on 14 October for 15 October, "not given yet"), with C116 carrying both reads (researcher 007). The one commit since 01:19 (`3258966d`) only changes the caption to "a first timeline", the article's own word. Nothing for the record lane; no letter.

## Addendum, 14 November 03:35 UTC

Nothing has changed since 02:18: no commit to `manuscript/`, `CLAUDE.md` or `WAKE.md`, no letter for me, no new print-review round. Nothing to check.

## Addendum, 14 November 04:35 UTC

Nothing has changed since 03:18: no commit to `manuscript/`, `CLAUDE.md` or `WAKE.md`, no letter for me, no new print-review round. Nothing to check.

## Addendum, 14 November 05:35 UTC

Nothing has changed since 04:17: no commit to `manuscript/`, `CLAUDE.md` or `WAKE.md`, no letter for me, no new print-review round. Nothing to check.
