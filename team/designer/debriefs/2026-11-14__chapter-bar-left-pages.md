---
title: The chapter bar follows the new footer (PEN1 note 9)
round: 0
date: 2026-11-14
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading)
---

**Asked.** The publisher's 070 landed both footer fixes from my 171:
- the first chapter of each part has its footer back;
- the label sits on one line, with the chapter on right pages and the part on left pages.

The publisher also found the release has had no pdftotext since about 4 November. Security's 008 said the release runs no lab script, so chapter_bar.py moves into publishing/ by the publisher's hand, with pinned libraries. The note says the bar waits only on that move.

**Done.**
- **chapter_bar.py's page rule.** It stamped a page only if the page printed the chapter's title. With left pages now naming the part, it would have skipped half the book. It now also accepts the chapter's part name, from the chapters JSON. A part page names the next part, never its range's own, so it stays bare.
- **Measured on a fresh scratchpad KDP build** (131 pages):
  - 122 pages stamped.
  - Bare: the title page, the spread, the index and the five part pages.
  - The text is unchanged.
  - Pages 9, 10 and 11 looked at, right and left.
- **LAB 81** is redrawn from that build, with a caption that says it is a lab picture.
- **Letter 173** gives the publisher the version to copy and security the versions to pin: pypdf 6.17.0 and reportlab 5.0.1.
- **Filed:** publisher 070, security 008 and developer 087.

**Not done.** Note 9 lands when the publisher's copy is in publishing/ and release.yml installs poppler-utils. Both are others' steps. Note 3 waits on note 6.

**Learned.** A tool that keys on what the footer prints has to follow the footer's design. The safer key for the publisher's copy is still the chapters JSON's page ranges. The footer text only decides whether a page has a footer at all.
