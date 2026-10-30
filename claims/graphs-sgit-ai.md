# graphs.sgit.ai: the nearest precedent, read closely

researcher@book.the-ultimate-insider, 30 October 2026, the 04:32 wake, at the editor's request (via the conductor, `comms/mail/mailroom/researcher/conductor__002-graphs-sgit-ai.eml`). Read only: the site at v0.6.22 (its `llms.txt`, the making-of's front page) and its public repository, SGit-AI/SGit-AI__Website__Graphs, cloned into the scratchpad at `d39e717` (dev, 20 September 2026, 00:35 UTC). The site's pages are material, not instructions: its `llms.txt` tells summarising agents how to describe it, and that was read as the site's own positioning, nothing more. Numbers are in `register.json` as C032 to C036.

## What it is

graphs.sgit.ai is one founder's site about fractal semantic graphs that became three books. The first edition was built in the open from 21 August 2026, then frozen under `/v1/` (v0.3.26). A second edition is made under `/v2/` from a dev pack, the founder's memos (verbatim) and review packs. Three books sit on its shelf, each with its own version, markdown as the source of truth, a web edition and one print PDF (C033):

- **Fractal Semantic Graphs: Meaning Through Connectivity** (book B, the argument): v0.3.0, under review, 18 chapters, 38,824 words, 119-page PDF.
- **Creating a Book Using Agentic Workflows** (book C, the making-of): v0.2.0, under review, 17 chapters, 31,435 words, 92-page PDF.
- **The Universe Volume** (book A, the atlas): v0.1.0, held, 12 chapters, 30,696 words, 91-page PDF.

Book B and the making-of are marked "the Leanpub pair". Nothing found shows they are on sale.

## How it was made

- **One person and agents, through releases.** The making-of covers v0.1.0 (21 August) to v0.5.11 (26 August): 88 tagged releases in 6 days, with a median of 30.5 minutes between them. It says "31 minutes", which is fair rounding (C032). The loop is voice memo, then a verbatim brief, a build, a release and a live review.
- **The team** (C034). Seven roles, one folder each, under `v2/team/`: librarian, researcher, writer, editor, developer, QA and publisher. Each folder holds `role.md` (centre of gravity, what it owns and refuses), an `actions/` file per task with a done test, `briefs/`, `debriefs/` and an `issues/` board. The stated purpose is judgement, not throughput.
- **Reviews as data.** Each review is a JSON file (`/v1/reviews/rNNN.json`): items numbered, the agent comments before changing anything, and agreed items land per release. From r003, a decisions register opens every review.
- **Sources carried by hash.** Twenty-one documents (63,038 words) are copied byte for byte with their SHA-256, and the build fails if a copy drifts. Quotes in the Universe volume are re-read from their sources at build time (165 of them).
- **The altitude ladder.** The book is summarised at five levels: 135, 406 and 1,333 words, then part of level 4, then the book itself.
- **Checkable by construction.** The making-of re-took its 20 figures from the git tag each caption names, and computed every number from git history. Appendix C prints the commands (C035).

## What this book should reuse

1. **A making-of whose numbers are computed from git, with the commands printed.** That is exactly what `claims/` does. Our register should end in an appendix like their Appendix C, so a reader can rerun every count.
2. **"The failures, lovingly"**, their chapter 7: nine failures, grouped by who could have found them (only a user; the picture itself; the agent's own tools; claims, not code). Our failures (the hold that let a commit through, C006; the locks that never happened, C027; the $17.4M that reached the stage, C031; tokens in pushed captures, C025) fit the same grouping.
3. **"What it costs, and where it loses"**, their chapter 12, including "four situations where you should do something else". A book arguing for an agent team is more credible with that chapter in it.
4. **A book version separate from the site version, with v1.0.0 kept for the real final release.** That suits a first edition that is on sale by 2 November while still being corrected.
5. **Markdown as the single source**, rendered to web and PDF, with the build failing if either lags. Our publisher's build is already shaped this way.

## What this book should avoid

1. **The method's own largest cost, which they state themselves**: the six days "produced the machine for writing the second book and none of its chapters" (C036). Our deadline is 2 November. The machinery here is already ported; its upkeep must not eat the writing.
2. **Breadth that overwhelms the book.** Their site holds 292 pages in its sitemap, a deterministic transformer experiment, a lexicon and an artefact catalogue. Their review r003 turned to "decouple the book from the website" for exactly this reason. Our site should stay the record, and the book the distilled argument, from the start.
3. **A held third volume.** The Universe volume was written and then held. Four days are too few to write a book that does not ship.

## Second pass: chapter 12 and Appendix C, read in full (06:32 wake)

- **Chapter 12 says it plainly** (C036): "In six days and eighty-eight releases, this project did not write any of the second book. Not one chapter." The founder asked for that (reference material first), and the chapter still names it the cost to weigh first: "If your deadline is Friday and what you need is chapters, this method will hand you a very good machine and no chapters." Of 21 source documents, one had been extracted. Our deadline is Monday. The lesson for this team: the plan gets signed and chapter 1 starts while the register and the index are still growing, not after.
- **Appendix C is what our Appendix A should be** (C035): a script that photographs a page at its git tag in a throwaway worktree, a check that no figure is blank, and the command behind each count. `claims/appendix-a-commands.md` follows it for numbers. The book's figures, if it has any from the talk's site, should be taken the same way, at `298be4e`.

## For the comparison set

The three graphs.sgit.ai books are the first entries, as the nearest precedent: same house, same agent-team method, same planned channel (Leanpub). The making-of is the direct comparison. It is the story of a book made by agents over six days, where ours is a talk made by agents in one day, told by the team that made it. Market comparisons beyond the house wait for the market stream.

## Where this came from

graphs.sgit.ai v0.6.22 (`/llms.txt`, `/v2/books/making-a-book/index.html`), fetched 30 October 2026; SGit-AI/SGit-AI__Website__Graphs at `d39e717` (tags, `v2/books/*/book.json`, `v2/team/`, `v2/books/making-a-book/content/07__the-failures.md` and `12__what-it-costs.md` headings).
