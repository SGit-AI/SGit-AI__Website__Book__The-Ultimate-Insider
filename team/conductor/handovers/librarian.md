# Handover for the librarian, to the account that continues the book

Written by conductor@book.the-ultimate-insider on 30 October 2026, at about 11:45 UTC, at the editor's word: the first account was nearly out of usage and another account continues. The conductor writes this because it holds `team/conductor/`; the librarian's own folder is the librarian's alone. The new librarian session reads this, then adopts what is right into its own `status.json` and debrief, and says so. Nothing here speaks for the editor or for the librarian.

## Who you were

- Role: `librarian@book.the-ultimate-insider`, folder `team/librarian/` (`ROLE.md` with its Done when, `policy.json`, `status.json`, `debriefs/`).
- First account's session: `session_01Kw9UwBgUFHEgwLsB3TrwA8`, key `sha256:e5768293c14e8cdc`. That key stays in the record; a new session makes and publishes its own (`admin/tools/pki-agent.README.md`) and never copies a private half across.
- First account's scheduled task: `trig_01MGyWHBgZ7Pzg95f2ozEAi5`, hourly at :09 London, paused (not deleted) at the editor's word at about 10:50 UTC, when usage reached 94%.

## Start here

1. Read `CLAUDE.md`, `team/conductor/WAKE.md`, `team/librarian/ROLE.md`, `policy.json`, `status.json`, your newest debrief, your board (`comms/issues/librarian/issues/`) and your mail (`comms/mail/mailroom/librarian/`), then the conductor's handover, `team/conductor/debriefs/2026-10-30__handover-to-the-next-account.md`.
2. Run `python3 admin/tools/start.py librarian --kind "takeover from the first account" --objective "<your first item below>" --model <model>`; it pulls dev.
3. Make and publish your session key.
4. Create your hourly task at :09 London only when the editor says the team restarts (the conductor relays it); until then work in your session when he opens it.
5. Every wake runs the five steps (`python3 admin/tools/wake.py`), and closes with the gate, a debrief and the end banner.

## Where you stand

The index of the talk's repository at `298be4e` is on dev (`index/`), the Cold-Read team's work is indexed read only (`index/cold-read/`), and `index/tools/check_sources.py` is ready to check chapters' sources. Its status was last written at about 10:11 UTC, before RC1's revision landed. C10b gave it comms paths; its policy should show them.

## First things to do

1. Run `index/tools/check_sources.py` on every chapter in `team/conductor/rc1/`, including the three new ones (`00b-how-to-read-a-map.md`, `11b-what-was-already-there.md`, `13-concepts-and-principles.md`), and send the findings to the conductor with file and line.
2. Add the index entries each chapter draws on (Done when 3), against the plan as signed and RC1 as it now stands.
3. Index the talk's commits after `298be4e` (the transcript and debrief at `a9c0b49` and anything later) apart, marked as added after the day (Done when 2).
4. Adopt, change or withdraw the 12 cards drafted as the librarian in `team/conductor/rc1/annotations/librarian.json`.

## Notes from this morning

- The drafted cards raise: the Cold-Read pin (`0dc6854` in the index is not in a fresh clone of that repository; the conductor's clone stood at `9e6a7a1` at 09:54), the licence of the talk's images in a CC BY 4.0 book (the talk repository is Apache-2.0 and some images carry third-party credits), whether the room and the host in chapter 10 knew the recording might be published, and chapter sources. The corrections pass fixed the stale decisions (U1, C10b) and named the editor's brief as the one file that crossed to the blind repository.
- The research dossier, `team/conductor/rc1/research/the-two-and-a-half-years.md`, cites public sources by date; index them as sources the book now uses.

## Mail addressed to you

`conductor__001-comms-in-git.eml`, `conductor__002-c10-signed.eml`, `conductor__003-review-and-rc1.eml`, `conductor__004-the-editors-voice.eml`. The newest from the conductor are the review-and-RC1 request, the editor's voice guidance (read his newsroom.sgit.ai articles: first person, honest about where he stands, the memo's order, plain words, public sources named and dated, private people never named, no em-dashes, British spelling, no superlative self-claims, never naming the model), and anything numbered after them.

## The companion

The editor is reading RC1 (294 pages) and the companion (98 cards, 12 drafted as you) on paper. His ticks become open decisions in `book.json` through the conductor; act on none until he signs it.

## Where this came from

`team/librarian/status.json`, `ROLE.md` and `key.json`; `comms/issues/librarian/` and `comms/mail/mailroom/librarian/`; `team/conductor/rc1/annotations/librarian.json`; `team/conductor/schedule.json`; the conductor's wake of 30 October, `team/conductor/wakes/20261030T103103Z.json`.
