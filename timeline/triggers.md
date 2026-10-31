# Two kinds of trigger: scheduled work and work the editor started

Kept by historian@book.the-ultimate-insider. Written 31 October 2026, 04:30 UTC, at the conductor's letter 015 (A13, with the researcher), from the editor's note in his RC1 review: "it's more interesting to show the work that happens automatically, right? And the work that happens that is triggered by me" (`briefs/2026-10-31__rc1-paper-review/batch-08-pages-34-to-38.md`, 31 October, after the day; his note 26, T18).

## Method

Every wake record in the talk's history at `298be4e` (`team/<id>/wakes/*.json`) carries a `kind`, written by the member when its wake opened. Each is sorted into one of three classes by that field alone:

- **scheduled**: the kind starts "scheduled" (a member's own hourly task fired);
- **editor**: the kind names the editor ("editor's request", "editor's chat", "the editor's wake, in session", "onboarding, editor's chat");
- **follow-up**: the kind names a follow-up (the one-off wakes members scheduled for themselves in the evening, "tonight's rule", at the editor's word of about 16:55, `3342cff`).

No record fell outside the three. The script is a dozen lines over `git show 298be4e:<file>`; it reads only the `kind` and `started` fields.

**What this does not see.** Work the editor started in a member's session without a wake record: the player's fixes in dev's session from 18:04 to 18:37 are commits, not wakes (`timeline/day/18.md`), and several of the evening's changes were made the same way. A count of wakes undercounts the editor's hand; a count of commits by session would be the next step, and is the researcher's.

## By hour (UTC, by the wake's start)

These are counts read from the record for the researcher to register (A13): the book takes them from the register, not from here.

| Hour | scheduled | editor | follow-up |
|---|---|---|---|
| 02:00 | 2 | 5 | 0 |
| 03:00 | 5 | 10 | 0 |
| 04:00 | 6 | 1 | 0 |
| 05:00 | 6 | 0 | 0 |
| 06:00 | 6 | 0 | 0 |
| 07:00 | 6 | 0 | 0 |
| 08:00 | 6 | 0 | 0 |
| 09:00 | 6 | 0 | 0 |
| 10:00 | 6 | 0 | 0 |
| 11:00 | 6 | 0 | 0 |
| 12:00 | 5 | 0 | 0 |
| 13:00 | 6 | 0 | 0 |
| 14:00 | 6 | 7 | 0 |
| 15:00 | 7 | 8 | 0 |
| 16:00 | 10 | 6 | 0 |
| 17:00 | 9 | 10 | 4 |
| 18:00 | 7 | 0 | 6 |

## What it shows

The day has three phases, and the triggers draw them without any other evidence.

1. **00:16 to about 04:00, the editor builds the machine by hand.** The first wake records appear at 02:14; until 04:03 most wakes are the editor's, in members' sessions: onboarding, the vault keys, building the five-step wake itself. Scheduled wakes begin at 02:33 (ruv-sgit's, the first in the record, `timeline/day/02.md`) and take over as the night goes on.
2. **About 04:00 to 14:00, the machine runs alone.** Every wake in the record is scheduled; none was started by the editor. The record suggests he was away (the morning review at 07:07 was written for him to read later, `timeline/day/07.md`; *inferred*), and he returns at about 13:50 with the dictated feedback round (`timeline/day/13.md`, `14.md`).
3. **14:00 to the hold, both at once, and a third kind.** The editor's wakes come back beside the schedule, and from about 17:00 members add follow-up wakes of their own, the "tonight's rule" the editor allowed so that a deadline between hourly slots could be met. The last hour has no editor wakes in the record at all: his hand is in dev's session, as commits (above).

This is the editor's own distinction made visible: the loop he starts by chat runs "until it reaches a state where it thinks there's nothing to continue", and the scheduled loop runs whether or not he is there. Through the long middle of the day, only the second existed.

## Every wake that was not scheduled

| Started (UTC) | Member | Class | Kind, as recorded | Record |
|---|---|---|---|---|
| 02:14:16 | conductor | editor | editor's request: build the five-step wake | `team/conductor/wakes/20261029T021416Z.json` |
| 02:47:58 | deck | editor | editor's request | `team/deck/wakes/20261029T024758Z.json` |
| 02:49:09 | researcher | editor | editor's request | `team/researcher/wakes/20261029T024909Z.json` |
| 02:51:43 | ruv-sgit | editor | editor's request | `team/ruv-sgit/wakes/20261029T025143Z.json` |
| 02:52:05 | conductor | editor | editor's request | `team/conductor/wakes/20261029T025205Z.json` |
| 03:03:11 | deck | editor | editor's request | `team/deck/wakes/20261029T030311Z.json` |
| 03:03:11 | ruv-sgit | editor | editor's request | `team/ruv-sgit/wakes/20261029T030311Z.json` |
| 03:05:50 | researcher | editor | editor's request | `team/researcher/wakes/20261029T030550Z.json` |
| 03:07:41 | dev | editor | editor's request | `team/dev/wakes/20261029T030741Z.json` |
| 03:08:34 | conductor | editor | editor's request | `team/conductor/wakes/20261029T030834Z.json` |
| 03:20:21 | dev | editor | editor's request | `team/dev/wakes/20261029T032021Z.json` |
| 03:21:33 | conductor | editor | editor's request | `team/conductor/wakes/20261029T032133Z.json` |
| 03:31:17 | designer | editor | editor's request | `team/designer/wakes/20261029T033117Z.json` |
| 03:42:39 | conductor | editor | editor's request | `team/conductor/wakes/20261029T034239Z.json` |
| 03:50:46 | designer | editor | editor's request | `team/designer/wakes/20261029T035046Z.json` |
| 04:02:56 | designer | editor | editor's request | `team/designer/wakes/20261029T040256Z.json` |
| 14:03:34 | conductor | editor | editor's request | `team/conductor/wakes/20261029T140334Z.json` |
| 14:09:15 | conductor | editor | editor's request | `team/conductor/wakes/20261029T140915Z.json` |
| 14:12:52 | storyteller | editor | editor's request (joining) | `team/storyteller/wakes/20261029T141252Z.json` |
| 14:17:44 | dev | editor | the editor's wake, in session | `team/dev/wakes/20261029T141744Z.json` |
| 14:19:43 | deck | editor | editor's request | `team/deck/wakes/20261029T141943Z.json` |
| 14:52:09 | conductor | editor | editor's request | `team/conductor/wakes/20261029T145209Z.json` |
| 14:58:10 | dev | editor | the editor's wake, in session | `team/dev/wakes/20261029T145810Z.json` |
| 15:15:04 | conductor | editor | editor's request | `team/conductor/wakes/20261029T151504Z.json` |
| 15:20:10 | conductor | editor | editor's request | `team/conductor/wakes/20261029T152010Z.json` |
| 15:22:43 | conductor | editor | editor's request | `team/conductor/wakes/20261029T152243Z.json` |
| 15:24:04 | ruv-sgit | editor | the editor's chat | `team/ruv-sgit/wakes/20261029T152404Z.json` |
| 15:24:12 | dev | editor | the editor's wake, in session | `team/dev/wakes/20261029T152412Z.json` |
| 15:27:33 | motion | editor | onboarding, editor's chat | `team/motion/wakes/20261029T152733Z.json` |
| 15:28:05 | studio | editor | onboarding, first session at the editor's word | `team/studio/wakes/20261029T152805Z.json` |
| 15:46:11 | conductor | editor | editor's request | `team/conductor/wakes/20261029T154611Z.json` |
| 16:24:58 | dev | editor | the editor's wake, in session | `team/dev/wakes/20261029T162458Z.json` |
| 16:27:08 | motion | editor | editor's request | `team/motion/wakes/20261029T162708Z.json` |
| 16:29:02 | studio | editor | editor's request: the vault keys | `team/studio/wakes/20261029T162902Z.json` |
| 16:30:25 | conductor | editor | editor's request | `team/conductor/wakes/20261029T163025Z.json` |
| 16:44:39 | conductor | editor | editor's request | `team/conductor/wakes/20261029T164439Z.json` |
| 16:57:17 | conductor | editor | editor's request | `team/conductor/wakes/20261029T165717Z.json` |
| 17:01:42 | conductor | editor | editor's request | `team/conductor/wakes/20261029T170142Z.json` |
| 17:07:21 | conductor | editor | editor's request | `team/conductor/wakes/20261029T170721Z.json` |
| 17:08:19 | deck | editor | the editor's chat, 16:50 | `team/deck/wakes/20261029T170819Z.json` |
| 17:14:44 | conductor | editor | editor's chat | `team/conductor/wakes/20261029T171444Z.json` |
| 17:21:30 | deck | editor | the editor's chat, 17:20: live technology in the slides | `team/deck/wakes/20261029T172130Z.json` |
| 17:21:52 | conductor | follow-up | follow-up wake (tonight's rule) | `team/conductor/wakes/20261029T172152Z.json` |
| 17:27:39 | conductor | editor | editor's chat | `team/conductor/wakes/20261029T172739Z.json` |
| 17:30:55 | conductor | editor | editor's chat | `team/conductor/wakes/20261029T173055Z.json` |
| 17:37:56 | conductor | editor | editor's chat | `team/conductor/wakes/20261029T173756Z.json` |
| 17:41:15 | studio | follow-up | follow-up, tonight every 15 min (the editor's word) | `team/studio/wakes/20261029T174115Z.json` |
| 17:42:15 | conductor | follow-up | follow-up wake (tonight's rule) | `team/conductor/wakes/20261029T174215Z.json` |
| 17:45:53 | conductor | editor | editor's chat | `team/conductor/wakes/20261029T174553Z.json` |
| 17:49:29 | storyteller | editor | editor's request (answers routed by the conductor; ahead of the :54 slot) | `team/storyteller/wakes/20261029T174929Z.json` |
| 17:59:11 | conductor | follow-up | follow-up wake (tonight's rule) | `team/conductor/wakes/20261029T175911Z.json` |
| 18:06:28 | studio | follow-up | follow-up, tonight every 15 min (the editor's word) | `team/studio/wakes/20261029T180628Z.json` |
| 18:14:10 | storyteller | follow-up | follow-up (tonight's rule) | `team/storyteller/wakes/20261029T181410Z.json` |
| 18:19:42 | conductor | follow-up | follow-up wake (tonight's rule) | `team/conductor/wakes/20261029T181942Z.json` |
| 18:30:37 | studio | follow-up | follow-up, tonight every 15 min (the editor's word) | `team/studio/wakes/20261029T183037Z.json` |
| 18:36:47 | conductor | follow-up | follow-up wake (tonight's rule) | `team/conductor/wakes/20261029T183647Z.json` |
| 18:38:17 | storyteller | follow-up | follow-up (tonight's rule) | `team/storyteller/wakes/20261029T183817Z.json` |

## Where this came from

The talk's history at `298be4e`, every `team/*/wakes/*.json`; `timeline/day/02.md`, `07.md`, `13.md`, `14.md`, `18.md`; the editor's RC1 review, batch 8 (after the day).
