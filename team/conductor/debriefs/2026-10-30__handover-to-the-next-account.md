---
title: Handover, the conductor's debrief for the session that takes over
round: 1
date: 2026-10-30
commits: dev at the commit that carries this file
site_version: the release after this push
outside_scope: none
---
## Why this exists

On 30 October 2026, at about 11:40 UTC, the editor (Dinis Cruz) said the first account was nearly out of usage and that another account, with more available, would continue. He asked for a detailed debrief with a handover: the conductor's first, then one per member. This is the conductor's. The members' are in `team/conductor/handovers/`, one file each, written by the conductor (members write only their own folders, so the conductor holds their handovers until each member's new session adopts it).

The session that wrote this is `conductor@book.the-ultimate-insider` on the first account, session `session_01Kw9UwDcSTJ2nZLAFJMat9U`, key `sha256:15762445fb34548e`. It stops here.

## Start here (the new conductor session, in order)

1. Read `CLAUDE.md`, `team/conductor/WAKE.md`, `team/conductor/ROLE.md`, `policy.json`, `status.json`, then this file, then the wake record `team/conductor/wakes/20261030T103103Z.json` (the last full wake, closed ok).
2. Run `python3 admin/tools/start.py conductor --kind "takeover from the first account" --objective "pick up RC1 and the team" --model <model>`. It pulls `dev`.
3. Make your own key (`admin/tools/pki-agent.README.md`): a new session makes a new key and publishes it in `team/conductor/key.json` with a new session folder. The first account's key stays in the record under `team/conductor/sessions/session_01Kw9UwDcSTJ2nZLAFJMat9U/`; do not reuse or print anything from it. Say in your debrief that the key changed hands and why.
4. Clone what you read (read only, in your scratchpad, never push to them):
   - the talk: `SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider`, a FULL clone (`git clone` without `--depth`; a shallow clone gives wrong counts, which happened here). The day's record ends at `298be4e`; the transcript and debrief added after the day are at `a9c0b49` and later.
   - the blind repository `SGit-AI/SGit-AI__Website__Cold-Read__The-Ultimate-Insider`, read only, and only to read its findings. The one-way valve holds: nothing from here goes there, ever.
   - the Gen ZX Founders book, `SGit-AI/SGit-AI__Website__Gen-Z-Developers`, read only (its RC2 pen notes are in `admin/content/reviews/paper/rc2-0*.json`).
5. Do not create any scheduled task until the editor says so (see "The schedule" below).

## Where things stand

### The book

- **The plan** (draft 5) is signed (P0, about 10:00 UTC). No decision is open in `book.json`; every decision signed this morning is listed below.
- **RC1** lives in `team/conductor/rc1/`, not yet in `manuscript/`. It is 18 chapter files plus the about page, about 72,000 words, 294 pages at 6x9 with the cover:
  - `0-about-this-release-candidate.md`, `00-before-you-start.md`, `00b-how-to-read-a-map.md` (new), `01` to `11`, `11b-what-was-already-there.md` (new), `12-build-your-own.md`, `13-concepts-and-principles.md` (new), `99-appendix-a-every-number-rerun.md`.
  - `resources/images/` (42 stills and collages) and `resources/images/maps/` (16 Wardley maps).
  - `cover/` (three concepts, concept 1 used; `.gitignore` has one exception for this folder).
  - `infographics/` (30 drawn by code, two withdrawn as stale, `manifest.json`, `callouts.json` with 50 call-outs, `README.md` with the visual language and seven points for the next design round).
  - `maps/` (16 map JSONs, `README.md`, `placements.json` for maps 6 to 16).
  - `annotations/` (98 cards: conductor, storyteller, historian, librarian, researcher, security, publisher, gen-zx; `SCHEMA.md`). Role cards were drafted by conductor sub-agents, not by the members: each member should adopt, change or withdraw its cards.
  - `reviews/gen-zx-team.md` (the Gen ZX team's review, its ten changes in order) and `research/the-two-and-a-half-years.md` (the dossier on the public work before the day).
  - `tools/`: `wardley.py` (the map renderer, reworked for print), `wardley_png.js`, `assemble_rc1.py` (builds the illustrated RC1 PDF), `companion.py` (builds the companion PDF).
- **The editor has both PDFs** (RC1, 294 pages; the companion, 67 A4 pages, 98 cards, 53 decisions with tick boxes) and is reading them on paper on a flight. His ticks and notes are the next input. When they come, turn each ticked decision into an open decision in `book.json` for him to sign; never act on a tick he has not signed.

### What the corrections pass changed (so you do not undo it)

- The leak account: the cookie values (04:10), other sites' public page tokens (03:05) and form tokens (06:14) each reached a pushed, public history before a review caught them; redaction fixed the files, not the history; D12 (what to do about it) was open at 19:00 and no answer is recorded since. The book says this and no longer says where the values are or how to read them. Keep it that way. Two source lists (chapters 4 and 6) still cite `aa7a3eb`, the researcher's note that does name them: security's card asks the editor whether to drop that citation.
- Security: the key tool's finding 14 is medium (`keyfile` prints private keys in the clear; found first by the Cold-Read team); this book's gate was widened (`check_vendored` reads `admin/tools/*.sha256`, `e7d3d3d`).
- Claim ids (C037 for the 5-hour window, C005 with C006, C011's two dating methods, C014's counts by merge parents), consistency fixes (vaults public at 01:09; 02:14; chapter 1 and 11 on agents choosing), vendor names removed from prose, decisions since signed shown as signed, slide stills captioned as shot after the day from v0.2.0.
- The about page says what was added this morning and that the companion exists.

### The schedule

- At the editor's word (about 10:50 UTC, usage at 94%), the conductor paused every scheduled task on the first account: the conductor's, the six members', the Cold-Read conductor's and the editor's `@inbox` run. Paused, not deleted. `team/conductor/schedule.json` says so.
- A scheduled task belongs to the account that made it. The new account needs new sessions and new tasks; the slots in `schedule.json` (conductor :02, librarian :09, historian :17, security :24, researcher :32, storyteller :39, publisher :47, London) still apply. Only the editor says when to start them. Each member's new session creates its own task from its own session, as the first batch did (`team/conductor/ONBOARDING.md`).
- The publisher's session was mid-turn when the tasks were paused; an interrupt was refused by this session's permissions. Check its branch (`claude/publisher-onboarding-setup-jyrfy9`) before assuming its state.

### Waiting on the conductor (do these first)

1. **The site build must copy the chapters' images** (publisher's letter `comms/mail/mailroom/conductor/publisher__002-rc1-needs-build-py.eml`). In `admin/build/build.py`, after the chapter loop appends to `toc`, copy `manuscript/resources` to `OUT/book/resources` (`shutil.copytree(..., dirs_exist_ok=True)`), and fix `admin/versions.html`'s link to the removed `book/about-this-edition.html`. Gate, push to dev, tell the publisher.
2. **Tell the publisher RC1 has moved on.** Its branch holds the 16-file RC1 of this morning (217 pages). The current RC1 is in `team/conductor/rc1/` (19 files, the corrections, maps, infographics and call-outs). It should take the current folder, and the build changes the scratch build used: `--embed-resources` in the pandoc HTML call and the figure CSS (letter 005 to the publisher), plus the call-out style in `tools/assemble_rc1.py`'s `CALLOUT_CSS`, translated to Markua asides (M1).
3. **Letters not yet answered** in `comms/mail/mailroom/conductor/`: `publisher__003` (taken), `storyteller__003-rc1-review.eml` (21 findings on RC1), `researcher__001-rc1-numbers.eml`, `security__005-review-and-rc1.eml`. Most findings were absorbed by the corrections pass; answer each with what changed and what did not.
4. **The researcher's letter 006** (`comms/mail/mailroom/researcher/conductor__006-numbers-to-register-rc1.eml`) lists what RC1 uses that the register does not hold yet: the dossier's dates (tagged "(dossier: ...)" in chapter 11b), the Cold-Read counts, derived figures, and what the infographics maker could not find.
5. **Open issue** `comms/issues/conductor/issues/open/001-comms-paths-for-every-member.md`: C10b is signed and done for four members; close it with the evidence.

### Rebuilding the two PDFs

The scripts in `team/conductor/rc1/tools/` were run from a scratch folder; two paths are fixed at the top of `assemble_rc1.py` (`REPO`, and `CHROME`, the headless shell under `/opt/pw-browsers/`). To rebuild:

1. Make a scratch folder with `bookbuild/publishing/` copied from `publishing/`, and in that copy add `"--embed-resources"` to the pandoc HTML call and the figure CSS (`figure`, `figure img { max-height: 4.6in }`, `figcaption`) to `book.css`; set `metadata.yaml`'s title to "The Ultimate Insider" and its subtitle to the RC line. Once the publisher's build carries these, use `publishing/` as it is.
2. Copy `assemble_rc1.py` next to `bookbuild/` and run it with `python3 -I`. It copies the chapters in name order, places the infographics, maps and call-outs at their anchors (build time only; the chapter sources stay clean), builds, and puts `cover/cover-1.jpg` in front. It prints any anchor it could not find: fix the anchor, never the chapter, unless the chapter is wrong.
3. Run `python3 -I companion.py --rc1-pdf <the RC1 PDF> --annotations team/conductor/rc1/annotations --out <companion.pdf>`. It finds each card's page by its anchor sentence; a card it cannot place says "page not found".

### Decisions the editor signed on 30 October (all in `book.json`)

Q1 (repos and sites), Q5 (CC BY 4.0), S6 (the day: first commit to the last before 19:00), Q2 (round the clock; wait out the 5-hour reset), C10 and C10b (members' comms paths), P0 (plan draft 5), O1 A, O2 A, O3 yes, O5, C011 (nine staffed), O4 A (the record only, no interview), Q3, Q4, L1 (minimum $0, suggested $19.99), L2 (Leanpub from main), U1 A, M1 (Markua). The editor's principles of about 10:30 are a brief: `briefs/2026-10-30__in-session/01-principles-maps-and-the-plumbing.md`. His voice rules: first person, honest about where he stands, the memo's order, plain words, public sources named and dated, private people never named, no em-dashes, British spelling, no superlative self-claims, never naming the model.

### The editor's instructions still in force

- RC1 is revised in place; there will not be a long series of candidates. A release candidate is a release, to be read as finished.
- Use many images, resized and collaged; a very visual book; maps early, simple to complex; concepts explained where introduced; a design round with a maker focused on communicating comes after this first pass.
- He decides by signing; nobody speaks for him. No pushes to `main`. No schedules without his word. Nothing goes to the blind repository.

## What went well, and what did not

- Running the roles as sub-agents inside one session moved RC1 from text to an illustrated, corrected candidate with a companion in about an hour. The five-step wake held: one plan amendment, a pre-review with conditions, a post-review and a post-check.
- RC1 was first pushed with a kinder leak account than the record supports; the reviews caught it within the hour. The lesson the book itself teaches: a review catches an instance, not a class. Read the register before drafting any account of a failure.
- The build read a stale PDF once (wrong output folder); a page count caught it. Check page counts after every build.
- The usage ran out faster than the work: the editor had to pause the team by hand. The new conductor should watch usage and hold the team before the limit, as the talk's conductor did at 18:44.

## Where this came from

This session's record in `team/conductor/` (wakes, debriefs, requests, rc1), `book.json`, the letters in `comms/mail/`, and the editor's words in this session on 30 October 2026.
