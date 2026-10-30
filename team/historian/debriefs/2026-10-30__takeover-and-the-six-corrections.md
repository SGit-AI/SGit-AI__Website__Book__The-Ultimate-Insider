---
title: Takeover on the second account, and the six corrections applied
round: 2
date: 2026-10-30
commits: this wake's commits on dev
site_version: the release after this wake's push
outside_scope: none
---
# Takeover on the second account, and the six corrections applied

historian@book.the-ultimate-insider, the editor's request in this session, 30 October 2026, from 13:02 UTC (wake record `wakes/20261030T130219Z.json`).

## The takeover

The editor (Dinis Cruz), in this session's chat, said this session continues the historian's role from the first account's session (`session_01Kw9UwBrRHk6F5eoPjZLn35`, key `sha256:85ffd0907275f5eb`), which stopped when that account ran out of usage.

- **Key.** Made in this session with the pinned `admin/tools/pki-agent.mjs` (hash checked; `keygen --session` and `keyqr` only, `keyfile` never run): `sha256:30ff97a9b187f7e6`, encryption `sha256:0bc5c865725c1671`, in `key.json` (`replaces` names the old key), `key.png` and `sessions/session_01Kw9UwEM61pEqMLtCbUHec7/`. The first session's folder is marked `superseded` until 13:02:34 UTC. Nothing from the first key was reused or printed; private halves stay in this session's `~/.sg-send/`.
- **Task.** At the editor's word in this session: `trig_01SHR9S5d1d24Re9GLPXeAL9`, `CRON_TZ=Europe/London 17 */2 * * *`, into this session, cron and prompt word for word from `team/conductor/schedule.json` (runs, historian). The first account's task `trig_016Shar3cqBT4mwmFwuQHhCD` stays paused there; this session cannot reach it and did not try.

## The handover, adopted

I adopt the conductor's handover (`team/conductor/handovers/historian.md`) as written, with three notes:

1. Its step 4 said to create the task only when the editor says the team restarts; the editor said so in this session, so the task exists.
2. Its "First things to do" stand as my `next`, in its order: the six corrections (done this wake), the RC1 review against `timeline/`, then the 12 drafted cards in `team/conductor/rc1/annotations/historian.json`.
3. The mail it lists (001 to 003) was answered by the first session; 004 and 005 are notices of new keys and need no reply. Decision C10b is signed, so my three `comms/` paths are back in `policy.json` (the conductor added them, about 10:45 UTC); the ask about it is closed.

## What shipped

The six corrections from `timeline/cold-read-comparison.md`, each checked again in the talk's history (a read-only clone in this session's scratchpad), not taken on the comparison's word:

1. The commits that name no member (`28fe01d`, `fb355d3`, `4a2481b`, `23739cc`, `13e1321`, `12e93db`, `013d97e`, `dbd75ad`, `c33e86a`) all carry dev's `Claude-Session` trailer, the session of dev's `56cbe55`. `day/16.md`, `17.md` and `18.md` now say dev, *inferred* from the trailer, and withdraw "the timeline does not guess".
2. Deck's wake of 18:20:09 (plan only, `89afb77`) never closes: in `day/18.md`, and in its reading of the hold, beside dev's 18:48 close.
3. The designer's status at 18:45:35 (`88b8f00`) says part 1 was locked at 18:30; no locked copy exists at `298be4e`. In `day/18.md`, with the reading that a member's status is a claim, not the record.
4. Brief 5 is headed about 17:10 London and committed at 17:08:41 (`e86b0aa`): in `day/17.md`, unsettled.
5. ruv-sgit's first vault deleted at the editor's go, 02:07:52 (`f21265b`): in `day/02.md`.
6. `after-1900.md` no longer states the talk as given at 19:00 from the day's record: 19:00 was the plan; the evidence it was given that evening is `a9c0b49`, added after the day, which gives the date and about 87 minutes but no start time.

## For others

- **Researcher:** C014 counts these commits as unattributed. The session trailer attributes the nine above to dev's session; whether the register changes is yours.
- **Storyteller and conductor:** RC1 text that calls the player and lock-tool commits nameless, or the talk given "at 19:00" as a recorded event, should be read against the corrected files. That review is my next item.

## Hard to find, inferred, how long

- The start time of the talk is in no record I can cite: the day holds the plan, the transcript the date.
- Inferred: authorship from the session trailer (a trailer names the session, not the role; dev's folder of 01:53 ties the two).
- Time: takeover (key, task, status) about 5 minutes; the six corrections, checked commit by commit, about 15.

## Next

Review RC1 as it stands (`team/conductor/rc1/`) for times, sequence and turning points against `timeline/`; findings to the conductor with file and line. Then the 12 drafted cards.

## Where this came from

The editor's words in this session; `team/conductor/handovers/historian.md`; `timeline/cold-read-comparison.md`; the talk's history at `298be4e` and `a9c0b49`; this wake's record.
