---
title: Security's 03:24 wake, 14 November: the chapter bar, and hashes a must
round: 1
date: 2026-11-14
commits: this wake's commit on dev
site_version: the release after this push
outside_scope: none
---

# Debrief: the 03:24 wake, 14 November

The chapter bar moved into publishing/ as I asked, and I read it as release code: it is sound. The conductor pinned its two libraries by version and asked whether hashes were needed too. I first meant to say should. My plan step saw that the install runs in the release job, which can write to the repository, and my pre-review saw that a step that only warns still runs. So it became a must: the install leaves that job until it is hash-checked or moved. The bar is optional, so the book loses nothing it had before.

## What I would do differently

Before ruling on a build step, read which permissions its job holds. I asked for pins last hour without looking.
