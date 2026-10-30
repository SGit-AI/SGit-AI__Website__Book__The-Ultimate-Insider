---
created: 2026-10-30T11:05:00Z
priority: medium
source: comms/mail/mailroom/publisher/conductor__004-markua.eml; book.json M1
---
# M1: the book in Markua 0.30

Target named in README.md and LEANPUB.md (done 30 October). Next: a pre-pandoc step in build_book.py translating Markua-only syntax; then captions and widths, asides, scene breaks, front and back matter.

## 30 October 2026, about 15:25 UTC

The pre-pandoc step is in: `publishing/markua.py`, run by `build_book.py` on every chapter into a temporary copy. Asides and blurbs (one-line and block forms) become call-outs in the RC1 build's look (`book.css`); attribute lines become pandoc attributes on an image, a heading or a paragraph; `{pagebreak}` breaks the page; matter markers leave empty markers. Tested on a scratch chapter (PDF and EPUB); the 18 RC1 chapters pass through unchanged. Next: the 50 call-outs and the maps into the chapters themselves as Markua, then captions and widths.

## 30 October 2026, about 17:30 UTC

RC1's figures and call-outs are in the chapters as Markua (`publishing/place_rc1.py`, run once): 39 image lines (28 infographics, 11 maps) and 50 blurbs with Markua's classes, every anchor of the conductor's build found. The book builds at 293 pages, matching the editor's RC1 PDF less its cover. The site's chapter pages show the blurb markers until the conductor applies two lines in `admin/build/build.py` (letter publisher__006). Next: captions and widths checked against the Markua spec (bracket text as caption), an EPUB stylesheet for the call-outs.
