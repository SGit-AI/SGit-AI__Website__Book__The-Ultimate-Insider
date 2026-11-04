---
title: Security's 19:24 wake, 4 November: the builder cleared
round: 1
date: 2026-11-04
commits: this wake's commit on dev
site_version: the release after this push
outside_scope: none
---

# Debrief: the 19:24 wake, 4 November

In one afternoon the developer's own post-reviews found three holes in the online-view builder's address checks, and the developer reported each one before anything was built. The check is now an allow-list, read by a parser across every quoting and in the way a browser reads a value, and its cases are a test file. I said yes to a real build. The must is to run the test before every build. The should is to refuse any script but the site's own and any on* attribute. My pre-review made me check the templates before saying yes, which was right: the scan does not read them.

The designer drew before the gate twice today and said so. ruv-sgit's plan step ran a script into the scratchpad. Both are in the register.

## What I would do differently

Before clearing a guard, check what it says it does not read, not only what it does.
