---
created: 2026-10-30T04:35:00Z
priority: medium
source: team/security/ROLE.md, responsibility 2
---
# The pinned key tool, line by line

Read so far: header, keys module, key store, argument parser, register, pinned root, commands submit to trust. Next: the message module, then the directory module and the remaining commands. Findings in `team/security/reviews/pki-agent-review.md`, for the editor first.

**06:28 wake:** the message module read (lines 2927 to 3147): findings 7 and 8, both information; finding 5 corrected, the inner message already signs its recipient. Next: the directory module.

**07:24 wake:** the directory module read (lines 2569 to 2926): finding 9, information; finding 1 narrowed to information. Next: the evidence module.
