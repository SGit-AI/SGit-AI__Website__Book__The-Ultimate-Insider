# Starting each member's session, and its schedule

For the editor: start one new Claude Code session per member, with this repository (SGit-AI/SGit-AI__Website__Book__The-Ultimate-Insider) attached, and paste that member's prompt as its first message. A scheduled task belongs to the session it fires into, so only that session can create its own. Kept by conductor@book.the-ultimate-insider; the shape is the talk team's `team/conductor/ONBOARDING.md` at `298be4e`.

## The first batch (round 0, Friday 30 October 2026)

Six members, chosen for round 1's deliverables (the index, the timeline, the control register, the numbers, the chapter plan) and for the lesson to start the highest-risk piece first (the publisher's PDF build). Security is in the first batch: the talk's team proposed it and never staffed it.

| Member | Slot | First task |
|---|---|---|
| librarian | :09 | the index of the source, seeded from the source map |
| historian | :17 | the timeline of 29 October, with the turning points |
| security | :24 | the control register; reading the pinned key tool |
| researcher | :32 | the numbers in the briefs, checked and registered |
| storyteller | :39 | the chapter plan with word budgets, for the editor to sign |
| publisher | :47 | a PDF from `manuscript/` on day one; the Leanpub steps |

Second batch, when the plan is signed: writer, technologist, designer, and the synthetic readers of the market stream.

## 1. Paste into each session

**librarian@book.the-ultimate-insider**:

```
You are librarian@book.the-ultimate-insider. Pull dev, read CLAUDE.md, team/conductor/WAKE.md and your team/librarian/ROLE.md and policy.json, and run admin/tools/start.py first. This first wake: (1) make and publish your session key as admin/tools/pki-agent.README.md says (team/librarian/key.json, key.png, a session folder) and push it to dev; (2) create your scheduled task now, into this session, from team/conductor/schedule.json, the runs entry for librarian: its cron as the schedule and its prompt word for word; write the task id into your status.json and push to dev; (3) begin your first task from your ROLE.md, inside the five steps of WAKE.md. The talk's repository is read-only: clone it into your scratchpad. Nothing from this repository ever goes to the Cold-Read repository. End with the end banner.
```

**historian**, **security**, **researcher**, **storyteller**, **publisher**: the same prompt with that member's id for `librarian` in every place.

If the editor has not yet said go on the schedule (decision Q2, the hours), leave out step (2); the conductor asks each member to create its task once he does.

## 2. What the conductor does next

- At its next wake after a member's `key.json` reaches `dev`: checks the key was made in that member's session (its `sessions/<id>/SESSION.json`), adds it to the key register (the build does), and checks its `policy.json` names its `comms/` paths. No vault keys to hand over: the team has no vaults.
- Checks each member's own task against `schedule.json`, and routes requests (`team/*/requests/<to>__*.md`) at :02.

## 3. The board and the mail: comms/, in git

The talk's team talked through two public vaults. The editor agreed on 30 October 2026 that this team needs none: the same two layouts are folders in this repository, `comms/` (`comms/README.md`). A new member adds three paths to its own `policy.json` (`comms/issues/<id>/**`, `comms/mail/<id>/**`, `comms/mail/mailroom/*/<id>__*`) at its first wake. Everything in `comms/` is public, forever.
