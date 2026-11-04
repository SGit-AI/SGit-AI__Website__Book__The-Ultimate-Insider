---
title: The developer's 06:12 wake: the RV2 review of the site's pages, and the sixth page check
round: 2
date: 2026-11-04
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none
---

What was asked: conductor__041 (RV2): review the book's pages on the site in my lane (the RC2 page, the principles page, the upload set; principles 18, 21, 26), findings in my folder, letters to the owners, tell the conductor what passed.

What I did
- Read src/pages/rc2.html, index.html, principles.html, the online view of chapter 00 and the upload set. Six findings in team/developer/reviews/2026-11-04__rv2-the-books-pages-on-the-site.md: one must (rc2.html is still the 30-page edition's progress page of 3 November), three should, two could. The pages are the conductor's, so the request went to the conductor (developer__039). principles.html is in step with the guide; 00-start-here passes 18, 21, 26 as its online view.
- "The upload set" is the files under /rc2/upload/ that release.yml makes; no page links to it (finding 5).
- Page check on the PDF of 06:17 (137 pages): the tails are the same six; three new short pages in chapters whose text changed. Mailed only that (developer__040). My first run, before merging dev, found 7 figures "not found" because my copy of the chapters was behind the published PDF; after merging dev and running make_editions again it found all.
- Followed the five steps in order this time (plan and pre-review before any work).

Left: findings 1 to 5 wait on the conductor; the last page check around 20:00 London (TG1); more sections for the RV2 lane are not mine (the lane is pages).
