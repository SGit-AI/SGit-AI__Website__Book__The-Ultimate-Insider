# The evening: 19:00 to the merge at 23:19

Read at `298be4e`. Kept apart from the day (decision S6): the work ended before 19:00, the talk was planned for 19:00, and the merge at 23:19 only published what was already done.

| Time (UTC) | Who | What happened | Evidence |
|---|---|---|---|
| 19:00 (planned) | the editor | The talk is given (hack::soho, IOActive London). No commit marks it. Up to `298be4e` the record holds only the plan for 19:00 (the talk's brief; `1f7c633`, the event named in the first pass), not the event. That it was given that evening, over about 87 minutes, rests on the talk as given, `a9c0b49` (30 October, 01:24), *added after the day* (`after-the-day.md`); that text does not state the start time | the talk's brief; `1f7c633`; `a9c0b49` (after the day) |
| 20:20 | (no commit) | The editor's usage limit resets, as `HOLD.md` expected | `team/conductor/HOLD.md` at `298be4e` |
| 23:19:09 | the editor | Merges `dev` into `main` (pull request #1), through GitHub | `b859ff0`; C007 |
| 23:19:51 | (release) | v0.2.0, the release of the merge: `main` bumps the middle number | `298be4e`; C009 |

## What the evening shows

Nothing. No member committed between 18:48 and 23:19, in the record or on any branch. The hold held: no wake ran, and the hold was never lifted on the day (C024). The only act of the evening is the editor's, and it is publication, not work: `298be4e` and `cb5b996` hold the same content, only `./version` differs (`BRIEF-CORRECTIONS.md`).

The work dev's 17:47 wake closed at 18:48 is the one thing finished on the day that the merge did not carry (`unmerged.md`).
