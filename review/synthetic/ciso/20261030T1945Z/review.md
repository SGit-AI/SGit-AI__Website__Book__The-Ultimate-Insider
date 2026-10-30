# SYNTHETIC READER: the CISO, run 20261030T1945Z

**A test instrument, never a reader.** This persona is fictional (`review/synthetic/personas.json`, `ciso`); its review is a prompt for the team, never evidence about the book, never counted as readership. Written by synthetic@book.the-ultimate-insider from what the run measured (`observations.json`) and saw (the screenshots), on `/review/ciso.html` as built from dev at `4dc4248` (the page is now a site page). Device: Desktop Chrome, 1280 by 720, the persona's own; plus a check on a 390-wide phone in `phone-check/`, which is the same persona on another device, not a second persona. The run read the page's structure and the first chapter's opening, not all three chapters.

## In its own voice

You fixed the thing I minded most. The page now asks nobody but its own site for anything, and the "How this works" line says so: "the site's scripts ask no third party on review pages". That is the sentence I wanted, and the run checked it rather than taking it on trust.

The bar at the foot of the screen, "Chapters" and "Send it back", is what a 43-screen page needed. I could stop in the middle of chapter 6 and get to my comments without scrolling.

What is still open is not the developer's to fix: 52 minutes asked of my 40, and four placeholder questions, one of them for a whole chapter. I would still like to be told which chapter to read first if I only have half an hour.

One new thing, on a phone: when I opened the pen on the last lines of the screen, the new bar sat on top of Keep and Cancel. A tap there would have taken me to the chapter list and lost my mark.

## Scores (1 to 5)

| Axis | Score | Since 20261030T1750Z | Why |
|---|---|---|---|
| Got the answer | 3 | same | The right three chapters; still 52 minutes against a 40-minute budget, with no "read this one first". |
| Clarity | 4 | same | Who, why, what and by when on the first screen; the prototype banner plain. |
| Trust | 4 | up from 3 | No request leaves for any other host, checked; sealing to the editor's key is still "next". |
| Design | 4 | same | A calm column and a pen under the paragraph; on a 390-wide phone the bar can cover the pen's buttons. |
| Navigation | 5 | up from 4 | Chapters and Send it back from anywhere on the page. |

## What the run measured

- Desktop: HTTP 200 in 412 ms; no console error; no request blocked, because none tried to leave.
- 130 anchored blocks; four question boxes, as before; smallest paragraph type 12 px (the panel); no horizontal overflow on either device.
- `nav.rv-jump`: fixed, visible, two links, "Chapters" to `#intro` and "Send it back" to `#send`.
- One click on the first anchored paragraph opened the pen on both devices.
- Phone check (iPhone 13, 390 by 664): with the pen opened on the first chapter's first paragraph, a hit test at the centre of Keep and of Cancel landed on the jump bar. The same test on a Pixel 7 (412 wide) and on the desktop found every pen control clear. A scripted click on Keep still worked, because the test tool scrolls a button clear before clicking; a thumb does not.
