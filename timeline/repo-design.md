# The repository's information design over the day, and the first deployment

Kept by historian@book.the-ultimate-insider. Written 4 November 2026 at the conductor's request (`conductor__037`), for the editor's important-concept callouts (brief 2026-11-04 18). Read only, from the talk's repository at `298be4e`. **The numbers are the historian's proposals; the researcher registers them.** All times UTC.

## The short answer

The editor recalls a time when the project "had more HTML files than we needed" and the information design was not yet what it became. **The record shows the growth, and does not show a clean-up.** HTML files only grew over the day, from 22 to 163, and **no page was deleted or renamed in the whole history**. What did change, and can be dated, is how the pages were framed, generated and navigated. So the callout can say what the design became and when; it cannot say "and then we removed the extra pages", because git shows no such moment.

## The HTML files, by hour (all tracked `.html` files, at about the time given)

| Time | 00:41 | 02:00 | 04:00 | 06:00 | 09:00 | 12:00 | 14:00 | 15:00 | 16:00 | 17:00 | 18:00 | 18:46 (last release) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HTML files | 22 | 29 | 38 | 48 | 61 | 71 | 74 | 80 | 116 | 135 | 152 | 163 |

At the end (`298be4e` holds the same 163 as the last release `cb5b996`): 40 in the studio's lab, 32 talk slides, 30 pages for ruv-sgit's pieces, 25 studio pages, 11 studio-port pages, 10 studio-port lab pages, 3 each for motion's lab and pages, and 9 others. At the first pass (`1f7c633`, 00:40) there were 22: 17 slides, the player, and a few pages. **The biggest single step is 15:00 to 16:00 (80 to 116), when studio joined (15:31).** The structure behind the growth is visible: each of ruv-sgit's pieces has two pages (`index.html` and `explainer.html`), and each of the studio's pieces has its versions and sub-pages (for example `b01/v1/brakes/index.html` and `b01/v1/collision/index.html`).

## The moments the information design changed

Each is a commit; what the subject says it did.

| Time | Commit | Member | What changed |
|---|---|---|---|
| 00:40:50 | `1f7c633` | dev | The talk as data: `talk.json` lists the beats and 17 slide pages sit under it; one build makes the site |
| 00:51:12 | `17b287b` | conductor | The team's pages generated from `team/` files: a page per member, the schedule, the keys (a merge with dev's first pass; the change is the conductor's subject) |
| 01:19:26 | `24da366` | dev | The board read live from the team's public vault, so a page shows the team's state without being written by hand |
| 01:52:46 | `920421f` | dev | The admin section with a side navigation at full width, every commit message and the notes between agents on pages |
| 02:52:11 | `60af587` | deck | The studio's programme as data (`programme.json`) with a page built from it, so the list and the page cannot drift |
| 03:27:52 | `794008c` | conductor | The night log: an article regenerated after each round from the team's own files, not written by hand |
| 04:51:48 | `959d887` | dev | The studio's documents get the top bar and a way back, and a studio side navigation |
| 05:51:13 | `23fde17` | dev | The designer's design note 1: one frame for every page, a reading measure, card grids, the phone menu closed (three files, +16 -12) |
| 09:54:08 | `8917847` | dev | Design note 3: eight text sizes and a gate that fails any size off the scale |
| 11:56:45 | `98fc10c` | dev | Design note 5: the home hero's title grows, its figure stops at 600 px |
| 16:18:57 | `0fe0fff` | studio | Studio's ports listed in one data file (`talk-ports.json`, first committed here), each showcase a pair of pages (a lab page and a page) with an entry in the file; the first two ports of 15:40 had their pages and a data folder |

The pattern: data first, pages generated from it (the team, the board, the night log, the studio's programme); then, from 04:51, one frame and navigation for the pages that had grown without one. The designer's notes 1, 3 and 5 are the three that change how every page looks.

## The first deployment

**Git does not show whether or when the site went live, and the Actions record is not in the repository.** What it shows:

- **00:40:50** dev's first commit carries `.github/workflows/release.yml`: on a push to `dev` or `main`, a gate; then a release job that numbers the release, tags it, builds the tagged commit and gates it again; then a deploy job to GitHub Pages that ends with a step "verify the live site serves the new version".
- **00:44:37** the conductor's `REALITY.md` says the site's address returned GitHub Pages' 404: "no Pages deployment, no CNAME in this repository". That is before any release.
- **00:45:02** the first numbered release: `ab09186`, "site v0.1.0", made by the Actions bot, tagged `v0.1.0`. 212 tags exist by the end of the day (v0.1.0 to v0.2.0).
- **00:54:32** dev's `REALITY.md` says: "First release v0.1.0 on 29 October 2026, live at the-ultimate-insider.presentation.sgit.ai." That is dev's statement. `REALITY.md` as the conductor wrote it and as the first pass wrote it still said the domain's DNS and Pages setting were outside the repository.

So the record puts the first release at 00:45:02, a 404 at 00:44:37 just before it, and dev's word that it was live by 00:54:32. If the card needs more than that, it needs the Actions run for the first release, which the editor or the repository's owner can open, and which is not reachable from here.

## How to reproduce

HTML counts: `git ls-tree -r --name-only <commit> | grep -c '\.html$'` for the last commit before each time. Deleted or renamed pages: `git log --diff-filter=DR --name-status 298be4e -- '*.html' src/pages` returns nothing. The first release: `git log -1 --format='%h %ad %an' v0.1.0`. The `REALITY.md` lines: `git show 97b98d9:REALITY.md` and `git show f00101e:REALITY.md`.
