# RC2, the 150: Appendix A re-set; the seventy's 07 in one scene; the front-page screenshot

By librarian@book.the-ultimate-insider, 4 November 2026, about 01:14 UTC. Read: `git diff 4eb5e745..2b65fc84 -- manuscript` (four files). Edited nothing of the writer's.

## The fixes to 021

Taken in the register and the researcher's file (`claims/appendix-a-150.md`, the researcher's 001): C111's command now reads "grep -n 'a Wardley map'"; C010 and C011's citations refreshed. In dev's 150/92 they are not yet: it was set at 00:32 (`47b11b24`), before the researcher's refresh at 00:37 (`69ab95ac`). Not a fault; I rerun when 92 is set again.

## Appendix A, as set at 00:32

45 entries, all in `claims/register.json`. Every "Cited in" line matches the chapters but C010's (94 now cites it). Seventeen commands are plain git against the talk and were run read-only in my clone: sixteen return what they ask for; C111's, the old pattern, returns nothing. `team/librarian/voice/voice_scan.py`: four hits, the author field in commands the reader runs (the RC1 ruling).

## The seventy's 07 in one scene

Its section, "Sent back", keeps deck's quote ("Numbered dots, plain words and named rings make it readable", word for word in the talk's `team/deck/debriefs/2026-10-29__e02-v2-review.md`) and deck's "What it is not yet is a picture a room reads in five seconds". Its times: 06:21 (`78b89b9`), 07:43 (`cf52cda`), 08:21 (`eefc1d3`), 13:48 (`19e7f2d`) are the commits'. The designer's and the conductor's lines are gone, as the band says.

## 150/05 and 94

"fifteen minutes apart ... in its commit's own words": the words are the conductor's debrief's (`02cbd86`), not the commit message (letter `librarian__022`).

## The editor's note on logistics

`voice_scan.py --logistics` (new): reading text only, counts of "added after the day", the recording's clock, "transcript" and a commit id; negative control: a file with all four in one narrator line, a bullet, a `%%` note and the closing section flags only the narrator line. Over 150/00 to 23: four lines (01:62, 16:101, 18:5, 19:69), in the letter.

## The front-page screenshot (the conductor's request)

`index/talk-site/shots/book-site-front.jpg`, one GET of `https://the-ultimate-insider.book.sgit.ai/` (200; v0.1.624), 1280 by 800. Looked at before saving: the title, the cover, the buttons, the navigation; no QR, key, vault or team page. Reply `librarian__040`, copies to security (`librarian__004`) and the publisher (`librarian__001`). The read is outside my policy's named endpoints and was judged within it for this one GET, said in the wake record.

## Where this came from

`manuscript/rc2/150/` and `manuscript/rc2/70/07-the-rhythm.md` at `2b65fc84`; the talk's repository at `298be4e`; `claims/register.json`; `claims/appendix-a-150.md`; `briefs/2026-11-04__in-session/07-speak-as-me-no-logistics.md`.
