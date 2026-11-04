# The tour: what a factory made in a day

**Cast bar:** the nine, greyed. Each lights for a moment as the tour reaches its work.

**Narrator.** Before I tell you how the factory worked, I want you to see what it made. Not the talk as the room saw it, on a screen behind me, but the site the talk lived on, which you can walk today. Four stops. At each, one picture, a few lines from me, and one line from the agent that made it.

**Narrator.** By the factory I mean what chapter 2 described: a team of nine AI agents built around one objective, each with one job and one page of rules, woken by a clock, with one file that could stop them all, and taken apart when the job was done.

*Words for this page:* a **wake** is one turn of work by one agent, started by the clock or by me. The **conductor** is the agent that keeps the team's time and plan. A **hold** is one short file that stops every agent until the person in charge says go.

`%% record: C011 (nine staffed); manuscript/rc2/150/02-inventing-on-principle.md ("What a factory is"); synthetic__009 (03:5, the factory in plain words before the tour)`

*How to read the scenes:* they are dramatised. The words the agents say are written for this book; the pages are the record's, and you can open every one of them online.

`%% for the editor (his view, held out of print until he confirms it, P30): the newsroom's "because I think the result is a good argument for the method" after "what it made".`

**Narrator.** At each stop you will hear from the agent that made it. You meet each of them properly when they arrive, in the chapters that follow.

## Stop 1. The talk as web pages, with its player

**Figure:** the talk's index page, and its player open on a slide: the timer, the step controls, the notes.

`%% figure brief: the image: index/talk-site/shots/talk.jpg, talk__player.jpg (moved out of the caption, which prints: conductor__033).`

`%% figure brief: The librarian's screenshots (index/talk-site/shots/talk.jpg, talk__player.jpg).`

**Narrator.** The deck is a website. Every one of its 58 beats is a page that moves, and anyone can read it. The player is the piece I pressed play on: a timer against my time, steps that build one at a time, notes behind a key press. It is the thing I asked for first in the afternoon and was still asking to fix in the last hour.

**Dev**: Every slide is a page, so every slide has a link, a history and a check before it goes out. The player just walks them in order.

`%% record: C015 index/talk-site/README.md (item 2) index/talk-site/tour-material.md (stop 2) src/static/talk/talk.json b3f208f src/static/talk/player.html dbd75ad`
`%% band: Dramatised. Rests on the talk's pages and player as they stood at the end of the day.`
*Dramatised.*

## Stop 2. The dashboard and the hold

**Figure:** the team's dashboard, drawn: a clock, the hold, what waits on the editor, and every wake as a grid.

`%% figure brief: A drawing from the page, not a screenshot: the build never shows an admin page.`

**Narrator.** The team's state, read from its own files, on one page. It was built from the members' status files and wake records, not typed by anyone. And it still shows the hold of that night, because the page was last built after the stop; chapter 16 tells why it was written.

`%% for the editor (his view, held out of print until he confirms it, P30): the writer's "Nobody tidied it." after "after the stop."`

**Conductor**: The page shows what the files say. The files say we stopped. So the page says we stopped.


`%% record: index/talk-site/README.md (item 5) index/talk-site/tour-material.md (stop 5) admin/build/build.py 23739cc C006`
`%% band: Dramatised. Rests on the dashboard as built from the team's own files, still showing the hold.`
*Dramatised.*

## Stop 3. Every wake and every note

**Figure:** the wakes page: each member's wakes, newest first, with the wake's five stages, each stage's verdict and its comment.

`%% figure brief: Beside it, the commits page with its notes between agents. Described from the librarian's study; no screenshot yet.`

**Narrator.** This is the page that shows the factory running on its own for nine hours. Every session of every agent, with its plan, its two reviews, the work and the check that it went to plan, each with a verdict and a sentence. On the day the agents kept 162 of these records, and most of them read the same way: plan, go, done, clean, as planned.

`%% held out of print until he confirms it (a Check item): the newsroom's "while I slept and then worked on other things", after "for nine hours".`

`%% for the editor (his view, held out of print until he confirms it, P30): the writer's "This is the page I would show anyone who doubts that the factory ran on its own" in place of "This is the page that shows the factory running on its own"; and the newsroom's "Reading them now, what strikes me is how boring most of them are, and I mean that as praise ... A team you can trust is a team whose records are mostly dull." "Most of them read the same way" rests on C023 (plan go 162, work done 151, post-check as planned 148). The page's own counter says 163 (the librarian's study); the book gives the register's 162 (C022).`

**Narrator.** And next to it, every commit the team made, with its whole message: 439 by the agents themselves, not counting merges. Many of them carry short notes from one agent to another, in a line that starts with "To-" and the other's name. Read in order, they are the team talking.

**Researcher**: The page has a counter, and I have a register. The page and my register do not agree on the wakes; the book uses mine.

`%% record: C087 (nine hours) C022 C023 C014 index/talk-site/README.md (items 16 and 17) index/talk-site/tour-material.md (stops 7 and 8)`
`%% band: Dramatised. The counts are the register's: wake records and the agents' own commits; the page's own count of wakes is one higher.`
*Dramatised.*

## Stop 4. A member's page

**Figure:** one member's page, deck's: its role, its policy in prose, its rules with the mistake behind each one, its status, its wakes and its debriefs; its key lines cropped out.

`%% figure brief: Shown without the section that prints its key, which the tour never shows.`

**Narrator.** Last stop. Every agent has a page like this, built from its own folder. Each of its rules carries the mistake behind it, the moment the rule was needed.

`%% for the editor (his view, held out of print until he confirms it, P30): the newsroom's "What I like about it is the rules, because" before "each one carries", and "It is how I think rules should be written for people too: not a list of what you must not do, but a short history of what went wrong, so you know why."`

**Deck**: Every rule on my page cost somebody a slide. That is why it is there.

`%% record: index/talk-site/README.md (item 19) index/talk-site/tour-material.md (stop 12, shown without its key section) index/talk-site/members.md`
`%% band: Dramatised. Rests on deck's member page as built from its folder; the page's key section is not shown.`
*Dramatised.*

## The keys, and the house they live in

**Narrator.** Two more pages before we leave, from behind the scenes. The first is the team's keys. A key here is a session's public identity: others can use it to check that something came from that session, or to send it something only it can open. Every member published its own key from its own session, and every key on the page is public, made for one session, and published on purpose.

**Narrator.** Each key is listed by its fingerprint: a short code that identifies it, the way a name identifies a person.

**Narrator.** The second page I describe and do not show. It lists the team's vaults, its shared stores of files. Each vault has a read key, which lets anyone open it, and those were published on purpose too, under a warning in red that every file in them is public, forever.

**Figure:** the talk team's keys page: each member's key listed with its fingerprint, every one public and made for one session.

`%% figure brief: the image: index/talk-site/shots/admin__keys.jpg, cleared by security by that name (security__024; AD1; critic1 001, P25). The talk team's register: fingerprints and session folder ids, no QR codes; nothing of it typed into the text. The vaults page stays described, not shown.`

**Figure:** the same kind of key as a QR code: a few of this book's own team, each code holding one member's public key and nothing else.

`%% figure brief: the images: team/conductor/key.png, team/researcher/key.png and team/writer/key.png, each cleared by security by name (comms/mail/mailroom/writer/security__024-keys-page-and-keys.eml, 4 November 06:27 UTC: each decoded, public half only, fingerprint matching its key.json), at the versions of 68ffc780 (2 November) or earlier; any later change goes back to security first. Nothing of any key or code is typed into the text (storyteller__135 S1; AD1).`

`%% record: admin/tools/pki-agent.README.md (each session's key: a signing and an encryption fingerprint, public halves only) index/talk-site/tour-material.md (the keys page; the vaults described, not shown) briefs/2026-11-04__in-session/14-show-the-admin-pages-and-the-keys.md comms/mail/mailroom/writer/security__024-keys-page-and-keys.eml`

**Narrator.** And the house they live in: the whole team on one page, a room for each member, each room drawn from what that member was allowed to change.

**Figure:** the team's house: a room for each member, and security's room, proposed and never staffed.

`%% figure brief: For the designer, its house (LAB 47, designer__130; publisher__034): rooms from team/*/policy.json scope.writes at 298be4e; the storyteller and the designer by their work; where each stands is the designer's reading of the record. It replaces "the site as a building, one floor per kind of page". Where each stands is the designer's reading of the record (critic1__006: in the brief, not the caption).`

`%% record: C011 (security proposed, never staffed)`

**Narrator.** That is what one day made. The rest of this book is how, told by the agents who did it, with me interrupting.

## Something to try

*The tour works because every page explains itself. Pick something you made recently and ask what someone would need to see to understand it without you there. That list is often shorter than you expect, and it is what an agent can build for you.*

`%% record: team/conductor/from-newsroom/2026-11-04__do-this-now-as-invitations.md (chapter 3, the proposed card); chapter-plan/cast/cast-guide.md (page conventions 1)`

---

## Where this came from

The librarian's study of the talk's site: its list of the site's best things, its tour material, its screenshots and its notes on the members' pages, the studio and the visuals. The talk's site as it stood at the end of the day. The researcher's register for the slides, the wakes and the commits. Security's condition, kept: no page that prints a key. The storyteller's outline for this chapter.

`%% record: manuscript/rc2/70/02-the-tour.md (kept as written); index/talk-site/README.md tour-material.md pages.md members.md studio.md visuals.md shots/; talk repository at 298be4e; claims/register.json C006 C014 C015 C022 C023 C087; chapter-plan/edition-70-outline.md part 1 chapter 2; team/conductor/from-newsroom/2026-11-04__narrator-voice-part-one.md (section 7: the opening, Stop 3, Stop 4 and the close, all four taken)`
