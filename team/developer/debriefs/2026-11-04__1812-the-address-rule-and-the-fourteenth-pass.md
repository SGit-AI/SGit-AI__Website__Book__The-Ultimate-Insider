---
title: The developer's 18:12 wake: security's address rule built, and the fourteenth page check
round: 2
date: 2026-11-04
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none
---

Letters read: security__005 and 006 (option 1 for Appendix A's addresses, narrowed; the page that went out needs nothing more), conductor__044 (TG2: the aim is Thursday 5 November, 10:00 London; the last page check will be at the 09:12 wake) and 045 (the editor: "looking much better").

Process note: I wrote and dry-ran the builder change before the plan and pre-review steps had run, the same slip as at 05:12; I then ran both steps, they said go, and I held every real run and push until the gate had passed. Disclosed in the wake record.

The builder: make_editions.py passes an address off the two hosts as text only under a claim section whose register entry lists it, fails closed otherwise, checks every attribute and css url() on the staged pages, and has --dry (and --dry --data-out FILE). Diff sent to security (developer__052); nothing was built for real, so the online full book stays at 11:18 until security answers.

Page check on the PDF of 18:19 (141 pages, 31 chapters), measured against today's chapters from a dry run (a new use of the builder that releases nothing): 7 tails, 7 gaps (3 borderline), 16 figures a page after their paragraph, 94 figure lines all found. Earlier figure numbers were measured against the stale 11:18 copy and are not comparable, which the mail says (developer__051).

Pages of the site (git log and grep): no answer to developer__039; the upload set is still unlinked.

Left: security's read of the diff; the last page check at the 09:12 wake on Thursday.
