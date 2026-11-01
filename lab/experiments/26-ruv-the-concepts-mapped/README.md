# LAB 26 (ruv): the concepts, mapped

By ruv.sgit@book.the-ultimate-insider, 1 November 2026 (the wake of 04:54 London), for the editor's LK1 ("a very infographic-driven book") and chapter 13, the one chapter with no picture (`team/ruv-sgit/survey/lk1-chapter-pictures.md`; `team/ruv-sgit/lk1-visual-plan.md`), in the id the designer reserved.

## What it tries

Chapter 13 is the book's reference: each concept has an entry, and each entry says where the book shows it. This page draws those entries: the concepts down the left in the chapter's five groups, the chapters down the right in the book's order, and a line from each concept to each chapter its entry names. A reader who meets a word in chapter 9 can see where else it lives, and the chapters with the most lines are where the ideas meet.

## How it is made

`tools/build.py` reads `manuscript/13-concepts-and-principles.md` and `manuscript/Book.txt` (read only) and writes `concepts.json`, `map.svg` and `pages.html`. Only the part of each entry before "Where it is thin" is read, so a line means "shown here", not "thin here". One label is shortened to fit its column: "The brief, the reality file and the corrections file" is set as "The brief, reality and corrections". No number is printed. The map follows the chapter: rebuild it when the chapter changes.

## Not yet

The visual plan also proposed marking the concepts the chapter calls thin; every entry has a "Where it is thin", so a mark would not tell them apart. Left out.

## Questions for the editor

Does the map help a reader find their way back, or is the chapter's own list enough? Should a line say which chapter explains a concept and which only shows it?
