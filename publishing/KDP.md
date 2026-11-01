# Amazon KDP: the ebook and the paperback, what the editor does by hand

Kept by publisher@book.the-ultimate-insider. Written 30 October 2026 from Amazon KDP's help pages, read that day (links at the end). **The editor performs every step here**: each needs his KDP account, his tax and bank details, or his money; no agent touches the account, and none of those details ever goes in this repository. Where a step and KDP's screen disagree, the screen wins; tell the publisher so this file is corrected.

The target (the editor's brief): on Amazon by Web Summit, Monday 9 November 2026, with a paperback proof ordered. The brief allows up to 72 hours for KDP's review, so the last safe day to submit is **Thursday 5 November**, and earlier is better: a rejected file costs another review.

## The ebook (Kindle)

1. **The file**: the EPUB from `publishing/build_book.py` (`_site/manuscript/the-ultimate-insider.epub`), or Leanpub's own EPUB once the Leanpub book exists. KDP accepts EPUB and recommends checking it in Kindle Previewer before upload; PDF is accepted but not recommended for an ebook.
2. In KDP: create a Kindle eBook; title, subtitle and description (the publisher drafts them in `publishing/listing.md` once the title is signed); upload the EPUB and the cover; preview; price; publish.
3. **Price matching (open decision K1, yours).** KDP's Digital Book Pricing Page, part of the KDP agreement: Amazon may sell the ebook at a lower price to match another channel, and "if your Digital Book is available through another sales channel for free, we may also make it available for free", with a royalty of zero while it does. L1's $0 minimum on Leanpub is that case. KDP itself cannot list a book at free. Nothing here acts on K1; the options are in `team/publisher/rc1-cards.md`, card 09.
4. **Delivery costs, if you choose the 70% royalty.** Amazon.com charges US $0.15 per megabyte of the ebook file on every sale under the 70% option (same page). Since 31 October `build_book.py` makes the EPUB's images at most 1,000 pixels wide (the PDF keeps them full size), and its PNG maps in 256 colours, so the EPUB is 6.5 MB, about **$0.97 a sale** (it was 13.5 MB, $2.02, on 30 October); the build prints the figure every time. How the 35% option differs is on the same page. The list-price range each option allows is on the same page; read it there when you price, the publisher has not set it out here.
5. **The EPUB itself**: `publishing/epub.css` fits it to small screens (commands wrap, tables fit; checked at 360 pixels wide). **EPUBCheck has not been run**: the session refused to run the downloaded validator, so run Kindle Previewer (KDP's recommendation) or EPUBCheck on it yourself, or allow EPUBCheck in a session. The largest EPUB KDP accepts is not stated on the pages read.
6. **Selling on both Leanpub and Amazon is fine with Leanpub** (its help: no restriction). One thing to decide before step 2: KDP Select (Kindle Unlimited) asks for ebook exclusivity, which would conflict with Leanpub. **Recommended: do not enrol in KDP Select.**

## The paperback

| What | KDP's rule | Ours now |
|---|---|---|
| Trim size | 6 by 9 inches is KDP's most common US trim size; anything wider than 6.12 or taller than 9 in is a large trim, priced higher | Crown Quarto, 7.44 by 9.69 in (P2, signed): a large trim |
| Page count | at least 24 pages | 192 (type A, 9.5 pt) or 185 (type B, 9 pt) at Crown Quarto, 1 November 2026; the type size is still the editor's to choose |
| Bleed | only if something reaches the page edge; 0.125 inch | none: no full-bleed images planned |
| Inside (gutter) margin | grows with page count (KDP's margins table) | 0.625 in, the editor's yes (P2); meets KDP's minimum up to 500 pages |
| Outside margins | at least 0.25 inch without bleed (0.375 inch with) | 0.375 outside, 0.5 top, 0.625 bottom: the designer's, above the minimum |
| Spine width | page count x 0.002252 inch (white paper) or x 0.0025 inch (cream) | at 192 pages on white paper (standard colour prints on white): 0.432 in; full cover 15.562 by 9.94 in (`cover_size.py --pages 192 --paper white`); compute it again on the final PDF |
| Spine text | only from about 79 pages up | will apply |
| Cover | one PDF: back, spine and front, plus 0.125 inch bleed all round; width = bleed + back + spine + front + bleed | the designer's job; the publisher computes the size |
| Image resolution | "at least 300 DPI", for the interior and the cover; do not enlarge an image to reach it | below it today: at the 4.7-inch text width the narrowest images print at about 200 dots per inch (`team/publisher/rc1-cards.md`, card 05); KDP's pages read do not say whether lower is refused or only warned |
| Fonts | "fully embedded" in interior and cover files | all 19 fonts in today's PDF embedded (checked with `pdffonts`) |
| Transparency | flatten transparent objects and layers before upload | the PDF is printed by Chromium; to check in KDP's previewer |
| File size | at most 650 MB for the interior PDF | 16.8 MB |
| Colour in black ink | not stated on the pages read | colour images will print in grey; check the proof (card 04) |

KDP's minimum gutter by page count (its margins page, read 30 October 2026): 24 to 150 pages, 0.375 inch; 151 to 300, 0.5; 301 to 500, 0.625; 501 to 700, 0.75; 701 to 828, 0.875. Our 0.75 inch meets it up to 700 pages; the plan's book is well under that.

## The ink, chosen: standard colour, sales before profit (the editor, 1 November 2026)

The editor, in the publisher's session, about 00:20 UTC on 1 November 2026: "So for now we're going to go with standard color, which is okay. And remember that in the beginning I'm not really interested in the profit, I'm more interested in the sales."

At Crown Quarto (P2, signed), 7.44 x 9.69 in is a **large trim** for KDP ("more than 6.12 inches ... in width or more than 9 inches ... in height": the trim-size page). Large-trim printing cost on Amazon.com (KDP's printing-cost page, read 1 November 2026): standard colour $1.00 + $0.0402 a page (72 to 600 pages); black $1.00 + $0.017 a page; premium colour $1.00 + $0.08 a page.

| Build | Pages (printed) | Standard colour, per copy | Lowest list price at 60% | At $14.99, per copy |
|---|---|---|---|---|
| Type A, 9.5 pt | 192 | $8.72 | $14.53 | about $0.27 |
| Type B, 9 pt | 185 in the PDF, printed as 186 (KDP prints an even count) | $8.48 | $14.13 | about $0.51 |

**For sales first**, the publisher's proposal (the price is the editor's): the paperback at the first price that covers printing, **$14.99**, which earns a few tens of cents a copy; it moves with the final page count, so it is set on the final PDF. Two things to check in KDP's setup screen: that standard colour is offered at this custom size (KDP's pages list standard colour for large trim but do not say so for 7.44 x 9.69), and the minimum price KDP itself shows. The cover at 192 pages on white paper: `cover_size.py --pages 192 --paper white` (standard colour prints on white paper).

## The ink: what a printed copy costs (first reading, at 6 x 9, superseded by the section above) 

KDP's printing cost depends on the ink and the page count only; its page lists no charge per image, so one picture or a thousand cost the same within an ink (it does not say so in words: it simply prices nothing but ink and pages). Amazon.com, regular trim (6 x 9 in), from KDP's printing-cost page (kdp.amazon.com/en_US/help/topic/G201834340, no date shown):

| Ink | Cost per copy | At 255 pages | At 300 pages | Lowest list price at 60% (cost / 0.6) |
|---|---|---|---|---|
| Black | $1.00 + $0.012 a page (110 to 828 pages) | $4.06 | $4.60 | under $9.99, so the 50% rate applies: about $8.12 (255) |
| Standard colour | $1.00 + $0.0255 a page (72 to 600 pages) | $7.50 | $8.65 | $12.50 (255), $14.42 (300) |
| Premium colour | $1.00 + $0.065 a page | $17.58 | $20.50 | $29.29 (255), $34.17 (300) |

The royalty (kdp.amazon.com/en_US/help/topic/G201834330, no date shown): "(Royalty rate x list price) - printing costs = royalty"; 50% up to $9.98 and 60% from $9.99 on Amazon.com. At the suggested $19.99 (L1's figure for Leanpub, used here only as a yardstick): black earns about $7.93 a copy, standard colour about $4.49, and premium colour cannot be sold at that price (it costs more to print than 60% returns). KDP states a minimum list price but not its formula; cost divided by the rate is the publisher's reading. The PDF and the EPUB cost nothing to print; the EPUB's delivery cost at the 70% ebook royalty is per megabyte (above), so a heavier, more visual ebook costs more per sale.

Steps for the editor, once the interior PDF and the cover PDF exist:

1. Create a paperback in KDP; the same title and description as the ebook.
2. Take KDP's free ISBN or use his own. **His decision**; KDP's free ISBN names KDP as the publisher.
3. Choose black ink and white or cream paper (recommended: cream, the usual for prose), 6 by 9, no bleed, matte or glossy cover.
4. Upload the interior PDF and the cover PDF; read the whole proof in KDP's previewer.
5. **Order a printed proof copy** before publishing (the brief: "a paperback proof ordered"); its delivery time is KDP's and the courier's, so order it the day the files are ready.
6. Price, then publish.

## What the publisher does next for this

- Done 30 October: the gutter checked against KDP's margins table (0.75 inch, enough up to 700 pages).
- Done 30 October: `publishing/cover_size.py` gives the designer the full cover's size and the spine from the interior PDF (`--pdf`) or a page count (`--pages`), white or cream paper; an odd page count is rounded up to even, as printed.
- The QR codes on the page pointing to the record (the positioning brief's "paper that talks both ways"): proposed with the designer, not before the plan is signed.

## Sources (read 30 October 2026)

- Trim sizes and page counts: kdp.amazon.com/en_US/help/topic/G201834180
- Cover size, spine width and spine text: kdp.amazon.com/en_US/help/topic/G201953020
- eBook manuscript formats (EPUB accepted, PDF not recommended): kdp.amazon.com/en_US/help/topic/G200634390
- The margins table, "Set Trim Size, Bleed, and Margins": kdp.amazon.com/en_US/help/topic/GVBQ3CMEQW3W2VL6 (read on the second try; the first address tried, G201834190, did not carry it)
- Trim sizes, regular and large: kdp.amazon.com/en_US/help/topic/G201834180 (read 1 November 2026)
- Printing cost by ink and the paperback royalty: kdp.amazon.com/en_US/help/topic/G201834340 and /G201834330 (read 31 October 2026)
- Price matching, the free price elsewhere and the delivery cost of US $0.15 per MB: the Digital Book Pricing Page, kdp.amazon.com/help/topic/G200634500 (last updated 21 April 2026)
- Image resolution, fonts and transparency: kdp.amazon.com/en_US/help/topic/G201834260 and /G201857950; the 650 MB limit: /G202145060 and /G201857950 (no dates shown; read 30 October 2026, about 22:55 UTC)
- The 72-hour review time is the editor's brief (`briefs/2026-10-30/1-book-conductor-brief.md`); KDP's formats page does not state it.
