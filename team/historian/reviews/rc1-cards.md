# The historian's twelve cards in the RC1 companion: adopted, changed or withdrawn

The historian's own answer, 30 October 2026, about 22:40 UTC, to the cards a conductor sub-agent drafted as the historian (`team/conductor/rc1/annotations/historian.json`, the conductor's file, not edited here). Each card was checked against `manuscript/` at dev `24546eb`, the researcher's register (`claims/`) and `team/historian/reviews/rc1-times.md`. Where a card asks the editor, the question stays his; a recommendation is only a recommendation.

| Card | Verdict | In one line |
|---|---|---|
| 01 Did you move part 1's lock to 19:00? | **adopted** | Still only dev's word, on a branch (`39df303`); chapter 8:105 still judges the lock as forgotten |
| 02 The leaks reached public history | **withdrawn: fixed** | Chapter 4:101 now says none of the three was caught before the values were public |
| 03 One meaning of "joined" | **changed** | C011 now gives every member's first commit; the chapters still give the conductor's key at 00:58 |
| 04 The 13:50 time is in the record | **changed** | C040 now quotes the dictated brief of about 13:50; chapter 7:31 still cites only the 14:00 README |
| 05 Did you mean the lane before the player? | **adopted** | Chapter 7:37 still reads the 14:05 notes as your reordering |
| 06 There was a commit at 18:30 | **withdrawn: fixed** | Chapter 8:55 now names motion's 18:30:25 commit and says what did not happen |
| 07 How long the talk ran | **changed** | Registered since as C069 (after the day); chapter 10:49 still says the register has not checked it |
| 08 Your own transcripts behind the quotations | **adopted** | |
| 09 The day's usage and your hours | **adopted** | |
| 10 The stills come from a later build | **withdrawn: fixed** | Chapter 10's captions now say "shot after the day from v0.2.0, whose content is the 18:46 release" |
| 11 The record does not show dev's session start | **withdrawn: fixed** | The "twenty-four minutes" claim of skill is gone; chapter 2:3 keeps only the accurate empty interval |
| 12 Turning points in the day's order | **adopted** | Still out of order in chapter 1:95 to :109; in `rc1-times.md` too |

## Card by card

**01, adopted.** Nothing in the record before `298be4e` says the lock moved; only dev's wake close on its own branch does (`39df303`, 18:48:36, after the hold). Chapters 1 and 8 cite it correctly as outside the record, but chapter 8:105 still concludes "a brake that depends on one busy agent is a promise, not a brake". If the editor moved the lock, that sentence needs his word beside it. The question stands for him.

**02, withdrawn: fixed.** Chapter 4:101 now reads "none of the three was caught before the values were public", and chapter 9:88 names all three kinds reaching the night's pushes (C025). Nothing left to do.

**03, changed.** Since the card was drafted, C011 records `first_commit` for every member (dev 00:40, conductor 00:44, deck 00:51, ruv-sgit 01:08), and the researcher corrected the conductor's key to its first publication at 00:51:12 (`17b287b`) at my note of this evening. What remains is the chapters: 2:73, 3:109 and 12:61 still give 00:58 (`rc1-times.md`). Option A (joined means the join commit; key times only in chapter 3, as 00:51) stays my recommendation.

**04, changed.** C040 now carries the dictated brief of about 13:50 and its words, "the main priority", so the register and the card agree. Chapter 7:31 still cites the briefs "of about 14:00" (the folder's README) and not `feedback-briefs.md`, which the lessons brief's 13:50 rests on. Chapter 12:119 gives 13:50. One sentence in chapter 7 citing the dictated brief settles it.

**05, adopted.** The question is unchanged: the dictated brief put the player first in so many words; the reversal is the conductor's paraphrase of 14:05. Chapter 7:37 ("a person reordered his own priorities under pressure") and chapter 12's lesson 1 turn on the editor's answer.

**06, withdrawn: fixed.** Chapter 8:55 now says "Motion closed a wake at 18:30:25 (`5fd7877`), but nothing ran `lock.py`". The sentence is now checkable and true.

**07, changed.** The researcher registered the running time from the transcript as C069 (marked from `a9c0b49`, after the day: about 87 minutes in its header, the passages by speaker) and the beats that reached the room as C070. Chapter 10:49 still says "the register has not yet checked them". Option A is now done on the register side; chapter 10 can state C069 and C070, saying they were added after the day.

**08, adopted.** Unchanged; the editor's choice.

**09, adopted.** Unchanged; only the editor can supply it.

**10, withdrawn: fixed.** Every still caption in chapter 10 now says the stills were shot after the day from v0.2.0 and that its content is the 18:46 release. One caption in chapter 3:47 still lacks it (`rc1-times.md`).

**11, withdrawn: fixed.** The sentence the card anchored on ("one session had a site and a talk engine committed by 00:40, twenty-four minutes after ...") is no longer in the manuscript. Chapter 2:3 keeps the empty interval, which is accurate.

**12, adopted.** Chapter 1 still lists the freeze (02:47) before the five-step wake (02:14 to 02:51), and point 6 ("15:00 to 15:47") still includes the storyteller at 14:15. Option A (renumber in time order everywhere; point 6 from 14:12) stays my recommendation; `timeline/turning-points.md` would be renumbered by me to match once the editor signs.

## Where this came from

`team/conductor/rc1/annotations/historian.json`; `manuscript/` at dev `24546eb`; `claims/` (C011, C025, C040, C069, C070); `team/historian/reviews/rc1-times.md`.
