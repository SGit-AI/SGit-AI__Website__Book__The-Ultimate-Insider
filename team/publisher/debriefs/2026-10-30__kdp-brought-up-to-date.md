---
title: KDP.md brought up to date: price matching, a $2 delivery cost, the 300 DPI rule and today's spine
round: 14
date: 2026-10-30
commits: this wake's commit on dev
outside_scope: none
---
## What was asked

My own next item: `publishing/KDP.md` current before the editor submits (the last safe day is Thursday 5 November). No new mail; no hold.

## What was done

- **Price matching**: KDP may make the Kindle edition free to match Leanpub's $0 minimum, with no royalty; written into the ebook steps, pointing at open decision K1, acting on nothing.
- **The delivery cost, new this wake**: under the 70% royalty Amazon.com charges US $0.15 per MB on every sale; today's 13.5 MB EPUB would cost about $2.02 a sale, nearly all of it the images. Smaller ebook images are the lever, the editor's to pull when he prices.
- **The paperback table**: 293 pages from today's build; spine 0.735 inch on cream (0.662 on white), full cover 12.985 by 9.25 inches, from `cover_size.py`; KDP's "at least 300 DPI" against our narrowest images at about 200; all 19 fonts embedded (checked with `pdffonts`); the 650 MB limit against our 16.8 MB; transparency and colour in black ink to check on the proof.
- Sources added, each page with its date where KDP shows one.

## What was hard, or inferred

- KDP's pages do not say whether an image under 300 DPI is refused or only warned, nor the largest EPUB accepted, nor how colour converts in a black-ink interior; each is written as not stated, not guessed.
- I left out the 70% option's list-price range and the 35% option's terms: the sub-agent's reading did not cover them, and a price rule half-remembered is how a submission bounces. KDP.md sends the editor to the page.
- Time: about 15 minutes, the KDP lookup (a sub-agent, one minute) alongside.

## Where this came from

kdp.amazon.com help topics G200634500 (21 April 2026), G201834260, G201857950 and G202145060, read 30 October 2026; `publishing/cover_size.py --pages 293`; `pdffonts` on the build's PDF.
