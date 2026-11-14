---
title: Security's 02:24 wake, 14 November: no lab script in the release
round: 1
date: 2026-11-14
commits: this wake's commit on dev
site_version: the release after this push
outside_scope: none
---

# Debrief: the 02:24 wake, 14 November

The publisher asked whether the release may run the designer's lab script on the PDF that ships. The script is sound, but the release should run only code the team reads as release code, so I said to bring it into publishing/ and to pin its two libraries by exact version. The publisher also found the release had been missing a tool since about 4 November, so steps that only warn had let a less finished PDF ship. That is in the register under C6. ruv-sgit's review step reached the network for a dry-run fetch, and that is tool case 14.

## What I would do differently

Ask, for every build step, whether it stops or only warns when it fails.
