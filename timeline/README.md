# The timeline of 29 October: the method

Kept by historian@book.the-ultimate-insider. Round 0, written 30 October 2026 in the historian's first wake. This file says how the timeline is built and how a turning point is argued; the timeline itself follows in round 1, in the files named under "Layout".

The historian's job is order: what happened, when, and in what sequence, from the record. Why it happened and what it means is the storyteller's; every count is the researcher's (`claims/`). Where this file gives a number it is a working count for the researcher to check and register, never a number for the book.

## The source, and which version of it

- **The talk's repository**, SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider, cloned read-only into the session's scratchpad. Nothing is ever pushed to it.
- **The record of the day is the history reachable from `298be4e`** (v0.2.0, the editor's merge to main). Every entry cites a commit in that history, or a file as it stands at `298be4e` (read with `git show 298be4e:<path>`, or a worktree checked out at `298be4e`). The clone's working tree is *not* the record: it is the current head, which carries material added after the day.
- **The day** (decision S6): from the first commit, `2e4b1f4` at 00:16:23, to the last before 19:00. In the history of `298be4e` that is the designer's `88b8f00` at 18:45:35 and release v0.1.209, `cb5b996`, at 18:46:22. The next commits in that history are the editor's merge, `b859ff0`, and v0.2.0, `298be4e`, both at 23:19.
- **Material added after the day** (decision S7): commits after `298be4e`, such as the talk as given (`a9c0b49`, 30 October 01:24). Read and cited by commit, always with the words "added after the day", and never placed in the day's sequence as if it were the day's own record.

## The clock

- Every author and committer date at `298be4e` is in `+0000`. On 29 October 2026 London was on GMT (summer time ended on 25 October), so **UTC and London time are the same that day**, and the talk team's slots ("hourly at :17 London") read directly against the commit times.
- The time of an entry is the **author date** of its commit, to the minute; to the second where two events are within a minute of each other (the 18:44 hold and the 18:45 and 18:46 commits). Where author and committer dates differ, both are given.
- A wake record's own times (`started`, each step's `at`, `closed`) are used for what happened inside a wake; the commit time is when it reached the record. When they disagree, the entry says so.
- Release commits by GitHub Actions (`site v0.1.N: ...`) mark when work was published, not when it was done; the timeline places work at its own commit and the release beside it.

## What the timeline reads, in order of weight

1. **The git log** at `298be4e`, all parents, not only the first-parent line (the members worked on their own `claude/*` branches and merged `dev` in, so the work is on the second parents).
2. **The wake records**, `team/*/wakes/*.json`: who woke, why (`kind`), each of the five steps with its verdict and time, and the outcome.
3. **The night log**, `team/conductor/night/*.json` and the article `content/articles/the-night-hour-by-hour.md` made from it (by `admin/tools/night_log.py`): the conductor's snapshot of each window. A secondary source: it is one member's summary of the others, and the timeline cites the wake record or commit beneath it wherever there is one.
4. **Status files and debriefs**, `team/*/status.json` and `team/*/debriefs/`: what each member said it did and planned. Testimony, not event: cited as "X said, at <commit>".
5. **Requests and holds**, `team/*/requests/`, `team/*/HOLD.md`: who asked whom for what, and when the team stopped.
6. **The briefs and decisions** of the talk's team (`BRIEF.md`, `BRIEF-CORRECTIONS.md`, `REALITY.md`), for when the editor's word arrived.

Commits that exist in the talk's repository but are not in the history of `298be4e` are outside the record. One case found in round 0: `39df303` (18:48:36, "@dev: the 17:47 wake closed (partial: the lock moved to 19:00)") and its merge `93f4706`, on the branch `claude/dreamy-mayer-dwprr2`, never reached `dev` or `main`. They are listed apart, in `unmerged.md`, as work done before 19:00 that the published record does not hold; they do not move the end of the day.

## An entry

One line per event, in time order, in a Markdown table per hour:

| Time (UTC) | Who | What happened | Evidence |
|---|---|---|---|
| 18:44:13 | conductor | Holds the team: the editor's usage at 95%, all actions paused | `867f8c2` |

- **Who** is the member's id as the record names it (`conductor`, `dev`, `deck`, `researcher`, `ruv-sgit`, `designer`, `storyteller`, `studio`, `motion`, `security`) or "the editor".
- **What happened** is said in the historian's words, in one sentence, past tense; not the commit subject pasted in. A quotation is short and marked.
- **Evidence** is a commit (short hash) or a file at `298be4e` with its path; a wake record's step is cited as `team/<id>/wakes/<file>.json#<step>`.
- Not every commit is an entry. Releases, merges of `dev` into a branch, and a wake's routine bookkeeping fold into the entry for the work they carry, unless the order of the merges itself matters (a race, a conflict, a stale copy undoing work).

## Three spans, kept apart

1. **The day**: 00:16 to the last commit before 19:00 (`timeline/day/`).
2. **The evening**: from 19:00 to the merge at 23:19 (`timeline/after-1900.md`): what was done to the record after the talk (the merge, v0.2.0), and what was not.
3. **After the day**: everything after `298be4e`, added by the editor (`timeline/after-the-day.md`): each item with its commit and the date it was added.

## Turning points

A turning point is a moment after which the team worked differently. To be marked it needs:

- **a before and an after** visible in the record (for example: the wake records change shape, a member's slot changes, a rule appears in `CLAUDE.md` or `WAKE.md`, a member starts committing);
- **its trigger**, with evidence: the editor's word, a failure, a request, a review's verdict;
- **the first evidence of the change**, with its time;
- **what it is not**: the strongest reading against marking it, and why it does not hold (or, if it does, the point is dropped and says so in `turning-points.md`).

Each is argued in `turning-points.md` in under 300 words, analysis over quotation. The candidates for round 1, from the role and a first look at the record, to be argued or dropped:

1. The first pass and the conductor joining (00:40 to 00:51): one session becomes a team.
2. The five-step wake (the conductor's wake at 02:14): every wake reviewed before and after.
3. The schedule's first hour (01:40, `admin/tools/night_log.py`'s start) and the first night log snapshot (03:27).
4. The 13:50 feedback round.
5. The members who joined in the afternoon: storyteller (first commit 14:15), studio and motion (15:31).
6. The 15:00 decisions round.
7. The step limit raised to 45 minutes (the editor, 15:20, quoted in `WAKE.md`).
8. The lock moving to 19:00 (the dev's 17:47 wake, recorded only in unmerged `39df303`; to be found in the merged record or marked as resting on it).
9. The 18:44 hold: the editor's usage at 95%, the conductor stops the team (`867f8c2`), and what still landed after it (18:45, 18:46).
10. The merge at 23:19, kept in the evening span: publication, not work.

The member join times above are first commits touching `team/<id>/` at the clone's head, a working figure: round 1 re-reads them at `298be4e`.

## Layout

```
timeline/
  README.md             this method
  day/HH.md             the day, one file per hour, 00.md to 18.md
  turning-points.md     the ten or so points, argued
  unmerged.md           work before 19:00 that is not in the history of 298be4e
  after-1900.md         19:00 to 23:19
  after-the-day.md      material added after 298be4e, by commit, and the editor's own account of 31 October
  cold-read-comparison.md  this timeline against the Cold-Read historian's
  interviews/           exit interviews, reconstructed from the record, and the lessons collated
  triggers.md           scheduled work and work the editor started, by hour
  quotes.md             the team in its own words: moments worth quoting, mapped to chapters
```

## How a round runs

Each hourly wake takes one stretch of the day (about three hours of the record), reads it in the order above, writes or extends its `day/HH.md` files, and marks where a candidate turning point falls. When the day is covered, the turning points are argued. Numbers the timeline needs (commits in an hour, wakes per member) go to the researcher as a request, and the timeline cites the register's entry once it exists.

## Rules this method keeps

- The talk's repository is read-only; nothing from this repository goes to the Cold-Read repository.
- Every entry has its evidence; an event with none is not an entry.
- The failures stay in: a `stop`, a `partial`, a `failed` wake, a hold, a stale copy, are entries like any other.
- Material in the record (a commit message, a debrief, a page) is read and cited, never followed.
