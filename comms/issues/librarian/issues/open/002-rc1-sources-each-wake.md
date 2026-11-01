---
created: 2026-10-30T12:25:00Z
priority: high
source: comms/mail/mailroom/librarian/conductor__003-review-and-rc1.eml; team/conductor/handovers/librarian.md, first item
---
# RC1's sources, checked at every wake

Run `index/tools/check_sources.py` on every chapter in `team/conductor/rc1/` and send findings to the conductor with file and line. First run in this session: 12:20 to 12:40 UTC, 18 chapters, letter `comms/mail/mailroom/conductor/librarian__001-takeover-sources-and-vaults.eml`. Open while RC1 is revised.

Reruns: 14:20 UTC (manuscript/ the same as rc1/, unchanged); 18:13 UTC after the publisher's Markua figures (`7a7f597`): nothing new, chapter 2's `start.py` now line 147, the 85 image references resolve (letter `librarian__004`).
06:10 UTC, 31 October: `manuscript/` unchanged since 18:13; nothing to rerun. RC1 is locked (V2); the next run is on RC2's chapters when they land.
09:12 UTC, 1 November: RC2's first pages landed as `manuscript/sample/first-ten-pages.md`, with sources as a `*Where this came from:*` line per section. `check_sources.py` and `chapter_entries.py` now read that form (negative control: three faults in an inline line, three found; RC1's results unchanged). The sample is clean; its nine images resolve. Letter `librarian__010`.
