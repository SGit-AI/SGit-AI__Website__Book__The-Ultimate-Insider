# The index entries `11b-what-was-already-there.md` draws on

From the chapter's `## Where this came from` in `manuscript/11b-what-was-already-there.md`, resolved by `index/tools/chapter_entries.py`. Each row is the index's own entry for the file: kind, owner, when it was added and last changed, and what it is.

## talk at 298be4e (11)

| Path | Kind | Owner | Added | Last changed | What it is |
|---|---|---|---|---|---|
| `.github/workflows/release.yml` | ci | dev | `1f7c633` 2026-10-29 00:40:50 | `1f7c633` 2026-10-29 00:40:50 | CI: gates, numbers (dev bumps the last number, main the middle), tags, builds and deploys every release |
| `content/articles/introducing-this-site.md` | article | dev | `1f7c633` 2026-10-29 00:40:50 | `5a91607` 2026-10-29 16:06:50 | the first article: a site for one talk, built the way the talk says to build things |
| `admin/build/build.py` | site build | dev | `1f7c633` 2026-10-29 00:40:50 | `23739cc` 2026-10-29 18:04:48 | Builds the site into _site/ from src/ and content/. Standard library only, so CI needs nothing installed. |
| `admin/build/validate.py` | site build | dev | `1f7c633` 2026-10-29 00:40:50 | `28fe01d` 2026-10-29 16:36:27 | The gate. Fails the build (exit 1) on any finding; CI runs it before every release and on the built tree. |
| `admin/build/agents.py` | site build | dev | `f00101e` 2026-10-29 00:54:32 | `24da366` 2026-10-29 01:19:26 | builds the team pages from team/<id>/ and checks each member's writes against its policy (agents.py check) |
| `admin/tools/start.py` | tool | conductor | `02cbd86` 2026-10-29 01:27:10 | `5700bab` 2026-10-29 02:18:10 | The first command of every session, scheduled or started from the editor's chat: get in sync, then say so. |
| `admin/tools/wake.py` | tool | conductor | `8c66751` 2026-10-29 02:16:00 | `5700bab` 2026-10-29 02:18:10 | The five-step wake, recorded: every wake leaves one record, team/<you>/wakes/<started>.json, with five steps. |
| `admin/tools/pki-agent.mjs` | tool | conductor | `17b287b` 2026-10-29 00:51:12 | `b859ff0` 2026-10-29 23:19:09 | the editor's key tool from pki.sgit.ai, pinned unmodified (one file, Node 18+); not read line by line on the day |
| `admin/notes/2026-10-29__first-agents-and-schedule.md` | admin note | Claude | `97b98d9` 2026-10-29 00:44:37 | `97b98d9` 2026-10-29 00:44:37 | the conductor's first proposal of agents and schedule, corrected the same day after it read BRIEF.md; the original left below |
| `team/conductor/WAKE.md` | document | conductor | `ecc048e` 2026-10-29 01:35:33 | `3342cff` 2026-10-29 16:59:22 | the wake protocol every member followed: the five steps, the checklist, when and how to stop; ported to the book unchanged in substance |
| `team/conductor/HOLD.md` | hold | conductor | `867f8c2` 2026-10-29 18:44:13 | `867f8c2` 2026-10-29 18:44:13 | the hold of 18:44 UTC, at the editor's word (his usage limit at 95%): every member's wake stops; still in place at the pin, never lifted in the record |

## this repository (5)

- `team/conductor/rc1/research/the-two-and-a-half-years.md`
- `briefs/2026-10-30__in-session/01-principles-maps-and-the-plumbing.md`
- `team/conductor/rc1/reviews/gen-zx-team.md`
- `team/conductor/rc1/maps/06-the-plumbing-under-the-day.json`
- `team/conductor/rc1/maps/07-one-piece-leads-to-the-next.json`

## Commits named (17)

`885128d`, `e53d055`, `753ef2c`, `0df0830`, `4edb92e`, `d52dc70`, `be1aaba`, `9c8503d`, `de32536`, `34d99ce`, `21e1f27`, `1b01902`, `ae9f85e`, `02c6dbb`, `298be4e`, `867f8c2`, `1f7c633`
