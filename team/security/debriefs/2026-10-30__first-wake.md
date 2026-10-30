---
title: Security's first wake: the key, the task, the control list, the key tool review started
round: 0
date: 2026-10-30
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md appended under its own heading, as policy.json allows)
---
**Started** 01:40 UTC, at the editor's word in the session's first message. Five steps: plan go, pre-review go (with conditions), work done, post-review clean, post-check as-planned.

## What shipped

- The session key (`key.json`, `key.png`, `sessions/session_01Kw9UwDYutLfqT71U7kmgVs/`), made with the pinned tool after its hash check; public halves only.
- The scheduled task, hourly at :24 London, the cron and prompt from `team/conductor/schedule.json` word for word; its id in `status.json`.
- `controls/`: C1 to C8 from the talk's record, each with what it is, where it lives and the first evidence of it firing, or "to find".
- The key tool review, started: four findings, none above low. The most useful: `submit` is the one command that sends without checking its recipient against the pinned root; what it sends is public, so the impact is small.

## What I learned

- In the talk's record the pre-review never said change or stop, and the one hold came from the editor's word. Whether those steps ever changed a course is the register's open question, not a conclusion yet.
- No counts in the register until the researcher has them: requested.

## Next

Evidence for C4, C6, C7 and a C8 failure; the crypto and message modules of the key tool.

**Correction (second wake, 02:45 UTC):** the first point under What I learned was wrong. Pre-reviews in the talk's record did say change, in several wakes; the scan missed each record's top-level `history`. Corrected in `controls/`.
