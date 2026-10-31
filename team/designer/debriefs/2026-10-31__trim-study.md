---
title: The trim study, at the editor's word
round: 0
date: 2026-10-31
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading, as policy.json's appends allow)
---
**Started** 00:12 UTC, from the editor's chat. Five steps: plan go, pre-review go with conditions (compare, do not choose; no book.json; no publisher's build), then the work.

## What happened

- **The editor asked** which KDP trim suits a book with this many infographics, and the minimum margins; I answered from KDP's help pages (sources cited in the session) and recommended 8 x 10, with 7.5 x 9.25 as the conventional alternative. He asked for PDFs at those sizes.
- **Three PDFs, one source**: `lab/tools/trims/build_trims.py` flows the same sample pages (LAB 01's worked page with the rail and a character, an RC1 infographic wide and tall, a full-bleed frame, two screenshots, LAB 04's strip) as a real book at each trim: mirrored margins with KDP's gutter inside, a folio outside, one full-bleed page, and the lab's type at the lab's sizes. 6 x 9 runs to 9 pages, 7.5 x 9.25 to 9, 8 x 10 to 8; on 6 x 9 a call-out is pushed onto a page of its own, which is the narrow page's cost made visible.
- **The renderer grew** to check a flowing book (no fixed pages): the 9 pt floor over the whole document, the page count left open.
- **Requests first**: ruv.sgit aligned its ids with the print, so the map entries in `lab/tools/ids.json` are gone; the PDF is unchanged.

## Not mine

The trim is the editor's to sign; the conductor is asked to open it as a decision and link the PDFs on /lab/; a signed trim goes to the publisher, whose build it is.
