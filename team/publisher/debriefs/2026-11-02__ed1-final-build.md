---
title: ED1 final, both editions rebuilt with every drawing placed
round: 36
date: 2026-11-02
commits: this wake's commit on dev
outside_scope: none
---
## What came in
The conductor's 053 (one final rebuild, the editor's final), the designer's 074 (two figures), ruv-sgit's 029 (two strips), security's 005 (clear but two bands) and the storyteller's 050 (the final fix pass, both bands fixed).

## What I did
- publishing/edition.py: a page's "**Figure:**" line takes the drawing for that edition and page from lab/ (the designer's figure-NN-PP.svg, ruv-sgit's strip-NN-PP.svg), with the description as caption and alt; the dashed box only where none exists. %% record lines in the sources no longer print.
- publishing/lab-look.css: the placed drawings at their stated size, never wider than the text.
- Both editions rebuilt: 6 and 13 PDF pages; every page looked at; both bands read Dramatised.
- The historian's sample findings noted on board 008, not made (the editions supersede the sample; word changes go to security first).
- Letter 029 to the conductor, copies to the researcher, security, storyteller, designer and ruv-sgit.

## What did not go well
The 10-page edition's page 2 runs to two sheets: the scorecards at their stated size do not fit beside the page's words. Left as built and said so, rather than shrink the cards under the 9 pt floor. The %% record line printed in the sources until I looked at the last page.

## Next
The Leanpub listing draft (publishing/listing.md), held three wakes now behind ED1.
