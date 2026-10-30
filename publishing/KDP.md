# Amazon KDP: the ebook and the paperback, what the editor does by hand

Kept by publisher@book.the-ultimate-insider. Written 30 October 2026 from Amazon KDP's help pages, read that day (links at the end). **The editor performs every step here**: each needs his KDP account, his tax and bank details, or his money; no agent touches the account, and none of those details ever goes in this repository. Where a step and KDP's screen disagree, the screen wins; tell the publisher so this file is corrected.

The target (the editor's brief): on Amazon by Web Summit, Monday 9 November 2026, with a paperback proof ordered. The brief allows up to 72 hours for KDP's review, so the last safe day to submit is **Thursday 5 November**, and earlier is better: a rejected file costs another review.

## The ebook (Kindle)

1. **The file**: the EPUB from `publishing/build_book.py` (`_site/manuscript/the-ultimate-insider.epub`), or Leanpub's own EPUB once the Leanpub book exists. KDP accepts EPUB and recommends checking it in Kindle Previewer before upload; PDF is accepted but not recommended for an ebook.
2. In KDP: create a Kindle eBook; title, subtitle and description (the publisher drafts them in `publishing/listing.md` once the title is signed); upload the EPUB and the cover; preview; price; publish.
3. **Selling on both Leanpub and Amazon is fine with Leanpub** (its help: no restriction). One thing to decide before step 2: KDP Select (Kindle Unlimited) asks for ebook exclusivity, which would conflict with Leanpub. **Recommended: do not enrol in KDP Select.**

## The paperback

| What | KDP's rule | Ours now |
|---|---|---|
| Trim size | 6 by 9 inches is KDP's most common US trim size | the PDF is 6 by 9 (`publishing/book.css`) |
| Page count | at least 24 pages (black ink, white or cream paper) | 4 today; the plan's 48,200 words should give well over 150 |
| Bleed | only if something reaches the page edge; 0.125 inch | none: no full-bleed images planned |
| Inside (gutter) margin | grows with page count (KDP's margins table) | mirrored since 30 October: 0.75 inch on the binding side, 0.55 inch outside (`publishing/book.css`); to check against KDP's margins table once read |
| Spine width | page count x 0.002252 inch (white paper) or x 0.0025 inch (cream) | computed once the page count is known |
| Spine text | only from about 79 pages up | will apply |
| Cover | one PDF: back, spine and front, plus 0.125 inch bleed all round; width = bleed + back + spine + front + bleed | the designer's job (not staffed); the publisher computes the size |

Steps for the editor, once the interior PDF and the cover PDF exist:

1. Create a paperback in KDP; the same title and description as the ebook.
2. Take KDP's free ISBN or use his own. **His decision**; KDP's free ISBN names KDP as the publisher.
3. Choose black ink and white or cream paper (recommended: cream, the usual for prose), 6 by 9, no bleed, matte or glossy cover.
4. Upload the interior PDF and the cover PDF; read the whole proof in KDP's previewer.
5. **Order a printed proof copy** before publishing (the brief: "a paperback proof ordered"); its delivery time is KDP's and the courier's, so order it the day the files are ready.
6. Price, then publish.

## What the publisher does next for this

- Check the gutter against KDP's margins table once it is read (mirrored margins done 30 October).
- Done 30 October: `publishing/cover_size.py` gives the designer the full cover's size and the spine from the interior PDF (`--pdf`) or a page count (`--pages`), white or cream paper; an odd page count is rounded up to even, as printed.
- The QR codes on the page pointing to the record (the positioning brief's "paper that talks both ways"): proposed with the designer, not before the plan is signed.

## Sources (read 30 October 2026)

- Trim sizes and page counts: kdp.amazon.com/en_US/help/topic/G201834180
- Cover size, spine width and spine text: kdp.amazon.com/en_US/help/topic/G201953020
- eBook manuscript formats (EPUB accepted, PDF not recommended): kdp.amazon.com/en_US/help/topic/G200634390
- The margins table (G201834190, "Set Trim Size, Bleed, and Margins") was not readable from this session; the gutter values come from it once read.
- The 72-hour review time is the editor's brief (`briefs/2026-10-30/1-book-conductor-brief.md`); KDP's formats page does not state it.
