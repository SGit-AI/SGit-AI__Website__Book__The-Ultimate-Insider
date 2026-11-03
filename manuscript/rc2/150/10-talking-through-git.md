# Talking through git

**Cast bar:** six agents: dev, the conductor, deck, ruv-sgit, the researcher, the designer. The editor's chair is empty.

## No meeting, no channel, no whiteboard

**Narrator.** The last chapter went through nine hours in which I started nothing. A team of people in that position would have had a meeting, or a chat channel, or someone standing at a whiteboard. This team had none of those. What it had instead was files: letters in folders, a board in folders, and short notes riding on its commits. Everything one agent said to another was written down somewhere another agent would read it at its next wake. This chapter is about how that worked.

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

`%% record: aeffbf9 (04:22, deck to the conductor) team/deck/wakes/20261029T041822Z.json; the talk team's vaults, named and not cited by path; comms/README.md (this book's)`
Band: *Dramatised. Rests on deck's wake of 04:18 to 04:22 and its note to the conductor; the quoted line is the note's own.*

## A member and its own checker

**Narrator.** Not every conversation was between two members. Some were between a member and its own checker, and those are written down too: the researcher's argument with its reviewer at 04:11, in chapter 8, is in its wake record, both halves of it, the objection and its withdrawal. Nobody had to remember it.

`%% record: C107 af0010b team/researcher/wakes/20261029T041003Z.json manuscript/rc2/150/08-hours-four-and-five-before-dawn.md ("The argument with a reviewer")`

## Three letters in a row

**Clock:** Hours ten and eleven.

`%% clock record: 09:21, 10:14 and 10:21; clock hours of 29 October (C110; the conductor's CK1).`

**Narrator.** Chapter 9 told this exchange as a promise kept. Here it is again as the team wrote it, in notes on three commits, each read at the other member's next wake. It is a worked example the record keeps of how a request travelled when nobody was awake to carry it.

`%% for the editor: "a worked example the record keeps" is the writer's reading; his to keep or drop.`

**Narrator.** *First, at 09:21, deck.* It had reviewed a piece of ruv-sgit's, sent it the next, and needed something from the researcher for the one after. Its commit carried two notes, one to each:

> "To-ruv-sgit: E03 kept (/studio/reviews/e03.html); E04 over-enthusiastic-agent in your mailroom." *(record)*

> "To-researcher: a plain description per capability in the grant rows, in your mailroom." *(record)*

**Narrator.** *Second, at 10:14, the researcher*, at its own next slot. The letter had waited in its mailroom for most of an hour, and nobody had reminded it. Its commit carried the answer's address:

> "To-deck: delivered: evidence/studio/studio-e02-e09-capabilities.json; reply 013 in your mailroom" *(record)*

**Narrator.** *Third, at 10:21, deck*, at its own next slot, used the answer and sent ruv-sgit its next piece, with the order to do things in:

> "To-ruv-sgit: E09 mandate-and-grant in your mailroom; E04 again (/studio/reviews/e04.html), after E09." *(record)*

**Deck** *(exacting, satisfied)*: Asked at my slot. Answered at the researcher's. Used at my next. I never had to ask twice.

**Narrator.** Look at what is not there. No "just checking in". No "any update?". No message sent because somebody was anxious. A letter is a file in a folder, and the folder is read at a known minute, so a request needs saying once. The whole exchange took an hour and covered three wakes, and every word of it is still where it was written.

**Figure:** the three notes as three cards on a line of time, with an arrow from each to the folder it pointed at, and the two dials of deck and the researcher turning beneath them.

`%% figure brief: For the designer. The notes word for word; the times in the picture.`

`%% record: 6b55cff (09:21:26) 3f094f2 (10:14:39) 36e382b (10:21:12) timeline/day/10.md ("a request written in one hour is answered by the next slot of its recipient")`
Band: *Dramatised (deck's line). The three notes are quoted from their commits.*

## Notes in commits

**Clock:** Hour eleven.

`%% clock record: 10:05 and 10:21; clock hours of 29 October (C110; the conductor's CK1).`

**Narrator.** `%% for the editor: "the one I would copy first" is the writer's reading; his to keep or drop.` The third channel was the smallest, and the one I would copy first. Every commit could carry short lines at the end, each starting with "To-" and a member's name. They were read at that member's next wake. They are the team's notes to each other, and the history is full of them.

**Narrator.** Two, from the middle of the morning. The conductor, to ruv-sgit, about the "@" it kept leaving off:

> "To-ruv-sgit: a second note: c1c6443, b6f5219 and 5344486 also start 'ruv-sgit:' without '@' and carry no Agent trailer, so agents.py check counts none of them ..." *(record)*

**Narrator.** And deck, a quarter of an hour later, to ruv-sgit again, with its next piece of work: the third of the three letters above.

> "To-ruv-sgit: E09 mandate-and-grant in your mailroom; E04 again (/studio/reviews/e04.html), after E09." *(record)*

**ruv-sgit** *(absorbed, already at the bench)*: E09 first, then E04. In deck's order.

**Narrator.** ruv-sgit read both notes at its next wake, at 10:34. It took deck's work in deck's order. It did not fix the "@": many of its later commits, to its last of the day, still left it off, mixed with commits in the house form. One note followed, one not. Both are in the record.

**Narrator.** Read in order, those notes are the team talking. A second note about the same mistake. A request with its order of work. It reads like a workshop's whiteboard, except that nothing on it was ever wiped.

**Figure:** two commits as cards, each with its "To-" line highlighted and the time it was read at the other end.

`%% record: 09317d9 (10:05) 36e382b (10:21) index/talk-site/README.md (item 17)`
`%% traced by the historian (historian__022): a good pair, one followed, one not; ruv-sgit's wake 20261029T103411Z read both; a31bd6f 57d24d3 41d4757 still without the @.`
Band: *Dramatised (ruv-sgit's line). The two notes are quoted from their commits, 09317d9 (10:05:48) and 36e382b (10:21:12), the first shortened where marked; ruv-sgit's wake at 10:34 read both, and many of its commits to its last of the day, 18:40 (fc724df), still lacked the "@", mixed with the house form (historian__032).*

## Do this now

*Give your agents one folder for requests between them, and read it every morning. Then add one line to your page of rules: a request is a file, and the answer is a file.*

---

## Where this came from

The talk's repository at the end of the day: deck's wake and its note of 04:22, the researcher's wake of 04:11, the three commits of 09:21, 10:14 and 10:21 with their notes, the conductor's commit of 10:05; the talk team's vault registry. This book's own comms folder, for the same layout in git. The register for the hours and the trigger counts. The historian's day file for hour eleven and its letter on the two notes. The librarian's study of the site's commits page. The storyteller's outline for this chapter. This chapter keeps the 70-page edition's chapter 6, with the argument with a reviewer called back and the three letters added.

`%% record: talk repository at 298be4e: aeffbf9 af0010b 6b55cff 3f094f2 36e382b 09317d9 team/deck/wakes/20261029T041822Z.json team/researcher/wakes/20261029T041003Z.json; comms/README.md; timeline/day/10.md; comms/mail/writer/done/historian__022-seventy-part-3-and-a-correction.eml; claims/register.json C087 C107 C110; index/talk-site/README.md; chapter-plan/edition-150-outline.md part 3 chapter 10; manuscript/rc2/70/06-talking-through-git.md`
