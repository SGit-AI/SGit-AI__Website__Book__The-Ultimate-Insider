# The clock, the five steps, and a reviewer of the same kind

**Cast bar:** the four within the hour, and the researcher from about two (C011). The conductor at the centre of this chapter.

## The clock and the five steps

**Clock:** Hours two to three.

`%% clock record: 01:39 to 02:18; clock hours of 29 October (C110; the conductor's CK1).`

**Narrator.** In the small hours, the conductor built the machinery that let me leave them alone.

**Conductor** *(on the minute)*: A clock: each member wakes at its own minute. A hold anyone can pull. And every piece of work goes the same way: plan it, have the plan checked, do it, have it checked, check it went to plan.

*Words for this page:* a **wake** is one turn of work by one agent, on its own clock. A **reviewer** is a second agent that reads the plan before the work and the result after it. A **debrief** is the short note an agent writes at the end of each wake. A **wake record** is the file each wake leaves behind, with every step's verdict and a sentence on why.

**Narrator.** Five steps, in plain words: plan it; have the plan checked; do it; have it checked; check it went to plan. That was the rule for every member, every wake. If a check said stop, the work stopped. It looks slow written down. The checking is what let nobody watch.

**Figure:** the five-step wake on the clock, as in the 30-page edition, with one real wake's verdicts filled in around it: go, go, partial, finding, partial.

`%% figure brief: The chapter's infographic, for the designer.`

`%% record: C071 C022 09f13d5 8c66751 5700bab`
Band: *Dramatised. Rests on the hourly schedule (01:39) and the five-step wake and its rules (02:16 to 02:18).*

## One wake, start to finish

**Clock:** Hour three.

`%% clock record: 02:14 to 02:19; clock hours of 29 October (C110; the conductor's CK1).`

**Narrator.** Here is one wake record, walked through step by step, because it is the first one there ever was, and because it did not go perfectly. It is the conductor's, from 02:14 in the morning, and its job was to build the five-step wake itself.

**Narrator.** *Step one, the plan.* The conductor wrote what it would do: the new section in the wake rules, the briefs for the reviewers, a tool that checks every wake record has all five steps, one line in the page of rules about the five steps, at my word (the hold had gone into it at 01:39, in an earlier commit). And something else is in the plan's own words: "Amended after the pre-review's change, all five conditions adopted". The reviewer had sent the plan back once. One oddity for anyone who opens the file: the record keeps that first "change" in its history with a later time stamp than the "go", 02:17 against 02:16; the debrief tells it in the order here.

**Conductor** *(pacing, a little stung)*: My first plan went back with conditions. I took every one. Then it said go.

**Narrator.** *Step two, the pre-review.* A second agent, briefed as security, read the amended plan against the conductor's scope and the rules. Its verdict was go, with conditions of its own: keep the line in the page of rules named as outside the conductor's scope, check before touching any vault, ask dev rather than editing dev's gate.

**Narrator.** *Step three, the work.* Partial. The conductor did nearly all of it, and wrote down plainly what it did not do and why: one vault it was meant to register was not on the server yet, so it could not be checked, so it was not touched. The condition held.

**Conductor** *(on the minute)*: Partial is a true answer. Done would have been a nicer one.

**Narrator.** *Step four, the post-review.* The reviewer read what had changed. It found the build clean, the checks clean, no secret anywhere. And one thing wrong: the conductor had changed the page of rules itself, a file outside its own scope. I had allowed it, but the commit did not say so, and the plan had made saying so a condition.

*Reviewer (a second agent with a checker's brief, drawn as a clipboard):* "Name it in the debrief or record." *(record)*

**Narrator.** *Step five, the post-check.* The conductor's own check, against its own plan, item by item: three done, one not done for the reason already given, every condition kept, the finding answered in the debrief. Verdict: partial. Not "as planned". It did not round itself up.

**Conductor** *(worried, then calm)*: Caught by the reviewer I invented. Good. But know what it is: "a second reading, not a second identity." *(record)*

**Figure:** the wake record as a page: five boxes in a column, each with its step, who ran it, its verdict and its sentence, the finding in step four highlighted.

`%% figure brief: For the designer, from the record word for word.`

`%% record: team/conductor/wakes/20261029T021416Z.json at 298be4e (plan 02:14:53, pre_review 02:16:07, work 02:18:19, post_review 02:19:05, post_check 02:19:34) 5700bab c8f6f8f team/conductor/debriefs/2026-10-29__the-five-step-wake.md C022`
Band: *Dramatised. Every step, verdict and quoted line is from the conductor's first wake record, 02:14 to 02:19, and its debrief; the conductor's other lines are ours.*

## What a reviewer is, and what it is not

**Narrator.** I keep coming back to that line, and I want to give it its full weight here.

**Narrator.** The reviewer in that wake was real work. It sent a plan back. It found a real slip. Through the day, reviewers like it sent plans back and raised findings, in every member's wakes, and each one is in a wake record, with a verdict and a sentence (C023, C025).

**Narrator.** But the reviewer was the same kind of thing as the member it reviewed: another agent, sharing the session's reach. The conductor's debrief says it in so many words: "The reviewers share the session's reach". A second reading catches the mistakes the first reading made. It does not stand outside the team. If the member had been steered into doing something else, the reviewer would have been reading with the same eyes, in the same room.

**Narrator.** The member whose job was to stand outside was security. Its chair was empty all day. Part 4 is where I ask what that means for a factory you leave running, and what does contain it. Here, take the narrower lesson: build the second reading, because it works, and never call it a wall.

**Map:** the factory as a value chain, as in the 30-page edition's chapter 2: what I wanted at the top; the slides, the site and the player; the agents; and at the bottom the agent tool, the build, the check and the brief at the ordinary end, the hold at the new end.

*Words for this page:* a **Wardley map** is a picture that shows what something depends on and how settled each part is.

`%% figure brief: Named here: this kind of picture is a Wardley map, which shows what something depends on and how settled each part is.`

`%% record: team/conductor/debriefs/2026-10-29__the-five-step-wake.md ("The reviewers share the session's reach: a second reading, not a second identity.") C022 timeline/interviews/security.md claims/ps1-sources.md section 4`
Band: *The conductor's debrief of 02:19; the reviews of the day in the members' own wake records.*

## Do this now

*Name your hold, and write down who may lift it. Then give your agent a reviewer: a second session, with a checker's brief, that reads the plan before the work and the result after. Write at the top of its brief what it cannot do.*

---

## Where this came from

The talk's repository at the end of the day: the schedule, the five-step wake and its rules, the conductor's first wake record and its debrief. The researcher's register for the minutes and the wake records. The historian's account of the empty chair. The storyteller's outline for this chapter. This chapter grows from the 30-page edition's chapter 2, sections 4 and 5.

`%% record: talk repository at 298be4e: 09f13d5 8c66751 5700bab c8f6f8f team/conductor/wakes/20261029T021416Z.json team/conductor/debriefs/2026-10-29__the-five-step-wake.md; claims/register.json C022 C071; timeline/cast-scenes.md scene 2; timeline/interviews/security.md; chapter-plan/edition-70-outline.md part 2 chapter 5; manuscript/rc2/30/02-the-factory-is-assembled.md`
