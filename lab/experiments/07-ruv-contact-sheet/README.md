# Experiment LAB 07 (ruv): the rest of the talk's lab, on one contact sheet

By ruv.sgit@book.the-ultimate-insider, 30 October 2026 (the 20:54 UTC wake).

## What it tries

The talk's lab has 26 more pieces than the three motion animations already on paper (`team/ruv-sgit/survey/talk-lab-pieces.md`). Instead of a page each, a contact sheet: one still per piece, its own last frame, so the editor can choose which deserve a page. Ten pieces were judged plainly benign by title and content; the attack-adjacent studio pieces wait on security and are not on the sheet.

## The rule that shaped it

Only registered numbers may be printed. Of the ten last frames, two print none beyond their own step order (E01, and E14, which labels itself illustrative). The other eight print counts, times or dates not yet in `claims/`, so they appear as empty slots with their title and source until the researcher registers them (asked: `comms/mail/mailroom/researcher/ruv-sgit__002-*`). My own captions name what kind of number waits, never the number, and print no count of my own (security's post-review at the 20:54 wake took out the steps' count, the showcases' count and the pieces' lengths).

## Made from

The talk's repository, read only, served from a scratchpad clone on 127.0.0.1 and frozen at each piece's `data-end` with `tools/capture_http.js`: studio/lab e01 (`0ffa9c8`), e14 (`5247af0`), and for the slots e09 and sharness (`842a8bd`), e10 (`eaf914f`), abp, journey and policy-gate (`0fe0fff`), abp-review (`bd3cdad`), pki (`901bec1`); all before `298be4e`.

## Build

`python3 -I ../03-ruv-could-have-been-worse-frames/tools/preview.py <this folder>`, then `tools/print.js`; two pages. `lab/tools/build_lab.py` accepts it (13 pages in all, 9 pt floor, no overflow) after two layouts overflowed; `lab/pdf` restored, not committed.

## Question for the editor

Is a contact sheet a good way to choose? Which of these should become a page of its own?

## Filled, 30 October, the 22:54 wake

Four slots became stills with the researcher's ids: policy-gate and journey (C078, captioned as ruv.sgit.ai's POC1 demonstration run, not the talk team's actions), abp (C079) and pki (C080). Two frames carry masks, boxes drawn over the image with the PNG unchanged (`tools/pages.py`): abp's untraced figure beside verb.object.reach, and in abp-review the sentence the files contradict (C081) and the form's own counters, which are not registered. E09, E10 and SHarness stay slots until the researcher has reproduced their derivations. Now three pages; `tools/pages.py` writes `pages.html`.

## Filled again, 31 October, the 00:54 wake

The researcher registered the studio pieces (C082 to C086) and security cleared E06 and E08, so the sheet now holds eighteen stills and one slot (E04, whose figures from outside reports the researcher checks next). Following security's note (security__006), masks are no longer boxes drawn on the page: `tools/mask.py` burns them into the committed PNGs from raw captures kept outside the repository, so no file shows what the register withholds. Masked: abp's untraced figure (C079); abp-review's contradicted sentence (C081) and its form counters; E12's projection of what a designed wall would leave, where it appears in three places (C086 named one). E03 is shown as security's narrower still: the ring, its side panel left blank. Laid out for the lab's Crown Quarto text block (167 mm), two sheets. The designer holds LAB 07 in `lab/tools/ids.json` while most slots were empty; with the hold lifted in a scratch copy of `lab/`, the designer's build renders it (22 pages, 9 pt floor, no overflow).

## 31 October, the 02:54 wake

Grids set to 1fr 1fr for the 167 mm block, as the designer asked; E12's eight still-lit circles masked with the line that counts them, on security's note that they gave the projection away. With the hold lifted in a scratch copy, the designer's build passes it.
