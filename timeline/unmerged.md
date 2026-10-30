# Work done before 19:00 that is not in the record

The record of the day is the history reachable from `298be4e` (`README.md`). These commits in the talk's repository are dated 29 October before 19:00 but are not in that history. They are listed so that nothing made that day is silently dropped; they do not move the end of the day (decision S6).

| Time (UTC) | Who | What it says | Commit | Where |
|---|---|---|---|---|
| 18:48:36 | dev | "the 17:47 wake closed (partial: the lock moved to 19:00)" | `39df303` | branch `claude/dreamy-mayer-dwprr2` |
| 18:48:37 | dev | merge of `origin/dev` into that branch | `93f4706` | same branch |

## Reading

Both came after the conductor's hold (18:44:13, C006) and after the last release of the day (v0.1.209 at 18:46:22, C005). The dev's wake that began at 17:47 closed after the hold and never reached `dev`: the release step the team relied on had stopped with the team. It is the record of a wake that finished but was never published.

Its subject says the lock moved to 19:00. The researcher has since established that no part of the talk was ever locked (C027): the lock tool shipped at 17:54 and the hold came first. So `39df303` is evidence of what the dev believed at 18:48, not of a lock.

Found 30 October 2026 by comparing every branch of the talk's repository with the history of `298be4e` (`git log --all --not 298be4e --until=2026-10-29T23:59Z`): these two are the only ones.
