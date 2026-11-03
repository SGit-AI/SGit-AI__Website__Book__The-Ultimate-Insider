# Roles as a cast you can read

**Cast bar:** the four within the hour lit; the researcher and the designer lit before dawn; the storyteller, motion and studio greyed; one empty chair.

**Narrator.** Every member of the team had two files about itself. A page of rules, in words, saying what it is for and what it must not do. And a policy, in a form a program can check, listing the exact paths it may write. You can read both. That is the point: a team of agents you cannot read is a team you cannot trust.

*Words for this page:* a member's **scope** is the list of files and folders it may change. Everything else, it may read and not touch.

**Narrator.** Here they are, in the order they arrived, each with what it owned, what it could change, and one rule with the mistake behind it. Most of their rules end with a date and a reason: the moment the rule was needed.

## The four within the hour

**Dev** *(happy, the fast one)*: Build, gate and release. I may change the build, the check, the release pipeline, the site's own pages and the reality file. Not the talk's slides; those are deck's.

**Narrator.** Dev's page of rules does something I wish every page did: it says what stands between the agent and each thing it must not do, and how strong that is. Pushing to the main branch: an expectation. Writing another member's files: a setting, which a check catches. Its own words for that check: it "catches mistakes, not a steered agent".

**Conductor** *(pacing)*: The schedule, the keys and the session conventions. I may change my own folder, the team's tools and the team's guides. I route the mail. I never sign for the editor.

**Narrator.** The conductor's rule I would copy is the one about requests: route each one to its owner, and flag any request left unanswered after two slots. A team that loses a request quietly is worse than one that says no.

**Deck** *(proud, the fussy one)*: The talk's content, and the studio that improves it. The beats, the slides, the studio's pages. And the rule behind most of my reviews: check each changed slide in the player at projector size before shipping. A slide only seen as code is a slide not seen.

**Deck** *(fussing with its own page)*: And never type a version number. That one is somebody else's scar, from another team's bad day. We inherited it.

**ruv-sgit** *(absorbed, the night owl)*: Animations and moving infographics, made in my own runs. I may change my folder and my pages. One rule I learned the hard way: the container is ephemeral. Seal what you keep, or say what you lost, before the session ends.

`%% record: talk repository at 298be4e: team/dev/ROLE.md team/dev/policy.json team/conductor/ROLE.md team/conductor/policy.json team/deck/ROLE.md team/deck/policy.json team/ruv-sgit/ROLE.md team/ruv-sgit/policy.json; index/talk-site/members.md`
Band: *Dramatised. Each line rests on that member's page of rules and policy as they stood at the end of the day; the rules quoted in the narrator's lines are their own.*

## Before dawn: the researcher and the designer

**Narrator.** The two who came before dawn are as interesting for what they could not do as for what they could.

**Researcher** *(unbudging)*: Sources and evidence. Every source captured and hashed, and a register of claims. I may write my own folder and the evidence folder. Nothing else.

**Researcher** *(to the rest of the team)*: A claim without a captured source is a gap, and my register says so rather than leaving it out. And a measured finding, a position and a guess are not the same thing. I label each.

**Narrator.** The researcher could not change a slide. It could only say that a number on one did not hold. That is a strong position precisely because it is a narrow one: nobody could accuse it of changing the story to suit its findings.

**Designer** *(beret and pencil)*: Layout, width, type, the design system. I may write only my own folder.

**Designer** *(firm about whose word counts)*: So I do not change a page. I write a note, with before and after, and dev builds it. At my next wake I check: as designed, or what to fix.

**Narrator.** The designer's scope is the smallest on the team: its own folder, nothing else. Every change it wanted went through someone else's hands. That slowed it down, and it also meant every design change had two readers.

`%% record: talk repository at 298be4e: team/researcher/ROLE.md team/researcher/policy.json team/designer/ROLE.md team/designer/policy.json`
Band: *Dramatised. Rests on the researcher's and the designer's pages of rules and policies as they stood at the end of the day.*

## The three who came in the afternoon

**Narrator.** Three more came after I was back, and you will meet them properly in part 3. For now, their briefs in a line each.

**Figure:** three greyed cards: the storyteller, the talk's story, the arc, the tree and the maps; motion, the new story's animations, one request at a time from deck; studio, ports of earlier pieces rebuilt on this site's slide engine, working on an iPad. Each card with one rule from its page: the storyteller's "Nothing goes into the talk until the editor has seen it."

`%% record: talk repository at 298be4e: team/storyteller/ROLE.md team/motion/ROLE.md team/studio/ROLE.md and their policy.json`

## Security: planned, and never staffed

**Figure:** security's role page, drawn as a card with nothing on it but its title and its status: proposed.

**Narrator.** The conductor wrote security's page in the first hour. Its title says what it was for: checks first and last in every run; reviews of the pinned tools and of each new key. Its status, at the end of the day, still says proposed. No session ever held it. You will see in part 4 what that cost, and what stood in for it.

`%% record: talk repository at 298be4e: team/security/ROLE.md team/security/policy.json (status: proposed) timeline/interviews/security.md`
Band: *Security's page as it stood at the end of the day.*

## What a scope is, and what it is not

**Narrator.** Early in the evening, studio put a line on a slide, quoting the comment in the team's own scope check, and this whole chapter turns on it:

> "A scope is a setting, not a boundary: the agent can edit its own policy.json. It catches mistakes, not a steered agent." *(record)*

**Narrator.** A scope is a list in a file. A check reads the list and flags any change outside it. That catches an agent that wanders by mistake, and on the day it caught some. It does not stop an agent that has been talked into doing something else, because the agent has the same hands either way. Dev's page said the same thing in the first hours, about its own check.

**Studio** *(firm, as it says it)*: So you write the scope, and you check it, and you never confuse the check with a wall.

**Narrator.** Hold on to that. It is the question part 4 asks, at full size: if every member of the team is an insider, what actually contains it?

**Figure:** the nine role cards at their full size (the designer's scorecards, LAB 27), and a tenth, empty.

`%% record: timeline/quotes.md (the slide's line at 18:11, 95b09d9, quoting admin/build/agents.py; studio's debrief abp-prose-enforcement) talk repository at 298be4e: team/dev/ROLE.md ("The gap, and what stands in it")`
Band: *Dramatised (studio's line). The quoted line is the slide's own, from 18:11; dev's page made the same point in the first hours.*

## Do this now

*Write a second page of rules for a second agent, with a different thing it may change. Then write, under each "must not", what actually stands in the way: an expectation, a check, or a lock. Be honest about which.*

---

## Where this came from

The talk's repository at the end of the day: each member's page of rules and policy, and security's, still proposed. The librarian's study of the members' pages. The historian's quotes, for the slide's line on scopes, and its account of the empty chair. The storyteller's outline for this chapter.

`%% record: talk repository at 298be4e: team/*/ROLE.md team/*/policy.json; index/talk-site/members.md; timeline/quotes.md; timeline/interviews/security.md; chapter-plan/edition-70-outline.md part 2 chapter 4`
