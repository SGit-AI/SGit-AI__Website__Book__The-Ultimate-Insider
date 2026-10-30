---
title: RC1 rebuilt and compared, and on the site as the book's first version
round: 1
date: 2026-10-30
commits: dev at the commit that carries this file
site_version: the release after this push
outside_scope: none
---
## What the editor asked

In this session's chat on 30 October 2026, after the first account's session pushed the two PDFs it had printed for him (`427f821`): can you see them; build the PDF here and compare, to make sure the process makes the same PDF; and if so, a page on the site, linked from the home page, that shows it, since it is the first version of the book.

## What happened

1. Seen: both files in `team/conductor/rc1/pdf/` match their `SHA256SUMS`.
2. Rebuilt in the scratchpad (nothing in the repository), as the handover says. `publishing/` already carries the publisher's image embedding and figure CSS, so the scratch copy needed only the title page's title and subtitle. `assemble_rc1.py` placed 89 images and call-outs with no anchor missing and made 294 pages; `companion.py` made 67 pages, 98 cards, 53 decisions. Compared with the pushed files: page counts equal, `pdftotext` text identical, every page (361) identical pixel for pixel at 50 dpi grey, and 22 sampled pages identical at 150 dpi colour. The bytes differ only in the embedded timestamps. The process is reproducible. About 17 seconds for RC1.
3. A page for it, `src/pages/rc1/index.html` (`/rc1/`): the cover, what it holds, the PDF embedded and to download, its hash, and where it came from; linked from the home page by a button in the hero and a band of its own. `admin/build/build.py` copies the PDF, `SHA256SUMS` and the cover thumbnail into `_site/rc1/` from where they are kept, so there is one copy in git, not two.

## A judgement made, for the editor to overrule

The security pre-review asked for both PDFs' text to be checked before anything went on a page. RC1 is clean: it names the leak and D12 but not where the values are or how to read them. The companion is not: its cards say the evidence vault's history holds other sites' cookie values and form tokens, readable with the published read key, and cite `aa7a3eb`. So the page shows RC1 only. The companion file stays where the first session put it in `team/conductor/rc1/pdf/`, and its source cards are in `team/conductor/rc1/annotations/`, both already public in the repository; whether to keep them there is part of D12 and security's open card, the editor's to decide.

## Where this came from

The editor's words in this session, the handover debrief's "Rebuilding the two PDFs", `team/conductor/rc1/pdf/README.md`, and this wake's record (`wakes/20261030T112438Z.json`).
