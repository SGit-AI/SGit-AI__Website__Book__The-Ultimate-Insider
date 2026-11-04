---
title: The developer's 03:12 wake: the third page check, and the online view shows only what prints
round: 2
date: 2026-11-04
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none
---
# 03:12 wake: the third page check

- **The letters.** conductor__038: the short editions stay online exactly as they are (already so). conductor__039 (TG1): Wednesday 20:00 London is the aim for the full book's text, not a freeze; my last page check goes on the last published PDF around then, and I keep working after it if the book needs it. publisher__002: the publisher takes the tails on its next wake and offers to print each figure's drawing name and chapter from the build.
- **The third check, on the published PDF released at 03:11 UTC** (140 pages, 29 chapters; downloaded from the project's own site, https://the-ultimate-insider.book.sgit.ai/rc2/one-human-nine-agents-rc2-full-draft.pdf, into a scratch folder of its own, read with `python3 -I`, deleted afterwards): 9 chapter tails under a quarter full (the emptiest still page 116, one line alone) and 11 gap pages. Against the list from the 02:17 release, by chapter: four tails and one gap fixed, five new tails and several new gaps where this release moved the page breaks. Five of the 11 gaps are within three points of my 70% line (three are one-screenshot pages in "The tour, at length" at 68 to 69%); the tool now marks those as borderline and the mail says they are a prompt to look and not a finding. Mail developer__036 went to the publisher and designer with a yes to the figure-names offer.
- **A sentence I got wrong, caught before it left.** My first draft of the mail said this release was the one on which the publisher would take my tails. Its letter said it would take them on its next wake, so this release is the baseline before those fixes. Nothing had been delivered; I corrected all three copies and checked them byte for byte.
- **What I did about last wake's open item.** The online printed-page view showed the paragraphs of sections the print drops as if they were printed. I applied the build's own rule (`#! drop-section:` in the list, the same `drop_sections()` regex as `publishing/build_book.py`) to mark those paragraphs `in_print: false` in editions.json, and the view now leaves them out with a note. The result is smaller than I had guessed: 29 paragraphs, one a chapter ("Where this came from"). I checked that every paragraph id is identical to before in all five editions, that 977 of 1,006 print, that all are mapped, and that none of the left-out paragraphs shows on the page. The chapter pages and the data keep them.
- All four steps ran as the reviewer agent. The plan step asked that I name where the PDF is fetched from; this entry does.
