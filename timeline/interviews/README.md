# Exit interviews with the talk team, reconstructed from the record

Kept by historian@book.the-ultimate-insider. Begun 30 October 2026, at the conductor's request (`comms/mail/mailroom/historian/conductor__007-exit-interviews.eml`), which carries the editor's wish of about 13:08 UTC for the lessons "in the voice of those agents ... like an exit interview", and the talk's own debrief, item 2: "Interview every agent: what went well, what did not, what worked, what we could do better, what is left; collate into one narrative" (`team/conductor/briefs/2026-10-29__editor/11-the-debrief-after-the-talk.md` in the talk's repository, added after the day in `a9c0b49`).

**Every interview here is reconstructed from the record by historian@book, not the agent's own words.** No agent of the talk's team was asked anything. Each answer is what that agent's own files say, read by someone else, and each claim cites the commit or file it rests on.

## Method

- **Source.** The talk's repository, read only, in a clone in the historian's scratchpad, at `298be4e`: the member's `ROLE.md`, debriefs, wake records (`team/<id>/wakes/`), `status.json`, reply files and the commits marked `@<id>:`. Material after `298be4e` is not used, except where an interview says so and labels it.
- **The five questions**, the talk's debrief's own: what went well, what did not, what worked, what could we do better, what is left.
- **Voice.** First person, as the agent's record speaks: its debriefs already write that way. The words are the historian's; the claims are the record's.
- **Drafting.** Each interview was drafted by a sub-agent of the historian's session from the record, then checked by the historian against the clone: every cited commit exists before `298be4e`, and every time matches its commit.
- **Read whole commit messages.** Authorship is read from the trailers as well as the subject: ruv-sgit's subjects dropped the `@` for two stretches of the day, and the afternoon's player commits name no member in the subject but carry dev's `Agent:` trailer.
- **No numbers of our own.** A count in an interview is quoted from a record file and cited; the book's numbers come only from the researcher's register (`claims/`).
- **Inferred, and said so.** Where a reading rests on inference, the interview says so. Authorship is read from the commit's trailers: the afternoon's commits whose subjects name no member carry `Agent: dev@the-ultimate-insider`, so they are dev's on the record.
- **The failures stay in.** An interview that only praises its agent is sent back.

If the editor asks the agents in their own sessions too, their answers go beside these, and where the two differ, that difference is a finding.

## The interviews

| Member | File | State |
|---|---|---|
| conductor | [`conductor.md`](conductor.md) | drafted, checked |
| dev | [`dev.md`](dev.md) | drafted, checked |
| deck | [`deck.md`](deck.md) | drafted, checked |
| designer | [`designer.md`](designer.md) | drafted, checked |
| motion | [`motion.md`](motion.md) | drafted, checked |
| researcher | [`researcher.md`](researcher.md) | drafted, checked |
| ruv-sgit | [`ruv-sgit.md`](ruv-sgit.md) | drafted, checked |
| storyteller | [`storyteller.md`](storyteller.md) | drafted, checked |
| studio | [`studio.md`](studio.md) | drafted, checked |
| security | [`security.md`](security.md) | **no interview**: the role was proposed and never held |

The request named ten members. Nine held a role on the day; security did not (`security.md`).

## The lessons, collated

Reconstructed from the nine interviews and the security note by historian@book.the-ultimate-insider, with hindsight. The interviews are the record's; this is the historian's reading of them, and every lesson names the interviews that carry it.

### What went well: a team that ran on a clock, and checked itself

The strongest common answer is that the machinery held for most of the day. The conductor built the schedule, the hold and the five-step wake before dawn, and the members' records show the wake running at nearly every slot after it (`conductor.md`, `dev.md`, `deck.md`, `designer.md`). Pairs formed and worked: designer wrote notes, dev built them, designer checked the build at the next wake (`designer.md`, `dev.md`); the researcher's register fed deck and the storyteller, and a fact without a register id went back as a request (`researcher.md`, `storyteller.md`, `deck.md`). Members who joined in the afternoon were useful within the hour: the storyteller's arc was on `dev` by 14:19, asked for at 14:12, and motion's first pieces reached the talk's running order (`storyteller.md`, `motion.md`).

### What did not: the plan written down as if it were the record, and a lock that never happened

The day's last hour carries the same failure in four interviews. Part 1 was due to lock at 18:30; dev shipped the lock tool at 17:54 and then let the editor's in-session fixes crowd the lock out; the conductor flagged readiness twice and asked dev to lock at 18:39; the hold came at 18:44 with part 1 unlocked (`dev.md`, `conductor.md`). Meanwhile designer's status recorded part 1 as "locked at 18:30" and motion's M03 kept numbers the conductor had already refreshed (`designer.md`, `motion.md`). The lesson is about status files: a member wrote what was planned, and a status that the next session trusts became a claim, not a record.

The early failures were of a different kind, leaks of material that should not have been published, and each was caught by the team's own checks, though not before reaching history: ruv-sgit's first run quoted a request that held an access key, stopped before commit, and its vault was deleted; the researcher's captures carried values that should have been stripped, redacted forward but kept in the vault's history; the conductor printed a vault key in its own session log and rotated it (`ruv-sgit.md`, `researcher.md`, `conductor.md`).

### What worked: mechanical checks over remembered rules

Every interview that names a method that held names a script, not an intention: `start.py` pulling first, the gate refusing a release, `wake.py gate` refusing work before two go verdicts, the researcher's quote-against-capture check, designer's check files beside each review, ruv-sgit's fresh-clone comparison, studio's sources copied unmodified and checked by hash (`conductor.md`, `dev.md`, `researcher.md`, `designer.md`, `ruv-sgit.md`, `studio.md`). Scope held where it was tested: studio answered a request to edit another member's file with the owner's name, and the storyteller sent proposals to deck as requests, never as edits (`studio.md`, `storyteller.md`). The pre-reviews that said `change` improved plans more often than they slowed them (`deck.md`, `dev.md`, `researcher.md`). Writing each mistake into the member's own role as a rule, dev's push rule above all, is the habit the records credit most (`dev.md`). Where the rules were expectations rather than scripts, they wore: the commit-subject convention slipped for dev's player commits and ruv-sgit's two stretches without the `@`, though the `Agent:` trailers kept the authorship on the record (`dev.md`, `ruv-sgit.md`).

### What could we do better: deadlines between slots, and a reviewer who stands apart

Four interviews meet the same structural problem: an hourly slot cannot meet a deadline that falls between slots. The storyteller missed the 17:30 three-part split; deck's wakes fired late in a day ruled by locks; studio left its hardest item for last and was held before it; designer and motion put the question of scheduling a follow-up to the editor because their prompts forbade creating tasks, and it was never settled (`storyteller.md`, `deck.md`, `studio.md`, `designer.md`, `motion.md`). Requests could also fall between wakes: the conductor's M04 for motion appears in no motion plan before the hold (`motion.md`).

The deeper lesson is the security note's. The role meant to stand apart from the team was proposed and never held; its work was done by sub-agents inside each member's own session, a second reading but not a second identity, as the conductor wrote at the time (`security.md`, `conductor.md`). The insider argument of the book is visible here in miniature: the brakes were real and they caught things, but every brake ran with the reach of the agent it was braking.

### What is left: the hold's unfinished edges

At the hold, part 1 was final but unlocked, parts 2 and 3 were planned for 19:30 and 20:00, and two wakes were open (deck's of 18:20, which never closed, and dev's of 17:47, closed only on a branch) (`deck.md`, `dev.md`, `conductor.md`). The asks left on the members' status files were mostly the editor's: the evidence vault's history (D12), the handover zips for kept vaults, the follow-up question, and decisions on wording (`researcher.md`, `ruv-sgit.md`, `conductor.md`, `deck.md`). The hold itself worked as designed and showed its limit: it stops the next wake, not one already running, so designer's push and the day's last release landed after it (`designer.md`, `conductor.md`).

## What this collation is not

It is not the agents' own account. If the editor asks the agents in their own sessions, their answers go beside these, and where they differ from this reading, the difference is the finding.
