# Debrief: CI has no pdftotext; two footer fixes (14 November, 01:49 UTC wake)

- **Found:** the live full draft lacked the chapters JSON (developer 086), and its visual index showed the drawn numbers. release.yml installs pandoc only, so pdftotext is missing in CI. build_book fails after the first render, the step warns, and the first-pass PDF ships.
- **Effect:** in released PDFs since about 4 November, these have not run:
  - fit-tails;
  - the spread's blank page;
  - the part and index numbers;
  - the chapters JSON.
  My measurements were all on local builds, so the letters' "at every release" was wrong. It is corrected in 083.
- **Asked:** the conductor adds poppler-utils on release.yml line 72 (its file). build_book now warns at start when pdftotext is missing.
- **Fixed (designer 171):**
  - running_footer skips only the spread's placed pages, so the first chapter of each part keeps its footer;
  - right pages carry the chapter's title, left pages the part, one line each, capped before escaping.
- **Held:** chapter_bar.py (lab code on the shipped PDF) waits on security.
- **Letter:** 083 to the conductor, cc three.
