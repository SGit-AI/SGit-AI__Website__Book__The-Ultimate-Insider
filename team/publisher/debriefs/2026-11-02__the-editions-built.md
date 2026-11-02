---
title: The 3- and 10-page editions built, and the signed title in the build
round: 33
date: 2026-11-02
commits: this wake's commit on dev
outside_scope: none
---
2 November 2026, wake started 04:47 UTC (team/publisher/wakes/20261102T044742Z.json), the editor's "See dev".

## What came in
The conductor's 048 (build the 3- and 10-page editions, the editor's word), 049 (SP1: the series page to the back) and 050 (NS1: the title signed, "One Human, Nine Agents, Nineteen Hours").

## What I did
- publishing/edition.py: a script in chapter-plan/cast/ to manuscript text in manuscript/editions/NN/ with its own Book.txt. Each page its own chapter; the cast bar, band and words box as fenced divs; the %% marker lines, the header and the writers' notes left out; the series page to the back (the 3-page borrows the 10-page's); the script's sources at the end. The words are the storyteller's, unchanged.
- Built both: _site/manuscript/one-human-nine-agents-edition-03.pdf (6 pages) and -10.pdf (12 pages), type A, Crown Quarto, stamped. Looked at every page: no stray fences or markers.
- publishing/markua.py: close_divs no longer adds a closing fence to a div that closes itself (the cause of the stray ":::" in the first build). The book still builds at 192 pages and the sample at 13.
- publishing/lab-look.css: styles for the cast bar, the words box and the band; the subtitle under the title in plain case.
- publishing/metadata.yaml: the signed title and subtitle. publishing/LEANPUB.md: the title named; the slug one-human-nine-agents free on 2 November (a check, not a reservation).
- Letters: conductor 025, security 005, researcher 004, storyteller 004.

## What did not go well
The first build printed stray ":::" lines: a block written with its own closing fence was closed a second time by markua.py. Found by looking at the pages, fixed in markua.py and edition.py, rebuilt.

## Next
publishing/listing.md, the Leanpub listing draft with the signed title. Then the readers' answers on the editions.
