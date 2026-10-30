# The Leanpub book: what the editor does by hand

Kept by publisher@book.the-ultimate-insider. Written 30 October 2026 from Leanpub's own help pages, read that day (links at the end); Leanpub's screens change, so where a step below and the screen disagree, the screen wins, and tell the publisher so this file is corrected.

Nothing here can be done by an agent: each step needs the editor's Leanpub account, his GitHub account or his money. The target is the first edition on sale on Monday 2 November 2026 (book.json, milestones).

## What is already in place

- `manuscript/Book.txt`, the chapter files it lists and `manuscript/resources/images/` in this repository, at the top level, in the layout Leanpub's Git and GitHub writing mode builds from: a `manuscript/` folder holding `Book.txt`, which lists the files of the book in order.
- `publishing/build_book.py`: the team's own build of the same `Book.txt` into a PDF and an EPUB, run by CI on every release (the site serves `/manuscript/the-ultimate-insider.pdf` and `.epub`), so a broken chapter shows up here before it shows up on a Leanpub preview.

## Steps, in order (about 30 minutes, once)

1. **Create the book.** On Leanpub, create a new book. For the writing mode choose **Cloud**, then **Using Git and GitHub**. In the same form give the repository as `SGit-AI/SGit-AI__Website__Book__The-Ultimate-Insider` and the branch names for previews and for publishing.
   - **Branch: `main` for both** (decision L2), so Leanpub builds only what you merged, the same rule as the site. Name it explicitly: the repository's default branch is `dev`, not `main`.
   - The book's URL slug is permanent-looking and public; it waits on the title (decision on the title, round 1). A neutral slug such as `the-ultimate-insider` keeps the options open.
2. **Let Leanpub read the repository.** On GitHub, in the repository's Settings, "Collaborators" (Leanpub's help calls it "Manage Access"), "Invite a collaborator", search for `leanpub`, "Add leanpub to this repository". Leanpub accepts within a few minutes. **Give it the Read role, nothing above it** (security's advice, recorded as control C9 in `controls/`; its reply is `team/security/requests/publisher__leanpub-as-collaborator-reply.md`): the repository is public, so Leanpub can read it anyway, and Write would let an outside account push to `dev`, which releases and deploys the site. If Leanpub's build fails with Read, raise it then. Removing the collaborator on the same page ends the access at any time.
3. **First preview.** In the book on Leanpub: Versions, Preview, "Create Preview". Today it holds one page (About this edition), which is the point: it proves the connection. Send the publisher (in the session or by a commit note) whether it built; nothing about the account itself.
4. **The book page** (Settings, About): subtitle, description, teaser, meta description; "Update Book". The publisher drafts these in `publishing/listing.md` once the title is signed.
5. **The cover** (Settings, Book Cover): an image 1800 by 2700 pixels; "Update Book Cover". The designer's job, not staffed yet; until then Leanpub's default cover stands.
6. **The price** (Store, Pricing): the minimum price, the suggested price and Leanpub's maximum discount; "Update Pricing". Decided: L1, a $0 minimum and $19.99 suggested (below).
7. **Your author profile**, if not done already; "Save Settings".
8. **Publish, on Monday 2 November**, only after your sign-off on the release candidate (round 4): Versions, "Publish New Version", "Publish Book".

## The price: decided

**L1, the editor's word, 30 October 2026 about 10:40 UTC**: a minimum price of **$0** (free), and a suggested price of **$19.99**. (The team had proposed a $9.99 minimum; the editor chose free.) **L2**: Leanpub builds from `main`, for previews and for publishing. Leanpub pays an 80% royalty on most sales and does not restrict selling the same book elsewhere (Leanpub's help, read 30 October 2026).

## The manuscript's format

The book is written in **Markua 0.30**, Leanpub's Markdown for books (decision M1; markua.com). Leanpub's own build is the official PDF and EPUB; `publishing/build_book.py` is the team's check of the same files on every release.

## Sources (read 30 October 2026)

- Getting started with the Git and GitHub writing mode (full and TL;DR): help.leanpub.com/en/articles/2916385 and /4868811
- Royalty rate and where else the book may be sold: help.leanpub.com/en/articles/5468013
- The 99-cent paid minimum is named in the title of a Leanpub announcement linked from help.leanpub.com/en/articles/3796821 (an article Leanpub marks outdated); the publisher did not read the announcement itself.
