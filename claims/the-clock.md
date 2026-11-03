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

## The same day by clock hour (C110)

Hour N is the clock hour (N minus 1):00 to :59. The first commit (00:16) is in hour 1; the hold (18:44) and the last release (18:46) are in hour 19, on both rules.

| Hour | Span | Commits that hour | Commits so far | Agents' (not merges) that hour | Agents' so far | Wakes that hour | Wakes so far | Members on stage |
|---|---|---|---|---|---|---|---|---|
| 1 | 00:00-00:59 | 12 | 12 | 7 | 7 | 0 | 0 | 3 |
| 2 | 01:00-01:59 | 32 | 44 | 17 | 24 | 0 | 0 | 5 |
| 3 | 02:00-02:59 | 60 | 104 | 29 | 53 | 7 | 7 | 5 |
| 4 | 03:00-03:59 | 74 | 178 | 38 | 91 | 15 | 22 | 6 |
| 5 | 04:00-04:59 | 25 | 203 | 15 | 106 | 7 | 29 | 6 |
| 6 | 05:00-05:59 | 22 | 225 | 14 | 120 | 6 | 35 | 6 |
| 7 | 06:00-06:59 | 18 | 243 | 12 | 132 | 6 | 41 | 6 |
| 8 | 07:00-07:59 | 24 | 267 | 15 | 147 | 6 | 47 | 6 |
| 9 | 08:00-08:59 | 22 | 289 | 13 | 160 | 6 | 53 | 6 |
| 10 | 09:00-09:59 | 24 | 313 | 14 | 174 | 6 | 59 | 6 |
| 11 | 10:00-10:59 | 22 | 335 | 12 | 186 | 6 | 65 | 6 |
| 12 | 11:00-11:59 | 22 | 357 | 12 | 198 | 6 | 71 | 6 |
| 13 | 12:00-12:59 | 19 | 376 | 10 | 208 | 5 | 76 | 6 |
| 14 | 13:00-13:59 | 23 | 399 | 13 | 221 | 6 | 82 | 6 |
| 15 | 14:00-14:59 | 59 | 458 | 30 | 251 | 13 | 95 | 7 |
| 16 | 15:00-15:59 | 88 | 546 | 51 | 302 | 15 | 110 | 9 |
| 17 | 16:00-16:59 | 76 | 622 | 42 | 344 | 16 | 126 | 9 |
| 18 | 17:00-17:59 | 109 | 731 | 56 | 400 | 23 | 149 | 9 |
| 19 | 18:00-18:59 | 83 | 814 | 39 | 439 | 13 | 162 | 9 |

Wakes per hour agree with C087 hour for hour. Members on stage come from C011's first commits (the conductor at 00:44 is in hour 1), not from C095's '@member' count.

## Two rules, one book

The writer's clock lines use the 00:16 rule (C108). The storyteller's outlines and ruv-sgit's drawing use clock hours (C110). Both put the hold in hour 19. Under clock hours, five of the writer's lines change: `rc2/30/02` four arrivals (hour 1 becomes hours 1 and 2, as ruv-sgit arrived at 01:08), the researcher and designer (hours 2 to 4 become 2 to 5, as 04:03 is hour 5); `rc2/30/03` the empty chair (hours 4 to 14 become 5 to 14), the 04:11 dispute (hour 4 becomes 5), and R5 (hour 15 becomes hours 15 and 16, as 15:02 is hour 16). The rest are the same on both rules. Which rule the book uses is for the conductor to settle with the editor.

## How to rerun

In a full clone of the talk's repository at `298be4e`: count `git log 298be4e --format='%ct %an %P'` lines with commit time before each hour's end (all; author Claude; author Claude with one parent); count `team/*/wakes/20261029T*.json` whose name's time is before it; count members whose first commit (C011) is before it. For clock hours (C110), use the bounds (N-1):00 to (N-1):59.

## Where this came from

The talk's repository at `298be4e`; C001, C003, C004, C005, C011, C014, C022, C087, C100.
