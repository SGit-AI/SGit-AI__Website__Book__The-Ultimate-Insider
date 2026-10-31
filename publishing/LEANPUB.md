# The Leanpub book: what the editor does by hand

Kept by publisher@book.the-ultimate-insider. Written 30 October 2026 from Leanpub's own help pages, read that day (links at the end); Leanpub's screens change, so where a step below and the screen disagree, the screen wins, and tell the publisher so this file is corrected.

Nothing here can be done by an agent: each step needs the editor's Leanpub account, his GitHub account or his money. The target is the first edition on sale on Monday 2 November 2026 (book.json, milestones).

## What is already in place

- `manuscript/Book.txt`, the chapter files it lists and `manuscript/resources/images/` in this repository, at the top level, in the layout Leanpub's Git and GitHub writing mode builds from: a `manuscript/` folder holding `Book.txt`, which lists the files of the book in order.
- `publishing/build_book.py`: the team's own build of the same `Book.txt` into a PDF and an EPUB, run by CI on every release (the site serves `/manuscript/the-ultimate-insider.pdf` and `.epub`), so a broken chapter shows up here before it shows up on a Leanpub preview.

## Steps, in order (about 30 minutes, once)

0. **The plan: settled.** The Git and GitHub writing mode needs a Standard or Pro author plan (Leanpub's help, article 6699163, 3 February 2023); you hold a lifetime Pro plan (the conductor's letter 016, 30 October 2026), so nothing to buy. You create the book yourself (your task E1 in `team/conductor/editor-tasks.json`).
1. **Create the book.** On Leanpub, create a new book. For the writing mode choose **Cloud**, then **Using Git and GitHub**. In the same form give the repository as `SGit-AI/SGit-AI__Website__Book__The-Ultimate-Insider` and the branch names for previews and for publishing.
   - **Branch: `main` for both** (decision L2), so Leanpub builds only what you merged, the same rule as the site. Name it explicitly: the repository's default branch is `dev`, not `main`.
   - The book's URL slug is permanent-looking and public; it waits on the title (decision on the title, round 1). A neutral slug such as `the-ultimate-insider` keeps the options open.
2. **Let Leanpub read the repository.** On GitHub, in the repository's Settings, "Collaborators" (Leanpub's help calls it "Manage Access"), "Invite a collaborator", search for `leanpub`, "Add leanpub to this repository". Leanpub accepts within a few minutes. **Give it the Read role, nothing above it** (security's advice, recorded as control C9 in `controls/`; its reply is `team/security/requests/publisher__leanpub-as-collaborator-reply.md`): the repository is public, so Leanpub can read it anyway, and Write would let an outside account push to `dev`, which releases and deploys the site. If Leanpub's build fails with Read, raise it then. Removing the collaborator on the same page ends the access at any time.
3. **First preview.** In the book on Leanpub: Versions, Preview, "Create Preview". Today it holds RC1 as `manuscript/Book.txt` lists it, once `dev` is merged into `main`; the point is that it proves the connection. Send the publisher (in the session or by a commit note) whether it built; nothing about the account itself.
4. **The book page** (Settings, About): subtitle, description, teaser, meta description; "Update Book". The publisher drafts these in `publishing/listing.md` once the title is signed.
5. **The cover** (Settings, Book Cover): an image 1800 by 2700 pixels; "Update Book Cover". The designer's job, not staffed yet; until then Leanpub's default cover stands.
6. **The price** (Store, Pricing): the minimum price, the suggested price and Leanpub's maximum discount; "Update Pricing". Decided: L1, a $0 minimum and $19.99 suggested (below).
7. **Your author profile**, if not done already; "Save Settings".
8. **Publish, on Monday 2 November**, only after your sign-off on the release candidate (round 4): Versions, "Publish New Version", "Publish Book".

## The price: decided

**L1, the editor's word, 30 October 2026 about 10:40 UTC**: a minimum price of **$0** (free), and a suggested price of **$19.99**. (The team had proposed a $9.99 minimum; the editor chose free.) **L2**: Leanpub builds from `main`, for previews and for publishing. **With L1, untick "Free purchases of this book require a Reader, Standard or Pro membership"** in the price settings: ticked, a reader needs a membership or a coupon to take the book at $0, and the landing page says "Free! With Membership"; unticked, it says "Free! Minimum Price" and anyone can take it (Leanpub's help, articles 4471731, 11 May 2025, and 6266784, 3 February 2023).

**Readers who pay $0 get every new version.** Leanpub's own landing-page wording: "All readers get free updates, regardless of when they bought the book or how much they paid (including free)." The notice of a new version is an email you choose to send when you publish ("Publish New Version", the box to email readers); Leanpub's help says it reaches "all your customers ... as long as they have not opted out" (article 494316, 10 March 2022), while another article of the same date says readers "need to opt in" (2248122). No page found treats $0 readers differently from paying readers for that email, and none says so outright: the new version itself is settled, the email to $0 readers is not. If it matters, one $0 test purchase from a second account settles it at the first published version.

Leanpub pays an 80% royalty on most sales and does not restrict selling the same book elsewhere (Leanpub's help, read 30 October 2026).

## The manuscript's format

The book is written in **Markua 0.30**, Leanpub's Markdown for books (decision M1; markua.com). Leanpub's own build is the official PDF and EPUB; `publishing/build_book.py` is the team's check of the same files on every release, and `publishing/markua.py` translates Markua's asides, blurbs, attribute lines, page breaks and matter markers for it.

On the versions (markua.com, read 30 October 2026): **Markua 0.30** ("Markua 0.30 Beta", leanpub.com/markua030/read) is what new Leanpub books use, and stays M1's target. The **specification** on markua.com is headed "Version 0.31.50 (2026-08-11)": the spec's own numbering, not a separate release a book chooses, so nothing changes for M1; the features the book uses are checked against it. **Markua 0.10** is the older manual (leanpub.com/markua/read), kept for Leanpub's courses; not for this book.

**Sizes.** Leanpub's guidance: each image under 1 MB, the book's images under 100 MB in all, the cover exempt (article 4212681, 30 January 2025). The manuscript's 58 images are 9.2 MB, none over 1 MB. A search summary says an EPUB over 20 MB cannot be uploaded in Upload mode; that mode is not this book's.

## Sources (read 30 October 2026)

- Writing modes and plans: help.leanpub.com/en/articles/6699163 (3 February 2023); the current author plans, Free, Standard and Pro: /3691778 (16 January 2026)
- Free books and the membership box: /4471731 (11 May 2025) and /6266784 (3 February 2023)
- New versions and the readers' email: /494316 and /2248122 (both 10 March 2022); free updates for every reader: the wording on Leanpub's book landing pages
- Image sizes: /4212681 (30 January 2025); Markua's versions: markua.com

- Getting started with the Git and GitHub writing mode (full and TL;DR): help.leanpub.com/en/articles/2916385 and /4868811
- Royalty rate and where else the book may be sold: help.leanpub.com/en/articles/5468013
- The 99-cent paid minimum is named in the title of a Leanpub announcement linked from help.leanpub.com/en/articles/3796821 (an article Leanpub marks outdated); the publisher did not read the announcement itself.
