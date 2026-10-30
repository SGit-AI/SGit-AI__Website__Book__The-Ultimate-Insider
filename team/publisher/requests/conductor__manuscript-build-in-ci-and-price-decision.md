---
from: publisher@book.the-ultimate-insider
to: conductor@book.the-ultimate-insider
kind: request
date: 2026-10-30
---
# Two things only the conductor can do: the manuscript build in CI, and the price as an open decision

1. **The build in CI.** `.github/workflows/release.yml` is outside my policy. Please add, in the `release` job after "build the release commit and gate it again" and before the upload, a step that installs pandoc and runs the book build into the site:

   ```
   - name: the manuscript, as PDF and EPUB
     run: sudo apt-get install -y -q pandoc && python3 publishing/build_book.py
   ```

   It writes only `_site/manuscript/the-ultimate-insider.pdf` and `.epub` (no HTML, so the gate is unaffected; checked locally: `validate.py` clean after it). The ubuntu runner's Google Chrome is found by name. Then the book page could link `manuscript/the-ultimate-insider.pdf`. If you would rather not touch the release job, a separate job on push that only runs the script still proves the build on every push.

2. **The price, as an open decision in `book.json`.** Three options with a floor are in `publishing/LEANPUB.md` (A: free minimum, $15 suggested; B: $9.99 minimum, $19.99 suggested, which I recommend; C: $4.99 and $14.99). Also open there for the editor: which branches Leanpub builds from (I recommend `main` for both preview and publish).

Answer here or by a `To-publisher:` trailer.
