# What exists

What exists in this repository and on its site, kept current by whoever ships. A thing not listed here does not exist, whatever a brief or a page says.

## The site

- The site at https://the-ultimate-insider.book.sgit.ai, built by `admin/build/build.py` (the talk's build, ported) into `_site/`, gated by `admin/build/validate.py` (the talk's gate, ported), released and deployed by `.github/workflows/release.yml` (the talk's, unchanged). v0.1.0 released from `dev` on 30 October 2026.
- The book's pages: home, the book (the manuscript, its contents, the title candidates), the plan (dates and rounds), decisions (open and decided), the briefs (each published in full), sources, about. Built from `book.json`, `briefs/` and `manuscript/`.
- The admin section, the talk's: admin and engineering, the dashboard, wakes, commits and messages, releases, the team and each member's page, the roles, the schedule, the key register, and the sources of truth (what exists, the rules for agents, the corrections, onboarding, the wake protocol). The board, the mail and the public vaults pages are built only when `team/conductor/vaults.json` exists.
- Every page has a `.md` twin; `llms.txt`, `sitemap.xml`, `robots.txt`, `version.txt`, `book.json`, `admin/keys/index.json`, `admin/commits.json` and the release data are generated. The offline cache (`src/static/sw.js`, kill switch `sw.json`) is the talk's.

## The team's machinery (ported from the talk's repository at `298be4e`, 30 October 2026)

- `admin/tools/`: `start.py`, `banner.py`, `wake.py`, `vault_check.py` (its email check adapted: our agent addresses have a dot after the @), `vault_handover.py`, `pki-agent.mjs` with its sha256 pin and README, `qr.mjs`. `admin/build/agents.py`.
- `CLAUDE.md` (the talk's rules, rule for rule, then the book's), `team/conductor/WAKE.md`, `team/conductor/reviews/` (the four sub-agent briefs), `team/conductor/known-keys/` (the DC Vault Registry, carried over, to be re-confirmed by the editor).
- The conductor: staffed (this session, conductor@book.the-ultimate-insider), with its key published (`sha256:15762445fb34548e`), `ROLE.md`, `policy.json`, `status.json`, `schedule.json` (proposed), `ONBOARDING.md`, and the Cold-Read hand-off in `handoffs/`.
- The first batch, proposed with `ROLE.md`, `policy.json`, `status.json` and a slot: librarian, historian, security, researcher, storyteller, publisher. Their prompts are in `ONBOARDING.md`.

## The book

- `book.json`: dates, rounds, phases, roles and decisions (S1 to S8 decided, Q2 to Q4 open).
- `briefs/2026-10-30/`: the editor's six brief files, as given.
- `manuscript/`: `Book.txt` and `about-this-edition.md`. No chapter: the plan is not signed.

## The historian's timeline (historian@book.the-ultimate-insider)

- `timeline/README.md`: the method for the timeline of 29 October (round 0): the record is the history reachable from `298be4e`, the day ends at `88b8f00` (18:45) and v0.1.209 `cb5b996` (18:46), UTC equals London that day, entries cite a commit or a file at `298be4e`, three spans kept apart, and ten candidate turning points to argue or drop in round 1. No timeline entries yet.
- `team/historian/`: staffed 30 October 2026; key published; its own hourly task at :17 London.

## The claims register (researcher)

- The researcher: staffed (session_01Kw9UwBta1dcP9qBJUURLPZ), key published (`sha256:4e0287f6640d61f0`), its own scheduled task hourly at :32 London.
- `claims/register.json` and `claims/README.md`: the numbers in the briefs checked against the talk's log at `298be4e`, 21 claims (17 checked, 2 corrected, 2 open). The talk's own claims (`evidence/claims/`) and the comparison set are not yet registered.

## The storyteller's chapter plan (storyteller@book.the-ultimate-insider)

- `chapter-plan/`: draft 1 of the chapter plan, **not signed**: thirteen chapters and the closing sources, 48,200 words, the workflow as the main thread with the talk's beats braided through it, the failures each chapter keeps, its evidence by path at `298be4e` or commit (index entries once the librarian's index exists), and word budgets and drafting timings (`budget.md`). Five open questions for the editor (`open-questions.md`, O1 to O5). No number in it is registered yet.
- `team/storyteller/`: staffed 30 October 2026; key published (`sha256:edc67e3cc68b3b07`); its own hourly task at :39 London. Requests to the conductor (the open questions into `book.json`) and the researcher (the numbers the plan leans on) in `team/storyteller/requests/`.

## The publisher (publisher@book.the-ultimate-insider)

- Staffed 30 October 2026, key `sha256:88b9a9682c1b72e9`, its own hourly task at :47 London.
- `publishing/build_book.py`: a PDF (6 by 9 inches, via pandoc and headless Chromium) and an EPUB from `manuscript/` in the order of `Book.txt`, into `_site/manuscript/` (never committed). Runs locally; not in CI yet (asked of the conductor).
- `publishing/LEANPUB.md`: the editor's steps to create the Leanpub book from this repository, and the price options. No Leanpub book exists yet.

## Not yet

- No member but the conductor is staffed; no scheduled task exists (the editor says go and sets the hours, Q2).
- Not ported yet, because each needs something only the editor can create: the team's two public vaults (and so the board, the mail, the vaults page, vault handovers), the editor's voice lane (`pane.js`, `lane.py`, its own vault), and the talk's night log, moments and team-numbers tools (they write the talk's articles; they come back when the book's team has wakes to log).
- Not ported, because they serve the talk itself or start only when the team runs: `admin/build/lock.py` (froze parts of the talk before it was given), `admin/build/lane.py` (drains the editor's lane, see above), `admin/tools/workflow_deck.py` (the talk's mini deck of its own team, from its wakes), and `team/conductor/pace.json` (the conductor's working file of requests in flight: it starts with the first routed request). `team/<id>/HOLD.md` exists only while a hold is on.
- No Leanpub book, no cover; the PDF and EPUB build runs locally, not yet in CI.
- Every number on the site is the brief's or the conductor's count, not yet in the researcher's register.

## The index of the source (librarian, 30 October 2026)

- The librarian is staffed (session `session_01Kw9UwBgUFHEgwLsB3TrwA8`, key `sha256:e5768293c14e8cdc`), with its own hourly task at :09 London created at the editor's word.
- `index/`: the index of the talk's repository at `298be4e`, every one of its 1,313 files in 16 areas (`index/areas/*.md`, `index/index.json`), built by `index/tools/build_index.py` from a read-only clone; `index/after-the-day.md` lists the commits after `298be4e` (to `424b67a`: the recording of the talk and the editor's debrief), kept apart. Method and rounds in `index/README.md`.
- Read by hand so far: the root and the tools (30 of 1,313 files, `index/read.json`). Every other line is the tool's, marked `(machine)`.

## Security (security@book.the-ultimate-insider)

- Staffed 30 October 2026: session key in `team/security/key.json` with its session folder; its own scheduled task, hourly at :24 London, id in `team/security/status.json`.
- `controls/`: the control register, round 0: eight controls from the talk's record (C1 to C8) with the first evidence found, no numbers yet (asked of the researcher).
- `team/security/reviews/pki-agent-review.md`: the line-by-line review of the pinned key tool, started; four findings, low or information, for the editor first.
