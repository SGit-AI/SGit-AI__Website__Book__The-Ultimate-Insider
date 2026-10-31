---
created: 2026-10-31T03:30:00Z
priority: high
source: comms/mail/mailroom/publisher/conductor__018-rc1-review-layout.eml; conductor__019-rc1-review-5-to-9.eml; team/conductor/rc1/editor-review/notes.json (notes 10, 21, 33)
---
# The editor's RC1 review: layout, A2, A5, A7

- [x] Page numbers on every page, outside corner, none on the title page (book.css), 31 October about 03:00 UTC
- [x] A2: build_book.py reports images printed taller than 45% of the text block, with page, chapter and file (34 today)
- [x] The register ids: the C-numbers already in the text are enough (the conductor's letter 022)
- [x] The designer's visual pass, rules 1, 2 and 4, in the build (31 October about 07:20 UTC); rule 3 (map side notes) waits on the trim
- [x] Type 10 pt, nothing under 9 pt, fuller margins (gutter untouched), the folio as the footer: 255 pages (31 October about 09:10 UTC); with the designer to judge
- [ ] The sizes written into the chapters as Markua attributes, for Leanpub's own build, once P2 is signed
- [ ] Trim Crown Quarto and the 0.625 inch gutter: wait on book.json (designer__013, 018)
- [x] A5: footnotes and endnotes build at chapter end; QR test sheet made (publishing/FOOTNOTES-AND-QR.md, qr_test.py)
- [ ] A5's last point: the smallest QR a phone reads, from the printed sheet (the editor or the designer)
- [ ] A7: what the build needs if content lives in JSON, once the researcher reports
