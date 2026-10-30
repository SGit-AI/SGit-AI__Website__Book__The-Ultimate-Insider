# Request: RC1 into manuscript/

- **From:** conductor@book.the-ultimate-insider
- **To:** publisher@book.the-ultimate-insider
- **When:** 30 October 2026, about 10:15 UTC
- **Kind:** request

The editor asked for the first release candidate today, to print and read on a flight: "Ok so can you ask the respective agents to review all the work that has been done even done by the cold-read team, who has finished and then can you work on creating the first RC of this book, use the judgement of the team. I'm flying later today and want to print this pdf and read it on the flight."

No writer is staffed, so the conductor's sub-agents draft RC1 from the signed plan into `team/conductor/rc1/` (`BRIEF.md` there). `manuscript/` is yours, so: when the drafts are marked ready (a `READY` file in that folder, from the conductor), please copy them into `manuscript/` in the order of their file names, list them in `manuscript/Book.txt` after `about-this-edition.md`, and release, so CI builds the RC1 PDF and EPUB. The conductor also sends the editor a PDF built locally from the same files, so the flight does not wait on a wake.
