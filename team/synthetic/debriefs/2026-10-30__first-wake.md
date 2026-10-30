---
title: The synthetic readers first wake: staffed, keyed, scheduled, the personas and the runner
round: 0
date: 2026-10-30
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading, as policy.json's appends allow)
---

synthetic@book.the-ultimate-insider, 30 October 2026, 14:13 to about 16:50 UTC, started by the editor's words in the session (the session's worker restarted once, about 14:25 to 16:30 UTC, which is most of the span).

## What shipped

- **Staffed.** `ROLE.md` and `policy.json` moved from `team/conductor/staffing/synthetic/` (drafts left in place). The only change to the role is that its Rules line now names `admin/tools/start.py` and `admin/tools/banner.py`, as the gate requires; the policy's `status` says adopted. Session key `sha256:468f84c8342951b0` (encryption `sha256:f0717a9c59ac6c81`) in `key.json`, `key.png` and `sessions/session_01Kw9UwB6ZZSnGiK8oPYMV9F/`. Scheduled task `trig_01TyU9ScRj2mMDFaMoaVqTk8`, the cron and prompt of `schedule.json`'s runs entry word for word, first fire 17:42 UTC.
- **The personas** (`team/synthetic/review/personas.json`): eight, from the project README's table, with the themes and questions of the reviewers study mapped to each; no names, no employers, nothing that could be read as a real person. The designer and project manager are not in the study's kinds of reader: their questions are mine, from what the README says they judge.
- **The runner** (`team/synthetic/review/run.mjs`): measures, it does not judge. The review in each persona's voice is written from its `observations.json` and screenshots, so a reader of a review can see what it was based on.

## What I learned

- The harness check against the home page found the one thing the runner exists to find: `theme.js` asks `api.github.com` for the star count on every page. Harmless on the public site, wrong on a reviewer's page. Raised with the conductor (it owns `theme.js`) and the developer.
- Paragraphs on the current site carry no ids: the anchor count is the runner's first useful number for the developer.

- My first commit put the files in `review/synthetic/`, as ROLE.md says, and the gate failed: the developer's drafted policy claims `review/**`. My own build check had run before the files were tracked, so it missed the overlap; the post-review caught it. The files moved to `team/synthetic/review/` before anything reached `dev`, and the developer has a letter asking it to narrow its claim.

## Not done, and why

- No persona run: the developer's first review page is not on `dev`. The board issue `001-first-persona-run.md` is blocked on it; the next wake after it lands runs all eight.
