# Source map: the talk's repository at v0.2.0

Repository: SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider, main at `298be4e` (site v0.2.0, merged from dev 23:19 on 29 October 2026, pull request #1, the repository's first). About 1,260 files outside `src/`; `team/` is 61 MB, `evidence/` 14 MB.

## The numbers (to be re-checked by the researcher)

- First commit 00:16:23, 29 October. Talk 19:00. Merge to main 23:19. 816 commits, 358 of them after 15:00.
- Authors: Claude 603, GitHub Actions 211 (one per site release), Dinis Cruz 2.
- Site versions: v0.1.0 to v0.1.209 on dev, then v0.2.0 on main: 211 releases.
- Members: conductor, deck, researcher, ruv-sgit, designer, dev, storyteller (joined ~14:12 UTC), motion and studio (joined 15:30 to 16:00 at the editor's word); security proposed by the conductor, never staffed.
- The talk: 58 beats in three parts (from 17 at 13:00), `src/static/talk/talk.json`. Player 977 lines (from 236), `src/static/talk/player.html`.
- The hold: 18:44, "the editor's usage limit is at 95%, pause all actions".

## Where things are

| what | where |
|---|---|
| the original brief, never edited; corrections kept apart | `BRIEF.md`, `BRIEF-CORRECTIONS.md` |
| what actually exists, kept by whoever ships | `REALITY.md` |
| how an agent starts a wake, the banner, checks | `admin/tools/start.py`, `banner.py`, `wake.py`, `vault_check.py`, `vault_handover.py` |
| the pinned key tool and its hash | `admin/tools/pki-agent.mjs`, `.sha256`, `pki-agent.README.md` |
| the team's numbers, moments, night log | `admin/tools/team_numbers.py`, `moments.py`, `night_log.py` |
| each member: role, policy, status, key, sessions | `team/<member>/ROLE.md`, `policy.json`, `status.json`, `key.json`, `key.png`, `sessions/` |
| the conductor's schedule, pace, hold, onboarding, wake procedure | `team/conductor/schedule.json`, `pace.json`, `HOLD.md`, `ONBOARDING.md`, `WAKE.md` |
| wakes, debriefs, reviews, briefs sent | `team/conductor/wakes/`, `debriefs/`, `reviews/`, `briefs/`; same under other members |
| the overnight record | `team/conductor/night/` |
| the editor's decisions, signed or open | `evidence/proposals/editor-decisions-deck.md` and the decisions page |
| claims, sources, incidents, ideas | `evidence/claims/`, `sources/`, `incidents/`, `ideas/` |
| the story work: tree, challenge, coverage, sequence, Wardley maps | `team/storyteller/story/`, `team/storyteller/maps/`, `evidence/story/` |
| the method the team said it followed | `evidence/METHOD.md`, `evidence/BEFORE-TONIGHT.md` |
| the talk: beats, slides, engine, player | `src/static/talk/talk.json`, `slides/`, `engine/`, `player.html` |
| the studio pieces and the SHarness capture | `src/pages/studio/`, `src/static/studio/data/harness.json` |
| articles | `content/articles/` |
| the site build | `admin/build/build.py` |

## Not in the repository (the editor holds these)

- The editor's voice memos (the narrative memo of the morning, the 13:50 feedback round, the 15:00 decisions round).
- The claude.ai session transcripts of 29 October, in which the three brief zips were written (`editor-briefs-2026-10-29.zip`, `-v2.zip`).
- Whatever was said on stage. If the talk was recorded, the recording is the primary source for part three (the live demos).

## Earlier work the book can reuse

- https://ruv.sgit.ai, the 15 October 2026 talk, whose player and pieces this team ported.
- https://gen-z-developers.sgit.ai, the Gen ZX Founders book: its roles (editor, reviewer, publisher, librarian, journalist, illustrator), its "every chapter ends with where it came from" rule, its synthetic readers, its paper-review loop, its covers drawn by code, and its Leanpub and Amazon listing work. Repository SGit-AI__Website__Gen-Z-Developers.
- https://newsroom.sgit.ai, the editor's article workflow.
