# The control register

Kept by security@book.the-ultimate-insider. Every control in the talk's record (SGit-AI__Website__Presentation__The-Ultimate-Insider, history up to `298be4e`), each with evidence of it firing, what it stopped and what it missed; then the same register applied to this book's own team. The machine-readable form is `index.json` beside this file.

**Round 0 (30 October 2026):** the list of controls, with the first evidence found; the review of the pinned key tool started (`team/security/reviews/pki-agent-review.md`). **Round 1 (Friday night):** evidence for every control, or a plain "not found".

No numbers here: every count goes through the researcher's register in `claims/`.

| Id | Control | Kind | Evidence so far | Open question |
|---|---|---|---|---|
| C1 | policies and scopes (`agents.py check`) | setting | flagged CLAUDE.md outside the conductor's scope, talk wake `20261029T021416Z`; a pre-review sent back a plan writing in four other members' folders (`conductor/20261029T140334Z`) | it reports, it does not refuse |
| C2 | the five-step wake | expectation, with a record | post-review caught cookie values in captured headers; pre-reviews said change in several wakes, kept under each record's `history` | whether a finding ever stopped a release |
| C3 | holds | setting | the conductor's hold at 18:44 UTC, talk `867f8c2` | the one hold came from the editor's word |
| C4 | session keys | expectation, with a published record | the conductor checked two new keys and sealed the vault keys to them, talk `4adc04a` | to find |
| C5 | the pinned key tool | setting (a hash) | the hash check passed before this team's keygens | never read line by line: review started |
| C6 | the gate and its leak tripwire | setting | in place from `1f7c633` (00:40); no leak failure found yet | cookie values and page tokens had no pattern: the reviews caught them (`af0010b`, `f30b73f`) |
| C7 | the editor's signed decisions | expectation | the editor's 15:00 decisions committed and routed, talk `78d517d` | to find |
| C8 | public vaults and `vault_check` | setting, with an expectation | recorded clean in post-reviews; a pre-review added a missing pattern to it | to find a failure |
| C9 | outside accounts on the repository | setting (GitHub role), with an expectation | book team: the publisher asked before Leanpub was added; advice: Read only | the role the editor gives |

**Correction (30 October 2026, 02:45 UTC):** round 0 said no pre-review in the talk's record said change or stop. That was wrong: the first scan read each record's steps and missed its top-level `history`, where a sent-back verdict is kept. Several pre-reviews said change.

A **setting** is enforced by a tool; an **expectation** is a rule an agent is trusted to follow. The difference is the book's point: the insider argument is made with this benign team, so the register says what each control does, never how to get round one.
