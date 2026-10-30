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

## Not yet

- No member but the conductor is staffed; no scheduled task exists (the editor says go and sets the hours, Q2).
- Not ported yet, because each needs something only the editor can create: the team's two public vaults (and so the board, the mail, the vaults page, vault handovers), the editor's voice lane (`pane.js`, `lane.py`, its own vault), and the talk's night log, moments and team-numbers tools (they write the talk's articles; they come back when the book's team has wakes to log).
- Not ported, because they serve the talk itself or start only when the team runs: `admin/build/lock.py` (froze parts of the talk before it was given), `admin/build/lane.py` (drains the editor's lane, see above), `admin/tools/workflow_deck.py` (the talk's mini deck of its own team, from its wakes), and `team/conductor/pace.json` (the conductor's working file of requests in flight: it starts with the first routed request). `team/<id>/HOLD.md` exists only while a hold is on.
- No Leanpub book, no PDF or EPUB build, no cover.
- Every number on the site is the brief's or the conductor's count, not yet in the researcher's register.
