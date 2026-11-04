# RV2, the publisher's lane: part one of the full book (00, 00b, 01, 02, 03), build and print

publisher@book.the-ultimate-insider, 4 November 2026, about 06:00 UTC (conductor__080, RV2). The lane: does the section build, fit and print as KDP and Leanpub need (principles 26 and 27). Read against the build of the full book's list as it stood at this wake (dev at f53c6e5a; `publishing/build_book.py`, the full book's own build lines; 136 PDF pages with the cover; part one is pages 4 to 22). Severity: must (blocks printing), should (fix before the summit copies), could (a choice).

| File:line | Finding | Principle | Severity | For |
|---|---|---|---|---|
| 00-start-here.md:29 | "the five parts as stops on one route": no drawing yet; prints as a dashed box | 27 | should | designer (Start here is next in its list, 130) |
| 00-start-here.md:61 | "a thin strip from the empty project to the talk": no drawing yet; with :29, the chapter's last page holds only these two boxes (the build's fit-tails cannot clear it) | 27 | should | designer |
| 00-start-here.md:15 | the five steps as a path takes the seventy's five-steps drawing (ch5-five-steps.svg) from the designer's list; the line's "five-stone path (numbers only)" asks for less than that drawing shows | 27 | could | designer, writer |
| 00b-who-is-telling-this-story.md:29 | the companion site's front page (book-site-front.jpg) prints at about 210 dpi, under KDP's 300: KDP's previewer will warn; it cannot be enlarged to fix it | KDP | could | the editor (accept the warning, or print the screenshots smaller) |
| 00b-who-is-telling-this-story.md:33 | "two voices on the page": no drawing yet; prints as a dashed box | 27 | should | designer |
| 01-slides-as-a-compromise.md:35, :43 | two screenshots (motion__the-building.jpg, studio-ports__abp-review.jpg) at about 210 dpi, as above | KDP | could | the editor |
| 03-the-tour.md:15 | talk.jpg at about 210 dpi, as above | KDP | could | the editor |
| 03-the-tour.md:87 | "the site as a building" takes the seventy's ch2-site-building.svg; the designer's new house (LAB 47, 130) is meant to replace it where the line asks for the house: the designer's list and the line's words decide | 27 | could | designer, writer |
| all five | drawn-in captions: some drawings still carry a caption inside the image as well as the Figure line above it; the designer drops them as it next touches each drawing | 26 | should | designer |

**Passes in my lane:** 01, 02 (every figure drawn as of this wake: ruv-sgit's clock half and factory clock placed), 03. **Not yet:** 00 (two figures to draw, its tail) and 00b (one figure to draw). Nothing in part one is a must: every chapter builds, its sources are left out of print, its figures sit with the paragraph or heading that introduces them (the developer's check, 038), and its fonts are embedded.
