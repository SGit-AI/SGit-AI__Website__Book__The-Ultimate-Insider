# The editor's setup sheet: Leanpub and KDP

Kept by publisher@book.the-ultimate-insider. Written 4 November 2026, about 00:40 UTC, for the editor's ask in the publisher's session ("can you help me setting up KDP and Leanpub?") and the conductor's 066, items 4 and 5. **Every account step is his, by hand**: nobody on the team logs in, uploads, submits or pays, and no account number, login, bank or tax detail ever goes in this repository. Where a screen and this sheet disagree, the screen wins; tell the publisher so the sheet is corrected.

The book is the full book (LP1), the one printed (PR2). It is not final yet: the page count, and with it the spine, the cover's width and the printing cost, move until the editor calls it final. Figures below are at today's count, **the interior 141 pages, printed as 142** (142 with the cover page). They rose from 112 on 4 November: about 01:10 UTC a fault that had shrunk every page to about 0.85 was fixed (the body now prints at the 9.5 pt the editor signed), and about 01:55 UTC the full book took its own measure and spacing and left its sources out of print (the editor's notes 06 and 10).

## 1. Leanpub

### The one choice first: how Leanpub gets the book (open, his)

Signed today: L2, Leanpub builds from `main` in its Git and GitHub mode. Since then RC2 has been laid out by our own build (`publishing/build_book.py --cast`): speakers, bands, words boxes, the margin clock, the figure map. Leanpub's Git mode does not use our build: it builds its own PDF and EPUB from `manuscript/Book.txt` with Markua, so the cast layout and the drawings placed by `publishing/rc2-figures.json` would not appear, and `manuscript/Book.txt` today lists RC1, not RC2. The options:

| | What happens | For | Against |
|---|---|---|---|
| **A. Git mode, as L2 signed** | Leanpub builds from `main`; RC2 would need a Markua version of every chapter, and a `manuscript/Book.txt` pointing at it | Leanpub's own EPUB and its print-ready PDF export; previews on every merge | RC2's layout lost; a second form of every chapter to keep in step; days of work |
| **B. Upload mode ("Bring Your Own Book")** | he uploads our full-book PDF (the online full draft's final version) and, when built, our EPUB | the book on Leanpub exactly as designed; nothing to translate | Leanpub "does not do any processing" of an uploaded PDF and generates no EPUB from it; every new version is a new upload; Leanpub's author services generally not available for upload books |
| **C. Both, later** | B first, A only if a Leanpub-built EPUB or export is wanted | quickest to sale | as B |

The conductor opens this as a decision; nothing changes until he signs. The steps below are B's; A's are `publishing/LEANPUB.md`, steps 1 to 3.

### Steps (option B)

1. Leanpub: create a book. Title and subtitle as signed (NS1): *One Human, Nine Agents, Nineteen Hours*; *How a factory of AI agents built a presentation in a day, and how to build yours*. The URL slug is public and looks permanent: `one-human-nine-agents` was free on 2 November (a check, not a reservation).
2. Writing mode: **Upload**, "By uploading ebook files directly (PDF and/or EPUB)", then the book's Upload page.
3. Upload the PDF: the full book with cover A on page 1 (the release's full draft today; the final one when he calls it final). Leanpub sells it as uploaded. An EPUB is not built yet for RC2 (see section 4); a PDF-only book is allowed.
4. Settings, About: subtitle, teaser, meta description, description: paste from `publishing/listing.md` (traced and cleared).
5. Settings, Book Cover: one image, 1800 by 2700 pixels, from cover A: the designer's to export.
6. Store, Pricing (L1, signed): minimum **$0**, suggested **$19.99**, and **untick** "Free purchases of this book require a Reader, Standard or Pro membership".
7. Preview the page; then Publish. Every reader gets every new version, whatever they paid.

## 2. KDP, the paperback: every field, by screen

**Ours** means signed or already traced. **Proposal** means the publisher's suggestion, his to take or change. **His choice** means only he can say.

### Paperback details

| Field | Value | Source |
|---|---|---|
| Language | English | ours |
| Book title | One Human, Nine Agents, Nineteen Hours | ours (NS1) |
| Subtitle | How a factory of AI agents built a presentation in a day, and how to build yours | ours (NS1) |
| Series | Gen ZX Founders (create the series in KDP; this is book 1 unless he numbers it otherwise) | ours (G1); the number his choice |
| Edition number | leave blank (or 1) | his choice |
| Author | Dinis Cruz | ours (cover A) |
| Contributors | none proposed | his choice |
| Description | the Description section of `publishing/listing.md`, as traced (KDP counts characters; it fits easily) | ours |
| Publishing rights | "I own the copyright and I hold the necessary publishing rights" | his choice: his to confirm |
| Primary audience | sexually explicit images or title: **No**; reading age: leave blank (adult) | proposal |
| Primary marketplace | Amazon.com | proposal |
| Categories (three) | Computers and Technology, Artificial Intelligence; Business and Money, Entrepreneurship; Computers and Technology, Software Development | proposal: the picker's own names may differ |
| Keywords (seven) | AI agents; multi-agent AI team; agentic AI workflows; AI for solo founders; build with AI agents; AI insider risk; git for AI collaboration | proposal |
| Low-content book, large print | No, No | ours |

### Paperback content

| Field | Value | Source |
|---|---|---|
| ISBN | KDP's free ISBN (KDP named as publisher, the book "Independently published") or his own | his choice |
| Publication date | leave blank (the day it goes live) | proposal |
| Ink and paper | **standard colour, white paper** | ours (INK1, 1 November) |
| Trim size | **7.44 x 9.69 in** (Crown Quarto, a large trim for KDP) | ours (P2) |
| Bleed | **No bleed** | ours (nothing reaches the page edge) |
| Cover finish | matte or glossy | his choice |
| Reading direction | left to right | ours |
| Manuscript | the interior PDF (section 3) | the publisher's, at the final count |
| Cover | the full cover PDF (section 3), not Cover Creator | the designer's |
| AI-generated content | see below | his answer |

**The AI question.** KDP asks, per title and per format, whether the book contains AI-generated content: text, images, translations (reported in KDP's own forum notice and in guides; read the exact question on his screen). The facts: the book's text was written by the writer agent and the team; the drawings were drawn by agents; screenshots are of the talk's site, which agents built; there are no translations. That points to "yes" for text and images. The answer is his to give.

### Paperback rights and pricing

| Field | Value | Source |
|---|---|---|
| Territories | worldwide rights | his choice |
| Primary marketplace | Amazon.com | proposal |
| List price | **$14.99**, signed on 1 November ("price is ok") at 192 pages, to be confirmed on the final count | ours (KDP.md) |
| What it earns, today's count | printing at large trim, standard colour: $1.00 + $0.0402 x 142 = **$6.71** a copy; at $14.99 and 60%, about **$2.29** a copy | KDP's printing-cost page, read 1 November; moves with the final count |
| A lower price, sales first | the floor at 60% is $6.71 / 0.6 = about **$11.18**; at $11.99, about $0.49 a copy; $9.99 and $10.99 are below the floor | proposal, his choice |
| Expanded distribution | at 40%, the floor is $6.71 / 0.4 = about **$16.77**: not possible at $14.99 | his choice |
| Proof copy | order one before publishing (his brief) | ours |

Two checks only his screen can do (`KDP.md`): standard colour offered at 7.44 x 9.69 in, and KDP's own minimum price at or below the price he sets.

## 3. KDP, the Kindle ebook: what differs

- Same title, subtitle, series, author, description, categories and keywords (the ebook has its own fields; copy them).
- **Kindle price: his choice; K1 is open** (deferred, "that will depend how I'll set up on KDP"): with L1's $0 on Leanpub, Amazon may match it and make the Kindle book free.
- **KDP Select: recommended No** (it asks for ebook exclusivity, which Leanpub would break).
- DRM: his choice. AI-generated content: the same facts as above.
- The file: an EPUB of RC2 is **not built yet** (section 4).

## 4. The print-ready files: where they stand

| File | State today | Against KDP's rules |
|---|---|---|
| **Interior PDF** (the full book without its cover page) | test build: 141 pages, 7.44 x 9.69 in (`build_book.py` without `--cover`), in the publisher's scratchpad, not committed; the final one at the final count | fonts: all 34 embedded; transparency: none found at page level (KDP's previewer is the last word); size: well under 650 MB |
| Its images | 17 raster images; **14 screenshots of the talk's site at 199 dots per inch** (1280 by 800 pixels at the printed width); the drawings are vector and print sharp | below KDP's "at least 300 DPI", and KDP says not to enlarge to reach it. Options for him: print the screenshots smaller (at 300 dpi a 1280-pixel shot is 4.27 in wide), or accept KDP's warning on the proof (KDP's pages read do not say whether it refuses or only warns) |
| **Cover PDF** (back, spine, front, 0.125 in bleed) | the front is cover A; **the back and the spine are not drawn**: the designer draws them from the final count | at 142 printed pages, white paper: spine **0.320 in** (8.1 mm), spine text allowed; full cover **15.450 x 9.940 in**, 4635 x 2982 px at 300 dpi (`publishing/cover_size.py --pages 142 --paper white`) |
| **EPUB** (Kindle; Leanpub if wanted) | not built for RC2 (`--no-epub`): the cast layout has not been tried in an EPUB | to build and check in Kindle Previewer once the book is final |
| Leanpub's own print-ready export | a Leanpub feature for books it generates (Git mode); not ours under option B | our interior is the print file |

## Sources (read 4 November 2026 unless said)

- Leanpub, Upload mode and what it does with an uploaded PDF: help.leanpub.com/en/articles/109306, /2829677, /6020853, /789845, /7033738; the print-ready export: /3333903, /1852748, /5375371. Leanpub's other steps: `publishing/LEANPUB.md` (read 30 October).
- KDP categories (three) and primary audience: kdp.amazon.com/en_US/help/topic/G201276790. Seven keywords: third-party guides, and KDP's keywords help title (its page not read). The AI-generated content question: KDP's forum notice as quoted in news reports of September 2023 (theBookseller, ADTmag) and current guides; KDP's own help page was not found.
- Printing cost and royalty, trim, bleed, margins, fonts, transparency, resolution: `publishing/KDP.md` and its sources (read 30 October and 1 November).
