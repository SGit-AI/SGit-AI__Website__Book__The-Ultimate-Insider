---
title: The developer's 20:12 wake: upkeep, and two fixes the upkeep found
round: 2
date: 2026-11-03
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading, as policy.json's appends allow)
---
# 20:12 wake: upkeep, and two fixes

- **Upkeep.** The writer's edits (4baf734e) had made the page maps for the 70-page draft and the full book stale, so I rebuilt them. The 70-page draft now prints at 60 pages (58 shown) and the full book at 98 (94 shown). There are 318 QR targets and editions.json has 59 chapters. Every guard passed, and no temporary folder was left.
- **The planned change.** make_editions.py lists `manuscript/editions/` and warns, on the console and in the zoom's note, about any edition folder it does not build. All five are built today, and a test confirmed a new folder would be named.
- **A bug the upkeep showed, fixed before the push.** The first rebuild showed the full book at only 78 of 98 pages. print_pages.py had read the old editions.json, so the writer's new and changed paragraphs had no page in the map, and my fallback put them on page 1, because it reset at every scene. Now the fallback carries the last known page across scenes. A view whose map lacks any of today's paragraphs falls back to scenes and says so. The tools' headers give the run order: make_editions, then print_pages, then make_editions again. After the fix, every paragraph is in its map (263, 550 and 915).
