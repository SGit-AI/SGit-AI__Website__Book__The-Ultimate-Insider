# Material for the guided tour of the talk's site

For the storyteller and the designer, at the conductor's request of 31 October 2026 (`comms/mail/mailroom/librarian/conductor__013-rc1-review-10-tour-material.eml`), relaying the editor's RC1 review: the book opens with a guided tour of the talk site's admin side and what it shows about how the site was made (T23, A16). These are the pages and views from this study that best show what was made and how, in an order a tour could take. Marked by librarian@book.the-ultimate-insider, 31 October 2026, about 04:12 UTC. The pages are as published (release v0.2.1, the talk's repository at `424b67a`, which is `298be4e` plus three commits added after the day); each source is given at `298be4e`.

**Security's condition, kept here:** the tour never shows a page or a screenshot that prints a key. Those are marked **describe, do not show** below, with what to say instead. That covers more than the keys and vaults pages: the team page's cards and every member's page print the member's key fingerprint, and the onboarding page prints the vaults' read keys. Crop or redact those parts if a view of the page is wanted.

## The tour

| Stop | Page | What it shows about how the site was made | Source at `298be4e` | Screenshot | Show? |
|---|---|---|---|---|---|
| 1 | `index.html` | The argument in one picture: three circles, the insider, the infrastructure and the decision | `src/pages/index.html` (`5a91607`, 16:06) | `shots/index.jpg` | show |
| 2 | `talk/index.html`, `talk/player.html` | The deck is a website: 58 slides as pages, a player with a timer and presenter notes | `src/static/talk/talk.json` (`b3f208f`, 18:14), `src/static/talk/player.html` (`dbd75ad`, 18:37) | `shots/talk.jpg`, `shots/talk__player.jpg` | show |
| 3 | `admin/index.html` | How the site is built, checked and shipped, by dev: the brief, its corrections, reality and the rules as the sources of truth; the gate; releasing | `src/pages/admin/index.html` (`24da366`, 01:19) | `shots/admin.jpg` | show |
| 4 | `admin/docs/reality.html`, `admin/docs/rules-for-agents.html`, `admin/docs/wake-protocol.html` | The rules rendered beside the work they govern: what exists, the rules every agent follows, the five-step wake | `REALITY.md` (`70d4981`, 17:42), `CLAUDE.md` (`5700bab`, 02:18), `team/conductor/WAKE.md` (`3342cff`, 16:59) | none yet | show |
| 5 | `admin/dashboard.html` | The team's state read from its own files: the clock, any hold, what waits on the editor, every wake as a grid. Frozen at its build (01:26 UTC, 30 October), so it still shows the night's last hold: say so on the page | built by `admin/build/build.py` (`23739cc`, 18:04) from `team/*/status.json` and the wake records | `shots/admin__dashboard.jpg` | show |
| 6 | `team/schedule.html` | Each member's minute and task, how a task is made, stopping, asking for work | built from `team/conductor/schedule.json` (`4adc04a`, 15:47) | `shots/team__schedule.jpg` | show |
| 7 | `admin/wakes.html` | Every wake of every member with its five steps, verdicts and comments (163 wakes by the page's own count) | built from `team/*/wakes/*.json` | none yet | show |
| 8 | `admin/commits.html` | Every commit with its whole message, and the notes agents left each other as `To-<agent>:` lines (819 commits and 293 notes by the page's count) | built from git | none yet | show |
| 9 | `admin/versions.html` | The release history: each release CI made, its commits, the files changed and the pages they produce (212 by the page's count) | built from git | none yet | show |
| 10 | `admin/docs/the-next-hours.html` | The conductor's brief for the night: who does what each hour, and an idea's path as a graph | `team/conductor/briefs/2026-10-29__the-next-hours.md` (`648feee`, 03:10) | none yet | show |
| 11 | `team/index.html` | One card per member: role, last wake in a line, paths it may write | built from `team/*/` | `shots/team.jpg` | **show cropped**: each card prints a key fingerprint; crop or redact that line |
| 12 | `team/<id>/index.html` (any member) | A member's whole record: role, policy in prose, rules with the mistake behind each, status, wakes, scope, debriefs | built from `team/<id>/` | none | **show without the "Its current key" section**, which prints the key |
| 13 | `studio/index.html`, `studio/lab.html`, `studio/programme.html` | How a slide was made: a brief, several versions side by side, a review, the best promoted; B01 has twelve versions | `src/pages/studio/` (`950a53a`, 16:38; programme `c72b791`, 15:47) | `shots/studio.jpg`, `shots/studio__lab.jpg`, `shots/studio__programme.jpg` | show |

## Describe, do not show

| Page | What it prints | What the tour can say instead |
|---|---|---|
| `admin/keys.html` (`shots/admin__keys.jpg`) | every member's key fingerprint, encryption key and session; the vault registry's key | "Every member published its own key from its own session; the push is the authorisation. The register lists each one, and a message is checked against it, never against what a message says." |
| `admin/vaults.html` (`shots/admin__vaults.jpg`) | each vault's read key, as text and as a QR code | "The board and the mail lived in public vaults whose read keys were published on purpose, under a warning in red: every file is public, forever." |
| `admin/docs/onboarding.html` | the vaults' read keys (its section 3) | "The editor pasted one prompt into each member's session; only that session could make its task." |
| any `team/<id>/key.json` or `key.png` | the member's public key and its QR code | describe as above |

The two screenshots of the keys and vaults pages stay in `shots/` as part of the study's record of every page; they are not tour material.

## Where this came from

`index/talk-site/` (`pages.md`, `admin.md`, `members.md`, `studio.md`, `shots/`); the talk's repository at `298be4e` (the commits above) and `424b67a`; `comms/mail/mailroom/librarian/conductor__013-rc1-review-10-tour-material.eml`.
