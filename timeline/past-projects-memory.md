# The editor's past projects as the team's memory

Kept by historian@book.the-ultimate-insider. Written 4 November 2026 at the conductor's request (`conductor__038`), for the editor's callout "his past projects as memory" (brief 2026-11-04 19). Read only, from the talk's repository at `cb5b996` (the last release of the day, 18:46); the pages named are public. **The numbers are the historian's proposals; the researcher registers them.** All times UTC.

## The short answer

The record shows the editor's past projects used four different ways, and they are kept apart below because they say different things. In order of how directly they speak: **he named seven pages in his own words** (almost all in his first brief, at 00:40); **agents captured 273 pages of his sites as evidence**, each time-stamped, across eight of the day's hours; **63 pages were used in the team's own files** (briefs, notes, pages, slides) beyond those captures; and **the team's first rules and tools were carried over from his earlier projects**, dated from the first minute. Nothing here says which pages an agent "read" without leaving a trace; git shows the text of what was written and what was captured.

## The count, corrected

The conductor's "about 2,666 lines" is **2,666 mentions of `newsroom.sgit.ai` on 2,525 lines** (`git grep -o` against `git grep`), and that includes its sub-sites such as `php.oct.2026.newsroom.sgit.ai`. All of `sgit.ai` is on 3,881 lines. Read as distinct pages (host and path, fragments and queries dropped) the repository holds **1,116 pages on 35 hosts**, 599 of them on `newsroom.sgit.ai` itself and 274 on `php.oct.2026.newsroom.sgit.ai`. Of the 4,617 mentions added across the day's commits, 3,765 sit in the researcher's evidence files (capture lists and manifests): most "lines" are repeats of a capture list, as the conductor expected.

## One: the pages he named in his own words

His quoted words (his first brief, and one later brief) name seven pages:

| Time | Page | Where |
|---|---|---|
| 00:40:50 | `sgit.ai` (the guidance for building the `*.sgit.ai` sites) | `BRIEF.md`, his request |
| 00:40:50 | `ruv.sgit.ai` ("what we did at ruv.sgit.ai as the UX and type of presentation and dynamic infographics") | `BRIEF.md` |
| 00:40:50 | `newsroom.sgit.ai` and `php.oct.2026.newsroom.sgit.ai` ("the kind of multi agent team we will be creating here") | `BRIEF.md` |
| 00:40:50 | `newsroom.sgit.ai/articles/ultimate-insider-three-collisions` (the article the talk is built on; both its `.html` and `.md`) | `BRIEF.md` |
| 16:32:22 | `pki.sgit.ai` | the conductor's brief of his words on the work section |

## Two: the pages agents captured as evidence

The researcher's source manifest (`evidence/sources/manifest.json`) records, for every captured page, its time, its HTTP status and a SHA-256 of what was stored. **273 of its 696 sources are pages of the sgit.ai network, all returned status 200.** This is the record's best evidence of "an agent read it". Captured at (UTC hour): 01 (77), 03 (18), 10 (5), 14 (13), 15 (9), 16 (3), 17 (111), 18 (37). By host: `newsroom.sgit.ai` 70, `sgit.ai` 42, `refs.php.oct.2026.newsroom.sgit.ai` 33, `pki.sgit.ai` 32, `php.oct.2026.newsroom.sgit.ai` 29, `abp.sgit.ai` 24, then team, games, nhi, open-source, updates and ux pages.

The manifest names what each batch was for (its `recorded_by` tag):

| Captured | Count | For | Tag |
|---|---|---|---|
| 01:50:05 to 01:50:41 | 20 of his newsroom articles in 36 seconds, among them `ultimate-insider-three-collisions` (01:50:09), two minutes before the researcher's first commit (01:52:10) | the researcher's map of ideas | `newsroom-ideas` (the tag `sgit-php-ideas` holds 53 more) |
| 01:50:23 | `nfrs.sgit.ai` and its `llms.txt` | the same reading | in the sources list |
| 14:25:32 to 14:26:10 | four newsroom articles on behaviour policies (application, process, three policies for an agent, approve at altitude) | the storyteller's requests R4 to R9 | `story-r4-r9` (13) |
| 16:21:33 to 16:21:34 | "Explorer coding", "The agent team as it runs", "The citizen developer is good news" | the storyteller's request S5 | `story-s5` (3) |
| 17:15 on | the newsroom's pages | studio's showcases of the newsrooms | `studio-work-newsrooms` (54) |
| through the afternoon | pki, the SHarness series, open source and investors, the capability pages | studio's showcases and the studio's pieces | `studio-work-pki` (36), `studio-work-sgit-sharness` (21), `studio-open-source-investors` (37), `studio-e02-e09` (17 and 5) |

Forty-nine of the captures are articles on `newsroom.sgit.ai` itself (three more are on its PHP October sub-site), each with its title in the manifest. The first batch is 79 sources in the 36 seconds from 01:50:05, 20 of them newsroom articles.

## Three: pages used in the team's own files

Beyond capture lists, **63 distinct pages** appear in a brief's text, a member's own note, a page or a slide of the site. First used by: dev 18, studio 14, researcher 10, deck 8, conductor 7, ruv-sgit 5, designer 1. By UTC hour: 00 (14, dev's first pass), 01 (9), 02 (3), 04 (1), 07 (1), 10 (2), 14 (4), 15 (7), 16 (2), 17 (7), 18 (13). The newsroom pages among them, with where each was first used:

- 00:40:50, dev: `ci-owns-the-version` on a page of the first pass (and in the workflow's first line, below); the newsroom's front page and the PHP October site's front page, the two most mentioned pages of the whole day (835 and 437 mentions), both named in his brief.
- 15:07:08, dev: `the-scripted-talk`, in the player's port.
- 15:44:56, deck: the PHP October site's team page (30 mentions), on a studio page.
- 17:03:28, conductor: `api.newsroom.sgit.ai`, in a brief.
- 18:20:06, studio: `where-to-invest-in-sgit` and `the-fork-next-door`, on the two showcases built that minute.
- 18:23:50, researcher: `investor-sgit-ai`, `what-open-source-is-and-is-not`, and three pages of the PHP October site (a research piece, a pulse page and a state page), in its notes for part two.

## Four: what the team carried over from his earlier projects

Dated from commits and role pages. These are the clearest cases of "I'm benefiting from all those past projects":

| Time | Commit | What | His project |
|---|---|---|---|
| 00:40:50 | `1f7c633` | dev's release workflow opens with "CI owns the version" and links the article | newsroom: `ci-owns-the-version` |
| 00:44:37 | `97b98d9` | the conductor's `CLAUDE.md` "modelled on web-summit.sgit.ai"; the roster "the shape of web-summit.sgit.ai's roster, with two fields added" | web-summit.sgit.ai |
| 00:51:53 | `20ab1a3` | deck's role (dev's page carries the same line): "Never type a version number: agents racing for release numbers is how the newsroom lost releases on 27 October 2026"; "The editor's abstract and the newsroom article set the argument" | newsroom |
| 00:53:45 | `a3a4807` | "Adopts the PHP newsroom's wake banners (its brief of 27 October 2026)" | PHP October newsroom |
| 01:35:33 | `ecc048e` | "This project's version of the newsroom conductor's guide, published as an article" | newsroom |
| 15:07:08 | `3314ffe` | "the player, ported from ruv.sgit.ai" | ruv.sgit.ai |
| 15:25:40 | `f00734f` | briefs for studio: "ports from ruv.sgit.ai" | ruv.sgit.ai |
| 15:40:21 | `c3ce566` | "first two ports from ruv.sgit.ai: the ABP slide and studio v4, the policy gate" | ruv.sgit.ai |

## How the counts were made, and which are registered

The script is `team/historian/tools/past_projects_scan.py` (read only, offline; its header states the rule: a page is a host ending in `sgit.ai` and a path, scheme, fragment and query dropped, a trailing slash not folded, case not folded). Run against the talk's repository it gives exactly the figures above. The researcher registered what it could rerun as **C127**: the manifest figures (696 sources, 273 on sgit.ai, all status 200, by hour), the first batch, and the carried-over list. **The book prints C127's figures only.** Not registered, and so not for print: the 1,116 pages on 35 hosts (read from the history, every page ever added; read from the final tree the same rule gives 1,123 on 35, and 1,117 with trailing slashes folded; the researcher's own rule gives 1,053 on 34, which I could not match, and have asked for its command), the 4,617 and 3,765 mentions, and the 63 used pages. On sites: the register's method (`git grep -o` for the name before `sgit.ai`, C126) gives **24 names**, of which its "sixteen" is the top sixteen (the command ends in `head -16`); my 35 hosts tell sub-domains such as `php.oct.2026.newsroom.sgit.ai` apart from the newsroom. The 49 newsroom article captures is the researcher's figure and is right: my first count of 52 used a substring match that also took three articles on the PHP October sub-site.

## The 63 pages used in the team's own files

Each page's first use outside the researcher's capture lists, by the rule above (the editor's quoted words, a brief's text, a member's own note, a page of the site, a slide or the talk's data).

| First used | By | In | Page |
|---|---|---|---|
| 00:40:50 | dev | a slide or the talk's data | `the-ultimate-insider.presentation.sgit.ai/` |
| 00:40:50 | dev | a page of the site | `newsroom.sgit.ai/articles/ci-owns-the-version.html` |
| 00:40:50 | dev | the editor's quoted words | `sgit.ai/` |
| 00:40:50 | dev | the editor's quoted words | `ruv.sgit.ai/` |
| 00:40:50 | dev | the editor's quoted words | `newsroom.sgit.ai/` |
| 00:40:50 | dev | the editor's quoted words | `php.oct.2026.newsroom.sgit.ai/` |
| 00:40:50 | dev | the editor's quoted words | `newsroom.sgit.ai/articles/ultimate-insider-three-collisions.html` |
| 00:40:50 | dev | the editor's quoted words | `newsroom.sgit.ai/articles/ultimate-insider-three-collisions.md` |
| 00:40:50 | dev | a page of the site | `sgit.ai/docs/guidance/repositories.html` |
| 00:40:50 | dev | a page of the site | `nhi.sgit.ai/` |
| 00:40:50 | dev | a page of the site | `pki.sgit.ai/` |
| 00:40:50 | dev | a page of the site | `nfrs.sgit.ai/` |
| 00:40:50 | dev | a page of the site | `sgit.ai/demos/vaults/kit-bag/index.html` |
| 00:54:32 | dev | a member's own note | `sgit.ai/llms.txt` |
| 01:08:25 | ruv-sgit | a page of the site | `ruv.sgit.ai/articles/how-it-was-made.html` |
| 01:08:25 | ruv-sgit | a page of the site | `ruv.sgit.ai/articles/the-studio.html` |
| 01:08:25 | ruv-sgit | a page of the site | `ruv.sgit.ai/studio/index.html` |
| 01:08:25 | ruv-sgit | a page of the site | `ruv.sgit.ai/articles/studio-setup-brief.html` |
| 01:08:25 | ruv-sgit | a member's own note | `dev.sgraph.sgit.ai/` |
| 01:09:58 | conductor | a member's own note | `web-summit.sgit.ai/` |
| 01:19:26 | dev | a page of the site | `sgit.ai/assets/vault-embed.js` |
| 01:27:10 | conductor | a member's own note | `web-summit.sgit.ai/keys/sha256-956934e47063ceaa.json` |
| 01:27:10 | conductor | a member's own note | `pki.sgit.ai/send/` |
| 02:52:11 | deck | a page of the site | `abp.sgit.ai/` |
| 02:52:11 | deck | a page of the site | `abp.sgit.ai/data/barriers.json` |
| 02:52:11 | deck | a page of the site | `abp.sgit.ai/examples` |
| 04:45:26 | designer | a member's own note | `presentation.sgit.ai/` |
| 07:54:47 | dev | a page of the site | `sgit.ai/assets/vault-ui-embed.js` |
| 10:14:39 | researcher | a member's own note | `what-can-it-do.games.sgit.ai/data/primitives.json` |
| 10:14:39 | researcher | a member's own note | `what-can-it-do.games.sgit.ai/data/` |
| 14:07:04 | conductor | a brief's text | `ux.sgit.ai/` |
| 14:07:04 | conductor | a brief's text | `ruv.sgit.ai/articles/the-talk-player.html` |
| 14:07:04 | conductor | a brief's text | `ruv.sgit.ai/llms.txt` |
| 14:28:47 | dev | a member's own note | `sgit.ai/api/append-lanes.md` |
| 15:07:08 | dev | a slide or the talk's data | `newsroom.sgit.ai/articles/the-scripted-talk` |
| 15:40:21 | studio | a page of the site | `ruv.sgit.ai/talk/slides/abp/index.html` |
| 15:40:21 | studio | a page of the site | `ruv.sgit.ai/studio/v4/index.html` |
| 15:40:21 | studio | a page of the site | `ruv.sgit.ai/data/abp.json` |
| 15:40:21 | studio | a page of the site | `ruv.sgit.ai/data/rules.json` |
| 15:40:21 | studio | a page of the site | `ruv.sgit.ai/data/report.json` |
| 15:44:56 | deck | a page of the site | `team.php.oct.2026.newsroom.sgit.ai/` |
| 16:18:57 | studio | a page of the site | `ruv.sgit.ai/ruv-sgit/define/journey/index.html` |
| 16:18:57 | studio | a page of the site | `ruv.sgit.ai/data/state-abp.json` |
| 17:03:28 | conductor | a brief's text | `api.newsroom.sgit.ai/` |
| 17:20:06 | studio | a page of the site | `pki.sgit.ai/people/how.html` |
| 17:21:29 | deck | a slide or the talk's data | `what-can-it-do.games.sgit.ai/` |
| 17:21:29 | deck | a slide or the talk's data | `sgit.ai/demos/index.html` |
| 17:21:29 | deck | a slide or the talk's data | `sgit.ai/demos/vaults/risk-mandate/index.html` |
| 17:25:36 | deck | a slide or the talk's data | `the-ultimate-insider.presentation.sgit.ai/articles/how-this-talk-was-b` |
| 17:47:28 | studio | a page of the site | `the-ultimate-insider.presentation.sgit.ai/ruv-sgit/policy-review.html` |
| 18:11:59 | studio | a page of the site | `the-ultimate-insider.presentation.sgit.ai/admin/wakes.html` |
| 18:11:59 | studio | a page of the site | `the-ultimate-insider.presentation.sgit.ai/team/ruv-sgit/index.html` |
| 18:20:06 | studio | a page of the site | `newsroom.sgit.ai/articles/where-to-invest-in-sgit.html` |
| 18:20:06 | studio | a page of the site | `newsroom.sgit.ai/articles/the-fork-next-door.html` |
| 18:23:50 | researcher | a member's own note | `newsroom.sgit.ai/articles/investor-sgit-ai.html` |
| 18:23:50 | researcher | a member's own note | `investor.sgit.ai/` |
| 18:23:50 | researcher | a member's own note | `newsroom.sgit.ai/articles/what-open-source-is-and-is-not.html` |
| 18:23:50 | researcher | a member's own note | `php.oct.2026.newsroom.sgit.ai/articles/dream-research-rooted-25-server` |
| 18:23:50 | researcher | a member's own note | `open-source.sgit.ai/index.html` |
| 18:23:50 | researcher | a member's own note | `refs.php.oct.2026.newsroom.sgit.ai/pulse/cve-2026-102764/` |
| 18:23:50 | researcher | a member's own note | `updates.php.oct.2026.newsroom.sgit.ai/views/state/v1/` |
| 18:23:50 | researcher | a member's own note | `sgit.ai/investors/index.html` |
| 18:34:32 | studio | a page of the site | `open-source.sgit.ai/` |

## coding.sgit.ai and nfrs.sgit.ai

**Neither is in the brief.** `BRIEF.md` names `sgit.ai`, `ruv.sgit.ai`, `newsroom.sgit.ai` and `php.oct.2026.newsroom.sgit.ai`; it points at "the guidance on sgit.ai for how to create these *.sgit.ai websites". Where they enter:
- **`nfrs.sgit.ai`:** first in dev's own first pass, at 00:40:50, on the sources page ("On this network: nhi.sgit.ai ... pki.sgit.ai ... nfrs.sgit.ai"); then the conductor's `REALITY.md` at 00:44:37, which lists "a row on nfrs.sgit.ai" among the things that did not exist yet; then the researcher's lists at 02:10:56; and the researcher captured `nfrs.sgit.ai` and its `llms.txt` at 01:50:23. Two pages in all.
- **`coding.sgit.ai`:** once, at 17:35:57, in the researcher's summary of what a newsroom page says ("... quality from coding.sgit.ai, non-functional ..."), among the studio's newsroom evidence. It was never captured and never used.

## What the record cannot show

- **Reading that left no trace.** An agent may have read a page and written nothing; git has the capture manifest (273 pages) and what was written, nothing else. The capture times are the researcher's own.
- **What a page was "used for" beyond where it was written.** The "for" column is the manifest's own tag or the file the page first appears in, not a judgement.
- **The projects themselves.** The newsroom's articles are not in this repository; their content is only as the team captured or quoted it.

## How to reproduce

Counts: `git grep -h -o 'newsroom\.sgit\.ai' cb5b996 | wc -l` (2,666) and `git grep -h 'newsroom\.sgit\.ai' cb5b996 | wc -l` (2,525). Distinct pages and where each first appears: `git log -p --reverse -U0 -G 'sgit\.ai' cb5b996`, reading the added lines for `sgit.ai` hosts and paths (1,116). Captures: `git show cb5b996:evidence/sources/manifest.json`, the entries whose `url` has `sgit.ai`. Inherited patterns: the commits named, `git show <hash>`.
