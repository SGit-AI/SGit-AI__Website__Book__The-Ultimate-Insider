# RC1 against the timeline: times, sequence and turning points

historian@book.the-ultimate-insider, scheduled wake of 30 October 2026, 20:18 UTC (`team/historian/wakes/20261030T201805Z.json`). The live text read is `manuscript/` at dev `6dc766c` (the publisher's Markua copy of RC1); file and line refer to it. Read only: nothing in `manuscript/` or `team/conductor/` was changed.

## Method

Every time of day, ordering of events, commit hash and turning-point claim in every chapter was checked against `timeline/` and, where they disagreed or the timeline was silent, against the talk's record at `298be4e` (a read-only clone). Four read-only sub-agents of this session did the first pass, about 440 checks in all; I verified every finding below against the record myself before listing it, and dropped none as unverified. Not checked: hashes in this book's own history before 30 October 10:19 and the Cold-Read repository's (not in my clones); chapter 11b's dates before the day (the researcher's register first).

## The pattern

Most findings are one of three kinds, and each has one fix:

1. **The plan told as the event.** The talk "given at 19:00", the usage "reset at 20:20", part 1 "locking" at 18:14, minutes counted "before the talk". To `298be4e` the record holds 19:00 and 20:20 as plans; that the talk was given rests on `a9c0b49`, added after the day, which states no start time. Fix: "due at 19:00", "that evening", and name the source as after the day.
2. **A wake's start, a header's time, or a slot, given for the commit.** Pick one clock per sentence; the commit time is the record's.
3. **The first commit and the first key.** The day's first commit is `2e4b1f4` at 00:16:23, not 00:40; the conductor's first key was published at 00:51:12, not 00:58.

The rest are single: the turning points not in time order (card historian-12), the storyteller placed in the wrong hour, the nameless commits that carry dev's `Agent:` trailer.

## Findings

| Where | The text says | The record says | Evidence |
|---|---|---|---|
| `manuscript/12-build-your-own.md:61` | the conductor's "first key at 00:58 (C011)" | First published at 00:51:12 as `team/keys/conductor.json` (`17b287b`); 00:58:19 (`41d38ba`) is when it moved to `team/conductor/key.json`, the path C011 counts. Say "first key published at 00:51, in its own folder at 00:58", or ask the researcher to note it in C011 | `17b287b`, `41d38ba`; `timeline/day/00.md` |
| `manuscript/11b-what-was-already-there.md:3` | "a talk on stage at seven in the evening" among the events the chapters tell | To `298be4e` the record holds 19:00 as the plan; that the talk was given rests on `a9c0b49` (added after the day), which gives no start time | `timeline/after-1900.md`; `1f7c633`; `a9c0b49` |
| `manuscript/99-appendix-a-every-number-rerun.md:110` | `dbd75ad` at 18:37:02, "23 minutes before the talk" | The commit time is right; "23 minutes before" assumes a 19:00 start the record holds only as the plan. Say "23 minutes before the talk was due" | `dbd75ad`; `timeline/after-1900.md` |
| `manuscript/00-before-you-start.md:28` | the team took the talk "to a stage in London at seven in the evening", as an event | To `298be4e` 19:00 is the plan; the event rests on `a9c0b49`, added after the day, with no start time. Say so, or "due on stage at seven" | `timeline/after-1900.md`; `a9c0b49` |
| `manuscript/00-before-you-start.md:67` | the span runs "to the talk at 19:00" | Decision S6 ends the day at the last commit before 19:00 (`88b8f00` 18:45:35, `cb5b996` 18:46:22); 19:00 is the planned talk | `timeline/README.md`; `timeline/after-1900.md` |
| `manuscript/01-pause-all-actions.md:7` | the editor's times in the player commits run "from 18:05 to the last at 18:37 (`dbd75ad`)" | The editor's times in the subjects run 18:05 to 18:25; `dbd75ad` carries "(the editor, 18:25)" and was committed at 18:37:02; the first is `23739cc` at 18:04:48 | `23739cc`, `12e93db`, `013d97e`, `dbd75ad` |
| `manuscript/01-pause-all-actions.md:9` and `:61` | the usage "would not reset until 20:20, after the talk had begun"; "The editor's usage reset at 20:20, as the hold had said it would" | 20:20 is `HOLD.md`'s expectation; nothing records the reset, and the talk's start is only planned | `team/conductor/HOLD.md` at `298be4e`; `timeline/after-1900.md` (20:20, no commit) |
| `manuscript/01-pause-all-actions.md:37` and `:39` | the night log's last snapshot "at 18:39" in the text, 18:38 in the caption | The snapshot runs until 18:38:34 and was committed at 18:39:16: pick one and say which | `team/conductor/night/20261029T1838.json`; `2ed6427` |
| `manuscript/01-pause-all-actions.md:49` and `:65` | "three commits landed after the hold" | Four commits follow `867f8c2` (18:44:13): `7968c99` 18:44:49 (the hold's own release), `88b8f00` 18:45:35, `3f5d7fc` 18:45:36, `cb5b996` 18:46:22. "Three" is right only if the hold's own release is excluded: say so | `git log 298be4e`, 18:44 to 19:00 |
| `manuscript/01-pause-all-actions.md:61` and `:71` (and the blurb at `:78`) | "The talk was given at 19:00"; "The talk went on stage unlocked" | That no part was locked is the record (C027); that the talk was given, and when, rests on `a9c0b49`, added after the day: say so | `timeline/after-1900.md`; `a9c0b49` |
| `manuscript/01-pause-all-actions.md:95`, `:103` to `:105` | the turning points "in order", with the freeze (02:47) before the five-step wake (02:14 to 02:51) | The five-step wake began at 02:14:16, before the freeze; swap them, or drop "in order" (this is card historian-12 still open) | `timeline/day/02.md`; `team/conductor/wakes/20261029T021416Z.json` at `298be4e` |
| `manuscript/01-pause-all-actions.md:109` | "Inside an hour" from 15:00, "storyteller at 14:15" joined | The storyteller joined before that hour (wake 14:12:52, commit `7d0244d` 14:15:17); only motion and studio joined inside it (15:31) | `7d0244d`; `timeline/day/14.md`; `timeline/turning-points.md` |
| `manuscript/01-pause-all-actions.md:119` | the relaxed schedule "left work landing without a member's name on it" | The afternoon's "Player:" commits and the lock tool carry `Agent: dev@the-ultimate-insider`; only the `@dev:` subject is missing. "without a member's name in its subject" | `4a2481b`, `dbd75ad` (bodies); `timeline/day/16.md` |
| `manuscript/02-midnight-an-empty-repository.md:73`, `manuscript/03-a-mandate-you-can-read.md:109` | the conductor's first key at 00:58 | As at chapter 12:61: first published 00:51:12 (`17b287b`), moved at 00:58:19 (`41d38ba`). Chapter 3 contradicts itself: the same paragraph gives 00:51 (`17b287b`) | `17b287b`, `41d38ba` |
| `manuscript/03-a-mandate-you-can-read.md:47` | the caption of E09 and E10 "as the talk showed them" does not say when the stills were made | `talk-s-e09.jpg` and `talk-s-e10.jpg` are not at `298be4e`; added after the day in `a9c0b49`. The ABP caption at `:37` says so; this one should too | `git cat-file -e 298be4e:...talk-s-e09.jpg` fails; `a9c0b49` |
| `manuscript/03-a-mandate-you-can-read.md:83` | the second article "at 14:57 (`10ba28c`)" | `10ba28c` was committed at 14:56:01 | `10ba28c` |
| `manuscript/04-the-hourly-machine.md:101`, `manuscript/08-the-locks-that-never-closed.md:125` | "the first commit at 00:40"; "the first commit of the day, at 00:40" | The day's first commit is the editor's empty repository, `2e4b1f4` at 00:16:23; 00:40:50 (`1f7c633`) is the first work commit, which carries the gate and the brakes slide. "The first work commit" | `2e4b1f4`, `1f7c633`; `timeline/day/00.md` |
| `manuscript/05-the-story-before-the-slides.md:33` | "At 18:14, with part 1 locking" | No lock was under way: 18:30 was the plan, and at 18:39 part 1 was "not yet locked" (C027). The storyteller's own "locked or locking" was its expectation | `2ed6427`; `team/conductor/HOLD.md` at `298be4e`; `timeline/day/18.md` |
| `manuscript/05-the-story-before-the-slides.md:55` and `:101` | "By 18:20, 40 minutes before the talk" | The 19:00 start is the plan: "40 minutes before the talk was due" | `timeline/after-1900.md` |
| `manuscript/05-the-story-before-the-slides.md:83` and `:89` | caption "on screen unchanged at 19:00"; the figure "said on stage in the present tense" | Both rest on the talk as given, `a9c0b49`, added after the day, unlabelled here. That text shows the definition slide at 8:38; the words spoken over it contain no cost figure. "Shown on stage", with the source after the day | `a9c0b49`, `content/articles/the-talk-as-given.md#definition` |
| `manuscript/06-the-editor-signs.md:13` and `:27` | the decisions-page design "written at 03:25" | The file's header says 03:25 but it was committed at 03:16:15: the header is later than its own commit (as brief 5's is). "By 03:16" | `59ac8ab` |
| `manuscript/06-the-editor-signs.md:35` | "at 03:00 the conductor wrote ... a brief for the hours he would be away" | Headed "03:00 London", committed at 02:57:23 (`c531560`); deck's programme it builds on is `60af587` at 02:52:11 | `c531560`, `60af587` |
| `manuscript/07-building-the-talk.md:8` | "On the night, the questions from the room took the margin, and the close with it" | From the talk as given (`a9c0b49`), added after the day; the sentence should say so | `a9c0b49` |
| `manuscript/07-building-the-talk.md:23` | "By 06:40 the first note had been built and checked as designed" | The check was committed at 06:45:17 (`51b2497`); 06:40:35 is its wake's start. Chapter 4:105 already says 06:45 | `51b2497`; `timeline/day/06.md` |
| `manuscript/07-building-the-talk.md:27` | "ruv-sgit's wake at 13:32 was idle" | 13:32 is its slot; the wake started 13:40:05 and committed at 13:41:29 (chapter 6:41 and :107 say 13:41) | `41d4757`; `timeline/day/13.md` |
| `manuscript/07-building-the-talk.md:103` | "From 01:40 the house form" of commit subjects | Set at 01:36:16 | `5c2bcc5` |
| `manuscript/07-building-the-talk.md:103` | the "Player:" and lock-tool commits stay unattributed "and the timeline does the same" | Corrected today: the timeline gives them to dev on their `Agent: dev@the-ultimate-insider` trailers; only C014's subject count leaves them unattributed | `timeline/day/16.md`, `17.md`, `18.md` |
| `manuscript/08-the-locks-that-never-closed.md:113` | the security role "wrote ... at 01:27 (`02cbd86`)", with its mandate and its hold row | First written at 00:51:12 in `17b287b`; `02cbd86` (01:27:10) added only the pull-first rule | `git log --reverse 298be4e -- team/security/ROLE.md` |
| `manuscript/08-the-locks-that-never-closed.md:47` | three chat wakes sent back for change at 17:21, 17:30, 17:45 | Minor: 17:21:52's kind is "follow-up wake (tonight's rule)", not the editor's chat; the times and verdicts are right | `team/conductor/wakes/20261029T172152Z.json` at `298be4e` |
| `manuscript/09-the-team-was-the-insider.md:130` | the editor settled C10b "at about 10:40 UTC on 30 October" | After the day, this repository: the commit that records it, `e7d3d3d`, is at 10:19:47 UTC, so the word came before 10:19; book.json's "about 10:40" is the conductor's, and is later than its own commit | `e7d3d3d` (this repository) |
| `manuscript/10-the-talk-as-given.md:3` and `:5` | "At 19:00 on 29 October the editor stood up ... and gave the talk"; "what happened at 19:00" | 19:00 is the planned start (brief 3; the title beat's cue "around 7 pm"); the transcript gives the venue and about 87 minutes, no start time. "That evening" | brief 3 and `src/static/talk/talk.json` at `298be4e`; `a9c0b49` |

## No findings

`0-about-this-release-candidate.md`, `00b-how-to-read-a-map.md`, `11-what-the-cold-reader-saw.md`, `13-concepts-and-principles.md`. Every other time, hash and ordering checked in the chapters above agrees with the record.

## Where this came from

`manuscript/` at dev `6dc766c`; `timeline/`; the talk's history at `298be4e` and `a9c0b49` (after the day); this repository's `e7d3d3d`; this wake's record.
