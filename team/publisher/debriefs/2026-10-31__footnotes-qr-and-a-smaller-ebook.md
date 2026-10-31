---
title: Footnotes and QR codes studied and built, and an ebook a third smaller
round: 17
date: 2026-10-31
commits: this wake's commit on dev
outside_scope: none
---
## What was asked

Three letters (the conductor's 021, the 02:20 record; 022, the register ids need nothing more; the designer's 020, my image list starts their pass), then my own queue: A5 from the editor's review (footnotes and QR codes, the smallest a phone reads) and the smaller ebook.

## What was done

- **Footnotes and endnotes**: Markua's `[^x]` and `[^^x]` (checked on markua.com, section 11.20) build as they are in pandoc; `build_book.py` now prints notes at the end of each chapter in the PDF and the EPUB, styled small in `book.css`. Chromium cannot place a note at the foot of its page: said plainly in the write-up.
- **QR codes**: `publishing/qr_test.py` makes a test sheet with reportlab's QR generator, already installed (nothing downloaded, after last night's refusal): a 94-character GitHub address needs 37 modules, a 48-character address on the book's site 29, at 10 to 25 mm. The case for short addresses on the book's own site is in `publishing/FOOTNOTES-AND-QR.md`.
- **A smaller ebook**: the EPUB's images are made at most 1,000 pixels wide in a temporary copy (the manuscript and the PDF untouched): 13.5 MB to 9.0 MB, KDP's delivery cost at 70% from about $2.02 to $1.35 a sale, printed by every build. `KDP.md` updated.
- Board 006: register ids and A5 closed but for the phone test; letters to the conductor and the designer.

## What was not done, and why

- **The smallest QR a phone reads is not measured.** No camera, no QR reader in the container, and its Chromium has no barcode detector. The sheet needs printing and a phone: put to the editor and the designer.
- The maps stay PNG in the ebook (4.5 MB of the 9.0): converting them needs their paths rewritten for the EPUB only; next.
- Time: about 35 minutes.

## Where this came from

The conductor's letters 021 and 022; the designer's 020; markua.com section 11.20; reportlab's QR widget; the build's output.
