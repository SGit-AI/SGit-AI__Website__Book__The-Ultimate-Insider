# What exists

What exists in this repository and on its site, kept current by whoever ships. A thing not listed here does not exist, whatever a brief or a page says.

## The site

- The site at https://the-ultimate-insider.book.sgit.ai, built by `admin/build/build.py` (the talk's build, ported) into `_site/`, gated by `admin/build/validate.py` (the talk's gate, ported), released and deployed by `.github/workflows/release.yml` (the talk's, unchanged). v0.1.0 released from `dev` on 30 October 2026.
- RC1, the book's first version, on its own page (`/rc1/`, linked from the home page): the PDF the editor printed on 30 October 2026 (294 pages), shown in the page and to download, with its hash. `admin/build/build.py` copies it from `team/conductor/rc1/pdf/` with the cover thumbnail; the companion PDF stays in the repository and is not on the page (its cards discuss where the leaked values are). The site build also copies `manuscript/resources/` to `book/resources/`.
- The book's pages: home, the book (the manuscript, its contents, the title candidates), the plan (dates and rounds), decisions (open and decided), the briefs (each published in full), sources, about. Built from `book.json`, `briefs/` and `manuscript/`.
- The admin section, the talk's: admin and engineering, the dashboard, wakes, commits and messages, releases, the team and each member's page, the roles, the schedule, the key register, and the sources of truth (what exists, the rules for agents, the corrections, onboarding, the wake protocol). The board, the mail and the public vaults pages are built only when `team/conductor/vaults.json` exists.
- Every page has a `.md` twin; `llms.txt`, `sitemap.xml`, `robots.txt`, `version.txt`, `book.json`, `admin/keys/index.json`, `admin/commits.json` and the release data are generated. The offline cache (`src/static/sw.js`, kill switch `sw.json`) is the talk's.

## The team's machinery (ported from the talk's repository at `298be4e`, 30 October 2026)

- `admin/tools/`: `start.py`, `banner.py`, `wake.py`, `vault_check.py` (its email check adapted: our agent addresses have a dot after the @), `vault_handover.py`, `pki-agent.mjs` with its sha256 pin and README, `qr.mjs`. `admin/build/agents.py`.
- `CLAUDE.md` (the talk's rules, rule for rule, then the book's), `team/conductor/WAKE.md`, `team/conductor/reviews/` (the four sub-agent briefs), `team/conductor/known-keys/` (the DC Vault Registry, carried over, to be re-confirmed by the editor).
- The conductor: staffed (this session, conductor@book.the-ultimate-insider), with its key published (`sha256:15762445fb34548e`), `ROLE.md`, `policy.json`, `status.json`, `schedule.json` (proposed), `ONBOARDING.md`, and the Cold-Read hand-off in `handoffs/`.
- The first batch, proposed with `ROLE.md`, `policy.json`, `status.json` and a slot: librarian, historian, security, researcher, storyteller, publisher. Their prompts are in `ONBOARDING.md`.

- **`comms/`**: the board and the mail in git; the conductor's notice and request in every member's mailroom (each member adds its own three paths to its policy).
- The manuscript build in the release job (`publishing/build_book.py`, the publisher's): every release publishes `/manuscript/the-ultimate-insider.pdf` and `.epub`; a failure warns and never stops the release.

## The book

- `book.json`: dates, rounds, phases, roles and decisions (S1 to S8 decided, Q2 to Q4 open).
- `briefs/2026-10-30/`: the editor's six brief files, as given.
- `manuscript/`: `Book.txt` and `about-this-edition.md`. No chapter: the plan is not signed.

## The historian's timeline (historian@book.the-ultimate-insider)

- `timeline/README.md`: the method for the timeline of 29 October (round 0): the record is the history reachable from `298be4e`, the day ends at `88b8f00` (18:45) and v0.1.209 `cb5b996` (18:46), UTC equals London that day, entries cite a commit or a file at `298be4e`, three spans kept apart, and ten candidate turning points to argue or drop in round 1. No timeline entries yet.
- `timeline/day/00.md` to `18.md`: the whole day, 00:16 to the last commit before 19:00; `timeline/after-1900.md` (to the 23:19 merge) and `timeline/after-the-day.md` (added after `298be4e`) kept apart, each entry with its commit or wake record; `timeline/unmerged.md`: the two commits of 18:48 outside the history of `298be4e`.
- `timeline/turning-points.md`: eight turning points argued, each with trigger, first evidence and what it is not; two candidates dropped.
- `team/historian/`: staffed 30 October 2026; key published; its own hourly task at :17 London.

## The claims register (researcher)

- The researcher: staffed (session_01Kw9UwBta1dcP9qBJUURLPZ), key published (`sha256:4e0287f6640d61f0`), its own scheduled task hourly at :32 London.
- `claims/register.json` and `claims/README.md`: the numbers in the briefs checked against the talk's log at `298be4e`, 21 claims (17 checked, 2 corrected, 2 open); then, at security's and the storyteller's requests, C022 to C028: the day's wake records and verdicts, the hold, the post-review findings, the talk's length, the part locks (none was ever applied) and the player port (15:07). 28 claims: 24 checked, 3 corrected, 1 open. Then the talk's own register (`evidence/claims/`, 320 claims) recounted, its three failed claims and the $17.4M slide registered (C029 to C031): 31 claims, 26 checked, 3 corrected, 2 open. Then graphs.sgit.ai read at the editor's request (`claims/graphs-sgit-ai.md`, C032 to C036): the first entries of the comparison set. 36 claims. Then a rerunnable command on every entry (`claims/appendix-a-commands.md`, for the book's Appendix A), C014 corrected, C037 added: 37 claims. Then graphs.sgit.ai's second pass and `claims/talk-claims-triage.md` (the talk's 80 claims placed on stage, C038), then matched to the talk's beats and the off-stage ones sorted (C039): 39 claims. Then $17.4M checked at source and the lessons brief's player priority corrected (C031, C040): 40 claims; both then settled with the historian's timeline (the 02:47 freeze). Then RC1's numbers reviewed against the register, and C011, C014, C018, C021, C023 corrected at the RC1 drafting's findings, C041 and C042 added: 42 claims. The researcher's board and mail are in `comms/`. Then, on 30 October at 13:02, the second session on the editor's second account (session_01Kw9UwBhzn98NK3Ydio5nEP, key `sha256:0f94386bc5e70a5e`, task every two hours at :32 London) took the role over and registered chapter 11b's dossier dates at source (C043 to C063) and corrected C040 again: 63 claims. The rest of the talk's claims and the market comparison set are not yet registered.

## The storyteller's chapter plan (storyteller@book.the-ultimate-insider)

- `chapter-plan/`: draft 5 of the chapter plan, **signed by the editor** (P0, 30 October 2026, about 10:00 UTC; RC1 is drafted from it) (drafts at 01:46 UTC and the 02:40, 03:40, 04:39 and 09:39 wakes): thirteen chapters and Appendix A (every number rerun from git), 49,200 words (drafts 1 to 3 said 48,200, a sum error), the workflow as the main thread with the talk's beats braided through it, the failure each chapter keeps, and for each chapter the register ids it may use (`claims/`), its index areas (`index/areas/`), its timeline hours and the historian's eight argued turning points (`timeline/`) and its controls (`controls/`); word budgets and drafting timings (`budget.md`); five open questions for the editor (`open-questions.md`, O1 to O5, in `book.json`).
- `team/storyteller/`: staffed 30 October 2026; key published (`sha256:edc67e3cc68b3b07`); its own hourly task at :39 London. Its `comms/` paths added at decision C10 (04:39 wake): its board in `comms/issues/storyteller/`, its mail in `comms/mail/storyteller/`; requests before that in `team/storyteller/requests/`.

## The publisher (publisher@book.the-ultimate-insider)

- Staffed 30 October 2026, key `sha256:88b9a9682c1b72e9`, its own hourly task at :47 London.
- `publishing/build_book.py`: a PDF (6 by 9 inches, via pandoc and headless Chromium) and an EPUB from `manuscript/` in the order of `Book.txt`, into `_site/manuscript/` (never committed). Run by CI in the release job since 30 October; the site serves `/manuscript/the-ultimate-insider.pdf` and `.epub`.
- `publishing/LEANPUB.md`: the editor's steps to create the Leanpub book from this repository, and the price options. No Leanpub book exists yet.
- `publishing/KDP.md`: the editor's steps on Amazon KDP for the ebook and the paperback, and what the PDF must still change for print. No KDP listing exists yet.
- `publishing/cover_size.py`: the paperback's full cover size and spine for the designer, from the PDF's page count.
- The build prints the words per manuscript file, the total and the PDF's page count (196 words, 3 pages on 30 October).
- The PDF embeds the manuscript's images (`manuscript/resources/images/`) and prints each figure on one page; the book targets Markua 0.30 (M1). Leanpub price decided (L1: $0 minimum, $19.99 suggested; L2: main). RC1 (sixteen files, 42 images, 217 pages) is on the publisher's branch, released once the site build copies the images.

## Not yet

- No member but the conductor is staffed; no scheduled task exists (the editor says go and sets the hours, Q2).
- No vaults, at the editor's word (30 October 2026): the board and the mail are `comms/` in git, the talk team's two layouts as folders (`comms/README.md`); the board and mail pages from those folders are not built yet. Not ported: the editor's voice lane (`pane.js`, `lane.py`, its own vault), and the talk's night log, moments and team-numbers tools (they write the talk's articles; they come back when the book's team has wakes to log).
- Not ported, because they serve the talk itself or start only when the team runs: `admin/build/lock.py` (froze parts of the talk before it was given), `admin/build/lane.py` (drains the editor's lane, see above), `admin/tools/workflow_deck.py` (the talk's mini deck of its own team, from its wakes), and `team/conductor/pace.json` (the conductor's working file of requests in flight: it starts with the first routed request). `team/<id>/HOLD.md` exists only while a hold is on.
- No Leanpub book, no KDP listing, no cover.
- Every number on the site is the brief's or the conductor's count, not yet in the researcher's register.

## The index of the source (librarian, 30 October 2026)

- The librarian is staffed (session `session_01Kw9UwBgUFHEgwLsB3TrwA8`, key `sha256:e5768293c14e8cdc`), with its own hourly task at :09 London created at the editor's word.
- `index/`: the index of the talk's repository at `298be4e`, every one of its 1,313 files in 16 areas (`index/areas/*.md`, `index/index.json`), built by `index/tools/build_index.py` from a read-only clone; `index/after-the-day.md` lists the commits after `298be4e` (to `424b67a`: the recording of the talk and the editor's debrief), kept apart. Method and rounds in `index/README.md`.
- Read by hand: every area, round 1 complete (842 of 1,313 files, all that are not images; the images are listed by folder: in those areas, every file but the images; `index/read.json`). Every other line is the tool's, marked `(machine)`.

## Security (security@book.the-ultimate-insider)

- Staffed 30 October 2026: session key in `team/security/key.json` with its session folder; its own scheduled task, hourly at :24 London, id in `team/security/status.json`.
- `controls/`: the control register, round 0: eight controls from the talk's record (C1 to C8) with the first evidence found, no numbers yet (asked of the researcher).
- `team/security/reviews/pki-agent-review.md`: the line-by-line review of the pinned key tool, nearly complete; fifteen findings, one medium (`keyfile` prints private keys, found first by the Cold-Read team), for the editor first.
- `controls/` now C1 to C10, counts cited by the researcher's claim ids (C022 to C025). Security's `comms/` paths are in its policy since decision C10 (the session refused the same edit before it); its board is `comms/issues/security/`.
- `index/cold-read/`: the Cold-Read repository indexed read only at `0dc6854` (30 October, 10:05 UTC), every file, lines the tool's. `index/tools/check_sources.py`: checks the paths, commits and register ids a chapter's sources name; run on RC1 as it lands.

## The PDF lab's design (designer@book.the-ultimate-insider)

- `lab/README.md`: the lab's visual language as rules (A4, twelve columns with a margin rail, RC1's palette, a 9 pt floor, one footer, one experiment header with keep, change and drop boxes).
- `lab/characters/`: the cast, three drawings (the conductor, security, the hold) and their rules; their lines are still placeholders, for the storyteller.
- `lab/tools/build_lab.py`: builds `lab/pdf/the-ultimate-insider-lab.pdf` from `lab/experiments/*/`, refusing text under 9 pt, overflowing pages and a wrong page count; writes `lab/pdf/SHA256SUMS`.
- `lab/experiments/01-designer-visual-language/`: LAB 01, the first experiment; the PDF is 4 pages with the cover (30 October 2026). Not on the site yet.

## The PDF lab, ruv.sgit's runs (ruv.sgit@book.the-ultimate-insider)

- Staffed 30 October 2026 at the editor's word (`book.json` X1): role and policy adopted from the conductor's draft into `team/ruv-sgit/`, session key `sha256:301885fb2fd5a83e` with its session folder; its own scheduled task, every two hours at :54 London, id in `team/ruv-sgit/status.json`.
- `lab/experiments/01-ruv-the-building-three-frames/`: the talk's M01 (at `5d13d72`) frozen on its own clock at three times, one A4 page (`page.pdf`), rebuilt by its `tools/make.sh`; run recorded in `lab/runs/20261030T1303Z-ruv-01-the-building.*`, no vault, no Ruflo hive (not available in the session). With the designer for the lab PDF and security for review; the editor's paper verdict to come.
