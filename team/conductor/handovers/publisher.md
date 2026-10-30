# Handover for the publisher, to the account that continues the book

Written by conductor@book.the-ultimate-insider on 30 October 2026, at about 11:45 UTC, at the editor's word: the first account was nearly out of usage and another account continues. The conductor writes this because it holds `team/conductor/`; the publisher's own folder is the publisher's alone. The new publisher session reads this, then adopts what is right into its own `status.json` and debrief, and says so. Nothing here speaks for the editor or for the publisher.

## Who you were

- Role: `publisher@book.the-ultimate-insider`, folder `team/publisher/` (`ROLE.md` with its Done when, `policy.json`, `status.json`, `debriefs/`).
- First account's session: `session_01Kw9UwDVeRbKJZUWiRoRrHK`, key `sha256:88b9a9682c1b72e9`. That key stays in the record; a new session makes and publishes its own (`admin/tools/pki-agent.README.md`) and never copies a private half across.
- First account's scheduled task: `trig_01D2wnhQDySKsG8ZL9XLmNsW`, hourly at :47 London, paused (not deleted) at the editor's word at about 10:50 UTC, when usage reached 94%.

## Start here

1. Read `CLAUDE.md`, `team/conductor/WAKE.md`, `team/publisher/ROLE.md`, `policy.json`, `status.json`, your newest debrief, your board (`comms/issues/publisher/issues/`) and your mail (`comms/mail/mailroom/publisher/`), then the conductor's handover, `team/conductor/debriefs/2026-10-30__handover-to-the-next-account.md`.
2. Run `python3 admin/tools/start.py publisher --kind "takeover from the first account" --objective "<your first item below>" --model <model>`; it pulls dev.
3. Make and publish your session key.
4. Create your hourly task at :47 London only when the editor says the team restarts (the conductor relays it); until then work in your session when he opens it.
5. Every wake runs the five steps (`python3 admin/tools/wake.py`), and closes with the gate, a debrief and the end banner.

## Where you stand

RC1 of this morning (16 files, 217 pages) was moved into `manuscript/` on the publisher's branch `claude/publisher-onboarding-setup-jyrfy9`, not released to dev, waiting on the conductor's fix to `admin/build/build.py` (copy the chapters' images; letter `publisher__002`). The image build changes, L1, L2 and M1 are in `publishing/` on dev. Board: 002 Leanpub book and price, 003 RC1 review, 004 Markua, 005 RC1 release, open. The session was mid-turn when the schedule was paused; check the branch before assuming anything.

## First things to do

1. Take the current RC1, not this morning's: `team/conductor/rc1/` now has 19 files (00b, 11b, 13 added; a corrections pass over every chapter), 16 maps in `resources/images/maps/`, infographics in `infographics/jpg/` placed by `infographics/manifest.json`, maps 6 to 16 by `maps/placements.json`, 50 call-outs in `infographics/callouts.json`, and the cover `cover/cover-1.jpg`. The conductor placed images and call-outs at build time (`team/conductor/rc1/tools/assemble_rc1.py`); in `manuscript/` they should become real image lines and Markua asides.
2. Release RC1 to dev once the conductor's build.py fix is on dev (the new conductor's first task).
3. The Markua pre-pandoc step in `publishing/build_book.py` (asides A>, W>, T>, `{width}`, page breaks, front and back matter), so the call-outs survive both builds; the call-out look is in `assemble_rc1.py`'s `CALLOUT_CSS` and `infographics/README.md`.
4. Adopt, change or withdraw the 14 cards drafted as the publisher in `team/conductor/rc1/annotations/publisher.json`.

## Notes from this morning

- Unchecked outside facts in the drafted cards: KDP's price-parity terms (publisher-09; cite the page before submission), Markua's treatment of bracket text as caption (publisher-14) and crosslink syntax (publisher-03), against the Markua 0.30 spec.
- The illustrated build is about 16 MB; check Leanpub's and KDP's limits and image sizes before the first upload. The build metadata still prints the internal working name; the title waits on the editor.
- Leanpub builds from main (L2): a preview waits on the editor merging dev into main.

## Mail addressed to you

`conductor__001-comms-in-git.eml`, `conductor__002-review-and-rc1.eml`, `conductor__003-the-editors-voice.eml`, `conductor__004-markua.eml`, `conductor__005-rc1-ready.eml`. The newest from the conductor are the review-and-RC1 request, the editor's voice guidance (read his newsroom.sgit.ai articles: first person, honest about where he stands, the memo's order, plain words, public sources named and dated, private people never named, no em-dashes, British spelling, no superlative self-claims, never naming the model), and anything numbered after them.

## The companion

The editor is reading RC1 (294 pages) and the companion (98 cards, 14 drafted as you) on paper. His ticks become open decisions in `book.json` through the conductor; act on none until he signs it.

## Where this came from

`team/publisher/status.json`, `ROLE.md` and `key.json`; `comms/issues/publisher/` and `comms/mail/mailroom/publisher/`; `team/conductor/rc1/annotations/publisher.json`; `team/conductor/schedule.json`; the conductor's wake of 30 October, `team/conductor/wakes/20261030T103103Z.json`.
