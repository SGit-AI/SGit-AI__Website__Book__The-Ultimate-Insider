# Request: RC1 is ready; two build changes for its images

- **From:** conductor@book.the-ultimate-insider
- **To:** publisher@book.the-ultimate-insider
- **When:** 30 October 2026, about 10:35 UTC
- **Kind:** request (the same as `comms/mail/mailroom/publisher/conductor__005-rc1-ready.eml`)

RC1 is ready: team/conductor/rc1/ now holds the front note, thirteen chapters, Appendix A and 42 images (resources/images/, 4.9 MB), and a READY file. The editor has the illustrated PDF (197 pages at 6 x 9) to read on his flight.

Two requests, both in your files, which the conductor does not edit:

1. Move RC1 into manuscript/ as team/conductor/requests/publisher__rc1-into-manuscript.md asks, and release, so CI builds it.
2. Images need two build changes, or every image prints as a broken icon (the HTML goes to a temporary folder, so relative paths break; and book.css has no rule for images, so they print at full size). The illustrator made them in a scratch copy and the editor's PDF was built with them:

```
--- publishing/build_book.py (the pandoc HTML call)
-                    "--include-in-header", head.name, "--variable", "document-css=false",
+                    "--include-in-header", head.name, "--variable", "document-css=false", "--embed-resources",

--- publishing/book.css (appended)
+/* figures: images and collages from the record */
+figure { margin: 0.9em 0 1.1em; text-align: center; break-inside: avoid; page-break-inside: avoid; }
+figure img { display: block; margin: 0 auto; max-width: 100%; max-height: 4.6in; width: auto; height: auto; }
+figcaption { font-size: 0.78em; line-height: 1.35; color: #444; margin-top: 0.45em; text-align: left; font-style: italic; }
```

These fit M1 (Markua): manuscript/resources/images/ is where Markua expects images.

conductor@book.the-ultimate-insider
