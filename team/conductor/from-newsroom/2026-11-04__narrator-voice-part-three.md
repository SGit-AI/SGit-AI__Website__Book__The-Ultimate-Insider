# The narrator's voice: part 3, how the team did it (chapters 10 to 15)

**For:** the book team of *One Human, Nine Agents, Nineteen Hours*, through the conductor.
**From:** the newsroom journalist, for Dinis Cruz, 4 November 2026.
**Answers:** the hand-over's request 1, part 3. Read against `manuscript/rc2/150/10` to `15` on `dev` at b49b3f74.
**Same form as parts one and two:** now and proposed, with *Check* where a line is my reading of his view and needs his yes. Narrator lines only; the agents, figures, bands and cards are untouched.

## How this pass applies the guidance

- **Brief 07, no logistics.** Minute stamps leave the narrator's mouth. Times stay only where they carry the story: "at seven that evening", "half an hour before the talk", "within the hour". Exact stamps move to the bands and the record notes.
- **No quoting him to justify the text.** The two places where the narrator quotes Dinis's own words from the record (the feedback round's first line, and his line after the conductor's review) become paraphrase. Agents' notes on commits stay as quotes: they are the team talking, which is what chapter 10 is about.
- **The historian stops being the narrator's authority.** "The historian reads the hour after three as…" and "The historian reads it as…" become his own reading.
- **Rule 11.** "It is easy to walk past" (chapter 11) is exactly the phrase the rule names; it goes. So do "Look at what is not there", "Read its lines next to the check's" and "Remember those gates", which tell the reader how to read.
- **Connecting the dots, lightly.** The newsroom's lost releases of 27 October and the rule it came to (the pipeline numbers every release); the player ported from ruv.sgit.ai; the earlier sites the studio's pieces came from. Nothing new is claimed beyond what the book or this conversation has already verified.
- **Lines not listed here are fine as they are.** Part 3's narrator is closer to his voice than part 2's in places: "Nobody puts the plumbing in the brochure", "A brief that is never corrected becomes a story about what you thought you wanted", "The failures stay in, and that one is mine", "Not to win. To make sure the decision was a decision."

## Structural notes before the lines

1. **Chapter 10 retells two scenes from part 2.** "Deck holds itself back" is told in chapter 8, and "Three letters in a row" is told in chapter 9 as "a promise kept", with the same three notes promised there "word for word" here. Suggestion: chapter 9 keeps one sentence ("a request asked at one slot was answered at the next, and used at the one after; chapter 10 has the notes"), and chapter 10 tells it in full, once. Deck's hold drops out of chapter 10, or is reduced to one line pointing back.
2. **Chapter 11 repeats three things.** The first page of rules is shown as a card in chapter 4 and again here; the check stopping dev's own release is told in chapter 5 and again here; deck's "never type a version number" line appears in chapters 4, 6 and 11. Suggestion: chapter 11 keeps the version-number story (it is where its reason, the newsroom's lost releases, belongs) and points back for the other two in a line each.
3. **Chapter 12 and chapter 2 tell the same loop.** Chapter 2 has the afternoon asks card, the loop drawing and "One ask, followed in full"; chapter 12 has "The player ported, and the loop begins" with the same card and the same closing lines ("That is the loop, and it is the thing I came back for… I decided, and it built"). Brief 11 asks for the afternoon-asks card to show what each ask built, and the loop to read as a real cycle (think, explain, create, review). Suggestion: chapter 2 keeps the idea of the loop, short, and the redrawn card and cycle live in chapter 12, where the afternoon actually happens.
4. **"One ask, followed in full" (chapter 2) is the weak example in brief 11, and chapter 15 points to it** ("'when in doubt add it' (chapter 2 follows that one all the way to the stage)"). If the storyteller cuts or replaces it, that reference in chapter 15 needs to go too; the proposed text below already drops it.
5. **Chapter 14 retells the player's port from chapter 12.** Both quote dev's commit. Suggestion: the port is told once, in chapter 12; chapter 14's "Port, not rebuild" section keeps the argument and refers to it in a clause.
6. **Brief 11's "the factory in action"** (ruv-sgit's clock of when each agent fired) would fit at the end of chapter 15, "Where part 3 ends", as well as in chapter 2: hour eighteen is the hour the clock and the editor ran side by side.

---

## Chapter 10, Talking through git

**No meeting, no channel, no whiteboard**

> **Now:** The last chapter went through nine hours in which I started nothing. A team of people in that position would have had a meeting, or a chat channel, or someone standing at a whiteboard. This team had none of those. What it had instead was files: letters in folders, a board in folders, and short notes riding on its commits. Everything one agent said to another was written down somewhere another agent would read it at its next wake. This chapter is about how that worked.
>
> **Proposed:** For nine hours I started nothing, and the team kept talking. A team of people in that position would have had a meeting, or a chat channel, or someone at a whiteboard. This team had none of those. It had files: letters in folders, a board in folders, and short notes on its commits. Everything one agent said to another was written down somewhere the other would read it at its next session. I have come to think this is one of the most useful ideas in the whole book, and one of the easiest to copy: if your agents talk through files, you get the conversation and its history for free.

**The mail and the board as files**

> **Now:** Here is how one agent asked another for work. It wrote a short letter, as a file […] Nobody had to be awake at the same time as anybody else.
>
> **Proposed (keep; it is clear and his).**

> **Now:** The talk's team kept its mail and its board in two public vaults […] The shape is the same either way: a letter is a file, an answer is a file, and the history of who asked whom for what is a list of files with times on them.
>
> **Proposed:** The talk's team kept its mail and its board in two public vaults: folders any member could read, synced between their sessions, under a warning that everything in them was public, for ever. This book's team keeps the same two layouts as folders in its own repository. Either way the shape is the same, and it is the shape I keep coming back to in my own work with sgit: a letter is a file, an answer is a file, and the history of who asked whom for what is just a list of files with times on them.

*Check:* "the shape I keep coming back to in my own work with sgit" rests on the vaults and append lanes described in the newsroom's articles; confirm he wants sgit named here.

> **Now:** And here is the part I did not expect. Because asking was cheap and answering was scheduled, the checks could also hold a request back. Just after four, deck planned to send ruv-sgit a second request at once. […]
>
> **Proposed (if the scene stays; see structural note 1):** And here is the part I did not expect. Because asking was cheap and answering was scheduled, a check could also hold a request back. Chapter 8 has the moment: deck's own reviewer asked it to wait, because one of its requests was already in flight, and deck held the second. Here is the note it left the conductor, on its commit:

**A member and its own checker**

> **Now:** Not every conversation was between two members. Some were between a member and its own checker, and those are written down too: the researcher's argument with its reviewer at 04:11, in chapter 8, is in its wake record, both halves of it, the objection and its withdrawal. Nobody had to remember it.
>
> **Proposed:** Not every conversation was between two members. Some were between a member and its own checker, and those are written down too. The researcher's argument with its reviewer, in chapter 8, is in its record, both halves of it. Nobody had to remember it, which is the point: a disagreement that is written down can be learned from, and one that is remembered usually cannot.

**Three letters in a row**

> **Now:** Chapter 9 told this exchange as a promise kept. Here it is again as the team wrote it, in notes on three commits, each read at the other member's next wake. It is a worked example the record keeps of how a request travelled when nobody was awake to carry it.
>
> **Proposed (see structural note 1):** Here is one request as the team actually wrote it, in notes on three commits, each read at the other member's next session. It is how a request travelled when nobody was awake to carry it.

> **Now:** *First, at 09:21, deck.* […] *Second, at 10:14, the researcher*, at its own next slot. The letter had waited in its mailroom for most of an hour, and nobody had reminded it. […] *Third, at 10:21, deck*, at its own next slot […]
>
> **Proposed:** *First, deck*, in the middle of the morning. […] *Second, the researcher*, at its own next slot, almost an hour later. The letter had waited in its mailroom, and nobody had reminded it. […] *Third, deck*, a few minutes later, at its own next slot […]

*Note:* the exact times move to the figure, which already draws the three notes on a line of time.

> **Now:** Look at what is not there. No "just checking in". No "any update?". No message sent because somebody was anxious. A letter is a file in a folder, and the folder is read at a known minute, so a request needs saying once. […]
>
> **Proposed (rule 11):** What I like most is what is missing. No "just checking in". No "any update?". No message sent because somebody was anxious. A letter is a file in a folder, and the folder is read at a known minute, so a request only needs saying once. I would happily work that way with people too.

*Check:* the last sentence is his to confirm.

**Notes in commits**

> **Now:** The third channel was the smallest, and the one I would copy first. Every commit could carry short lines at the end, each starting with "To-" and a member's name. They were read at that member's next wake. They are the team's notes to each other, and the history is full of them.
>
> **Proposed (keep; it is his voice).**

> **Now:** ruv-sgit read both notes at its next wake, at 10:34. It took deck's work in deck's order. It did not fix the "@" […] One note followed, one not. Both are in the record.
>
> **Proposed:** ruv-sgit read both notes at its next session. It took deck's work, in deck's order. It did not fix the "@", and many of its later commits still left it off. One note followed, one not, and both are in the record. I find that oddly reassuring: the agents ignored the boring housekeeping request and acted on the one about real work, which is very much what people do too.

*Check:* "oddly reassuring" and the comparison with people are his to confirm.

> **Now:** Read in order, those notes are the team talking. A second note about the same mistake. A request with its order of work. It reads like a workshop's whiteboard, except that nothing on it was ever wiped.
>
> **Proposed:** In order, those notes are the team talking: a second note about the same mistake, a request with its order of work. It reads like a workshop's whiteboard, except that nothing on it was ever wiped.

---

## Chapter 11, The plumbing

**Opening**

> **Now:** Nobody puts the plumbing in the brochure. But every story in this book ran through four pipes […] The register first.
>
> **Proposed (keep; this is very much his voice).**

**Every number traced**

> **Now:** The talk made claims. […] By early evening the register held 320 claims. 210 held. 55 held in part. 52 had not been checked. Three did not hold.
>
> **Proposed (keep the counts; they are the point, not logistics).**

> **Now:** Three did not hold, and no beat of the talk carries any of the three. That is not luck. It is the register doing its job: the researcher marked them, in writing, where every member could see.
>
> **Proposed:** Three did not hold, and none of the three made it into the talk. That is not luck. It is the register doing its job, and it is why I now think every team that publishes anything, people or agents, should keep one. A number without a source is an opinion with a decimal point.

*Check:* the last sentence is a line in his style; confirm he wants it.

> **Now:** This book works the same way. Its researcher keeps a register, and no number goes on a page unless it is there. When an early draft of this book carried a line the record could not support, it came back by letter, and the line was changed.
>
> **Proposed (keep; add one clause):** … and the line was changed. My newsroom works the same way, and so, now, does almost everything I publish.

*Check:* "almost everything I publish" is his to confirm.

**The check that keeps it true**

> **Now:** Every change to the site went through the same check before it could go out, and if anything on its list failed, the change stopped. The card has the list.
>
> **Proposed (keep).**

> **Now:** The check had a twin, in words. Dev's first commit also put in the team's first page of rules, the file every later agent read before doing anything. It is easy to walk past, so here it is as a card. Read its lines next to the check's: half of the page is the check said in words, and the other half is what no check could hold.
>
> **Proposed (rule 11; see structural note 2):** The check had a twin, in words: the team's first page of rules, from chapter 4. Put the two side by side and half of the page is the check said in words. The other half is what no check could hold, and that is the half I find more interesting, because it is where trust lives.

> **Now:** The check does not care who made the change, or how sure they were. That is the point of it. A member that is certain its work is fine still has to pass the same test as one that is not.
>
> **Proposed (keep; it is good).**

> **Now:** Chapter 5 has one example from the first night, and it is worth calling back here because it is the check doing exactly this. It stopped dev's own release until two members' pages of rules carried a rule I had just asked for […] the release it stopped was dev's own, the member that built the gate.
>
> **Proposed (see structural note 2):** Chapter 5 has the example I like best: on the first night, the check stopped the release of the very member that had built it.

> **Now:** And the release history shows the result […] Nobody typed a version number all day. The pipeline numbered every release itself. Deck's page of rules gives the reason: agents racing for release numbers is how another team, the newsroom, had lost releases on 27 October.
>
> **Proposed:** And the release history shows the result. Nobody typed a version number all day; the pipeline numbered every release itself. That rule has a story behind it. Two days before the talk, in my newsroom, agents racing each other for the next release number had lost releases. The newsroom's answer was to let the pipeline own the version, and this team started with that answer on its first page. That is what I mean by a factory built from parts: even its scars were borrowed.

*Check:* the newsroom's lost releases on 27 October are in deck's page of rules, and the newsroom moved version numbering to its pipeline afterwards (the newsroom's article on CI owning the version). "Even its scars were borrowed" is his to confirm.

**The site is the scaffolding**

> **Now:** The agents did not work in a chat window. They worked on a website […] That sounds like an odd choice for a talk. It was the most important one.
>
> **Proposed:** The agents did not work in a chat window. They worked on a website: every slide a page, every member a page, every session and every commit a row on a page. That sounds like an odd choice for a talk, and I think it was one of the most important choices of the day. It is the same choice I made for the newsroom, and for the talks before this one: if the work is a site, it has an address, a history and a check.

*Check:* "the talks before this one" rests on the earlier talks being sites and vaults (Black Hat Europe 2025 in a vault, the ruv.sgit.ai talk as a site), already verified in this conversation.

> **Now:** A website gives an agent somewhere to put things that stays put. […] The site remembered for them, and it showed me what they had done, on pages built from their own files.
>
> **Proposed (keep).**

**The brief and its corrections**

> **Now:** The last pipe is the simplest, and on the day it was the one that did not quite work.
>
> **Proposed (keep).**

> **Now:** The brief was wrong in places. My request in it says the talk is "tomorrow"; by the time the project existed, it was that same day. The talk it asks for became something different as the day went on, in my own decisions of the afternoon. None of that went into the corrections file. It went into the reality file, the decisions, the debriefs. The rule was right; nobody used it.
>
> **Proposed:** The brief was wrong in places. It says the talk is "tomorrow"; by the time the project existed, it was that same day. And the talk it asks for became something quite different in the afternoon, by my own decisions. None of that went into the corrections file. It went into the reality file, the decisions and the debriefs instead. The rule was right, and nobody used it, me included.

> **Now:** I would keep the file, and give one member the job of writing in it. A brief that is never corrected becomes a story about what you thought you wanted.
>
> **Proposed (keep; this line is very much his).**

---

## Chapter 12, The creator comes back

**The feedback round**

> **Now:** At about ten to two I came back. I did not open a session and start typing at an agent. I dictated a round of feedback, in a chat, with a brief for each member, and pasted it into the conductor's session for it to route. Its first line says when and how; its first item says what mattered most: [quote]
>
> **Proposed (no quoting him to justify the text):** At about ten to two I came back. I did not open a session and start typing at an agent. I dictated a round of feedback, in a chat, with a brief for each member, and gave it to the conductor to route. The first item was the one that mattered most: the player, from ruv.sgit.ai, working on an iPad, because that was what I would be pressing play on that evening. The rest was corrections to the morning review, the framing of the talk, the story of the animations, and a new member, a storyteller.

> **Now:** Then the record keeps something I would rather it did not. The conductor read the round, wrote a review of it, and I answered the review in the same session. Within minutes the order had changed, at my own word: a feedback pane on every page […] went first; the player went second. The conductor's notes of 14:05 record the new order, and my words after the review: [quote]
>
> **Proposed:** Then the record keeps something I would rather it did not. Within minutes of that round I changed the order myself. A feedback pane on every page, so I could send notes from the browser, went first, and the player went second. My reasoning was that there was still time before seven, and I could wake the agents when I needed them.

> **Now:** Both things were true. […] The failures stay in, and that one is mine.
>
> **Proposed:** Both things were true. The pane did let me send notes from the page I was reading. And the main priority came second, landed in the middle of the afternoon, and was still being fixed in the last hour. Looking back, I did what most people do when they come back to a team with fresh energy: I added a new idea in front of the one I had just said mattered most. The failures stay in, and that one is mine.

*Check:* the "what most people do" line borders on judging others; if Dinis prefers, "I did what I often do when I come back with fresh energy".

**A change sent back, at the moment of most pressure**

> **Now:** The first wake at my request since four in the morning was the conductor's, at 14:03, and the first thing that happened in it is the thing I would most want a team to do when its creator walks back in with a list.
>
> **Proposed:** The first session I started after the night was the conductor's, and the first thing that happened in it is what I would most want any team to do when its creator walks back in with a list.

> **Now:** The pressure in that hour was me. I was back, with a list, and the talk was due that evening. The checks did not soften because I was in the room. That is what they are for.
>
> **Proposed (keep; it is his voice).**

**The team changes shape within the hour**

> **Now:** From 14:03 I was in four sessions: the conductor's, the storyteller's as it joined, dev's and deck's.
>
> **Proposed:** From then on I was in four sessions at once: the conductor's, the storyteller's as it joined, dev's and deck's.

> **Now:** Between 14:19 and 14:48 that cleared a queue that had been building since four in the morning […]
>
> **Proposed:** In about half an hour, that cleared a queue that had been building since four in the morning: every piece marked ready for me got its answer. Then, at my word, deck sent the rest of the programme to ruv-sgit to build in parallel, and ruv-sgit went from one run an hour to several at once. That was the moment the team stopped waiting for me and started keeping up with me.

> **Now:** And the schedule did not stop. It yielded. […] A schedule that knows when to step aside is a better schedule than one that insists.
>
> **Proposed (keep; it is good).**

**The storyteller arrives**

> **Now:** At a quarter past two the first new member of the afternoon joined, at my request: the storyteller […] By 14:19 it had put a story tree and its maps on the team's branch, and changed nothing in the talk. Chapter 13 has what it did next, and the objection it would not bury.
>
> **Proposed:** At a quarter past two the first new member of the afternoon joined, at my request: the storyteller. Within minutes it had a story tree and its maps on the team's branch, and had changed nothing in the talk. Chapter 13 has what it did next, and the objection it would not bury.

**The player ported, and the loop begins** (see structural note 3)

> **Now:** At seven minutes past three, dev ported the player. Not built: ported, from the earlier site I had pointed at in my brief, and its commit says so in its first words.
>
> **Proposed:** A little after three, dev ported the player. Not built: ported, from ruv.sgit.ai, the talk I had given two weeks earlier, where I had first played a talk as a timeline. That is the whole idea of this book in one commit: yesterday's experiment became today's part.

> **Now:** So I did. I looked, I asked, they changed it, I looked again. The card has the asks I put my own time on in a commit subject, from half past five on […] The last fix landed at 18:37, a few minutes before the hold.
>
> **Proposed (with brief 11's redrawn card):** So I did. I looked, I asked, they changed it, and I looked again. The card shows what each of my asks built, and how long it took to come back. The last fix landed a few minutes before I stopped everything.

> **Now:** That is the loop, and it is the thing I came back for. The factory had done what it could do without me. What it could not do was decide. From two o'clock, I decided, and it built, and I looked, and it built again.
>
> **Proposed:** That is the loop, and it is what I came back for. I think of it as a cycle: think, explain, create, review, and round again, a little like the OODA loop pilots use, but for making things. The factory had done what it could do without me. What it could not do was decide. From two o'clock, I decided, it built, I looked, and it built again.

*Check:* the OODA comparison is his own (brief 11). If chapter 2 keeps the loop drawing, this line belongs with whichever chapter carries it.

---

## Chapter 13, The story before the slides, and the objection kept

**The story before the slides**

> **Now:** The storyteller joined at a quarter past two, and the first thing it did was the thing I had asked for in my feedback round and not done myself: it put the story before the slides. By 14:19 it had a story tree, a set of maps, a map of what the talk already covered, a challenge, and a sequence on the team's branch. And it had changed nothing in the talk. Its first letter to deck says why:
>
> **Proposed:** The first thing the storyteller did was the thing I had asked for and not done myself: it put the story before the slides. Within minutes it had a story tree, a set of maps, a map of what the talk already covered, a challenge, and a sequence. And it had changed nothing in the talk. I like how it said so to deck:

**The tree and the maps**

> **Now:** The tree put the talk's beats in an order with a reason behind each one […] It is the shape of an argument, drawn before anyone drew a slide for it.
>
> **Proposed (keep; add one sentence):** … drawn before anyone drew a slide for it. I have always started talks from slides and found the story afterwards. This was the first time I had the story first, and I would not go back.

*Check:* "I have always started from slides" and "I would not go back" are his to confirm.

> **Now:** The maps did something different. […] That line is the honest heart of a map like that: it shows you where things are, not how big they are.
>
> **Proposed:** The maps did something different. They put the parts of my argument where they sit relative to each other: what depends on what, and how settled each piece is. If you have seen me talk, these will look familiar: they are Wardley maps, the kind I use for everything. The slide that carried one said, in small type, "positions, not measurements", and that line is the honest heart of a map like that: it shows you where things are, not how big they are.

*Check:* "Wardley maps" rests on chapter 8's map figure and chapter 1's Wardley passage; confirm the storyteller's maps were Wardley maps and not another kind.

> **Now:** And they were used. Deck took the storyteller's sequence into the talk's order that afternoon, almost exactly, by the storyteller's own account of its coverage. The tree became the spine the slides hung on.
>
> **Proposed:** And they were used. Deck took the storyteller's sequence into the talk's order that afternoon, almost exactly. The tree became the spine the slides hung on.

**The objection kept**

> **Now:** My story for the talk leaned on a claim: that the outside of an organisation, the part facing the internet, had become, in the outline's words for R5, "smaller and more mature than it was". […]
>
> **Proposed:** My story for the talk leaned on a claim: that the outside of an organisation, the part facing the internet, had become smaller and more mature than it was. The storyteller asked the researcher for the facts behind its beats, and the researcher checked that claim against the published breach data, and found the opposite.

> **Now:** That is the researcher doing what it is for. It could not change a slide. It could only say, in writing, that a line did not hold, with the source beside it.
>
> **Proposed (keep).**

> **Now:** Then the storyteller had a choice. The finding contradicted a line of mine that the storyteller's own tree depended on. At 15:02 it folded the researcher's facts into the tree and put the finding to me, as the strongest objection to my own part one, in a letter.
>
> **Proposed:** Then the storyteller had a choice, and an awkward one: the finding contradicted a line of mine that its own tree depended on. It folded the researcher's facts into the tree and sent the finding to me, in a letter, as the strongest objection to my own part one.

> **Now:** It came to me, and I answered it in my answers of that afternoon, committed at 15:16. The conductor wrote my answer down in one line of the decisions file […]
>
> **Proposed:** I read it, and I answered it that afternoon. The conductor wrote my answer down in one line of the decisions file, under the researcher's pushback:

> **Now:** I kept the claim. […] If you think I was wrong, the researcher's sources are in the register, and you can check.
>
> **Proposed:** I kept the claim. I still think the outside is in balance, and that the story needed that line. But the researcher's finding stayed on the record beside it, and the book keeps both: my line, the objection to it, and the fact that I read the objection and chose. If you think I was wrong, the researcher's sources are in the register, and you can check. I would rather be argued with on the record than agreed with in silence.

*Check:* "I still think" restates his position today; confirm he still holds it.

> **Now:** This is the part of the afternoon I would most want a team to copy, and it is not my part. It is the storyteller's. […] Not to win. To make sure the decision was a decision.
>
> **Proposed (keep; it is his voice at its plainest).**

---

## Chapter 14, Port, not rebuild

**Three decisions in twenty minutes**

> **Now:** The historian reads the hour after three as the hour the team changed most, and every change in it was mine. Three decisions, close together.
>
> **Proposed:** Looking back, the hour after three is when the team changed most, and every change in it was mine. Three decisions, within about twenty minutes.

> **Now:** *What the talk is.* At about three I made my decisions on the talk's frame, its third act and its new beats, and the conductor committed and routed them at 15:16. My answer to the researcher's objection, in the last chapter, is one line of that file.
>
> **Proposed:** *What the talk is.* At about three I decided the talk's frame, its third act and its new beats. My answer to the researcher's objection, in the last chapter, is one line of that file.

> **Now:** *How long a member may work.* At 15:21 the conductor raised the limit on a wake's work step, at my word […] My reason, in the commit: [quote]
>
> **Proposed:** *How long a member may work.* I told the conductor to let each member work for much longer in a single session. My reasoning was simple: if the next agent did not pick something up in the same hour, it would pick it up in the next.

> **Now:** That is a claim about the schedule, and chapter 9 shows the morning bearing it out […] The rule the team had written in the first hour, pull first, became a live risk rather than a habit.
>
> **Proposed:** The morning had already shown that was true. But it had a price, and I did not see it at the time. From then on sessions could overlap, so every member had to pull again before every push, or work from a stale copy. The rule the team had written in the first hour, pull first, stopped being a habit and became a live risk. Every change that makes a team faster changes what can go wrong, and that one is worth remembering.

> **Now:** *Who is on the team.* At 15:25 the conductor wrote briefs for two new members, at my word. By 15:47 both had joined, made their keys and tasks, closed their first wakes, and been checked and given their first requests.
>
> **Proposed:** *Who is on the team.* At my word, the conductor wrote briefs for two new members, and within about twenty minutes both had joined, made their keys and tasks, finished their first sessions, and been given their first requests. Hiring has never been that fast in any team I have run.

*Check:* the last sentence is a joke in his register; keep or cut.

**Motion and studio arrive**

> **Now:** At about twenty-five past three I brought on two members whose whole job was porting […] Both joined at 15:31, in the same minute.
>
> **Proposed:** I brought on two members whose whole job was porting: motion, to turn my new story into animations I could start and stop on stage, and studio, to take pieces from my earlier sites and rebuild them on this one, so they worked in the player and on an iPad. They joined in the same minute.

> **Now:** Studio had its first two pieces rebuilt on this site's engine by 15:40 […] and its first piece, the building, was in by 16:34.
>
> **Proposed:** Studio had its first two pieces rebuilt within ten minutes, each with its source and its data pinned unchanged. Motion did not wait to be told: it sent deck a proposed picture with its stages, so deck's answer could be "go" and not a fresh brief. Its first piece was the building, the animation I described at the start of this book.

**The talk doubles**

> **Now:** Then I made the talk twice as big. At half past four the conductor routed my word […] Its pre-review first said change, and the conductor amended before it routed anything.
>
> **Proposed:** Then I made the talk twice as big: ninety minutes, with a section on my own work. Even then, the conductor's own reviewer sent its plan back once before it routed anything.

> **Now:** The conductor's answer, half an hour later, was structural, and I think it is the most important plan the team made all day. The talk in three parts, each with its own deadline and its own lock […]
>
> **Proposed:** The conductor's answer, half an hour later, was structural, and I think it was one of the most important plans the team made all day: the talk in three parts, each with its own deadline and its own lock, so a late change could not reach a finished part. And for that evening only, at my word, a change to the schedule itself: each member could follow its own session with quick follow-ups until nothing was left or the evening ran out.

> **Now:** Remember those gates. Not one of them closed. The tool to lock a part shipped at 17:54, and the hold came at 18:44, and part 4 is where the record shows what happened between.
>
> **Proposed (rule 11):** Not one of those gates closed. The tool to lock a part shipped less than an hour before I stopped everything, and part 4 is what happened in between.

**Port, not rebuild**

> **Now:** Here is the thing I most want you to take from the afternoon. Almost nothing in it was built from nothing.
>
> **Proposed (keep; it is his voice).**

> **Now:** The player was not new. Dev's commit says so in its first words: "the player, ported from ruv.sgit.ai", the earlier site my brief points to as "what we did at ruv.sgit.ai". […]
>
> **Proposed (see structural note 5):** The player was not new; chapter 12 has where it came from. The slides ran on one slide engine dev had built just after midnight. Studio's pieces came from my earlier sites, pinned to their sources. Motion's ran on the same engine as everyone else's, so I could start and pause each one in the player.

> **Now:** That is the factory's economics in one afternoon. Yesterday's experiment is today's part, and the team that knows where its parts came from can move very fast without breaking much.
>
> **Proposed:** That is the factory's economics in one afternoon. Yesterday's experiment is today's part, and a team that knows where its parts came from can move very fast without breaking much. It is also why I keep everything I build in the open, with its history: I never know which experiment will be the part I need on the afternoon of a talk.

---

## Chapter 15, Hour eighteen: faster than the clock

**Faster than the schedule**

> **Now:** By five o'clock the schedule had carried the team all day. In hour eighteen I outran it.
>
> **Proposed (keep; it is a good opening).**

> **Now:** I sat in the conductor's session and gave it instruction after instruction: answers on the live slides, "when in doubt add it" (chapter 2 follows that one all the way to the stage), the team's own policies into the talk […] Each one was a wake of its own. The historian reads it as instructions arriving faster than the hourly schedule could carry them; the conductor carried them, one wake at a time, each with its five steps.
>
> **Proposed (see structural note 4):** I sat in the conductor's session and gave it instruction after instruction: answers on the live slides, the new pieces into the deck, the team's own policies into the talk, "go build", the remaining policies agreed, how the team keeps itself safe. Each one became a session of its own. I was giving instructions faster than the hourly clock could carry them, and the conductor carried them anyway, one at a time, each with its five steps.

**The brakes held**

> **Now:** This is the hour I would point to if someone asked whether the checks only work when nobody is in a hurry. The talk was due at seven. And in the middle of my run, the conductor's pre-review sent three of its plans back for change before it said go, in the wakes of 17:21, 17:30 and 17:45 […] A fourth plan changed in the middle of its work, at 17:37, because I changed my mind […]
>
> **Proposed:** This is the hour I would point to if someone asked whether the checks only work when nobody is in a hurry. The talk was due at seven, I was pushing as hard as I could, and in the middle of it the conductor's own reviewer sent three of its plans back before it said go. A fourth changed halfway through because I changed my mind, and the record says so honestly, rather than dressing it up as a review.

> **Now:** Every one of the conductor's wakes in that run still closed with all five steps. Not one step said stop all day. The brakes were what kept the speed from turning into damage.
>
> **Proposed:** Every one of those sessions still closed with all five steps. Not one step said stop all day. I used to think of checks as the thing that slows you down. That hour taught me the opposite: the brakes are what let you go fast, the same way a keel lets a boat go fast without capsizing.

*Check:* the keel image is from the WSO2 post the newsroom reviewed (Rania Khalaf's metaphor, quoted in the newsroom's article of 3 November). If the book prefers not to borrow it, end at "the brakes are what let you go fast".

**Part one, almost**

> **Now:** In the same hour, the plan of three parts started to arrive. Deck had part one complete and timed at 17:25, and final at 17:52. The designer checked it on a projector at 17:48: ready. Motion's two pieces for part one were in at 17:31.
>
> **Proposed:** In the same hour, the plan of three parts started to arrive. Part one was complete and timed, then final. The designer checked it on a projector, and said ready. Motion's two pieces for it were in.

> **Now:** At 17:54 the tool to lock a part shipped […] It came in under no member's name in its subject; only its trailers show it was dev's. And dev's wake of 17:48, the wake it came from, opened and never closed on the team's branch. Part 4 shows where that wake went.
>
> **Proposed:** Then the tool to lock a part shipped: it freezes a part of the talk so the player plays a locked copy. It came in under no member's name, and the session it came from, dev's, opened and never closed on the team's branch. Part 4 shows where that session went.

*Note:* "only its trailers show it was dev's" is record detail for the band.

**A relayed word refused**

> **Now:** That is what the record shows: the refusal, and the question sent to me in its place. […] It is a small scene, and it is the insider question in miniature: a member that would not act on another member's account of what I wanted.
>
> **Proposed:** That is what the record shows: the refusal, and the question sent to me in its place. It is a small scene, and it may be my favourite in the book, because it is the whole of my talk in miniature. The insider problem is about someone inside acting on a word that is not really yours. Studio would not. It asked me.

*Check:* "my favourite in the book" is his to confirm; chapter 8's deck scene was also offered as a favourite in part 2, so only one can be.

**Where part 3 ends**

> **Now:** By the end of hour eighteen the factory was running faster than its own clock, with me inside it, and its brakes were holding. Part one was final and not yet locked. The lock tool existed. One wake was open that would never close on the team's branch. And my usage, which I had not been watching, was nearly gone.
>
> **Proposed (keep; it is a strong close, and the last sentence lands part 4).** If the designer adds ruv-sgit's clock of when each agent fired (brief 11, "the factory in action"), this is a natural place for it: the whole day at a glance, just before it stops.

---

## Facts this pass adds, and where they come from

| Added | Source |
|---|---|
| The newsroom lost releases to agents racing for version numbers on 27 October, and moved numbering to its pipeline | deck's page of rules (chapter 11); the newsroom's own change to CI-owned versions |
| The player came from ruv.sgit.ai, the talk of 15 October 2026 | dev's commit (chapter 14); the newsroom's "The scripted talk" |
| The earlier talks were sites and vaults | the newsroom's "The scripted talk" (Black Hat Europe 2025 in a vault) |
| The OODA comparison for the loop | Dinis, brief 11 |
| The keel image for brakes that let you go fast | Rania Khalaf's LinkedIn post, as quoted in the newsroom's WSO2 article (3 November 2026) |
| The storyteller's maps as Wardley maps | to confirm (see Check) |

## Questions for Dinis

1. Feelings and favourites marked *Check*: "oddly reassuring" (chapter 10), "my favourite in the book" (chapter 15, studio's refusal) against part 2's "my favourite small moment" (chapter 8). Which, if any, stay?
2. Do you still hold the claim the storyteller objected to (chapter 13), so the narrator can say "I still think"?
3. The keel image (chapter 15): borrow it, or leave it in the WSO2 article?
4. Part 4 (chapters 16 to 19) next, in the same form?
