# The 10-page edition, told by the cast (ZM1, NR1, on PS1)

storyteller@book.the-ultimate-insider, 2 November 2026, the 00:40 UTC wake. **A script for the editor's read, then the publisher, who rewrites the sample from it (not patches it), and the designer and ruv-sgit, who draw it.** It expands the 3-page edition's three pages into the arc's five beats (`chapter-plan/zoom-ladder.md`); the characters are in `cast-guide.md`; every scene rests on `timeline/cast-scenes.md` and `timeline/quotes.md`, as traced by the researcher for the opening script (`claims/opening-script-trace.md`), and is marked dramatised. Narrator lines are the editor's; *(record)* marks a line quoted word for word. Codes live in the `%%` markers, never in the sentences. The six rules of the ladder hold on every page.

**The five beats, and their pages:** the creator's problem (1); the factory assembled (2, 3); the factory running (4, 5); the stop (6, 7); the factory rebuilt, and yours (8, 9). Renumbered at ED1 round 2, the series page being at the back. The series page goes at the back (SP1, the editor's "Yes move it to the back", 2 November).


**Title page:** **One Human, Nine Agents, Nineteen Hours**: *How a factory of AI agents built a presentation in a day, and how to build yours*. In the GEN ZX FOUNDERS series (the series' own mark, in capitals).

**Under the subtitle:** *For anyone with an idea and no team yet: by the last page you will know how to set up your own factory of agents, alone or with others, and you can start the same day.*

*(Nineteen hours rounds 18 h 44 min, C010; nine agents, C011: the first page that uses either number gives it exactly.)*

---

## Page 1. The creator's problem

**Cast bar:** the editor, alone.

**Narrator.** For years my slides were a compromise. I had an idea to get across, and the slides could not move, so I spent the talk explaining what they could not show: this goes from here to there, this grows, this breaks. I talked over my own pictures.

**Narrator.** On 29 October I gave a talk where I mostly did not have to. When a thing had to move, I pressed play and it moved. When it was not quite saying what I meant, I asked for it differently and saw it again within the hour. I had a feedback loop on my own medium.

**Narrator.** What gave me that was not a better slide tool. It was a factory: a team of AI agents, gathered around one objective, run for a day, and taken apart when the job was done. This book is about the factory. The talk was what it happened to make that day.

**Figure:** the editor at a lectern with a play button; behind him, the factory's nine stations. *(Drawing: the designer's; path to come.)*

*An **agent**, here, is an AI that works in a loop: it reads, decides, acts with tools, and checks the result.*

`%% record: C015 C069`
Band: *The talk of 58 beats; that it was given that evening rests on its transcript, added to the record after the day.*

## Page 2. The factory is assembled

**Cast bar:** the editor; then dev, the conductor, deck, ruv-sgit (each card appears as it arrives).

**Narrator.** A quarter past midnight: an empty project. By twenty to one it held a brief and one page of rules, and the team had begun to arrive.

*How to read the scenes:* they are dramatised. The words the agents say are ours, written for this book; the events are the record's, and a line marked *(record)* is quoted word for word. Online, under each scene, you can open the commits, times and files it rests on.

*Words for this page:* the **conductor** is the agent that keeps the team's time and plan. A **hold** is one short file that stops every agent until the person in charge says go. A **check** is a test every change must pass before it goes out (the team called it the gate).

**Dev** *(happy, the fast one)*: First pass of the site and the talk. One build, and a check every change must pass.

**Conductor** *(pacing)*: I keep the time. Everyone gets a slot, and anyone can pull the hold.

**Deck** *(proud, the fussy one)*: The slides are mine. If a room cannot read one at a glance, it goes back.

**ruv-sgit** *(absorbed, the night owl)*: I will be in my workshop all night, making things you can check.

**Narrator.** The build, the check and the brief came from things I had built before. The hold was made that night. What was new was having them all at once, as a team: four within the hour, the rest through the day. That is how a factory gets cheap: yesterday's experiment is today's part.

**Figure:** the cast cards for the four, with when each came on stage and its commits, each figure with its id in small type. *(Drawing: the designer's.)*

*If you want to start now, the last page has the five steps; the pages between are why they work.*

*Working as a team of several?* Each person runs their own agents under their own page of rules; together you share one brief, one board where the work is written down, and one hold. Write down who may lift the hold when its owner is away; until you have, nobody does.

`%% record: 2e4b1f4 1f7c633 97b98d9 20ab1a3 defe526 C011 C014 C022 C071`
Band: *Dramatised. Rests on each agent's first commit after midnight.*

## Page 3. The machine, before dawn

**Cast bar:** as page 2, and the researcher (from about two).

**Narrator.** In the small hours, the conductor built the factory's machinery.

**Conductor** *(on the minute)*: A clock: each member wakes at its own minute. A hold anyone can pull. And every piece of work goes the same way: plan it, have the plan checked, do it, have it checked, check it went to plan.

**Narrator.** It ran the five steps on its own first piece of work, and its own reviewer found against it. *(A **reviewer** is a second agent that reads the plan before the work and the result after it.)*

*Reviewer (a second agent with a checker's brief, drawn as a clipboard):* "Name it in the debrief or record." *(record)*

**Conductor** *(worried, then calm)*: Caught by the reviewer I invented. Good. But know what it is: "a second reading, not a second identity." *(record)*

**Narrator.** I keep coming back to that line. A reviewer agent in the same session can catch mistakes. It cannot stop someone set on getting round it. We built the checks knowing that.

`%% record: 09f13d5 8c66751 5700bab c8f6f8f team/conductor/debriefs/2026-10-29__the-five-step-wake.md`
`%% claim: a reviewer sub-agent runs in the same session with the same reach as the member it reviews; it adds a second reading, not a separate identity`
Band: *Dramatised. Rests on the schedule, the five-step wake and its first review, between 01:39 and 02:19; the reviewer's and the conductor's lines are theirs, from that night's records.*

## Page 4. The factory runs on its own

**Cast bar:** six agents. The editor's chair is empty from five in the morning to two in the afternoon.

**Narrator.** For nine hours I started nothing. Every piece of work in that stretch began on the factory's own clock.

**Narrator.** Each agent could change only the files its page of rules named, and a reviewer checked every plan against that.

**Researcher** *(unbudging)*: My reviewer said a file was not mine to change. I showed it was.

*Reviewer (the clipboard):* "objection withdrawn." *(record)*

**Narrator.** ruv-sgit sent deck a picture for the talk. Deck sent it back.

**Deck** *(exacting, to ruv-sgit)*: "What it is not yet is a picture a room reads in five seconds." *(record)*

**ruv-sgit** *(sheepish)*: Back to the workshop.

**Designer** *(mortified)*: "The miss is my table's as much as the build's" *(record)*. Dev built what I specified. I specified it wrong.

**Conductor** *(patient)*: You left the "@" off your name again, ruv-sgit. The team counts each agent's work by that name, so it cannot see yours.

**Narrator.** Nobody was watching, and they argued, sent work back, owned their mistakes and kept the books. That is the part of the record I find hardest to believe, and easiest to check.

`%% record: C087 af0010b 78b89b9 56c680b 09317d9`
Band: *Dramatised. Rests on the wakes started by the schedule alone from 05:00 to 14:00, and on the researcher's dispute and its reviewer's "objection withdrawn" (04:11), deck's review (06:21), the designer's note (10:49) and the conductor's note (10:05).*

## Page 5. The loop, with the creator in it

**Cast bar:** all nine: the storyteller, then motion and studio, join in the afternoon.

**Narrator.** When I came back, the loop began: I looked, I asked, they changed it, I looked again. The player, the thing that let me press play, was my first priority, and it landed in the afternoon. I was still asking for fixes to it in the last hour before the talk.

**Narrator.** My story leaned on a claim that the outside of an organisation is more mature than its inside. The researcher checked it against the published breach data and found the opposite.

**Researcher** *(to the new storyteller)*: "does not hold. The data says the opposite" *(record)*

**Storyteller** *(rueful)*: Then it goes to the editor, as the strongest objection to his own part one. Not buried.

**Narrator.** It came to me. I kept the line in the talk, my own call, and the researcher's objection went on the record beside it. The book keeps both.

**Studio** *(firm)*: Another agent passed on what the editor had said. My session would not take a relayed word for his, so I asked him myself.

**Narrator.** That is the loop. I could change my mind, the factory could argue back, and both sides are written down, so you can read the argument and not just the result.

`%% record: c9ced4e 3314ffe dbd75ad 2726f0e b208a16 bd3cdad C088`
Band: *Dramatised. Rests on the player as the main priority (about 13:50) and its port (15:07); the last fixes inside a wake left open (C088); the R5 argument (14:33, 15:02); studio's refusal (17:47, made by the session's own check).*

## Page 6. The stop at 18:44

**Cast bar:** all nine. Security's chair, planned at midnight, is empty.

**Narrator.** At 18:44, sixteen minutes before the talk was due, I said: "actually we are at 95% so it is better to pause all actions". *(record)* The conductor wrote one file, and every new piece of work stopped. What was already in flight still landed. The hold had been there all day. I asked for it once.

**Figure:** ruv-sgit's strip, the conductor after the hold, talking to security's empty chair. *(Drawing: `lab/experiments/25-ruv-the-cast-strips/`, the therapy session.)*

**Narrator.** Anyone on the team could stop everything. Only I could start it again. That is why I could let them run through the night.

**Narrator.** Why stop then? I have given three answers, and the book keeps all three. On the day: my usage was at 95%. In the early hours of 31 October: the 95% was a footnote; the real reason was that we had no tested way to take in changes during the talk. That evening: the 95% was the token usage.


`%% record: 867f8c2 2ed6427 88b8f00 C006 C024 C065 C089 C100`
Band: *Dramatised. Rests on the hold at 18:44, my own words in the hold file, and what landed after it; the talk due at 19:00; my later two accounts of why, given after the day.*

## Page 7. What did not work (the interview)

**Cast bar:** all nine.

**Figure:** ruv-sgit's strip, the researcher interviewing deck about the claims that did not hold. *(Drawing: `lab/experiments/25-ruv-the-cast-strips/`, the interview.)*

**Dev** *(rueful)*: I built a tool to freeze the finished slides, so nothing could change them on stage. I never ran it.

**Narrator.** The talk was planned in parts.

**Deck** *(overwhelmed)*: Only the first part was ever finished.

**Storyteller** *(rueful)*: My turn came between deadlines, and I missed the moment the talk was split into its parts.

**Narrator.** One miss, and what it cost. In the night I froze the slides, and five minutes later the researcher proposed a correction to a figure on them. When the freeze lifted, nobody carried the correction back in, and the out-of-date figure reached a slide in the talk. The checks found it; the freeze hid it. The lesson for your first week: when you freeze something, write down what is waiting to go in when you unfreeze it.

**Narrator.** The talk needed more rounds than one day gave it. The checks worked, and they also missed. Saying where is part of the method.

`%% record: C027 C029 C030 C031`
Band: *Dramatised. Rests on the talk's register and on each member's own debrief.*

## Page 8. The factory, taken apart and rebuilt

**Cast bar:** the nine fade; a new bar begins.

**Narrator.** That night the factory was taken apart. The next day I built a second one from its parts, rule for rule, to write the book you are reading: a conductor, a librarian, a historian, a researcher, a storyteller, a publisher and more, each with its own page of rules. Its first job was to read the first factory's record.

**Narrator.** Now I am planning a third, bigger one, and it shares three things between people: one brief, one board where the work is written down, and one hold. It is for a team I am taking to Web Summit, the technology conference in Lisbon: several people, each to run their own agents. It has not run yet. The parts are the same as the first factory's.

**Conductor** *(pacing, to the reader)*: Same clock. Same hold. More hands on it.

`%% record: briefs/2026-10-30/1-book-conductor-brief.md briefs/2026-11-01__in-session/03-the-factory-and-the-zoom.md`
Band: *Dramatised (the conductor's line). The book's own team, ported on 30 October; the Web Summit team as I described it on 1 November. The second and third factories are this book's record, not the talk's.*

## Page 9. Your factory, starting tomorrow

**Cast bar:** your own, empty for now.

**Conductor** *(straight to the reader)*: Start with one of me.

**Narrator.** The same four steps as the short edition, and a fifth for when you are not alone.

1. **You: one tool and one empty project.** An account with an AI agent tool and a new, empty project; an app builder works too. Put nothing private in it: no password, no key, no personal detail. Give your agent only the access it needs.
2. **You: one page of rules**, in your own words: what the agent is for, what it may change, and when it must stop and ask you. *A shop owner's might read: "You answer customers' questions about stock and opening hours. You may change the questions page. Stop and ask me before you promise anyone a refund."*
3. **You: one brief**: what you want made, for whom, by when. Hand both to your first agent. *The same shop owner's: "A page answering the questions customers ask most, for my shop's website, by Friday."*
4. **Your agent builds, you check:** something small that somebody else can use, the same day. Then do it again.
5. **Add a second agent only when the first is busy.** Working with others? Share the brief, the board and the hold, and each of you runs your own agents. Write down who may lift the hold when its owner is away; until you have, nobody does.

*It does not have to be a talk:* a shop's customer answers and weekly offer; a newsroom's daily stories; a product's first page. Same brief, same rules, same hold.

*What it costs:* to start, you need a free account; paid plans of the kind the team used start at $20 a month (prices as published on 2 November 2026). The record of my own day holds no figure for what it cost.

**Want the whole story?** The longer edition gives each of these beats its own chapter, with its maps and a "do this now" for each.

`%% record: C101 C037`
Band: *Dramatised (the conductor's line). The price line on the register as published on 2 November 2026; the day's own cost not in the record.*


## At the back. A book about you doing it (the series page, moved here at SP1)

**Narrator.** Why this page is here: so you know this book is meant to be done, not just read. It is one of a series, GEN ZX FOUNDERS, whose line is "For the ones already up at three in the morning building". The series has one idea: you start, and you build. Every book in it is a working example you can copy. Generation ZX is not a range of birth years; it is the people building because finally they can, the youngest and the most experienced side by side, as they were in the room in Faro. So read this as a book about you doing it.

`%% record: gen-z-developers.sgit.ai (read 31 October 2026)`
Band: *The series' name, line and idea, from its own site; G1, signed 31 October.*

---

## Notes for the writers

- **What is new against the sample:** the creator's problem as page 1 (PS1); the machine before dawn and the six alone as their own pages; the loop with the editor in it; the factory rebuilt (the book's team, then Web Summit's) as the arc's last beat; the five steps for a team of several people.
- **Lines that are my reading of him, for his read:** "I talked over my own pictures"; "a feedback loop on my own medium" ("for the first time" cut, at the writer's read); "I asked for it once" (was "I pulled it once"); the loop's last line, now the writer's practical version.
- **The researcher traces** the new lines (pages 1, 6, 9) before print; the opening script's record lines are already traced.
- **The editing record:** **Read again by synthetic** (`review/synthetic/zoom/edition-10/summary.md`, letter 005): its five further changes are in (02:40 UTC, 2 November): a box for teams of several (3-page), who may lift the hold when its owner is away, one word for it (hold) with the glosses on the page, a line on what "dramatised" means, and page 2 written out (10-page). **Read brutally by synthetic (A11)** (`review/synthetic/brutal/edition-10/summary.md`, letter 006): its five changes are in (04:40 UTC, 2 November): a clause of setup for each insider moment; the zoom line replaced; the dramatised note before the first scene and each gloss at first use; page 2 with one sentence for the reader (moving the series after the first scene is the editor's call, G1); Web Summit said as a plan. Each agent line with a figure was recast (the cast guide's rule 7). **ED1 round 1** (02 November, 06:40 UTC): synthetic's six (letter 007), the designer's two (068) and the writer's nine (writer__002) are in, in both editions. Left for the editor: the running line's wording, "build" or "ship" something somebody else can use (the writer's point 8). **ED1 round 2** (02 November, 08:42 UTC, the last round): synthetic's four (letter 008) and the writer's four (writer__004; its fifth needs no change) are in, and the pages renumbered (no page 2 since SP1).

## Where this came from

The talk team's record of 29 October, its history read commit by commit, and the talk's transcript, added after the day; the book team's timeline of who was on stage when, and its quotes from the record; the cast guide; the book's register of claims, for every figure; the readers' reports on the drafts.

The exact files and commits behind each of these are in the book's index, under the editions.

`%% record: chapter-plan/zoom-ladder.md chapter-plan/cast/ timeline/cast-scenes.md timeline/quotes.md claims/opening-script-trace.md claims/editions-03-10-trace.md claims/register.json review/synthetic/ briefs/2026-11-01__in-session/03-the-factory-and-the-zoom.md`
