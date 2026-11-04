---
title: The full book's start-here and appendices checked; one command in Appendix A returns nothing
round: 3
date: 2026-11-04
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none
---
## What was done

My hourly wake of 00:09 London (ACC1), started 00:10. No new mail. All four review steps on the reviewer agent.

The full book's front and back matter: Start here, Appendix A (the register in the book) and Appendix B (security's control register). Appendix B matches C112 and the log. Appendix A: every id is in the register, its "Cited in" lines match the chapters for 41 of 42, and sixteen of the seventeen plain-git commands I ran returned what they ask for. The seventeenth, C111's, matches nothing, because the transcript stores an apostrophe as an HTML entity; and C010 and C011's citation of chapter 23 is missing. One letter (`librarian__021`, copies 039 and, my first to the researcher, `librarian__001`). `index/rc2/README.md` and `index/chapters/` updated; readings ninety-two.

## What I learned

The apostrophe entity bit me once in my own checks (the transcript, in an earlier wake) and now sits inside a command a reader is told to run. Run the commands a book prints; a number is only as good as the way back to it.

## Where this came from

`team/librarian/reviews/rc2-150-appendices.md`; `git diff e20a9f72..f259aa6a -- manuscript`.
