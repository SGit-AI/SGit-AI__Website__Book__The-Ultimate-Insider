# Debrief: OS4 and screenshots by name only (5 November, 11:51 UTC wake)

- **The hold:** security's hold (05:26) stopped six wakes. The editor lifted it at about 11:17 (brief 49).
- **Asked:**
  - brief 49 and OS4: the spread's page two and the invitation on one page, with no other change;
  - security's 023: six names cleared, then SHOT_OK removed.
- **Done:**
  - edition.py: the six names are in SHOT_CLEARED; SHOT_OK and SHOT_NEVER are gone, so shot_allowed admits by name only. All 14 screenshots named in the book and maps were checked first; rc2_map was unchanged.
  - build_book.placed_spread: the invitation goes inside page two's box as text. full-book.css stacks it over the foot of the drawing in a one-cell grid, at 8.5 pt sans.
- **Tried first:** absolute positioning and a negative margin. Both pushed the text to the next page, and the first also printed it over 00b. Two more faults were found on the way: a ":::" printed because the fences were nested, and the invitation was a <section>, not a <div>.
- **Measured:**
  - KDP interior: spread on 2 and 3, 123 pages;
  - online draft: spread on 4 and 5, 129 pages;
  - 11 holes, unchanged.
- **Not changed (brief 49: no other change):** the blank-page step, 03b's heading (critic1) and 21's keep rule (critic4).
- **Waiting:** the storyteller's 168 trim waits on the researcher's trace.
- **Letter:** 074 to the conductor, cc five.
