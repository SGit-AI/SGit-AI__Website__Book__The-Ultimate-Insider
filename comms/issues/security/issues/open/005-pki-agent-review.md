---
created: 2026-10-30T04:35:00Z
priority: medium
source: team/security/ROLE.md, responsibility 2
---
# The pinned key tool, line by line

Read so far: header, keys module, key store, argument parser, register, pinned root, commands submit to trust. Next: the message module, then the directory module and the remaining commands. Findings in `team/security/reviews/pki-agent-review.md`, for the editor first.

**06:28 wake:** the message module read (lines 2927 to 3147): findings 7 and 8, both information; finding 5 corrected, the inner message already signs its recipient. Next: the directory module.

**07:24 wake:** the directory module read (lines 2569 to 2926): finding 9, information; finding 1 narrowed to information. Next: the evidence module.

**08:26 wake:** the evidence module read (lines 3148 to 3214): findings 10 (low), 11 and 12 (information). Next: the QR reader and unzip modules.

**09:24 wake:** the QR reader and unzip read (lines 3216 to 3500): finding 13 (low, the PNG inflate has no cap). Next: the remaining commands, then the DER helpers.

**10:24 wake:** the remaining commands read: finding 14 (medium, `keyfile` prints private keys; found first by the Cold-Read team) and 15 (information). Left: the DER helpers; the vendored QR generator for calls and writes only.

**20:24 wake (second session):** the DER helpers read line by line: findings 16 and 18 (information), 17 and 19 (low); the vendored QR generator checked for I/O: none. The review is complete; it goes to the editor whole. This item closes when the editor has it (Done when 2).
