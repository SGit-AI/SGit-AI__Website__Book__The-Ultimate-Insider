# The opening script, traced

researcher@book.the-ultimate-insider, 1 November 2026, the 14:32 UTC wake (board 008, NR1). The storyteller's `chapter-plan/cast/opening-script.md` at `5165769`, read line by line against `claims/register.json`, `claims/agents-how-they-work.md` (C096) and the talk's record at `298be4e` (with `a9c0b49` for material added after the day). Times are UTC, which was London time on 29 October.

**In short:** every quoted line marked *(record)* is in the record, word for word (9 of 9). Every number in a band has its register id. Seven times or citations need fixing; one agent line claims more than the record shows; one new entry (C100) backs "sixteen minutes".

## What needs a change

| Page | The script says | The record says | Change to |
|---|---|---|---|
| 5 | the freeze at 02:47 (`60af587`) | the editor's word to deck was at 02:47; deck recorded it in `60af587` at 02:52:11 (`team/deck/requests/researcher__before-tonight.md`) | band: "the freeze at 02:47, recorded at 02:52 (`60af587`)" |
| 5 | Researcher: "I do not remember numbers. I read each one from its capture, every time." and its `%% claim:` | the talk's method did capture sources (`evidence/METHOD.md`: "A claim without a captured source is a gap"), but 52 of its 320 claims were never checked, and one out-of-date figure reached a slide (C029, C031) | bubble: "I read a number from its capture, not from memory. With no capture, I wrote 'not checked'." `%% claim:` "the researcher graded the talk's claims against stored captures of their sources; 52 of 320 were never checked (C029)" |
| 6 | the designer's idle wake (03:42) | the wake opened at 03:39; the commit with the quote is `09c02ff`, 03:43:16 | 03:43 |
| 6 | deck's review (06:25) | `78b89b9`, 06:21:41 | 06:21 |
| 7 | studio's refusal (17:41) | the wake opened at 17:41 (`team/studio/wakes/20261029T174115Z.json`); the refusal is in `bd3cdad`, 17:47:28 | 17:47, and the band cites `bd3cdad` with the wake record |
| 7 | Studio: "A relayed word is not his word. I asked him myself." | "The session's safety check refused a member marking its own policy agreed on a word relayed by another agent; the editor is asked in this session" (`team/studio/debriefs/2026-10-29__abp-review.md`) | keep the line, but the band should say the session's own check made the refusal, and studio then asked the editor. The record does not show studio deciding it |
| 8 | the conductor's plan at 18:36, cited as `team/conductor/wakes/20261029T183647Z.json` | the quoted words "Leave the lock to dev" are in `team/conductor/night/20261029T1838.json`, committed in `2ed6427` at 18:39:16 ("18:36: part 1 not yet locked") | add `2ed6427` and the night file to the band |
| 8 | "sixteen minutes before I went on" | the record holds 19:00 London as the time the talk was due; it holds no clock time for when he went on (C100) | in his voice it may stay, as his; the band says "sixteen minutes before the talk was due (C100)" |
| 8 | motion's record of 18:26, cited as `5d13d72` | motion's wake record has the editor's change at 18:26:37 (`team/motion/wakes/20261029T182543Z.json`); `5d13d72` is the work commit at 18:29:28 | add the wake record to the band |
| 8, note | "on 31 October, that the 95% was a footnote ...; the same evening, that it was the token usage" | the footnote account is from the early hours of 31 October (batch 7, committed 01:48); the token account is about 19:00 the same day (C089) | "in the early hours of 31 October ...; that evening ..." |

## What holds as written

- **Page 1:** 00:16 (C001, 00:16:23); nine agents and the editor (C011, open for "ten"); 58 beats (C015); about 87 minutes (C069, from `a9c0b49`, added after the day). "On stage in London": C100.
- **Page 3:** dev 00:40 (`1f7c633`), the conductor 00:44 (`97b98d9`), deck 00:51 (`20ab1a3`), ruv-sgit 01:08 (`defe526`): first commits, C011. The researcher 01:52 (`01e9ed3`).
- **Page 4:** the schedule at 01:39 (`09f13d5`, 01:39:47); the five-step wake from 02:16 (`8c66751`) to 02:18 (`5700bab`); its close at 02:19 (`c8f6f8f`). Both quotes are in `c8f6f8f`: "Name it in the debrief or record" in the wake record `20261029T021416Z.json`, and "a second reading, not a second identity" in the conductor's debrief. The `%% claim:` on the reviewer's reach holds: it is the conductor's own description of its setup, in that debrief.
- **Page 5:** the freeze quote is deck's file, word for word; the correction at 02:52:56 (`a082c52`), five minutes after the editor's word (C031).
- **Page 6:** C087: from 05:00 to 13:59 every wake was started by the schedule. "I started nothing" holds for wakes; the record cannot show he did nothing else. The designer's 10:49 (`56c680b`) and the conductor's 10:05 (`09317d9`) hold. "Again" holds: `09317d9` calls it "a second note".
- **Page 7:** R5 at 14:33 (`2726f0e`), the storyteller at 15:02 (`b208a16`), the designer at 17:48 (`ec962a2`), "DEVIATION RECORDED" in `team/conductor/wakes/20261029T140915Z.json`. The storyteller at 14:15, motion and studio at 15:31 (C011).
- **Page 8:** the hold at 18:44:13 (C006, C024); the designer's commit 82 seconds after it, "a minute and a half" (C065); the day's last release at 18:46 (C005).
- **Page 9:** none of the three claims that did not hold reached the stage (C030); one out-of-date figure did (C031); no part was ever locked (C027). The lock tool `4a2481b` (17:54) is dev's line to own: its commit carries no `@dev`, so the historian should confirm it was dev's.
- **Page 10:** the Faro quote is the newsroom's, as the editor's brief of 31 October cites it; C091 for the day.

## Not traced here

The storyteller's slot "between two deadlines" (page 9), deck's "parts two and three never got finished" (page 9; C027 has them in progress at 18:44, and C070 shows 8 of part 3's 20 beats reached on stage): these are the members' own debriefs, the historian's to confirm. Pages 2, 11 and 12 carry no numbers.

## Where this came from

`chapter-plan/cast/opening-script.md` at `5165769`; the talk's repository at `298be4e` and `a9c0b49` (read-only clone), each commit and file named above; `claims/register.json` C001 to C100. Checked on 1 November 2026, about 14:40 UTC.
