---
title: Type A the build's default, and $14.99 recorded
round: 30
date: 2026-11-01
commits: this wake's commit on dev
outside_scope: none
---
## What was asked

The editor's answers to the conductor's brief 28, relayed in letter 041: type A (9.5 pt), and the price is fine ($14.99, on the final page count); two checks in KDP's setup screen before the listing.

## What was done

- `build_book.py`: type A by default, B kept to compare. The book is 192 pages, the sample 13; the cover at 192 pages computed.
- `KDP.md`: type A and $14.99 with his words; the two setup checks as his steps, since they need his account.
- Board 009; a reply to the conductor.

## Where this came from

The conductor's letters 041 and 042; the build's output; `cover_size.py --pages 192 --paper white`.
