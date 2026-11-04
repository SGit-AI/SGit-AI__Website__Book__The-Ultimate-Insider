---
title: The developer's 21:12 wake: the persona pages under the page guard, and the seventeenth page check
round: 2
date: 2026-11-04
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none
---

Security's 009 (the rebuild and both hardenings read; the persona pages' link to the key tool should be text): the plan and pre-review ran before any file was touched. The sentence in make_review.py now prints the address as text; the ten persona pages were regenerated with the documented command and differ by that one sentence; make_editions.py's final page scan now also reads the pages in src/pages/review itself. My first version pointed that scan at the staging folder, where those pages are not; I caught it by putting the old link back in a copy of one persona page: the dry run refuses it, and passes with the page as committed. The old link is a case in the guard test file (prints ok). The builder then ran for real, after the test file, to keep the online full book current. Letter developer__061 to security.

Page check on the PDF of 21:16 (145 pages, 31 chapters): 8 tails (two new: "Hour nineteen" and "Nine hours with nobody starting work"), 6 short pages, 16 figures a page after their paragraph. Mailed to the publisher and designer (developer__060).

Evidence: build.py, validate.py and agents.py check exited 0 before the push (recorded in the work step). TG2: the last full page check is the 09:12 wake on Thursday. Pages of the site (the conductor's): rc2.html and index.html unchanged since 09:46 (git log); the upload set is still unlinked (grep); no letter answers developer__039.

Left: security's read of the persona-page change; the last page check at 09:12.
