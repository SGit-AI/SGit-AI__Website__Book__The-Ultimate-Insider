# Experiment (ruv, id to be named): the cast in strips

By ruv.sgit@book.the-ultimate-insider, 1 November 2026 (the wake of 00:54 London, 00:54 UTC), for the editor's CH1 ("imagine that each one is a character and persona in this book ... use them to help explaining the story") and NR1 (the book told by its cast), routed by the conductor (`conductor__008`, `conductor__009`).

## What it tries

One moment of the talk's day told by its characters as a strip: the hold at 18:44, told by the conductor at ninety-five and by the hold itself. Three panels, a "dramatised" band naming the moment and its claims, and nothing else on the page.

## The rules it keeps

- **The words are the storyteller's.** Every line is quoted word for word from the storyteller's letters to the designer (`storyteller__005-the-casts-first-lines.eml`, `storyteller__020-the-conductors-poses.eml`); this member writes no line.
- **The drawings are the designer's**, referenced in place in `lab/characters/` (read only).
- **Dramatised, and marked**; the moment rests on C006 (the hold) and C065 (the work in flight still landing 82 seconds later), and the failure stays in.
- **No number in a bubble**, no line over the cast's 90 characters: `tools/strip.py` refuses both.
- **No real person drawn**; security is not used, because the talk's security member was proposed and never staffed.

## The tool, for what comes next

`python3 -B -I tools/strip.py scripts/<name>.json ...` sets any script as a strip, one sheet per script. A script names its title, moment, claims, and panels (who, drawing, pose, line, source). A panel whose drawing does not exist yet is set as a dashed placeholder. The NR1 interview and therapy session will be set from the storyteller's scripts when they come (asked: `ruv-sgit__001` to the storyteller, copied to the historian).

## Its id

LAB 28, reserved by the designer (`designer__050`) and declared in `experiment.json` on 1 November 2026 (the 04:54 wake); before that the header was `experiment.proposed.json`. The folder's number is only its place in this member's list.

## Questions for the editor

Does a strip of the cast tell the hold better than a timeline? Should the scenes be this short, or longer, with more voices?

## Checked (1 November 2026)

The researcher checked the strip against the register (`claims/the-hold-strip-check.md`): it holds. One phrase changed at their note: the 95 percent is now given as the hold's own reason (C006), since the editor has given other accounts since (C089, still open, so not cited).

## Round 2 (1 November 2026, the 08:54 wake)

The designer kept it, with one note: its second page held only the dramatised note and the sources. The drawings are now 19 mm wide, the panels tighter, the line sources folded into the dramatised note (each line's exact place stays in `scripts/the-hold.json`), and the header's "tries" one line shorter; in a scratch copy of the designer's build the strip holds one page. The characters' words and the moment are unchanged.

## Round 3: the two NR1 scenes (2 November 2026, the wake of 03:44 UTC)

The storyteller wrote two scripts on the historian's record (`storyteller__026`; `chapter-plan/cast/scripts/` at `6452450`): an interview, the researcher and the deck on the claims that did not hold and the out-of-date figure on the definition slide (C029 to C031); and a therapy session, the conductor after the hold, talking to security's empty chair (C006, C021, C024, C065, C089). Both are copied word for word into `scripts/` and set as the second and third sheets. The bands are the storyteller's; every number in them is in the register (C031 holds the freeze at 02:47 and the correction five minutes later; C021 the 95 percent; C065 the 82 seconds). C089 is open by design and sits beside the checked C021.

The tool now reads the storyteller's format beside its own. Poses map to the drawings that exist: the designer's four moods (proud as happy, pacing as stressed), and the conductor's named poses to the designer's own drawings (at ninety-five as `conductor-alarmed.svg`, on the minute as `conductor-calm.svg`). The empty chair is an empty dashed frame with no bubble. At security's note (`security__013`), pose names are no longer printed or put in the image text, and number words (two and up) are refused in a bubble or the alt text as well as digits; "one", as the storyteller uses it, passes.
