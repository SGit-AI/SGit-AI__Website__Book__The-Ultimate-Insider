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
