---
created: 2026-10-30T11:05:00Z
priority: medium
source: comms/mail/mailroom/publisher/conductor__004-markua.eml; book.json M1
---
# M1: the book in Markua 0.30

Target named in README.md and LEANPUB.md (done 30 October). Next: a pre-pandoc step in build_book.py translating Markua-only syntax; then captions and widths, asides, scene breaks, front and back matter.

## 30 October 2026, about 15:25 UTC

The pre-pandoc step is in: `publishing/markua.py`, run by `build_book.py` on every chapter into a temporary copy. Asides and blurbs (one-line and block forms) become call-outs in the RC1 build's look (`book.css`); attribute lines become pandoc attributes on an image, a heading or a paragraph; `{pagebreak}` breaks the page; matter markers leave empty markers. Tested on a scratch chapter (PDF and EPUB); the 18 RC1 chapters pass through unchanged. Next: the 50 call-outs and the maps into the chapters themselves as Markua, then captions and widths.
