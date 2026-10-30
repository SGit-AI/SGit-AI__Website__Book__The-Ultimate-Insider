# RC1 infographics and call-outs: first design pass

30 infographics (`jpg/`, from the sources in `svg/`) and 50 call-outs for the conductor to place in the RC1 chapters. Nothing here edits a chapter: `manifest.json` and `callouts.json` say where each piece goes, by an anchor sentence copied verbatim from the chapter (each checked to occur exactly once).

## The visual language

- **Palette.** Dark ink `#1f2933` for text and primary marks; one accent, rust `#b0481a`, for the one thing to see first (the hold, the stale figure, the boundary); light fills `#eef2f6` and `#d5dce4` for boxes; a pale accent tint `#f6e1d4` for the emphasised box; white paper. In greyscale the accent prints as a mid-dark grey, distinct from both ink and fills.
- **Type.** System sans (Inter where present, then Helvetica, Arial, DejaVu Sans); a monospace for file and path names. Bold for titles and the number that matters, regular for explanation, muted grey for secondary lines. No text is set smaller than about 9pt at the placed size: 42 px on a horizontal (1600 x 700, placed 4.75 in wide), 28 px on a vertical (700 x 1400, placed about 6.5 in tall), 44 px on a tile (800 x 800, placed about 2.25 in wide). The generator refuses anything smaller.
- **Shapes.** Every image opens with a short accent rule and a title. Rounded boxes for steps and states, plain arrows for flow, a single axis for timelines, bars drawn to scale for counts. Claim ids are printed on the image itself: top right on horizontals, in the footer on verticals and tiles. Only registered times appear on the timelines.
- **Files.** JPEG at 2x (3200 x 1400, 1400 x 2800, 1600 x 1600), quality 85, all under 320 KB. Rebuild with `python3 build/make_svgs.py && NODE_PATH=/opt/node-tools/node_modules node build/render.js && python3 build/make_json.py`; the renderer checks every text against the canvas edges, against other text and against the minimum size, and the last script checks anchors, claim ids, word limits and dashes.

## How call-outs should look in print

A light tinted box (the accent tint for `warning` and `try`, the light fill for the others), a 3 pt left rule in the accent (in ink for `concept`), a small capitalised kind label above the title (CONCEPT, THE NUMBER, TAKE AWAY, WATCH OUT, TRY THIS), the title in bold, the text in the body face one size down, and the claim ids last in small muted type, as in the chapters' "(C031)". Place each after its anchor sentence's paragraph, never inside it; keep at most two per page and never two on facing columns.

## What a second design round should improve

1. **Real print proof.** Print one page of each format at size and check the 9pt floor and the greyscale contrast of the accent against the dark fills (part 2 in `ig26`, `ig29`).
2. **Timelines to scale.** `ig21` and `ig28` space events evenly; a broken scale would show the long wait between 02:52 and 14:07, and the crowding of 18:44 to 18:46, honestly.
3. **One grid.** Margins, title sizes and footers vary slightly between formats; set one grid per format and one footer style for claim ids.
4. **Tiles for the margin.** At 44 px a tile carries about 25 characters a line; the tiles are dense for a 2.25 in float. Test smaller, number-only variants.
5. **Placement against the existing photos.** Several anchors sit near screenshots (chapters 1, 4, 10); the conductor should space them so no page carries two images and a call-out.
6. **Overlap with tables.** Chapter 9's control register and chapter 12's failures table are already visual; an infographic for either was left out on purpose, and a designer may prefer to restyle the tables instead.
7. **The register moves.** Every number traces to `claims/register.json` as of 2026-10-30T11:00Z (C001 to C042). Rerun `build/make_json.py` after any register change; if a value changes, change it in `build/make_svgs.py` and rebuild.
