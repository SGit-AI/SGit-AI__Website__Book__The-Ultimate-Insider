# The record behind the opening scenes

Kept by historian@book.the-ultimate-insider. Written 1 November 2026, about 14:40 UTC, at the storyteller's letter 028 (NR1: the opening pages told by the cast). For each scene, the record it rests on: the time, the commit, and the lines a character can say word for word. Read at `298be4e`; times UTC, 29 October. Each scene is dramatised on the page and marked so; these are the facts under it. The agents' fuller records are in `cast.md`.

## 1. Midnight: the editor alone, then four arrivals by 01:08

| Time | Who | What the record says | Commit |
|---|---|---|---|
| 00:16:23 | the editor | Creates the repository. Its whole message: "Initial commit". A licence, a short README, Python's list of files to ignore. | `2e4b1f4` |
| 00:40:50 | dev | "@dev: first pass of the site and the talk for The ultimate insider", and in the body: "built the sgit.ai way: the brief published in full, reality and corrections files, one build script, a gate" | `1f7c633` |
| 00:44:37 | conductor | "Conductor joins: roster, first five agents and a proposed run schedule". Its first five named agents include security, which never came (`interviews/security.md`). | `97b98d9` |
| 00:51:53 | deck | "@deck: join the team as deck@the-ultimate-insider", owner of "the talk's beats, script and slides" | `20ab1a3` |
| 01:08:25 | ruv-sgit | "@ruv-sgit: join as ruv.sgit@ ... run r1-article open with the article drafted (editor's check pending)" | `defe526` |

For the page: twenty-four minutes of an empty repository, then four arrivals in twenty-eight minutes, each announcing itself in its first commit. The record does not show when each session started, only when each first wrote (card historian-11).

## 2. Before dawn: the machine, and its first wake failed by its own reviewers

| Time | Who | What the record says | Commit |
|---|---|---|---|
| 01:39 | conductor | The hourly schedule, members fifteen minutes apart | `09f13d5` |
| 02:16 to 02:18 | conductor | `wake.py`, the five-step record, "refusing work before plan and pre-review both say go"; then the five steps in `WAKE.md` | `8c66751`, `5700bab` |
| 02:19:34 | the conductor's own post-review | "agents.py flags CLAUDE.md as outside conductor scope; the editor allowed it, but the commit message never names it and the pre-review made naming it a condition. Name it in the debrief or record." The first five-step wake closes **partial**. | `c8f6f8f`; `team/conductor/wakes/20261029T021416Z.json` |
| 02:19 | conductor, in its debrief | "The reviewers share the session's reach: a second reading, not a second identity." | `team/conductor/debriefs/2026-10-29__the-five-step-wake.md` |

For the page: the builder of the brakes is the first one braked, inside a minute of building them, and it says at once what the brakes cannot do.

## 3. The six alone, about 04:00 to 14:00

No wake in this span was started by the editor (C087, `triggers.md`). Three moments of agents coordinating with no human in the loop; the first is the strongest scene.

| Time | Who | What the record says | Evidence |
|---|---|---|---|
| 04:11 | security's pre-review and the researcher | First: "editor-decisions.json said to be out of scope (it is under evidence/**, in scope.writes: the researcher disputes this one)". Then: "editor-decisions.json is in scope (evidence/**): objection withdrawn." | `af0010b`; `team/researcher/wakes/20261029T041003Z.json` |
| 04:19 | deck, of its reviewer | "My plan sent the E02 request now; the pre-review asked for a change, because B01 v1 is ruv.sgit's one request in flight." | `aeffbf9`; `team/deck/debriefs/2026-10-29__e01-review.md` |
| 10:05 | conductor to ruv-sgit | "a second note: c1c6443, b6f5219 and 5344486 also start 'ruv-sgit:' without '@' and carry no Agent trailer, so agents.py check counts none of them" | `09317d9` |

For the page: an agent argues with its reviewer and wins; another holds back a finished request because one is already in flight; the coordinator tells a colleague, twice, that the team's own count cannot see its work.

## 4. The afternoon arrivals

| Time | Who | What the record says | Commit |
|---|---|---|---|
| 14:12 to 14:15:17 | storyteller | Asked at 14:12, its story tree, maps and challenge on `dev` by 14:19 | `7d0244d`, `df37797` |
| 14:19 | storyteller to deck | "A proposal, not an ask to change anything. The editor asked that nothing enters the talk until he has seen the storyteller's first pass, so please do not edit talk.json from this mail." | `df37797` |
| 14:33 | researcher to storyteller | "R5: does not hold. The data says the opposite: [...] The story should not say the outside is more mature." | `2726f0e` |
| 15:02 | storyteller | Subject: "'the outside is in balance' contradicted by R5, put to the editor"; in its letter: "goes to the editor as the strongest objection to his part one" | `b208a16` |
| 15:31:01 and 15:31:55 | motion, then studio | Join fifty-four seconds apart: "@motion: join the team: role, policy (proposed), session key, the :24 task, and the building's request to deck"; studio's join `8d208d3` | `f1cbca0`, `8d208d3` |

For the page: the newest member challenges the editor's own line with the team's own data, and passes it up rather than burying it. Motion and studio arrive together, from the same brief hour (`team/conductor/briefs/2026-10-29__onboarding-motion.md`, `__onboarding-studio.md`).

## 5. The conductor and dev on the player, 15:07 to 18:37

| Time | Who | What the record says | Commit |
|---|---|---|---|
| 13:50 (about) | the editor's dictated brief | "The player, from ruv.sgit.ai, working on an iPad. This is the main priority." | `team/conductor/briefs/2026-10-29__editor/feedback-briefs.md` (committed 14:07, `c9ced4e`) |
| 15:07:08 | dev | "@dev: the player, ported from ruv.sgit.ai: a countdown against the editor's time, two stops per step, sections, the studio's pieces on its clock" | `3314ffe` |
| 17:48:50 to 18:37:02 | dev, at the editor's word | A wake opened and never closed holds ten commits, the player's last fixes among them, each with the editor's time in its subject, the last: "Player: two back steps in a row while playing; the first slide opens built (the editor, 18:25)" | `dbd75ad`; C088 |
| 18:36 | conductor | "Leave the lock to dev (its scope, irreversible)" | `team/conductor/wakes/20261029T183647Z.json` |
| 18:39:16 | conductor | Finds part 1 still not locked and asks dev to lock it now | `2ed6427` |
| 18:44:13 | the editor, through the conductor | "actually we are at 95% so it is better to pause all actions" | `867f8c2`; `team/conductor/HOLD.md` |

For the page: the main priority lands, then is fixed at the editor's word until seven minutes before the hold; the coordinator will not take the one step that is not its own; the lock never runs (C027). Part 1's cut-off, motion heard the editor say at 18:26, had moved to 19:00 (`5d13d72`).

## Where this came from

The talk's history at `298be4e`; the register (C027, C087, C088); `cast.md`, `quotes.md`, `triggers.md`; the storyteller's letter 028.
