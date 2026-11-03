# The making of this book: its own record

Kept by historian@book.the-ultimate-insider. Written 3 November 2026 at the writer's request (`writer__145`), for the back matter's "The making of this book, and its dates". **Everything here is this book's record, not the talk's.** The talk's day is in `day/`; this file is the second factory's, read from this repository's history (whole, not shallow: its first commit is `f3cea028`) and from `book.json`'s signed decisions. Every time is UTC, from its commit or its record; no session, task, key or account is named.

## 30 October: built from the talk's parts, and the plan signed

| Time | What | Evidence |
|---|---|---|
| 00:35:46 | The repository's first commit | `f3cea028` |
| 00:46:11 | The book's site, on the talk site's build, gate and release pipeline | `79f0eb81` |
| 00:56:04 | The conductor staffed, at the editor's word | `bb1f57c0` |
| 00:59:50 | The day's span set (the work ended at 19:00, not at the merge) and the hand-off to the Cold-Read team written: the only thing that ever crossed to it | `8c7e3ab0`; `team/conductor/handoffs/` |
| 01:17:44 | The talk team's machinery ported, rule for rule; the first batch of members proposed | `3b403fb0` |
| 01:41:08 to 01:42:34 | Six members staffed within a minute and a half, each publishing its own session key: historian, security, librarian, researcher, publisher, storyteller | `19e266fb`, `81fd2ef8`, `f3e634f3`, `e69f073b`, `6d357179`, `5c2d2f9c` |
| 10:07:02 | The editor's word on the plan; review requests to every member; RC1 begun | `90e1b52d` |
| 10:20:11 | The historian's timeline compared with the Cold-Read team's, read only | `a163c373`; `cold-read-comparison.md` |
| 10:28:30 | RC1 ready for the publisher: thirteen chapters, an appendix, 42 images | `f6ce7ffa` |
| 11:03:47 | One handover per member, written by the conductor, for the account that continued the book (the first was nearly out of usage) | `cfcc2951`; `team/conductor/handovers/` |
| about 13:00 | H1, the handover rule, decided by the editor: "Yes that H1 plan is good" | `book.json` H1 |
| 13:03:33 | The historian's takeover on the second account: a new session key, the first session marked superseded | `bb14e7c6` |
| 13:04:04 to 14:14:13 | Four more staffed: ruv-sgit and the designer for the PDF lab, then synthetic and the developer | `afbb50d7`, `28396879`, `e36d0e94`, `8f10a08e` |

## 31 October to 1 November: the review, the editions, and two failures

| Time | What | Evidence |
|---|---|---|
| 31 October, 01:48:28 | The editor's paper review of RC1, with his account of the stop ("just a footnote") | `49c701e`; `after-the-day.md` |
| 31 October, 04:05:52 | RC2 named (V2), in a commit led by a change to eight members' tasks | `ad49aa1e` |
| 1 November, 09:45:31 | A hold written by a member on its own judgement: the storyteller, when the gate went red for every member | `621e5de2` |
| 1 November, 12:42:59 | The hold lifted at the editor's word, given in synthetic's session | `daabf92d` |
| 1 November, 13:05:15 | PS1 and ZM1: the book is about the factory, and comes as a zoom, from one page to 150 | `3a81af7b` |
| 1 November, after 16:22 | The evening lost to the usage limit: every task kept firing, but nothing reached dev after 16:22 | `team/conductor/editor-briefs/2026-11-02T0015Z.json`; `9395328b` (2 November 00:06:38) |

## 2 and 3 November: the writer, RC2, and the full book

| Time | What | Evidence |
|---|---|---|
| 2 November, 04:56:47 | The writer staffed, the twelfth member | `68ffc780` |
| 2 November, 15:34:07 | RC2 begins on the signed ladder of editions | `4056d2b9` |
| 2 November, 18:38:06 | The researcher's trace refuses a line in chapter 1 (the brake was not an old part) | `fde3fea4` |
| 2 November, about 21:55 | RL1 decided: "Ship something somebody else can use, then do it again" | `book.json` RL1 |
| 3 November, 01:18 | ACC1: every member hourly, at its own minute, until the book is done | `book.json` ACC1 |
| 3 November, 02:26:47 | The historian's letters saying the talk conductor "rewrote" dev's page: an error, two chapters resting on it | `5c4c7d17` |
| 3 November, 10:06:31 | TA1: the review steps run as a read-only reviewer, by tool list | `0dc3f6ef`; `book.json` TA1 |
| 3 November, 11:23:44 | The historian corrects its own "rewrote" (the writer sets the chapters right at 11:33:41) | `21e5ad53`; `ffeae66b` |
| 3 November, 20:36:58 | The full book's body complete in draft, chapters 1 to 23 | `04b227e0` |

## Reading

Two things stand out against the talk's day. The second factory was staffed the way the first was: the conductor first, then members joining in their own sessions with their own keys, six of them inside two minutes. And it kept its failures in the same way: a hold written by a member and lifted only by the editor, an evening lost to a limit the rule was meant to beat, and an error of the team's own historian caught by its own later check. The talk's day lasted nineteen hours; this book's record runs from 30 October to the full book's draft on 3 November, and it is still being written.
