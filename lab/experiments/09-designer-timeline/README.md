# LAB 09: a component toolkit, the timeline

By designer@book.the-ultimate-insider, 31 October 2026: task A12 of the editor's RC1 review (`team/conductor/rc1/editor-review/notes.json`; `comms/mail/mailroom/designer/conductor__008-rc1-review-5-to-9.eml`): "a reusable component toolkit for the book's visuals, timelines first: code fed by JSON, several modes (horizontal, vertical), an example page per component".

**What it tries.** `lab/tools/components/timeline.py` turns a JSON file of events into an SVG in the lab's language. Two modes, horizontal and vertical. Times are to scale; a gap longer than the spec's `break_after_minutes` is drawn as a marked break, never silently squeezed (RC1's design round, point 2). Labels that would collide stack on further levels with a leader line. One event may carry the accent. Text is 9 pt at the size it is drawn.

**What it is made from.** Seven registered times (`claims/register.json`: C001, C012, C028, C013, C018, C006, C005) in `lab/tools/components/examples/the-day.json`.

**How it is used.** On a lab page: `{{timeline:<spec from lab/>:<horizontal|vertical>:<length in mm>}}`. From the command line, for the book or the site: `python3 lab/tools/components/timeline.py <spec.json> [mode] [length]`.

**The question for the editor.** Is a timeline to scale, with the night as a marked break, clearer than one spaced evenly? Which component next (proposed: a map with side notes, a counter strip, a before-and-after panel from LAB 08)?
