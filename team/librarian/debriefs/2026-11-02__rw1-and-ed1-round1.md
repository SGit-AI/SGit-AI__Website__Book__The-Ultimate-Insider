---
title: RW1 in the voice scanner; ED1 round 1 on the 3- and 10-page editions
round: 3
date: 2026-11-02
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none
---
## What was asked

My idle wake of 09:09 London. Letter 016 (RW1, the editor's word: no religious words; add them to my voice scanner) and letter 017 (ED1: two rounds of reviews on the 3- and 10-page editions, each member in its own lane; mine is sources and the editor's first person).

## What was done

- **My task back to active** (every two hours) before the work, WAKE.md Cadence 4.
- **RW1**: `voice_scan.py` flags CLAUDE.md's religious words and their longer forms. It keeps the list reversed so the scanner never uses the words itself. A test line is flagged, the scanner passes its own scan, and the editions and the sample have none.
- **ED1 round 1** (`team/librarian/reviews/ed1-round1.md`): the end lists and register ids hold. All eight *(record)* quotes are word for word in the talk's record at `298be4e`, each traced to the commit that first holds it. The one change asked: name that commit in each band, so a reader can trace a quote from its page. Two third-person lines go into the first person. Letter to the storyteller (`librarian__001`, copy to the conductor), reply to the conductor (`librarian__012`).

## What went wrong

My first edit to the scanner was wrong three ways. It matched two places, a comment spelled the banned words out in full, and reversing a regex broke it. I restored the file and redid it with plain reversed words and the regex built in code. Later a comment of my own still named two of the words; the scanner's run on itself caught it. A tool that enforces a rule has to pass the rule, as the em-dash showed on 31 October.

## For the editor

Nothing waits on you from this wake.

## Where this came from

`comms/mail/mailroom/librarian/conductor__016` and `__017`; CLAUDE.md (RW1); `manuscript/editions/` at `e5bc048`; the talk's repository at `298be4e`; this wake, `team/librarian/wakes/20261102T091218Z.json`.
