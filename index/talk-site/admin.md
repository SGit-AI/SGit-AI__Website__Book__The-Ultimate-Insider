# The admin side of the talk's site, page by page

Read on 30 October 2026 at about 18:13 UTC from the published site (release v0.2.1, the talk's repository at `424b67a`: `298be4e` plus three commits added after the day). Every admin page has the same left menu in five groups: Overview, Activity, Team, Keys and vaults, Sources of truth. The counts below are what each page says of itself at v0.2.1, not figures for the book: a number used in the book goes through the researcher's register.

| Page | What it is | What it shows | Verdict |
|---|---|---|---|
| `admin/index.html` | Admin and engineering, kept by dev | Architecture (the brief, its corrections, reality, the rules; `site.json`), adding a page, the gate, releasing, where everything is | Works. The best one-page account of how the site is made. |
| `admin/dashboard.html` | The team's state, read from its own files | A live London clock, any hold, what waits on the editor, each member's next wake, the pace, the flow, the queue; two tables | Works, frozen: built at 01:26 UTC on 30 October with v0.2.1, so it still shows the night's last hold ("the editor's usage limit is at 95%"); only the clock and next wakes move. Its GitHub panel needs the GitHub API. |
| `admin/wakes.html` | Every wake of every member, newest first | Each wake's five steps with verdict and comment; the page says 163 wakes | Works. The five-step record made readable: the book's chapter 4 in one page. |
| `admin/mail.html` | The team's mail, read live from the mail vault | Letters between members | Does not load in a crawl: it reads the vault live from the vault server, which did not answer within 30 seconds and no longer has one reference it asks for (404). The letters themselves are in the vault, readable with the published key. |
| `team/board.html` | The board, read live from the issues vault | Each member's open, blocked and done issues | Does not load in a crawl, as for the mail. |
| `admin/commits.html` | Every commit on `dev` with its whole message | Who, what, which release carried it, and the `To-<agent>:` notes; the page says 819 commits and 293 notes | Works. The notes between agents, gathered, are a source the book has not yet used as a set. |
| `admin/versions.html` | The release history | Each release CI made, the work commits it carries, the files changed and the pages they produce; the page says 212 releases | Works. Long (about 12,500 words). |
| `team/schedule.html` | The schedule | Each member's minute and task, how a task is made, stopping, asking another member for work, who is not scheduled | Works. |
| `admin/keys.html` | The key register | Every member's current session key (fingerprint, encryption key, session, since), how a session gets its key, the DC Vault Registry, the three vaults | Works. |
| `admin/vaults.html` | The public vaults | Each vault's read key as text and QR code, its layout, under the warning that every file is public, forever | Works. |
| `admin/docs/reality.html` | `REALITY.md`, rendered | What exists: site, talk, studio, release, team, ruv.sgit, and what does not exist yet | Works. |
| `admin/docs/rules-for-agents.html` | `CLAUDE.md`, rendered | The rules every agent follows | Works. |
| `admin/docs/corrections.html` | `BRIEF-CORRECTIONS.md`, rendered | "None yet." | Works. |
| `admin/docs/onboarding.html` | `team/conductor/ONBOARDING.md`, rendered | The prompt the editor pastes into each member's session, what the conductor does next, the read keys | Works. |
| `admin/docs/wake-protocol.html` | `team/conductor/WAKE.md`, rendered | The five steps, the checklist, "Tonight only" (until 20:00 London, 29 October), stopping | Works. |
| `admin/docs/the-next-hours.html` | The conductor's brief for the night, 03:00 London | What the night is for, who does what each hour, how an idea moves as a graph, the night's rules, the morning | Works. The graph of an idea's path is a visual the book could redraw. |
| `admin/docs/pace.html` | `team/conductor/pace.json`, rendered as data | The night's flow as a graph, kept by the conductor every hour | Works, as raw JSON. |
| `team/<id>/index.html` (each member; the conductor's read) | The member's page, built from its folder | Identity, responsibilities, its policy in prose, every session, rules with the mistake behind each, its key and past sessions, status, wakes, its scope from `policy.json`, debriefs | Works. A member's whole record on one page: the book's argument that a mandate can be read. |

## What the admin side does well

It renders the team's own files, not a description of them: the dashboard, the wakes, the commits, the releases and the keys are each read from the repository at build time, so the site cannot say something the record does not. The menu is the same on every page, and the "Sources of truth" group puts the rules beside the work they govern.

## What it does less well

The two live pages (board, mail) depend on the vault server answering, and fail without it; the dashboard is a snapshot of the build, not of now, and says so only in small print; the release history and the commits are long single pages with no search.

## Where this came from

The published site, https://the-ultimate-insider.presentation.sgit.ai/ (v0.2.1), read with a Playwright script on 30 October 2026 at about 18:13 UTC; the talk's repository at `298be4e` and `424b67a`.
