---
title: RC2 chapter 3 checked; my tools taught to read RC2's record notes
round: 3
date: 2026-11-02
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none
---
## What was asked

My scheduled wake of 22:09 London. No new mail. The writer's chapter 3 landed, and chapters 1 and 2 were revised: their sources now in plain names, with the exact commits and paths in a `%% record:` note kept out of print.

## What went wrong, and was fixed

My tools read a `%% record:` note as one code span with spaces in it, and skipped it. Their first "clean" on chapters 2 and 3 checked nothing, and rebuilding the index entries would have emptied them. I caught it when the rebuild showed zeros, restored the entries, and taught both tools to split the note. A test note with two faults shows both, and RC1's results are unchanged. A clean result from a checker is worth only what it read; a zero is worth looking at.

## What was done

- Chapters 2 and 3 checked clean, their record notes included; chapter 1's one flag answered in its own list.
- Chapter 3's six record quotes word for word with their speakers (`index/rc2/README.md`); `index/chapters/` rebuilt with the record notes' files and commits.
- Review `team/librarian/reviews/rc2-03.md`; letter `librarian__003` to the writer, copy to the conductor: one band into the first person, and the chapter 1 paragraph the writer marked as his reading of the editor, to be named sentence by sentence.

## For the editor

Chapter 1 carries a paragraph the writer marks as "the writer's reading of his view, beyond the voice note; his to keep or drop" (a note at line 11). It is yours to keep or drop.

## Where this came from

`manuscript/rc2/30/` at `6808e12`; the talk's repository at `298be4e`; this wake, `team/librarian/wakes/20261102T221052Z.json`.
