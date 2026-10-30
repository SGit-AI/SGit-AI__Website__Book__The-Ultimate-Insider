# SYNTHETIC READER: the CISO, run 20261030T1750Z

**A test instrument, never a reader.** This persona is fictional (`review/synthetic/personas.json`, `ciso`); its review is a prompt for the team, never evidence about the book, never counted as readership. Written by synthetic@book.the-ultimate-insider from what the run measured (`observations.json`) and saw (the four screenshots), on `/review/ciso.html` built locally from the developer's `review/tools/make_review.py` at dev `ddfa4bc` (the page is not on the site yet). Device: Desktop Chrome, 1280 by 720. The run read the page's structure and its first chapter's opening; it did not read all three chapters.

## In its own voice

The first screen did its job. Inside thirty seconds I knew who was asking, why me ("if the controls in these chapters would not survive your audit committee"), what was asked and by when, and what I would get back. I liked that it told me it was a prototype with fictional data before anything else: that is the sentence I look for and rarely find.

"How this works" is the part I would show my own team. It says what stays in my browser, what the anchor is for, and it admits the one call the page makes: the site's top bar asking GitHub for its star count. Credit for saying so. But I opened a page meant for me and my browser told a third party; I would rather the review page made no outside call at all than explain the one it makes.

The pen is good: one click on a paragraph, five marks, a line, Keep. It did not get in the way of reading. Comments stay in local storage and leave as a file I save myself; the sealing to the editor's key is promised as "next". Until it is built I would not send anything I would mind being forwarded.

Two things would cost you my time. You ask for about 52 minutes and I gave you 40: tell me which of the three chapters to read first if I only have half an hour. And the questions are placeholders (four across three chapters, one chapter with only one); the ones I care about, "which controls could I adopt on Monday, which need budget", are not asked yet.

## Scores (1 to 5)

| Axis | Score | Why |
|---|---|---|
| Got the answer | 3 | The right chapters for "do the controls hold up" (a mandate, the editor signs, the team was the insider), but 52 minutes against a 40-minute budget and no "read this one first". |
| Clarity | 4 | Who, why, what and by when on the first screen; the prototype banner plain; the pen self-evident. |
| Trust | 3 | Honest about everything, including the one outside request; but the request still happens, and sealing is not built yet. |
| Design | 4 | A calm column, a side panel that stays out of the way, a pen that sits under the paragraph; 43 screens on one page is long, with no sense of progress. |
| Navigation | 4 | The three chapters are linked from the top; no way back to the top or to "Sending it back" from inside a chapter. |

## What the run measured

- HTTP 200 in 127 ms; no failed local request; one console error, the blocked star-count request.
- 130 anchored blocks (`data-a`), every chapter paragraph among them; 114 of 132 visible paragraphs carry their own id (the 18 without are the letter and the panel, outside the chapters).
- Smallest paragraph type 12 px (the panel); no horizontal overflow; about 12,300 words over 43 screens.
- One click on the first anchored paragraph opened the pen (`4-pen.jpg`). Four question boxes (chapter 3: one, chapter 6: one, chapter 9: two).
- Blocked: `https://api.github.com/repos/SGit-AI/SGit-AI__Website__Book__The-Ultimate-Insider`, from `theme.js`. Nothing else tried to leave.
