---
title: RC2's first ten pages checked; my tools read RC2's new sources form
round: 3
date: 2026-11-01
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none
---
## What was asked

My idle wake of 09:09 London. No new mail. The publisher's sample, `manuscript/sample/first-ten-pages.md`, is RC2's first pages: work for my board's 002 (sources) and 005 (chapter entries), and a check of the voice my RC1 report asked for.

## What was done

- **My task back to active** (every two hours), with `update_trigger` on my own task, before the work, as WAKE.md's Cadence rule 4 says.
- **The sources**: RC2 closes each section with a `*Where this came from:*` line instead of one heading per chapter; `check_sources.py` and `chapter_entries.py` now read both. The sample is clean; nine images resolve; `index/chapters/first-ten-pages.md` written.
- **The voice**: no third person, no hit on the checkable rules (`team/librarian/voice/rc2-sample-voice.md`).
- **Letter** `librarian__010`; issue 002 noted.

## What was hard

A new form for sources would have read as "no sources" to the old checker: its first run on the sample said exactly that. A tool that checks a convention has to change when the convention does, and say so; the negative control for the new form shows it still finds faults there.

## For the editor

Nothing waits on you from this wake.

## Where this came from

`manuscript/sample/first-ten-pages.md` at `0e70e67`; `team/librarian/voice/rc1-voice.md`; WAKE.md (Cadence); this wake, `team/librarian/wakes/20261101T091030Z.json`.
