# RC2, the 30-page edition: traced chapter by chapter

researcher@book.the-ultimate-insider. Each chapter of `manuscript/rc2/30/` as the writer sends it, against `claims/register.json` and the talk's record at `298be4e` (and `a9c0b49` for material added after the day). Board 011.

## Chapter 1, "The creator's problem" (2 November 2026, the 18:32 wake)

**In short:** every figure and quote holds, with one exception. The line that "none of the parts was new", naming "the brake", does not hold against the historian's lineage. The same line is in the 10-page edition, and I passed it there; that was my miss.

| Line | Holds? | Why |
|---|---|---|
| The voice note of 1 November, quoted | holds | word for word in `briefs/2026-11-01__in-session/03-the-factory-and-the-zoom.md` |
| "three days after the talk" | holds | 29 October to 1 November |
| The building quote, "from the recording" | holds | C102, 15:50 on the transcript's clock; added after the day (`a9c0b49`) |
| "I changed it at 18:26, about half an hour before the talk was due to start" | holds | motion's wake record, 18:26:37 (C102); 34 minutes before 19:00 (C100). "Due to start" is right; the record has no start time |
| "about 87 minutes, to a room in London" | holds | C069; C100 (the venue, from `a9c0b49`, added after the day: the line says so) |
| "my first priority; I said so at about ten to two" | holds | the editor's brief, about 13:50, "the main priority" (C104's feedback round) |
| "By seven minutes past three a first version was in" | holds | `3314ffe`, 15:07:08 |
| "My last request in the record has my own time on it, 18:25" | holds | `dbd75ad`; the last of the eight asks with his time (C105) |
| "A change came back within the hour" | holds | C105: each of the eight was recorded or landed within 12 minutes of the time written; the player fixes are the clearest "came back" |
| Bret Victor, CUSEC 2012, the quote | holds | C103 |
| "Nine of them, each with one job and one page of rules" | holds | C011; each staffed member's `ROLE.md` at `298be4e` |
| "the first four within the hour of an empty project" | holds | C001, C011: 52 minutes |
| "One chair at the table stays empty all day" | holds | security, proposed at 00:44 (`97b98d9`), never staffed (C011) |
| **"None of the parts was new: the build, the check every change had to pass, the brief, the brake that could stop them all. Each came from something I had built before."** | **does not hold for the brake** | The historian's lineage (`timeline/lineage.md`, line 19): the hold was invented that night, with the schedule (`09f13d5`, 01:39). The build, the gate and the brief were reused. Suggested: "Most of the parts were not new: the build, the check every change had to pass, the brief. The brake that could stop them all was made that night." |

## Chapter 2, "The factory is assembled" (2 November 2026, the 20:32 wake)

**In short:**
- The arrivals, the scenes and the quotes all hold, and the year of daily work is now C106.
- Two passages still say the hold was not new. These are the line fixed in the scripts and the map's bottom row.
- One line, "every member, every wake", needs its number.
- "Nothing else" in the empty project misses one file.

| Line | Holds? | Why |
|---|---|---|
| "A new repository with a licence, a short read-me and nothing else" | not quite | `2e4b1f4` has three files: `LICENSE`, `README.md` and `.gitignore`. Say "a licence, a short read-me and an ignore file", or "and almost nothing else" |
| "Its first commit says 'Initial commit'" | holds | `2e4b1f4` |
| "By twenty to one the first agent had read both and was building" | holds | `1f7c633`, 00:40, with `BRIEF.md` and `CLAUDE.md` |
| Dev: the brief in full, "what is real, and what we got wrong" | holds | `BRIEF.md`, `REALITY.md`, `BRIEF-CORRECTIONS.md` in `1f7c633` |
| Conductor: "Security is on the list" | holds | `97b98d9`, 00:44: "conductor, security, researcher, deck, dev" |
| Deck: owner of the beats, script and slides | holds | `20ab1a3`, 00:51 |
| ruv-sgit: "First run is open. An article drafted, waiting for the editor's check" | holds | `defe526`, 01:08 |
| "Four agents, all within the hour" | holds | C001, C011: 52 minutes |
| **"None of it was new. The build, the check, the brief, the hold: each piece came from something I had built before"** | **does not hold** | The hold was made that night (`timeline/lineage.md`; `09f13d5`, 01:39). The scripts are fixed (the storyteller's 064); use the 10-page script's line: "The build, the check and the brief came from things I had built before. The hold was made that night." |
| **The map: "Every part of it [the bottom row: the agent tool, the build, the check, the hold and the brief] was already ordinary to me that night ... Only the top of the picture was new"** | **does not hold for the hold** | Same source. The schedule and the five-step wake were also made that night, though they are not in the row. Move the hold out of the bottom row (to the new end, as the storyteller's map now does), and say "Almost every part of it" |
| "working with an agent tool every day for about a year" | holds | C106, the editor's own article of 9 October 2026, as his own account |
| "dev's first commit calls it the sgit.ai way" | holds | `1f7c633`: "built the sgit.ai way" |
| **"Every member, every wake"** (the five steps) | **holds as the rule, not as a count** | 160 of the day's 162 wake records have all five steps (C022). Also, 46 of the agents' commits were made with no wake open (C088). Say "the rule for every member, every wake", or give 160 of 162 |
| The reviewer scene: a file outside its rules, allowed but not named | holds | post-review at 02:19:05 in `team/conductor/wakes/20261029T021416Z.json`: CLAUDE.md "outside conductor scope; the editor allowed it, but the commit message never names it"; closed partial (`c8f6f8f`) |
| The card: "the count of wake records the team kept that day" | holds | C022: 162 |
| The researcher at about two, the designer before four, six by four in the morning | holds | 01:52 and 03:41 (C011) |
| "the one who would tell me 'no' in writing before the day was out" | holds | R5, 14:33 (`2726f0e`) |
| "From five, it did" | holds | C087 |
| The minutes on the dial | holds | C071 |

## The same line in the editions (my miss)

The 3-page edition, page 1 ("None of it was new. Each piece came from something I had built before") and the 10-page edition, page 2 ("The build, the check, the brief, the hold: each piece came from something I had built before") make the same claim. I passed both on 2 November (`claims/editions-03-10-trace.md`) without checking it against the lineage. The 10-page line names the hold, so it does not hold. The 3-page line is general, and fails for the same reason. Reported to the storyteller and the publisher (`researcher__008`).

## Where this came from

`manuscript/rc2/30/01-the-creators-problem.md` as on dev at 18:33 on 2 November; `timeline/lineage.md`; the talk's record at `298be4e` and `a9c0b49`; C001, C011, C069, C088, C100, C102, C103, C104, C105.
