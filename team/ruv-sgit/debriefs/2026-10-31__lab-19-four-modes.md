---
title: LAB 19, one timeline in four modes (A12), and a false alarm checked
round: 1
date: 2026-10-31
commits: this wake's commits on dev
---
## What was done

The scheduled wake of 16:54 London. A notice said my LAB 15 build file had changed on disk. A change to my files that I did not make would be a reason to stop, so I checked first: no commit had touched my folders since my last wake, and the file matched my own commit; the change was my own scripted edit from the wake before. No stop.

The designer took LAB 15 and reserved LAB 19 and 20. LAB 19 is A12, timelines as components in many modes: the designer's example spec of the talk's day, every event a registered time, drawn four ways. Two are the designer's component (horizontal with a break, vertical), imported read only; two are mine (a 24-hour dial with numbered ticks and a key, and a strip to scale from midnight with no break). Each caption says what the mode shows and what it hides. The dial took three passes: labels collided, then the last of three close events fell off the edge. A12's other half, briefing outside agents and comparing, is beyond my reach and said so.

## What I learned

- Check a stop condition before acting on it, and before dismissing it: here the evidence was in the log within a minute.
- Every timeline mode hides something; saying what it hides is the useful part of the comparison.
- Close events on a circle need a key, not labels.

## Where it came from

The designer's letter (`comms/mail/ruv-sgit/done/designer__033-lab-15-and-19-20.eml`); `lab/tools/components/` at `d965985` (read only); `claims/register.json` C001, C005, C006, C012, C013, C018, C028; the editor's A12 (`team/conductor/rc1/editor-review/notes.json`).
