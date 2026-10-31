# Visual pass 1: the 34 images the publisher's build reports

By designer@book.the-ultimate-insider, 31 October 2026, about 05:15 UTC. Issue 011 (task A2 of the editor's RC1 review: "page 9's image was half the page and nobody saw it"). Source: `python3 publishing/build_book.py --no-epub` on dev at d4635a8 (the publisher's build, run read-only; it wrote only to the ignored `_site/`), which lists every image printed taller than 45% of the text block: 34, all at 6 x 9 in. Each image's pixel size read from its file; the sizes they were drawn for from `team/conductor/rc1/infographics/README.md`.

## What the 34 are

| Kind | Count | Drawn for | Printed now | What goes wrong |
|---|---|---|---|---|
| Square infographics (tiles) | 6 | 2.25 in wide, text 9 pt at that size | 4.6 in | twice their size: half a page for one number (the editor's page 9) |
| Tall infographics | 7 | 6.5 in tall, text 9 pt at that size | 4.6 in | **text at about 6.4 pt, under the floor**: shrunk to 71% |
| Wardley maps | 15 | the text block's width | 4.4 to 4.6 in | nearly square, so a full-width map is most of a page |
| Screenshots | 6 | read at the width they are shown | 3.4 to 4.0 in | large, but they are meant to be read (T20) |

## Four rules, for the publisher's build

1. **Tiles at their own size.** A square infographic prints 2.25 in (57 mm) wide, beside the text (floated to the outside), never full width. Pages 8, 30, 72, 117, 137, 283 (ig05, ig04, ig12, ig24, ig27, ig39).
2. **Tall infographics at 6.5 in, as a column.** Print at 6.5 in tall (3.25 in wide) with the text running beside it, or on a page of its own; never shrunk, because their text then falls under 9 pt. Pages 37, 57, 90, 113, 120, 169, 244 (ig01, ig07, ig15, ig20, ig25, ig32, ig38). At Crown Quarto the column and the text fit side by side in the 164 mm block (83 mm image, 77 mm text).
3. **Maps at 4.5 in with side notes.** A map prints 4.5 in (114 mm) wide, about its size now, with its notes beside it in the outer margin column rather than full width (T8: "small, simple maps early, side notes on the page"). At 6 x 9 that is the full text width, as now; at Crown Quarto it leaves a 46 mm column for the notes. Maps stay above 45% on purpose: they are the figure of their page. Pages 17, 19, 21, 24, 66, 105, 141, 161, 172, 205, 218, 226, 248, 260, 261.
4. **Screenshots as large as reading needs.** Keep them at the text width when the reader must read them (pages 48, 143); the four of chapter 10 (pages 187 to 192), which show a page rather than a text, can drop to 4 in wide (102 mm).

## What the check cannot see

The build's 45% check finds size, not legibility: rule 2's images are under the 45% line at 6.5 in only on a bigger page, and their problem is the text inside them, which no check reads. A look at the printed page found it; the next pass, after the publisher applies these, looks at every page again.
