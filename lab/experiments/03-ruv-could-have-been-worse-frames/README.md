# Experiment LAB 05 (ruv): it could have been much worse, in two frames

By ruv.sgit@book.the-ultimate-insider, 30 October 2026. The lab's experiment 1 ("An animation as three frames") on the talk's second animation, made only after security said it could be (comms/mail/ruv-sgit/done/security__003-m02-before-you-make-it.eml).

## What it tries

The talk's M02 in two stills frozen on its own clock: at 11.5 s, the first incident alone (what the way in could have reached, what happened); at 32 s, the still, both incidents side by side and the line the room was left with. Two frames, not three: the still holds everything the third would.

## What it is made from

- M02 v1, `src/static/motion/lab/could-have-been-worse/v1/index.html` in the talk's repository at `f45028c` (unchanged at `298be4e`), read only; frozen with `?t=` and `?theme=light` by `tools/capture_http.js`, served from a scratchpad clone on 127.0.0.1.
- Its two public sources, as it names them: Microsoft MSRC, 19 January 2024; AWS security bulletin AWS-2025-015.

## Security's three conditions, kept

1. Only those two sources, named and dated as M02 names them; nothing added of how either incident worked.
2. The caption keeps the reading apart from the report: "Two public incidents, as their vendors reported them. 'What was possible' is the talk's reading; 'what happened' is the vendor's." (security's words).
3. No number from outside the register: the page has none but the times on the animation's clock, the source's date and the bulletin's id.

## Build

`python3 -I tools/preview.py <this folder>` sets `pages.html` as the lab would (the designer's `lab/tools` at `f212c8e`, read only), then `node tools/print.js` prints `page.pdf`. `lab/tools/build_lab.py` accepts it (9 pages with LAB 05 at the time, all text at 9 pt or more, no overflow); `lab/pdf/` is the designer's and was not committed. `SHA256SUMS` holds the hashes.

## Questions for the editor

Does the contrast read without the motion? Is the still alone enough?

## Its id

First declared LAB 04, which the designer's condensed storyboard had already printed; then LAB 06 for a wake; now LAB 05, the id the lab PDF prints it under (lab/tools/ids.json; an id once printed is never reused, lab/README.md). The designer owns the numbering.
