---
title: The Personas section: each persona on RC1, an exit interview, a briefing and a PDF debrief
round: 0
date: 2026-10-31
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading, as policy.json's appends allow; policy widened by two paths at the editor's word)
---

synthetic@book.the-ultimate-insider, at the editor's word in the session, 31 October 2026, 02:27 UTC.

## What the editor asked

"Go with the personas you have right now." A proposal on time: "Are you thinking about reading time or your reading time?" And "a whole section for all the different personas": an overview of each, what they thought of RC1, an exit interview, where they get stuck, would they buy the book, with a briefing and a PDF debrief. Not run all the time: at a major change, or when someone has a question for them.

## What shipped

- **The personas kept** (`personas.json`), and when they run written into `ROLE.md`.
- **The eight RC1 reads** (`review/synthetic/rc1/<persona>.json`): each persona read its two or three chapters from RC1 as locked, in its own voice, and answered the same exit interview. Read by eight sub-agents in parallel, each told to write one file and change nothing else. Every quoted passage was checked against RC1 by a script: 45 quotes, 44 exact, one paraphrase corrected and marked.
- **The briefing** (`rc1/briefing.md`): all eight would "maybe" buy it; they trust it (trust 4 for every one) and it is not yet what they would pay for; they stall on chapter 1's opening paperwork; they want cost, a kit and the so-what first; they remember the hold.
- **The section**: `/personas/` and a page per persona, built by `review/synthetic/tools/build_section.py`; the PDF debrief (18 pages) printed by Chromium (`print_pdf.mjs`). Checked at 1280 and 390 wide: no overflow.
- **The reading-time proposal** (`reading-time.md`): the ask set by the reader's time, not the book's; twenty minutes by default, one named chapter, the rest offered.

## What I learned

- **Eight identical "maybe"s are a finding about the method.** Eight sub-agents of one model, given the same instructions, hedged the same way. The briefing says so twice; the useful signal is in where each stopped and what each missed, which differ a great deal.
- **Ask for quotes, then check them.** Asking each reader to quote the exact words it stuck on made every complaint findable, and a twenty-line script made it checkable. One paraphrase would otherwise have reached the editor as a quotation.
- **The site's styles mean something.** Tables inside an `<article>` run wide on purpose; the persona pages first broke out of their column. A `<section>` keeps them in it.
