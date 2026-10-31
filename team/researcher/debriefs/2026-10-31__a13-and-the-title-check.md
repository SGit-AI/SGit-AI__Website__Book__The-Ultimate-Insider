---
title: A13 registered (wakes by trigger, commits outside wakes), the exact-title check, and a first catalogue of the editor's articles
round: 1
date: 2026-10-31
commits: this wake's commit on dev
site_version: the release after this push
outside_scope: none; REALITY.md appended under my own heading
---

researcher@book.the-ultimate-insider, 31 October 2026, the 04:32 wake.

## What shipped

- **A13, with the historian.**
  - C087: the 162 wakes by trigger, 105 scheduled, 47 started by the editor, 10 follow-ups, by hour. It agrees with the historian's table to the wake.
  - C088: of the 439 agent commits, 46 were made with no wake of their member open, 36 of them before 03:00. Eleven sit inside wakes opened and never closed, among them the editor's player fixes from 17:54 to 18:37, in dev's 17:48 wake. That corrects the timeline's reading of those fixes as wake-less.
- **The exact-title check for N7 and N8.**
  - Neither is a book title (Open Library, a search engine's index of Amazon).
  - N7's words sit in four 2026 Amazon subtitles.
  - Amazon's own search, Google Books and Nielsen were not reachable from here, and the letter says so.
- **A4, begun.** `claims/articles-catalogue.json` and `.md`, 41 newsroom articles: the newsroom's curated collections, RC1's titles, and 11b's dossier set.
- Letters: historian `researcher__001`, storyteller `researcher__002`, conductor `researcher__010`, ruv-sgit `researcher__004`.

## The scripts

C088, run in a full clone of the talk's repository; it needs the wake windows first.

```
for f in $(git ls-tree -r --name-only 298be4e team | grep -E '^team/[^/]+/wakes/[^/]+\.json$'); do git show 298be4e:$f | python3 -c "import json,sys;d=json.load(sys.stdin);print('$f'.split('/')[1]+'\t'+d['started']+'\t'+(d.get('closed') or ''))"; done > spans.tsv
git log 298be4e --no-merges --author=Claude --format='%H%x09%cI%x09%s%x09%b%x1e' | tr '\n' ' ' | tr '\036' '\n' > commits.tsv
```

Then for each commit: its member by the subject's `<id>:` or `@<id>:` prefix, else the body's `Agent: <id>@the-ultimate-insider`, else "Conductor joins" for the conductor. A commit counts as in a closed wake when its time falls between that member's started and closed, two minutes either side. It counts as in a wake left open when it falls after a wake that has no closed time; otherwise no wake was open.

## What was hard

The historian's note that the player fixes "are commits, not wakes" looked right until the windows were drawn: dev opened a wake at 17:48:50 and never closed it. An unclosed wake is its own finding. The record shows the editor arriving in a session and the wake's paperwork never finishing.

## Next

A4's placement and graph; A7; T12; A9; E04.

## Where this came from

`comms/mail/mailroom/researcher/historian__010`, `storyteller__014`, `conductor__020` to `__023`, `ruv-sgit__005`; `timeline/triggers.md`; the talk's repository at `298be4e`; openlibrary.org and the web search, read 31 October 2026; https://newsroom.sgit.ai/newsroom/wire.json.
