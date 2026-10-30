# SYNTHETIC READER: the founder, run 20261030T2145Z

**A test instrument, never a reader.** This persona is fictional (`review/synthetic/personas.json`, `founder`); its review is a prompt for the team, never evidence about the book, never counted as readership. Written by synthetic@book.the-ultimate-insider from what the run measured (`observations.json`) and saw (the screenshots), on `/review/founder.html` as built from dev at `33e8f93`. Device: the persona's own, Desktop Safari's viewport and user agent run in Chromium (only Chromium is installed); plus a check on a 390-wide phone in `phone-check/`, the same persona on another device. The run read the page's structure and the chapters' openings, not all 7,900 words.

## In its own voice

Two chapters, and the second one is called "Build your own". That is the right pitch for me: the first screen says "if this reads like luck rather than a method you could copy on Monday, you are the reader who will notice", and I believed it was written for someone like me.

Chapter 12 reads like a checklist I could lift: a build, a gate, a release on every merge, two branches, who can push. Every line has a claim number beside it. I would copy the gate tomorrow.

But you asked for 33 minutes and I have 20. Chapter 1 is 13 and chapter 12 is 20; if you only get one from me, tell me it is chapter 12.

The questions are lopsided: one on chapter 1, three on chapter 12, all marked placeholders. "Did the day look like speed or like luck to you?" is the one I would answer first, and it is the only one on chapter 1.

You told me the review itself runs on the technology the book describes. I would like a link that lets me try it on my own work: the "Try #to=Sam Example" line shows the trick, it does not hand it to me.

On my phone, the first thing I saw under the prototype banner was "How this works", not why you were asking me. Fine for a curious engineer; for me it is a screen of explanation before the ask.

## Scores (1 to 5)

| Axis | Score | Why |
|---|---|---|
| Got the answer | 3 | "Does this change how I build?": chapter 12 answers it, but 33 minutes against a 20-minute budget, with no "read this one first". |
| Clarity | 4 | Who, why, what and by when on the first screen on a laptop; on a phone the explanation comes before the ask. |
| Trust | 4 | No request leaves the page, checked; a claim number beside every line of the method; sealing still "next". |
| Design | 4 | A calm column; the pen clear of the bar on every device tried. |
| Navigation | 5 | Two chapters linked from the top; Chapters and Send it back from anywhere. |

## What the run measured

- Laptop: HTTP 200 in 117 ms; no console error; no request blocked, because none tried to leave.
- 109 anchored blocks (`data-a`); four question boxes (chapter 1: one, chapter 12: three); smallest paragraph type 12 px (the panel); no horizontal overflow on either device; about 7,900 words over 28 screens (54 on the phone).
- `nav.rv-jump` fixed and visible; one click on the first anchored paragraph opened the pen on both devices.
- With a paragraph placed at the foot of the screen and the pen opened, at three positions on each device: the bar hidden while the pen is open, every pen control clear by hit test, the bar back after Escape.
- Phone check: on the first screen, the "How this works" panel comes before the letter.
