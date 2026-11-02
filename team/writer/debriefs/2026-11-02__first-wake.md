---
title: First wake, the writer staffed
round: 0
date: 2026-11-02
commits: this wake's commits on dev
outside_scope: team/conductor/schedule.json (one value, at the editor's word)
---
writer@book.the-ultimate-insider, 2 November 2026, 04:52 to about 05:15 UTC, the editor's first-session prompt (WR1; `team/conductor/ONBOARDING.md` 1e). All five steps.

## What was done

1. `ROLE.md` and `policy.json` copied from `team/conductor/staffing/writer/` into `team/writer/` (drafts left in place; the policy's `status` marked adopted, nothing else changed); `status.json`.
2. Session key made with `admin/tools/pki-agent.mjs keygen --session` (hash checked first; `keyfile` never run): `team/writer/key.json`, `key.png`, `sessions/session_01Kw9UwEUmsEmG4LeHpKY5FJ/`. Fingerprint `sha256:e9e9bd611953df6a`, encryption `sha256:6054d1bd03923618`. Private halves stay in `~/.sg-send/`.
3. Own task `trig_01XcHwiizLtkXBLL6Z1xmq2X`, into this session, `CRON_TZ=Europe/London 28 */2 * * *`, the prompt of `schedule.json`'s writer entry word for word; first run 06:28 UTC.
4. Read the zoom ladder, the cast guide, the 3- and 10-page editions and synthetic's three summaries (the room's read of the sample, the 10-page read, the brutal read). Letter `writer__001` to the storyteller: the 30-page edition's outline, six things per chapter and three yes-or-no questions.

## What went wrong

- The build failed as soon as `team/writer/` existed: the conductor's `schedule.json` gave the writer's `minute` as the number 28 where every other member has a string, and the dashboard escapes it as text. The file is the conductor's, outside my policy; I asked the editor, who said "Fix it, at my word", and I changed that one value to `"28"`, named in the commit and in a `To-conductor:` trailer. `agents.py check` will show it as outside my scope: that is why.

## Next

- The 30-page edition's beat 1, the wake after the storyteller's outline lands and the editor signs RP1.
- Read the editor's voice on newsroom.sgit.ai (the writer's rules, `how-i-work-with-claude.md`) before the first chapter: not done this wake.
