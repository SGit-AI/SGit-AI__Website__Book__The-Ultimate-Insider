---
title: The covers for upload, and chapter 1's still slide
round: 0
date: 2026-11-04
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading)
---

**Asked.** The conductor's 059 put the covers for upload first (FB1: print files to KDP by Thursday 5 November). Its 057 asked for the still slide missing from chapter 1, and its 058 for what lands by Wednesday night.

**Done.**
- **LAB 44, KDP's full cover:** back, spine and front with bleed, sized with the publisher's own rule (cover_size.py) at today's 132 white pages.
  - Cover A sits on the front, its stripes carried into the bleed.
  - The spine reads top to bottom, inside KDP's margin.
  - The back has listing.md's description (traced and cleared), the nine heads and the barcode area left empty.
  - The PDF's page box is exactly 15.427 x 9.940 in.
  - A guides preview shows the trim, folds, safe area and barcode box.
- **LAB 44, Leanpub's cover:** 1800 x 2700 px, from cover_signed(height). LAB 33's default output is byte-identical (cmp).
- **LAB 43, chapter 1's still slide:** 112 x 63 mm, plain on purpose, put in my list for the publisher.
- **Letters and filing:** letters 124 (conductor, copied to the publisher: the covers, the slide, the plan to Wednesday night) and 125 (ruv-sgit: none of its drawings flagged yet). Eight incoming letters copied to done/.

**What went wrong.**
- Python here has no playwright, so the renderer runs node's playwright (`node -e`), as the lab's own renderer does.
- Chromium rounded the PDF page to 15.430 x 9.943 in, neither with nor without `preferCSSPageSize`. pypdf now sets the page box to the exact size over the art, which is drawn from the top left at the exact size. The script refuses a PDF more than 0.0005 in off.
- A cleanup replace missed its anchor, and its assert caught it. The leftover code drew the slide's frame twice; it was fixed by hand before the commit.

**Learned.** Give the trim in inches (7.44 x 9.69), not in millimetres rounded to 189 x 246.1: the difference showed in the PDF's width.

**Next.** The Do this now card, the loop, the title page and Start here, in the conductor's order (letter 124's list). Then the spine at the final count.
