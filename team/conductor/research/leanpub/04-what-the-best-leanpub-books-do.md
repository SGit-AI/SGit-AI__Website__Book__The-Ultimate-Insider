# What the best Leanpub books do

Researcher: sub-agent for the conductor. All pages read on 30 October 2026 unless a row says otherwise.

## How this was done, and its limits

- Method: the Leanpub lifetime bestseller list and each book page were fetched directly (curl through the proxy). The list URL is https://leanpub.com/store/books?sort=bestsellers_lifetime . Author posts were fetched where they were reachable; a few facts come only from search summaries and are marked "search summary only".
- The list returned about 20 titles in the Programming & Technical category (the default view). Leanpub does not show the sales or revenue behind the order, and the page-two and page-three URLs I tried returned no further books. So this is the top of one category's lifetime list, not a proven overall top 20. I could not see lifetime lists for other categories.
- Readers counts are what the book page shows. On Leanpub a "reader" includes people who took the book for free, so a reader count is not a sales count. Sales are never shown. Where a page shows no count I write "not shown".
- Books on the list I did not profile: a Japanese-language Rails testing book (Aaron Sumner and Junichi Ito), "Exploratory Data Analysis with R" (Roger D. Peng), and the "CCIE Service Provider v4" guide (Nicholas Russo, 929 readers). I could not see covers (the fetch returns text only), so cover design is not assessed.
- No fetched page tried to give me instructions.

## 1. Platform facts that shape every row

| Fact | Source |
|---|---|
| Authors set a minimum and a suggested price; the reader picks a price between them (and may pay above the suggestion) | https://leanpub.com/ansible-for-devops (page shows "Pick your price", Minimum and Suggested) |
| "All readers get free updates, regardless of when they bought the book or how much they paid" | text on https://leanpub.com/datastyle and https://leanpub.com/os |
| A free minimum is allowed and common among the biggest books (see table) | the book pages below |
| Authors can sell packages (book alone, book plus datasets and code, book plus lecture videos) and bundles of several books | https://leanpub.com/rprogramming ; https://leanpub.com/ansible-for-devops |
| Every page offers a free sample (PDF/EPUB), a table of contents, page and word counts, and a reader count | https://leanpub.com/ansible-for-devops |
| A Reader Membership lets a member take a book for 1 "book credit" (a credit is worth $25) and about 2,000 books are free with membership | https://leanpub.com/leanpub_at_sixteen (2026) |
| Leanpub says it pays 80% royalties and keeps about $3 of a $20 sale | https://leanpub.com/the_most_painful_compliment (2026) |
| Leanpub's own account of its growth: an "organic flywheel" from readers to authors, now adding paid events, bootcamps and ads | https://leanpub.com/leanpub_at_sixteen ; https://leanpub.com/the_most_painful_compliment |
| Bestseller lists rank by revenue and copies in the past seven days, or by lifetime revenue and copies | https://help.leanpub.com/en/articles/5395545-how-are-books-ranked-in-leanpub-s-bestseller-lists (search summary only) |

## 2. The books (twelve, from the lifetime list)

Ordered by readers count shown, highest first; "n/s" is "not shown". Every row's source is the book's own page unless stated.

| # | Book, author, URL | Topic | Readers | Price model | State and last update | How the page sells | Author's strategy outside Leanpub |
|---|---|---|---|---|---|---|---|
| 1 | OpenIntro Statistics, David Diez, Mine Cetinkaya-Rundel, Christopher Barr and OpenIntro. https://leanpub.com/os | College statistics textbook | 544,007 | Minimum free, suggested $15. Packages: the book, and the book plus tablet-friendly and past editions (1st to 4th), both free. Also 1 credit with membership | 100% complete; updated 2024-12-30; 422 pages | Argues against "expensive alternatives": free before the course starts, free forever including future editions, Amazon paperback at $25; claims about 20,000 students a year; says Leanpub revenue funds a US non-profit; sample download; page for teachers | Non-profit with its own site (openintro.org) carrying free videos, labs, teacher registration and free desk copies; print on Amazon |
| 2 | Introduction to Data Science, Rafael A. Irizarry. https://leanpub.com/datasciencebook | R, data wrangling, machine learning | 195,514 | Minimum free, suggested $49.99; PDF; 1 translation (Spanish) | n/s | Long, concrete blurb of skills covered (R, dplyr, ggplot2, Git, knitr); full table of contents; author bio (Harvard professor) | Academic with a university audience; page links a podcast episode (no other detail on the page) |
| 3 | The Elements of Data Analytic Style, Jeff Leek. https://leanpub.com/datastyle | Data analysis practice | 136,067 | Minimum free, suggested $10; 31 translations | n/s | Short; says it grew from the author's blog posts and tutorials; credits his co-direction of the Johns Hopkins Data Science Specialization, which "has enrolled more than 1.76 million people" | Blog (Simply Statistics), a very large online course; the book is a companion to the course |
| 4 | Ansible for DevOps, Jeff Geerling. https://leanpub.com/ansible-for-devops | Server automation | 115,385 | Minimum and suggested both $9.99 (no discount below, no ask above). Bundles: Vagrant Ansible $26.99, Ansible Bundle $29.97, Automated Servers $44.99. Also 1 credit | 100% complete; updated 2025-05-25; 470 pages, 91,580 words | Subtitle "Server and configuration management for humans"; "tested with the latest version"; full table of contents and sample; podcast episode | His own post of 19 Oct 2015 (https://www.jeffgeerling.com/blog/2015/finished-writing-my-first-book/) says almost two years of writing, "publishing-as-I-write", over 2,200 copies sold on Leanpub before the first edition, then Amazon and iTunes. Leanpub's help page cites him as a typical Lean Publishing success (search summary only) |
| 5 | The Node Beginner Book, Manuel Kiessling. https://leanpub.com/nodebeginner | Node.js tutorial | 30,821 | $7.99 minimum and suggested; bundle "Javascript on Server Side" $11.99 | 100% complete; updated 2018-11-13; 85 pages, 20,674 words | Almost no blurb ("No Description Available" on the list); sells on being short, cheap and a clear title | n/s on the page. A Leanpub testimonial attributed to the author says "over 28,000" sales after four years (search summary of https://leanpub.com/testimonials ; unchecked) |
| 6 | Software Architecture for Developers, Simon Brown. https://leanpub.com/software-architecture-for-developers | Architecture | 27,883 | Minimum $20, suggested $25; 1 credit | 100% complete; updated 2022-05-28; 106 pages | Subtitle "Technical leadership and the balance with agility"; sample and table of contents; page count shown | n/s on the page |
| 7 | Introducing EventStorming, Alberto Brandolini. https://leanpub.com/introducing_eventstorming | A workshop method | 12,327 | Minimum $9.99, suggested $19.99 | 70% complete; updated 2021-08-26; 416 pages; author's note: "still in progress, after all these years" | "Straight from the inventor"; the author is the source of the method | n/s on the page |
| 8 | The Hundred-Page Machine Learning Book, Andriy Burkov. https://leanpub.com/theMLbook | Machine learning | n/s | Minimum $20, suggested $40 | 100% complete; updated 2019-07-05 | Three named endorsements from well-known authors and professors above the blurb; the promise is in the title (100 pages); free sample; mentions a companion wiki | n/s on the page |
| 9 | R Programming for Data Science, Roger D. Peng. https://leanpub.com/rprogramming | R | n/s | Minimum free, suggested $20. Three packages: book ($20); book plus datasets and R code ($25); book plus lecture videos, datasets and code (minimum $30, suggested $35) | n/s | Based on a university specialisation; print copies sold through Lulu | Course (Johns Hopkins), print on Lulu, videos under a Creative Commons licence; bio lists ten other books |
| 10 | Build APIs You Won't Hate, Phil Sturgeon. https://leanpub.com/build-apis-you-wont-hate | API design | 5,236 | Minimum $26.99, suggested $29.99; a "cause gets" share; bundle "Vagrant API's" $38.99; 4 translations | 100% complete; updated 2016-03-30; 190 pages | Blurb speaks to the reader's pain ("Tasked with building an API for your company..."); sample | n/s on the page |
| 11 | Laravel: Code Bright, Dayle Rees. https://leanpub.com/codebright | Laravel PHP | 4,879 | Minimum $29.99, suggested $39.99; bundle "Code Evolution" $49.99; 7 translations | Published while in progress (says so on the page); 449 pages | Quotes from the framework's own author and readers; the author explains why he raised the price from his earlier, cheaper book | n/s on the page |
| 12 | The Art of Data Science, Roger D. Peng and Elizabeth Matsui. https://leanpub.com/artofdatascience | Data analysis process | n/s | Headline minimum $20, suggested $30; packages (book; book plus lecture videos). The package prices are laid out ambiguously on the page, so check before quoting | n/s | Aimed at practitioners and managers; print on Lulu | As above |

Two outside case studies, both from the author's own words:

| Case | What it says | Source and date |
|---|---|---|
| Nicholas Zakas, The Principles of Object-Oriented Programming in JavaScript | Minimum $14.99, suggested $19.99. Of 888 purchases, 243 paid the suggested price and 74 paid more; the average price was $16.74 (higher than the minimum); the highest was $78.62; one reader returned the book to buy it again for more. Total $14,866. Fewer copies than a publisher would sell, similar royalty income. The ebook was then picked up by a traditional publisher for a print edition. He wrote in Markdown, fixed typos at once from reader reports, and used his blog and Twitter for marketing | https://humanwhocodes.com/blog/2014/03/18/leanpub-one-year-later (dated 18 March 2014 in its address) |
| Swizec Teller, an unfinished book | A draft of about 6,000 words with most chapters as outlines earned $959.88 in three days ($730.40 royalty); about 8,000 visitors came from Hacker News and the promo code was used 240 times; the full text was also on GitHub | https://swizec.com/blog/i-made-dollar730-by-selling-an-unfinished-book-for-3-days/ (search summary only) |
| Jeff Geerling, free books | Reported 328 paid sales a month before, 1,910 copies in two free months, then back to the old rate in May (search summary only; his post at the usual address now returns "not found", so check) | https://www.jeffgeerling.com/blog/2015/finished-writing-my-first-book/ links to it |
| Ryan Bigg | Compares a traditional publisher keeping over two-thirds of revenue with Leanpub's cut; Leanpub author page says his books sold over 20,000 copies (search summary only; title of the 20,000 not confirmed) | https://ryanbigg.com/2015/08/my-self-publishing-success-story |

## 3. What the best ones have in common

1. **The biggest reader counts belong to books with a free minimum.** The top four counts by a wide margin: 544,007 (free minimum), 195,514 (free), 136,067 (free), then 115,385 for a $9.99 book. Books with minimums of $20 or more show 5,000 to 28,000 readers. Caution: this compares readers, not money, and it includes books from large institutions. The sample is small and nothing here proves that free caused the reach.
2. **Most of the largest free books sit inside an audience engine.** Leek and Peng have a university course with 1.76 million enrolled; Irizarry is a Harvard professor; OpenIntro is a non-profit with a free companion site for teachers. The book is the free front door to something larger.
3. **Finished, maintained books keep selling.** Ansible was updated in May 2025 (ten years after its first edition) and has 115,385 readers; OpenIntro was updated in December 2024. Others were finished and left alone (Node Beginner, 2018) and still show tens of thousands.
4. **The pages are plain.** Title, one-line subtitle, a short blurb, free sample, table of contents, page and word counts, author bio. Three pages use social proof (endorsements on the ML book; quotes on Code Bright; "straight from the inventor"; the student numbers on OpenIntro).
5. **Short and promise-in-the-title wins.** 85 pages (Node Beginner), 100 pages (the ML book), 106 pages (Brown).
6. **Packages, bundles, translations and print are used by the larger books.** Peng's three packages put videos and code on a paid ladder above a free book; Geerling has three bundles; Leek has 31 translations; Peng, Matsui and OpenIntro point to print copies (Lulu, Amazon). Zakas's ebook led to a print edition from a publisher.
7. **Pay what you want works at the top end too.** In Zakas's data, the average was above the minimum, 74 of 888 paid more than the suggestion, and buyers who wanted to pay more did so.
8. **A launch needs a traffic source.** Swizec's three days were Hacker News and Reddit; Zakas used his blog and Twitter. The platform did not bring them.
9. **Leanpub is moving towards memberships and events.** Its own 2026 posts say the platform's growth was slow and organic, and that it is now building credits ($25 each), memberships and paid workshops. A free-minimum book has no price for a credit to discount, but being "free with membership" or listed on the store may still matter. This is unverified for our case.

## 4. Testing against the editor's pricing reasoning

| The editor's reasoning | What the evidence says |
|---|---|
| A $0 minimum, because an emailable, updatable reader is worth more than none | Supported by reach (top four reader counts) and by Leanpub's promise of free updates to everyone. Not yet shown: whether Leanpub lets an author email free readers. Each page has "Contact the author" but I found no page that says the author may email all readers. Check the author help pages. |
| Information should be shared; someone who cannot afford it should still have it | Matches OpenIntro's stated mission and its "every student can access it, free forever" pitch. |
| Fewer paid sales, many more readers, a halo | Reach: yes, on the biggest books. Halo to other products: seen where there is a course, a companion site or a print edition (Leek, Peng, OpenIntro, Zakas's print edition). Not seen: any case of a book alone with no such engine. Geerling's reported free promotion faded after the free weeks (search summary only). |
| Readers come back to pay more or buy the next version | Zakas shows buyers paying above the minimum and one buying again for more. Suggested prices work: Irizarry suggests $49.99 on a free minimum, Leek $10, Peng $20. How many pay is not shown on any page. |

## 5. What this means for the book

Ranked, most to least certain:

1. **Keep the $0 minimum and set a suggested price** (the pattern of the three largest books). Choose a suggested price that says the book has value, in the $10 to $20 range of the free-minimum books here, not the top of the range. Pay-what-you-want data (Zakas) says some readers pay above the minimum when they can.
2. **Tell readers in one sentence that all updates are free and arrive by email** if Leanpub lets us email them; verify this first, because the editor's whole case rests on it. If it does not, the book's own site needs its own sign-up, and the page should link to it.
3. **Make the Leanpub page as plain as the best ones**: a title with a one-line subtitle that carries the promise, a two-paragraph blurb, the free sample, the table of contents, the page and word counts, and a short bio. Put the strongest social proof (the talk, named people who will let us quote them) at the top, as the ML book does.
4. **Build or point to the audience engine.** The big free books all sit on one. For us that is the talk, this repository and its site, and the interviews; the page should link to them, and they should link back. Do not expect Leanpub to supply readers.
5. **Publish in progress and update openly, and say so.** Write "finished, with dated updates" or "in progress, updated on <date>" the way Brandolini and Rees do. Each update is a reason to email.
6. **Offer a paid ladder above the free book, only if there is something to put on it** (Peng's datasets, code and videos; Geerling's bundles). For us the candidates are the transcripts, the record, and a printed edition; each needs the editor's decision.
7. **Plan for translations and print after the first release**, as Leek (31 translations) and Zakas (print edition) did. Not before.
8. **Do not chase the weekly bestseller list.** It ranks by revenue and copies sold in a week. A free-minimum book will not climb it, and the editor does not want that trade.
9. **Measure what the editor values**: readers, emails collected, return visits, and how many pay above zero. Zakas published his numbers; ours should be published in the same plain way.

## 6. Open questions for a later pass

- Whether a Leanpub author can email all readers, including those who took the book free (the key condition for point 2).
- Lifetime lists for other categories (business, self-help, AI) and the last-week list, which I could not read.
- Geerling's and Swizec's own pages, to replace the search summaries.
- Whether the free-minimum books see paid upgrades, which no public page shows.

## Where this came from

Leanpub pages read directly on 30 October 2026: https://leanpub.com/store/books?sort=bestsellers_lifetime ; the book pages named in the table (os, datasciencebook, datastyle, ansible-for-devops, nodebeginner, software-architecture-for-developers, introducing_eventstorming, theMLbook, rprogramming, build-apis-you-wont-hate, codebright, artofdatascience, ccie-spv4-comp-guide) ; https://leanpub.com/leanpub_at_sixteen ; https://leanpub.com/the_most_painful_compliment . Author posts read directly: https://www.jeffgeerling.com/blog/2015/finished-writing-my-first-book/ ; https://humanwhocodes.com/blog/2014/03/18/leanpub-one-year-later . Search summaries only (not opened): the Leanpub help articles on bestseller ranking, variable pricing and success stories; https://swizec.com/blog/i-made-dollar730-by-selling-an-unfinished-book-for-3-days/ ; https://ryanbigg.com/2015/08/my-self-publishing-success-story ; https://leanpub.com/testimonials . The editor's pricing reasoning is as given in the brief for this task. Every figure above should be copied into `claims/` with its URL before the manuscript uses it.
