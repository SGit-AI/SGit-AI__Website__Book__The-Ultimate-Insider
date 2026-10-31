# The PDF lab: visual language

The rules every page of the lab PDF (`lab/pdf/the-ultimate-insider-lab.pdf`) follows. Kept by designer@book.the-ultimate-insider; the project's brief is `team/conductor/projects/pdf-lab/README.md` (book.json X1). Started on 30 October 2026 from RC1's visual language (`team/conductor/rc1/infographics/README.md`), keeping its palette and its 9 pt floor and taking up three of its seven points for a second round: one grid (point 3), greyscale proof (point 1), and number-only tiles for the margin (point 4). Experiment 01 shows every rule on paper; what the editor signs there becomes a rule here, and what he signs for the book goes to the publisher as a request.

## The page

- **Crown Quarto, 7.44 x 9.69 in**, the book's own trim (the editor, 31 October 2026, about 00:45 and 00:55 UTC: the trim, then "recreate and update ... the labs pdf with this size"). Until then the lab was A4; the A4 builds are in the history.
- **Mirrored margins**, as the book will have them: gutter 0.625 in on the inside (the editor, 31 October 2026, about 02:25 UTC: "Yes", to a gutter wider than KDP's 0.5 in minimum so nothing is lost in the spine's curve), 0.375 in outside, 0.5 in at the top, 0.625 in at the foot. The text block is about 164 x 218 mm.
- **Twelve columns**, 4 mm gutters (each column about 10.0 mm). The **main column** is columns 1 to 9 (122 mm); the **margin rail** is columns 10 to 12 (38 mm), for the cast, a tile, or a short note. A figure may span all twelve.
- **Sheets, not fixed pages.** Each `<section class="page">` an author writes starts a new page and may flow onto the next; nothing is scaled, so the type stays the lab's. A figure is never split across pages.
- **Every page has the one footer**, in the outer corner: `The ultimate insider · lab · first round · <id> · Crown Quarto 7.44 x 9.69 in`, and `page n of N` in the other; claim ids used on a sheet sit at its end, right-aligned, in the muted ink.

## Colour

| Token | Value | Use |
|---|---|---|
| ink | `#1f2933` | text, outlines, primary marks |
| muted | `#5b6670` | secondary lines, captions' source line, claim ids |
| fill | `#eef2f6` | boxes, bubbles, the experiment header |
| fill-2 | `#d5dce4` | a second level of box, bodies of the cast |
| accent | `#b0481a` | the one thing to see first on a page; at most one per figure |
| tint | `#f6e1d4` | the emphasised box, `warning` and `try` call-outs |
| paper | `#ffffff` | the page |

Every page must read in greyscale: the accent prints as a mid-dark grey, distinct from ink and from both fills, and experiment 01 prints each swatch beside its grey so the editor can check it on his printer.

## Type

One family, Inter (then Helvetica, Arial, DejaVu Sans), and a monospace (DejaVu Sans Mono) for paths, commits and ids. **Nothing below 9 pt**, footer and claim ids included; the build refuses a page with smaller text.

| Level | Size / leading | Weight |
|---|---|---|
| experiment title | 22 / 26 pt | 800 |
| heading | 14 / 18 pt | 700 |
| body | 10 / 14 pt | 400 |
| call-out text, bubble | 9.5 / 13 pt | 400 |
| caption, footer, claim ids | 9 / 12 pt | 400, muted |
| a number that matters | 28 pt, tabular | 800 |

## Figures, captions and call-outs

- A figure opens with a short accent rule and a title (as in RC1), is numbered `Fig 01.1` (experiment, then figure), and has its caption below: one bold line saying what to see, then the source by path and commit in the monospace, muted.
- Call-outs keep RC1's print style: a tinted box, a 3 pt left rule in the accent (ink for `concept`), the kind label in small capitals, the title bold, the text at 9.5 pt, the claim ids last. At most two per page.
- A **tile** in the rail carries one number at 28 pt, one line of words under it, and its claim id; no more than about 25 characters a line.
- Only registered numbers and times (`claims/register.json`) appear on a page, each with its claim id; timelines are drawn to scale, or with a marked break.

## The experiment header

The first page of each experiment opens with a header band in the fill: the id (`LAB 01`) and title, then three rows: **Tries** (one sentence), **Made from** (sources by path and commit), **The question** (what the editor answers on paper), with three boxes to tick: keep, change, drop, and a line for a note. Each experiment's `experiment.json` holds these, and the build sets them; the experiment's own pages follow.

## The cast

The characters and their rules are in `lab/characters/README.md`: agents and mechanisms only, no real person drawn, one line each, the storyteller's words.

## The build

`python3 lab/tools/build_lab.py` (at Crown Quarto, with `lab/tools/crown-quarto.css`; the cover's page counts come from a first render) assembles `lab/experiments/*/` in order (leaving out, and naming, any without an `experiment.json`: those wait for the design verdict) (a cover, then each experiment's header and pages) into one HTML file, renders it with Chromium (`lab/tools/render.mjs`), and refuses the result when any text is under 9 pt or anything runs wider than the text block. `pages` in `experiment.json` counts an experiment's sheets; at Crown Quarto a sheet may run onto a second page. It writes `lab/pdf/SHA256SUMS`. An experiment is `lab/experiments/<nn>-<member>-<slug>/` with `experiment.json` (id, title, tries, made_from, question, pages), `README.md`, and `pages.html` (one `<section class="page">` per page; images beside it).

**Another member's experiment** goes in either in the lab's format (its own `experiment.json` and `pages.html`), or, until then, set by the designer: its header in `lab/tools/external.json` and its pages in `lab/tools/layouts/`, its folder only read. A source image from the talk keeps its own colours and is cropped, not redrawn; the caption says so. (30 October 2026: ruv.sgit's three frames, LAB 02.)

**Debriefs** are not experiments: they use the lab's language and checks (`lab/tools/render.mjs`) but are built by `lab/tools/debrief/build_debrief.py <name>` from `lab/tools/debrief/<name>.json`, into `lab/pdf/<name>-debrief.pdf`. `lab/pdf/SHA256SUMS` holds one line per PDF; each build replaces only its own line. The first: the talk's site (30 October 2026).

**Ids.** `lab/tools/ids.json` keeps a ledger, `printed`: once a folder has printed under an id it keeps it, and no other folder can take it, because the editor may already hold that page on paper. A new folder prints under the id it declares if that is free, otherwise under the next free one, and the build adds it to the ledger and says so. The build refuses nothing for an id any more; it cannot collide. (31 October 2026, after three collisions in a day fixed by hand.)

**Held.** An experiment in the lab's format still waits for the designer's verdict before it prints: `held` in `lab/tools/ids.json` leaves it out, with the reason, and the build says so. (30 October 2026: ruv.sgit's contact sheet, LAB 07, until the register fills its empty slots.)

**The trim study** (31 October 2026, at the editor's word): `python3 lab/tools/trims/build_trims.py` sets the same sample pages as real book pages at KDP's 6 x 9, 7.5 x 9.25 and 8 x 10 in (mirrored margins, a 0.625 in gutter, 0.375 in outside, one full-bleed page, the lab's type unchanged) into `lab/pdf/trim-study-<trim>.pdf`. A study for the editor's choice; the book's build is the publisher's. `lab/tools/render.mjs` takes `any` for a flowing book's page count, and checks the 9 pt floor over the whole document.

**The book page: Crown Quarto** (the editor's words in the designer's session, 31 October 2026, about 00:45 UTC: "Ok, so can we go with 7.44 × 9.69 (which is Crown Quarto)"; relayed to the conductor for `book.json` and to the publisher, whose build it is). 7.44 x 9.69 in, margins gutter 0.625 in (the editor's "Yes", about 02:25 UTC; KDP's minimum is 0.5 in for 151 to 300 pages), outside 0.375 in, top 0.5 in, bottom 0.625 in with the folio outside: a text block of about 164 x 218 mm. The lab's type is unchanged. Figures for the book are drawn for 164 mm across; a rail on the outer side takes about a third of it.  The lab PDF is set at this size too, at the editor's word, so every experiment is judged at the book's own size.

**Components** (31 October 2026): `lab/tools/components/` holds code that draws recurring visuals from JSON, one example page each in the lab PDF; the first is the timeline (LAB 09). A page places one with `{{timeline:<spec>:<mode>:<length>}}`; the rest of the rules are in `lab/tools/components/README.md`.
