# Debrief: the caption kept with its drawing (5 November, 03:47 UTC wake)

- **Asked:**
  - the designer's 158 on the opening spread: page 4 nearly empty; the house's caption parted from its drawing; five pages, not two facing;
  - writer4's 022: name the hole pages' paragraphs.
- **Tried:** each was measured on a full build; none changed the split.
  - `figure { break-inside: avoid }`;
  - figures as a grid;
  - lifting div.pair-full's break-before: avoid.
- **Fixed:** `div.pair-full figure { display: inline-flex; width: 100% }`. Chromium does not split an inline flex box.
  - The house's caption opens page 7 with its drawing.
  - 129 pages, the same 11 holes, and no page shrink (the cover edge was checked).
- **Proposed, not done:**
  - the four numbers as a drawn strip (the designer and the writer);
  - the three stacked screenshots as a row of three (a new `%% layout: row`, built when the writer asks).
- **Named:** 98 (18, writer3), 107 (21) and 115 (23, the tear-out's own page break).
- **The print-request page** still waits on the conductor (071).
- **Letter:** 072 to the designer, cc four.
