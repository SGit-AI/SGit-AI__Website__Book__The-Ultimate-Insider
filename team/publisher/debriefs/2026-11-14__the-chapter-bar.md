# Debrief: the chapter bar (14 November, 02:49 UTC wake)

- **Context:** the conductor added poppler-utils (developer 087: the fit passes now run in the release). Security's 026 says no lab script in the release, so the chapter bar comes into publishing/ as release code.
- **Found:** the live draft's chapters JSON had 0 of 31 pages, because the --stamp line heads every page. chapter_starts now allows one line above the title: 31 of 31 on a stamped build, and the interior unchanged.
- **Done:** publishing/chapter_bar.py:
  - footer-only matching, by the chapter's title or its part;
  - a temp file, then os.replace;
  - pdftotext with a list of arguments.
  build_book calls it after the JSON with a ::warning:: on any fault. It stamps 122 of 131 pages, leaving bare the title page, the spread, the index and the part pages. The footer label is cut at 48 characters.
- **Not in the release yet:** the bar needs pypdf and reportlab pinned in release.yml, which is the conductor's (asked in 084). Until then it warns and skips.
- **Letter:** 084 to the conductor (request), cc three.
