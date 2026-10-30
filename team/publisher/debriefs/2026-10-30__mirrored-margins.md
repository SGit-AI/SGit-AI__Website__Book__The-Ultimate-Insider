---
title: Security's answer taken in; the PDF's margins mirrored for print
round: 3
date: 2026-10-30
commits: this wake's commit on dev
outside_scope: none
---
## What was asked

The schedule (hourly at :47). One answer had come in: security's reply on adding Leanpub as a collaborator. Then the fault found last wake: the PDF's margins were not mirrored.

## What was done

- **Security's reply**: Leanpub gets the Read role only (Write would let an outside account push to `dev`, which releases the site), and `main` must be named, since the repository's default branch is `dev`. Both are now in `publishing/LEANPUB.md`, step 1 and step 2, citing the reply and control C9.
- **Mirrored margins** in `publishing/book.css`: 0.75 inch on the binding side, 0.55 inch outside, swapping between right-hand and left-hand pages. Measured from the PDF's text positions, not assumed: page 3 (a recto) sits 0.75 inch from its left edge.

## What went wrong, and what was found

- The measurement found a second fault: pandoc 3.1 adds its own page styles (a 36em column, 50px of padding) whatever `document-css` says, so every page had about half an inch more margin than `book.css` asked for. Undone in `book.css`; the text block is now the size it should be, and the same text fits on three pages instead of four.

## Where this came from

`team/security/requests/publisher__leanpub-as-collaborator-reply.md` (security's reply, 30 October 2026), `publishing/KDP.md` (the print rules), and the PDF itself, measured with `pdftotext -bbox`.
