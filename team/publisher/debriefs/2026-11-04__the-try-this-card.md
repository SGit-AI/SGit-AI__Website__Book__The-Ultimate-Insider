---
title: The Try this card in every chapter; screenshots at print resolution
round: 73
date: 2026-11-04
commits: this wake's commit on dev (and last wake's, pushed at its start)
outside_scope: none
---
## What came in
The conductor's 081 (cast bars, the sources, chapter 2's map); the designer's 131 (its RV2 read of 01) and 133 (the concept callout); the developer's 040; ruv-sgit's 067 (a must on chapter 2, already fixed last wake); security's 016 (nine memory shots) and 017 (keys pages and key images); writer2's 015 and writer4's 005.

## What I did
- The gate was clean again, so last wake's commit went to dev first.
- "#! try-this-card": each chapter's "Something to try" / "Try this" / "Do this now" section becomes the designer's card, the label "Try this" everywhere, three labelled parts when there are three paragraphs.
- "#! extra-css" also takes a stylesheet directly in lab/tools/book/, checked at every build (no @import, expression, behavior, -moz-binding or escape; url() only #id or an inline SVG passing unsafe_svg).
- Screenshots at about two thirds of the column: 318 dpi.
- SHOT_CLEARED: the nine memory shots.
- Letters: conductor 054, designer 046, ruv-sgit 019, writer2 003, writer4 003.

## What did not go well
The first card build set its text in the serif italic: lab-look's rule for italic paragraphs outranked the card's sans. Fixed in full-book.css before committing.

## Next
The concept callout (concept.css); the cast bar's faces when drawn; RV2 part two.

After the post-review: the stylesheet check also refuses image-set(), cross-fade(), src() and @font-face (a bare address could pass in image-set); try-this.css still passes.
