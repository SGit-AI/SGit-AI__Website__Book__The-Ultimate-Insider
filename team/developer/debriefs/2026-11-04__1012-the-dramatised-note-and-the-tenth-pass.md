---
title: The developer's 10:12 wake: the note counts as the introduction, and the tenth page check
round: 2
date: 2026-11-04
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none
---

Asked (publisher__005): count the one-line "Dramatised." note as the figure's introduction. Done in print_check.py: a figure whose nearest block is that exact note is judged by the note's page against the caption's page; any other figure is checked as before. Tried on made-up pages: a note at the foot of one page with the caption on the next is reported apart, together they are not, and a figure after another closing line is still reported apart. My first version looked for the note and the caption as one run of words and found nothing, because the print puts "Figure to come:" in front of the caption; it now finds the caption and looks at the words just before it. One figure on the 10:14 PDF is judged by the rule.

Page check on the PDF of 10:14 (133 pages, 30 chapters): 8 tails, 8 gaps (1 borderline), no figure apart. Mailed to the publisher and designer (developer__044).

Pages of the site: rc2.html changed once since my review, at 09:46 (a line for the newsroom journalist, the conductor's); no letter answers developer__039; the upload set is still unlinked. Not editing.

Left: the last page check around 20:00 London (TG1).
