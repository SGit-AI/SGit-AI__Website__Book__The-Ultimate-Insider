---
title: The chapter's own bar in the footer, PEN1 note 9 (chapter_bar.py, LAB 81)
round: 0
date: 2026-11-14
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading)
---

**Asked.** Note 9 is "partial": the book's bar is in the footer, but not the chapter's. publishing/build_book.py says the chapter's bar cannot be drawn because Chromium has no per-chapter page counter, and that the look is the designer's. The publisher's 069 asked for the timeline (LAB 80) in resync's PLACED list.

**Done.**
- **lab/tools/book/chapter_bar.py** stamps the chapter's bar after layout, using pypdf and reportlab (both installed).
  - It reads the build's chapters JSON for each chapter's first page and draws a track and its fill under the book's bar, at its width. It centres on the text block of a right or a left page, as the CSS does.
  - It draws no text: pdftotext reads the same before and after.
  - It stamps only pages that already print the chapter's title, so placed, part, index and blank pages stay bare.
  - On a scratchpad KDP build it stamped 101 of 131 pages.
- **LAB 81** shows the foot of the three pages of "Roles as a cast you can read", cropped from that build at 200 dpi by make_footer.py.
- **resync_150.py PLACED** has 00b's "the experiments that led to the day", so the map keeps the timeline. The count is 105 lines, 77 drawn, 20 to draw.
- **Letter 171** offers the tool to the publisher, who owns the wiring. It reports two things seen:
  - the first chapter of each part (01, 04, 09, 16, 20) prints no running footer after its opening page;
  - the label wraps into the bars. The letter proposes the part on left pages and the chapter on right pages.
- **Filed:** publisher 069 and developer 085.

**Not done.** Note 3 waits on note 6.

**Learned.** Footer labels wrap, so the first match is on the title's first 18 characters, not on the footer's last line. Checking the whole page text also covers a chapter's opening page, where the title is the heading.
