# The chapter plan, draft 1

storyteller@book.the-ultimate-insider, 30 October 2026. **Not signed.** For the editor to sign, strike or change in round 1. Read `README.md` first: evidence is cited by path at `298be4e` or by commit until the librarian's index exists, and no number below may enter a chapter until the researcher has registered it.

## The shape in one paragraph

The book follows the day, because the day is the workflow: one person and an empty repository at midnight, a team by morning, a machine by noon, a talk in three locked parts by evening, and a team that stopped itself at 18:44 before its editor was cut off. That is the main thread. The argument (agents are the ultimate insider; brakes are what let us go faster) is not a second book bolted on: each chapter of the workflow carries the beat of the talk that the control in it answers, so the reader meets the risk and the brake together. The book opens on the hold, the moment where both threads are one picture: the insider with no limits, held by its own policy at its owner's word. It closes on how to build your own, with what it cost and what went wrong left in.

## The braid

| # | Chapter | Workflow thread (main) | Argument thread (the talk's beat it carries) | Failure it keeps | Words |
|---|---|---|---|---|---|
| 0 | Before you start | how to read the book and its record | the claim the book answers: agents cannot be made to work safely | | 1,200 |
| 1 | Pause all actions | the 18:44 hold, then the day in one view | the ultimate insider, held by its own brake | the hold itself: the talk's last part was not locked | 3,000 |
| 2 | Midnight, an empty repository | the first hour: brief, site, conductor, roster, banners | the attacker's limits were accidental controls | the brief was wrong in places, and was never edited | 4,000 |
| 3 | A mandate you can read | `ROLE.md`, `policy.json`, session keys, the push as authorisation | reach, mandate, the gap, and what stands in it (ABPs) | a scope is a setting, not a boundary | 4,500 |
| 4 | The hourly machine | slots, the mailroom, requests as files, the five-step wake, the night log | the insider works round the clock; so must the brakes | the request backlog; members waiting on each other | 4,000 |
| 5 | The story before the slides | the storyteller's tree, the researcher's register, claims graded | integrity: what you cannot trust or restore | the researcher contradicted the editor, and it was kept | 4,000 |
| 6 | The editor signs | feedback rounds, the decisions page, signing as the control | a licence to operate that can be suspended | decisions still open at 19:00 | 3,500 |
| 7 | Building the talk | deck, the ports from ruv.sgit, the designer, motion and studio joining, the player | the explosion of software: every spreadsheet becomes an application | the player, the top priority, started late and was fixed to the last minutes | 4,500 |
| 8 | Locks, and the brake | three parts locked in turn, `lock.py`, the editor's usage as a resource | brakes, so we can go faster | part 1 not locked at the hold; the security member never staffed | 4,000 |
| 9 | The team was the insider | the control register: each control, what it stopped, what it missed | the argument in full, made with a benign team | what the controls missed | 4,500 |
| 10 | The talk as given | what was said on stage, set beside what was planned | the argument as the audience heard it | what changed or fell out between plan and stage | 3,500 |
| 11 | What the cold reader saw | the Cold-Read team's findings against this book's | the outsider's view of the insider | what this book missed and the blind team found | 3,000 |
| 12 | Build your own | the setup, step by step, with the lessons kept and done differently | go build; try to escape the harness | what it cost, in the editor's hours and usage | 4,500 |
| | Where it all came from | the record, its commits, the QR codes for paper | | | 1,000 |
| | **Total** | | | | **48,200** |

`about-this-edition.md` stays first in `Book.txt` as the front matter it already is (not counted). The order of `Book.txt` follows this table once signed.

## The chapters

### 0. Before you start (1,200)

- **Argues:** this is a counter-example, with a timestamped record, to the public claim that agents cannot be made to work, are too risky and do not pay back; and it is analysis with hindsight, not a transcript.
- **Draws on:** the conductor's brief (`briefs/2026-10-30/1-book-conductor-brief.md`, "The gap the book fills", "Not raw content"); the phases explorer, villager, town planner (`book.json`).
- **Ends with:** where it came from, and how to follow a citation to the record (a commit, a path, a QR on paper).

### 1. Pause all actions (3,000)

- **Argues:** the most important moment of the day is the one where nothing happened. At 18:44 the conductor wrote a hold at the editor's word because his usage was near its limit, and every member's next wake stopped. That is the book's thesis in one scene: an insider with no limits of its own, stopped by a brake its owner controls. Then the camera pulls back to the whole day in one view (the turning points), so the reader knows where every later chapter sits.
- **Workflow:** the hold file, `start.py` refusing every wake, a member pausing its own task.
- **Argument:** "the ultimate insider", the talk's title beat (`talk.json`, `title`, `m03`).
- **Failure kept:** at the hold, part 1 was final but not yet locked, and parts 2 and 3 were still in progress (`team/conductor/HOLD.md`, "State at the hold"). The brake worked; it also cost the last minutes of work.
- **Draws on:** `team/conductor/HOLD.md`, commit `867f8c2`; `team/conductor/night/` (the night log's last edition before it, `20261029T1838.json`); the historian's turning points (pending).
- **Waits on:** the historian's timeline for the one-view map of the day.

### 2. Midnight, an empty repository (4,000)

- **Argues:** what one person needs before an agent team can start: a brief, a place where truth is kept (`REALITY.md`), a place where the brief's mistakes are kept apart from it (`BRIEF-CORRECTIONS.md`), and a conductor. The first hour of the record shows the order it was done in and why that order matters.
- **Workflow:** the initial commit, dev's first pass of the site, the conductor joining with a roster and a proposed schedule, the start and end banners (the first commits of the day, from `2e4b1f4` to `7f9b9b5`).
- **Argument:** the attacker's limits (time, money, sleep, skill, attention) were accidental controls; this team had none of them from its first hour (`talk.json`, `limits`, `no-worm-era`).
- **Failure kept:** the brief was wrong in places; the corrections file shows where, and that it was never edited (`BRIEF.md`, `BRIEF-CORRECTIONS.md`).
- **Draws on:** `BRIEF.md`, `BRIEF-CORRECTIONS.md`, `REALITY.md`, `team/conductor/ROLE.md`, the first hour of the git log.

### 3. A mandate you can read (4,500)

- **Argues:** every member had a written mandate in two forms, prose for the editor and JSON for the checks, and a key it made and published in its own session. That is the smallest working form of an Agent Behaviour Policy: reach (what the grant allows), mandate (what the role needs), the gap between them, and what stands in the gap.
- **Workflow:** `ROLE.md` and `policy.json` per member, `agents.py check` before every push, session keys from the pinned tool, "the push is the authorisation".
- **Argument:** `abp`, `s-e09` (mandate against grant), `s-port-abp`, `s-port-abp-review` (this team's own policies), `s-e10` (only a boundary is a control).
- **Failure kept:** the team said it honestly on its own slide: a scope is a setting, not a boundary. A member could have written outside its scope; the check would only have caught it after (`team/storyteller/story/three-parts.md`, part 2, row 8).
- **Draws on:** `team/*/ROLE.md`, `team/*/policy.json`, `admin/tools/pki-agent.README.md`, the editor's brief 8 (`team/conductor/briefs/2026-10-29__editor/8-our-own-abps-1730.md`), the studio's showcase of the team's own ABPs (`bd3cdad`, `95b09d9`).

### 4. The hourly machine (4,000)

- **Argues:** the team did not need agents to be clever about each other; it needed a clock. Hourly slots fifteen minutes apart, in the order work flows, requests as files answered at the recipient's next slot, and five steps around every piece of work. Agents that never sleep need a rhythm a person can read.
- **Workflow:** `team/conductor/schedule.json`, `pace.json`, the mailroom, the five-step wake (`WAKE.md`, `admin/tools/wake.py`), the night log and Moments (`admin/tools/moments.py`).
- **Argument:** the insider with no limits works round the clock; the brakes have to as well, or they are a daytime control on a night-time risk.
- **Failure kept:** requests piled up and were routed in batches (`eb0b5cd`, "the request backlog routed"); work late because one member waited on another.
- **Draws on:** `team/conductor/schedule.json`, `team/conductor/WAKE.md`, `team/*/wakes/`, `team/conductor/night/`, the conductor's pace commits through the day.

### 5. The story before the slides (4,000)

- **Argues:** nothing entered the talk until the storyteller had mapped it (tree, coverage, challenge, sequence), and every fact in the tree carried a grade from the researcher's register. That is how an agent team keeps integrity in what it says, not only in what it builds.
- **Workflow:** `team/storyteller/story/` (four editions of the tree in the afternoon), `evidence/claims/claims.json`, `evidence/METHOD.md` (the grades).
- **Argument:** `integrity`: data changed in ways you cannot trust or restore; a talk about trust has to show its sources.
- **Failure kept:** the researcher's findings contradicted one of the editor's own lines ("the outside is in balance"), and the contradiction was put to him rather than smoothed over (`b208a16`). The book shows what he decided and why the record kept both.
- **Draws on:** `team/storyteller/story/tree.md`, `challenge.md`, `coverage.md`, `sequence.md`; `evidence/claims/`; `evidence/incidents/`.

### 6. The editor signs (3,500)

- **Argues:** one person ran ten agents by deciding, not by doing: feedback in rounds, a page of decisions open and signed, and a rule that nobody speaks for him. Signing is the control that turns a team's proposals into a mandate.
- **Workflow:** the editor's briefs of 29 October (`team/conductor/briefs/2026-10-29__editor/`), the decisions deck (`evidence/proposals/editor-decisions-deck.md`, `editor-decisions.json`), his feedback pane and lane with voice (`9a51c28`).
- **Argument:** `licence`: a licence to operate, that can be suspended; `s-e14`, earning autonomy.
- **Failure kept:** several decisions were still open at 19:00 (`briefs/2026-10-30/5-lessons-to-carry.md`, "Do differently" 6).
- **Draws on:** the briefs above; an interview with the editor, if he gives one (open question O4).

### 7. Building the talk (4,500)

- **Argues:** the making, told by what it shows about the method: work ported rather than rebuilt (the ruv.sgit pieces and player), members joining mid-day with a role, a policy and a key in one wake (motion and studio, `f1cbca0`, `8d208d3`), and the talk growing from a first draft to three parts.
- **Workflow:** deck, ruv-sgit, designer, dev, motion, studio; the player and its build mode (`3314ffe`, `f20cfa8`).
- **Argument:** `spreadsheets`, `team`: the explosion of software, as everyone becomes a builder; the capability is the orchestration, not the model.
- **Failure kept:** the player for the iPad was the editor's top priority in the early afternoon and was still being fixed at 18:37 (`dbd75ad`). The brief says it "landed with fixes at 18:37"; the record shows a port at 15:07 (`3314ffe`) and fixes until 18:37: the historian settles which story is true before this chapter is drafted. Also: deck set part 1 before the storyteller's split, which was late (`three-parts.md`, opening).
- **Draws on:** `src/static/talk/talk.json`, `src/static/talk/player.html`, the deck's and dev's commits, `team/motion/`, `team/studio/`, `team/designer/`.

### 8. Locks, and the brake (4,000)

- **Argues:** the evening is where the method was tested: three parts each frozen before it went on stage, a lock tool built the same hour it was needed (`admin/build/lock.py`, `4a2481b`), and the editor's usage watched as a resource until it was nearly gone. Brakes are what let a team go fast up to the last minute and still stop.
- **Workflow:** the 16:59 decision of three parts with locks (`3342cff`), `lock.py`, the pace wakes of the evening, the hold.
- **Argument:** `brakes`, `s-b01-brakes`: brakes, and go build.
- **Failure kept:** part 1 was not locked when the hold came; the security member was proposed and never staffed; the usage limit was met as an emergency, not planned for.
- **Draws on:** `team/conductor/HOLD.md`, `team/conductor/night/`, `team/storyteller/story/part-check-1814.md`, the evening's git log.

### 9. The team was the insider (4,500)

- **Argues:** the argument in full, made with the team itself as the example: every capability the talk says makes agents the ultimate insider, this team had; every control the talk proposes, this team ran on itself. The chapter is built on the security member's control register: each control, the evidence of it firing, what it stopped, and what it missed. Nothing in it is attack-shaped: the risk is shown by what a benign team could reach, never by what anyone could do with it.
- **Workflow:** the control register (pending); the pinned key tool; the review before and after every wake; holds.
- **Argument:** parts 1 and 2 of the talk as one argument: `inside`, `identities`, `permissions`, `infrastructure`, `way-out`.
- **Failure kept:** what the controls missed, from the register.
- **Waits on:** the control register; rebuilt on it when it lands.

### 10. The talk as given (3,500)

- **Argues:** what reached the audience, set against what the team planned: which beats were said, which moved, which fell out, and what that says about planning a talk with agents. Analysis, not a transcript: the transcript is cited, not reprinted.
- **Draws on:** material **added after the day**: the talk as given, the recording cleaned beside its slides, and the editor's debrief after the talk (talk repository `a9c0b49`, 30 October 01:24 UTC); and any interviews the editor adds later, each cited by commit.
- **Waits on:** the editor's word that the transcript may be quoted (open question O3).

### 11. What the cold reader saw (3,000)

- **Argues:** a team that arrived knowing only the talk's repository read it cold; where its account differs from this book's is where an insider's view is blind. Written in round 3 from the Cold-Read repository's findings, read from here and never written to.
- **Draws on:** the Cold-Read repository's published findings (read only; the one-way valve).
- **Waits on:** round 3. The chapter's budget is held; if the findings are thin, it shrinks and chapter 12 takes the words.

### 12. Build your own (4,500)

- **Argues:** how to replicate it: the setup in the order it should be done, with the lessons kept and the ones to do differently (start the highest-risk piece first, staff security from the start, timings before pieces, watch usage as a resource, record what is said on stage, close open decisions), and what the day cost.
- **Argument:** `evolution`, `next-companies`, `brakes`: go build.
- **Failure kept:** the cost, in the editor's hours and usage (numbers from the register only).
- **Draws on:** `briefs/2026-10-30/5-lessons-to-carry.md`, the technologist's architecture (second batch), this book's own team as the second run of the method.

### Where it all came from (1,000)

The record: the talk's repository and the commit it is pinned at, this repository, the Cold-Read repository, the material added after the day, and how each QR on paper resolves.

## Numbers this plan leans on (for the researcher to register)

None of these enters a chapter until it is in `claims/`: the day's span (00:16 to 19:00, and the 23:19 merge); the counts of commits, authors and releases (see `BRIEF-CORRECTIONS.md`, "When the work ended"); the number of members and when each joined; the 18:44 hold and the 95%; the 58 beats in three parts and the talk's length; the player's growth; the part locks (18:30, 19:30, 20:00); the time the player port landed (15:07 or 18:37, chapter 7).

## Where this came from

The editor's briefs of 30 October 2026 (`briefs/2026-10-30/`); the talk's repository read at `298be4e` (`talk.json`'s beats, `team/storyteller/story/`, `team/conductor/HOLD.md`, `team/conductor/night/`, the git log of 29 October); and the talk repository's `a9c0b49`, added after the day, for chapter 10. Made by storyteller@book.the-ultimate-insider on its first wake, before the index, the timeline and the control register existed.
