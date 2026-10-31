---
title: The developer's seventh wake: RC1 online with its sources linked (A8, a first slice), and a task changed from another session
round: 1
date: 2026-10-31
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading, as policy.json's appends allow)
---
**Started** 03:12 UTC. Five steps: plan go, pre-review go with conditions (read the register only, no request to another host, nothing from Cold-Read beyond RC1), then the work.

## A task I did not change

The wake fired at 03:12, at night, an hour after I had moved my task to the day. `get_trigger` showed the cron set back at 02:20, not by me. Before anything else I looked for why: the conductor's letter of 01:32, `book.json` Q6 as amended by the editor at about 01:20, and WAKE.md's new Cadence all say round the clock while there is work. So the change is explained, and no hold; but it was made from another session, which my record now says plainly (issue 006). researcher@ found the same on its own task and asked the conductor for the editor's word on dev.

## [RC1, augmented](../../../review/read/index.html)

The editor, in his review of RC1 (batch 5): commits and paths printed as text are "not enough because it doesn't link to where it goes"; he wants "this online iPad PDF kind of mode ... showing the provenance of every idea, every page, every paragraph". The first slice:

- Every RC1 chapter as a page; every commit hash, file path and register id in a paragraph linked where it can be verified. 1377 sources, 540 of them commits.
- **Only what is verified.** A hash or path is looked up in this repository and in a read-only clone of the talk's at `298be4e`. A path in both, with nothing in the paragraph to say which, stays plain; so does anything in neither (Cold-Read's commits, 11b's older projects), so nothing links into the blind repository.
- Each chapter ends with its numbers from the register: value, state, source and the command that reruns it.
- A count beside each paragraph of the sources it carries; the review pages' anchors.

## What went wrong on the way

The first run linked 505 commits and left chapter 9's own commits plain. This session's clone of the book was shallow (50 commits), so older commits of this very repository looked unknown. Unshallowed, 540; and the tool now refuses to run on a shallow clone, so its output cannot depend on how deep a clone happens to be.

## Still waiting

The sealed note (R1/R2); the length per page and the "short of time" chapters (the editor); the questions (the storyteller). A8's next steps are on issue 007.
