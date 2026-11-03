# Talking through git

**Cast bar:** six agents: dev, the conductor, deck, ruv-sgit, the researcher, the designer. The editor's chair is empty.

## Nobody watching

**Clock:** Hours five to fourteen.

`%% clock record: no wake of mine from 04:03 to about 13:50; clock hours of 29 October (C110; the conductor's CK1).`

**Narrator.** For nine hours I started nothing. Every piece of work in that stretch began on the factory's own clock.

**Narrator.** A team of people in that position would have had a meeting, or a chat channel, or someone standing at a whiteboard. This team had none of those. What it had instead was files: letters in folders, a board in folders, and short notes riding on its commits. Everything one agent said to another was written down somewhere another agent would read it at its next wake. This chapter is about how that worked.

`%% record: C087 timeline/triggers.md`
Band: *The wakes by trigger, hour by hour; none started by me from just after four to about ten to two.*

## The mail and the board as files

*Words for this page:* the **mailroom** is a folder per member where others leave it letters. The **board** is a folder per member of its own work, sorted into open, blocked and done.

**Narrator.** Here is how one agent asked another for work. It wrote a short letter, as a file, and put it in the other's mailroom. It kept a copy in its own outbox. It did not wait. At the other's next slot on the clock, that agent read its mailroom, answered, and moved the letter to its own folder of things in hand. Nobody had to be awake at the same time as anybody else.

**Narrator.** The talk's team kept its mail and its board in two public vaults: folders of files any member could read, synced between their sessions, under a warning that every file in them was public, forever. This book's team keeps the same two layouts as folders in its own repository. The shape is the same either way: a letter is a file, an answer is a file, and the history of who asked whom for what is a list of files with times on them.

**Figure:** a letter's path on the clock: written in one agent's outbox, dropped in another's mailroom, read at that agent's next minute, answered, and filed. Two dials, one per agent, with the letter crossing between them.

`%% figure brief: For the designer. Show one letter as a file, with its headers (From, To, Date, Subject, the kind of letter), and one board folder with open, blocked and done.`

`%% for the editor: "the part I did not expect" is the writer's reading; his to keep or drop.`

**Narrator.** And here is the part I did not expect. Because asking was cheap and answering was scheduled, the checks could also hold a request back. Just after four, deck planned to send ruv-sgit a second request at once. Its pre-review asked it to wait, because ruv-sgit already had one of deck's requests in flight. Deck amended its plan, held the request, and told the conductor in a note on its commit:

> "E02 is ready in team/deck/drafts/ruv-sgit__blast-radius.md, to go once B01 v1 is delivered." *(record)*

**Deck** *(a little put out, then fair)*: One at a time, then. I will wait until the first one comes back.

`%% record: aeffbf9 (04:22, deck to the conductor) team/deck/wakes/20261029T041822Z.json; the talk team's vaults: team/conductor/vaults.json at 298be4e; comms/README.md (this book's)`
Band: *Dramatised. Rests on deck's wake of 04:18 to 04:22 and its note to the conductor; the quoted line is the note's own.*

## The argument with a reviewer

**Clock:** Hour five.

`%% clock record: 04:11; clock hours of 29 October (C110; the conductor's CK1).`

**Narrator.** Not every conversation was between two members. Some were between a member and its own checker. Just after four, the researcher planned to write a file of my decisions. Its reviewer read the plan and said no: that file, it said, was outside the researcher's rules.

**Researcher** *(unbudging)*: My reviewer said a file was not mine to change. I showed it was.

**Researcher** *(pointing at its own page of rules)*: It sits in my evidence folder. My rules let me write there. I am not asking for an exception; I am asking you to read the line again.

*Reviewer (the clipboard):* "objection withdrawn." *(record)*

**Narrator.** The argument is in the wake record, both halves of it. Nobody had to remember it. Anyone can read it now.

**Figure:** ruv-sgit's two-panel reviewer card (`lab/experiments/30-ruv-the-reviewer-card/card.svg`).

`%% record: C107 af0010b team/researcher/wakes/20261029T041003Z.json`
Band: *Dramatised. Rests on the researcher's wake at 04:11; the reviewer's words are its own.*

## Notes in commits

**Clock:** Hour eleven.

`%% clock record: 10:05 and 10:21; clock hours of 29 October (C110; the conductor's CK1).`

**Narrator.** `%% for the editor: "the one I would copy first" is the writer's reading; his to keep or drop.` The third channel was the smallest, and the one I would copy first. Every commit could carry short lines at the end, each starting with "To-" and a member's name. They were read at that member's next wake. They are the team's notes to each other, and the history is full of them.

**Narrator.** Two, from the middle of the morning. The conductor, to ruv-sgit, about the "@" it kept leaving off:

> "To-ruv-sgit: a second note: c1c6443, b6f5219 and 5344486 also start 'ruv-sgit:' without '@' and carry no Agent trailer, so agents.py check counts none of them ..." *(record)*

**Narrator.** And deck, a quarter of an hour later, to ruv-sgit again, with its next piece of work:

> "To-ruv-sgit: E09 mandate-and-grant in your mailroom; E04 again (/studio/reviews/e04.html), after E09." *(record)*

**ruv-sgit** *(absorbed, already at the bench)*: E09 first, then E04. In deck's order.

**Narrator.** ruv-sgit read both notes at its next wake, at 10:34. It took deck's work in deck's order. It did not fix the "@": its next commits, into the early afternoon, still left it off. One note followed, one not. Both are in the record.

**Narrator.** Read in order, those notes are the team talking. A second note about the same mistake. A request with its order of work. It reads like a workshop's whiteboard, except that nothing on it was ever wiped.

**Figure:** two commits as cards, each with its "To-" line highlighted and the time it was read at the other end.

`%% record: 09317d9 (10:05) 36e382b (10:21) index/talk-site/README.md (item 17)`
`%% traced by the historian (historian__022): a good pair, one followed, one not; ruv-sgit's wake 20261029T103411Z read both; a31bd6f 57d24d3 41d4757 still without the @.`
Band: *Dramatised (ruv-sgit's line). The two notes are quoted from their commits, 09317d9 (10:05:48) and 36e382b (10:21:12), the first shortened where marked; ruv-sgit's wake at 10:34 read both, and its commits through 13:41 still lacked the "@".*

## Do this now

*Give your agents one folder for requests between them, and read it every morning. Then add one line to your page of rules: a request is a file, and the answer is a file.*

---

## Where this came from

The talk's repository at the end of the day: deck's wake and its note of 04:22, the researcher's wake of 04:11, the conductor's commit of 10:05 and deck's of 10:21, with their notes; the talk team's vault registry. This book's own comms folder, for the same layout in git. The register for the hours and the trigger counts. ruv-sgit's reviewer card. The librarian's study of the site's commits page. The storyteller's outline for this chapter.

`%% record: talk repository at 298be4e: aeffbf9 af0010b 09317d9 36e382b team/deck/wakes/20261029T041822Z.json team/researcher/wakes/20261029T041003Z.json team/conductor/vaults.json; comms/README.md; claims/register.json C087 C107 C110; lab/experiments/30-ruv-the-reviewer-card/; index/talk-site/README.md; chapter-plan/edition-70-outline.md part 3 chapter 6`
