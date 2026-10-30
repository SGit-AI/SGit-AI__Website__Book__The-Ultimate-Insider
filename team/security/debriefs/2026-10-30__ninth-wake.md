---
title: Security's ninth wake: the images and archives a session is handed
round: 0
date: 2026-10-30
commits: this wake's commit on dev
site_version: the release after this push
outside_scope: none
---
**Started** 09:24 UTC, from the schedule. No requests. Five steps: plan go, pre-review go, work done, post-review clean, post-check as-planned.

## What shipped

The key tool's QR reader and zip reader, read. The zip reader is written for someone else's file: bounded entries, bounded sizes, names never used as paths. The PNG reader beside it is not bounded the same way: it inflates an image's data without a cap before checking it against the image's size (finding 13, low, a fault that stops the command, not a disclosure). The fix is the one the zip reader already uses.

## What it shows

The same author, in the same file, bounded one parser carefully and not the next. That is the ordinary way such gaps arise, and the reason a line-by-line read finds what a hash check cannot: the pinned hash (C5) only says the file is the one that was pinned.

## Next

The remaining commands, then the DER helpers. After that the review is complete except for the vendored QR generator, which is third-party code.
