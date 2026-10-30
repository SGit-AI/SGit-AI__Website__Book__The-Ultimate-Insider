---
title: Staffed, and the index of the source in round 0
round: 0
date: 2026-10-30
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: REALITY.md and BRIEF-CORRECTIONS.md, appended under the policy's appends
---
## What was asked

The editor, in this session: make and publish the session key, create the librarian's own scheduled task from `team/conductor/schedule.json`, and begin the first task from `ROLE.md`: the index of the talk's repository, seeded from `briefs/2026-10-30/3-source-map.md`, with `index/README.md` (method and first areas) in round 0.

## What was done

- **The key**, made in this session with the pinned `pki-agent.mjs` (hash checked first): `sha256:e5768293c14e8cdc`, encryption `sha256:d80ab019dee0adf0`; `key.json`, `key.png` and `sessions/session_01Kw9UwBgUFHEgwLsB3TrwA8/`. Private halves stay in `~/.sg-send/`.
- **The task** `trig_01MGyWHBgZ7Pzg95f2ozEAi5`, into this session, `CRON_TZ=Europe/London 9 * * * *`, the prompt word for word from `schedule.json`. Its id is in `status.json`.
- **The index**: a tool, `index/tools/build_index.py`, that reads a scratchpad clone of the talk's repository and writes one row per file at `298be4e` (1,313 files, 16 areas): path, area, kind, owner, first and last commit with UTC time, size, and one line on what it is. `index/after-the-day.md` lists the three commits after the pin, to `424b67a`, kept apart. The root and the tools (30 files) are read by hand (`index/read.json`); every other line is marked `(machine)`.
- **Every path the source map names exists at `298be4e`.**

## What went wrong, and what was found

- **Nine files had no commit** on the first run: they were added in merge commits (conflicts resolved there), which `git log` does not list without `-m`. A second pass with `-m` for exactly those files fixed it.
- **Early commit subjects say `conductor:` without the `@`**, so the owner rule takes both forms.
- **The source map's file count is off**: it says about 1,260 files outside `src/`; the index finds 1,083 at `298be4e` (1,147 at `424b67a`). Recorded in `BRIEF-CORRECTIONS.md` for the researcher.
- **The machine lines are only as good as the file's first heading**: a script whose first comment is vendored code (`pki-agent.mjs`) gets a useless line until read by hand. That is what round 1 is for.

## For the editor

Nothing waits on you from this wake. Members can start using `index/` now; round 1 reads every area by hand, conductor and evidence first.
