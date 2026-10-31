---
title: The day schedule on my task; the index entries each chapter draws on
round: 2
date: 2026-10-31
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none
---
## What was asked

My scheduled wake of 00:09 London, the last night wake. The conductor's letter 010, relaying the editor's signed Q6 and WAKE.md's new Cadence section: switch my own task to day hours, or to twice a day when idle. My board's issue 005 (ROLE.md, Done when 3): the index entries each chapter draws on.

## What was done

- **My task**, with `update_trigger` on my own task only: `CRON_TZ=Europe/London 9 8-22/2 * * *`, prompt unchanged, next run 08:09 London. Active, since 004 and 005 are work I can move; `status.json` says so.
- **`index/chapters/`**: one file per chapter, the index's entries for the files it cites, by repository, and the commits it names; a README table. Built by a new tool, `index/tools/chapter_entries.py`, which resolves paths as `check_sources.py` does and places folders and the files added after the day.
- **Reply** to the conductor, `librarian__007`; letter 010 filed.

## What was hard

- **Active or idle is a judgement.** Most of my board waits on the revision, but the voice pass and the chapter entries do not; I took the active schedule and said why, rather than idling with work in hand.
- **Ten bare names stay unplaced**, each matching several files. The tool lists them rather than guess, which is the same rule the checker keeps.

## For the editor

Nothing waits on you from this wake.

## Where this came from

`comms/mail/mailroom/librarian/conductor__010-cadence.eml`; `team/conductor/WAKE.md` (Cadence); `book.json` Q6; `manuscript/` at `f942f37`; `index/index.json`, `index/cold-read/index.json`; this wake, `team/librarian/wakes/20261031T001139Z.json`.
