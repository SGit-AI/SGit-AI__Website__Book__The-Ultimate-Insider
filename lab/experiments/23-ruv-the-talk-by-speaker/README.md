# Experiment LAB 23 (ruv): the talk as given, by speaker

By ruv.sgit@book.the-ultimate-insider, 31 October 2026 (the 20:54 UTC wake), the first picture made for the editor's LK1 ("a very infographic-driven book", `conductor__007`), for chapter 10, the chapter with the fewest pictures drawn from the record (`team/ruv-sgit/survey/lk1-chapter-pictures.md`).

## What it tries

The talk's 102 passages as one strip across the page, each shaded by who spoke (the editor, the room, the host), the three parts marked above it. A reader sees at once how long the editor spoke, that the room came in during part two as well as at the end, and how the parts divided the evening.

## Made from, and what it does not take

The talk repository's `team/conductor/talk-record/transcript.json` at `a9c0b49`: material added after the day, generated from the recording by the talk team's conductor (C069 says so, and this page cites it so). Only each passage's start time and speaker class are read (`passages.json` keeps just those); no words of the talk and no names reach the page or any file here. The part boundaries are where the transcript's article places its part headings (`content/articles/the-talk-as-given.md`, same commit). Passages that share a start time share its interval. The last passage's end is not stamped, and the strip says so. The only printed numbers are C069's (102 passages: 83 the editor's, 18 the room's, 1 the host's; about 87 minutes) and minute ticks.

## Its id

LAB 23, reserved for me by the designer (designer__041). Until then its header was `experiment.proposed.json` and the lab build left it out.

## Build

`python3 -B -I tools/build.py --talk <clone>` writes `passages.json`, `strip.svg` and `pages.html`; the preview is `../03-ruv-could-have-been-worse-frames/tools/preview.py` then `tools/print.js`.

## Questions for the editor

Does the strip carry chapter 10's shape better than its screenshots? Should the beats be marked as well?

## Round 2 (1 November 2026)

The designer's note (`designer__047`): at 12 mm the strip read as a rule; it is now 20 mm tall, and reads as a picture. Nothing else changed: the passages are the same, byte for byte. The beats as small ticks above the strip, the designer's second suggestion, wait on the beats' times being registered (asked of the researcher, `ruv-sgit__020`). Run `lab/runs/20261101T0254Z-ruv-23-*`.

## The beats (1 November 2026, the 04:54 wake)

The researcher registered when each beat was first heard (C097, `claims/beat-times.md`). The strip now carries one dot above it for each block of speech in which a beat was first heard; beats first heard in the same block share a dot, as the researcher's caution asks, and no beat is named. The beats the recording does not reach have none. Run `lab/runs/20261101T0454Z-ruv-26-*`.
