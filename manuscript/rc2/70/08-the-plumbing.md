# The plumbing

**Cast bar:** all of them, all day: this chapter is about what ran under every scene.

`%% for the editor: "Nobody puts the plumbing in the brochure." and "It was the most important one." are the writer's; his to keep or drop.`

**Narrator.** Nobody puts the plumbing in the brochure. But every story in this book ran through four pipes, and if you build your own factory you will need all four. A site to work on. A check every change passes. A register for every number. And a brief, with a file beside it for what turned out to be true.

**Figure:** the plumbing as a building's services: the site, the check, the register and the brief, each drawn as a pipe running into the factory floor.

`%% figure brief: For the designer. Four pipes, labelled, each with the one thing it carries: the work, the yes or no, the source, what was asked and what is real.`

## The site is the scaffolding

**Narrator.** The agents did not work in a chat window. They worked on a website: every slide a page, every member a page, every wake and every commit a row on a page. That sounds like an odd choice for a talk. It was the most important one.

**Narrator.** A website gives an agent somewhere to put things that stays put. Its work is a file with a history, not a message that scrolls away. And a site can show the team its own state: the dashboard, the wakes page, the release history, all built from the files the agents wrote. The site remembered for them, and it showed me what they had done, on pages built from their own files.

**Dev** *(happy, the fast one)*: Every page is a file, so every page has a history and a check before it goes out. You never have to ask what changed. You look.

`%% record: index/talk-site/README.md (items 2, 5, 16 to 18); talk repository at 298be4e: admin/build/build.py`
Band: *Dramatised (dev's line). Rests on the talk's site as it stood at the end of the day.*

## The check that keeps it true

**Narrator.** Every change to the site went through the same check before it could go out: every link resolves, every page has its plain-text twin, no code loaded from elsewhere, every script parses, every beat has a slide, no long dash in the prose, and a tripwire over every file for anything that looks like a secret. If any of those failed, the change stopped.

**Narrator.** The check does not care who made the change, or how sure they were. That is the point of it. A member that is certain its work is fine still has to pass the same test as one that is not.

**Narrator.** One example from the first night. At about a quarter past one, the check stopped dev's release until two members' pages of rules carried a rule I had just asked for: every session report opens and closes with a banner. Dev added the lines; the release went out.

`%% record: 24da366 (about 01:19) team/dev/debriefs (the-board.md: "the gate the conductor added at the editor's rule refused the release without it"); historian__022`

**Narrator.** And the release history shows the result: each release the pipeline made, the commits it carried, the files they changed and the pages those files produce. Nobody typed a version number all day. The pipeline numbered every release itself. Deck's page of rules gives the reason: agents racing for release numbers is how another team, the newsroom, had lost releases on 27 October.

**Figure:** one row of the release history, drawn: a release number, its commits, the files changed and the pages they make. A drawing from the page, not a screenshot: the build never shows an admin page.

`%% record: 1f7c633 (admin/build/validate.py) index/talk-site/README.md (item 18) team/deck/ROLE.md at 298be4e ("Never type a version number ...")`
Band: *The check as first built at 00:40, and the release history as the site showed it.*

## Every number traced

**Narrator.** The talk made claims. Numbers about insiders, about breaches, about what agents do. Every one of them went into a register: a file listing the claim, where it came from, the captured source, and a grade for how well the source supports it. By early evening the register held 320 claims. 210 held. 55 held in part. 52 had not been checked. Three did not hold.

**Researcher** *(unbudging)*: A claim without a captured source is a gap, and the register says so rather than leaving it out. Gaps are allowed. Hiding them is not.

**Narrator.** Three did not hold, and none of those three was said on stage. That is not luck. It is the register doing its job: the researcher marked them, and the story went round them.

**Narrator.** This book works the same way. Its researcher keeps a register, and no number goes on a page unless it is there. When an early draft of this book carried a line the record could not support, it came back by letter, and the line was changed.

**Figure:** the talk's register as a stacked bar: held, held in part, not checked, did not hold. The counts in the bar, with its id in small type.

`%% record: C029 (320 claims, built 18:20: 210 hold, 55 hold in part, 52 not checked, 3 do not hold) C030 (the three, none on stage) team/researcher/ROLE.md at 298be4e claims/README.md (this book's register)`
Band: *Dramatised (the researcher's line). The talk's own register of claims, as the book's register counts it.*

## The brief and its corrections

**Narrator.** The last pipe is the simplest, and on the day it was the one that did not quite work.

**Narrator.** The brief was my request, published in full and never edited. Beside it sat two files. The reality file, kept current by whoever shipped: what exists now, and nothing else. It changed all day, every time something was built. And the corrections file, for when the brief turned out to be wrong.

**Narrator.** At the end of the day, the corrections file still said what it said in the first half hour:

> "None yet." *(record)*

**Narrator.** The brief was wrong in places. My request in it says the talk is "tomorrow"; by the time the project existed, it was that same day. The talk it asks for became something different as the day went on, in my own decisions of the afternoon. None of that went into the corrections file. It went into the reality file, the decisions, the debriefs. The rule was right; nobody used it.

**Narrator.** I would keep the file, and give one member the job of writing in it. A brief that is never corrected becomes a story about what you thought you wanted.

`%% for the editor: "I would keep the file, and give one member the job of writing in it." and the sentence after it are the writer's reading of his view; his to keep or drop.`

`%% record: fde3fea (this book: the researcher's trace refusing a line) talk repository at 298be4e: BRIEF.md BRIEF-CORRECTIONS.md (unchanged since 1f7c633) REALITY.md (changed through the day, last at 17:42, 70d4981); BRIEF.md's request: "presentation that I'm delivering tomorrow in central london"; C104 (the afternoon's decisions)`
Band: *The brief, the reality file and the corrections file as they stood at the end of the day.*

## Do this now

*Add one check to your project that every change must pass. Start with the one that would have saved you last time.*

---

## Where this came from

The talk's site and repository at the end of the day: the build and the check, the release history, the brief, the reality file and the corrections file, the members' pages of rules. The register: the talk's claims and the three that did not hold, the afternoon's decisions. The librarian's study of the site. The storyteller's outline for this chapter.

`%% record: talk repository at 298be4e: 1f7c633 admin/build/build.py admin/build/validate.py BRIEF.md BRIEF-CORRECTIONS.md REALITY.md team/deck/ROLE.md team/researcher/ROLE.md; claims/register.json C029 C030 C104; index/talk-site/README.md; chapter-plan/edition-70-outline.md part 3 chapter 8`
