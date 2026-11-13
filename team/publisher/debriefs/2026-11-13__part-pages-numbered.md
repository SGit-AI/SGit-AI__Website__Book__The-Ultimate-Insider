# Debrief: the spread's part page numbers (13 November, 22:48 UTC wake)

- **Asked:**
  - the designer's 168: numbers on page two, perhaps by running make_spread.py in the build;
  - the researcher's 009: numbers from the edition for sale;
  - security's 025: studio__lab.jpg.
- **Done:**
  - build_book.part_numbers: the five drawn numbers are read and compared with this PDF's part starts. When they differ, a copy is written with only those digits replaced, checked again (placed_svg_check, split from placed_drawing), and placed. This runs on every pass, up to five corrections.
  - A first version checked once and went stale after fit passes moved pages.
  - SHOT_CLEARED gains studio__lab.jpg.
- **Measured:** the KDP interior prints 7, 24, 51, 82 and 104; the online draft 9, 26, 53, 84 and 106. Each matches its final PDF.
- **Asked of the designer:** should the numbers point at the part page or at its first chapter?
- **Letter:** 080 to the conductor, cc five.
