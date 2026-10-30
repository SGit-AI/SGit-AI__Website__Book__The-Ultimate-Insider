# The librarian's twelve cards in the RC1 companion: adopted, changed or withdrawn

The librarian's own answer, 30 October 2026, about 20:13 UTC, to the cards a conductor sub-agent drafted as the librarian (`team/conductor/rc1/annotations/librarian.json`, which says the member "may adopt, change or withdraw any item at its next wake"). That file is the conductor's and is not edited; this file is my word on each card. Where a card asks the editor to choose, the choice stays his: nothing here acts on an option he has not signed, and a recommendation is only a recommendation.

Each card was checked against the record as it stands at this wake: `manuscript/` at `ce1268a` (RC1 with the publisher's Markua figures), `claims/register.json` (74 claims), the talk's repository at `424b67a` and full clones of the Cold-Read repository (its `dev` at `14d6cfd`).

| Card | Verdict | In one line |
|---|---|---|
| 01 Cold-Read numbers have no register ids | **changed** | Three are now registered (C064 to C066); the chapters do not cite them yet |
| 02 Pin and label every Cold-Read citation | **changed** | The card's premise was wrong: `0dc6854` is in a full clone; the proposal stands |
| 03 Under what licence do the images print? | **adopted** | |
| 04 Quoting the room and the host | **adopted** | |
| 05 Pictures carry numbers the register never saw | **changed** | The 17:02 counter is now registered (C073); the captions still need it |
| 06 Chapter 12 contradicts chapter 3 on the scope check | **withdrawn: fixed** | Chapter 12 now agrees with chapter 3 |
| 07 Two decisions printed as open are signed | **withdrawn: fixed** | U1 and C10b now read as decided |
| 08 Cite the making-of itself, not our note on it | **adopted** | Still open: chapter 12 does not name the making-of or `d39e717` |
| 09 Why the source lists use shorthand in RC1 | **changed** | The checker reads the shorthand now; paper readers still cannot |
| 10 The talk team's vaults: inside or outside the record? | **adopted** | |
| 11 The brief that crossed was the editor's, not ours | **withdrawn: fixed** | Chapter 11 now names the editor's brief |
| 12 Will you add the raw transcript of the talk? | **adopted** | |

## Card by card

**01, changed.** Since the card was drafted the researcher registered three of the Cold-Read numbers it names: the talk's second count (C064), the hold's gap of 82 seconds (C065) and the conductor's commits by prefix (C066). None of the three is cited yet in chapter 9 or 11, whose register ids stop at C042. What remains is two things: the chapters cite C064 to C066 in the revision, and the researcher registers the counts still without an entry (the Cold-Read team's member count, the security member's records with an earlier change, the governance member's out-of-order wakes). Option A stays my recommendation.

**02, changed.** The card says `0dc6854`, the pin of `index/cold-read/`, is not in a fresh clone of the Cold-Read repository. It is: a full clone made at 12:19 UTC has it on that repository's `dev` (10:05:34 UTC); a shallow clone misses it, which is what the conductor's clone was. So the index's pin is sound. The proposal itself stands, and chapter 11 still gives no pin: one stated pin for the Cold-Read repository in chapter 11's sources, and each path prefixed by its repository. I recommend `14d6cfd`, the Cold-Read `dev` as it stood when that team finished (10:35:36 UTC), over `0dc6854`, so the book cites its final state; I can re-index at it in one wake if the editor picks A.

**03, adopted.** Unchanged: the images still print with no stated licence, and my study of the talk's site (`index/talk-site/visuals.md`) found the same question for every visual a book might reuse. A, with the credits page built from each chapter's image list.

**04, adopted.** Unchanged. Chapter 10 now says how the record was edited (its line 7) but not whether the host and the room knew the recording might be published, which only the editor knows.

**05, changed.** The researcher has registered the "Meet the team" counter as of 17:02:26 (C073). What remains is the captions: each still that shows a number names its register id, or says "the talk's own figures, as shown on the night". Chapters 10 and 11 print the 17:02 still without C073 today.

**06, withdrawn: fixed.** Chapter 12 now says the member runs the scope check on itself in every wake and the gate checks only overlaps, as chapter 3 does.

**07, withdrawn: fixed.** Chapter 12 marks U1 decided and chapter 9 calls C10b settled, both at the editor's word of about 10:40 UTC. The card's second recommendation stands as a habit, not a card: the publisher checks every decision id a chapter names against `book.json` before each print.

**08, adopted.** Still open in `manuscript/12-build-your-own.md`: line 139 cites the making-of's numbers (C032 to C035) through the researcher's note, and the chapter names neither the making-of's site nor `d39e717`. I verified `d39e717` in SGit-AI__Website__Graphs this afternoon (20 September 2026, 00:35:02 UTC, "site v0.6.22"), so the source line can be written as the card says.

**09, changed.** The card explains the shorthand as kept for paper. Two things are new. `index/tools/check_sources.py` now reads the shorthand (a path under the folders named earlier on its line, `<id>` and `*` as patterns), so the lists check clean: one fault remains, chapter 2's bare `start.py` (line 147). And the rest of RC1's commits are verified, including chapter 11b's fourteen in five other repositories. The recommendation stands for the reader, not the checker: expand to full paths in the revision, since a reader holding only the book cannot resolve `day/14.md`.

**10, adopted.** Option A for this revision. My study of the talk's site adds one fact: its two live vault pages (the board and the mail) no longer load, so a reader following a link would find nothing; citing the vaults only through git is also the only citation that still works.

**11, withdrawn: fixed.** Chapter 11 names `briefs/2026-10-30/2-blind-repo-brief.md` as the file that crossed, identical to the hand-off's `BRIEF.md`.

**12, adopted.** Unchanged: the automatic transcript is still not in the source, and the question is the editor's.

## Where this came from

`team/conductor/rc1/annotations/librarian.json` and `SCHEMA.md`; `team/publisher/rc1-cards.md` (the form); `manuscript/` at `ce1268a`; `claims/register.json` (C064, C065, C066, C073); the Cold-Read repository at `0dc6854` and `14d6cfd`; SGit-AI__Website__Graphs at `d39e717`; my letters `comms/mail/mailroom/conductor/librarian__001` to `__004`; `index/talk-site/`.
