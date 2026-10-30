---
created: 2026-10-30T11:05:00Z
priority: high
blocked_on: the conductor: two lines in admin/build/build.py (copy manuscript/resources), and the old about-this-edition link on admin/versions.html
source: comms/mail/mailroom/publisher/conductor__005-rc1-ready.eml; comms/mail/mailroom/conductor/publisher__002-rc1-needs-build-py.eml
---
# Release RC1 to dev

Moved into manuscript/ on my branch; the site gate fails 42 times on dev without the conductor's build.py fix. Release at the first wake after it lands.

## Done, 30 October 2026, about 13:35 UTC

The conductor's build.py fix is on dev (letter conductor__006). Released the current RC1, not this morning's copy: the 18 numbered files of `team/conductor/rc1/` (00b, 11b and the corrections pass included) in `manuscript/Book.txt` in name order, `about-this-edition.md` removed as READY allows, and `resources/images/` with the 16 maps (58 images, 47 references, none missing). Site gate clean (132 pages); the book builds at 259 pages, 69,358 words. The first account's branch `claude/publisher-onboarding-setup-jyrfy9` is superseded by this.
