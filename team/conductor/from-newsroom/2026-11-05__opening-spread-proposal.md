# The opening spread: a proposal

**For:** Dinis, and through him the book team of *One Human, Nine Agents, Nineteen Hours*.
**From:** the newsroom journalist, 5 November 2026.
**With:** `opening-spread-mockup.pdf` (two pages at the book's trim, Crown Quarto 7.44 by 9.69 in) and PNGs of each page.

## What is wrong with the current opening (RC2, pages 2 to 5)

- **It opens with instructions, not a reason.** "If you only read one page, read this one" and a five-step formula ask the reader to act before they know why they should care.
- **It undersells the cast.** The nine agents, the book's strongest visual asset, appear as nine lines of text on page 4. The cover has them; the opening drops them.
- **It offers a shortcut.** "The short way: part five first, then back to the start" tells the reader the middle can be skipped. The book is a story and should be read in order.
- **Two pages of navigation before the first sentence of the story.** The formula belongs in chapter 23, the five parts in one short list, and the timeline strip (page 5) is a lot of white space for one line.
- **There is no "who I am".** A reader picking it up on Leanpub does not know who Dinis is, what the talk was, or why the day matters.

## What the spread does instead

Two pages that could be published on their own and make someone want the book.

**Page 1, the hook, in his voice.**

- A headline: *Nineteen hours. Nine agents. One talk.*
- **Narrator.** "Hi, I am Dinis Cruz", marked with the narrator figure and label used on every other page, and a closing line saying that throughout the book he is the Narrator. Then the talk, the empty folder after midnight, what it became by the evening, the agents working while he was away, and the stop a quarter of an hour before he walked on stage.
- Why the book exists: the workflow is the part he most wants to show, because the reader can build one too.
- **The cast, big:** all nine as drawn by the book's designer, each saying hello in a line, and security's empty chair, greyed.
- One line on how the book is told: the agents on the day, him from now, every scene resting on the record.

**Page 2, the proof and the path.**

- Four numbers: 00:16, an empty project; 19:00, on stage; 162 work sessions, each recorded; 1 file that could stop them all.
- **What the factory made:** three images: the talk's own home page with its title, a slide (an agent is a reasoning engine in a loop), and the grid of 58 slides, each a web page.
- **The house,** the designer's drawing of the team's repository with every agent in its room, beside two more images: the page where Dinis approved each agent's policy, and the night log, hour by hour.
- **The story in five parts,** one line each, in order, ending: "Read it in order. It is a story, and it ends with yours."
- **An invitation, not a disclaimer:** "We would love to hear from you", with where to write (GitHub issues, LinkedIn, the address as book.json FB2 gives it) and the companion site. No "draft": this page goes into the printed book.

## What moves elsewhere

- **The five-step formula** goes to chapter 23 only (it is already there in full), or to a one-page card at the very end.
- **"The book as a map" and the two routes** are cut; the five parts on page 2 replace them.
- **"Zero to presentation"** (page 5) folds into page 2's four numbers.
- **"Who is telling this story"** stays where it is, right after the spread, now shorter, since the spread already introduces him and the cast.

## Facts in the spread, and where they come from

| In the spread | Source |
|---|---|
| 29 October 2026, a talk in London called The Ultimate Insider | the book's own introduction |
| An empty project after midnight (00:16) | the book: the empty repository at 00:16 |
| On stage at 19:00 | the book: the talk was due as hour nineteen ended |
| 58 slides, a player | the talk's player ("58 slides") |
| Nine agents; security planned and never staffed | the book's cast and chapter 6 |
| 162 work sessions, each recorded | the researcher's register (162 wake records) |
| The stop a quarter of an hour before the talk | the hold at 18:44 |

*Check:* "while I was away" follows the book's own line that the record does not say where he went. "The workflow behind it is the part I most want to show you" is his to confirm.

## Assets used

- Cast drawings: `lab/characters/cast/*-happy.svg` (security: `security-worried.svg`, greyed); the narrator: `narrator-happy.svg`.
- The house: `lab/experiments/47-designer-the-house/the-house.svg`.
- Screenshots, cropped: `index/talk-site/shots/index.jpg`, `talk__slides__loop.jpg`, `talk.jpg`, `studio-ports__abp-review__masked.jpg`, `articles__the-night-hour-by-hour.jpg`.

The mock-up is HTML rendered to PDF; the book team's designer should rebuild it in the book's own pipeline and type, not paste it in.
