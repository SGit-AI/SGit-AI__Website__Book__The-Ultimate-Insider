# Talking through git

**Cast bar:** six agents: dev, the conductor, deck, ruv-sgit, the researcher, the designer. The editor's chair is empty.

## No meeting, no channel, no whiteboard

**Narrator.** While the factory ran, two things ran under it.

`%% for the editor: the interlude's opening line (SC2, brief 36, signed; the storyteller's wording in its 163); chapters 10 and 11 step outside the clock, and 11 hands back to it ("In hour fourteen, I came back.").`

**Narrator.** For nine hours I started nothing, and the team kept talking. A team of people in that position would have had a meeting, or a chat channel, or someone at a whiteboard. This team had none of those. It had files: letters in folders, a board in folders, and short notes on its commits, all kept in git, the tool programmers use to keep every version of every file, with who changed what, and when. Everything one agent said to another was written down somewhere the other would read it at its next session.

`%% Hold (P30: an opinion in his voice, the newsroom's; prints once he confirms; storyteller__150): "I have come to think this is one of the most useful ideas in the whole book, and one of the easiest to copy: if your agents talk through files, you get the conversation and its history for free."`

`%% for the editor: the opening is the newsroom journalist's rewrite (part three, chapter 10), close to its words; "one of the most useful ideas in the whole book" is his to keep or change.`

`%% record: C087 (hours 05 to 13 UTC, nine hours, no wake started by me) timeline/triggers.md`
`%% band: The wakes by trigger, hour by hour; none started by me from just after four to about ten to two.`

## The mail and the board as files

**Narrator.** Here is how one agent asked another for work. It wrote a short letter, as a file, put it in the other's mailroom, kept a copy in its own outbox, and did not wait. At the other's next session, that agent read its mailroom, answered, and moved the letter to its own folder of things in hand. Nobody had to be awake at the same time as anybody else.

**Narrator.** The talk's team kept its mail and its board in two public vaults, shared folders any member could read, synced between their sessions, under a warning that everything in them was public, for ever. This book's team keeps the same two layouts as folders in its own repository. Either way the shape is the same: a letter is a file, an answer is a file, and the history of who asked whom for what is just a list of files with times on them.

*Words for this page:* the **mailroom** is a folder per member where others leave it letters. The **board** is a folder per member of its own work, sorted into open, blocked and done.

`%% Check (the newsroom, part three, chapter 10; his to confirm before it prints): "Either way the shape is the same, and it is the shape I keep coming back to in my own work with sgit: a letter is a file, an answer is a file, and the history of who asked whom for what is just a list of files with times on them."`

**Figure:** a letter's path on the clock: written in one agent's outbox, dropped in another's mailroom, read at that agent's next minute, answered, and filed. Two dials, one per agent, with the letter crossing between them.

`%% figure brief: For the designer. Show one letter as a file, with its headers (From, To, Date, Subject, the kind of letter), and one board folder with open, blocked and done.`

`%% Hold (P30: a reading of his view, not in the record or his briefs; prints once he confirms; storyteller__147): "And here is the part I did not expect."`

**Narrator.** Because asking was cheap and answering was scheduled, a check could also hold a request back: in chapter 8, deck's own reviewer asked it to wait, because one of its requests was already in flight, and deck held the second.

`%% record: aeffbf9 (04:22, deck to the conductor) team/deck/wakes/20261029T041822Z.json manuscript/rc2/150/08-hours-four-and-five-before-dawn.md (deck holds itself back); the talk team's vaults, named and not cited by path; comms/README.md (this book's); the storyteller's ruling 1 for part three (chapter-plan/edition-150-outline.md): the hold told in 8, one line here`

## A member and its own checker

**Narrator.** Not every conversation was between two members. Some were between a member and its own checker, and those are written down too. The researcher's argument with its reviewer, in chapter 8, is in its record, both halves of it, the objection and its withdrawal. Nobody had to remember it, which is the point: a disagreement that is written down can be learned from, and one that is remembered usually cannot.

`%% record: C107 af0010b team/researcher/wakes/20261029T041003Z.json manuscript/rc2/150/08-hours-four-and-five-before-dawn.md ("The argument with a reviewer")`

## Three letters in a row

**Clock:** Hours ten and eleven.

`%% clock record: 09:21, 10:14 and 10:21; clock hours of 29 October (C110; the conductor's CK1).`

**Narrator.** Here is one request as the team actually wrote it, a note on a commit, read at the other member's next session. It is how a request travelled when nobody was awake to carry it.

**Deck**: In the middle of the morning I needed something from the researcher for my next piece, so my commit carried a note to it:

> "To-researcher: a plain description per capability in the grant rows, in your mailroom."

**Researcher**: It waited in my mailroom until my next session, and nobody reminded me. My answer went back the same way, with its address on my commit.

**Deck**: I asked once, at my session. The researcher answered at its own. I used it at my next, and sent ruv-sgit its next piece. Nobody chased anybody, and I did not have to ask twice.

`%% Hold (P30: an opinion in his voice, the newsroom's; prints once he confirms; storyteller__150): "What I like most is what is missing."`

**Narrator.** No "just checking in". No "any update?". No message sent because somebody was anxious. A letter is a file in a folder, and the folder is read at a known minute, so a request only needs saying once. The whole exchange took an hour and three sessions, and every word of it is still where it was written.

`%% Check (the newsroom, part three, chapter 10; his to confirm before it prints): "I would happily work that way with people too."`

**Figure:** the three notes as three cards on a line of time, with an arrow from each to the folder it pointed at, and the two dials of deck and the researcher turning beneath them.

`%% figure brief: For the designer. The notes word for word; the times in the picture.`

`%% record: 6b55cff (09:21:26) 3f094f2 (10:14:39) 36e382b (10:21:12) timeline/day/10.md ("a request written in one hour is answered by the next slot of its recipient")`
`%% band: Dramatised (deck's and the researcher's lines, told in their voices at critic2__003; one note quoted, the three drawn word for word in the figure, the newsroom's pass 2, p59 to 60). The notes in the record: 6b55cff "To-ruv-sgit: E03 kept (/studio/reviews/e03.html); E04 over-enthusiastic-agent in your mailroom." and "To-researcher: ..."; 3f094f2 "To-deck: delivered: evidence/studio/studio-e02-e09-capabilities.json; reply 013 in your mailroom"; 36e382b "To-ruv-sgit: E09 mandate-and-grant in your mailroom; E04 again (/studio/reviews/e04.html), after E09."; the researcher's answer came almost an hour after deck's ask, deck's next note six and a half minutes after that (historian__054).`
*Dramatised.*

## Notes in commits

**Clock:** Hour eleven.

`%% clock record: 10:05 and 10:21; clock hours of 29 October (C110; the conductor's CK1).`

`%% Hold (P30: a reading of his view, not in the record or his briefs; prints once he confirms; storyteller__147): "... and the one I would copy first."`

**Narrator.** The third channel was the smallest. Every commit could carry short lines at the end, each starting with "To-" and a member's name. They were read at that member's next session. They are the team's notes to each other, and the history is full of them.

**Narrator.** Two, from the middle of the morning. The conductor, to ruv-sgit, about the "@" it kept leaving off:

> "To-ruv-sgit: a second note: ... also start 'ruv-sgit:' without '@' and carry no Agent trailer ..." *(record)*

**Narrator.** Without them, the team's own count of who did what missed those commits.

`%% record: the elided commits in the conductor's note: c1c6443 b6f5219 5344486 (researcher__002 to writer2: the hashes off the page); the note goes on "so agents.py check counts none of them", put in plain words above (synthetic__001)`

**ruv-sgit** *(already at the bench)*: I read both notes. I did what deck asked next, in the order it asked. The "@" I left as it was.

**Narrator.** Many of its later commits still left it off. One note followed, one not, and both are in the record.

`%% Check (the newsroom, part three, chapter 10; his to confirm before it prints, the newsroom's question 1): "I find that oddly reassuring: the agents ignored the boring housekeeping request and acted on the one about real work, which is very much what people do too."`

**Narrator.** In order, those notes are the team talking: a second note about the same mistake, and nothing on it ever wiped.

`%% Hold (P30: a reading of his view, not in the record or his briefs; prints once he confirms; storyteller__147): "It reads like a workshop's whiteboard, except that nothing on it was ever wiped."`

**Figure:** two commits as cards, each with its "To-" line highlighted and the time it was read at the other end.

`%% record: 09317d9 (10:05) 36e382b (10:21) index/talk-site/README.md (item 17)`
`%% traced by the historian (historian__022): a good pair, one followed, one not; ruv-sgit's wake 20261029T103411Z read both; a31bd6f 57d24d3 41d4757 still without the @.`
`%% band: Dramatised (ruv-sgit's line, now telling what it did: storyteller__147, S3; deck's third letter told once, S2). The two notes are quoted from their commits, 09317d9 (10:05:48) and 36e382b (10:21:12), the first shortened where marked; ruv-sgit's wake at 10:34 read both, and many of its commits to its last of the day, 18:40 (fc724df), still lacked the "@", mixed with the house form (historian__032).`
*Dramatised.*

## Something to try

*The team talked through files, so every request and answer could be read later. If you have more than one agent, try one folder for their requests, and a rule: a request is a file, and so is its answer.*

`%% record: team/conductor/from-newsroom/2026-11-04__do-this-now-as-invitations.md (chapter 10, the proposed card); chapter-plan/cast/cast-guide.md (page conventions 1)`

---

## Where this came from

The talk's repository at the end of the day: deck's wake and its note of 04:22 (pointed back to, in chapter 8), the researcher's wake of 04:11, the three commits of 09:21, 10:14 and 10:21 with their notes, the conductor's commit of 10:05; the talk team's vault registry. This book's own comms folder, for the same layout in git. The register for the hours and the trigger counts. The historian's day file for hour eleven and its letter on the two notes. The librarian's study of the site's commits page. The storyteller's outline for this chapter. The newsroom journalist's pass on the narrator for part three, and its card. This chapter keeps the 70-page edition's chapter 6, with the argument with a reviewer called back and the three letters told here in full, once.

`%% record: talk repository at 298be4e: aeffbf9 af0010b 6b55cff 3f094f2 36e382b 09317d9 team/deck/wakes/20261029T041822Z.json team/researcher/wakes/20261029T041003Z.json; comms/README.md; timeline/day/10.md; comms/mail/writer/done/historian__022-seventy-part-3-and-a-correction.eml; claims/register.json C087 C107 C110; index/talk-site/README.md; chapter-plan/edition-150-outline.md part 3 chapter 10 and its rulings for part three; team/conductor/from-newsroom/2026-11-04__narrator-voice-part-three.md (chapter 10) team/conductor/from-newsroom/2026-11-04__do-this-now-as-invitations.md; manuscript/rc2/70/06-talking-through-git.md`
