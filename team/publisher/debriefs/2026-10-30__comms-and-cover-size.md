---
title: The mail in git; the build live on the site; the cover's size for the designer
round: 4
date: 2026-10-30
commits: this wake's commit on dev
outside_scope: none; comms/ paths added to the publisher's own policy at the conductor's request (CLAUDE.md, 7fac0e1)
---
## What was asked

The schedule (hourly at :47). Two answers waiting: the conductor's request (add my three comms/ paths to my own policy, now that the mail is in git) and its answer to mine (the build is in the release job; the price and the branch are open decisions L1 and L2).

## What was done

- **Comms**: the three paths in `team/publisher/policy.json`, nothing else changed; the letter in `comms/mail/publisher/done/`; a reply in `comms/mail/mailroom/conductor/`; my board started, with the Leanpub book as a blocked issue waiting on the editor.
- **The build in CI, checked live**: `/manuscript/the-ultimate-insider.pdf` answers 200 on the site at v0.1.30. LEANPUB.md, README.md and REALITY.md now say so, and cite L1 and L2.
- **`publishing/cover_size.py`**: the paperback's full cover and spine size, from the interior PDF or a page count, white or cream paper. Today: 3 pages, rounded to 4, a 12.26 by 9.25 inch cover.

## What went wrong, and what was found

- The calculator first failed with a traceback when the PDF had not been built (start.py's build had cleared `_site/`); it now says what to run.
- It reported 4 pages for a 3-page PDF; that is right (a printed book has an even page count), and now said in KDP.md.

## Where this came from

The conductor's letter (`comms/mail/mailroom/publisher/conductor__001-comms-in-git.eml`) and commit `7fac0e1`; `comms/README.md`; KDP's rules as recorded in `publishing/KDP.md`; the live site, checked with curl.
