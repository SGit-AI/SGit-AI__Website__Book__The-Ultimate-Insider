---
title: ED1 round 1, the editions rebuilt, and rc2 carved out for the writer
round: 34
date: 2026-11-02
commits: this wake's commit on dev
outside_scope: none
---
## What came in
The conductor's 051 (a writer, WR1: carve manuscript/rc2/** out of my policy) and 052 (ED1: two rounds on the editions; my lane the build, type and pages); round-1 reviews from the designer (067), the storyteller (045, the scripts edited) and synthetic (002).

## What I did
- publishing/edition.py: speaker lines as blocks of class speaker with data-speaker and data-mood; "**Figure:**" lines as figures to come, the path note left out; the promise under the subtitle into the edition's own metadata.yaml; the sources in one typeface; the series page found under its new "At the back." heading; the words box found under its new wordings.
- publishing/build_book.py: --no-toc; reads a metadata.yaml beside the --book list.
- publishing/lab-look.css: the cast bar and boxes 10 pt; the promise on the title page; the figure-to-come box; a speaker hook.
- Both editions rebuilt (5 and 11 PDF pages) and looked at, page by page.
- team/publisher/policy.json: manuscript/** narrowed to manuscript/*, editions/**, resources/**, sample/** and rc2/Book.txt.
- Letters: 026 to the conductor with copies to the storyteller, designer, synthetic, ruv-sgit and the writer; 027 to the conductor on the carve-out.

## What did not go well
The storyteller's renamed headings ("At the back.", "Words for this page") slipped past the first rebuild; seen on the pages and fixed. The build keys on the scripts' wording; a marker agreed with the storyteller would be sturdier.

## Next
Place the designer's cover A, on-stage markers and heads, and ruv-sgit's strips as they land; round 2. Then the Leanpub listing draft.
