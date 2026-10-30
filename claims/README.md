# The claims register

Kept by researcher@book.the-ultimate-insider. Every number the book may use comes from here: `register.json`, one entry per claim, with where it is cited, the value, its state, the evidence (commit or path) and the method, so anyone can run it again.

- **Source:** the talk's repository (SGit-AI__Website__Presentation__The-Ultimate-Insider) at `298be4e` unless an entry says otherwise. Anything after `298be4e` is material added after the day, cited by commit and said so.
- **Times** are UTC. London was on GMT on 29 October 2026, so they are London times too.
- **States:** `checked` (the record agrees), `corrected` (the record gives another number: use the register's), `open` (the record does not settle it, or the editor must decide). A contradiction of the editor is recorded even when the editor keeps the claim.
- **Asking for a number:** write `team/<you>/requests/researcher__<slug>.md` (the mail vault, once it exists).

## Round 1, first pass: the numbers in the briefs (30 October 2026)

21 claims: 17 checked, 2 corrected, 2 open. The conductor's counts in `BRIEF-CORRECTIONS.md` (814 commits by 18:46: 603 Claude, 210 GitHub Actions, 1 the editor; 210 releases on the day plus v0.2.0) all agree with the log.

- **Corrected:** files outside `src/` are 1,083, not about 1,260 (C019); "nineteen hours" is 00:16 to 19:00, 18 h 44 min, not to the 23:19 merge (C010).
- **Open, for the editor:** "a ten-agent team": the record has nine staffed agents and security proposed, never staffed (C011). "Twenty minutes before the lock": there were several locks; 18:37 is 23 minutes before the talk (C018).
- **For the failures-stay-in rule:** one work commit (`88b8f00`, @designer, 18:45:35) and a release (v0.1.209) landed after the 18:44 hold (C006).

## Round 1, second pass: the requests of security and the storyteller (30 October 2026, 02:32 wake)

C022 to C028, and C018 settled: 28 claims, 24 checked, 3 corrected, 1 open (C011, ten agents or nine).

- **The controls in numbers:** 162 wake records; no step said stop all day; 11 pre-reviews sent a plan back; 4 post-review findings, 3 of them other sites' tokens in captured pages already pushed (C022 to C025). One hold (C024).
- **The talk:** 74 min 55 s of beats against a 90-minute countdown (C026). No part was ever locked (C027). The player port landed at 15:07, not 18:37 (C028).

## Round 1, third pass: the talk's own register (30 October 2026, 03:32 wake)

C029 to C031, and C023's method stated at security's question: 31 claims, 26 checked, 3 corrected, 2 open.

- **The talk's register** holds 320 claims, built at 18:20: 210 hold, 55 in part, 52 not checked, 3 do not (C029). None of the three that fail reached the stage (C030).
- **A correction that never reached the stage:** the definition slide said $17.4M a year, while the talk's own register had found it superseded by the 2026 edition's $19.5M (C031, open until the figure is checked at source).

## Round 1, fourth pass: graphs.sgit.ai (30 October 2026, 04:32 wake)

At the editor's request, `graphs-sgit-ai.md`, the nearest precedent read closely, with C032 to C036: 36 claims, 29 checked, 3 corrected, 4 open. Its three books are the first entries of the comparison set.

## Round 1, fifth pass: every number rerunnable (30 October 2026, 05:32 wake)

Every entry now has a `command`, read-only and pinned to a commit; `appendix-a-commands.md` is the reading copy for the book's Appendix A. C014 corrected (ruv-sgit 84, conductor 107; 13 commits unattributed). C037, the editor's cost of the day: not in the record, open. 37 claims: 28 checked, 4 corrected, 5 open.

## Round 1, sixth pass: the precedent closed, the talk's claims triaged (30 October 2026, 06:32 wake)

C035 and C036 checked by reading graphs.sgit.ai's Appendix C and chapter 12 in full. C038 and `talk-claims-triage.md`: 80 of the talk's 320 claims are placed on stage by its register, and 46 of them were not confirmed whole by 18:20; none enters the book without its own entry. 38 claims: 31 checked, 4 corrected, 3 open.

## Round 1, seventh pass: the talk's claims matched to its beats (30 October 2026, 07:32 wake)

C039: of the 80 claims placed on stage, 55 are in a beat of the talk at `298be4e`, and 29 of those were not confirmed whole by 18:20 (13 in part, 16 not checked). The 63 off-stage claims that do not hold whole are sorted by group in `talk-claims-triage.md`. 39 claims: 32 checked, 4 corrected, 3 open.

## Round 1, eighth pass: two failures, read closer (30 October 2026, 08:32 wake)

- **C031, checked at source.** $17.4M is right for the 2025 edition and $19.5M is the 2026 one. The slide line was written at 00:40 and never changed, though the talk's researcher proposed the exact replacement to deck at 02:52, about 16 hours before the talk.
- **C040, the player priority.** The editor's briefs of about 14:00 make the player the main priority, but the same hand-over put the editor's own feedback lane first, at his word. The lessons brief is corrected in `BRIEF-CORRECTIONS.md`.

40 claims: 33 checked, 5 corrected, 2 open.

## Round 1, ninth pass: the freeze (30 October 2026, 09:32 wake)

The historian's timeline, verified against `298be4e`, settles both: the $17.4M fix (C031) arrived five minutes after the editor froze the slides at 02:47 and was never carried across the 14:07 lift; the player (C040) was not started by 14:53, because the editor's lane went first. 40 claims: 33 checked, 5 corrected, 2 open.
