# The index of the source

Kept by librarian@book.the-ultimate-insider. Every file in the talk's repository (SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider) at `298be4e`, the record of the day, with where it is, what it is, who made it and when; and, kept apart, what was added after the day. Its purpose: no member wastes a wake finding something. Ask the librarian where something is (`team/<you>/requests/librarian__<slug>.md` until the mail vault exists); the answer comes at the next :09 slot.

The index says where things are and what they are. It is not a source of numbers for the book: a count here is the index's own measure, and any number a chapter uses goes through the researcher's register (`claims/`).

## How to use it

| you want | open |
|---|---|
| one area, as a table you can read | `areas/<area>.md` |
| everything, to filter by path, kind, owner or time | `index.json` (one row per file) |
| what came after the day (the recording, the editor's debrief) | `after-the-day.md` |
| where to start reading, by question | the seed, `briefs/2026-10-30/3-source-map.md`, "Where things are"; every path it names exists at `298be4e` (checked 30 October) |

## The areas, at `298be4e`

| area | file | files | lines checked by hand |
|---|---|---|---|
| the root: brief, corrections, reality, rules, CI | `areas/root.md` | 11 | all |
| the tools and the site build (`admin/`) | `areas/tools.md` | 19 | all |
| conductor (schedule, wakes, night log, briefs sent, reviews, hold) | `areas/team-conductor.md` | 214 | all 114 that are not images (30 October, 02:09 wake) |
| ruv-sgit | `areas/team-ruv-sgit.md` | 189 | all but the images (04:09 wake) |
| designer | `areas/team-designer.md` | 145 | all but the images (04:09 wake) |
| dev | `areas/team-dev.md` | 100 | all but the images (04:09 wake) |
| deck | `areas/team-deck.md` | 84 | all but the images (04:09 wake) |
| studio | `areas/team-studio.md` | 55 | all but the images (04:09 wake) |
| storyteller (story tree, maps) | `areas/team-storyteller.md` | 54 | all but the images (04:09 wake) |
| motion | `areas/team-motion.md` | 44 | all but the images (04:09 wake) |
| researcher | `areas/team-researcher.md` | 42 | all but the images (04:09 wake) |
| security (proposed, never staffed) | `areas/team-security.md` | 2 | all but the images (04:09 wake) |
| evidence: claims, sources, incidents, ideas, proposals, story, studio, method | `areas/evidence.md` | 118 | all 38 that are not images; the 80 studio captures labelled by folder (03:10 wake) |
| articles (`content/articles/`) | `areas/articles.md` | 6 | all but the images (05:09 wake) |
| the talk: beats, slides, engine, player (`src/static/talk/`) | `areas/talk.md` | 49 | all but the images (05:09 wake) |
| the rest of the site (`src/`: pages, studio, assets) | `areas/site.md` | 181 | all but the images (05:09 wake) |

1,313 files in all, 1,083 of them outside `src/`. Debrief images are counted by folder in each area table and listed one by one in `index.json`.

## Method

1. **The source is read, never written.** The talk's repository is cloned into the session's scratchpad and read with `git ls-tree`, `git log` and `git show`; nothing is pushed to it. Nothing from this index goes to the Cold-Read repository.
2. **One tool, rerun every wake.** `python3 index/tools/build_index.py <clone> --at 298be4e` writes `index.json`, `areas/*.md` and `after-the-day.md`. It is deterministic: the same clone gives the same index.
3. **Each row**: path; area (the top folder, one area per team member); kind (from the path: role, policy, wake record, debrief, review, request, brief sent, night log, claim, slide, page and so on); owner (the member folder it lives in, else the member named in the subject of the commit that added it, `@<id>:` or `<id>:`, else the commit's author); `added` and `changed`, the first and last commit touching the file at or before the pin, with its time in UTC; size; and one line on what it is.
4. **Files first added in a merge commit** (a conflict resolved there) are found with a second pass, `git log -m`, so every file has a commit.
5. **The line on what it is** is read from the file by the tool: the `title` of a Markdown file's front matter, else its first heading; for a wake record, its kind, outcome and the first sentence of its work step; for a night-log snapshot, its span and the size of each list; else an `about`-like field of a JSON file, the docstring or first comment of a script, the title of a page. Such a line is marked `(machine)` until the librarian has read the file and either confirmed it or written a better one in `read.json`. Keys and session records are described, never quoted.
6. **After the day is kept apart.** Commits after `298be4e` are listed in `after-the-day.md`, commit by commit, and never mixed into the areas. Cite them by commit and say they were added after the day (CLAUDE.md, decision S7).
7. **Prose rules apply to the tool's output**: no em-dashes, pipes escaped, long lines cut.

## Rounds

- **Round 0 (30 October, first wake):** the tool, the whole machine index (16 areas, every file), `after-the-day.md` to `424b67a`, and the first two areas read by hand: the root and the tools.
- **Round 1, first wake (30 October, 02:09):** the conductor's area read by hand (every file but its images); the tool now reads front matter, wake records and night-log snapshots, which improves every member's area.
- **Round 1, second and third wakes (03:10, 04:09):** evidence, then every other member's folder, read by hand (all but the images); the tool now reads a letter's headers and a run's purpose.
- **Round 1, complete (30 October, 05:09):** the articles, the talk and the site read by hand. Every file at `298be4e` that is not an image (842 of 1,313) has a line the librarian checked; the 471 images are listed by folder in each area table and one by one in `index.json`.
- **Next:** what the editor adds after the day, indexed apart as it arrives (to the release candidate, Monday 2 November); and, once the plan is signed, the index entries each chapter draws on; the editor's material (decision Q4) when it arrives, in its own area.
