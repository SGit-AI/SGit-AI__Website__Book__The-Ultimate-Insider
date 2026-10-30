# The talk's site, page by page

Kept by librarian@book.the-ultimate-insider, at the conductor's request of 30 October 2026 (`comms/mail/mailroom/librarian/conductor__007-talk-site-study.eml`), relaying the editor's ask of about 13:08 UTC: go through the talk's website properly, every page, the admin side above all, and say what was made, what works and what does not. First pass, 30 October 2026, 16:13 to 16:31 UTC. The designer turns it into a short PDF debrief; the screenshots in `shots/` are for that.

## The best things on it, so far

The request asks for twenty. These are the ones I have looked at, in a screenshot or the page itself, in this first pass; the list grows to twenty once each animation has been watched in motion, not only at its first frame. In the order a reader of the book would meet them.

1. **The home page's three circles** (`/`, `shots/index.jpg`): the insider, the infrastructure and the decision as a Venn diagram, with "the scenario" in the overlap. The talk's whole argument in one picture.
2. **The talk as 58 web pages with a player** (`talk/index.html`, `talk/player.html`): every slide a page that animates, a timer, presenter notes behind one key, a slide grid. The deck is a website, read by anyone.
3. **"Three known problems. One perfect storm."** (`talk/slides/three/`): the opening slide, the circles drawn one at a time.
4. **"A reasoning engine in a loop, with tools"** (`talk/slides/loop/`): the definition of an agent as three boxes on a circle, sourced on the slide to Anthropic (December 2024) and Simon Willison (June 2025).
5. **The dashboard** (`admin/dashboard.html`): the team's state read from its own files: a live London clock, any hold (it still shows the night's last hold, "the editor's usage limit is at 95%"), and what waits on the editor. The book's chapter 1 is this panel.
6. **The public vaults page** (`admin/vaults.html`): each vault's read key as text and as a QR code, under a red box: "Every file in these vaults is public, forever."
7. **The key register** (`admin/keys.html`): every member's fingerprint, encryption key and session, with the rule "the push is the authorisation".
8. **Who builds this site** (`team/index.html`): one card per member, its role, its last wake in one line, its key and how many paths it may write.
9. **Fourteen explained animations by ruv-sgit** (`ruv-sgit/*/`, each with an `explainer.html`): the blast radius, mandate against grant, the lethal trifecta, five published examples in the same chart, and ten more, each with a frame-by-frame explanation and the data it was drawn from.
10. **"Meet the team"** (`motion/meet-the-team/`, M03): nine agents and one editor as an orbit, the prelude to part 1.
11. **The storyteller's Wardley maps** (`talk/slides/maps/`): pioneers, settlers and town planners, with "positions, not measurements" on the slide.
12. **The editor approves each agent's policy, item by item** (`studio-ports/abp-review/`): the review page the editor used for ruv-sgit's policy, as a slide.
13. **One action's journey** (`studio-ports/journey/`): an agent's request, its policy row, the decision and its receipt, in three acts: allowed, denied, sent to a human.
14. **The studio** (`studio/index.html`): a brief per part of the argument, several versions side by side, the best promoted into the deck, with a programme, reviews and techniques.
15. **Two long articles with the night in pictures**: `articles/the-night-hour-by-hour.html` (88 images) and `articles/the-talk-as-given.html` (58 images; added after the day, `a9c0b49`).

## What works and what does not

303 pages reachable from the home page (`pages.md`, by section). 298 load with content and no error in the browser. Five do not, all where a page depends on another service:

- `team/board.html` and `admin/mail.html` read the team's vaults live from the vault server and did not finish within 30 seconds; the mail page asked for a vault reference the server no longer has (404).
- `talk/slides/live/vault-risk-mandate/` embeds a page on sgit.ai that the browser blocked as cross-origin.
- `talk/player.html` asks for `talk/engine/locked/locks.json`, which is not published (404); the player still runs.
- `talk/slides/live/sharness-playground/` embeds sharness.ai, which calls a location service the browser blocked; the playground still shows.

Four more pages (the dashboard, the wakes, the studio's briefs, one lab version) show a panel from the GitHub API, which refused this crawl (rate limit, from this container); that is likely the crawler's address, not the site.

## Method

- **Not built locally.** The request asks for a local build at `298be4e`. This session's permission check refused to run the talk repository's own build script (code from another repository), so I did not work round it. Instead: the published site, which the editor also named, crawled with a Playwright script of my own (`crawl.json` is its output), and each page mapped to its source file in the talk's repository at `298be4e`.
- **What the published site is.** Release v0.2.1, the talk's repository at `424b67a`: `298be4e` plus three commits added after the day (`index/after-the-day.md`). `pages.md` marks a source "(after)" when it arrived after the day.
- **Verdicts** are mechanical (status, content, browser errors); whether a page is good is in the list above, and grows next wake.
- **Screenshots**: 90, the first screen of each page at 1280 by 800, JPEG, in `shots/`, named by path. Agent pages under `team/<id>/`, the studio's lab and review versions, and the admin documents are listed, not shot.
- `visuals.md`: the 63 slides, animations, maps and ports a book could reuse or redraw, with source and last change. Reuse waits on the licence question (the talk's repository is Apache-2.0, the book CC BY 4.0, and some images carry third-party credits).

## Still to do

The twenty, watched in motion; the admin pages' content read one by one (dashboard, wakes, commits, releases, schedule); the `team/<id>/` pages; the studio's lab versions.
