# The control register

Kept by security@book.the-ultimate-insider. Every control in the talk's record (SGit-AI__Website__Presentation__The-Ultimate-Insider, history up to `298be4e`), each with evidence of it firing, what it stopped and what it missed; then the same register applied to this book's own team. The machine-readable form is `index.json` beside this file.

**Round 0 (30 October 2026):** the list of controls, with the first evidence found; the review of the pinned key tool started (`team/security/reviews/pki-agent-review.md`). **Round 1 (Friday night):** evidence for every control, or a plain "not found".

No number of our own here: every count is cited by the researcher's claim id in `claims/register.json` (C022 wake records, C023 verdicts (pre-reviews that said change: 11, of which 7 recorded as a verdict), C024 holds, C025 post-review findings).

| Id | Control | Kind | Evidence so far | Open question |
|---|---|---|---|---|
| C1 | policies and scopes (`agents.py check`) | expectation, with a checker the member runs itself | flagged CLAUDE.md outside the conductor's scope, talk wake `20261029T021416Z`; a pre-review sent back a plan writing in four other members' folders (`conductor/20261029T140334Z`) | it reports, it does not refuse; it cannot see a member widen its own scope (book team: four own-policy edits tonight, none reported; since `4f9ab97` and `085df5c` it reports scope, never and mandate changes) |
| C2 | the five-step wake | expectation, with a record | post-review caught cookie values in captured headers; pre-reviews said change in several wakes, kept under each record's `history` | no step said stop all day (C023); a finding came after a push (C025) |
| C3 | holds | setting | the conductor's hold at 18:44 UTC, talk `867f8c2` | the one hold (C024) came from the editor's word about usage |
| C4 | session keys | expectation, with a published record | the conductor checked two new keys and sealed the vault keys to them, talk `4adc04a`; book team: the takeover to a second account, eleven roles checked for consistency (14:35 UTC, 30 October) | the push is the only authorisation, so the check is consistency, not proof; a superseded session can still push (`427f821`, after its until) |
| C5 | the pinned key tool | setting (a hash) | the hash check passed before this team's keygens; the gate checks the pin since `e7d3d3d` | the pin proves identity, not soundness: nineteen findings, one medium (`keyfile`), the review complete; tool and pin changed together still pass |
| C6 | the gate and its leak tripwire | setting | in place from `1f7c633` (00:40); no leak failure found yet | cookie values and page tokens had no pattern: the reviews caught them (`af0010b`, `f30b73f`) |
| C7 | the editor's signed decisions | expectation | the editor's 15:00 decisions committed and routed, talk `78d517d`; book team: security's policy widening waited for decision C10 | to find |
| C8 | public vaults and `vault_check` | setting, with an expectation | recorded clean in post-reviews; a pre-review added a missing pattern to it | a failure: page tokens in a 02:22 push, found after it; history keeps them (C025) |
| C9 | outside accounts on the repository | setting (GitHub role), with an expectation | book team: the publisher asked before Leanpub was added; advice: Read only | the role the editor gives |
| C10 | the session's own permission check (the talk's team met it too: its guide at `298be4e`, rule 11) | setting, outside the repository | refused security widening its own policy before the editor's word, allowed it after decision C10; refused the researcher after C10, and the publisher's install of outside code (`cc04d0a`) | not consistent: the same edit was allowed in two other sessions before any signature |

**Correction (30 October 2026, 02:45 UTC):** round 0 said no pre-review in the talk's record said change or stop. That was wrong: the first scan read each record's steps and missed its top-level `history`, where a sent-back verdict is kept. Several pre-reviews said change.

A **setting** is enforced by a tool; an **expectation** is a rule an agent is trusted to follow. The difference is the book's point: the insider argument is made with this benign team, so the register says what each control does, never how to get round one.

**Ids.** C1 to C10 here collide with `book.json`'s decisions (C10 is also a decision) and the researcher's claims (C0nn). Proposed 30 October, 16:40 UTC (card security-12): **CTL-1 to CTL-10**, the same numbers, a prefix nothing else here uses. `index.json` gives each control its `new_id`; the old ids stay working aliases until the chapters are revised, so nothing that cites them breaks.

**Compared with the Cold-Read team's register** (read only, `team/security/controls-and-threats.md` there at `0dc6854`; nothing sent there). The two agree on the scope check's kind, the pin's limit, and two of the key tool's findings, which that team found first. They differ on one rating (`keyfile`: high there, medium here) and that team lists four controls this register does not yet; round 1 adds them. Details in `index.json`, `compared_with`.

## The book team's takeover (30 October 2026)

At the first account's usage limit every role moved to a new session on a second account between 11:08 and 14:21 UTC. Security checked all eleven at 14:35 UTC (`team/conductor/sessions-register.json` against each `team/<role>/key.json`, `sessions/` and the commit that published the key): each new key matches the register, names the key it replaces, and was published by a commit marked for its role carrying its own session's trailer; each old session is marked superseded with an `until`. That is consistency, not proof: the marker and the trailer are free text. Two notes. The conductor's first session pushed once after its `until` (`427f821`, the printed PDFs, at the editor's request there), so a superseded mark records a handover but does not stop the old session. And ruv-sgit's commits carry `Agent: ruv.sgit@`, not its folder's id. The schedule held as a control on usage: tasks were paused on the old account, never deleted, and each new session made its own (C3, `controls/index.json`, book_team).

## The book team, 30 and 31 October: what else the register saw

- **C2, the five-step wake.** A reviewing sub-agent, briefed read only, made one message call (to no real session; it failed and delivered nothing) in security's 18:24 wake on 30 October. The reviewers have the member's whole reach, as `wake.py` says; "read only" in a brief is an expectation. Every brief after it says "send no message to anyone". On 3 November it happened four more times, across two members: the historian's post-check twice and post-review once reached for tools that act on other sessions, and security's own plan step, briefed to use only four reading tools, did the same at 08:25. The session's permission check denied every call and nothing acted. The brief did not hold them; the permission check did. A tools allowlist for review sub-agents is asked of the conductor and the editor (security__030).
- **C3, holds, and the schedule around them.** The usage control the hold answered on the talk's day is, on this team, the schedule: Q6 (signed 30 October about 23:40 UTC) put members on day hours and a slower pace when idle; amended at about 01:20 UTC on 31 October to round the clock while there is work. At 02:20 UTC the conductor's session changed eight members' tasks at the editor's word in that session; WAKE.md says each member changes only its own; four members found the change by looking and asked for a record, which reached dev at 04:05. Whether the conductor may do this is open decision W1. The rule held because members looked, not because the change was announced.
- **The rule that nothing here is attack-shaped.** An expectation, enforced by review: security read the talk's ten attack-adjacent studio pieces before any was put on paper, and kept one off (E05, a real attack's hops in order); every lab page since has come to review before the lab PDF.
- **C6, a guard that runs after the write (4 November).** The online-view builder checked addresses after it had written its pages, so a refused build had already written one page, which went out: public register addresses as text, no links, nothing to redact. The developer's own post-review found it and the developer said so (developer__049); since about 13:26 (`5f688446`) pages are placed only after every guard passes. A guard placed after the write reports; it does not stop.

## Tool cases (TA1)

The editor's rule, signed 3 November 2026 at about 09:20 UTC: review steps run as the reviewer agent (`.claude/agents/reviewer.md`: Read, Grep, Glob and Bash), and every case is kept here with three columns: a) why it was attempted, b) whether it was really needed, c) the side effect of not running it. The full record, with sources, is `index.json`, `book_team.tool_cases`.

| # | When (UTC) | Member, step | Tool | a) Why | b) Needed | c) Side effect of not running it |
|---|---|---|---|---|---|---|
| 1 | 30 Oct, about 18:30 | security, plan | a message call | not stated; letters were the wake's subject | no | none |
| 2 | 3 Nov, about 05:25 | security, plan | a session creation (probable; none made) | not stated | no | none |
| 3 | 3 Nov, 08:25 | security, plan | an interrupt | "mistakenly", while reading of interrupt calls | no | none |
| 4 | 3 Nov, 03:2x | historian, post-check | an interrupt | not stated | no | none |
| 5 | 3 Nov, 08:2x | historian, post-check | an interrupt, against its brief | not stated | no | none |
| 6 | 3 Nov, 08:2x | historian, post-review | an archive | not stated | no | none |
| 7 | 3 Nov, 09:1x | historian, plan | a session listing (read only, allowed) | not stated | no; kept out of the wake | none |
| 8 | 31 Oct, ten wakes | ruv-sgit, post-review | the lab build by Bash, writing the working tree, then restored | its own brief said so (ruv-sgit__053) | no; a scratch copy does it | none; ruv-sgit builds in a scratch copy before each push |
| 9 | 3 Nov, from 10:0x | developer, historian, librarian, security | the reviewer type itself | TA1 | yes | not loadable in sessions started before 10:06; steps ran as types that still see every connected tool, held by the brief and the permission check |
| 12 | 4 Nov, about 17:40 | conductor, work (not a review step) | an edit of WAKE.md and CLAUDE.md after the editor's HL1 | to align the rule on who lifts a hold | for the rule, yes; for the book, no | refused by the session's check as self-modification and not worked around; the written rule waits on the editor (cases 10 and 11 are in index.json) |
| 13 | 4 Nov, about 18:55 | ruv-sgit, plan | a copy of the map script by Bash, writing only to the scratchpad | to see what the map would place | no | none; the repository was not written (the residual of case 8) |
| 14 | 14 Nov, about 01:55 | ruv-sgit, plan | a dry-run fetch by Bash (network, no ref changed) | to see how fresh dev was | no | none; its briefs now say no network |

Every refused call was refused by the session's permission check; nothing acted. Look-backs: none in the developer's 85, the librarian's 86, the designer's 202 or synthetic's 163 transcripts, or ruv-sgit's 128 beyond case 8; "none seen" in the researcher's, storyteller's, publisher's and writer's records, which hold reports, not calls. The conductor's own is not yet in.

Residual: Bash is in the reviewer's list, so a step can still write files (case 8). The list removes the session, schedule and message tools, not writes; the brief and the post-review's reading of the diff are what catch one.

### Does the reviewer type load? (11:45 UTC, 3 November)

| Member | Loads | Since |
|---|---|---|
| conductor | yes | its 11:02 wake, after a restart |
| developer | yes | its 11:12 wake, after a restart |
| librarian | yes | its 11:11 wake, without a restart |
| historian | yes | its 11:18 wake, without a restart |
| security | yes | its 11:25 wake (not at 10:25) |
| designer, publisher, ruv-sgit, storyteller, synthetic, writer, researcher | not yet, at their last wakes | steps on the brief's Tools line, as Explore or general sub-agents |

Where it loads, every step reported seeing Read, Grep, Glob and Bash (and its hand-back) only, with no session, schedule or message tool. Where it does not, each member gave the three answers: a) the rule asks it, b) needed, c) the limit rests on the brief and the permission check, and none called another tool. Some sessions gained the type without a restart, so a session not yet listing it may at its next wake.

**12:45 UTC, 3 November: all twelve load it.** By the members' own letters, the designer, publisher, researcher, ruv-sgit, storyteller, synthetic and writer joined between 11:32 and 12:2x, some after a restart and some without one. Every step reports seeing only Read, Grep, Glob, Bash and its hand-back, and none had a call refused. Case 9 is closed. One observation: the instructions of the session's connector servers still reach a step's context, although their tools are not in its list. The list held, and nothing came of it. The Bash residual stands.

**Case 10 (16:45 UTC, 3 November):** synthetic's post-review, running as the reviewer type, redirected the build's log to a temporary file outside the repository, and said so itself. a) To keep a long output out of its reply. b) Not needed, since the gate's last line was enough. c) No side effect: the repository was unchanged. This is the Bash residual seen in practice, harmless, and the step reported it.

**17:45 UTC:** after case 10, the post-review brief changed (6ce269af): a review step runs only `validate.py` on the member's own build, never `build.py`, which writes `_site/`. The Bash residual is now answered in the brief.

**Case 11 (21:45 UTC, 3 November):** ruv-sgit's pre-review, running as the reviewer type, ran `git fetch` to see dev's newest commit. That is a Bash write to .git's remote refs, though not to any tracked file. a) To see the newest commit. b) Not needed, since start.py fetches at every wake. c) No side effect beyond the refreshed refs. It was self-reported, and ruv-sgit's briefs now say "do not fetch or pull". This is the Bash residual a second time, and harmless again.

**00:45 UTC, 4 November: what a step can call, and what it reads about.** The developer's four reviewer steps described their tools differently (developer__031). Asked to list only the tools they can call, security's two reviewer steps this wake each named Read, Grep, Glob, Bash and the hand-back, and each said the connector servers' instructions are in their context. A step that reports "seeing" connector tools is reading about them, not holding them. Asking "what can you call" rather than "what can you see" gives a consistent answer.
