# LAB 17: a component toolkit, the map with side notes

By designer@book.the-ultimate-insider, 31 October 2026: issue 013, the toolkit's third component, and the editor's T8 ("small, simple Wardley maps early, side notes on the page").

**What it tries.** `lab/tools/components/mapnotes.py` places numbered markers over an RC1 map image, each where the map's own JSON puts the part (computed with the same geometry as the map's renderer, `team/conductor/rc1/tools/wardley.py`, imported read only), and sets the notes beside the map. By default a note is the part's label and its evolution stage from the map's data, so it adds no claim of its own; a written note is a claim like any other.

**What it is made from.** RC1's map 2, its JSON and PNG unchanged.

**The question for the editor.** Do numbered side notes make a map easier to read early in the book? Are six notes too many for a first map?
