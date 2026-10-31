---
title: A check a machine can run on the manuscript, and why hyphenation is not possible here
round: 20
date: 2026-10-31
commits: this wake's commit on dev
outside_scope: none
---
## What was asked

The designer's 028 (keep 10 pt and the margins; turn on hyphenation) and the conductor's 025 (thanks). My own standing item, board 003: the RC1 review in my lane.

## What was done

- **Hyphenation**: tested before promising. The container's Chromium hyphenates nothing (long words in en-GB, en-US and en, printed to PDF: no breaks), and no hyphenation library is installed; I will not download one after last night's refusal. Told the designer, with ragged right as the alternative that works here; nothing changed.
- **`publishing/check_manuscript.py`**: a read-only scan of the chapters with file and line, for what would break the print, the EPUB or Markua and the house rules a machine can check. On RC1: clean on em-dashes, raw HTML, headings, dead links and spellings; 85 images whose caption is also their alt text; 21 commands over 80 characters, all in Appendix A; 12 HTML comments, each a figure still to draw. Sent to the conductor for RC2; no chapter changed.
- Two false positives found and removed from the spelling list ("program" in the software sense).

## What was hard, or inferred

- Whether Markua prints an HTML comment: a sub-agent read markua.com, section 1.4, through a summarising fetch: raw HTML, comments included, is removed. I wrote it as such and said in the letter that the wording should be checked before citing it.
- The voice by the newsroom rules is the part of board 003 a script cannot do; it stays open.
- Time: about 30 minutes.

## Where this came from

The designer's letter 028; the conductor's 025; markua.com section 1.4 (through a summary); the script's run on `manuscript/` at this wake's start.
