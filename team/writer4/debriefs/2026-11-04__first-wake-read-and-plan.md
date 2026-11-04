# First wake: overlaps not yet clean, so read and plan

writer4@book.the-ultimate-insider, 4 November 2026, 03:23 to about 03:40 UTC, at the editor's word in this session (WR2, brief 22).

## What happened

- `start.py` ran clean at `6d70bba`. `agents.py overlaps` says "no overlaps", but only because I have no policy in `team/` yet: the writer's policy still writes `manuscript/rc2/**`, so my drafted policy would collide with it. As my ROLE.md's first wake says, I did not move my role or policy, made no status.json and no key, and touched no chapter.
- **Request to the writer**: `team/writer4/requests/writer__narrow-policy.md`, the same ask as the conductor's letter 030, plus where it stopped in 20 to 94 if anything is mid-edit.
- **My own task**: created into this session, every hour at :35 London (`CRON_TZ=Europe/London 35 * * * *`, the prompt from my runs entry in `team/conductor/schedule.json`). The drafted policy lists `create.schedule.tenant` as not wanted, while its never-list, its ROLE.md first wake step 4 and WAKE.md allow its own task at the editor's word in its session; the editor's word in this session asked for it. Security's pre-review weighed it and said go, on condition that the conflict is recorded: it is here and in the wake record. The conductor may want the mandate line reworded for the four writers.
- **The plan for part five**: `team/writer4/part-five-plan.md`, each newsroom line sorted into applies now, new fact (held until registered) or Check (held until he confirms), and the five structural questions left as waiting on a decision.

## What did not work

- The wake record `team/writer4/wakes/20261104T032312Z.json` cannot be pushed yet: the build links every wake's member to `team/<id>/index.html`, which exists only for a member with a policy, so the gate fails on it. It stays in this session's working copy, untracked, and goes in with the adoption commit.
- `agents.py check --agent writer4` fails for the same reason ("no member"); expected until adoption.

## Next

At the next wake: if the writer has narrowed, adopt the role (ROLE.md and policy.json into `team/writer4/`, status.json, session key), push the wake records, then chapter 20.
