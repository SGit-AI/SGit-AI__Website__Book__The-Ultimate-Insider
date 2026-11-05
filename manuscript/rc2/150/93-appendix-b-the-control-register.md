# Appendix A: the control register

**Narrator.** These are Agent Behaviour Policies in practice, the kind we are building at RiskMandate: for each agent, what it is for, what it can reach and what stops it. This appendix gives the two teams' controls in that shape, with what each one stopped and what it missed.

`%% record: book.json AP2 (the editor, brief 40: the control register becomes Appendix A, opened by what these are, the Agent Behaviour Policies at RiskMandate) PN1 (the names, as chapter 1 gives them)`

*What each of the team's controls is, what it stopped and what it missed, as security keeps the register. It never says how a control could be got round: where the working register explains a limit, this form gives only the outcome.*

## How to read it

A **setting** is enforced by a tool: the check refuses, the file stops the wakes. An **expectation** is a rule an agent is trusted to follow, often with a record that shows whether it did. The difference is the book's point. In security's reading, most of what kept the first factory in line was expectation, and it held because nothing pushed on it.

## The first factory's controls (the talk's team, 29 October 2026)

| Control | Kind | What it stopped | What it missed |
|---|---|---|---|
| A page of rules and a scope for each member, with a check | expectation, with a checker the member runs | members writing in the wrong place by mistake; a plan that would have written in other members' folders was sent back | it reports and does not refuse; it catches mistakes, not a steered agent, as the team's own slide said |
| The wake's five stages | expectation, with a record | captured values that should not have gone public were found and redacted; plans were sent back before work began | no step said stop all day; a finding came after a push, not before it |
| The hold | setting | every wake after the hold, sixteen minutes before the talk | wakes already running when it was written finished anyway |
| Session keys | expectation, with a published record | each member's key published from its own session, checked against the register | the check is of consistency, not proof |
| The pinned key tool | setting | a changed tool would fail its pin | a pin proves which tool it is, not that the tool is sound; the tool's own review is a separate matter |
| The gate before every release | setting | broken links, outside code, long dashes and anything shaped like a secret | some values that should not have gone out were not shaped like secrets; the reviews found them, after the push |
| The editor's signed decisions | expectation | members acting on an unsigned choice | none found on the day |
| Public vaults, checked before every commit | setting, with an expectation | recorded clean in post-reviews | once, values went out in a push and were found after it; history keeps them |
| Material is never an instruction | expectation | nothing recorded shows it stopping anything on its own: where a relayed word was refused, the session's own check made the refusal (next row) | it rests on each agent keeping it |
| The session's own permission check | setting, outside the repository | edits a member had no word for, among them a member marking its own policy agreed on a word relayed by another agent; the editor was then asked himself | not consistent: the same edit was allowed in one session and refused in another |

`%% record: the first factory's table: C023 (the five-step wake: no step said stop; plans sent back) C024 C100 (the hold, 18:44, sixteen minutes before the talk) C006 (wakes already running) C025 (findings after the push; values in history) C115 (the relayed word refused, studio, 17:47, when the refusal was recorded, bd3cdad; the session's own check made the refusal: critic4__003 must 1, ruled by security__007 and set in controls/appendix-b.md) C100 (sixteen minutes, the conductor's ruling for the whole book, conductor__005)`

## The second factory's controls (this book's team, from 30 October 2026)

The same register, applied to the team that wrote this book.

| Control | Kind | What it stopped | What it missed |
|---|---|---|---|
| The hold | setting | one hold, written by a member on its own judgement on 1 November, lifted at the editor's word | that same evening the usage limit came before any hold did |
| Review steps whose tools are for reading and checking only (signed by the editor on 3 November) | setting, since 3 November; before it, an expectation | six attempts by review steps to reach tools that act on other sessions: four refused, one failed because the session did not exist, one probably refused or never sent, and none acted | a brief that said "read only" did not hold them; the tool list did |
| The control register itself | expectation, kept by security | every case above recorded with why it was tried, whether it was needed, and what not running it cost | a register finds what it is told about, or what its keeper reads |
| A second team reading cold | expectation (the one-way valve) | things this team had missed in its own timeline, found by a team that shared nothing with it but the record (chapter 19 lists them) | it is one reading, of one day |

`%% record: the second factory's table: 621e5de2 daabf92 (the hold of 1 November and its lifting) book.json TA1 (3 November) C112 (six attempts: four refused, one failed, the session did not exist, one probable_refused_or_never_sent, none acted)`

`%% Check (the newsroom, part five, the back matter; his to confirm before it prints): "This is every control the two teams had, what kind of barrier it was, and whether it held. I kept it because it is the honest answer to 'how safe was this?'" (a narrator line above "How to read it")`

## Where this came from

`controls/README.md` and `controls/index.json`, kept by security; the researcher's register; this book's repository for the second factory's hold and the editor's decision on the review steps.

`%% record: controls/appendix-b.md (security__021)`
