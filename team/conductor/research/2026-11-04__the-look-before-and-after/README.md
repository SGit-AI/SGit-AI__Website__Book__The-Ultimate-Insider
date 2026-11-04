# The look before and after: the full book's first pages, 00:30 and 09:55 UTC

Made by conductor@book.the-ultimate-insider, 4 November 2026, about 09:58 UTC, at the editor's ask (brief 26: "before you do any changes, can you see what I mean? ... From the first batch of pages, let's say there must 10 pages before and after"). Unlike the other studies here, this one is pictures: the point is how the pages look.

**Method.** Both PDFs built locally the same way as the site's full draft (`publishing/build_book.py --book manuscript/editions/rc2-150/Book.txt --cast --figures publishing/rc2-figures.json`, the signed cover and `lab/tools/book/speakers.css`): **before** from `dev` at `89bd8a50` (00:30 UTC, the version he liked), **now** from `dev` at 09:55 UTC. Pages rendered at 40 to 60 dpi; counts over pages 3 to 40 (cover and title page left out). The sheets show only pages already published on the site; the only codes in them are chapter 3's public key QR codes, cleared by security (019), and at this size none is readable.

| Pages 3 to 40 | Before | Now |
|---|---|---|
| Pages more than 35% blank at the foot | 7 | 12 |
| Content width, share of the page | 86% | 81% |
| Ink, share of the page | 14.5% | 10.2% |
| Words | 15,512 | 9,888 |
| First page of the tour (screenshots, the dashboard) | 11 | 17 |

**What it shows** (the conductor's reading): the opening (pages 3 to 16) lost its visual rhythm: before, every page there had a visual (the printable Start here card, the speaker and slide drawing, the player and policy screenshots, the greyed cast cards, the tour); now the new introduction and chapter 1 come first as text, a "Try this" card sits alone on a page, and the narrower measure leaves more white. From page 17 the new version is richer than before (the tour, the house, the day at a glance, the concept callouts, the agent cards).

**The sheets**
- `pages-01-16-before-after.png`: pages 1 to 16, before above, now below.
- `pages-03-08-close-up.png` and `pages-09-14-close-up.png`: closer, before above, now below.
- `pages-17-32-before-after.png`: pages 17 to 32.

The fixes are proposed to him as LY1 (book.json), open: nothing changes until he says go.
