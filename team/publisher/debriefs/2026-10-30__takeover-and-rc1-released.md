---
title: The takeover on the second account, and the current RC1 released into the manuscript
round: 9
date: 2026-10-30
commits: the key and task commit and this wake's commit, both on dev
outside_scope: none
---
## What was asked

The editor, in this session: make and publish a new key, mark the first account's session superseded, create my own task from `team/conductor/schedule.json`, adopt the conductor's handover (`team/conductor/handovers/publisher.md`) and begin its first item, all inside the five steps.

## The handover, adopted

I adopt the handover as written, with one change of fact: it said to create my task only when the editor says the team restarts; the editor said so in this session, so the task exists (trig_01F7F7AipdKEhWgbxEj3YVja, every two hours at :47 London, the prompt word for word). Its four first things are now mine:

1. The current RC1 into `manuscript/`: **done this wake**.
2. RC1 released to dev: **done this wake** (the conductor's build.py fix was already there, letter 006).
3. The Markua pre-pandoc step, so the conductor's call-outs survive both builds as asides: next.
4. The 14 cards drafted as me in `team/conductor/rc1/annotations/publisher.json`: adopt, change or withdraw, with the three unchecked outside facts (KDP price parity, Markua captions, crosslinks) checked first.

Also taken from the handover and the conductor's letters 008 and 009: whether readers who take the book at $0 receive each new version and its notice, the membership setting, Pro for GitHub mode, and Markua 0.31 against M1's 0.30; the illustrated build's size against Leanpub's and KDP's limits.

## What was done

- **Key**: sha256:38b052cb21de1bb4, made in this session with `pki-agent.mjs keygen --session`; `key.json`, `key.png` and `sessions/session_01Kw9UwBKgLvosZHuWWWX8wY/`; the first session superseded until 13:03:01 UTC. No private half left `~/.sg-send/`.
- **Task**: created into this session, its id in `status.json`.
- **RC1**: the 18 numbered files of `team/conductor/rc1/` in `manuscript/Book.txt` in name order, `about-this-edition.md` removed (READY allows it), `resources/images/` with the 16 maps: 58 images, 47 references, none missing. Site gate clean at 132 pages; the book builds at 259 pages and 69,358 words (the morning's copy was 217 pages, 58,580 words). LEANPUB.md's description of the manuscript layout no longer names the removed file.
- Board 005 done; a reply to the conductor (letter 004 in my outbox).

## What was hard, or inferred

- The handover counts "19 files"; there are 18 numbered chapters plus `BRIEF.md`, which is the conductor's brief and not a chapter. I took the 18.
- I first moved the conductor's letters out of my mailroom into my inbox with `git mv`; the mailroom is written by others, so I put them back and copied instead, as the first session did. Nothing was committed in between.
- Time: the key and task about 15 minutes; RC1 and its checks about 20.

## Where this came from

`team/conductor/handovers/publisher.md`; the conductor's letters 006 to 011; `team/conductor/rc1/READY`; `team/conductor/schedule.json` (runs, publisher); `admin/tools/pki-agent.README.md`; the build's own output.
