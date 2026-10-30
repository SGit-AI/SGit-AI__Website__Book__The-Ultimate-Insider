# RC1 as printed, 30 October 2026

The two PDFs the editor printed for his flight, built at about 10:57 UTC on 30 October 2026 by the first account's conductor session from `team/conductor/rc1/` as it stood then (the chapters committed in `5d73a4e`).

- `the-ultimate-insider-RC1.pdf`: RC1, 294 pages at 6 x 9 in, with the cover (concept 1), the map chapter and 16 Wardley maps, chapter 11b, the concepts and principles part, 28 infographics and 50 call-outs placed at build time, and the corrections pass.
- `the-ultimate-insider-RC1-companion.pdf`: the companion, 67 A4 pages, 98 cards (53 decisions with tick boxes), each matched to its page in the RC1 PDF above. The role cards were drafted by conductor sub-agents, not the members.

`SHA256SUMS` holds their hashes. Rebuild with `team/conductor/rc1/tools/assemble_rc1.py` and `companion.py` (the conductor's handover says how). When RC1 is revised in place, replace both files together, so the companion's page numbers still match.

## Rebuilt and compared, 30 October 2026, about 11:30 UTC

The second conductor session rebuilt both from `team/conductor/rc1/` as the handover says (a scratch copy of `publishing/`, which now carries the image embedding and figure CSS itself, with the metadata title and subtitle set to the title page's), with `assemble_rc1.py` and `companion.py` under `python3 -I`. Both came out the same as the files here: RC1 294 pages and the companion 67, `pdftotext` text identical, every page rendered at 50 dpi identical pixel for pixel, and 22 sampled pages at 150 dpi in colour identical too. Only the bytes differ (the files' embedded timestamps), so the hashes in `SHA256SUMS` hold for these files only, not for a rebuild.

RC1 is on the site at `/rc1/`; the companion is not, because its cards discuss where the leaked values are and how they could be read (D12), which the book itself no longer says.
