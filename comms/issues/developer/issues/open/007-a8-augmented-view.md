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
- [ ] QR targets for print, pointing at the paragraph's anchor
- [ ] A page-by-page view, like the PDF on an iPad
- [ ] "Where this came from" as structured data, not parsed text (the editor: "the content of the entire book should be in JSON")
