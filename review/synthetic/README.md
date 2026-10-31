# Synthetic readers

**SYNTHETIC READER: a test instrument, never a reader.** Kept by synthetic@book.the-ultimate-insider (`team/synthetic/ROLE.md`). Eight fictional personas go through the reviewer experience (`team/conductor/projects/reviewer-experience/README.md`) in a real browser and say what worked, with scores, before any real reviewer sees it. Their reviews are prompts for the team, never evidence about the book, never counted as readership. No persona is a real person; no real person is contacted; a run sends nothing anywhere.

## What is here

- `personas.json`: the eight personas (board member, CISO, CTO, developer, designer, project manager, journalist, founder), each with its device, time budget, themes (A to E, from the reviewers study), questions, voice, and what would impress or lose it; the seven-step reading path; the five scores (got the answer, clarity, trust, design, navigation), 1 to 5 with a sentence each. Proposed: the editor may keep, change or add.
- `run.mjs`: the runner. It serves `_site/` on a local port, opens `/review/<persona>/` in Chromium with the persona's device and a fictional token in the fragment, and writes `observations.json` and three screenshots: load time, console errors, paragraph anchors, smallest type, line length, overflow, what one click on a paragraph does, and every request to another host, blocked and listed.
- `<persona>/<run>/`: one folder per persona per run: `observations.json`, the screenshots, and `review.md`, the persona's review in its own voice with its scores, written from what the run saw. `runs/<run>.md`: the summary for the developer and the editor, with what changed since the last run.

- `names/<run>.md` and `.json`: candidate titles tested with the personas, title and subtitle alone; a test, never a choice.

- `rc1/<persona>.json`: each persona's read of its RC1 chapters and its exit interview; `rc1/briefing.md`, what they say together. `reading-time.md`: the proposal on reading time.
- `tools/build_section.py` and `tools/print_pdf.mjs`: the site's Personas section (`src/pages/personas/`) and its PDF debrief (`src/static/personas/`).

## Running it

```
python3 admin/build/build.py
node review/synthetic/run.mjs --persona all              # or --persona ciso
node review/synthetic/run.mjs --persona ciso --path /review/ciso/ --run 20261030T1700Z
python3 review/synthetic/tools/build_section.py && node review/synthetic/tools/print_pdf.mjs   # the Personas section and its PDF
```

Only Chromium is installed in a session: the Firefox and Safari personas run in Chromium with those devices' viewport and user agent, and say so.

## State

30 October 2026: run `20261030T1750Z`, the CISO through the developer's first page built locally; run `20261030T1945Z`, the CISO again on the page as released, with a phone-width check (`runs/`). Run `20261030T2145Z`: the founder through its page, and the pen checked clear of the jump bar on a phone. Run `20261030T2345Z`: both pages again after the developer's changes. The other six personas wait for their own pages.

`--device` runs a persona on another device as a check; the check is recorded under the persona's run, never as another persona.
