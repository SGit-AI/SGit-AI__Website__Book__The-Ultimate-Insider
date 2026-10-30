---
title: The designer's first wake: staffed, keyed, scheduled, and the lab's first page printed
round: 0
date: 2026-10-30
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading, as policy.json's appends allow)
---
**Started** 13:03 UTC, at the editor's word in the session's first message (book.json X1). Five steps: plan go, pre-review go with conditions, then the work.

## What happened

- **Staffed.** `ROLE.md` and `policy.json` copied from `team/conductor/staffing/designer/` into `team/designer/` (the drafts stay). The gate refused my `ROLE.md` at once: it did not name `admin/tools/banner.py`. One paragraph added, and said so in the file; nothing else changed from the draft.
- **Keyed.** Session key `sha256:3ed7d8c321f7d1bd` made with `pki-agent.mjs keygen --session` and published (`key.json`, `key.png`, `sessions/session_01Kw9UwBewU3HcqCUwmQ57Na/`); only the public halves are in git.
- **Scheduled.** My own task, `trig_014x1ynLjnntBf5zrk7uYrML`, from `schedule.json`'s runs entry for designer, its cron and prompt word for word; first run 14:57 UTC.
- **The lab's visual language**, as rules in `lab/README.md`: A4, twelve columns with a nine-column main and a three-column margin rail, RC1's palette kept, the 9 pt floor kept and enforced, one footer, one experiment header with keep, change and drop boxes to tick on paper. It takes up three of RC1's seven points for a second design round (one grid, greyscale proof, tiles for the margin).
- **The cast**, drawn (`lab/characters/`): the conductor (square, a clock face), security (round, a magnifying glass), the hold (an octagon, the only one in the accent). Told apart by shape so they survive greyscale. No real person drawn; the editor appears only in his own quoted words.
- **The build** (`lab/tools/build_lab.py`, `render.mjs`, `lab.css`): it refuses text under 9 pt, a page whose content overflows, and a wrong page count. It refused my first version (page 2 overflowed by 292 px), which is why LAB 01 is three pages, not two.
- **LAB 01, one visual language for paper**: printed as `lab/pdf/the-ultimate-insider-lab.pdf`, 4 pages with the cover, hash in `SHA256SUMS`. Every number on it traces to the register (C002, C006, C011, C024).

## Judged as design

My own reading of the rendered pages: the type-scale labels wrapped and the rail's tile carried a number the body did not, against the rail rule I had just written; both fixed before the push. Open: the cast's bubbles hold placeholders, marked as such, because the words are the storyteller's.

## Next

1. Ask the storyteller for the cast's first lines (one each, at most 90 characters).
2. Ask the conductor for a site page for the lab PDF.
3. A design verdict on ruv.sgit's first experiment when it lands; then the next of my own (the condensed storyboard, experiment 3 of the brief).
