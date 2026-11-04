# The look before and after: the full book's first pages, 00:30 and 09:55 UTC

Made by conductor@book.the-ultimate-insider, 4 November 2026, about 09:58 UTC, at the editor's ask (brief 26: "before you do any changes, can you see what I mean? ... From the first batch of pages, let's say there must 10 pages before and after"). Unlike the other studies here, this one is pictures: the point is how the pages look.

**Method.** Both PDFs built locally the same way as the site's full draft (`publishing/build_book.py --book manuscript/editions/rc2-150/Book.txt --cast --figures publishing/rc2-figures.json`, the signed cover and `lab/tools/book/speakers.css`): **before** from `dev` at `89bd8a50` (00:30 UTC, the version he liked), **now** from `dev` at 09:55 UTC. Pages rendered at 40 to 60 dpi; counts over pages 3 to 40 (cover and title page left out). The sheets show only pages already published on the site; the codes in them are chapter 3's public key QR codes, cleared by security (019), and one code inside the talk's policy-page screenshot on page 6 of the before version (the talk site's own published link to ruv.sgit's policy); at this size none is readable (the largest is about 22 px).

| Pages 3 to 40 | Before | Now |
|---|---|---|
| Pages more than 35% blank at the foot | 7 | 12 |
| Content width, share of the page | 86% | 81% |
| Ink, share of the page | 14.5% | 10.2% |
| Words | 15,512 | 9,888 |
| First page of the tour (screenshots, the dashboard) | 11 | 17 |

**What it shows** (the conductor's reading): the opening (pages 3 to 16) lost its visual rhythm: before, every page there had a visual (the printable Start here card, the speaker and slide drawing, the player and policy screenshots, the greyed cast cards, the tour); now the new introduction and chapter 1 come first as text, a "Try this" card sits alone on page 12 (with a stray "Dramatised" label above it), and the narrower measure leaves more white. From page 17 the new version is richer than before (the tour, the house, the day at a glance, the concept callouts, the agent cards).

**The sheets**
- `pages-01-16-before-after.png`: pages 1 to 16, before above, now below.
- `pages-03-08-close-up.png` and `pages-09-14-close-up.png`: closer, before above, now below.
- `pages-17-32-before-after.png`: pages 17 to 32.

The fixes were proposed to him as LY1 (book.json); he signed them at about 10:35 UTC (brief 27).

## After the first LY1 change (11:05 UTC)

Built the same way from `dev` at `4320725c`, after the publisher's LY1 change (the measure, screenshots beside their text, no holes) and before the writers' changes. Pages 3 to 40:

| | Before (00:30) | 09:55 | 11:05 |
|---|---|---|---|
| Pages more than 35% blank at the foot | 7 | 12 | 10 |
| Content width, share of the page | 86% | 81% | 83% |
| Ink, share of the page | 14.5% | 10.2% | 10.8% |

Better, and still worse than the version he liked: the visuals the writers are putting back in 00 to 09 are not in yet. The publisher's own count (058) is over the whole book (22 such pages of 127, 7 of them inside a chapter), so its numbers differ from these by range, not by finding. `pages-01-16-three-builds.png`: pages 1 to 16 in the three builds, top to bottom.

## At v0.1.785 (12:05 UTC), the site's live full draft

Measured the same way on the PDF the site serves (142 pages; the earlier columns are local builds): pages 3 to 40, 9 pages more than 35% blank at the foot (7 before, 12 at 09:55, 10 at 11:05); width 83%. The writers' visuals are in, but 36 of them still print as "Figure to come" boxes (8 in pages 3 to 40), asked of the designer and the publisher. The publisher's own count (059) is over the whole book (8 holes in 141 pages).

## At v0.1.799 (17:05 UTC), the site's live full draft

The same way, on the PDF the site serves (143 pages), before the writer's work held during the hold (12:34 to 16:30) lands at its 17:28 wake: pages 3 to 40, 9 pages more than 35% blank at the foot (no gain since 12:05; 7 in the version he liked); width 83%; "Figure to come" boxes 26 in all (36 at 12:05), 7 of them in pages 3 to 40 (8 at 12:05). The publisher's own counts (060: 26 of 36 boxes filled, 9 holes in 142 pages) are over the whole book on its local build, not this range.

## At v0.1.815 (18:05 UTC), the site's live full draft

The same way, on the PDF the site serves (141 pages), after the writer's held work and the designer's and publisher's LY1 passes: pages 3 to 40, **6 pages more than 35% blank at the foot (7 in the version he liked, 12 at 09:55)**; width 83%; "Figure to come" boxes 19 in all (36 at 12:05), 5 of them in pages 3 to 40. He read it at about 17:48: "it is looking much better" (brief 32).

## At v0.1.831 (19:05 UTC), the site's live full draft

The same way, on the PDF the site serves (142 pages): pages 3 to 40, 6 pages more than 35% blank at the foot (7 in the version he liked); width 83%; "Figure to come" boxes 16 in all (36 at 12:05), 4 in pages 3 to 40. The publisher's own local build (062): 141 pages, 16 boxes, 8 near-empty pages over the whole book.

## At v0.1.860 (21:08 UTC), the site's live full draft

The same way, on the PDF the site serves (145 pages): pages 3 to 40, 6 pages more than 35% blank at the foot (7 in the version he liked); width 83%; "Figure to come" boxes 13 in all (36 at 12:05), 2 in pages 3 to 40. The publisher's own local build (064): 141 pages, 13 boxes, 9 pages more than 35% blank over the whole book.
