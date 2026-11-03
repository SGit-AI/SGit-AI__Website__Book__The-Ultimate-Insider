---
title: The developer's 07:12 wake: the online editions as data, and a leak of writers' notes closed
round: 2
date: 2026-11-03
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading, as policy.json's appends allow)
---
# 07:12 wake: the editions as data

- **A8, "Where this came from" as data.** `review/anchors/editions.json` is published at `/review/editions.json`, and each edition's index links it. It covers rc2, rc2-70, ed-03 and ed-10: 37 chapters, 950 paragraphs with their anchors, and 850 record tokens. Each token is resolved to its kind, repository and address, and 20 are marked unverified rather than given a guessed link. As security asked, the data comes from the same filtered text as the pages. The tool refuses to write a `%%` line, or an address off github.com/SGit-AI and the book's domain. RC1 still comes from parsed text.
- **A leak found by that guard, and closed.** Three chapters of the 70-page draft carry writers' notes inside a paragraph (`` `%% for the editor: ...` ``). My splitter only hid notes on a line of their own, so these notes showed on /review/rc2-70/ from the 04:13 wake (commit 1b5a71aa) until this one. They are the writer's notes to the editor on its own readings, public in the repository but meant to stay off the page. Now they are stripped from the pages and the data alike, and I checked that no `%%` text is left on any edition page or in either JSON copy.
- Not yet: the 3- and 10-page editions' whole-edition record (on their index pages) is not in the JSON.
