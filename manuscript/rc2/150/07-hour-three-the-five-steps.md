# Hour three: the five steps, and the first to be caught

**Cast bar:** the conductor at the centre; dev, deck, ruv-sgit and the researcher around it; the editor in every session.

**Clock:** Hour three.

`%% clock record: 02:00 to 02:59 on 29 October: the five-step wake from 02:14, the first caught at 02:19, the first scheduled wake with a record at 02:33, the freeze at 02:47, the gate's record check at 02:51; clock hours of 29 October (C110; the conductor's CK1).`

## A wake that checks itself

**Narrator.** By two in the morning the team had a clock and a hold. What it did not have was a rule for what happens inside a wake. In this hour the conductor wrote one, and the first wake to follow it was the wake that wrote it.

*Words for this page:* a **reviewer** is a second agent that reads the plan before the work and the result after it. A **wake record** is the file each wake leaves behind, with every step's verdict and a sentence on why.

**Narrator.** I asked for a rule for what happens inside a session, and the conductor wrote one within the hour. Within minutes its tool would refuse work until both the plan and its review said go, and the steps were in the wake rules, with a brief for each reviewer.

`%% for the editor (his view, held out of print until he confirms it, P30): the newsroom's "not because I expected the agents to misbehave" (critic5 002).`

**Conductor** *(on the minute)*: Plan it, have the plan checked, do it, have it checked, check it went to plan. And the tool will not let anyone skip to the third.

`%% record: team/conductor/wakes/20261029T021416Z.json (opened 02:14:16) 8c66751 (02:16, wake.py: work refused before plan and pre-review both say go) 5700bab (02:18, the steps in WAKE.md, the review briefs, wake.py check) timeline/day/02.md`
`%% band: Dramatised (the conductor's line). Rests on the first wake record and the two commits that built the steps.`
*Dramatised.*

## One wake, start to finish

**Narrator.** Here is that first wake record, walked through, because it is the first one there ever was and because it did not go perfectly. Its job was to build the five-step wake itself.

**Conductor**: Step one, the plan. I wrote what I would do: the new section in the wake rules, the briefs for the reviewers, a tool that checks every wake record has all five steps, and one line in the page of rules about the five steps, at the editor's word. My first plan went back with conditions. I took every one: "Amended after the pre-review's change, all five conditions adopted". Then it said go.

`%% record: the record keeps that first "change" with a later time stamp than the "go", 02:17 against 02:16; the debrief tells it in the order here (moved out of the reading text, P4).`

**Narrator.** *Step two, the pre-review.* A second agent, briefed as security, read the amended plan against the conductor's scope and the rules. Its verdict was go, with conditions of its own: keep the line in the page of rules named as outside the conductor's scope, check before touching any vault, ask dev rather than editing dev's gate.

**Conductor** *(on the minute)*: Step three, the work: partial. One vault I was meant to register was not on the server yet, so I could not check it, so I did not touch it. The condition held. Partial is a true answer; done would have been a nicer one.

**Narrator.** *Step four, the post-review.* The reviewer read what had changed. It found the build clean, the checks clean, no secret anywhere. And one thing wrong: the conductor had changed the page of rules, a file every member follows and one outside the conductor's own scope. I had allowed it, but the commit did not say so, and the plan had made saying so a condition.

*Reviewer (a second agent with a checker's brief, drawn as a clipboard):* "Name it in the debrief or record." *(record)*

**Conductor**: Step five, my own check against my own plan, item by item: the finding answered in the debrief and the closing commit, every condition kept. Verdict: partial, not "as planned". The wake closed partial, and the next commit named the edit. Caught by the reviewer I invented. Good. But know what it is: "a second reading, not a second identity." *(record)*

**Narrator.** The review caught its own author on the first run. It is also the first entry in the register's list of what the day's post-reviews found and what each fixed.

**Figure:** the wake record as a page: five boxes in a column, each with its step, who ran it, its verdict and its sentence, the finding in step four highlighted; the verdicts of this hour's first wake filled in: go, go, partial, finding, partial.

`%% figure brief: For the designer, from the record word for word. The chapter's picture, as the seventy's chapter 5 drew it.`

`%% record: team/conductor/wakes/20261029T021416Z.json at 298be4e (plan 02:14:53, pre_review 02:16:07, work 02:18:19, post_review 02:19:05, post_check 02:19:34) 5700bab c8f6f8f team/conductor/debriefs/2026-10-29__the-five-step-wake.md timeline/day/02.md ("What the hour shows": the historian's reading, "the strongest early evidence that the steps were more than ceremony") C025 (its first entry: "CLAUDE.md written outside the conductor's scope ... not named in the commit message")`
`%% band: Dramatised. Every step, verdict and quoted line is from the conductor's first wake record, 02:14 to 02:19, and its debrief; that it is the strongest early sign the steps were more than ceremony is the historian's reading of the hour; the conductor's other lines are ours.`
*Dramatised.*

## A rule becomes a setting

**Narrator.** A rule one member writes is a rule one member follows. What happened next turned it into something else.

**Narrator.** Later in the hour dev's first scheduled wake began, at its own minute, and the conductor's request was in its mail: put the check for wake records into the gate. Dev did. From then on, a closed wake record that skipped a step, or recorded work without two go verdicts before it, failed the gate, and not only for the member that skipped. For every member. Dev tested it the way a check should be tested, with a record it knew was wrong, and the gate found every missing step.

**Dev**: It changes the gate for everyone. I said so in the commit, and I ran the whole gate before I pushed.

**Narrator.** That last line is the pre-review's, made into dev's habit: the reviewer had set it as a condition, because a change to the gate is a change to every member's day. And dev's own post-check, run by a sub-agent briefed as the conductor, still closed the wake partial, because one file it had planned to change was not in the diff when it looked. The check that had just become everyone's was applied, the same minute, to the one who built it.

**Figure:** one rule's journey in an hour: written in the conductor's wake rules, asked of dev by mail, in the gate within the hour, and from then on a red mark on any member's release whose wake skipped a step.

`%% figure brief: For the designer. A line of time across hour three, with the rule moving from a page to a setting. The times in the picture, not in any line.`

`%% record: team/dev/wakes/20261029T024849Z.json (started 02:48:49; pre_review condition: "wake.py check in validate.py changes the gate for every member: say so in the debrief and commit, run the full gate before pushing"; post_check partial) 99aaf05 (02:51: "a closed wake record that skipped a step, or recorded work without two go verdicts before it, fails the gate for every member (negative control ...)") cf4ca8b timeline/day/02.md ("What the hour shows")`
`%% band: Dramatised (dev's line). Rests on dev's first scheduled wake, its commit at 02:51 and its wake record.`
*Dramatised.*

## The first scheduled wake, and the schedule beside me

**Narrator.** The first wake in the record that the clock started, and not me, is not the conductor's. It is ruv-sgit's, at its own minute. The conductor's earlier wake that hour left only a commit, because wake records did not exist yet.

**Narrator.** ruv-sgit's first scheduled wake was small and complete: answer the conductor's onboarding request, make and publish its session key, add a second-pass mode to its runner. Every step is recorded, and every verdict is the one you would want: go, go, done, clean, as planned.

`%% for the editor (his view, held out of print until he confirms it, P30): "Looking back, I think this is the strongest early sign that the steps were more than ceremony" after "on the first run" (critic1 001's proposal; the historian's reading agrees, timeline/day/02.md).`

**ruv-sgit** *(not looking up)*: The clock said go. So I went. Small things, every step, then back to the bench.

**Narrator.** But the clock was not in charge yet. I was still awake and in the sessions, asking, and most of the hour's work was started by me. The schedule ran beside me, not instead of me. That changes in hour five.

**Figure:** a card, hour three's wakes by trigger: those the schedule started and those I started.

`%% figure brief: For the designer, from C087 (hour 02 UTC, which is hour three on the margin clock: 2 scheduled, 5 the editor's). The counts on the card only.`

`%% record: team/ruv-sgit/wakes/20261029T023328Z.json (kind "scheduled, hourly at :32"; started 02:33:28) 0d13c43 (02:37: "wake closed: five steps recorded (go, go, done, clean, as-planned)") c81df64 (02:05, the conductor's 02:02 wake, no record) C087 C110`
`%% band: Dramatised (ruv-sgit's line). Rests on its first scheduled wake record and its closing commit; the count is the register's.`
*Dramatised.*

## The freeze

**Narrator.** One more thing happened in this hour, and it was mine.

**Narrator.** The researcher had delivered its first round of evidence earlier in the hour: the talk's claims graded, the incidents gathered, and a list of changes to make to the talk before I gave it. Deck took the first items on it. Then, in deck's session, I froze the talk. My words, as deck wrote them down:

> "do not touch the deck. talk.json and the slides are frozen from now on" *(record)*

**Narrator.** Five minutes later, the researcher proposed the rest of its list to deck, as exact replacement text. One of the items was a number on the talk's definition slide, which the researcher now had a newer source for. It arrived just after a freeze I had set. Deck recorded the rest of the list as not acted on, because of the freeze.

**Researcher**: The text is exact. Apply it, or say why not. It is in the record either way.

**Narrator.** Deck turned the freeze into a programme of experiments within the hour. What it cost is a story for part four, because the cost did not show until the afternoon. The shape of it: a correction that was right, delivered on time by its own clock, and five minutes late by mine.

`%% for the editor (his view, held out of print until he confirms it, P30): the writer's "I do not regret the freeze: I wanted the night spent on experiments, not on re-cutting a talk I had not yet seen whole", in place of the paragraph's first sentence.`

`%% record: 75ddb3e (02:10, the researcher's first round) 79b6709 (02:20, deck's first items; C031: "after deck had already released the earlier items of the same list at 02:20") team/deck/requests/researcher__before-tonight.md (deck's 03:00 update, quoting the editor at 02:47) 91772e6 (D01) a082c52 (02:52, the exact text) 60af587 (02:52, the programme, in the wake opened at 02:47) C031 (its beginning: the proposal five minutes after the freeze; its cost is told in part 4)`
`%% band: Dramatised (the researcher's line). My words are as deck recorded them; the times are the commits'.`
*Dramatised.*

## What the hour leaves

**Narrator.** By three in the morning, every piece of work on the team went the same way, and a skipped step stopped the release of whoever skipped it. A reviewer had caught its own author. The clock had started its first wake. And I had made a decision whose cost nobody could yet see.

**Narrator.** The reviewer's line from this hour comes back later: a second reading, not a second identity. Through the day, reviewers like it sent plans back and found real things, and each one is in a wake record. But the reviewer was the same kind of thing as the member it reviewed, sharing the same session's reach. Part four asks what that means.

## Something to try

*The five steps only mattered because a check read them.*

*If your agents keep a record of each run, a check that reads it can stop a release when a step is missing. One way to test that check is with a record you know is wrong.*

`%% record: team/conductor/from-newsroom/2026-11-04__do-this-now-as-invitations.md (chapter 7, the proposed card); chapter-plan/cast/cast-guide.md (page conventions 1)`

---

## Where this came from

The talk's repository at the end of the day: the conductor's first five-step wake record, its commits and its debrief; dev's first scheduled wake and its commit putting the record check in the gate; ruv-sgit's first scheduled wake; the researcher's first round and its proposal; deck's update quoting my freeze, and its programme. The historian's account of hour three. The register for the post-review findings, the wakes by trigger, the correction and the freeze. The storyteller's outline for this chapter. This chapter keeps the 70-page edition's walk through one wake record (chapter 5) as written.

`%% record: talk repository at 298be4e: 8c66751 5700bab c8f6f8f 99aaf05 cf4ca8b 0d13c43 c81df64 75ddb3e 79b6709 a082c52 60af587 91772e6 team/conductor/wakes/20261029T021416Z.json team/dev/wakes/20261029T024849Z.json team/ruv-sgit/wakes/20261029T023328Z.json team/conductor/debriefs/2026-10-29__the-five-step-wake.md team/deck/requests/researcher__before-tonight.md; timeline/day/02.md; claims/register.json C025 C031 C087 C110; chapter-plan/edition-150-outline.md part 2 chapter 7; manuscript/rc2/70/05-the-clock-and-one-wake.md`
