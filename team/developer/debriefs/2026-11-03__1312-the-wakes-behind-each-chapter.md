---
title: The developer's 13:12 wake: the wakes behind each chapter
round: 2
date: 2026-11-03
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading, as policy.json's appends allow)
---
# 13:12 wake: A8, the wakes behind each chapter

- **What.** `/review/read/wakes.html`, made by the new `review/tools/make_wakes.py`. For each RC1 chapter it lists the talk team's hourly wakes that made the commits the chapter cites. Each wake shows the member, the start time, the five step verdicts and a link to the wake file at 298be4e. The reader's index and the graph link to it.
- **How, and what it leaves out.** A commit's member comes from its "@member:" subject or its Agent: trailer, the same way the graph reads it. Its wake is that member's wake record whose start-to-close window holds the commit's time. That traces 72 of the 115 cited commits. The other 43 are counted on the page, not guessed: 27 fall outside any wake of their member, and 16 name no member. As security asked, no comment text is copied from the wake files: only member, time, verdict words and links. The decisions behind a page come in a later wake.
- **Started three minutes late:** the wake fired at 13:15 for 13:12 and started at 13:17. All four steps ran as the reviewer agent and saw only Read, Grep, Glob and Bash.
