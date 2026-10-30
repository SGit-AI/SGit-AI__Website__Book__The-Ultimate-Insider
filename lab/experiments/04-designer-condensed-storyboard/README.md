# LAB 04: the condensed storyboard

By designer@book.the-ultimate-insider, 30 October 2026: the brief's experiment 3 (`team/conductor/projects/pdf-lab/README.md`: "B01's storyboard, a quarter of its size: frames, words and cost in a strip that fits half a page").

**What it tries.** The whole of B01's storyboard (eight frames, the talk's "the overlap fills in") as a four-by-two strip in the top half of a page, each frame with its number, beat and time, and the first line of its words; the cost in one line under it. A second page shows one frame as the storyboard gives it, so the editor can judge what the strip gives up.

**What it is made from.** `src/static/studio/lab/b01/storyboard/index.html` at `ecdcdf9` in the talk's repository (unchanged at `298be4e`), made by ruv.sgit on the day; read only from a clone. The frames are drawn by the page's own script: each was rendered in Chromium in the page's light theme and saved as `frames/b01-frame-<n>.jpg`, and its words, beat, time and cost read from the rendered page. Nothing is redrawn and no word is new except the first-line cut (marked "...") and the cost line, which restates the storyboard's own table.

**The numbers.** Only the storyboard's own times (the talk's clock, and the act openers' 3 s), none from the day.

**The question for the editor.** Does the strip carry the story without the motion and the notes? Is a frame this small readable on paper? Does the book want strips like this beside its chapters?

**A rule it tests.** At this size the labels drawn inside each frame are well under the lab's 9 pt floor. The build checks only the page's own text, not text inside an image, so it cannot catch this; the page says so, and the editor's verdict decides whether a reduced source image may carry text below the floor.
