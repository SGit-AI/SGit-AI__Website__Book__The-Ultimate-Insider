# Hours four and five: before dawn

**Cast bar:** six agents: the conductor, dev, deck, ruv-sgit, the researcher, and the designer from 03:41; the editor in the sessions until just after four, then his chair empty.

**Clock:** Hour four.

`%% clock record: 03:00 to 03:59 on 29 October: the conductor's first scheduled wake at 03:03, the researcher's finding at 03:05, the night log at 03:27, dev's rule on pushes at 03:34, the designer at 03:41; clock hours of 29 October (C110; the conductor's CK1).`

## Every member on its own slot

**Narrator.** Hour four is the first hour in which every member that existed woke on its own slot. The conductor's first scheduled wake with a record came at 03:03, and it made deck's programme of experiments the team's queue. Deck's first scheduled wake followed at 03:18, ruv-sgit's second at 03:33, with deck's first experiment delivered in two versions.

**Narrator.** And yet most of the hour's wakes were still mine. I was in the sessions, asking. The schedule ran beside a present editor, not instead of one. The card has the hour.

**Figure:** a card, hour four's wakes by trigger: those the schedule started and those I started.

`%% figure brief: For the designer, from C087 (hour 03 UTC, which is hour four on the margin clock: 5 scheduled, 10 the editor's). The counts on the card only.`

**Conductor** *(on the minute)*: Backlog, then schedule, then work. For everyone. A new ask goes into the schedule, not straight into somebody's hands.

`%% record: team/conductor/wakes/20261029T030304Z.json 8543269 (03:03) 648feee (03:10: "Backlog, then schedule, then execute, for everyone") team/deck/wakes/ (started 03:18:53) e8bd87a (03:33) C087 C110 timeline/day/03.md`
Band: *Dramatised (the conductor's line). Rests on its first scheduled wake and its commit of 03:10; the count is the register's.*

## Two failures, two rules

**Narrator.** Two failures in this hour stay in. Both were caught by the team's own checks after the fact, and in both the answer was a rule, not a retry, written down within the hour.

**Narrator.** The first was the researcher's. In its first round it had captured web pages as evidence for the talk's claims, and pushed them to the team's public repository. At 03:05, in a wake I had asked for, its post-review returned a finding: the captured pages had carried other sites' data in with them, and a check run to find it had printed several to the session log. The researcher redacted it in the files and told me.

**Researcher** *(unbudging, and for once not pleased with itself)*: My own review found it. After the push. A review that runs after the push is a review that runs late.

**Narrator.** That is the lesson the register draws, and it is the right one: redaction does not reach a commit already pushed. The review worked; it worked at the wrong end. Hour five, below, shows what changed.

`%% record: team/researcher/wakes/20261029T030550Z.json (post_review: finding) 59ac8ab C025 (its second entry, and its note: "a story of the controls catching a leak late, not preventing it")`
Band: *Dramatised (the researcher's line). Rests on its wake of 03:05 and the register's account of the finding; told as the team's finding and its rule only.*

**Narrator.** The second was dev's. Its release loop had counted a push the server refused as a push that went through, and commits stayed off the team's branch until dev checked. The rule it wrote at 03:34 is one line, and this book's own team still follows it: a push is done when the commit is on the shared branch, not when the command says so.

**Dev** *(fast, then sheepish)*: The loop said pushed. The branch said otherwise. The branch wins.

`%% record: 6a6be6d (03:34: "a push is done when the commit is in origin/dev") team/dev/ROLE.md at 298be4e (the push rule) timeline/interviews/dev.md`
Band: *Dramatised (dev's line). Rests on dev's commit of 03:34 and the rule in its page.*

**Narrator.** And a third, smaller, the conductor's own: at 03:07 it closed a wake with a correction whose time it had typed by hand, and the time was wrong. From then on, its times came from the clock. Small failures with small rules are the ones most teams never write down.

`%% record: cabcd57 (03:07)`

## The night log

**Narrator.** At 03:27 the conductor gave itself a new duty, and it changed what the record is. At every one of its wakes from then on, it wrote a snapshot of the team and an article about it, regenerated from the team's own files: who woke, what they did, what waits. Not from memory, and not from what anyone said. From the files.

**Conductor** *(pacing, pleased)*: Every round, the team as its files say it is. If the files are wrong, the log is wrong, and somebody will see it.

**Narrator.** It is the page I would have read first if I had woken at six. This book does not cite the log itself; it cites the wakes and commits the log was built from, because the log is a reading and the commits are the record.

**Figure:** the night log's first edition, drawn as a page: the hour, each member's line, what waits on the editor.

`%% figure brief: For the designer. A drawing from the page, not a screenshot: the log sat among the admin pages, which the book never shows.`

`%% record: 794008c 3616efc (03:27 to 03:29) team/conductor/night/20261029T0327.json timeline/README.md (the timeline cites the wakes and commits beneath the log)`
Band: *Dramatised (the conductor's line). Rests on its commits of 03:27 to 03:29.*

## The designer arrives, and my last word of the night

**Narrator.** At 03:41 the sixth member joined: the designer, with its role, its policy, its key, its own task at :39, and a first design note, all in its first session. Its first scheduled wake, a minute later, had nothing to do: the session that made it had already done the hour's work. It said so, and closed idle.

**Designer** *(beret and pencil, exacting)*: Idle is a true answer. I will not invent work to fill a slot.

**Narrator.** At 04:02 I asked for one more wake, in the designer's session, and agreed its policy. That commit, at 04:03, is my last word of the night. The next is at about ten to two in the afternoon. The record does not say where I went, and I am not going to tell you either: it does not matter. What matters is what happened while I was gone.

`%% for the editor: "I am not going to tell you either: it does not matter" is the writer's; his to keep or drop. The thirty says only "The record does not say where I went."`

`%% record: c6dcf89 (03:41) 09c02ff (03:42, idle) f448345 (04:03, the editor agrees the designer's policy) team/designer/wakes/ (started 04:02:56) C011`
Band: *Dramatised (the designer's line). Rests on its first commit and its idle first wake; my last word of the night is the commit of 04:03.*

## Hour five: the schedule alone

**Clock:** Hour five.

`%% clock record: 04:00 to 04:59 on 29 October: the researcher's wake at 04:10, its dispute at 04:11, deck holding its next request at 04:19; clock hours of 29 October (C110; the conductor's CK1).`

**Narrator.** From four o'clock, every wake in the record is scheduled but one, and every one closes with all five steps. The team settles into the order the schedule set: the conductor plans the hour, the researcher gathers, deck reviews and holds, ruv-sgit makes, the designer notes, dev builds.

**Figure:** a card, hour five's wakes by trigger: almost all the schedule's.

`%% figure brief: For the designer, from C087 (hour 04 UTC, which is hour five on the margin clock: 6 scheduled, 1 the editor's). The counts on the card only.`

`%% record: C087 C110 timeline/day/04.md ("What the hour shows")`

### Deck holds itself back

**Narrator.** Just after four, deck had a second request ready for ruv-sgit and planned to send it. Its reviewer pointed out that ruv-sgit already had one of deck's requests in flight.

**Deck** *(a little put out, then fair)*: One at a time, then. I will wait until the first one comes back.

**Narrator.** It is the first sign in the record of members pacing each other, rather than the conductor pacing them. And it came from a review, not from a rule anyone had written for it.

`%% record: aeffbf9 (04:19) team/deck/wakes/20261029T041822Z.json team/deck/debriefs/2026-10-29__e01-review.md`
Band: *Dramatised. Rests on deck's wake of 04:18 and its commit of 04:19: its reviewer asked it to hold the second request while the first was in flight.*

### The argument with a reviewer

**Narrator.** At ten past four the researcher woke on its own slot for the first time, and its wake holds two scenes. The first is an argument. It planned to write a file of my decisions, and its reviewer read the plan and said no: that file, it said, was outside the researcher's rules.

**Researcher** *(unbudging)*: My reviewer said a file was not mine to change. I showed it was.

**Researcher** *(pointing at its own page of rules)*: It sits in my evidence folder. My rules let me write there. I am not asking for an exception; I am asking you to read the line again.

*Reviewer (the clipboard):* "objection withdrawn." *(record)*

**Narrator.** The argument is in the wake record, both halves of it. A reviewer that can be argued with, on the record, by pointing at the rules, is a reviewer doing its job. So is a member that argues by pointing at the rules and not at its own certainty.

**Figure:** ruv-sgit's two-panel reviewer card (`lab/experiments/30-ruv-the-reviewer-card/card.svg`).

`%% record: C107 af0010b team/researcher/wakes/20261029T041003Z.json`
Band: *Dramatised. Rests on the researcher's wake at 04:11; the reviewer's words are its own.*

### The same failure, caught in time

**Narrator.** The second scene in the same wake is the one I would put in front of anyone building a team like this. The researcher's post-review returned a finding of the same kind as the one at 03:05: more of other sites' data, captured along with a page. The card has the register's count.

**Figure:** a card, the researcher's two findings of the small hours side by side: at 03:05, found after the push; at 04:10, found before the close, the values counted, the files redacted in the same wake, none left.

`%% figure brief: For the designer, from C025 (04:10: 28 values; 30 files redacted in the same wake, 0 left). The counts on the card only. Rail: nothing of what was captured, how, or from where; no value, site or field shown.`

**Narrator.** This time the finding came before the close, and the files were redacted in the same wake. The control did not change. The reviewer was the same kind of reviewer, with the same brief, at the same step. What changed was the member's practice: it was looking for the thing it had already been caught on once.

**Researcher** *(unbudging, quietly)*: Same kind of mistake. Found before the close this time, and redacted in the same wake.

**Narrator.** Hold on to that difference, and to its limit. A check after the push finds what has already gone out. A member looking for the thing it was caught on last time found this one before its wake closed. It did not make the team safe: later in the morning, at 06:14, the researcher found a third case of the same kind, and that one had gone out in the first push, like the case at 03:05. Found late again. Part 4 counts them all, and keeps them all in.

`%% record: team/researcher/wakes/20261029T041003Z.json (post_review: finding) 1ef6675 (04:10) C025 (its third entry, found before the close, redacted in the same wake; its fourth entry, 06:14, found after the push) timeline/day/04.md ("The control did not change; the member's practice did.")`
Band: *Dramatised (the researcher's line). Rests on its wake of 04:10 and the register's account; told as the team's finding and its rule only.*

## Six agents, a clock and a brake

**Narrator.** So by four in the morning there were six agents, a clock and a brake. A factory that could run without me. From just after four, it did.

**Figure:** the cast bar at four in the morning: six cards lit, three greyed, one empty chair.

**Map:** the factory as a value chain: what I wanted at the top; the slides, the site and the player; the agents; and at the bottom the agent tool, the build, the check and the brief at the ordinary end, and the hold at the new end.

*Words for this page:* a **Wardley map** is a picture that shows what something depends on and how settled each part is.

`%% figure brief: Named here: this kind of picture is a Wardley map. The hold at the new end, the build and the check at the ordinary end.`

**Figure:** hours one to five on the margin clock: each hour's commits, and its wakes by trigger where the register has them by hour (from hour three, when wake records began).

`%% figure brief: For the designer, from C095 (commits by hour, claims/talk-commits-by-member-hour.md) and C087 (wakes by trigger, by hour). The part's infographic; the counts in the picture only.`

`%% record: C011 C087 C095 C110 timeline/day/00.md to 04.md manuscript/rc2/30/02-the-factory-is-assembled.md ("So by four in the morning there were six agents, a clock and a brake.")`
Band: *The narrator's close is kept from the 30-page edition; the counts are the register's.*

## Do this now

*Write your one page of rules: what your agent is for, what it may change, and when it must stop and ask you. Then write your hold: one file that stops everything, and the name of the one person who may lift it.*

---

## Where this came from

The talk's repository at the end of the day: the conductor's first scheduled wake, its rule on asks and its night log; the researcher's wakes of 03:05 and 04:10, with their findings and its dispute; dev's rule on pushes; the conductor's correction of a typed time; the designer's arrival and its idle first wake; my last word of the night; deck holding its next request. The historian's account of hours four and five. The register for the members, the wakes by trigger, the commits by hour and the post-review findings. ruv-sgit's reviewer card. The storyteller's outline for this chapter. The narrator's close and the scenes of the reviewer and of deck's hold are kept from the 30- and 70-page editions.

`%% record: talk repository at 298be4e: 8543269 648feee e8bd87a 59ac8ab cabcd57 794008c 3616efc 6a6be6d c6dcf89 09c02ff f448345 aeffbf9 af0010b 1ef6675 team/conductor/wakes/20261029T030304Z.json team/researcher/wakes/20261029T030550Z.json team/researcher/wakes/20261029T041003Z.json team/deck/wakes/20261029T041822Z.json; timeline/day/03.md 04.md; claims/register.json C011 C025 C087 C095 C107 C110; lab/experiments/30-ruv-the-reviewer-card/; chapter-plan/edition-150-outline.md part 2 chapter 8; manuscript/rc2/30/02-the-factory-is-assembled.md 03-the-factory-runs.md; manuscript/rc2/70/06-talking-through-git.md`
