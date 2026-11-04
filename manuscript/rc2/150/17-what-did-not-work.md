# What did not work

**Cast bar:** all nine, after the hold; security's chair empty. Off the clock now.

**Narrator.** This chapter has no clock in the margin. The day is over, and what is left is the accounting, at full size: the failures stay in.

`%% for the editor: proposed, not printed until you confirm (the writer's reading, then the newsroom's added line, chapter 17): "I want it at full size, because the failures are the useful part, and because a book about a factory that only shows what worked would be a brochure. In security we learn more from incidents than from anything that went well, and I think the same is true here."`

## The miss behind the stop

**Narrator.** Chapter 16 told why I stopped. Behind it is a miss nobody on the team owned: there was no tested way to take a change in while the talk was running, see what was new, and know it would not break what was finished.

`%% for the editor: proposed, not printed until you confirm (the newsroom, chapter 17): "and I would do the same again" after "show"; and, at the end, "Next time, that is the first thing I would build."`

`%% record: C089 (settled 4 November: time ran out, diminishing returns, the 95% a coincidence; the missing way to take in changes during the talk is his own account of 31 October, after the day: 49c701e, "the reason why I was thinking about let's lock V1") C006 C027 C100 timeline/after-the-day.md`
`%% band: The miss as he named it after the day; the reason for the stop is told once, in chapter 16.`

## The misses, one at a time

**Figure:** ruv-sgit's strip, the researcher interviewing deck about the claims that did not hold.

`%% figure brief: lab/experiments/25-ruv-the-cast-strips/edition/strip-10-07.svg`

**Narrator.** Each miss has its own card: what happened, what it cost, and whose own record says so. Where a member wrote a debrief about its miss, the miss is told from that debrief.

### The lock never turned

*What it cost:* the first part was never locked; nothing stopped it changing on stage but the hold. *Whose record:* dev's last wake, and the conductor's request.

**Narrator.** Told in chapter 16.

**Dev**: I built the lock, and I never turned it. Every time I looked up, there was one more fix.

`%% record: 4a2481b (17:54) 2ed6427 (18:39) dbd75ad (18:37) team/dev/wakes/20261029T174850Z.json 39df303 (18:48, on a branch) timeline/unmerged.md C027 C088 timeline/interviews/dev.md`
`%% band: Dramatised (dev's lines). Rests on the lock tool, the conductor's request, dev's last wake and its close on a branch.`
*Dramatised.*

### Two parts of three unfinished

*What it cost:* two parts of the talk never reached their finished state. *Whose record:* deck's status and its last wake.

**Narrator.** Only part one of the talk was finished. Parts two and three were still in progress when I stopped, and deck's last session, which had planned them, never closed.

**Deck**: Only the first part was ever finished.

**Deck** *(to itself, rearranging slides that will not be shown)*: I reviewed other agents' work all night. I did not finish my own.

`%% record: team/deck/status.json at 298be4e ("next": parts 2 and 3) team/deck/wakes/20261029T182009Z.json (never closed) 89afb77 (18:21) C027 timeline/interviews/deck.md`
`%% band: Dramatised (deck's lines). Rests on deck's status and its last wake.`
*Dramatised.*

### The moment missed

*What it cost:* the talk was split into parts without the storyteller's split. *Whose record:* the storyteller's debrief.

**Narrator.** The conductor asked the storyteller to split the story into three parts by a deadline in the late afternoon. The request landed between the storyteller's sessions, its next turn came after the deadline, and deck had set part one before the split reached it. The storyteller's own letter to deck says the split "is late".

**Storyteller**: My turn came after the deadline. A slot every hour is fine until the decisions come faster than the slots.

`%% record: 3342cff (16:59, "To-storyteller: split the arc into three parts ... to deck by 17:30") team/storyteller/debriefs/2026-10-29__three-parts.md team/storyteller/requests/deck__three-parts.md ("is late") 3260997 (17:25, part one set) timeline/interviews/storyteller.md`
`%% band: Dramatised (the storyteller's lines). Rests on the conductor's brief, the storyteller's debrief and its letter to deck.`
*Dramatised.*

### The correction lost in the freeze

*What it cost:* an out-of-date figure on a slide at the end of the day. *Whose record:* the researcher's proposal and deck's reply file.

**Narrator.** In the night I froze the slides, and five minutes later the researcher sent a correction to a figure on one of them: the average annual cost of insider risk. The figure had been on the definition slide since the first pass. When I lifted the freeze, for the framing only, nobody carried the correction back in, and the out-of-date figure was still on the slide at the end of the day. The researcher had the newer figure from its source; nobody owned moving it across the lift.

`%% for the editor: proposed, not printed until you confirm (the newsroom, chapter 17; critic3's P32): "That one is mine. I set the freeze, and I did not say what was waiting when it ended."`

**Narrator.** The figure: the slide said $17.4M a year, the 2025 edition's number, from a survey a vendor paid for; the 2026 edition says US$19.5M. The record caught it, and the freeze kept it in.

`%% for the editor: proposed, not printed until you confirm (the writer's reading, the storyteller's M2): "Not a disaster on stage. A small, true error."`

`%% for the editor: proposed, not printed until you confirm (the newsroom, chapter 17; the storyteller's M3): "What I would do differently: when I freeze something, I write down what is waiting to go in when it is unfrozen."`

`%% record: C031 (on stage $17.4M, Ponemon for DTEX, 2025 edition; at source in 2026, US$19.5M; correction proposed a082c52, 02:52; the freeze 02:47; lifted 14:07 for the framing only; the slide file has no commit after 00:40) team/deck/requests/researcher__before-tonight.md (deck's 03:00 update)`
`%% band: The register's account of the figure, the freeze and the correction.`

### Other sites' data, pushed before it was stripped

*What it cost:* values from other sites' pages went out in a public push, and the history keeps what was pushed. *Whose record:* the researcher's debrief and the post-reviews.

**Narrator.** Told in chapter 8. Pages the researcher captured as evidence carried other sites' data in with them, three times in the night, and each time the team's own checks caught it, two of them after the push. None of it was a key, a credential or anything personal. Looking back, it was nothing sensitive, an agent that got a bit excited, and I keep it here as an example of the checks catching things.

**Researcher**: I would build the redaction before the first push, not after the findings.

`%% record: C025 (entries 2 to 4: two found after the push, one before the close) C068 ("none a key, an account credential, a vault key or a personal detail") team/researcher/debriefs/2026-10-29__the-first-evidence-round.md timeline/interviews/researcher.md (its "what could we do better", reconstructed)`
`%% band: Dramatised (the researcher's line, on its reconstructed interview's own lesson). Told as the team's finding only: nothing of what was captured, how, or from where. The decision about the vault's history (D12) is settled by his word and not printed (briefs/2026-11-04__in-session/20, "a massive kind of false positive"; added after the day).`
*Dramatised.*

### A key printed into a log

*What it cost:* a vault key in one session's own log, and a rotation. *Whose record:* the conductor's debrief.

**Conductor**: Checking a format, I printed a vault key into my own session log. I rotated it at once, and I wrote it down. It is my worst moment of the day, by my own record.

**Narrator.** The response is what this card records: the key rotated first, the report straight after, nothing hidden.

`%% for the editor: proposed, not printed until you confirm (the newsroom, chapter 17; the storyteller's S5): "I want it in, because the response is the part to copy. That is what I would ask of any engineer on my team."`

`%% record: team/conductor/debriefs/2026-10-29__hourly-and-handover.md team/conductor/debriefs/2026-10-29__two-public-vaults.md timeline/interviews/conductor.md`
`%% band: Dramatised (the conductor's line). The event and the rotation only; nothing of the key is printed.`
*Dramatised.*

### A record that says what did not happen

*What it cost:* the next session would have read part one as locked. *Whose record:* the designer's status, against the conductor's.

**Narrator.** The designer's last status says part one was locked after its check. It never was. The conductor's last request to dev and the hold file both say not locked, and the register counts the parts locked by the end of the day at none. The designer wrote what had been planned, not what had happened, in the one file the next session would trust.

**Designer**: I wrote the plan down as if it were the fact. A status is the wrong place for a guess.

`%% record: team/designer/status.json at 298be4e ("locked at 18:30 after its check") 2ed6427 team/conductor/HOLD.md C027 timeline/interviews/designer.md`
`%% band: Dramatised (the designer's line, on its reconstructed interview's own lesson). Rests on its status file and the conductor's record.`
*Dramatised.*

### Work with no name on it

*What it cost:* the team's count of work by member could not see some of it. *Whose record:* the commits themselves, and the register's correction.

**Narrator.** Two kinds. In the afternoon, the player's commits went out with no member named in their subjects; only the trailers show they were dev's. And from the morning, many of ruv-sgit's commits left off the "@" in front of its name. Anything counting work by the subject line saw work landing with nobody's name on it. The register's count of commits by member was corrected for both, afterwards.

`%% record: C014 (commits by member, with or without @, and its correction) 28fe01d fb355d3 23739cc 12e93db 013d97e dbd75ad c33e86a 4a2481b (Agent: dev in their trailers) 15707dc (08:43) fc724df (18:40) timeline/day/08.md 16.md`
`%% band: The commits as they stand, and the register's count of them.`

### The claims that did not hold

*What it cost:* nothing on stage: no beat of the talk carries any of them. *Whose record:* the talk's own register of claims.

**Narrator.** The talk's own register, built that evening, graded every claim it made, and three did not hold. One was in the article only, one on no beat or slide at all, one in the story tree only. No beat of the talk carries any of the three. The one in the story tree was the objection chapter 13 told, and I kept my line.

**Researcher** *(ticking a list)*: I marked each one that did not hold. The day's checks worked, and they also missed. Saying where is part of the method.

**Figure:** the misses as cards on one page, each with its cost in a line.

`%% layout: full`

`%% figure brief: For the designer. One card per section above, nine in order; no register id inside the drawing (principle 28); the sources of each card, for the record only: the lock (C027), the parts (C027), the moment (3342cff), the freeze (C031), the captures (C025, C068), the printed key (the conductor's debrief), the status (C027), the unnamed work (C014), the claims (C029, C030).`

`%% record: C029 C030 (where each of the three was) 78d517d (15:16, my answer to R5)`
`%% band: Dramatised (the researcher's line). Rests on the talk's register of claims.`
*Dramatised.*

## Something to try

*A short list of your last few misses, each with what it cost and what would catch it sooner, is the cheapest memory a team of agents can have. If you keep one, keep it where your agents will read it.*

---

## Where this came from

My account of why we stopped, given after the day, as the register holds it, and the miss behind it. The talk's repository at the end of the day: the lock tool and dev's last wake, deck's status and its last wake, the conductor's brief to the storyteller and the storyteller's debrief, the freeze and the correction proposed after it, the researcher's captures and their post-reviews, the conductor's debriefs, the designer's status, the commits with no member's name. The register for every miss it holds. The historian's reconstructed interviews, for the members' own lessons. ruv-sgit's interview strip. The storyteller's outline for this chapter. This chapter grows from the 70-page edition's chapter 11.

`%% record: claims/register.json C006 C014 C025 C027 C029 C030 C031 C068 C088 C089 C100; timeline/after-the-day.md; timeline/interviews/; timeline/unmerged.md; talk repository at 298be4e: 4a2481b 2ed6427 dbd75ad 39df303 89afb77 3342cff 3260997 a082c52 15707dc fc724df team/dev/wakes/20261029T174850Z.json team/deck/wakes/20261029T182009Z.json team/storyteller/debriefs/2026-10-29__three-parts.md team/researcher/debriefs/2026-10-29__the-first-evidence-round.md team/conductor/debriefs/2026-10-29__hourly-and-handover.md team/designer/status.json; lab/experiments/25-ruv-the-cast-strips/edition/; chapter-plan/edition-150-outline.md part four chapter 17; manuscript/rc2/70/11-what-did-not-work.md`
