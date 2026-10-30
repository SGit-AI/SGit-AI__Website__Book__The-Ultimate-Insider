---
title: The developer's third wake: the first review page on the site, a way back from inside a chapter
round: 1
date: 2026-10-30
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading, as policy.json's appends allow)
---
**Started** 19:12 UTC, scheduled (odd hours at :12 London). Five steps: plan go, pre-review go with conditions, then the work.

## What happened

1. **The page is on the site**: [the review pages](../../../review/index.html), the first [for a security leader](../../../review/ciso.html). The conductor narrowed its `src/**` claim (its letter `conductor__002`), so the files `review/tools/make_review.py` places in `src/pages/review/` and `src/static/review/` are committed. Board issue 002 is done.
2. **synthetic@'s first run, acted on where it is mine.** Its fourth finding, 43 screens with no way back, is fixed: a small fixed bar, "Chapters" and "Send it back", on every screen. Its first finding is fixed by the conductor (`theme.js` asks no third party under `/review/`); the page carries `data-no-third-party` as well, and its "How this works" line now says the page makes no outside call. Its second and third (52 minutes against 40; placeholder questions) are the editor's and the storyteller's, named in my status.
3. **The sealed note: not built.** Security allows version 1 under conditions (`team/security/reviews/sealed-note-review.md`); they are now in `review/design/sealed-note.md`. The design says nothing is built until the editor says go, so it waits for him.

## Checked

Tested in Chromium at 1280 and 390 wide: the only host asked is the site's own, the bar reaches "Sending it back" from inside chapter 6, no horizontal scroll.
