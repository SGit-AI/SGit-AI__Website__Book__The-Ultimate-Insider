---
title: The takeover on the second account; RC1's sources, all 18 chapters
round: 2
date: 2026-10-30
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none
---
## What was asked

The editor, in this session, 12:17 UTC: take over the librarian's role from the first account's session, which ran out of usage; make and publish a key, mark the first session superseded, create my own scheduled task from `team/conductor/schedule.json`, adopt the conductor's handover (`team/conductor/handovers/librarian.md`) and begin its first item inside the five steps.

## The handover, adopted

I adopt it as written, with three changes:

- **Its step 4 is overtaken**: it says to create the task only when the conductor relays the editor's restart. The editor said it in this session, so the task exists: `trig_01FSNcFLFBHSd9sEGYn86ndy`, every two hours at :09 London, the prompt word for word from `schedule.json`. The first account's task, `trig_01MGyWHBgZ7Pzg95f2ozEAi5`, stays paused there; I do not touch it.
- **"C10b gave it comms paths; its policy should show them"**: it does (`e7d3d3d`). My status's ask to the editor about them is withdrawn, and my board and mail folders open now.
- **Its third item (Done when 2) has nothing new**: the talk's `dev` is still at `424b67a`, three commits after `298be4e`, all in `index/after-the-day.md` already. I check again each wake.

Its four items are on my board: 002 (sources, each wake), 005 (index entries per chapter), 006 (the 12 drafted cards), and the talk's later commits stay in `next`. The voice review from letter 004 is 004.

## What was done

1. **Key**: `sha256:7c3cf6b4d63370b0` (`team/librarian/key.json`, `key.png`, `sessions/session_01Kw9UwEJGqU63vtsX81uGNm/`), replacing `sha256:e5768293c14e8cdc`; the first session superseded from 12:17:38 UTC. Private halves in this session's `~/.sg-send/` only; `keyfile` never run.
2. **Task**: created into this session, id in `status.json`.
3. **RC1's sources**: `check_sources.py` on all 18 chapters; 15 clean; the rest, and what the record says about the talk's vaults (chapter 4 says "encrypted", the record does not), sent to the conductor: `comms/mail/mailroom/conductor/librarian__001-takeover-sources-and-vaults.eml`.
4. **The checker** reads source lists' shorthand now (a path under the folders named earlier on the line, `<id>` and `*` as patterns, "after the day" on the line). On a full-history run it took 101 findings to 17, and a made-up chapter with eight faults still shows all eight.

## What was hard

- **This repository's container clone is shallow.** The first run reported eighteen of this repository's own commits as missing; a deeper fetch found them all. The same effect explains the drafted card's claim that the Cold-Read pin `0dc6854` is not in a fresh clone: it is on that repository's `dev`.
- **Chapter 11b cites commits in five other repositories** the checker does not read: issue 007.

## For the editor

Nothing waits on you from this wake.

## Where this came from

`team/conductor/handovers/librarian.md`; `team/conductor/schedule.json`; `admin/tools/pki-agent.README.md`; `comms/mail/mailroom/librarian/conductor__001` to `__005`; the talk's repository at `298be4e` (`team/conductor/vaults.json`, `team/conductor/debriefs/2026-10-29__two-public-vaults.md`, `b620234`) and at `424b67a`; the Cold-Read repository at `14d6cfd`; SGit-AI__Website__Graphs at `d39e717`; this wake, `team/librarian/wakes/20261030T121726Z.json`.
