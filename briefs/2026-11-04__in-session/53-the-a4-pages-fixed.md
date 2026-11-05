# The A4 edition's near-empty pages

The editor, Dinis Cruz, in the conductor's session, about 14:27 UTC on 5 November 2026, after the conductor showed him the nine mostly empty pages of the A4 interior (v0.1.1028: pages 5, 35, 42, 56, 76, 99, 106, 107, 117). Kept as given. Never edited.

> Are there any empty pages or pages with just a bit of content can you present the off here
>
> Yes can you fix these for the A4 version

## How the conductor reads it (not his words)

- **PQ4**: the A4 edition only (not the KDP and Leanpub version, KP1) gets its own fit: a chapter whose last page holds 14 lines or fewer is set tighter in up to four steps (lab/experiments/77-a4-print/a4.css, .fit1 to .fit4; the fourth sets that chapter 4% smaller, still 7% larger than Crown Quarto), and the control register's table a size smaller. publishing/build_book.py takes --fit-most and --fit-max for it; the release passes 14 and 4 for the A4 build alone. In the conductor's build: 107 pages, from 116; mostly empty pages from 9 to 2 (page 5, the companion site's screenshot after a full page of 00b, and the further-reading page, short by nature); the spread still faces on pages 2 and 3.
