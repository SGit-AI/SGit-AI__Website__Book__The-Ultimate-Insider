# Handover for the researcher, to the account that continues the book

Written by conductor@book.the-ultimate-insider on 30 October 2026, at about 11:45 UTC, at the editor's word: the first account was nearly out of usage and another account continues. The conductor writes this because it holds `team/conductor/`; the researcher's own folder is the researcher's alone. The new researcher session reads this, then adopts what is right into its own `status.json` and debrief, and says so. Nothing here speaks for the editor or for the researcher.

## Who you were

- Role: `researcher@book.the-ultimate-insider`, folder `team/researcher/` (`ROLE.md` with its Done when, `policy.json`, `status.json`, `debriefs/`).
- First account's session: `session_01Kw9UwBta1dcP9qBJUURLPZ`, key `sha256:4e0287f6640d61f0`. That key stays in the record; a new session makes and publishes its own (`admin/tools/pki-agent.README.md`) and never copies a private half across.
- First account's scheduled task: `trig_0187JjB8uJUHxvgeCoAGXoKj`, hourly at :32 London, paused (not deleted) at the editor's word at about 10:50 UTC, when usage reached 94%.

## Start here

1. Read `CLAUDE.md`, `team/conductor/WAKE.md`, `team/researcher/ROLE.md`, `policy.json`, `status.json`, your newest debrief, your board (`comms/issues/researcher/issues/`) and your mail (`comms/mail/mailroom/researcher/`), then the conductor's handover, `team/conductor/debriefs/2026-10-30__handover-to-the-next-account.md`.
2. Run `python3 admin/tools/start.py researcher --kind "takeover from the first account" --objective "<your first item below>" --model <model>`; it pulls dev.
3. Make and publish your session key.
4. Create your hourly task at :32 London only when the editor says the team restarts (the conductor relays it); until then work in your session when he opens it.
5. Every wake runs the five steps (`python3 admin/tools/wake.py`), and closes with the gate, a debrief and the end banner.

## Where you stand

`claims/register.json` holds C001 to C042 (35 checked, 5 corrected, 2 open at its last status). The RC1 numbers review was sent to the conductor. Board: 001 RC1 review, open.

## First things to do

1. Answer the conductor's letter 006 (`comms/mail/mailroom/researcher/conductor__006-numbers-to-register-rc1.eml`): register or reject each number RC1 now uses that the register does not hold, chiefly the dossier's dates in chapter 11b (tagged "(dossier: ...)"), the Cold-Read counts in chapters 9 and 11, derived figures, and what the infographics maker could not find (`team/conductor/rc1/infographics/README.md`).
2. Correct the register where the drafted cards found it wrong: C014 (the `Agent: dev` trailers; merges 165 by parents, 164 by the agents), C011 (dev and ruv-sgit dated by join commits as well as first keys), C040 (a 13:50 time exists in the dictated brief). The corrections pass already changed the chapters to match; the register must follow.
3. Add a claim for the evidence vault's history (`aa7a3eb`), at the level the book uses it: that values reached a pushed history, never the values or where they are.
4. Adopt, change or withdraw the 12 cards drafted as the researcher in `team/conductor/rc1/annotations/researcher.json`.

## Notes from this morning

- The dossier (`team/conductor/rc1/research/the-two-and-a-half-years.md`) found no public source for the date the editor went full time or for SHarness against sgit speed; these stay questions for the editor, never numbers.
- Use a full clone of the talk repository; a shallow clone gave wrong counts on the first account.

## Mail addressed to you

`conductor__001-comms-in-git.eml`, `conductor__002-graphs-sgit-ai.eml`, `conductor__003-c10-signed.eml`, `conductor__004-review-and-rc1.eml`, `conductor__005-the-editors-voice.eml`, `conductor__006-numbers-to-register-rc1.eml`, `storyteller__001-appendix-commands.eml`. The newest from the conductor are the review-and-RC1 request, the editor's voice guidance (read his newsroom.sgit.ai articles: first person, honest about where he stands, the memo's order, plain words, public sources named and dated, private people never named, no em-dashes, British spelling, no superlative self-claims, never naming the model), and anything numbered after them.

## The companion

The editor is reading RC1 (294 pages) and the companion (98 cards, 12 drafted as you) on paper. His ticks become open decisions in `book.json` through the conductor; act on none until he signs it.

## Where this came from

`team/researcher/status.json`, `ROLE.md` and `key.json`; `comms/issues/researcher/` and `comms/mail/mailroom/researcher/`; `team/conductor/rc1/annotations/researcher.json`; `team/conductor/schedule.json`; the conductor's wake of 30 October, `team/conductor/wakes/20261030T103103Z.json`.
