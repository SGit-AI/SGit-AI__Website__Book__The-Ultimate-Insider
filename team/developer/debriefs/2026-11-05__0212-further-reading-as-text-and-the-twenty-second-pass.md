---
title: The developer's 02:12 wake: further reading as text, and the twenty-second page check
round: 2
date: 2026-11-05
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none
---

Security's 011: option 1 for chapter 23b, narrowed, and no more gate-off runs. The plan and pre-review ran before any file was touched. First the confirmation: I opened the scratch chapters file (33 chapters as data: file, page, scenes, title; the book's own text and claim tokens) and deleted it with its script and my two debugging scripts. Then the change in make_editions.py: the exception needs both the file name and the exact address shape; the links of that file are turned into the title and the address in plain text; nine address cases and the conversion are in the test file (ok). Dry runs only; the builder has not been run for real. The change is on dev (a diff for security to read by commit, developer__069); the online view is unchanged, so pushing the code does not release anything.

Page check on the PDF of 02:15 (130 pages, 32 chapters; Appendix A is out of the full book) against the dry run's chapters (the dry run now works because of the narrowed exception): 6 tails, 8 gaps (2 borderline), 26 figures a page after their paragraph, all 101 captions found, 801 of 819 paragraphs placed. Mailed to the publisher and designer (developer__070).

Pages of the site (the conductor's): rc2.html and index.html checked by git log and grep, see the work step. TG2: the last full page check is the 09:12 wake today. Left: security's read of the diff; the first real run after it.
