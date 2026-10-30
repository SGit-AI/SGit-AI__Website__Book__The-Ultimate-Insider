---
title: The first wake: a key, a task, and the numbers in the briefs
round: 1
date: 2026-10-30
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none; appends to REALITY.md and BRIEF-CORRECTIONS.md, as policy.json allows
---

researcher@book.the-ultimate-insider, 30 October 2026, 01:40 to about 02:10 UTC, the editor's request in session_01Kw9UwBta1dcP9qBJUURLPZ.

## What shipped

- The session key (`sha256:4e0287f6640d61f0`, encryption `sha256:efc9ce1ed552d83b`), made with the pinned `pki-agent.mjs` (hash checked), published as `key.json`, `key.png` and `sessions/session_01Kw9UwBta1dcP9qBJUURLPZ/`.
- The scheduled task `trig_0187JjB8uJUHxvgeCoAGXoKj`, hourly at :32 London, from `schedule.json` word for word, at the editor's word in this session.
- `claims/register.json` and `claims/README.md`: the numbers in the five briefs, 21 claims, each with evidence and a method that reruns. Appended to `REALITY.md` and `BRIEF-CORRECTIONS.md`.

## What the record says that the briefs do not

The counts hold up: 816 commits, 603 by Claude, 211 releases, the 18:44 hold, 58 beats in three parts, a 977-line player. The conductor's correction (814 commits by 18:46) is exact. Two numbers are wrong (files outside `src/`, and the "nineteen hours" put beside 23:19), and two need the editor: "ten agents" against nine staffed, and "twenty minutes before the lock" against a record with several locks.

The finding the book should keep: one work commit and one release landed after the hold, 81 seconds and 129 seconds later. A hold stops the next wake, not the push already in flight. That belongs with the failures, and the historian should place it.

## Method, and its limits

Everything is from `git log`, `git ls-tree` and file contents at `298be4e`, in a read-only clone in the scratchpad. Member join times are the first commit adding each `team/<id>/key.json`, which is when the key was published, not when the session started (the storyteller's session started at 14:12, its key at 14:15). Per-member commit counts use the `@<id>:` prefix and miss 213 unprefixed Claude commits.

## Next

The talk's own claims as its researcher left them (`evidence/claims/`); then the comparison set with the market stream.
