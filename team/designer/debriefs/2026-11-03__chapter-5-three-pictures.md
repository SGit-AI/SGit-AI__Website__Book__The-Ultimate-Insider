---
title: Chapter 5's three pictures, and the card rows measured
round: 0
date: 2026-11-03
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading)
---

**What came in.** The conductor's 046: the editor likes the RC2 draft. He asks for tighter layout and the missing pictures, the player's interface first, and the clock in the margin. Every member now runs every hour (ACC1). The publisher's 017: the speech cards and the four heads are placed, and the clock prints as a margin note. The storyteller's 074: the clock's table and ten moments to show as screenshots. Synthetic's 003: ten pictures to come, and card rows cut at the right margin on pages 7, 10, 23 and 25.

**What I did.**
- I built RC2 at fef68eb with the publisher's command into my scratchpad and measured page 7. The card rows end at the text block's edge (163.6 mm), so they are not cut. The read was made on an older build with a scratch figure list. I reported the measurement, not a fix.
- LAB 40 holds three of chapter 5's pictures:
  - the nine cards turning into folders, each sheet drawn only where `git ls-tree` at 298be4e shows it;
  - two cards from this book's record, with the commits and quotes checked at build;
  - three generic people with small factories, joined by one brief, one board and one hold, marked as a plan not yet run.
- Lab PDF 121 pages.
- Letters: 096 to the publisher, copied to synthetic, with the Figure order (rc2-figures.json is the publisher's file and was not touched) and the measurement; 097 asks the writer for the rule line under each card of this book's team.

**What went wrong.** The first draft of the second card ran 0.6 mm past 164 mm, and the HOLD word overflowed its file in the third picture. Both were seen on a screenshot and fixed.

**Next.** The five steps as a path; this book's team as cards once the writer answers; the chapter's map, if I am named owner; the player's interface in chapter 1 is a screenshot (the storyteller's list), which is the publisher's to place unless asked.

Source: the wake record `team/designer/wakes/20261103T015806Z.json`; the letters in `comms/mail/designer/done/`.
