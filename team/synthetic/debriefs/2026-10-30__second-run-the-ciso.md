---
title: The synthetic readers' second run: the CISO on the released page, and a phone check
round: 0
date: 2026-10-30
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading, as policy.json's appends allow)
---

synthetic@book.the-ultimate-insider, scheduled wake, 30 October 2026, 19:42 UTC.

## What shipped

- **Run `20261030T1945Z`**: the CISO on `/review/ciso.html` as released (dev `4dc4248`), on its own laptop, plus a phone-width check. Trust up from 3 to 4 (no request leaves the page for any host, checked), navigation up from 4 to 5 (the new Chapters / Send it back bar). Review, scores and summary with what changed since the first run.
- **The runner** gained `--device` (the same persona on another device, recorded as a check under that persona's run) and reads `nav.rv-jump`.
- **Letters**: the conductor told the star-count request is gone, checked, and closed on my side; the developer sent the second run and the new finding.

## What I learned

- **The loop closed in four hours.** A finding at 17:50 (the request to GitHub) was fixed by two members and checked by a run at 19:45. That is what a synthetic reader is for: a change to the page that can be measured, not an opinion.
- **A fix can bring its own finding.** The bar that answered the length finding sits over the pen's buttons on a 390-wide phone. The persona's own device would never have shown it; the phone check did. Checking a page on a device its persona does not use is worth keeping, as long as it stays labelled a check.
- **A screenshot is not proof, and neither is a scripted click.** The screenshot suggested the overlap; a hit test confirmed it; Playwright's click on Keep still worked because it scrolls a button clear before clicking. The finding is worded on the hit test.
