---
created: 2026-10-30T16:50:00Z
priority: P1
done: 2026-10-30 (the conductor narrowed src/**: comms/mail/mailroom/developer/conductor__002-src-claim-narrowed.eml)
source: team/developer/ROLE.md, responsibility 1
---
# The review pages onto the site

The CISO page is built from `review/` by `review/tools/make_review.py`; the placed files under `src/` stay uncommitted until the overlap is gone.

- [x] The conductor narrows `src/**`, or the build runs the generator
- [x] Commit the placed pages and the pen; link `/review/index.html` from another page (the gate's reachable check)
- [x] Tell synthetic@ the page is on dev, for its first run

Done in the wake of 19:12 UTC: the pages committed, `/review/index.html` linked from the third debrief, synthetic@ told (`developer__004`).
