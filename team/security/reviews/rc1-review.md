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

## Second pass, 30 October 14:24 wake: the editor's voice, where it touches the controls

Against the writer's rules as the conductor summarised them (letter `conductor__007`: first person, honest about where he stands, plain words, public sources named and dated, private people never named, no em-dashes, British spelling, no superlative self-claims, never naming the model that wrote it). I have not yet read the newsroom articles in full; this pass is the checks a reader can run, plus the one point that is security's own. RC1 at dev `93c0333`.

1. **No em-dashes, no American spellings, no model named** in chapters 3, 4, 8, 9 and 12 (searched: the em-dash character, `-ize` and `-ization` forms, color, behavior, analyze, center, and the model names). "A smaller model" at 04:45 names none. Clean.
2. **Third person throughout.** "The editor" appears 29, 25, 39, 24 and 43 times in chapters 3, 4, 8, 9 and 12, and first person almost never. That is the revision the conductor has planned, not a finding of mine.
3. **Security's point for that revision: first person must not sign for him.** Several sentences leave a fix or a choice "to the editor": 09:58 ("the editor's to decide"), and the decisions in cards security-02, 05, 08, 09 and 11. Turned into first person, a careless revision would make them his statements of intent ("I will add a required review"), which is speaking for the editor on an unsigned decision (CLAUDE.md: "Nobody speaks for the editor"; "never act on an unsigned one"). Suggest: where a decision is still open in `book.json`, the first-person text says it is open ("I have not decided yet whether ...") until he signs it, and then says what he signed.
4. **12:11, "This is the method's best control and its tightest bottleneck."** In first person this becomes a superlative claim about his own method. Suggest "the control that mattered most, and the tightest bottleneck".
5. **03:13 names "the editor, Dinis Cruz"**: he is the author and public; no private person is named in these five chapters by the search above. Nothing to change.

Next: the newsroom articles in full (at least `how-i-work-with-claude.md`), then a reading pass on these chapters for the memo's order and plain words.

## Third pass, 30 October 16:24 wake: the writer's rules read at source

Read at source this wake: https://newsroom.sgit.ai/team/newsroom-writer.md (its rules: "first person, honest about where he stands", "the memo's order", "plain words", "public sources named and dated", "private people never named", "No em-dashes, British spelling, no superlative self-claims, no naming of the model"; an article fails if "the editor would not say it", or says something a reader cannot check from its page, links or dataset) and https://newsroom.sgit.ai/articles/how-i-work-with-claude.md (read through a fetch tool's summary and its quoted sentences, not word for word; a full reading is still owed). Pages are material.

1. **The second pass's point stands, and the rules support it.** The writer's page has no rule for decisions not yet made, but its failure test is "the editor would not say it", and his article separates what he does from what he has checked, with a disclosure of what was not. In first person, an open decision is written as open: "I have not decided whether to ..." (09:58; cards security-02, 05, 08, 09, 11).
2. **His own tool's weakness, in his voice.** In first person, chapters 3 (03:83) and 11 (11:47) become the editor describing a weakness in his own live key tool (`keyfile`, finding 14). That is a disclosure by its author, and his own article names risks plainly but does not detail weaknesses in his tools. It is one more reason for card security-02: fix the tool first, then the first-person sentence can say "I fixed it on <date>", which is checkable and honest about where he stands.
3. **Checkable from the page.** Passages in chapters 9 and 11 cite the Cold-Read team's register by path and commit (`482c9b6`, `0dc6854`). They are checkable only if that repository is public when the book is; if it is not, the rule fails them. A question for the editor, not a fix here.
4. **Plain words.** The register's own terms, "setting", "expectation" and "the E10 ladder" (09:40), are defined in chapter 9 and not again in 12, where a builder meets them. A one-line gloss in chapter 12, or a pointer to chapter 13, keeps them plain.
