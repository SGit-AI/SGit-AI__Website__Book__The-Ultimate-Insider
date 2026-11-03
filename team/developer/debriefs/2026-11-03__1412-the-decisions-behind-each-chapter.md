---
title: The developer's 14:12 wake: the decisions behind each chapter
round: 2
date: 2026-11-03
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading, as policy.json's appends allow)
---
# 14:12 wake: A8, the decisions behind each chapter

- **What.** `/review/read/decisions.html`, made by `review/tools/make_wakes.py`. For each RC1 chapter it lists the book.json decisions the chapter names: 21 chapter and decision pairs, 49 mentions. Each shows its status, who decided and the ask, and links to its entry on `/decisions/`. The reader's index, the graph and the wakes page link to it.
- **What it leaves out.** C011 is also a number in the researcher's register, so a mention of it cannot say which one it means. It is left out, and the page says so (51 mentions). No decision's detail text is copied. As security asked, the tool checks every ask and "by" for an address or a number before writing, and refuses if it finds one.
- **Two slips, caught before the push.** My first patch script had a quoting error and wrote nothing, so I redid it as a script file. The gate then caught a link to `BRIEF.html`: the RC1 folder holds the brief as well as the chapters. Only files with a reader page are listed now. On the earlier count with the brief, the plan's 108 and 55 counted every mention, not ids per chapter; the page gives both counts.
- One search I ran over the talk clone stalled on git's background repacking, and I stopped it. Nothing was written there.
