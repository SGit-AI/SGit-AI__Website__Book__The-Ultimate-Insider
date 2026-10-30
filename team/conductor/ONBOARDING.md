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

## 1b. Takeover: the second account (30 October 2026)

The first account ran out of usage; at the editor's word every member continues in a new session on the second account, which takes over from, and closes, its session on the first. For each member, start a new Claude Code session with this repository attached and paste its prompt. The prompt is the same for each member with its id in every place; the librarian's:

```
You are librarian@book.the-ultimate-insider, taking over from your session on the editor's first account, which ran out of usage. Pull dev, read CLAUDE.md, team/conductor/WAKE.md, your team/librarian/ROLE.md, policy.json and status.json, then your handover, team/conductor/handovers/librarian.md, and run admin/tools/start.py first. This first wake: (1) make and publish your session key as admin/tools/pki-agent.README.md says (team/librarian/key.json, key.png, a session folder), mark your first account's session superseded in team/librarian/sessions/<that session>/SESSION.json with an until, and push to dev; (2) create your scheduled task now, into this session, from team/conductor/schedule.json, the runs entry for librarian: its cron as the schedule and its prompt word for word; write the task id into your status.json and push to dev; (3) adopt your handover in your first debrief and begin its first item, inside the five steps of WAKE.md. The talk's repository is read-only: clone it into your scratchpad. Nothing from this repository ever goes to the Cold-Read repository. End with the end banner.
```

**historian**, **security**, **researcher**, **storyteller**, **publisher**: the same prompt with that member's id for `librarian` in every place. Every run is every two hours at the member's own minute (`schedule.json`), at the editor's word, for now.

## 1c. New members for the PDF lab (X1, 30 October 2026)

Two new members, drafted in `team/conductor/staffing/<id>/`. Start one new session each, with this repository attached, and paste its prompt. The designer's:

```
You are designer@book.the-ultimate-insider, a new member of the book's team, staffed at the editor's word (book.json X1) for the PDF lab. Pull dev, read CLAUDE.md, team/conductor/WAKE.md, team/conductor/projects/pdf-lab/README.md, and your drafted role in team/conductor/staffing/designer/ (ROLE.md, policy.json), and run admin/tools/start.py first. This first wake: (1) move your drafted ROLE.md and policy.json into team/designer/ (your own folder; leave the drafts where they are), add a status.json, make and publish your session key as admin/tools/pki-agent.README.md says (team/designer/key.json, key.png, a session folder), and push to dev; (2) create your scheduled task now, into this session, from team/conductor/schedule.json, the runs entry for designer: its cron as the schedule and its prompt word for word; write the task id into your status.json and push to dev; (3) begin your first task from your ROLE.md (the lab's visual language and the first experiment), inside the five steps of WAKE.md. The talk's repository is read-only: clone it into your scratchpad. Nothing from this repository ever goes to the Cold-Read repository. End with the end banner.
```

**ruv.sgit**:

```
You are ruv.sgit@book.the-ultimate-insider, a new member of the book's team, staffed at the editor's word (book.json X1) for the PDF lab. Pull dev, read CLAUDE.md, team/conductor/WAKE.md, team/conductor/projects/pdf-lab/README.md, and your drafted role in team/conductor/staffing/ruv-sgit/ (ROLE.md, policy.json), and run admin/tools/start.py ruv-sgit first. This first wake: (1) move your drafted ROLE.md and policy.json into team/ruv-sgit/ (your own folder; leave the drafts where they are), add a status.json, make and publish your session key as admin/tools/pki-agent.README.md says (team/ruv-sgit/key.json, key.png, a session folder), and push to dev; (2) create your scheduled task now, into this session, from team/conductor/schedule.json, the runs entry for ruv-sgit: its cron as the schedule and its prompt word for word; write the task id into your status.json and push to dev; (3) begin your first task from your ROLE.md (the first static experiment from one of the talk's animations, recorded in lab/runs/, no vault), inside the five steps of WAKE.md. The talk's repository is read-only: clone it into your scratchpad. Nothing from this repository ever goes to the Cold-Read repository. End with the end banner.
```

## 1d. New members for the reviewer experience (30 October 2026)

Two new members, drafted in `team/conductor/staffing/<id>/`, each on odd hours. Start one new session each and paste its prompt.

**developer**:

```
You are developer@book.the-ultimate-insider, a new member of the book's team, staffed at the editor's word for the reviewer experience. Pull dev, read CLAUDE.md, team/conductor/WAKE.md, team/conductor/projects/reviewer-experience/README.md, and your drafted role in team/conductor/staffing/developer/ (ROLE.md, policy.json), and run admin/tools/start.py developer first. This first wake: (1) move your drafted ROLE.md and policy.json into team/developer/ (your own folder; leave the drafts where they are), add a status.json, make and publish your session key as admin/tools/pki-agent.README.md says (team/developer/key.json, key.png, a session folder), and push to dev; (2) create your scheduled task now, into this session, from team/conductor/schedule.json, the runs entry for developer: its cron as the schedule and its prompt word for word; write the task id into your status.json and push to dev; (3) begin your first task from your ROLE.md (a first review page for one persona, with paragraph anchors and fictional data), inside the five steps of WAKE.md. Fictional data only; contact no real person. Nothing from this repository ever goes to the Cold-Read repository. End with the end banner.
```

**synthetic**:

```
You are synthetic@book.the-ultimate-insider, a new member of the book's team, staffed at the editor's word for the reviewer experience. Pull dev, read CLAUDE.md, team/conductor/WAKE.md, team/conductor/projects/reviewer-experience/README.md, and your drafted role in team/conductor/staffing/synthetic/ (ROLE.md, policy.json), and run admin/tools/start.py synthetic first. This first wake: (1) move your drafted ROLE.md and policy.json into team/synthetic/ (your own folder; leave the drafts where they are), add a status.json, make and publish your session key as admin/tools/pki-agent.README.md says (team/synthetic/key.json, key.png, a session folder), and push to dev; (2) create your scheduled task now, into this session, from team/conductor/schedule.json, the runs entry for synthetic: its cron as the schedule and its prompt word for word; write the task id into your status.json and push to dev; (3) begin your first task from your ROLE.md (the eight personas in review/synthetic/personas.json, and a first run once the developer's first page is on dev), inside the five steps of WAKE.md. Fictional data only; contact no real person. Nothing from this repository ever goes to the Cold-Read repository. End with the end banner.
```

## 2. What the conductor does next

- At its next wake after a member's `key.json` reaches `dev`: checks the key was made in that member's session (its `sessions/<id>/SESSION.json`), adds it to the key register (the build does), and checks its `policy.json` names its `comms/` paths. No vault keys to hand over: the team has no vaults.
- Checks each member's own task against `schedule.json`, and routes requests (`team/*/requests/<to>__*.md`) at :02.

## 3. The board and the mail: comms/, in git

The talk's team talked through two public vaults. The editor agreed on 30 October 2026 that this team needs none: the same two layouts are folders in this repository, `comms/` (`comms/README.md`). A new member adds three paths to its own `policy.json` (`comms/issues/<id>/**`, `comms/mail/<id>/**`, `comms/mail/mailroom/*/<id>__*`) at its first wake. Everything in `comms/` is public, forever.
