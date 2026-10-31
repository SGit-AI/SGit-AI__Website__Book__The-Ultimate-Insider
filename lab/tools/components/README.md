# The component toolkit

Code that draws the book's recurring visuals from data, in the lab's language, so a figure is changed by changing its data, not redrawn. Task A12 of the editor's RC1 review (31 October 2026). Kept by designer@book.the-ultimate-insider; ruv.sgit and the developer are welcome to propose components by letter.

Every component: a JSON spec in, an SVG out, one SVG unit to the millimetre, text at 9 pt at the size it is drawn, the lab's palette, one accent at most, and only registered numbers and times (`claims/register.json`), each with its claim id. Each has an example page in the lab PDF.

| Component | Modes | Example page | Use on a lab page |
|---|---|---|---|
| `timeline.py` | horizontal, vertical | LAB 09 | `{{timeline:<spec from lab/>:<mode>:<length mm>}}` |

Proposed next: a small Wardley map with side notes (T8), a counter strip (a row of registered numbers), a before-and-after panel (LAB 08's form).
