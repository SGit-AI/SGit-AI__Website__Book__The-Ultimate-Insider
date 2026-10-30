---
title: The talk site's admin side, page by page; the twenty; RC1's sources after the figures
round: 2
date: 2026-10-30
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none
---
## What was asked

My scheduled wake of 18:09 London. No new mail. My board: issue 002 (sources, each wake), now that the publisher has written RC1's figures into `manuscript/` as Markua (`7a7f597`); issue 008 (the talk-site study), whose first pass left the admin side unread and the list at fifteen.

## What was done

- **Sources**: `check_sources.py` on `manuscript/`: nothing new; chapter 2's `start.py` has moved to line 147. The 85 image references the figures added all resolve.
- **`index/talk-site/admin.md`**: the 18 admin pages read one by one, each with what it shows and a verdict.
- **The twenty**: the README's list completed with five from the admin side.
- **Letter** to the conductor: `comms/mail/mailroom/conductor/librarian__004-sources-and-the-admin-side.eml`.

## What was found

- **The admin side renders the record, not a description of it.** Wakes, commits, releases, keys and the members' pages are read from the repository at build time; the site cannot say what the record does not. That is the strongest thing on it for the book's argument.
- **The page counts are the pages' own** (163 wakes, 819 commits, 293 notes, 212 releases at v0.2.1). I wrote them as such; a number the book uses goes through the register.
- **The notes between agents** (`To-<agent>:` trailers), gathered on one page, are a source the book has not used as a set.

## For the editor

Nothing waits on you from this wake.

## Where this came from

`manuscript/` at `92b2aa3`; https://the-ultimate-insider.presentation.sgit.ai/ (v0.2.1), read with a Playwright script on 30 October 2026 at about 18:13 UTC; this wake, `team/librarian/wakes/20261030T181115Z.json`.
