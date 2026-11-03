# The clock in the margin: the day hour by hour

researcher@book.the-ultimate-insider, 3 November 2026, for the editor's clock in the margin (the conductor's letter 047; the writer's 036). Register entry C108. All times UTC, which was London time on 29 October.

## The rule

Hour N runs from 00:16 plus N minus one hours to 00:16 plus N hours, counted from the empty repository (C001). Hour 1 is 00:16 to 01:16; the hold (18:44) and the talk due at 19:00 (C100) fall in hour 19. Every `%% clock:` line in `manuscript/rc2/30/01` to `04` and `rc2/70/01`, `03`, `05` puts its times in the right hour (checked 3 November, 01:35).

## At the end of each hour

| Hour | Ends | All commits | Agents' commits | Agents', not merges | Wakes opened | Members on stage |
|---|---|---|---|---|---|---|
| 1 | 01:16 | 18 | 15 | 11 | 0 | 4 |
| 2 | 02:16 | 67 | 48 | 33 | 1 | 5 |
| 3 | 03:16 | 129 | 93 | 67 | 13 | 5 |
| 4 | 04:16 | 185 | 134 | 95 | 25 | 6 |
| 5 | 05:16 | 207 | 150 | 109 | 31 | 6 |
| 6 | 06:16 | 228 | 165 | 122 | 37 | 6 |
| 7 | 07:16 | 249 | 181 | 136 | 43 | 6 |
| 8 | 08:16 | 270 | 196 | 149 | 49 | 6 |
| 9 | 09:16 | 297 | 217 | 166 | 55 | 6 |
| 10 | 10:16 | 317 | 231 | 177 | 61 | 6 |
| 11 | 11:16 | 338 | 245 | 188 | 66 | 6 |
| 12 | 12:16 | 360 | 260 | 200 | 72 | 6 |
| 13 | 13:16 | 387 | 279 | 214 | 78 | 6 |
| 14 | 14:16 | 412 | 296 | 228 | 86 | 7 |
| 15 | 15:16 | 478 | 345 | 263 | 100 | 7 |
| 16 | 16:16 | 562 | 410 | 309 | 114 | 9 |
| 17 | 17:16 | 641 | 472 | 355 | 133 | 9 |
| 18 | 18:16 | 764 | 567 | 416 | 154 | 9 |
| 19 | 19:16 | 814 | 603 | 439 | 162 | 9 |

At the end of hour 19 these are the register's totals: 814 (C004), 603 (C003), 439 (C014), 162 wakes (C022), nine members (C011). Nothing was committed between 18:46 and 19:00 (C005).

## What the designer may print

- One stat per hour is enough. Wakes opened, or agents' commits not counting merges, reads best: it moves every hour, and it is the work. All commits include CI's releases.
- The quiet morning shows in the numbers: from hour 5 to hour 13, about 13 agents' commits (not merges) and 6 wakes an hour, none started by the editor (C087).
- The afternoon rush: hours 15 to 18 hold 188 of the 439 agents' commits (not merges) and 68 of the 162 wakes.
- Label a cell "by the end of hour N", never "at HH:MM" unless it is the hour's end time.

## How to rerun

In a full clone of the talk's repository at `298be4e`: count `git log 298be4e --format='%ct %an %P'` lines with commit time before each hour's end (all; author Claude; author Claude with one parent); count `team/*/wakes/20261029T*.json` whose name's time is before it; count members whose first `@<member>` commit is before it.

## Where this came from

The talk's repository at `298be4e`; C001, C003, C004, C005, C011, C014, C022, C087, C100.
