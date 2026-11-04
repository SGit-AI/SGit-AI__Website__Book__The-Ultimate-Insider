---
title: Chapter 16's two drawings in proportion, and the start sheet in one run
round: 0
date: 2026-11-04
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading)
---

**Asked.** The conductor's 055 passed on the editor's note on pictures "too big and out of proporsion", with chapter 16's hold file and the stopped wake clock as his example. Its 056 asked for the title page, Start here variations, and two fixes to the printable start sheet.

**Done.**
- **ch10-hold-file.svg (LAB 42):** 164 by 100 mm before, 140 by 63 mm now. The last line went from 21 pt to 13 pt and the title from 13 pt to 11 pt, with four ruled lines instead of seven. The first try at 124 mm was too narrow for the "What lifts it" line and the caption; the screenshot showed it, and the drawing went to 140 mm.
- **ch4-clock-stopped.svg (LAB 39):** 164 by 80 mm before, 134 by 64 mm now. "82 seconds" went from 31 pt, touching its card's edge, to 18 pt inside the card.
- **All 44 of my drawings in the full book measured:** none sets type above 14 pt. The story tree (180 mm) and the checklist (147 mm) are the tall ones, left for a look at full size.
- **ch1b-start-sheet.svg:** each step is one text run with a bold tspan. A run that opens on punctuation follows the bold with no space. The drawn caption is gone.
- **The split cards:** two_files() now draws either card alone, so each file holds only its own card. They render exactly as before.
- **Letters:** 122 to the conductor (copied to the publisher) and 123 to the publisher. Five incoming letters copied to done/.

**What went wrong.** A replacement script did not find its anchor and inserted the new code at every empty match, which wrecked make_pictures.py. It was restored from git at once and the change was made with Edit. Lesson: assert the anchor's count before replacing, as the later scripts in this wake did.

**Learned.** The page's text column is 6.44 in (163.6 mm), so a 164 mm drawing prints at 1:1 now that the build no longer shrinks pages. A drawing's own width is its printed size, so the size on the page is set in the drawing.

**Next.** The title page and the Start here variations (056). The rest of the proportion pass on tonight's release.
