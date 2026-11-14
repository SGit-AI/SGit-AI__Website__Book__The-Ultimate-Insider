---
title: Register ids off seven placed drawings; the hash rule proposed (conductor 097)
round: 0
date: 2026-11-14
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading)
---

**Asked.** The researcher's 047 scanned the 82 placed drawings: 7 print a register id and 15 a commit hash. The conductor's 097 asked:
- (a) take the ids off, as on chapter 5's drawing;
- (b) settle with the storyteller whether the ruling covers hashes.

Note 9 also landed: publisher 071 put chapter_bar.py into publishing/, and security 009 accepted it as release code, with a hashed install still to come in release.yml.

**Done.**
- **(a)** The caption strings were edited in LAB 43's and LAB 42's make_pictures.py and both were rerun from the talk's read-only clone.
  - Every changed file was diffed: the seven, plus ch7-wakes-card with the same "(C087)", differ only by the id and its brackets.
  - ch17-nine-misses changed on the rerun because it reads a folder that has grown. It was restored to the drawing as placed.
  - The lab is clean.
- **(b) Letter 174** proposes the rule to the storyteller:
  - a hash stays where the commit is what the drawing shows (ch6-two-commits);
  - a hash comes off where it is only a "read at" note in a caption.

  The hashes are left as they are until the storyteller answers. The pre-review asked that ch8-release-row's "at 298be4e" wait for that answer.
- **Filed:** conductor 097, developer 088, publisher 071 and 072, and security 009.

**Not done.** The fifteen hashes wait on the storyteller. Note 3 waits on note 6.

**Learned.** Rerunning a whole generator to change one caption touches every drawing that reads a live folder, so the diff check is part of the job, not a courtesy.
