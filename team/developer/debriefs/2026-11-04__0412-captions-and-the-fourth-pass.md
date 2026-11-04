---
title: The developer's 04:12 wake: figures found by their captions, and the fourth page check
round: 2
date: 2026-11-04
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none
---

What was asked: the page check on the full book each build (conductor__036), and the publisher's offer of figure names (publisher__003).

What I did
- Looked at the newly published PDF (137 pages, 04:18). Captions print as text, so I rewrote the figure check to find each figure by its caption and compare it with the page where the paragraph before it ends. A first version flagged 17 figures; reading the page boundaries showed most were figures under a heading, compared with the previous section's last paragraph. Fixed by marking the first paragraph after a heading (`after_heading`, a flag only; the ids are unchanged in all five editions) and skipping those 26 figures.
- Two flags were left (pages 21 and 96). The paragraph's last words ran across a page break, so the search missed them. Added `tidy` and `locate`, which read across the break and ignore the running head and page number. Both flags went; none are apart now.
- Re-ran the three tools in the documented order. The online page view says its numbering is built here and may sit a page off near the end (local build 132 pages against CI's 137 here).
- Mailed the publisher and designer only what changed (developer__037): 7 tails, 10 gaps, 6 borderline; judged the four predicted tails by the published file alone (two hold); took back the "yes" to the figure names because captions suffice.

Not done / left
- The 26 figures under headings are unchecked; asked the publisher what counts as the paragraph before them.
- Last page check on the last published PDF around 20:00 London (TG1).

Disclosures: the local build page count differs from CI's, so all lists come from the published file. The scratch PDF was deleted after each run.
