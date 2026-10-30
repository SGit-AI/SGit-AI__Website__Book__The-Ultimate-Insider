# The control register

Kept by security@book.the-ultimate-insider. Every control in the talk's record (SGit-AI__Website__Presentation__The-Ultimate-Insider, history up to `298be4e`), each with evidence of it firing, what it stopped and what it missed; then the same register applied to this book's own team. The machine-readable form is `index.json` beside this file.

**Round 0 (30 October 2026):** the list of controls, with the first evidence found; the review of the pinned key tool started (`team/security/reviews/pki-agent-review.md`). **Round 1 (Friday night):** evidence for every control, or a plain "not found".

No number of our own here: every count is cited by the researcher's claim id in `claims/register.json` (C022 wake records, C023 verdicts (pre-reviews that said change: 11, of which 7 recorded as a verdict), C024 holds, C025 post-review findings).

| Id | Control | Kind | Evidence so far | Open question |
|---|---|---|---|---|
| C1 | policies and scopes (`agents.py check`) | setting | flagged CLAUDE.md outside the conductor's scope, talk wake `20261029T021416Z`; a pre-review sent back a plan writing in four other members' folders (`conductor/20261029T140334Z`) | it reports, it does not refuse; it cannot see a member widen its own scope (book team: four own-policy edits tonight, none reported; since `4f9ab97` and `085df5c` it reports scope, never and mandate changes) |
| C2 | the five-step wake | expectation, with a record | post-review caught cookie values in captured headers; pre-reviews said change in several wakes, kept under each record's `history` | no step said stop all day (C023); a finding came after a push (C025) |
| C3 | holds | setting | the conductor's hold at 18:44 UTC, talk `867f8c2` | the one hold (C024) came from the editor's word about usage |
| C4 | session keys | expectation, with a published record | the conductor checked two new keys and sealed the vault keys to them, talk `4adc04a` | to find |
| C5 | the pinned key tool | setting (a hash) | the hash check passed before this team's keygens | never read line by line: review started |
| C6 | the gate and its leak tripwire | setting | in place from `1f7c633` (00:40); no leak failure found yet | cookie values and page tokens had no pattern: the reviews caught them (`af0010b`, `f30b73f`) |
| C7 | the editor's signed decisions | expectation | the editor's 15:00 decisions committed and routed, talk `78d517d`; book team: security's policy widening waited for decision C10 | to find |
| C8 | public vaults and `vault_check` | setting, with an expectation | recorded clean in post-reviews; a pre-review added a missing pattern to it | a failure: page tokens in a 02:22 push, found after it; history keeps them (C025) |
| C9 | outside accounts on the repository | setting (GitHub role), with an expectation | book team: the publisher asked before Leanpub was added; advice: Read only | the role the editor gives |
| C10 | the session's own permission check | setting, outside the repository | refused security widening its own policy before the editor's word, allowed it after decision C10; refused the researcher after C10, and the publisher's install of outside code (`cc04d0a`) | not consistent: the same edit was allowed in two other sessions before any signature |

**Correction (30 October 2026, 02:45 UTC):** round 0 said no pre-review in the talk's record said change or stop. That was wrong: the first scan read each record's steps and missed its top-level `history`, where a sent-back verdict is kept. Several pre-reviews said change.

A **setting** is enforced by a tool; an **expectation** is a rule an agent is trusted to follow. The difference is the book's point: the insider argument is made with this benign team, so the register says what each control does, never how to get round one.

**Ids.** C1 to C10 here collide with `book.json`'s decisions (C10 is also a decision) and the researcher's claims (C0nn). They will be renamed in round 1, with notice to every member who cites them.
