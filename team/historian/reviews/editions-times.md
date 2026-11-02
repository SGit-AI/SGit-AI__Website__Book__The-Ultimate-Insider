# The 3- and 10-page editions and the sample, against the timeline

historian@book.the-ultimate-insider, wake of 2 November 2026, 09:20 UTC (`team/historian/wakes/20261102T092049Z.json`). Read only: `manuscript/editions/03/`, `manuscript/editions/10/` and `manuscript/sample/first-ten-pages.md` at dev `ca9958a`, against `timeline/` (`cast.md`, `cast-scenes.md`, `after-1900.md`, `after-the-day.md`) and the talk's record at `298be4e`. Dramatised lines are not findings; only a time, an order, an attribution or a fact the record contradicts. A read-only sub-agent of this session made the first pass (about 55 checks); I verified each finding below against the record and corrected one line number.

No religious word (RW1) appears in any of these files.

## Findings

| Where | The text says | The record says | Evidence |
|---|---|---|---|
| `manuscript/editions/03/02.md:21` | "Later the researcher joined", told after the conductor's first five-step wake was caught by its own review | The researcher joined at 01:52:10, before that review at 02:19: the order is reversed. "Earlier, the researcher had joined", or move the line up | `01e9ed3`, `c8f6f8f`; `timeline/cast.md` |
| `manuscript/sample/first-ten-pages.md:68`; `:145` and its source line `:156` | "The conductor came first"; "One agent first, the conductor", "the order the team itself was set up in on 29 October" | Dev came first, at 00:40:50 (the site, the gate and the talk); the conductor joined at 00:44:37. If the method's advice is to start with a conductor, say it is the advice, not the day's order | `1f7c633`, `97b98d9`; C011; `timeline/cast-scenes.md`, scene 1 |
| `manuscript/editions/03/01.md:9`; `manuscript/editions/10/02.md:39` | "At a quarter past midnight I opened an empty project, wrote a brief and one page of rules" | The 00:16:23 commit holds only a licence, a README and a file list; the brief (`BRIEF.md`) and the rules (`CLAUDE.md`) first reach the record in dev's commit at 00:40:50. He may have written them in chat first; the record dates them to 00:40, by dev | `2e4b1f4`, `1f7c633` |
| `manuscript/sample/first-ten-pages.md:3` | "At seven that evening I walked on stage in London and gave the talk" | The start time is in no record; 19:00 was the plan. That the talk was given rests on the transcript added after the day (`a9c0b49`), which gives no start time | `timeline/after-1900.md`; `timeline/after-the-day.md` |
| `manuscript/sample/first-ten-pages.md:50`, `:98` | "from 18:39, minutes before I went on stage"; "At 18:44, sixteen minutes before the talk" | The plan told as the event; the editions already say "before the talk was due" (`03/03.md:97`, `10/06.md:9`): the sample should match | `2ed6427`, `867f8c2`; `timeline/after-1900.md` |
| `manuscript/editions/10/01.md:13`, `:29` | "On 29 October I gave a talk ... I pressed play"; the band "given on the evening of 29 October" | That it was given that evening rests on `a9c0b49`, added after the day; the band should say so, as the sample's line 19 does for the length | `timeline/after-the-day.md`; C069 |
| `manuscript/editions/10/07.md:55` | "the out-of-date figure went on stage" | Minor: right by the register (C031), but "on stage" rests on the talk as given, after the day, unmarked; the day's record shows it reached the slide (the sample's `:116` wording) | C031; `a9c0b49` |

## What holds

The hold at 18:44:13 and the designer's commit after it; the quiet stretch from about five in the morning to two in the afternoon (C087); the bands of edition 10's fourth chapter (04:11, 06:21, 10:05, 10:49); R5 at 14:33 and 15:02; the player at 15:07; studio's refusal at 17:47; the 02:47 freeze and its 02:52 correction; the locks never run (C027); the editor's later accounts of why the team stopped, marked as after the day (C089).

## Where this came from

`manuscript/editions/` and `manuscript/sample/` at dev `ca9958a`; `timeline/`; the talk's history at `298be4e` and `a9c0b49` (after the day); the register (C011, C027, C031, C069, C087, C089).
