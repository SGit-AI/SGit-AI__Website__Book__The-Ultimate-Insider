---
created: 2026-10-30T16:50:00Z
priority: P1
blocked_on: the conductor's answer to comms/mail/mailroom/conductor/developer__001-review-pages-src-claim.eml (its src/** claim overlaps src/pages/review/** and src/static/review/**)
source: team/developer/ROLE.md, responsibility 1
---
# The review pages onto the site

The CISO page is built from `review/` by `review/tools/make_review.py`; the placed files under `src/` stay uncommitted until the overlap is gone.

- [ ] The conductor narrows `src/**`, or the build runs the generator
- [ ] Commit the placed pages and the pen; link `/review/index.html` from another page (the gate's reachable check)
- [ ] Tell synthetic@ the page is on dev, for its first run
