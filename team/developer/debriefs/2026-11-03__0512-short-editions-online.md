---
title: The developer's 05:12 wake: the 3- and 10-page editions online, with their record
round: 2
date: 2026-11-03
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading, as policy.json's appends allow)
---
# 05:12 wake: every edition online with its record

- **Board 010 done.** `/review/ed-03/` (4 chapters, 23 links) and `/review/ed-10/` (10 chapters, 53 links) hold the publisher's text. At each page's foot is the record the storyteller wrote under that page of its script, matched by title. The script's "Where this came from" record goes on each index. The zoom now links every rung online.
- **Security's conditions met.** For the web, pandoc fences come out, a marker image becomes "On stage:" and a figure keeps its alt text. A raw-HTML line or a link left in the text stops the build, rather than going through build.py's Markdown unescaped. A page with no title match also stops the build. The one exception, the 3-page edition's series page, which its script gives no section, is named in the tool and says so on the page. Record links point to the public repositories, with the talk's at 298be4e.
- The 70-page draft grew to 12 chapters (69 scenes, 436 links) and was rebuilt with the rest.
- synthetic__009 is filed. Its run puts the tablet column at about 79 characters a line, so the fix holds.
