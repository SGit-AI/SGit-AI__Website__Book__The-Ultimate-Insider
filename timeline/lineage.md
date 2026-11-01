# The factory's lineage: what the day was built on, and what it handed on

Kept by historian@book.the-ultimate-insider. Written 1 November 2026, about 16:40 UTC, at the conductor's letter 022 (PS1: the book is about how a creator was given a factory of agents "built on earlier experiments and flows", and the talk a side effect). This file shows, from the record, one project's work used in the next. The talk's history is read at `298be4e`; the public work before the day is chapter 11b's and the researcher's register's, not repeated here.

## What the day reused, in the order it arrived

| Time (UTC, 29 Oct) | What was reused | From | The record |
|---|---|---|---|
| 00:40:50 | **The site's way of working**: "the brief published in full, reality and corrections files, one build script, a gate, a .md twin for every page and llms.txt" | the sgit.ai sites ("built the sgit.ai way") | `1f7c633` |
| 00:44:37 | **The repository's rules** (`CLAUDE.md`), "modelled on web-summit.sgit.ai" | the Web Summit site's team | `97b98d9` |
| 00:51:12 | **The key tool**, `admin/tools/pki-agent.mjs`: "an unmodified copy of https://pki.sgit.ai/agents/pki-agent.mjs (the editor's own tool)", its hash matching the PHP newsroom's pinned copy | pki.sgit.ai; the PHP newsroom | `17b287b`; `admin/tools/pki-agent.README.md` at `298be4e` |
| 00:53:45 | **The session banners**: "Adopts the PHP newsroom's wake banners (its brief of 27 October 2026)" | the PHP newsroom | `a3a4807` |
| 01:08:25 | **The vaults**: ruv-sgit joins as "the runner against dev.send.sgraph.ai", making its work in encrypted vaults | SGit and the send service | `defe526` |
| 01:09:58 | **The team's board and mail**, Issues-FS lite and Email-FS lite, two public vaults "in web-summit.sgit.ai's pattern" | the Web Summit site's team; Issues-FS, Email-FS | `31b0f86` |
| 15:07:08 | **The talk player**, "ported from ruv.sgit.ai", its notice kept | ruv.sgit.ai | `3314ffe` |
| 15:40 | **The studio's first pieces**, rebuilt from ruv.sgit.ai with the source commit and data pinned unmodified | ruv.sgit.ai | `c3ce566` |
| 14:19 onward | **Wardley maps** as the storyteller's frame | the editor's practice (chapter 00b, chapter 11b) | `df37797` |

What the day **invented** rather than reused is as telling: the hourly schedule (`09f13d5`, 01:39), the hold (`team/conductor/WAKE.md`, Stopping), the five-step wake (`8c66751`, `5700bab`, 02:16 to 02:18), the locks (`4a2481b`, 17:54) and the follow-up wakes of the evening (`3342cff`). The plumbing came from earlier projects; the controls were made that night, and the controls are what failed and held.

## What the day handed on: this book's team

The book's own team, from 30 October, was built from the talk's in the same way, and says so in its own files:

| What was handed on | The record, in this repository |
|---|---|
| **The rules, ported "rule for rule"** from the talk's `CLAUDE.md` at `298be4e` | `CLAUDE.md`, first paragraph |
| **The wake protocol**, "ported unchanged in substance" from the talk's `WAKE.md` at `298be4e`, the five steps included | `team/conductor/WAKE.md`, first paragraph |
| **The key tool**, "copied unchanged from the talk's repository", its hash still matching | `admin/tools/pki-agent.README.md` |
| **The vault tools**, kept for the day a vault is needed | `CLAUDE.md` ("No vaults for now"); `admin/tools/vault_handover.py` |
| **The book's roles and rules** (editor, reviewer, publisher, librarian; "every chapter ends with where it came from"; synthetic readers; the paper review) | the Gen ZX Founders book, gen-z-developers.sgit.ai (`briefs/2026-10-30/3-source-map.md`) |
| **The talk team's own record**, read as the book's source, never written | `CLAUDE.md`, "The talk's repository is read-only" |

And the factory improved between the two: the book's team added sessions handed over between accounts with new keys and a sessions register (`team/conductor/sessions-register.json`; the editor on 31 October: the constraint "is actually forcing me to do better engineering", C089), and slower cadences when idle (Q6). One project's controls became the next project's starting point.

## For the book

The chain the editor names in PS1 is on the record at both ends: the talk's team started from the sgit.ai sites, the Web Summit team's pattern, the PHP newsroom's banners and pinned key tool, SGit's vaults and ruv.sgit.ai's player; the book's team started from the talk's rules, protocol and tools, and from the Gen ZX book's roles. What each team made new was its controls.

## Where this came from

The talk's history at `298be4e` (the commits above); this repository's `CLAUDE.md`, `team/conductor/WAKE.md`, `admin/tools/pki-agent.README.md`, `briefs/2026-10-30/3-source-map.md`; the register (C089); the conductor's letter 022.
