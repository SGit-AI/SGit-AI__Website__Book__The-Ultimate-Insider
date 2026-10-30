---
title: The reviewer experience, designed; developer@ and synthetic@ drafted; R1 and R2 for the editor; brief 2
round: 1
date: 2026-10-30
commits: dev at the commit that carries this file
site_version: the release after this push
outside_scope: none
---
## What the editor asked

About 13:30 UTC: zoom in on the feedback capability. A vault per reviewer and a pen lane; every collaborator onboarded with their own PKI key; a review that makes time-poor reviewers productive and visibly impressed, because spreading the team's technology is a side objective; simulate it first with a developer and synthetic readers in the newsroom's personas; a site that feels personalised but is deterministic, with sealed messages for some readers; and his own review, diffs included.

## What shipped

- `team/conductor/projects/reviewer-experience/README.md`: the reviewer's first ten minutes, step by step; each piece (identity, personalisation, the pen lane, the editor's review, diffs) in a first version without vaults and with them once signed; eight fictional personas; four phases (simulate, the editor, one friendly reviewer, the first wave); who does what.
- Two members drafted in `team/conductor/staffing/`: developer@ (builds it; fictional data only, no contact with anyone) and synthetic@ (runs the personas in a real browser; test instruments, never readership); runs on odd hours (:12, :42) to spread the load; prompts in `ONBOARDING.md` 1d.
- `book.json`: R1 (a vault per reviewer) and R2 (PKI onboarding), open.
- Brief 2 (`editor-briefs/2026-10-30T1345Z`), the delta since brief 1.

## Read for it

The PHP newsroom's synthetic readers (`admin/synthetic/personas.json` there), the Gen ZX book's pen notes (`admin/content/reviews/paper/rc2-0*.json` there), read only. The Cold-Read team's synthetic readers exist too; nothing was taken from or sent to that repository.

## Where this came from

The editor's words in this session; this wake's record (`wakes/20261030T133602Z.json`).
