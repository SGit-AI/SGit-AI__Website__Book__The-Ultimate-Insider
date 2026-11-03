# RC2, the 30-page edition, the pages: layout and pictures, read by three readers

**SYNTHETIC READERS: test instruments, never readers. A look at a first-draft PDF.** By synthetic@book.the-ultimate-insider, 3 November 2026, at the conductor's ask (conductor__024: the editor wants it tightened, the missing pictures in, nothing too tight). The 32-page draft PDF of the thirty, built from dev with the publisher's own command, viewed page by page as images by the three readers the editor named. Reader by reader in this folder.

**The build on dev fails as it stands.** The writer's new player Figure line in chapter 1 makes four Figure lines to the figures list's three drawings, and `build_book.py` refuses. For this read I built it with a scratch copy of the list holding a gap for the new line; `publishing/` is unchanged.

## The answers

| Reader | Would pick it up | Pictures missing | Too tight |
|---|---|---|---|
| Conference team member | yes | 10 | 13 |
| Newsroom builder | yes | 10 | 8 |
| First-build finisher | maybe | 10 | 10 |

As they flip it: a confident cover with the cast on it, a lively book inside, and dashed "Figure to come" boxes that make the back half feel unfinished.

## What works

- **One head per run of a speaker:** followable for all three, and the moods in brackets are "the cheeky part I liked" (the newsroom builder).
- **The "Words on this page" boxes:** all three say they help, landing just where a word is first needed; the first-build finisher says they help them most.
- **Pictures named by all three:** the slide and the speaker (page 4), the clock dial with the five steps (12; "the best picture in the book" for the first-build finisher), the first wake with the 162 (13), the wakes by hour with the empty chair (15), the relayed word at studio's door (19), the 82 seconds and the HOLD file (22), the cards of what did not work (24).

## What is missing: the same ten for all three

1. Pages 4 to 5: **the talk's player**, which chapter 1 describes; a dashed box, split across the page break. The screenshot the line names is in the repository (`index/talk-site/shots/talk__player.jpg`); the build places only an .svg under `lab/`.
2. Page 11: **the map** the text asks the reader to look at first.
3. Page 18: the map of the day, who was on stage when.
4. Page 23: the three speech cards, the editor's three accounts of why he stopped.
5. Page 27: the nine cast cards turning into folders of files.
6. Page 28: this book's team as cast cards.
7. and 8. Page 29: the two cards from this book's record; three people, each with a small factory, joined by one brief, board and hold.
9. Page 30: the map of one project's parts carried forward ("Map to come").
10. Page 31: the five steps as a path.

## What is too tight, or too empty

- **Card rows past the right margin, the last card cut:** pages 7, 10, 23 and 25, for all three (checked on pages 7 and 23).
- **Crowded:** pages 17 and 28 (many speaker runs, little air), 24 for two; the "Do this now" line hard against the narrator's on page 14.
- **Near-empty pages carrying only a source note:** 8, 20 and 26 for all three, 14 for two, and 32 two-thirds blank.
- **Contents (page 3):** no heading and no page numbers (checked).

One more, mine, not the readers': on page 7 the caption under the cast cards is the Figure line's brief to the designer ("each with its job in one line ... drawn not yet lit"), printed as the caption.

## For the publisher and the designer, in order

1. The player on pages 4 to 5: place the existing screenshot (or a drawing of it), and never let a placeholder split across a page.
2. The map on page 11, then the other eight pictures.
3. Card rows and strips inside the right margin (7, 10, 23, 25).
4. Source notes kept with their chapter, not alone on a near-empty page (8, 20, 26).
5. Contents with a heading and page numbers; captions that read as captions, not briefs.

## Limits

Three fictional readers voiced by one session's sub-agents, looking at 80 dpi page images of a draft; the clock in the margin is hidden for now and was not marked missing. Built from dev at `ec33a751`.
