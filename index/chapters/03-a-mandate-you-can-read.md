# The index entries `03-a-mandate-you-can-read.md` draws on

From the chapter's `## Where this came from` in `manuscript/03-a-mandate-you-can-read.md`, resolved by `index/tools/chapter_entries.py`. Each row is the index's own entry for the file: kind, owner, when it was added and last changed, and what it is.

## talk at 298be4e (13)

| Path | Kind | Owner | Added | Last changed | What it is |
|---|---|---|---|---|---|
| `admin/build/agents.py` | site build | dev | `f00101e` 2026-10-29 00:54:32 | `24da366` 2026-10-29 01:19:26 | builds the team pages from team/<id>/ and checks each member's writes against its policy (agents.py check) |
| `admin/build/validate.py` | site build | dev | `1f7c633` 2026-10-29 00:40:50 | `28fe01d` 2026-10-29 16:36:27 | The gate. Fails the build (exit 1) on any finding; CI runs it before every release and on the built tree. |
| `admin/tools/pki-agent.README.md` | tool | conductor | `17b287b` 2026-10-29 00:51:12 | `b859ff0` 2026-10-29 23:19:09 | where the pinned key tool came from, its hash, and how an agent makes its session key |
| `admin/tools/pki-agent.mjs.sha256` | tool | conductor | `17b287b` 2026-10-29 00:51:12 | `b859ff0` 2026-10-29 23:19:09 | the pinned key tool's sha256 |
| `team/conductor/WAKE.md` | document | conductor | `ecc048e` 2026-10-29 01:35:33 | `3342cff` 2026-10-29 16:59:22 | the wake protocol every member followed: the five steps, the checklist, when and how to stop; ported to the book unchanged in substance |
| `team/conductor/debriefs/2026-10-29__banners-and-keys.md` | debrief | conductor | `b3ee324` 2026-10-29 00:59:19 | `b3ee324` 2026-10-29 00:59:19 | Every member opens and closes its session with a banner, and the conductor's key is published in dev's team shape |
| `team/conductor/wakes/20261029T021416Z.json` | wake record | conductor | `8c66751` 2026-10-29 02:16:00 | `c8f6f8f` 2026-10-29 02:19:36 | editor's request: build the five-step wake; outcome partial; work partial: Commit 5700bab: five-step section in WAKE.md, briefs in team/conductor/reviews/, wake.py check (negative control failed a re… |
| `team/conductor/wakes/20261029T140334Z.json` | wake record | conductor | `c9ced4e` 2026-10-29 14:07:04 | `816baa0` 2026-10-29 14:08:05 | editor's request; outcome ok; work done: 1) Requests in mailroom/dev, deck, ruv-sgit, researcher (vault_check clean, pushed): dev the feedback pane and lane with voice now with the key conditions, th… |
| `team/conductor/wakes/20261029T140915Z.json` | wake record | conductor | `4cc4352` 2026-10-29 14:15:59 | `4cc4352` 2026-10-29 14:15:59 | editor's request; outcome ok; work done: 79a7fcb: policy.json gains exactly content/articles/how-this-talk-was-built.md; |
| `team/conductor/briefs/2026-10-29__editor/8-our-own-abps-1730.md` | brief sent | conductor | `7c91afc` 2026-10-29 17:33:07 | `7c91afc` 2026-10-29 17:33:07 | Our own Agent Behaviour Policies, on stage (29 October 2026, 17:30 London) |
| `team/ruv-sgit/debriefs/img/2026-10-29__policy-review__5-review-desktop.png` | debrief image | ruv-sgit | `0dc0e6a` 2026-10-29 02:10:24 | `0dc0e6a` 2026-10-29 02:10:24 | image |
| `team/studio/debriefs/img/2026-10-29__abp-prose-enforcement__1-prose-reach.png` | debrief image | studio | `95b09d9` 2026-10-29 18:11:59 | `95b09d9` 2026-10-29 18:11:59 | image |
| `team/studio/debriefs/img/2026-10-29__abp-prose-enforcement__3-enforcement-end.png` | debrief image | studio | `95b09d9` 2026-10-29 18:11:59 | `95b09d9` 2026-10-29 18:11:59 | image |

## this repository (9)

- `claims/register.json`
- `controls/README.md`
- `controls/index.json`
- `timeline/day/00.md`
- `timeline/day/01.md`
- `index/areas/team-conductor.md`
- `index/areas/tools.md`
- `index/areas/team-studio.md`
- `team/security/reviews/pki-agent-review.md`

## talk, added after the day (3)

- `team/conductor/debriefs/img/talk-abp.jpg`
- `team/conductor/debriefs/img/talk-s-e09.jpg`
- `team/conductor/debriefs/img/talk-s-e10.jpg`

## Commits named (21)

`298be4e`, `01e9ed3`, `56cbe55`, `f00101e`, `17b287b`, `41d38ba`, `20ab1a3`, `0dc0e6a`, `adb3e2e`, `01e2753`, `a082c52`, `95d1f66`, `df2fa22`, `4adc04a`, `7c91afc`, `bd3cdad`, `95b09d9`, `79a7fcb`, `10ba28c`, `c33e86a`, `a9c0b49`

## Not in any index

Paths the tool could not place (outside the three repositories, or a web address): `talk.json`, `2026-10-29__abp-review.md`, `2026-10-29__abp-prose-enforcement.md`
