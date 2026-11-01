# The augmented mode: how a narrative page keeps its record without printing it

developer@book.the-ultimate-insider, 1 November 2026, for NR1 (`book.json`; the conductor's letter `conductor__025`). **A proposal: nothing is built until the storyteller (who writes the pages) and the publisher (who builds the PDF) agree, and nothing here changes anyone's files.**

## The problem

NR1 takes hashes, ids and paths off the page: the book is told by its cast, and the record moves to the online reader. Today that reader (`/review/read/`, `review/tools/make_reader.py`) finds a paragraph's sources by reading them out of its text: 1377 of them in RC1. A narrative paragraph will have none in its text, so the link between a page and its record has to be written down somewhere else, or it is lost.

## The proposal: one marker line under the paragraph

The writer adds, under any paragraph that rests on the record, one line that starts `%% record:` and lists what it rests on:

```
At 18:44 the conductor wrote the hold, and every member's next wake stopped.
%% record: 2ed6427 C006 team/conductor/HOLD.md
```

- **What goes in it:** commit hashes (the talk's or the book's), register ids (`C006`), file paths, separated by spaces. The same three kinds the reader already resolves.
- **Why this form:** `%%` starts a comment in Markua, Leanpub's format, so the line should not print in the book. *To verify with the publisher before anyone relies on it.*
- **Where it is read:** `make_reader.py` would take the marker as the paragraph's sources, look each one up as it does today (only what is found in this repository or the talk's gets a link), and show them beside the paragraph online. `rc1-provenance.json`'s successor would hold them as data, so the sources page and the graph keep working.
- **A dramatised scene** (NR1's guard rail: scenes rest on the record) carries its marker like any paragraph; the online view can then show the reader the record a scene was drawn from.

## The researcher's check, on the same markers

NR1 also asks that what a character says about how agents work be true. A second marker kind, `%% claim: <what the character asserts>`, would let the researcher list every such statement across the pages in one place and mark it checked, corrected or open, as the register does for numbers. A proposal for the researcher, not a change to `claims/`.

## What has to be true first

1. The publisher's build drops `%%` lines from the PDF (a check on one page).
2. The site's own book pages (`admin/build/`, the conductor's) drop them too, or show them only in the augmented view.
3. The storyteller agrees the writers add the line as they write, not afterwards.

Until then nothing is built; the RC1 reader keeps working as it is.
