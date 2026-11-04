# WC1 for my tools; Appendix A re-set; the 150's chapter 1 as the editor's account

By librarian@book.the-ultimate-insider, 4 November 2026, about 02:17 UTC. Read: `git diff c2639c49..cc38dfa6 -- manuscript` (four files: 150/01, 92, 93, Book.txt); the conductor's 026 and the editor's WC1 (`book.json`, brief 10). Edited nothing of the writer's.

## WC1: the tools

The editor's decision WC1: no "Where this came from" in the printed book; the sources stay in each chapter as `%% record` lines. What changed:

- `index/tools/check_sources.py`: reads every `%% record` and `%% clock record` line anywhere in a chapter, as well as the section and the inline lines; "no sources" is now only reported when there is no section, no inline line and no record line. The record notes' shorthand is taken: parenthetical comments dropped, quoted words and hostnames and money skipped, a page of the talk's site (`talk/slides/three`, `studio-ports/abp-review`, `articles/<name>.html`), a letter by its number (`security__001`), a file name cut to its tail (`__the-five-step-wake.md`), glob patterns against folders too.
- `index/tools/chapter_entries.py`: the same record lines and the same shorthand, plus a bare file name only one file has; the entries now also draw on the per-section notes, so most chapters gain files.
- `team/librarian/voice/voice_scan.py`: already ends the reading text where a heading is missing; tested on a file with none. `--logistics` added at 01:15.

After the post-review's finding (parentheses hid any path; the `__` rule was broad) two changes: a path with an extension inside a parenthesis is checked (quoted words are not), and the letter-number rule needs the form `folder/name__NNN`. Checked both ways. Over the 30, the 70 and the 150 as they stand: every old finding is still found but four known non-faults (a hostname, a shorthand range, a folder pattern, a web address); no new finding. Negative controls: a chapter with no section and three bad record lines (an unknown register id, a nonexistent path, a missing commit, a nonexistent manuscript path) is flagged four times; a clean one is clean; one with no sources at all is flagged "no sources". The writer may convert the sections now (letter `librarian__023`).

## Appendix A, re-set (46 entries)

All ids are in the register. "Cited in" matches the chapters but for C010 (94 cites it). The twenty plain-git command lines run against the talk and return what they ask for, C111's now too ('a Wardley map'). C115 (studio's refusal of a relayed word) is new; C068's command is held out of print until the editor decides D12, as security asked.

## The 150's chapter 1

Rewritten as the editor's own account (his brief 04): his claims follow that brief (a long wish to present better; slides written in the last hours or days; a feedback loop while creating; the talk before, for ruv.sgit.ai, gave the confidence; the player and the first ports came from there; "a continuum"). The quoted passages of his voice note and the transcript are gone; the Wardley moment is now told in the narrator's words, with the transcript's own ("the best thing I have learned in the last decade", "it is how I think", genesis to commodity). The two debrief titles in the record note are in `index/talk-site/crawl.json`.

## A correction of mine

Letter 022 said "fifteen minutes apart" is not in the commit message of `09f13d5`. It is, wrapped over two lines (and in `02cbd86`'s): the writer was right. Corrected in 023.

## Where this came from

`index/tools/`, `team/librarian/voice/voice_scan.py`; `manuscript/rc2/` at `cc38dfa6`; `claims/register.json`; the talk's repository at `298be4e` and `a9c0b49`; `briefs/2026-11-04__in-session/04` and `10`.
