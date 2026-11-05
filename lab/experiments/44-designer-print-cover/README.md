# LAB 44: the covers for upload

    python3 lab/experiments/44-designer-print-cover/make_print_cover.py [--pages 129] [--paper white]

- `kdp-full-cover-<pages>-<paper>.pdf`: KDP's full cover, back, spine and front with 0.125 in bleed, at the exact size
  `publishing/cover_size.py` gives (its page box set exactly; Chromium alone rounds it). The file to upload.
- `kdp-full-cover-<pages>-<paper>.svg`: the same, as drawn. `-guides.svg` and `-guides-preview.png` add the trim, the
  spine folds, the safe area and KDP's barcode box, for checking only.
- `leanpub-cover-1800x2700.png` (and its `.svg`): Leanpub's one cover image, cover A drawn taller.

At the final page count, run it again with `--pages`: only the spine and the cover's width move. The publisher checks
the files against KDP's rules (publishing/KDP.md); the editor uploads them by hand.
