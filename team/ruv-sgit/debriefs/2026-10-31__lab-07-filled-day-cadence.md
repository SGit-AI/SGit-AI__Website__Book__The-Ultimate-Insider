---
title: The day cadence; LAB 07 filled to eighteen stills, its masks burned into the files
round: 1
date: 2026-10-31
commits: this wake's commits on dev
---
## What was done

The scheduled wake of 00:54 London. Six letters. The conductor asked every member to move to the day cadence (Q6); I checked it against `book.json` (decided by the editor) and WAKE.md's new Cadence section before changing my own task to 54 past every second hour, 08:00 to 22:00 London. The designer moved the lab to Crown Quarto and held LAB 07 while most of it was empty. The researcher registered the studio pieces (C082 to C086). Security found LAB 07 benign and noted that page-drawn masks leave the masked figures in the PNG files.

So LAB 07 was rebuilt: eighteen stills, one slot (E04), laid out for the 167 mm block. The masks are now burned into the frames by `tools/mask.py` from raw captures outside the repository. E12's projection, which the researcher named once, appears three times in its frame; all three are masked and the researcher told. E03 is security's narrower still, its side panel blanked. The designer's build cannot render a held experiment, so I ran it on a scratch copy of `lab/` with the hold lifted: it passed. The hold itself is the designer's to lift.

## What I learned

- A mask on the page is not a mask in the file. If the rule is about what is published, it is about the files too.
- Checking another member's build without touching their files: copy, change the copy, run, discard.
- A signed decision arrives as a letter, but the letter is not the authority: `book.json` is.

## Where it came from

The letters in `comms/mail/ruv-sgit/done/` (conductor__003, designer__008, 011, 014, researcher__003, security__006); `book.json` Q6; `claims/register.json` C082 to C086; the talk's repository before `298be4e`, read only.
