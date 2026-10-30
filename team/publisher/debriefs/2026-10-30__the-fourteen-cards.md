---
title: The fourteen cards drafted as the publisher, answered; KDP may match a free Leanpub price
round: 12
date: 2026-10-30
commits: this wake's commit on dev
outside_scope: none
---
## What was asked

The handover's fourth item: adopt, change or withdraw the 14 cards a conductor sub-agent drafted as the publisher for the RC1 companion the editor is reading on paper, checking three outside facts first. Letter 014 (the conductor applied my site patch) filed.

## What was done

- **Three facts checked** on official pages by a research sub-agent, quoted and dated: KDP's Digital Book Pricing Page, Markua's specification (0.31.50) on images and on crosslinks.
- **`team/publisher/rc1-cards.md`**: my verdict on each card, with reasons. Seven adopted, six changed, one withdrawn. The conductor's annotations file is not edited; the letter to the conductor (`publisher__007`) points at mine.
- The image sizes card 05 talks about, measured.

## What was found

- **KDP may price the Kindle edition at free.** Its pricing page, part of the KDP agreement, says Amazon may match a lower price elsewhere and, if the ebook is free elsewhere, "may also make it available for free", with no royalty while it is. L1's $0 minimum on Leanpub is exactly that case. It does not stop a Kindle listing; it is a consequence the editor did not have in front of him when he signed L1. I gave options and no recommendation over his reasons.
- **Every image's caption is its alt text.** Markua reads the bracket text as alt text and shows it as the caption when there is no title. Fixing that is a per-image job, after the captions are settled.
- Four of the cards were overtaken by the day's work (the move, the infographics, the cover, the call-outs). Drafted cards age fast when the team moves hourly; answering them the same day is what keeps the companion honest.

## What was hard, or inferred

- No page settled whether Markua's `#n` crosslink prints a number when headings show none; I wrote it down as a test for the first Leanpub preview instead of guessing.
- The 300 dots per inch print guideline in card 05 is the usual one; I did not re-read KDP's page on it this wake and said so.
- Time: about 25 minutes, the research sub-agent's 3 minutes alongside.

## Where this came from

`team/conductor/rc1/annotations/publisher.json` and `SCHEMA.md`; kdp.amazon.com/help/topic/G200634500 and A1PEZSREZLRJ1Y, kdp.amazon.com/terms-and-conditions; markua.com; `manuscript/resources/images/`; the conductor's letter 014.
