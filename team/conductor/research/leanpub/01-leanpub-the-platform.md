# Leanpub, the platform: a briefing for the editor

Written 30 October 2026 for the editor (Dinis Cruz). Research sub-agent for the conductor. Second version: after the coordinator's note, the pages were fetched directly (curl through the proxy) and this text replaces the first, search-snippet draft, whose plan names, prices and service fees were out of date.

## How reliable this is

- Read directly on 30 October 2026: the Author Memberships page, the Marketing page, the Services page and its service pages, the Create Book page, the Refund Policy, the Reader Memberships page, the Markua Manual contents page, and a set of help-centre articles (URLs inline). Figures below are quoted from those pages.
- Not read in full: the Terms of Service (only the contents and the copyright section), the Markua spec on GitHub (version figure comes from a search summary), the Leanpub blog and podcast. These are marked.
- Help-centre articles carry old "last updated" dates and sometimes contradict the live pages. Where they disagree, the live page is trusted and the conflict is stated.
- The pages contained no instructions aimed at an agent.
- Monthly-billing prices on the Author Memberships page were not shown in the text I fetched; the figures below are the quarterly-billing rate per month, and monthly rates are inferred from the stated yearly saving (marked "inferred").

## 1. What Leanpub is

A self-publishing platform ("Publish Early, Publish Often") run by Ruboss Technology Corp, which holds the site copyright for 2010 to 2026 (https://leanpub.com/lifetime/buy footer). It builds ebooks (and courses) from your manuscript, sells them on its bookstore, and pays authors 80% royalties. Its own sales pitch says "dozens of authors have earned over $50,000, hundreds over $10,000" (https://leanpub.com/authors). Founders named on the site: Peter Armstrong and Len Epp (https://leanpub.com/authors).

## 2. Writing and publishing

**Writing modes** (https://leanpub.com/create/book, read 30 Oct 2026):
- Three in-browser editors: Minimal (prose), Visual (WYSIWYG, structured books), Source (edit the Markua directly; "best for technical books, programming books, power users").
- Files on your computer: GitHub and Dropbox. The page says: "GitHub and Dropbox require a Pro, Max, or Ultra membership." (The older help article, https://help.leanpub.com/en/articles/3688537-how-much-does-leanpub-cost-for-authors-to-use, last updated 2019, speaks of "Free, Standard and Pro" plans: stale.)
- Upload your own PDF and/or EPUB.
- Starting points: blank, a free template, or an AI interview (GhostAI Studio, needs Max or Ultra). Book language: 96 languages supported.
- Bitbucket (named in the old manual) is not on the current create page.

**GitHub mode.** Authors page: "if you're using GitHub writing mode, set up a post-commit hook to publish automatically with zero clicks" (https://leanpub.com/authors). Chapter order is controlled by `Book.txt` (taught in Leanpub's own manual; details not read). So a push to the repository can publish a new version.

**Markua.** Leanpub's Markdown-based format for books and courses. The Markua Manual contents page covers text, resources, asides, blurbs, quizzes, footnotes, crosslinks, directives, page breaks and appendices, and says "No inline HTML" (https://leanpub.com/markua/read). The manual covers Markua 0.10 and 0.30. The spec on GitHub showed version 0.31.36 dated 2024-04-30, per search summary (https://github.com/markuadoc/markua-spec). Books default to Markua 0.30 "in beta" per an older help article (https://help.leanpub.com/en/articles/1319778-how-do-i-write-a-book-in-markua-today-what-s-the-current-status-of-markua, 2022, stale wording). No "Markua 1.0" was found. You switch between Leanpub Flavoured Markdown and Markua with a checkbox on the book's manuscript-format page.

**Preview and publish.** Preview builds the book for you only; Publish puts it on sale and makes it instantly available to current readers (https://help.leanpub.com/en/articles/4541239-there-are-limited-previews-and-publishes-when-you-have-a-free-plan-what-does-this-mean). Free and Mini plans: preview or publish up to 20 times a month, collectively. Light and above: unlimited (https://leanpub.com/authors).

**In-progress books and updates.** Readers who have bought get every new version free; the 60-day refund exists partly because "many Leanpub books are written in-progress" (https://leanpub.com/refunds). On the Publish page you tick "Notify your readers", write Release Notes, and press Publish Book; in plain-text modes (browser, GitHub, Dropbox) that both publishes and sends the email to readers whose accounts accept new-version emails from you. Rules: use it for "significant new content" only, not offers (https://help.leanpub.com/en/articles/4178568-i-m-publishing-an-in-progress-book-how-can-i-contact-my-readers-when-i-publish-a-new-version-of-my-book-with-a-new-chapter, 23 Aug 2023). Authors do not get buyers' email addresses (search summary of https://help.leanpub.com/en/articles/569141-why-don-t-i-get-all-the-reader-email-addresses-is-it-possible-to-see-the-details-of-the-readers-who-purchase-one-s-book; not read directly).

**Formats.** PDF and EPUB, a free sample as PDF or EPUB or read online (book pages such as https://leanpub.com/sample-fiction-book via search); no DRM (refund policy: "no DRM or anti-circumvention"). MOBI: one author page lists it; Leanpub's own current pages do not mention it. A print-ready PDF export exists, now from Light upward (see below).

**Themes, images, extras.** Custom themes on Light and above. Packages and "Extras" (videos, artwork, source files, code samples, templates, worksheets; not services or software licences) are defined in the Terms (https://leanpub.com/read/tos/content-and-copyright, definitions section).

## 3. Price and money

**Royalty.** "80% on purchases of $7.99 and up; 80% minus 50 cents on purchases from $0.99 to $7.98" (https://help.leanpub.com/en/articles/10549058-leanpub-product-pricing-flexibility-to-enhance-your-book-marketing-opportunities-for-authors, 13 Feb 2025; same on https://leanpub.com/create/book). A $20 sale pays $16.

**Variable pricing.** Authors set a minimum and a suggested price; the buyer picks on a slider between them and may pay more (https://help.leanpub.com/en/articles/110750-why-do-i-see-a-suggested-price-and-a-minimum-price-when-i-buy-a-leanpub-book-what-is-variable-pricing, read via search). A free minimum is allowed. In 2024 the minimum paid ebook price became as low as $0.99; for bundles, courses and tracks, $7.99 (same pricing article). Upper limit: $500 per the quickstart page (search summary; not re-read). Price can be changed any time (search summary of help article 110704).

**Free copies and Reader Memberships.** For a book with a free minimum there are two checkboxes on the Pricing page: "Allow Free Purchases", and "Free purchases of this book require a Reader, Standard or Pro membership". Untick the second and anyone can take the book free without a membership (https://help.leanpub.com/en/articles/9333803-should-i-opt-my-book-in-to-the-free-with-membership-feature-on-leanpub-i-m-concerned-my-royalties-will-go-down-what-should-i-do, 4 June 2024). Reader memberships: Mini Reader $7.99 a month (about 2,000 "Free With Membership" books, one credit every six months), Light Reader $17.99, Standard Reader $27.99; credits buy books up to $25 (https://leanpub.com/readers/membership). Half of each membership's revenue goes to authors of the free-with-membership books the member uses; the help article says the pool "does not pay much revenue" per membership. A search summary said pool payouts come annually and manually above $100 (not re-read).

**Coupons.** Coupon links with a set price, maximum uses, start and end dates, also free-copy and batch coupons (https://help.leanpub.com/en/articles/640826-how-can-i-create-coupons-for-my-books-bundles-or-courses-to-give-them-away-for-free-or-at-a-discount-as-part-of-a-promotion), read via search only.

**Bundles and packages.** Bundles of your books and packages with Extras are in the Terms and the create menus ("Create a Bundle", "Create a Track"); mechanics beyond that not read.

**Refunds.** "Within 60 days of a purchase, you can get a 100% refund on any Leanpub purchase, unless we determine that you are or have been abusing the refund policy." Last updated 7 October 2024; courses have special rules; refund typically 3 to 5 business days (https://leanpub.com/refunds). No partial refunds (search summary). An older help article still says 45 days: stale.

**Payouts** (https://help.leanpub.com/en/articles/110527-how-and-when-do-you-pay-royalties, dated 27 June 2026): royalties paid on the 7th of each month via Wise or PayPal (changed from the 1st in July 2024); new authors start in "layaway" until a method is chosen; Wise recommended; a 60-day hold on each sale's royalties because of the refund window; minimum payout $20 for PayPal and $100 for Wise (raisable). Example in the article: a 16 May sale is paid on 7 August.

## 4. Author plans (fees) and paid services

**Author Memberships** (https://leanpub.com/authors, read 30 Oct 2026; figures are the quarterly rate per month):

| Plan | Per month | Billed | Adds |
|---|---|---|---|
| Free | $0 | | 80% royalties, 20 previews or publishes a month (Free-plan editor list not confirmed) |
| Mini | $8.99 | $26.97 every 3 months | Up to 100 books and courses, 20 previews/publishes a month, Minimal, Visual and Source editors, upload mode |
| Light | $13.99 | $41.97 | Unlimited previews and publishes, custom themes, print-ready PDF export |
| Pro | $18.99 | $56.97 | AI Support, GitHub and Dropbox sync, Google Analytics, InDesign export, Leanpub API |
| Max | $32.99 | $98.97 | Two months on The Shelf a year (a $179 value), VIP support, monthly AI usage, GhostAI Studio and Drawer, member prices on AI tools |
| Ultra | $89.67 | $269 | Max plus 10 times the AI usage, four 30-minute calls a year with the founders, priority queue for Launch videos and the Podcast |

Monthly billing costs more: the page says quarterly "saves $12 a year" on Mini, Light and Pro, $24 on Max, $112 on Ultra, so monthly prices are inferred as about $9.99, $14.99, $19.99, $34.99 and $99 (inferred, not seen). There are also annual and lifetime options (toggles on the page); their prices were not found in the text (https://leanpub.com/lifetime/buy returned no prices). The old help article names Free/Standard/Pro: stale.

**Book Weekend**: two days live on Zoom with the founder; the ticket includes six months of Ultra and a month on The Shelf (https://leanpub.com/authors). Price not found.

**Marketing** (https://leanpub.com/marketing, 30 Oct 2026): pay once, no subscription.
- 1 Week Shelf Spot + 1 Weekly Sale newsletter spot: $129.
- 1 Month Shelf Spot + 1 Weekly + 1 Monthly Sale newsletter spot: $179 on the page ($199 in the help article https://help.leanpub.com/en/articles/10339186-marketing-packages-for-authors, Feb 2025: stale).
- Audience: Weekly Sale over 90,000 subscribers; Monthly Sale over 130,000 (the package box on the same page says 140,000: inconsistent). The Shelf shows on the homepage and on the post-purchase Thank You pages. Packages can be bought only after a book is published. Authors who opt in to Leanpub discounts also get free inclusion in the weekly and monthly sale newsletters (https://leanpub.com/authors).

**Services** (https://leanpub.com/services, 30 Oct 2026):
- GhostAI: AI writing collaborator in the Leanpub editor, or a plugin for Claude Code or Codex; editor use comes with Max or Ultra; plugin is a one-time purchase (price not found).
- AudiobookAI: AI-narrated audiobook with synced transcript, from $999 (up to 200,000 words, then $2 per 1,000) (https://leanpub.com/services/audiobook_ai).
- TranslateAI: 31 languages, from $349 per language (https://leanpub.com/services/translate_ai). The $49 and $79 figures from the earlier search draft are old.
- CourseAI $499; ImportAI, IndexAI, AccessibilityAI each from $249.
- Publish on Amazon: Leanpub publishes your Markua or LFM book on Amazon (Kindle, paperback, hardcover), $1,299, 10 free paperbacks, you earn 80% of Leanpub's Amazon publisher revenue (https://leanpub.com/services/publish_on_amazon).
- GhostAI Accelerator $1,499; GlobalAuthor from $3,499; PodcastBook and NewsletterBook from $3,499; ConferenceBook from $4,999; ghostwriting books $18,000 to $72,000.
- "Frontmatter" as a Leanpub product: not found.

**Print.** Leanpub does not sell print itself; it exports a print-ready PDF for KDP, IngramSpark and others (help article 3333903, via search). Authors can also pay royalties toward promotion (search summary).

## 5. Readers, discovery, promotion, analytics

- **Reader features.** Free updates, library, bell and email notice of new versions, free samples, reader profile pages with reviews shown on the profile (Reader Memberships page: "Optional public profile page and the ability to show reviews on your profile"). Book-page star ratings or written reviews: not confirmed. Author-added testimonials on the book page are confirmed by help article 4236092 (via search). Wishlist or "notify me": not found.
- **Bookstore.** Search by language and category; lists for Bestsellers Last Week, Bestsellers All Time, New Releases; the author picks 3 to 5 categories and applies them by publishing a new version (help articles 5395545, 10070084, via search).
- **Podcast, blog, newsletter.** The Leanpub Podcast and Launch videos (author interviews) exist; Ultra authors get a priority queue for them (https://leanpub.com/authors). The blog's 2026 posts are "Why Books Die Alone", "The Most Painful Compliment" and "Leanpub at Sixteen" (footer of any page). Newsletter: Weekly and Monthly Sale (section above). Whether a free author can ask for a podcast slot: not found.
- **Analytics.** Per-book Sales page (last 30 days by default), Individual Purchases page, refunds; sale emails capped at 10 a day and not a record; Google Analytics and the API from Pro (help articles 10003878, 7217185, via search; Authors page).

## 6. Terms that matter

- Copyright stays with the author: "Leanpub Authors or Organizations retain the copyright to their work"; only the copyright holder may publish; the public-domain policy bars CC0 or public-domain books (https://leanpub.com/read/tos/content-and-copyright). The licence clause itself was not read in full.
- No exclusivity. "It is absolutely ok to publish separately on Leanpub and Amazon, or any other self-publishing platform, at the same time" (https://help.leanpub.com/en/articles/117414-can-i-sell-my-book-on-leanpub-and-on-amazon-at-the-same-time, 29 Jun 2023). KDP Select demands exclusivity, but you can retire a Leanpub book "temporarily or permanently ... with one click" (https://help.leanpub.com/en/articles/1319791-can-i-use-leanpub-with-kdp-select).
- ISBN: not needed (https://help.leanpub.com/en/articles/110532-do-i-need-an-isbn-to-publish-my-book-on-leanpub, "No :)", 5 May 2025). You may insert your own in plain-text modes (search summary).
- Leanpub books are not sold by Leanpub on Amazon or Apple (help article 1308104, via search).

## 7. What changed recently

- Apr to Oct 2026: the Author Memberships page is now Mini, Light, Pro, Max, Ultra, with Shelf months and GhostAI built into Max and Ultra. Print-ready PDF and custom themes moved down to Light.
- AI services are priced in the hundreds and thousands of dollars (AudiobookAI, TranslateAI), and "Publish on Amazon" and ghostwriting books are new premium lines (page read 30 Oct 2026; launch dates not found).
- 27 June 2026: royalty-payment article updated (7th of the month, layaway default).
- 5 May 2025: ISBN article. 13 Feb 2025: minimum price $0.99 article (change made 2024). 7 Oct 2024: refund policy last updated (60 days).
- 2022: Reader Memberships began.

## What this means for the book

Plan: $0 minimum, $19.99 suggested, in-progress with updates, Markua from GitHub.

1. **The plan fits the platform.** Leanpub supports a free minimum with a paid suggested price on a slider. A reader who pays $19.99 yields about $16; free copies yield nothing. On the Pricing page untick "Free purchases ... require a Reader, Standard or Pro membership" so a free copy needs no membership, which fits a book meant to be read.
2. **GitHub mode needs Pro.** About $18.99 a month on quarterly billing ($56.97 per quarter; monthly billing about $19.99, inferred). One quarter of Pro is a bounded cost; GitHub plus a post-commit hook gives "zero clicks" publishing, which suits our push-to-dev habit. Confirm before paying whether sync survives a downgrade (not found). Fallback: Free or Mini with the Source editor and pasted or uploaded chapters, limited to 20 builds a month.
3. **Markua is the risk.** The beta label and the gap between the 0.10 manual and the 0.31 spec mean a trial chapter must be previewed before the manuscript layout is fixed. Our `manuscript/Book.txt` matches Leanpub's `Book.txt` convention in name; check the exact rules.
4. **In-progress with updates is the platform's strength.** Publish the first chapters early, notify readers only for real new content, tell buyers about the 60-day refund (it is automatic) and keep the failures in as versions. Royalties are held 60 days, so first payouts lag by about two to three months.
5. **Use for free:** coupons for review copies, the opt-in to Leanpub discount promotions (weekly and monthly sale newsletters), 3 to 5 categories, testimonials, the sample chapter, the Sales page and API (Pro) as the source for any sales number in the claims register.
6. **Paid marketing: later, and only after a signal.** $129 (one week) or $179 (one month) buys a Shelf spot and newsletter slots to 90,000 to 130,000 subscribers. For a free-minimum book, newsletter readers mostly take it free, so the spend buys readers, not income; judge it once a first version has sold. Max includes two Shelf months a year, but at $32.99 a month that is not worth it for one book.
7. **Not needed:** AudiobookAI ($999), TranslateAI ($349 per language), CourseAI ($499), Publish on Amazon ($1,299), GlobalAuthor, ghostwriting. The book's rules (author voice, traced numbers, the failures stay in) argue against AI rewriting or ghostwriting the text. If a paperback is wanted, Light ($13.99 a month) gives the print-ready PDF; take your own ISBN for KDP and do not enrol in KDP Select.
8. **Limits to plan around:** you cannot email buyers directly (only via Leanpub's update emails), so keep the book's own site as the contact route; the Markua spec is moving; plan names and prices change often, so re-check https://leanpub.com/authors the day you subscribe.
9. **Still to check:** annual and lifetime plan prices, Free-plan editor access, whether book pages show star reviews, bundle and package mechanics, the Terms licence clause, and the Markua `Book.txt` rules. Fetching works through curl, so a second pass can read the Terms, the manual and the blog.

## Where this came from

All read on 30 October 2026.
Fetched directly:
- https://leanpub.com/authors
- https://leanpub.com/marketing
- https://leanpub.com/services and /services/audiobook_ai, /translate_ai, /publish_on_amazon, /ghost_ai
- https://leanpub.com/create/book
- https://leanpub.com/refunds
- https://leanpub.com/readers/membership
- https://leanpub.com/markua/read (contents)
- https://leanpub.com/read/tos and /read/tos/content-and-copyright
- https://leanpub.com/lifetime/buy
- Help centre: https://help.leanpub.com/en/articles/ numbers 3688537, 4541239, 10549058, 9333803, 10339186, 110527, 1319778, 1319791, 117414, 110532, 4178568, 4405350
Via search summaries only (marked in the text): other help articles cited by number, https://github.com/markuadoc/markua-spec, Leanpub book pages and the older Leanpub Manual.
