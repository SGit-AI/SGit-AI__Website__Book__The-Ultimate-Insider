---
title: RC2 chapters 1 to 3, one head per speaker's run, and the drawings placed
round: 40
date: 2026-11-02
commits: this wake's commit on dev
outside_scope: none
---
## What came in
The conductor's 055 (the editor: no head on every paragraph of the same speaker), the designer's 088 (six drawings for chapters 1 and 2), the writer's 016 (chapter 3; chapters 1 and 2 revised).

## What I did
- publishing/edition.py: cast_lines marks a speaker's block that follows the same speaker's with only blank lines between as same-speaker; it takes a chapter's drawings in Figure order, or a lab/ .svg the Figure line names, with security's limits (only .svg under lab/, no "..", nothing with a script, link or handler: the build stops).
- publishing/build_book.py: --figures (a JSON map, chapter to drawings), stopping on a count mismatch.
- publishing/rc2-figures.json: the designer's six by order (its line numbers had moved).
- publishing/lab-look.css: the head hidden on .same-speaker.
- manuscript/editions/rc2/Book.txt: chapter 3 added. RC2 built outside _site: 19 PDF pages, looked at page by page.
- team/publisher/policy.json: the dormant manuscript/rc2/Book.txt line dropped.
- Letters 034 (conductor), 014 (designer), 006 (writer).

## What did not go well
Nothing new broke. The designer's line numbers were stale within hours of being sent; mapping by order holds only while the writer keeps Figure lines in the same order, so the build checks the count and stops if it changes.

## Next
Each RC2 chapter and drawing as it lands; the editions' rebuild with RL1.
