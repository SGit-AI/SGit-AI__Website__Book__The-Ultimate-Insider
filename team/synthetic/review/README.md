# Synthetic readers

**SYNTHETIC READER: a test instrument, never a reader.** Kept by synthetic@book.the-ultimate-insider (`team/synthetic/ROLE.md`). Eight fictional personas go through the reviewer experience (`team/conductor/projects/reviewer-experience/README.md`) in a real browser and say what worked, with scores, before any real reviewer sees it. For now these files live in `team/synthetic/review/`, not `review/synthetic/` as ROLE.md says: the developer's policy claims `review/**`, so both claimed them and the gate failed. They move back when the developer's policy leaves `review/synthetic/**` out. Their reviews are prompts for the team, never evidence about the book, never counted as readership. No persona is a real person; no real person is contacted; a run sends nothing anywhere.

## What is here

- `personas.json`: the eight personas (board member, CISO, CTO, developer, designer, project manager, journalist, founder), each with its device, time budget, themes (A to E, from the reviewers study), questions, voice, and what would impress or lose it; the seven-step reading path; the five scores (got the answer, clarity, trust, design, navigation), 1 to 5 with a sentence each. Proposed: the editor may keep, change or add.
- `run.mjs`: the runner. It serves `_site/` on a local port, opens `/review/<persona>/` in Chromium with the persona's device and a fictional token in the fragment, and writes `observations.json` and three screenshots: load time, console errors, paragraph anchors, smallest type, line length, overflow, what one click on a paragraph does, and every request to another host, blocked and listed.
- `<persona>/<run>/`: one folder per persona per run: `observations.json`, the screenshots, and `review.md`, the persona's review in its own voice with its scores, written from what the run saw. `runs/<run>.md`: the summary for the developer and the editor, with what changed since the last run.

## Running it

```
python3 admin/build/build.py
node team/synthetic/review/run.mjs --persona all              # or --persona ciso
node team/synthetic/review/run.mjs --persona ciso --path /review/ciso/ --run 20261030T1700Z
```

Only Chromium is installed in a session: the Firefox and Safari personas run in Chromium with those devices' viewport and user agent, and say so.

## State

30 October 2026: personas and runner written; the runner checked against the site's home page (not a persona run, not kept). The first run waits for the developer's first review page on `dev` (`comms/issues/synthetic/issues/blocked/001-first-persona-run.md`).
