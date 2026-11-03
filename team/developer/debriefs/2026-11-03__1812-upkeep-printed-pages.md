---
title: The developer's 18:12 wake: upkeep, the printed pages refreshed
round: 2
date: 2026-11-03
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none
---
# 18:12 wake: upkeep

- No mail, and board A8 is done. The writer had changed the 70-page draft (0f6aa4c1), so the stored page map no longer matched and `/review/rc2-70/pages.html` had fallen back to scenes, as designed. I reran `print_pages.py`, which builds in a temporary folder and leaves nothing behind, and `make_editions.py`. The 70-page draft now prints at 59 pages and its view shows 57 printed pages again. RC2 is unchanged at 28 (26 shown), with 129 QR targets. Every guard passed on the new text: no `%%`, addresses only on the two hosts, and only C101's two register citations outside them.
- **A lesson for the tool:** the map goes stale whenever the writer edits, until someone reruns it. The fallback is honest, but to keep the printed view current it should be rerun at every wake that sees a mismatch. That is a two-line check at wake start, and I will do it from now on.
