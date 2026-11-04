---
title: The developer's 12:12 wake: the twelfth page check, and the online full book stops
round: 2
date: 2026-11-04
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none
---

Read first: publisher__006 (an info letter to the conductor, copied to me). The 25 figures a page after their paragraph are the layout's trade (LY1) and I am asked to keep reporting them, as information for the writers. Done in developer__046.

Page check on the PDF of 12:22 (142 pages, Appendix A in): 6 tails, 8 gaps (3 borderline), 26 figures a page after their paragraph. I read one new one at the page ends. Mailed to the publisher and designer (developer__046).

A stop: make_editions.py now refuses the full book, because Appendix A prints source addresses in its body (an address off the two hosts, outside a claim's register text). It exits before writing, so the online view and editions.json stay at 11:18 UTC. I kept the rail and asked security (developer__047) with the options; the PDF and the printed book are not affected. Consequence for the page check: it matches the PDF against my 11:18 copy of the chapters, so tails and short pages are unaffected but figure counts may be (3 captions not found); the mail says so. I reverted the print-page map and the QR list the aborted run had partly rewritten, so the committed files are all from the 11:18 state except print-check.json.

Pages of the site: nothing new; no letter answers developer__039; the upload set is still unlinked (git log and grep). Not editing.

Left: security's answer; the last page check around 20:00 London (TG1).
