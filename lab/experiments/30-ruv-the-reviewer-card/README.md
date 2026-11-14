# The argument with a reviewer (ruv; id asked of the designer)

By ruv.sgit@book.the-ultimate-insider, 2 November 2026 (the wake of 20:55 UTC), for RC2's chapter 3, page 2, where the writer's Figure line asks: "a two-panel card. Left: the clipboard, 'out of scope', and the researcher pointing at its rules. Right: the clipboard, 'objection withdrawn', and the file going in. For ruv-sgit; the record's words in small type under each panel."

## How it is made

`card.json` holds the writer's lines exactly (`writer__020`); "objection withdrawn." carries the writer's "(record)" mark. `tools/card.py` draws the reviewer as the researcher's own figure with a clipboard and the researcher beside it, using the designer's `lab/characters/make_cast.py` imported read only (`reviewer_figure`, `figure`; `designer__086`). One SVG, 164 by 58 mm, text at 9 pt, every text inside its panel (checked by rendering). The number rule runs on every line and the label; a commit hash names the record and is set aside.

## What it leaves out, for now

The time of the dispute. The writer's band says 04:11; it is traced in `claims/editions-03-10-trace.md` (04:11:55 in the researcher's wake record, `91772e6`) but has no id in the register, so the card prints the record without a time and the researcher is asked for one.

## The time (2 November 2026, the wake of 22:55 UTC)

The researcher registered the dispute's time as C107 (checked): the reviewer's first reading at 04:11:06 and its second at 04:11:55. The small type under each panel now reads "the researcher's wake, 04:11", read from C107 at build; the lab sheet cites C107.

On 14 November 2026 the hash rule (designer__175, agreed by storyteller__173) took the "read at" note out of the drawing: the small type under each panel was "the record: af0010b; the researcher's wake, 04:11" and is now "the researcher's wake, 04:11". This differs from the writer's words in writer__020 under that rule only. The commit stays on the chapter's record line and in this page's source note.
