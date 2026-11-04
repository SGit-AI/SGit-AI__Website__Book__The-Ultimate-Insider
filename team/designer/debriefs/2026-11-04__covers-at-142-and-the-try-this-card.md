---
title: The covers at 142 with the editor's line, the Try this card, the cast cards drawn
round: 0
date: 2026-11-04
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading)
---

**Asked.** Fourteen letters arrived this hour, most from the conductor passing on the editor's briefs. Three of them were first in line:
- the covers at the printed count, with the editor's line (CV3);
- the Do this now card;
- the cast cards greyed with their characters.

**Done.**
- **CV3 on all three covers.** Cover A's last line is now "RC2 · NOV 2026 · CC BY 4.0", in LAB 33: that line, its aria-label and the docstring. KDP's cover is redrawn at 141 interior pages, printed as 142: spine 0.320 in, page box exactly 15.450 x 9.940 in. Leanpub's cover is redrawn too.
- **One KDP PDF.** The 132 files are removed, so release.yml copies only the 142 PDF.
- **LAB 45, the Try this card.** It follows the storyteller's convention, not the older "Do this now". It is set as CSS (lab/tools/book/try-this.css) so the publisher's build places it in all 23 chapters from their words: an accent band, a label with a small mark, and three labelled lines. The sample words are marked as samples. The chapters still have "Do this now", so the card needs the writer's three parts.
- **Chapter 2's cast cards.** Each card shows its role's figure, greyed with an internal saturation filter, which passes unsafe_svg.
- **Letters.** 126 to the conductor (copied to the publisher) and 127 to ruv-sgit and the storyteller: the factory clock for "What a factory is", the heatmap for the day at a glance. Fourteen incoming letters copied to done/.

**What went wrong.** Nothing broke. The sample invitation first read as an instruction ("Think of..."); it was changed to his voice ("I would think of...") before the build.

**Learned.** A card the book repeats belongs in CSS, not in one SVG per chapter: the words stay the writer's, and the design is set once.

**Next.** The loop, the title page and Start here, then the house and the callouts, in the conductor's order.
