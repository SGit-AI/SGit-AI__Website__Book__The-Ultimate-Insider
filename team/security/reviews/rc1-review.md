# Security's review of RC1 (first pass)

By security@book.the-ultimate-insider, second session (`session_01Kw9UwFe8iX6rP7bn78h2m9`), 30 October 2026, from about 13:05 UTC, against `team/conductor/rc1/` as it stood at `2c49993` on dev. The drafts are the conductor's; this review changes none of them. Findings go to the conductor by letter (`comms/mail/mailroom/conductor/security__006-rc1-review-first-pass.eml`), each with the file and the line. Line numbers are those of the files at that commit.

Read in this pass: chapter 9 in the passages the storyteller flagged, then chapters 3, 4, 8, 11, 11b and 12 where they describe a control, checked against `controls/`, `admin/build/validate.py`, `admin/tools/pki-agent.README.md` and `team/security/reviews/pki-agent-review.md`. Not yet read in full: chapters 3, 4, 8 and 12 beyond the control passages, and the editor's voice in all of them (the next pass).

## 1. The four chapter 9 passages flagged as reading like methods

The rule: nothing on this team builds or describes anything attack-shaped. The test used here: a passage may say what a member could do, why it mattered, what the control stopped and what it missed; it may not say how a control could be got round, step by step, or join a capability to the consequence that makes it a route.

| Line | Verdict | Why |
|---|---|---|
| 09:52 (the hold reads at the start of a wake) | keep | It says what happened (a wake already running committed after the hold) and what the control missed (a hold stops the next wake, not the running one). The Cold-Read threat label "keep working through a hold" is quoted as a name, not as a step. The fix is stated in chapter 12 (line 73). |
| 09:58 (a tool and its pin changed in one commit) | keep | A residual named at the level of design, with the fix named and left to the editor (card security-11). It is the editor's own repository and the book tells him first. |
| 09:96 (nothing checked a key against its session) | change one clause | After option B (card security-06) the sentence states the risk without the consequence: good. The last clause, "because the marker and the trailer are free text", explains which two fields a check would have to trust. Suggest ending at "consistency, not proof." The reader loses nothing; the clause is the only how in the paragraph. |
| 09:114 (the permission check was inconsistent) | keep | It records that the same edit was allowed in some sessions and refused in others, by commit, and draws the lesson (a boundary that holds inconsistently cannot be planned around). It describes a control's inconsistency, not a way to exploit it. |

## 2. Corrections where the text says more or less than the record

1. **11:47**, "the remedy it names is a warning in the tool's README". That remedy is now in place in this repository: `admin/tools/pki-agent.README.md` says "Never run `keyfile` in a session", added by the conductor after finding 14. Suggest: "... and the remedy it names, a warning in the tool's README, is now in this repository's copy; the tool itself is unchanged (card security-02)."
2. **03:83 and 09:60**, "by its tenth wake it had read every command". True of the commands. The review is not yet line by line complete: the DER helpers (2394 to 2495) and the vendored QR generator (checked for network calls and file writes only) remain (`pki-agent-review.md`, Coverage and Next). Suggest "had read every command; the low-level helpers remain".
3. **08:77**, "The reviews ... caught tokens in captured pages ... they worked as brakes on individual pieces of work." Chapter 4 (line 73) now says, correctly, that none of the three token findings came before the values were public. "Caught" and "brakes" overstate it here. Suggest "found tokens in captured pages after they were pushed".
4. **11b:65**, the five-step wake "serves safety, as a second reader the agent cannot skip". Chapter 9 (line 88) says the opposite, correctly: the verdicts are written by the member, nothing proves a sub-agent ran, and the order bent three times. Suggest "a second reader the protocol requires", with a pointer to chapter 9.
5. **11b:89**, "a team that can be stopped in one push". Holds as written of the next wake; chapter 9 (line 52) shows a running wake committing after it. A half sentence keeps the two chapters consistent: "stopped in one push, from its next wake".
6. **12:65**, "Each member creates its own scheduled task, from its own session." Today's takeover adds the case a builder will meet: when an account runs out, each member's task is paused (never deleted) on the old account and a new session on the new account makes a new key and a new task, and marks the old session superseded (`team/conductor/sessions-register.json`; `team/security/sessions/`). It is the book team's own evidence for this control and is going into the register (Done when 3); the chapter may want a sentence.

## 3. The twelve cards in `annotations/security.json`

This session adopts the cards drafted for security, with these answers:

| Card | Answer |
|---|---|
| security-01 | adopt; applied. Add correction 2 above. |
| security-02 | adopt, unchanged: a decision for the editor (fix the live key tool before the book describes it). |
| security-03 | adopt; applied, checked: `check_vendored` reads `admin/tools/*.sha256` (`admin/build/validate.py`, line 109, `e7d3d3d`). |
| security-04 | adopt; applied, checked in chapter 4 (line 73); add correction 3 above for chapter 8. |
| security-05 | adopt; partly applied. Still open for the editor: D12, and `aa7a3eb` in the source lists at 04:100 and 06:90. |
| security-06 | adopt; applied. Add the one-clause change to 09:96 above. |
| security-07 | adopt; applied, checked: the gate calls only `agents.py overlaps` (`validate.py`, line 133). |
| security-08 | adopt, unchanged: a question for the editor. |
| security-09 | adopt, unchanged: a decision for the editor; the valve holds only while the Cold-Read team is closed. |
| security-10 | adopt, with one condition: it stays true only once 09:96 drops its last clause. |
| security-11 | adopt, unchanged: a decision for the editor. |
| security-12 | adopt; the renaming of control ids is security's own (board 004), next wake. |

## Next pass

The editor's voice in chapters 3, 4, 8, 9 and 12, by the newsroom writer's rules (conductor's letter 007); the full text of chapter 9's control sections against `controls/index.json`; and the book team's own controls, the takeover first, in the register.
