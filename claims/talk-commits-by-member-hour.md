# The talk's commits by member and by hour, 29 October 2026

researcher@book.the-ultimate-insider, 31 October 2026, at ruv-sgit's request for the LK1 chart (`comms/mail/mailroom/researcher/ruv-sgit__011-talk-commits-by-member-and-hour.eml`). The data is claim C095.

**Method**, as the conductor's `team/conductor/tools/day_heatmap.py` counts: the talk's repository at `298be4e`, non-merge commits from 00:00 to 18:59 UTC (London time that day), each by its commit time's hour. A commit counts for a member when its subject opens `@<member>:`. Releases (commits by GitHub Actions, `site v...`) have their own row. Commits with no `@member` prefix have their own row too, so the columns add up: 49 agent commits that name their member another way (a bare prefix, or only an `Agent:` trailer, C014) and the editor's initial commit.

| Member | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| conductor | 0 | 6 | 7 | 11 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 8 | 10 | 7 | 21 | 8 | 99 |
| ruv-sgit | 0 | 2 | 10 | 8 | 4 | 4 | 4 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 15 | 1 | 0 | 0 | 54 |
| dev | 2 | 4 | 3 | 8 | 2 | 2 | 0 | 4 | 2 | 2 | 2 | 2 | 0 | 3 | 4 | 7 | 4 | 0 | 1 | 52 |
| deck | 1 | 1 | 4 | 4 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 9 | 4 | 4 | 10 | 2 | 59 |
| researcher | 0 | 1 | 5 | 4 | 3 | 3 | 3 | 2 | 4 | 4 | 2 | 2 | 2 | 2 | 3 | 4 | 6 | 4 | 3 | 57 |
| studio | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 6 | 6 | 9 | 26 |
| designer | 0 | 0 | 0 | 3 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 19 |
| storyteller | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 2 | 4 | 3 | 3 | 15 |
| motion | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 2 | 2 | 2 | 9 |
| releases | 2 | 9 | 18 | 19 | 7 | 6 | 4 | 7 | 5 | 7 | 7 | 7 | 6 | 7 | 17 | 18 | 17 | 26 | 21 | 210 |
| other (no @member prefix) | 5 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 3 | 3 | 3 | 3 | 2 | 0 | 0 | 7 | 9 | 10 | 50 |
| **all** | 10 | 26 | 47 | 57 | 22 | 20 | 16 | 22 | 18 | 21 | 19 | 19 | 16 | 20 | 47 | 69 | 59 | 82 | 60 | 650 |

Night (00 to 05): 182; day (06 to 18): 468. These are C092's non-merge counts, 182 and 468. The member totals by `@` prefix (conductor 99, dev 52) are lower than C014's (106, 64), which also reads bare prefixes and trailers: print the method beside the chart.

## Where this came from

The talk's repository at `298be4e`, read only; `team/conductor/tools/day_heatmap.py` for the method. The command is C095's in `claims/appendix-a-commands.md`.
