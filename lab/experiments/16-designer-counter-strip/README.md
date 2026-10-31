# LAB 16: a component toolkit, the counter strip

By designer@book.the-ultimate-insider, 31 October 2026: issue 013, the toolkit's second component (the first is the timeline, LAB 09).

**What it tries.** `lab/tools/components/counters.py` draws a row of numbers from a JSON file: each 28 pt, its words at 9 pt wrapped to the tile, its claim id beneath; one may carry the accent. Shown at three widths: the text block, the main column, and the rail, where the tiles wrap one per row because a tile is never narrower than 28 mm (the first draft let them crowd; a look at the page caught it).

**What it is made from.** Four checked claims (`claims/register.json`: C002, C009, C022, C024). C011 (nine staffed members) is left out because the register marks it open.

**The question for the editor.** Do counts read better as a strip than in the text? Is one number in the accent enough emphasis?
