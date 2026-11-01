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

None reserved is left; the header is `experiment.proposed.json` and the lab build leaves this out until the designer names an id. In a scratch copy given a temporary id, the designer's build passes it.

## Questions for the editor

Does a strip of the cast tell the hold better than a timeline? Should the scenes be this short, or longer, with more voices?

## Checked (1 November 2026)

The researcher checked the strip against the register (`claims/the-hold-strip-check.md`): it holds. One phrase changed at their note: the 95 percent is now given as the hold's own reason (C006), since the editor has given other accounts since (C089, still open, so not cited).
