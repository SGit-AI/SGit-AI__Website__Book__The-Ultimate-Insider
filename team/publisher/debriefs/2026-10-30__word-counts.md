---
title: A quiet hour: word counts in the build
round: 6
date: 2026-10-30
commits: this wake's commit on dev
outside_scope: none
---
## What was asked

The schedule (hourly at :47). Nothing new for me: my comms paths are now C10b, open for the editor, and the Leanpub book, the price, the branch and the KDP choices all wait on him.

## What was done

- `publishing/build_book.py` now ends with the words in each file `Book.txt` lists, the total, and the PDF's page count. Today: 196 words, 3 pages. Words are counted as a reader sees them: no HTML comments, code fences or link targets. It is a measure for the writer against the plan's word budgets, and the page count the cover calculator needs; it adds no dependency and cannot fail the release.

## What went wrong, and what was found

- Nothing went wrong. Found: the five-step wake has no cheap idle path (`wake.py close` refuses a wake that skipped a step, idle or not), so an hour with nothing to do still costs four sub-agents. For the conductor to weigh against the editor's usage, not mine to change.

## Where this came from

My status and board; `book.json` (C10b, L1, L2); `admin/tools/wake.py` (the close check).
