#!/usr/bin/env bash
# Rebuild experiment 01 (ruv): capture M01's three frames from a read-only clone of the talk's repository, then print page.html to page.pdf.
# Usage: tools/make.sh <path to a clone of SGit-AI__Website__Presentation__The-Ultimate-Insider>
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"; talk="$1"
node "$here/tools/capture.js" "$talk/src/static/motion/lab/the-building/v1/index.html" "$here/frames" light '22.5 30 43'
node "$here/tools/print.js" "$here/page.html" "$here/page.pdf"
(cd "$here" && sha256sum page.pdf frames/*.png > SHA256SUMS)
