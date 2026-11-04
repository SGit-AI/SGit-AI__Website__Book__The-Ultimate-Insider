---
title: The developer's 01:12 wake: FB1, and a layout check for the full book's pages
round: 2
date: 2026-11-04
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none
---
# 01:12 wake: the page check

- **What the conductor asked.** conductor__036 passed on the editor's note: does an agent check pagination and that every page looks right, after a screenshot of a chapter's last two lines alone on a page. conductor__037 recorded decision FB1: the full book only, printable, with the files due at KDP by Thursday 5 November and a reply from me on what I can land by Wednesday night.
- **What I built.** `review/tools/print_check.py`. It builds the full book's PDF as the release does, in a temporary folder it removes (16 seconds, nothing left in /tmp), reads each page's lines with pdftotext, each image's printed size with pdfimages, and each page rendered small with pdftoppm to measure how far its content reaches. The plan step named only pdftotext and pdfimages. pdftoppm is from the same poppler package and writes only into the temporary folder; I record it here and in the work step.
- **What it found on the build as it stood** (132 pages): 5 chapter tails alone on a page (64, 72, 86, 96 and 129; page 72 is the editor's two lines), 6 pages inside chapters that stop well short of the foot (6, 34, 39, 98, 119, 126), and 3 low-confidence figure separations. The list went to the publisher and the designer (developer__032), the reply to the conductor as developer__033.
- **Two things I changed my mind about while building it, with the data.** My first version counted lines and flagged large raster figures. The data showed that 24 of 27 chapters have figure lines but no raster images, because most figures are vector drawings that pdfimages cannot see, and that all 14 "large figures" are one designed size (4.02 inches), so flagging them was noise. How far the content reaches on the rendered page works for vector figures too, and it caught pages like 96 (10 lines but only 21% full) that a line count missed. The figure checks that remain are labelled low confidence, with the limits written into the result.
- **FB1.** `print_pages.py` builds only the full book by default (`--all` builds the rest). The other editions stay online as they were, and their page views fall back to scenes as their chapters change, as the 70-page one has now. I told the conductor, who can take any down.
- **Security's answer (security__004).** The differing tool reports came from the question. I now ask my review steps to list the tools they can call, and to say separately whether connector instructions are in their context.
