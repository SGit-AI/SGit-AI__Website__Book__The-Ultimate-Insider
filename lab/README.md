# The PDF lab: visual language

The rules every page of the lab PDF (`lab/pdf/the-ultimate-insider-lab.pdf`) follows. Kept by designer@book.the-ultimate-insider; the project's brief is `team/conductor/projects/pdf-lab/README.md` (book.json X1). Started on 30 October 2026 from RC1's visual language (`team/conductor/rc1/infographics/README.md`), keeping its palette and its 9 pt floor and taking up three of its seven points for a second round: one grid (point 3), greyscale proof (point 1), and number-only tiles for the margin (point 4). Experiment 01 shows every rule on paper; what the editor signs there becomes a rule here, and what he signs for the book goes to the publisher as a request.

## The page

- **A4 portrait**, printed at home on one side. Margins 16 mm all round; the text block is 178 x 265 mm.
- **Twelve columns**, 4 mm gutters (each column about 11.2 mm). The **main column** is columns 1 to 9 (131 mm); the **margin rail** is columns 10 to 12 (43 mm), for the cast, a tile, or a short note. A figure may span all twelve.
- **A 4 mm baseline**: body leading 14 pt is close to it; spacing between blocks is a multiple of 4 mm.
- **Every page has the one footer**: on the left `The ultimate insider · lab · first round`, in the middle the experiment's id (`LAB 01`), on the right `page n of N`; claim ids used on the page sit above the footer, right-aligned, in the muted ink. No other running text.

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

`python3 lab/tools/build_lab.py` assembles `lab/experiments/*/` in order (leaving out, and naming, any without an `experiment.json`: those wait for the design verdict) (a cover, then each experiment's header and pages) into one HTML file, renders it with Chromium (`lab/tools/render.mjs`), and refuses the result when any text is under 9 pt, any page's content overflows its page, or the page count differs from the cover's plus the sum of the experiments' declared `pages`. It writes `lab/pdf/SHA256SUMS`. An experiment is `lab/experiments/<nn>-<member>-<slug>/` with `experiment.json` (id, title, tries, made_from, question, pages), `README.md`, and `pages.html` (one `<section class="page">` per page; images beside it).

**Another member's experiment** goes in either in the lab's format (its own `experiment.json` and `pages.html`), or, until then, set by the designer: its header in `lab/tools/external.json` and its pages in `lab/tools/layouts/`, its folder only read. A source image from the talk keeps its own colours and is cropped, not redrawn; the caption says so. (30 October 2026: ruv.sgit's three frames, LAB 02.)

**Debriefs** are not experiments: they use the lab's language and checks (`lab/tools/render.mjs`) but are built by `lab/tools/debrief/build_debrief.py <name>` from `lab/tools/debrief/<name>.json`, into `lab/pdf/<name>-debrief.pdf`. `lab/pdf/SHA256SUMS` holds one line per PDF; each build replaces only its own line. The first: the talk's site (30 October 2026).

**Ids.** An experiment prints under the id its folder declares, unless `lab/tools/ids.json` gives it another, and an id once printed is never reused, because the editor may already hold that page on paper. The build refuses two experiments with one id. (30 October 2026: LAB 04 was printed first as the condensed storyboard, so ruv.sgit's M02 and M03 print as LAB 05 and LAB 06.)
