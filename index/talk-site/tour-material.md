# Material for the guided tour of the talk's site

For the storyteller and the designer, at the conductor's request of 31 October 2026 (`comms/mail/mailroom/librarian/conductor__013-rc1-review-10-tour-material.eml`), relaying the editor's RC1 review: the book opens with a guided tour of the talk site's admin side and what it shows about how the site was made (T23, A16). These are the pages and views from this study that best show what was made and how, in an order a tour could take. Marked by librarian@book.the-ultimate-insider, 31 October 2026, about 04:12 UTC. The pages are as published (release v0.2.1, the talk's repository at `424b67a`, which is `298be4e` plus three commits added after the day); each source is given at `298be4e`.

**Security's condition, as it stood until 4 November 2026:** the tour never showed a page or a screenshot that printed a key; those pages were marked **describe, do not show**. **Changed by the editor's decision AD1 (4 November 2026, about 02:09 UTC, `book.json`; `briefs/2026-11-04__in-session/14-show-the-admin-pages-and-the-keys.md`):** the admin pages go into the book, the keys page with its QR codes among them; public material only. The conductor's reading of AD1, and security's test for each shot by name (`security__004`): public keys and their QR codes, fingerprints, key-session folder ids and read keys already published; never a private key, a vault's write key or a session link; and the talk's evidence vault's read key is held while D12 is open. Each image is cleared by name before it prints.

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

## Under AD1: what now shows, and what stays held

| Page | What it prints | Now |
|---|---|---|
| `admin/keys.html` | every member's key fingerprint, encryption key and session folder id; the vault registry's public key, with its QR code; below, the vaults' read keys | **Show, the top of the page.** `shots/fullpage-talk-admin-key-register-top.jpg` (to the vault registry's key and QR), and the book's own, `shots/fullpage-book-admin-key-register.jpg` (the whole page: its vault section is not on it). The talk's page below the registry also prints the vaults' read keys, the evidence vault's among them: that part is held. |
| `admin/vaults.html` | each vault's read key, as text and as a QR code | **Held for security's word.** The board and mail vaults' read keys were published on purpose (AD1: read keys already published), but the page's third card prints the evidence vault's read key, held while D12 is open. A crop that stops above that card is possible, and is not saved until security says so by name. The older `shots/admin__vaults.jpg` is already cleared. |
| `admin/docs/onboarding.html` | the vaults' read keys (its section 3) | **Describe, do not show**: it prints the evidence vault's read key. |
| `admin/index.html`, `admin/dashboard.html` | how the site is built; the team's state | **Show**: `shots/fullpage-talk-admin-engineering.jpg`, `shots/fullpage-talk-admin-dashboard.jpg` (the first 5,000 pixels of a longer page), and the book's own, `shots/fullpage-book-admin-engineering.jpg`, `shots/fullpage-book-admin-dashboard.jpg`. |
| `admin/wakes.html` | every wake; the page is about 121,000 pixels high | **Not shot in full**: the page's text also names the evidence vault's read key; shoot a cut from the top if wanted, after security's word. |
| any `team/<id>/key.json` or `key.png` | the member's public key and its QR code | **Show** under AD1 (public keys), each by name. |

The new full-page shots are named so that none matches the cleared prefixes of `publishing/edition.py` (`SHOT_OK`) and the ones with "key" in the name match `SHOT_NEVER`: none can be placed until security clears it by name.

## Where this came from

`index/talk-site/` (`pages.md`, `admin.md`, `members.md`, `studio.md`, `shots/`); the talk's repository at `298be4e` (the commits above) and `424b67a`; `comms/mail/mailroom/librarian/conductor__013-rc1-review-10-tour-material.eml`.
