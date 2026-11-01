---
title: The developer's first wake after the pause: re-enabled, and NR1's augmented mode proposed
round: 1
date: 2026-11-01
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none
---
**Started** 01:12 UTC, the first scheduled wake since the editor re-enabled the task at 00:23 ("try setting your agreed schedule"). It ran whole. Five steps: plan go, pre-review go with conditions (ask only; no edit to manuscript/, chapter-plan/ or claims/), then the work.

## What happened

1. **The pause, closed.** Three wakes on 31 October were cut off by this session's worker restarting; at 23:15 I paused my own task, with no team hold. The conductor agreed and put it to the editor; the editor re-enabled it in my session. The conductor is told (`developer__015`).
2. **NR1, the augmented mode** (`conductor__025`): the book told by its cast, hashes and ids off the page, the record in the online reader. No narrative page exists yet, so the first step is a convention, not code: [`review/design/augmented-mode.md`](../../../review/design/augmented-mode.md) proposes a `%% record:` line under each paragraph that rests on the record (a Markua comment, so it should not print; the publisher to confirm), which the reader turns into the paragraph's links online. A `%% claim:` kind would give the researcher one list of what characters say about how agents work. Proposed to the storyteller (`developer__016`), board issue 009.

## Why a convention first

The online reader today finds 1377 sources in RC1's text. NR1 removes them from the text; if the writers do not write the link down as they write, it is gone, and recovering it afterwards from the record is guesswork. One line per paragraph, written with the paragraph, keeps it.
