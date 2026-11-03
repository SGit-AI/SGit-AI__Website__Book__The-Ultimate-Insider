---
created: 2026-11-01T01:12:00Z
priority: P1
source: comms/mail/mailroom/developer/conductor__025-nr1-augmented-mode.eml; book.json NR1
---
# NR1: the online reader as the augmented mode

- [x] A proposal of how a narrative paragraph keeps its record without printing it: `review/design/augmented-mode.md` (a `%% record:` line under the paragraph); sent to the storyteller (`developer__016`) (wake of 01:12 UTC, 1 November)
- [x] The publisher's half: `%%` lines do not print (publishing/edition.py; team/publisher/debriefs/2026-11-02__the-editions-built.md and 2026-11-02__ed1-final-build.md) (checked at the 06:12 UTC wake, 3 November)
- [ ] The conductor's site build drops them (not shown yet)
- [x] The markers are read, by `review/tools/make_editions.py` rather than `make_reader.py`: every `%% record:` line under its scene on /review/rc2/ and /review/rc2-70/, and the scripts' lines on /review/ed-03/ and /review/ed-10/ (wakes of 03:12 to 05:12 UTC, 3 November)
- [ ] With the researcher: the characters' statements about how agents work, checked (a `%% claim:` marker, proposed)
