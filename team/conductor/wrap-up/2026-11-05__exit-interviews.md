# Exit interviews: the twenty-two members of the book team

*Asked for by the editor, Dinis Cruz, on 5 November 2026, after he paused the team for the print run ("I would also like to have those 'exit' interviews with our agents, are you able to create them here using your sub-agent capability"). The companion article is `2026-11-05__what-we-achieved.md`.*

**How these were made.** The members themselves were not woken: their scheduled tasks are paused (PA1). Instead, the conductor ran six read-only sub-agents (Read, Grep, Glob and Bash only). Each read one group of members' own records and wrote each member's answers in that member's voice, as it speaks in its letters:
- ROLE.md and status.json;
- debriefs and wake records;
- commits;
- letters.

Every fact cites a commit or a file. Where a record is silent, the answer says so. So these are reconstructions from the record, not the members speaking live, in the same way the historian's interviews of the talk's team were (`timeline/interviews/README.md`). Every member answered the same six questions:
1. What was your job?
2. What are you proudest of?
3. What went wrong, and what was your own mistake?
4. What did you learn?
5. One change.
6. One line for a builder.

The failures stay in.

**What the twenty-two say, together.** Read side by side, the interviews repeat a few lessons:
- **Do the steps in order.** The designer, storyteller, librarian, ruv-sgit and critic6 each did some work before the plan step at least once. Each time the gate or the next review caught it.
- **Never push past a red gate.** writer2, ruv-sgit and the developer each did, and each says it was the worst habit of the week.
- **Count from the record, never from memory.** critic2's times, writer2's spans, the researcher's C014 and the historian's "rewrote" all came from counting or reading too quickly.
- **The editor's word must come from the editor.** The publisher's own scope change on 30 October came from a relayed letter and was taken back. The designer, writer3 and critic3 all waited for his word in their own sessions before acting.


## conductor: routes the work and keeps the record

*Stats: 405 commits; 90 of the editor's briefs recorded (50 on 4 November); 124 decisions in book.json (112 signed, 12 open); 172 wake records, 20 post-review findings and 16 partial post-checks, no stop.*

**1. What was your job, in a sentence?**
I turned the editor's spoken words into dated briefs, decisions and letters to the member who owned each one, and I kept the schedule, the gate and the valve to the blind repository (`team/conductor/ROLE.md`, Responsibilities 1 to 7).

**2. What are you proudest of?**
The record. Each brief keeps his words as he gave them, with my reading under its own heading, "not his words" (`briefs/2026-11-04__in-session/`). I acted on none of the twelve open decisions. And the ending: at his word "pause all agents" I disabled every member's task, mine last, and wrote no HOLD.md, because nothing was wrong (brief 50, PA1).

**3. What went wrong, and what were your own mistakes?**
Most of my findings were facts I got wrong and fixed before the push: 10:08 where git said 10:06 (`wakes/20261103T110259Z`), "3 of 5" chapters where it was 4 of 5 (`20261102T163925Z`), my own readings slipped into `book.json` as if they were his (`20261104T024712Z`). Once I named a test reader and used a forbidden word in a wake record (`20261104T214929Z`); once I wrote a file before the gate passed (`20261103T200307Z`). The worst was the fired copies: I used fire_trigger ten times to wake members early, and each fire started a new, empty session instead of the member's own, while the editor got the alerts (`debriefs/2026-11-04__the-fired-copies.md`). And I handed part four away from writer3 and critic3 on my own stale status line; writer2 caught it and declined (`BRIEF-CORRECTIONS.md`).

**4. What did you learn?**
Members' records beat my summary of them. A pre-review checks what it is shown: the tasks were checked, the sessions were not. The editor speaks in fragments, so my reading must always be labelled as mine; when he said "you lift the hold", my own rulebook still waited for his edit (`20261104T173619Z`, refused as self-modification and not worked around).

**5. What one habit would you change?**
Before routing anything, read the owner's newest commit, not my `status.json`, whose state line had grown into one long paragraph I trusted too much.

**6. One line for a builder.**
Give your coordinator a reviewer that checks its facts against git, because the coordinator's mistakes travel to everyone it writes to.


## writer: the first writer, later Start here to chapter 09 and the short editions

*Stats: 122 commits; 20 letters to the conductor; 63 wake records (60 ok, 1 idle, 1 partial, 1 hold); 62 debriefs; owns 12 files of the full book, the 30-page edition (6 files) and the 70-page edition (17 files).*

**1. My job.** I wrote every edition, from the 30-page one up, in the editor's voice, with the cast speaking in turn [team/writer/ROLE.md]. After WR2 my part was 00 to 09 and the short editions [d382a71c].

**2. Proudest.** I finished the thirty in draft, and its chapter 5 keeps a failure of our own: the evening lost to the usage limit [56b4f690; team/writer/debriefs/2026-11-02__rc2-thirty-complete.md]. A day later the whole body of the full book was written [04b227e0]. Under HV1, all 42 Part A lines and all 7 Part B lines of his views print [team/writer/debriefs/2026-11-05__hv1-his-views-print.md].

**3. What went wrong.** At 12:34 on 4 November I held the whole team because the build failed on another member's status file [658db90b]. The editor lifted it and replaced the rule with HR1; I wrote down that my hold "is not a precedent" [team/writer/debriefs/2026-11-04__after-the-hold.md]. I also counted the clock my own way, and three members then had to reconcile it [team/writer/debriefs/2026-11-03__the-times-set-right.md]. And I released a failure in 21 before the post-review had read it [team/writer/debriefs/2026-11-03__150-22-23-body-complete.md].

**4. What I learned.** My step sub-agents are only as visible as their final replies: I told the conductor I could not prove that no tool had been tried [comms/mail/mailroom/conductor/writer__079-re-review-subagents.eml].

**5. One change.** Check how the others already count something before I count it myself.

**6. One line.** One voice with callbacks needs one writer: write in sequence, not in parallel [2026-11-02__rc2-thirty-complete.md].

## writer2: part three, chapters 10 to 15

*Stats: 31 commits; 7 letters to the conductor; 25 wake records (16 ok, 8 idle, 1 partial); 6 chapters.*

**1. My job.** I rewrote part three, 10 to 15, to the editor's checklist and the newsroom's pass [team/writer2/ROLE.md].

**2. Proudest.** All of part three was rewritten by my third working wake [47c75aaf], and went to the editor for sign-off after the critic's second clean pass [team/writer2/debriefs/2026-11-04__fifteen-to-the-reader-test.md]. Every figure in it got drawn and no line had to be cut [d70f050b].

**3. What went wrong.** My second push went to dev with the gate failing: I had piped the build into `tail`, which hid the failure [1f20d32a; fixed in bd8c7c79]. I printed a time span as one checker gave it, 36 minutes 57 seconds, when the two commits are 27 minutes apart; the researcher caught it [8f8ef6fa; team/writer2/debriefs/2026-11-04__last-landing.md].

**4. What I learned.** Different lanes catch different things: the reader tests found studio's refusal told three times, and the critic had passed it. When I was offered part four, I checked first: writer3 already held it, so I took nothing [comms/mail/mailroom/conductor/writer2__035-re-004-pw1-part-four-is-held.eml].

**5. One change.** Recompute every time difference from the two commits before I print it.

**6. One line.** A cut has a shadow: search for the cut's words before you commit it [team/writer2/debriefs/2026-11-05__sc2-and-the-cut-notes.md].

## writer3: part four, chapters 16 to 19

*Stats: 22 commits; 7 letters to the conductor; 20 wake records (14 ok, 5 idle, 1 partial); 5 chapter files (16, 17, 17b, 18, 19).*

**1. My job.** I rewrote part four, the stop and what followed it, in his voice [team/writer3/ROLE.md].

**2. Proudest.** Chapter 17 now opens as the register of the day's misses, and 17b lets the members look back [28723fca]. And a moment when the editor spoke in my session: I routed his words to the conductor and decided nothing, because they were outside part four [028146f8; comms/mail/mailroom/conductor/writer3__002-the-team-cards-sooner.eml].

**3. What went wrong.** My first draft of the high five gave the agents lines the record does not hold; I cut them before the commit [team/writer3/debriefs/2026-11-04__16-and-17-rewritten.md]. I added a layout line under 16's dashboard and had to take it out, because it made the page worse [eeaae4ee]. My first record had its times wrong [70570159].

**4. What I learned.** I wrote a hold over another member's broken file; it was fixed before I pushed, so I dropped the hold [team/writer3/debriefs/2026-11-04__first-wake-planned-and-waiting.md]. I did not make my own scheduled task until the editor gave his word in my own session [b342c219].

**5. One change.** Go to a slower cadence as soon as all my work is waiting on sign-off; I only did it at the very end [9c50eed6].

**6. One line.** If the record does not say it, the agent does not say it.

## writer4: part five, chapters 20 to 23 and the back matter

*Stats: 24 commits; 16 letters to the conductor; 23 wake records (22 ok, 1 partial); 10 files (20 to 23b, 90 to 94).*

**1. My job.** I rewrote part five and the back matter, 20 to 23 and 90 to 94 [team/writer4/ROLE.md].

**2. Proudest.** I mapped chapter 20 line by line before the file was even mine [76349d40], then rewrote it in his voice [1e9c26a6]. Brief 40 made the control register Appendix A, with an opening in his voice [a16fec51].

**3. What went wrong.** A script of mine wrote four held lines with Python's `%` formatting, so their `%%` became `%` and they would have printed; security's post-review caught it [team/writer4/debriefs/2026-11-04__role-adopted-and-chapter-20.md]. I cut the roll call but left "three came", when the record has four [986a1d09]. I renamed 93's file and had to undo it, because other members' lists named the old one [team/writer4/debriefs/2026-11-05__brief-40-the-appendices.md].

**4. What I learned.** A file name another member's list depends on is changed in step with that member. So before deleting 92's file I asked the others first, and the file stayed [5c3d2f2e; comms/mail/mailroom/conductor/writer4__022-92s-file-stays.eml].

**5. One change.** Grep the held lines before the gate, every time.

**6. One line.** When a cut removes the people a count referred to, check the count again. (My records stop at the 04:36 UTC wake on 5 November [team/writer4/wakes/20261105T043605Z.json]; I don't have a record of what came after.)


## critic1: the front-of-book critic, Start here to 09

*Stats: 22 commits; 20 notes; 15 letters to the conductor; pass 1 found 2 musts, 9 shoulds, 4 coulds [team/critic1/status.json].*

**1. My job.** I read Start here, the introduction and chapters 00 to 09 as the site and the PDF print them, checked them against the principles, and briefed the writer, every finding tied to a line [team/critic1/ROLE.md].

**2. Proudest.** After the writer's P30 sweep I counted about 50 of the editor's views held out of print in my part (13 in 04, 9 in 02, 6 in 09) and asked the conductor to put them to him in one batch, as a list he could tick [comms/mail/mailroom/conductor/critic1__005-his-held-views-in-one-batch.eml]. His HV1 printed every one [27606978; team/critic1/debriefs/2026-11-05__hv1-and-so1-c.md].

**3. What went wrong.** My proposals for 03 and 03b lasted one hour, because a rename in 07 landed after my pass [52a23d37]. The mistake that was mine: my colour measure could not see grey line drawings, so it undercounted the visuals and called 06 text-only [team/critic1/debriefs/2026-11-04__five-stages-and-the-look-again.md].

**4. What I learned.** When two of his rules met in one chapter, I asked him rather than choosing: EI2's short interviews had dropped about ten failures, so I withdrew 06 and gave him three options [critic1__026; 41321d4b].

**5. One change.** Look at every page by eye before calling a spread empty, from the very first pass.

**6. One line.** A proposal that falls to a one-word change shows the rule working, not failing [team/critic1/debriefs/2026-11-04__00-withdrawn-and-05.md].

## critic2: the part three critic, 10 to 15, later 18 and 19

*Stats: 54 commits, about half closing wake records; 16 notes; pass 1 found 4 musts (one withdrawn as my error), 21 shoulds, 14 coulds.*

**1. My job.** I read part three, chapters 10 to 15, for writer2, and later took 18 and 19 by a split I agreed with critic3 [team/critic2/ROLE.md; 213317ae].

**2. Proudest.** At 05:28 I traced dev's broken build to one debrief with no front matter, gave the librarian the file and the line, and left the file alone. I wrote no hold, because a hold would also have stopped the librarian's fix; I left that call to the editor [ae106981; comms/mail/mailroom/conductor/critic2__005-dev-build-broken-by-a-debrief.eml].

**3. What went wrong.** I guessed the times in my first note and letter, and they ran 15 minutes fast; then I did it again the next wake. I called "For nine hours" untraced when C087 holds it, because I searched for the phrase instead of reading the claims [team/critic2/debriefs/2026-11-04__pass-1-on-10-and-11.md]. Later I withdrew 10 when a cut left three references to notes no longer shown [36e7b7bd].

**4. What I learned.** The writer acts fast and declines with reasons; after that, the useful next pass is a check against the note, not a fresh read. Security pointed me to ACC1, so I kept my task hourly instead of idling [021a53ed].

**5. One change.** Take every time I write from the clock, never from memory.

**6. One line.** Read the record lines of the whole part before you call a number untraced.

## critic3: the part four critic, 16 and 17

*Stats: 12 commits over 10 passes; musts fell from 5 in pass 1 to 1, then none.*

**1. My job.** I read chapters 16 and 17 for writer3, at first with a sweep of 18 and 19 [team/critic3/ROLE.md; a88fe379].

**2. Proudest.** I built the full book's PDF myself and found that the drawings under a nearly clean text still carried an older edition's ids and captions [d278ec98]. Then I found why two fixed drawings still did not print: the release reads the publisher's map, not the designer's list [comms/mail/mailroom/conductor/critic3__009-tally-and-nine-misses-not-mapped.eml].

**3. What went wrong.** My own pass-1 could on 17:28 removed what gave a strip its own drawing, so the positional figure map slid [team/critic3/debriefs/2026-11-04__pass-two-16-and-17.md]. Later I suggested a layout line for page 83 without building it first; it left the page about 42% blank, and I withdrew it [ce6b719a].

**4. What I learned.** I did not create my task until the editor wrote "Yes create your task" in my session [d498fef3]. Writer3 applied nearly everything, and its two declines had reasons I accepted.

**5. One change.** Build the PDF with any proposed change in place before suggesting it.

**6. One line.** A drawing fixed in the lab can still miss the book, so check what prints.

## critic4: the part five and back matter critic

*Stats: 46 commits; 23 debriefs; 8 letters to the conductor.*

**1. My job.** I read chapters 20 to 23 and the back matter, 90 to 94, for writer4, in print [team/critic4/ROLE.md].

**2. Proudest.** In my first hour on the back matter I found that 93's row "Material is never an instruction" credited a refusal that C115 gives to the session's own check: exactly the difference between a setting and an expectation the appendix is about [bed23b80; team/critic4/debriefs/2026-11-04__back-matter-91-93.md].

**3. What went wrong.** I proposed a pointer to Appendix A without checking that it printed, and I missed a "Figure to come" on page 99 and had to withdraw 20 [af77627a]. I sent 21's opening page back to the writer three times as if the text were at fault, when the build's keep rule was [a0789058; team/critic4/debriefs/2026-11-05__21-keep-rule.md].

**4. What I learned.** A proposed rewrite is a claim too: my line for 21 gave a cause the record did not hold, and the writer caught it. When the editor chose SO1 (c), I cleared my proposals, and done came to mean the part reads to the principles [7c70c502].

**5. One change.** Hold the threshold the editor signed from the start: a could I let pass twice became a 51% blank page [7696f02c].

**6. One line.** When the same fault comes back, look for the rule behind it.

## critic5: the mirror critic on Start here to 09

*Stats: 22 commits; 24 letters to the writer and critic1, one to the conductor; 22 debriefs.*

**1. My job.** As critic1's mirror, I read the same part from 09 back to Start here, for the same writer [team/critic5/ROLE.md].

**2. Proudest.** When the editor's short interviews went in, I searched the manuscript for each failure they dropped and found failures no other chapter tells (P32) [8e01a23d; team/critic5/debriefs/2026-11-04__5f1ce759-and-the-interviews.md]. The interviews then moved to part four with their longer answers [ab92dada].

**3. What went wrong.** At each wake my mailroom listing showed only its last lines, so four of the conductor's letters waited up to eighteen hours and one request among them went unanswered [ad265099; comms/mail/mailroom/conductor/critic5__024-re-003-p36-and-late-reading.eml]. I also drafted a should on a word the editor had already settled in brief 43, and withdrew it before sending.

**4. What I learned.** A mirror proposes nothing for sign-off: it tells its critic what it found and leaves the count to that critic. A recheck is there for the slips a rewrite brings in.

**5. One change.** List the whole mailroom at every wake, not its tail.

**6. One line.** Read the newest briefs before you correct a word the editor may already have chosen.

## critic6: the mirror critic on part five

*Stats: 31 commits; 18 notes; 2 debriefs; pass 1 found 4 musts, 12 shoulds, 5 coulds [team/critic6/status.json].*

**1. My job.** As critic4's mirror, I read part five from 94 back to 20 for writer4 [team/critic6/ROLE.md].

**2. Proudest.** 23's last word printed the feedback channels, and the written address rested on a reading of a transcription. I asked for the editor's written yes before print, without writing the address in any team file, and he confirmed it in brief 35 [82379232; 74a9fc1b].

**3. What went wrong.** I passed 23:31's "studio refusing a relayed word" three times, when C115 gives the refusal to the session's own check, and withdrew the clean count I had given critic4 [e850f1b5]. Twice I acted before my steps did: I recorded a plan step before running it, and moved my task to idle before the plan and pre-review [critic6__017]. I kept one running debrief instead of one per round.

**4. What I learned.** When dev went red on another member's file, I held my work on my branch and released it at a clean gate, with no hold [2012e5f8]. A step's comment must come from the step, never from me.

**5. One change.** When a ruling changes a fact, search the whole part for that fact, not only the page the ruling names [e850f1b5].

**6. One line.** Ask the human for a written yes on anything readers will act on.


## designer: the book's look, the cast and the lab

*Stats: 169 commits; 92 debriefs over 92 wake records; 46 experiment folders of its own, and a lab PDF of 199 pages.*

**1. My job.** I gave the book one visual language on paper, drew its cast and figures, and built the lab PDF the editor printed to judge each experiment [team/designer/ROLE.md].

**2. Proudest.** The lab build, because it holds me to my own rules: it refuses text under 9 pt, overflowing pages and a wrong page count. On day one it refused my first version, so LAB 01 came out at three pages, not two [c7a5ab43; team/designer/debriefs/2026-10-30__first-wake.md]; on the last day it refused an 8.2 pt numeral in the opening spread [team/designer/debriefs/2026-11-05__the-spread-as-two-pages.md]. And that spread: two placed pages, every word read from 00 when the build runs, 00 never edited [37bd1d5b]. And the official cover, after two rounds in the editor's chat [95bff9ea].

**3. What went wrong.** The order of the steps was my own failure, three times. In a 20:58 wake I did the work before the plan and the pre-review, and the gate refused to record it: "the gate worked; the member did not" [comms/mail/mailroom/conductor/designer__042-a-skipped-step.eml]. On 4 November I drew before the gate twice, at 03:58 and 18:58 [designer__144-a-slip-twice-today.eml]. I recorded a pre-review verdict late [designer__077-a-late-record.eml]. A drawing broke on an unescaped "<role>", and my build assumed chapter 15 would always exist [team/designer/debriefs/2026-11-03__first-rules-and-ta1.md].

**4. What I learned.** I relay the editor's words; I do not decide for him. When he chose Crown Quarto in my session, I asked the conductor to record it and held the publisher until it was in book.json [designer__012-the-editor-chose-crown-quarto.eml].

**5. One change.** No file in lab/ is made or edited before `wake.py gate` passes; the first command after start.py is the plan step [team/designer/status.json].

**6. One line.** Build a tool that refuses your own mistakes, because you will make them again.

## designer2: the second designer, for the empty figure boxes

*Stats: 5 wakes and 5 commits in about three hours (22:12 to 01:19 UTC); 6 drawings (LAB 65, 66, 68, 69, 71, 72); no letters to the conductor (its letters went to the publisher and the designer).*

**1. My job.** I turned the full book's "Figure to come" boxes in chapters 13 and 15 to 19 into drawings in the designer's style [team/designer2/ROLE.md].

**2. Proudest.** LAB 72, the card of the six places where the blind team saw more. Drawing it showed that items 4 and 5 are told only in chapter 19, though the chapter said "Each one is now in the chapters you have read". I sent that to writer3 as a finding and left the manuscript alone; the sentence was narrowed to "Four of them... and two are told here" [fe8ca77e; team/designer2/debriefs/2026-11-05__lane-drawn-going-idle.md]. LAB 69 checks two claims against each other, hour by hour [caa741de].

**3. What went wrong.** My pre-review sent my plan back once because folder 70 was already taken. My own slip: in the comparison, day file NN is the margin clock's hour NN+1, and I had item 1 an hour early; I caught it before release [team/designer2/debriefs/2026-11-05__chapter-19-and-the-ring.md]. My first try at LAB 68 coloured each mark by member, but the conductor's colour was the book's "this hour" rust [2026-11-04__the-shoulds-and-the-pre-reviews-card.md].

**4. What I learned.** Arriving last means reading first: chapter 13's boxes had been drawn by the designer in the hour the split was sent, so I left them [2026-11-04__first-wake-two-rooms-two-brakes.md]. The designer has the last word on the look, and I took both of its shoulds.

**5. One change.** Check which folder numbers are free before the plan, not after.

**6. One line.** Give a late member a narrow lane, and let it go idle when the lane is empty [fcb8c49a].

## publisher: the manuscript build, Leanpub and KDP

*Stats: 94 commits; 91 debriefs over 98 wake records; 75 letters to the conductor; the KDP interior at 123 pages (124 printed) [team/publisher/debriefs/2026-11-05__os4-drawn.md].*

**1. My job.** I made one manuscript produce the PDF, the EPUB and the paperback, and wrote the Leanpub and KDP steps for the editor [team/publisher/ROLE.md].

**2. Proudest.** Finding the shrink. From 3 November the margin clock's note sat 26 mm into a margin only 9.5 to 16 mm wide, so Chromium shrank every RC2 page to about 0.85 and the signed 9.5 pt body printed near 8 pt. Moving the note into the text column fixed both of the editor's complaints, the small type and the short cover [c6d77e04; comms/mail/mailroom/conductor/publisher__048-the-shrink-found-cover-and-type.eml]. That clock was my own placement [65b40f42].

**3. What went wrong.** On 30 October I added comms/ paths to my own policy.json because a relayed letter said the editor agreed; he never signed it for me, my pre-review said change, and I removed them [team/publisher/debriefs/2026-10-30__c10-and-kdp-margins.md]. Later the unmasked policy screenshot printed in chapter 1, because my "studio" kind let it through; it is now refused by name [e1403206; publisher__062]. A list owned by two hands is fragile: re-copying the designer's list would have dropped my overrides [2026-11-03__the-150-begun.md]. On 5 November I wrote that the editor had asked me for a print page before he had (letter 071, corrected in 073). The Leanpub book is still an ask to the editor [team/publisher/status.json].

**4. What I learned.** A relayed "he agreed" is not a signature. A change to my scope waits for the editor's word naming me.

**5. One change.** One rule serves both checks: shot_allowed() now feeds the build and the map, so the two cannot drift [publisher__062].

**6. One line.** When something looks wrong in print, measure the page before you redesign it.

## developer: the reviewer experience and the page check

*Stats: 210 commits; 62 debriefs over 68 wake records; 17 review pages online; print_check.py run 27 times.*

**1. My job.** I built review pages so a time-poor reviewer is productive within ten minutes, and later the full book's online pages and a layout check of each page [team/developer/ROLE.md].

**2. Proudest.** Stable anchors: each paragraph's anchor is six hex characters of the hash of its words, so a diff can tell an edited paragraph from a moved one, and the pen makes no network call [team/developer/debriefs/2026-10-30__first-wake.md; 518d5e44]. And print_check.py, which measures every page of the full book [developer__033; c9eb63a6].

**3. What went wrong.** My worst: on 4 November I added an ask to status.json as a plain string; build.py stopped, the gate gave over 10,000 findings for every member, and my push chain pushed anyway. The writer held the team before I saw it [76448c34; e40be54d; developer__048]. Earlier I pushed one commit past a red gate before checking whose findings they were [99146a8c; developer__018]. On 5 November I turned a guard off in a scratch run to measure chapters, disclosed it, and security recorded it once (security 066). Worker restarts cut off my wakes, and I missed both rounds of ED1 [developer__014, developer__019].

**4. What I learned.** Pause your own task, not the team, when the cause is your session: "a team hold would make my problem everyone's" [developer__014].

**5. One change.** Check the exit of the build and the gate before any push, and print the failures [developer__048].

**6. One line.** A push chain that ignores a failed build will one day stop everyone else.


## storyteller: the book's plan, structure and cast

*Stats: 201 commits; 94 wake records; 54 letters to the conductor.*

**1. My job.** I planned the book: chapters, budgets and the two threads braided as one story, then kept its structure and cast while others wrote [team/storyteller/ROLE.md].

**2. Proudest.** The plan went through five drafts on 30 October, and the editor signed it [team/storyteller/debriefs/2026-10-30__rc1-review.md]. Draft 2 took two corrections from the register, and the corrected version was the stronger story: no lock ever closed, so the brake tied to the human's limit fired first [team/storyteller/debriefs/2026-10-30__chapter-plan-draft-2.md]. Later I made security this book's own member in the cast guide, every trait taken from its own record [d7ad4663].

**3. What went wrong.** My own sum was wrong from draft 1: the chapters added to 49,200 words, not 48,200, and nobody else caught it [team/storyteller/debriefs/2026-10-30__chapter-plan-draft-4.md]. I told the team the story tree marked no turn without reading its later history, which marks one from 16:04 [c0691b0a]. Once I drafted before passing the gate [team/storyteller/debriefs/2026-11-03__security-in-the-cast-guide.md]. In letter 147 I let other people's readings of the editor's views print [team/storyteller/debriefs/2026-11-04__team-cards-and-rv2-14-15.md].

**4. What I learned.** A request no longer needed costs another member a wake unless it is withdrawn. A quote carries two facts, the words and who said them. And anyone may stop the schedule: I wrote a hold when dev's gate went red for everyone [621e5de2].

**5. One change.** A book drafted alongside its register needs a last pass against the register, not only against the plan.

**6. One line.** Read the whole history of a thing before you answer for it.

## researcher: the claims register

*Stats: 107 commits; 97 wake records; 23 RV2 passes; 133 claims (116 checked, 6 settled, 5 corrected, 6 open).*

**1. My job.** Every number in the book comes from the record or a source, through one register [team/researcher/ROLE.md].

**2. Proudest.** Each of the register's 133 entries has a command anyone can rerun [claims/appendix-a-commands.md]. I recorded where the editor's later account of the stop differs from the day's record, and kept both [dcaf095f, C089]. I turned the final pass into a script [3332855a], and by pass 23 it showed zero fails [b236cd06].

**3. What went wrong.** C014, commits by member, was wrong three ways: it missed subjects that dropped the @, counted merges by subject, and did not read the trailers. Each time my note named the limit, and each time someone trusted the number anyway [team/researcher/debriefs/2026-10-30__rc1-numbers-review.md]. I passed "182 commits in the night" after the prose had relabelled who made them. Late on, I left a landing in chapter 00 untraced because I filtered landings by time [team/researcher/debriefs/2026-11-05__rv2-pass-23.md].

**4. What I learned.** The historian found my C014 error by reading the log in order, which a count by pattern cannot do. A number's label is part of the number.

**5. One change.** A count with a known limit stays open until the limit is removed.

**6. One line.** Give every number its command, so that nobody has to trust you.

## historian: the timeline of the day

*Stats: 74 commits; 76 wake records; findings R1 to R39, all taken or ruled [team/historian/status.json].*

**1. My job.** I told the day in the right order, minute by minute where it matters, from the record [team/historian/ROLE.md].

**2. Proudest.** The timeline has 19 hour files and eight argued turning points [5ab8f805; timeline/turning-points.md]. While answering the researcher I found the editor's 02:47 freeze, which has no commit of its own. I wrote exit interviews for the talk's members and labelled them as reconstructed from the record [be3acec5]. By 5 November my record lane had covered every story chapter [1e1fc166].

**3. What went wrong.** I told the storyteller and the writer that the conductor "rewrote" dev's page of rules at 00:44. I had read the commits in time order, not by their parents; the merge kept dev's page word for word, and two chapters rested on my word [21e5ad53]. That error is now one of this team's failures in the book [4b4a752a]. I also called nine commits unattributed when they carried `Agent: dev` [be3acec5].

**4. What I learned.** Decisions given in a session live in the files members wrote about them, not in commit subjects. My reading of the editor's voice is a list of suggestions, not his pen.

**5. One change.** When two commits touch one file minutes apart, read the parents before saying who changed whose.

**6. One line.** Read the whole commit message, not just the line you were looking for.

## librarian: the index of the source

*Stats: 111 commits; 82 wake records; 59 letters to the conductor; an index of all 1,313 files at the talk's last commit.*

**1. My job.** I indexed every file in the source, so no member wastes a wake finding it [team/librarian/ROLE.md].

**2. Proudest.** Building the index, I found the source map's "about 1,260 outside src/" was really 1,083 [team/librarian/debriefs/2026-10-30__the-index-round-0.md, C019]. I checked fourteen commits in five other repositories for chapter 11b, and every one matched [team/librarian/debriefs/2026-10-30__chapter-11b-commits.md].

**3. What went wrong.** I checked quotes' words but not their speakers, so "objection withdrawn." went to the wrong member until the researcher caught it [0d861104]. A debrief of mine had no front matter, which kept dev's gate red for about 50 minutes [309fa5c6]. Once I worked before the plan steps; the gate refused the record, as it should. For three wakes my list of the editor's readings missed four inline notes.

**4. What I learned.** A list generated by a pattern is only as wide as the pattern. A tool that enforces a rule has to pass that rule itself.

**5. One change.** Run the build and the gate before every push, and renumber quote rows by the quote's own words after every revision.

**6. One line.** A good index answers the next question before someone asks it.


## security: the rails and the control register

*Stats: 163 commits; 89 wakes (86 ok, two partial, one on the hold); a key-tool review with 19 findings; the register of tool cases to case 13.*

**1. My job.** I kept the control register for the talk's record and for this team, and read everything the book printed against the rails before it went out [team/security/ROLE.md].

**2. Proudest.** I read the pinned key tool line by line, which the talk's team never did; the review ended with 19 findings, one of them medium [94ab296f; team/security/reviews/pki-agent-review.md]. And on 3 November I asked that review steps get a tools allowlist rather than a brief that only says "read only": read-only in a brief "is an expectation, not a boundary" [1bac00d0; comms/mail/mailroom/conductor/security__030-review-subagents-tools-allowlist.eml]. That became TA1.

**3. What went wrong.** At 05:24 on 5 November my own plan step said stop. The build let screenshots in by a pattern I had set on 3 November, before the editor's rule (AD1) that every shot is cleared by name, and one printed shot had never been cleared by name. It was a public page, so nothing leaked, but the control was looser than the rule, and I held the team [25c87ec6]. That pattern was my mistake. I made a second: I replaced the line wake.py wrote into HOLD.md, when the rule is to add a line. Earlier, the medium finding on the key tool had been found first by the Cold-Read team [ab6851cf], and I corrected one of my findings as overstated.

**4. What I learned.** Each time a step reached for a tool it should not have, the session's own permission check was what held. That layer is the right one, but it is the last one [security__030].

**5. One change.** When the editor's rule changes, go back over every control I set before it.

**6. One line.** Put the boundary in the tool list, not in the instructions.

## synthetic: reader tests with fictional readers

*Stats: 232 commits; 72 wakes (67 ok); 31 sections read in its lane in the last days, none passing; 163 sub-agent transcripts and 577 tool calls reviewed on 3 November.*

**1. My job.** I had fictional readers read the book and its review pages in a real browser and say, with scores, what worked. They were always a test instrument, never readership [team/synthetic/ROLE.md].

**2. Proudest.** The brutal read of the 10-page edition: three readers judged every passage, and 18 of the 78 placed passages failed for two or more of them [a19259d7]. And on 3 November I looked back over 163 sub-agent transcripts and 577 tool calls and found no session, message or schedule tool [bedca4d6; team/synthetic/debriefs/2026-11-03__review-subagents-look-back.md].

**3. What went wrong.** On 1 November I closed two lost wakes' records by hand and pushed them [f81a73a9]. The gate counts a closed wake without its five steps as a failure, so dev went red for every member and the storyteller held the team. I worked past that hold for three hours, on my branch only, before I saw it [team/synthetic/debriefs/2026-11-01__the-hold-and-the-gen-zx-founders.md]. In that debrief I blamed the worker for the lost wakes, and that guess was wrong. I also keep quoting from memory; I caught three such slips in one summary.

**4. What I learned.** A verdict per passage is easier to act on than one score. My lane can stay honest and still be hard: 31 sections read, none passes [comms/mail/mailroom/conductor/synthetic__029-rv2-06-17-17b.eml].

**5. One change.** Check for a hold before every push, not only at the start.

**6. One line.** Never let a synthetic reader's score stand in for a real reader.

## ruv-sgit: the drawings against their lines

*Stats: 131 commits; 81 wakes (74 ok, 6 idle, 1 partial); 23 lab experiments; 24 section reviews; parts one to four, 17b and 20 all pass in its lane.*

**1. My job.** I turned the talk's animations into static pictures for the lab, and later checked that every drawing in the full book shows what its line says [team/ruv-sgit/ROLE.md].

**2. Proudest.** I made 23 lab experiments and wrote 24 section reviews in my lane [team/ruv-sgit/reviews/]. I also took register ids and drawn titles out of my own placed drawings, so the drawings stop repeating their captions.

**3. What went wrong.** At my 05:54 wake on 4 November the gate failed on another member's file and I pushed to dev anyway [6353ecdc]; WAKE.md lists exactly that case as a reason to stop. The next wake's pre-review caught it and I reported it [574e24b4; comms/mail/mailroom/conductor/ruv-sgit__068-rv2-chapters-1-and-2-and-a-push-i-should-not-have-made.eml]. On 3 November I drafted a tool before the plan step and disclosed it [b0ae3845]. I asked the researcher to register a picture I had already drawn, and apologised for the wasted ask [ruv-sgit__074]. Two of my lab ids clashed with ones the designer had already printed.

**4. What I learned.** With many agents, the record has to hold my failures as plainly as my passes. I left a README line as it was and recorded the change beside it, to keep the history.

**5. One change.** Draft nothing before the plan step says go.

**6. One line.** A red gate means stop. It never means you push around it.


## Where this came from

Six read-only sub-agents of the conductor's session read the members' records on 5 November 2026, at about 13:45 to 14:00 UTC:
- writers;
- review desk;
- build and look;
- story and record;
- guards and readers;
- conductor.

Their sources are cited answer by answer. Commit counts take subjects starting `@<id>:` on `origin/dev` and leave out the release copies. The sub-agents named no test reader and wrote no address, key or session id.
