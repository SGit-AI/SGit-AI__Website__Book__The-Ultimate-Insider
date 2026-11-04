# RV2, the developer's lane: the site's pages of the book

4 November 2026, 06:30 UTC, in answer to conductor__041. Lane: the RC2 page, the principles page, the upload set; principles 18, 21 and 26. Read: `src/pages/rc2.html`, `src/pages/index.html` (where it points to the RC2 page), `src/pages/principles.html` against `team/conductor/guides/the-principles.md`, the online view of chapter 00 (`src/pages/review/rc2-150/00-start-here.html`) against `manuscript/rc2/150/00-start-here.md`, and the upload set (`.github/workflows/release.yml` line 109 on, and what the site serves under `/rc2/upload/`). Severity: must, should, could.

## Findings

| # | Where | Principle | Severity | Finding |
|---|---|---|---|---|
| 1 | `src/pages/rc2.html` lines 1 to 3, 9 to 25 | 21 (and the full-book decision FB1) | must | The page is the 30-page edition's progress page as of 3 November, about 00:15 UTC: the title is "RC2, being written", the heading "The 30-page edition, chapter by chapter", and the table has six rows (chapters 1 to 5 and "the series page") that are not the full book's 29 chapters. A reader is told the book is a 30-page draft with security and the researcher still to read chapters 4 and 5. The full book is now the book. |
| 2 | `src/pages/rc2.html` lines 12 to 14 | 21 (say it once) | should | The same message is given three times: "the latest version of every edition is always here" (12), "drafts in review" (13), "a draft in review ... rebuilt at every release" (14). Keep one. |
| 3 | `src/pages/rc2.html` line 10 | 21, FB1 | should | The primary button is the 30-page draft; the full book is the third button and reads "as far as it goes". The full book should lead; the older editions stay online as they are (conductor__038). |
| 4 | `src/pages/index.html` lines 16 and 48 | 18 | should | The home page's button reads "RC2, being written now" and the zoom list says "30 pages: being written now"; it does not say the full book is the book, or that it is published as a PDF. |
| 5 | the upload set | none of 18, 21, 26 | could | `/rc2/upload/` is served (the page count file answers 200 and says 136 pages), but no page of the site links to it or says what it holds. The editor's word (brief 20) is that it is "the master of everything"; a reader or the editor cannot find it from the site. Links are the conductor's pages; the publisher knows the file names. |
| 6 | `src/pages/review/rc2-150/00-start-here.html` | 26 | could | The online view prints each Figure as a text line (lines 10, 14 and 29), not as a drawing, so one caption per figure and the caption above it cannot be checked here. They can be checked only on the PDF, which is the designer's and the publisher's lane. Not a fault: a limit of this lane. |

## Passed in my lane

- `src/pages/principles.html`: in step with `the-principles.md` (35 principles in both, same commit at 05:09 UTC). No finding.
- `00-start-here`, online view only: principle 18 (the formula, the map, the hellos, the path to the talk are all there), principle 21 (the five steps are said once in text; the figure line says "the words stay in the text above"), principle 26 (three figure lines, one caption each, none below). Passes in my lane as the online view. The printed page is the designer's.
- No other manuscript section is in my lane; I have not read the others.

## What I did not check

The printed layout (the designer's and publisher's lanes; my page check measures how far a page is filled and where a caption falls, nothing about how a page looks). Nothing here is a sign-off: only the editor signs a section off (SO1, open).

## Status at 08:30 UTC

Findings 1 to 4 are addressed by the conductor's commits of 08:10 and 08:11 (66b3b0de, 9441dd02, 89b60fd3): the RC2 page is now the full book's, as a draft in review, and the home page says so. Read again at the 08:12 wake: rc2.html leads with the full book's PDF and carries one "every edition is a draft" note. Finding 5 (nothing links to the upload set) is still open; finding 6 is a limit, not a fault.
