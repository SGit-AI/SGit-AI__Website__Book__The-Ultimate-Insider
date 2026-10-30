---
title: The EPUB fitted to small screens; EPUBCheck refused in the session
round: 13
date: 2026-10-30
commits: this wake's commit on dev
outside_scope: none; a third-party validator downloaded to the scratchpad, refused, deleted, never committed
---
## What was asked

My own next item after the cards: EPUBCheck on the EPUB, which KDP takes, and the small-screen fixes card 14 named (Appendix A's commands, the tables). Letter 015 from the conductor was a notice: card 09 is now open decision K1, the editor's; not acted on.

## What was done

- **`publishing/epub.css`**: the EPUB's own styles, written after pandoc's (`build_book.py` joins pandoc's default stylesheet and this file, because `--css` replaces pandoc's rather than adding to it). Code wraps and is set smaller, tables take the screen's width, images never exceed it, and the call-outs keep the RC1 look in colour.
- **Checked** by opening the EPUB's chapters in Chromium at 360 by 640 pixels, a small phone: in all five chapters with code or tables, the page is exactly as wide as the screen; Appendix A's commands wrap (looked at as an image).

## What did not happen, and why

- **EPUBCheck was not run.** I downloaded the W3C validator's PyPI wrapper (version 5.3.0, its hash matching PyPI's), installed it into the scratchpad, outside the repository, as the pre-review's conditions asked. Its first call happened to fail on a missing file; the second, on the real EPUB, was refused by the session's permission system as running code from outside. That is a boundary set for this session, not one for me to route around: I deleted the download and put it to the editor. Two ways: allow it in a session, or run EPUBCheck or Amazon's Kindle Previewer on his own machine on `/manuscript/the-ultimate-insider.epub` from the site.
- The `--check` flag the plan named for `build_book.py` was not added: without the validator in the session it would check nothing.

## Where this came from

The conductor's letter 015; `team/publisher/rc1-cards.md` card 14; pandoc's default `epub.css`; the build's EPUB, opened in Chromium.
