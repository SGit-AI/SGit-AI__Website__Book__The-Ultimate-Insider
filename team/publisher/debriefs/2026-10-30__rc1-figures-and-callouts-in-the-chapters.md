---
title: RC1's figures and call-outs written into the chapters as Markua
round: 11
date: 2026-10-30
commits: this wake's commit on dev
outside_scope: none; a two-line patch to admin/build/build.py tested in a scratch worktree and sent to the conductor, not applied
---
## What was asked

The handover's first item, its last part: the conductor's RC1 build placed the infographics, the maps and the call-outs only at build time, so the PDF the editor is reading had them and `manuscript/` did not; "in `manuscript/` they should become real image lines and Markua asides". Letter 013 from the conductor was a reply, filed.

## What was done

- **`publishing/place_rc1.py`**: the conductor's placement logic (`assemble_rc1.py`), the same anchors in the same order, writing into the chapter files: 28 infographics (the two withdrawn left out) copied into `manuscript/resources/images/infographics/`, maps 6 to 16, and the 50 call-outs as Markua blurb blocks with Markua's own classes (information, discussion, tip, warning, exercise for concept, number, takeaway, warning, try). A dry run first: every anchor found. It refuses to run twice.
- **`publishing/markua.py`**: `discussion` and `D>` now print as the number call-out.
- **The check**: the chapters' text is unchanged (377 lines added, one changed: the map 5 path the conductor's placements replace); the book builds at 293 pages against 294 for the editor's RC1 PDF, whose extra page is the cover; a call-out page looked at as an image. 72,462 words with the call-outs.
- **The site**: its own renderer showed the blurb markers as text. `admin/build/build.py` is the conductor's, so the two-line fix went to it as a request with the patch, tested in a scratch worktree (gate clean, no marker left).

## What was hard, or inferred

- Releasing before the site fix was a judgement: the PDF and EPUB, which are the book, are right now and match what the editor reads; the site pages stay readable with the markers showing. Holding the manuscript back would have kept CI's PDF without the call-outs the editor is annotating.
- Number call-outs have no Markua class of their own; I used `discussion`, the least used, and said so in `markua.py`. Leanpub's own look for a discussion blurb is not the RC1 look; the editor sees Leanpub's look in the preview.
- Size: the illustrated PDF is 16.8 MB and the EPUB 13.5 MB; the images are 15 MB, none over Leanpub's 1 MB guidance.
- **A mistake, caught by the scope check:** to see its options I ran the conductor's `assemble_rc1.py --help`; it takes no options and ran its build, which made an untracked `team/conductor/rc1/tools/bookbuild/manuscript/` and then stopped before writing anything else. No tracked file changed (git status, and the RC1 PDFs still match their SHA256SUMS); I deleted the folder before commit. Lesson: read another member's script, never run it to read it.
- Time: about 30 minutes, the pre-review's change (name the image path in full) included.

## Where this came from

`team/conductor/handovers/publisher.md`; `team/conductor/rc1/tools/assemble_rc1.py`, `infographics/manifest.json`, `infographics/callouts.json`, `maps/placements.json` and `pdf/the-ultimate-insider-RC1.pdf` (read only); the build's output.
