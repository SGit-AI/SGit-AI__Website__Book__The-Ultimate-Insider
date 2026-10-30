---
title: The developer's first wake: staffed, keyed, scheduled, and the first review page
round: 0
date: 2026-10-30
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading, as policy.json's appends allow)
---
**Started** 14:13 UTC, at the editor's word in the session's first message. Five steps: plan go, pre-review go with conditions, then the work.

## What happened

1. **Staffed.** `ROLE.md` and `policy.json` copied from `team/conductor/staffing/developer/` (drafts left in place). The only change to `ROLE.md` is a paragraph naming `admin/tools/start.py` and `admin/tools/banner.py`, which the gate requires. `policy.json` already named its `comms/` paths.
2. **Keyed.** Session key `sha256:a3770d977b1feee2` (encryption `sha256:b17098b698aed6a2`) made with `pki-agent.mjs keygen --session` after the hash check; `team/developer/key.json`, `key.png` and `sessions/session_01Kw9UwDci5vCJDFdj3c12ay/`. Only public halves were written; the private halves stay in the session's `~/.sg-send/`.
3. **Scheduled.** Task `trig_01JE8iqDzf2AJjnnz7qLewck`, from `schedule.json`'s runs entry for developer: its cron (`CRON_TZ=Europe/London 12 1-23/2 * * *`) and its prompt word for word. The session's worker restarted between the key and the task, so the task was created at 16:30 UTC, not just after 14:15.
4. **The first review page**, for a security leader, built and tested, but not on the site yet: see "The overlap" below.

## The page, and why it is built this way

- **One persona first: the CISO.** The reviewers study (`team/conductor/research/reviewers/01-who-should-review-the-book.md`, section 1.2) gives it a send list (the argument, the controls) and four questions. Chapters 3 (the mandate), 6 (the editor signs) and 9 (the team was the insider) carry those themes, about 52 minutes of reading at 230 words a minute. The brief says about forty: a fourth of the time is in chapter 3, which is the longest; whether to trim to two chapters or keep three is a question for the editor and the storyteller.
- **Made at build time, from files.** `review/tools/make_review.py` reads `review/personas/ciso.json` and the RC1 chapters (`team/conductor/rc1/`, `5d73a4e`) and writes `src/pages/review/ciso.html`; the site's build wraps it like any page. It also places the hand-written sources (`review/pages/index.html`, `review/static/pen.js` and `pen.css`) in `src/`. Nothing in `admin/build/` changed.
- **Stable anchors.** Each paragraph, quote, list item and table is `<chapter>-<6 hex of the sha256 of its words>` (images by their alt text). An anchor survives a paragraph moving and changes when its words change, so a revision's diff can tell an edited paragraph from a moved one. 130 anchors, none clashing, listed in `review/anchors/rc1.json` as the base for the diffs.
- **The pen.** Click a paragraph (or Enter on it): five marks (agree, unclear, wrong, cut, more), a line of text, Keep. Answers to the questions sit in boxes at the end of each chapter. All of it stays in the browser (`localStorage`, memory if that is blocked) and is saved as a JSON file on the reader's own machine; `pen.js` makes no network call.
- **The greeting** reads a name from the link's fragment (`#to=Sam Example`, fictional), shown as text, never as HTML. This is the first step toward the sealed note (ROLE.md, 2), not the note itself.
- **How this works**: a side panel, five lines, one per piece the reader meets.

## The overlap, and why the page is not on the site

My drafted policy writes `src/pages/review/**` and `src/static/review/**`; the conductor's writes `src/**`. The gate's overlap check counts tracked files only, so my first gate run, before the commit, was clean; the post-review ran the gate on the commit and it failed on all four files. I took the commit back before it reached `dev`, moved the hand-written sources under `review/`, and left the placed files in `src/` uncommitted. A request went to the conductor (`comms/mail/mailroom/conductor/developer__001-review-pages-src-claim.eml`): narrow `src/**`, or have the build run the generator. The conductor's policy is the conductor's to change, so I did not touch it. The lesson for the next new member: run `agents.py overlaps` after `git add`, not before.

To see the page now: `python3 review/tools/make_review.py && ./run-website-locally.sh`, then open `/review/ciso.html#to=Sam%20Example`.

## What is not done

- Sending: comments sealed to the editor's key and sent with SG/Send (ROLE.md, 3). Needs the editor's public key named for it, and security's review of the design.
- The sealed note per person (ROLE.md, 2), the diffs (4), the other seven personas.
- The questions are placeholders from the study, marked as such, until the storyteller writes them per persona.
- The look is the site's tokens and a small stylesheet, `src/static/review/pen.css`, for the designer to take over.
