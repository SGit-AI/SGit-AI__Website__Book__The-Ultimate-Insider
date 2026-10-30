#!/usr/bin/env bash
# Rebuild experiment 02 (ruv): sample M01 from a read-only clone of the talk's repository, draw the strip, print the preview.
# Usage: tools/make.sh <path to a clone of SGit-AI__Website__Presentation__The-Ultimate-Insider>
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"; talk="$1"
node "$here/tools/sample.js" "$talk/src/static/motion/lab/the-building/v1/index.html" "$here/paths.raw.json"
python3 -I -c "import json,sys;d=json.load(open(sys.argv[1]))
for k in ('people','agents'): d[k]=[[{'t':p['t'],'x':round(p['x']),'y':round(p['y']),'red':p['red']} for p in f] for f in d[k]]
json.dump(d,open(sys.argv[2],'w'),separators=(',',':'))" "$here/paths.raw.json" "$here/paths.json"; rm "$here/paths.raw.json"
python3 -I "$here/tools/build.py"
sed -i 's/page {n} of {N}/page 1 of 1/' "$here/page.html"
node "$here/../01-ruv-the-building-three-frames/tools/print.js" "$here/page.html" "$here/page.pdf"
(cd "$here" && sha256sum page.pdf long.svg paths.json > SHA256SUMS)
