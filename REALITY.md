# What exists

What exists in this repository and on its site, kept current by whoever ships. A thing not listed here does not exist, whatever a brief or a page says.

## The site (from site v0.1.0)

- **The site** at https://the-ultimate-insider.book.sgit.ai, built by `admin/build/build.py` (Python standard library only) into `_site/`, gated by `admin/build/validate.py`, released and deployed by `.github/workflows/release.yml`. The same pattern as the talk's site at commit `298be4e`.
- **Pages**: home, the book (the manuscript, its contents and the title candidates), the plan (dates and rounds), the team (the proposed roles), decisions (open and decided), the briefs (each published in full), sources, about, the release history, and the sources of truth below. Every page has a `.md` twin; `llms.txt`, `sitemap.xml`, `robots.txt` and `version.txt` are generated.
- **`book.json`**: the book's dates, rounds, phases, proposed roles and decisions, from the briefs. The plan, team, decisions and book pages are built from it, and it is published at `/book.json`.
- **`briefs/2026-10-30/`**: the editor's six brief files, as given.
- **`manuscript/`**: `Book.txt` (the order Leanpub builds in) and one file, `about-this-edition.md`. No chapter is written: the plan is not signed.

## Not yet

- No team member is staffed: no `team/` folders, no schedule, no keys, no wakes, no `start.py` or `banner.py`. The roles on the team page are proposals.
- No Leanpub book, no PDF or EPUB build, no cover.
- The blind repository is not set up from here, and never written into from here.
- Every number on the site is the brief's, not yet re-checked by a researcher.
