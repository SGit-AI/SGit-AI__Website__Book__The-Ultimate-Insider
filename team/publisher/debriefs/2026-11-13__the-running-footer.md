# Debrief: the running footer (13 November, 18:49 UTC wake)

- **Context:** the team was paused from 5 November (PA1) until today (RS1). The editor read the printed A4 copy, and his pen notes come in rounds (PEN1). Round 1 sent notes 3, 6, 8, 9, 15, 16, 20 and 29 to me.
- **Built:**
  - `#! running-footer`: build_book.running_footer puts each chapter on a named page (by its index) with its part and title in the footer, and a book progress bar in the middle box;
  - css_string escapes the titles (no "<", no control characters, backslash and quote escaped).
- **Faults on the way:**
  - the div's class was written "{.rf rf1}" and printed as text;
  - the last page of each chapter took the next chapter's name, fixed with break-before on the wrapper;
  - the bar did not draw until its box had a width.
- **Measured:**
  - KDP interior: 124 pages (was 123), spread on 2 and 3; online draft 126;
  - holes inside chapters down from 11 to 8.
- **Answered, not built:**
  - 3: the designer's drawing;
  - 6: the writers' word;
  - 15: a placeholder for the designer;
  - 16: next, with the storyteller;
  - 29: confirmed.
- **Letter:** 076 to the conductor, cc the designer, the storyteller and the writer.
