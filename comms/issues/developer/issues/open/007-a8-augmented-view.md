---
created: 2026-10-31T03:12:00Z
priority: P1
source: comms/mail/mailroom/developer/conductor__005-rc1-review-5-to-9.eml; team/conductor/rc1/editor-review/notes.json (A8); briefs/2026-10-31__rc1-paper-review/batch-05-pages-10-to-13.md
---
# A8: RC1 online, augmented

The editor: "this online iPad PDF kind of mode application or view that has that augmented capability ... we should be showing the provenance of every idea, every page, every paragraph".

- [x] First slice, `/review/read/`: every RC1 chapter; commits, file paths and register ids linked where verified in this repository or the talk's at `298be4e` (1377 sources, 540 commits); each chapter's numbers with value, state, source and rerun command; a source count per paragraph; the review pages' anchors (wake of 03:12 UTC, `review/tools/make_reader.py`)
- [x] Register values that are dicts or lists (77 of 86) shown as nested lines, not raw program text (wake of 05:12 UTC)
- [x] The provenance of every paragraph as data: `review/anchors/rc1-provenance.json`, 414 anchors and their 1377 sources (commit, path or claim, with its repository), the base for the graph and QR targets (wake of 07:13 UTC)
- [x] Every review page's chapter list links each chapter to its augmented view (the study's "offer the record link, not only the PDF")
- [x] The provenance turned round, `/review/read/sources.html`: each of the 42 numbers and 135 commits with every paragraph that rests on it (987 paragraph links, all landing) (wake of 09:13 UTC)
- [x] The graph, first view: `/review/read/graph.html`, chapters by the talk team's members, each cell the commits of that member a chapter cites (115 commits; member read from the talk's own record) (wake of 13:15 UTC)
- [ ] The graph's next views: wakes and decisions behind a page
- [x] QR targets for print, pointing at the record under each scene: `review/anchors/qr-targets.json`, 131 targets (RC2, the 70-page draft, the 3- and 10-page editions), https on the book's own domain only; images wait on a QR library (wake of 06:12 UTC, 3 November; notice developer__023 to the publisher)
- [x] A page-by-page view, like the PDF on an iPad, first for RC2: `/review/rc2/pages.html`, one scene at a time (33), previous and next by button or arrow key, the place kept in the link, the record under each page; a "page" is a scene until print page breaks can be read from the PDF (wake of 11:12 UTC, 3 November)
- [x] "Where this came from" as structured data, for the online editions: `review/anchors/editions.json`, published at `/review/editions.json` (4 editions, 37 chapters, every paragraph with its anchor and every record token resolved or marked unverified) (wake of 07:12 UTC, 3 November); RC1 still from parsed text
- [x] The editions.json guard checks every address in the data, not only `url` fields: other hosts pass only as citations found in the register entry of their claim, listed in `outside_citations` and never linked on a page; QR targets get no exception (wake of 08:12 UTC, 3 November; the two today: C101's pricing pages)
- [x] The final address sweep allows a listed outside citation only under its own claim: outside the claims' register text every address must be on the two hosts; tested on a scratch clone, a citation put into a paragraph is refused (wake of 09:12 UTC, 3 November)
- [x] The page view for every edition: rc2-70 (82 scene-pages), ed-03 (4) and ed-10 (10) as printed pages, linked from each index and the zoom (wake of 12:12 UTC, 3 November)
