#!/usr/bin/env python3
"""RC1's figures and call-outs, written into manuscript/ as Markua, once (the conductor's handover, first item).

The conductor's RC1 build (team/conductor/rc1/tools/assemble_rc1.py) placed the infographics, maps 6 to 16 and
the 50 call-outs at build time, so the PDF the editor reads has them and the chapters in manuscript/ do not.
This script places them the same way, with the same anchors and in the same order, but into the chapter files
themselves: images as image lines, call-outs as Markua blurbs with Markua's own classes, which
publishing/markua.py turns back into the call-out look for the team's build. Leanpub then sees what the editor
read. Reads team/conductor/rc1/ only; writes manuscript/*.md and manuscript/resources/images/infographics/.

    python3 publishing/place_rc1.py --dry-run   # counts and misses, writes nothing
    python3 publishing/place_rc1.py

Run it once, on chapters that are still RC1's: it refuses a chapter that already holds a placed image or blurb.
"""
import argparse
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RC1 = os.path.join(ROOT, "team", "conductor", "rc1")
MAN = os.path.join(ROOT, "manuscript")
# the call-out kinds of the RC1 build, as Markua's blurb classes (publishing/markua.py maps them back)
CLASS = {"concept": "information", "number": "discussion", "takeaway": "tip", "warning": "warning", "try": "exercise"}
LABEL = {"concept": "Concept", "number": "The number", "takeaway": "Take away", "warning": "Watch for", "try": "Try this"}


def add_images(name, text, placements):
    """As assemble_rc1.add_images: after the anchor's paragraph, in file order; "replace" swaps an image path."""
    placed, missed = 0, []
    for p in [p for p in placements if p.get("chapter") == name]:
        img = p["image"]
        if p.get("replace"):
            if p["replace"] in text:
                text = text.replace(p["replace"], img)
                placed += 1
            else:
                missed.append(img)
            continue
        a = p.get("anchor", "")
        i = text.find(a) if a else -1
        if i < 0:
            missed.append(img)
            continue
        end = text.find("\n\n", i)
        end = len(text) if end < 0 else end
        while text.startswith("\n\n![", end):
            nl = text.find("\n", end + 3)
            end = len(text) if nl < 0 else nl
        text = text[:end] + f"\n\n![{p['caption']}]({img})" + text[end:]
        placed += 1
    return text, placed, missed


def add_callouts(name, text, callouts):
    """As assemble_rc1.add_callouts, written as a Markua blurb block instead of a pandoc div."""
    placed, missed = 0, []
    for c in [c for c in callouts if c.get("chapter") == name]:
        a = c.get("anchor", "")
        i = text.find(a) if a else -1
        if i < 0:
            missed.append(c.get("title"))
            continue
        end = text.find("\n\n", i)
        end = len(text) if end < 0 else end
        kind = re.sub(r"[^a-z]", "", (c.get("kind") or "concept").lower()) or "concept"
        ids = c.get("claim_ids") or []
        tail = f" ({', '.join(ids)})" if ids and not any(x in c["text"] for x in ids) else ""
        block = (f"\n\n{{blurb, class: {CLASS.get(kind, 'information')}}}\n"
                 f"**{LABEL.get(kind, kind.title())}: {c['title']}**\n\n{c['text']}{tail}\n{{/blurb}}")
        text = text[:end] + block + text[end:]
        placed += 1
    return text, placed, missed


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()
    callouts = json.load(open(os.path.join(RC1, "infographics", "callouts.json"), encoding="utf-8"))
    placements = [{"chapter": m["chapter"], "anchor": m["anchor"], "caption": m["caption"],
                   "image": "resources/images/infographics/" + os.path.basename(m["file"])}
                  for m in json.load(open(os.path.join(RC1, "infographics", "manifest.json"), encoding="utf-8"))
                  if not m.get("withdrawn")]
    placements += json.load(open(os.path.join(RC1, "maps", "placements.json"), encoding="utf-8"))
    with open(os.path.join(MAN, "Book.txt"), encoding="utf-8") as f:
        names = [n.strip() for n in f if n.strip() and not n.startswith("#")]
    out, images, blurbs, missed = {}, 0, 0, []
    for n in names:
        text = open(os.path.join(MAN, n), encoding="utf-8").read()
        if "{blurb" in text or "resources/images/infographics/" in text:
            sys.exit(f"place_rc1: {n} already holds placed figures or blurbs; run once, on RC1's chapters")
        text, ip, im = add_images(n, text, placements)
        text, cp, cm = add_callouts(n, text, callouts)
        images, blurbs = images + ip, blurbs + cp
        missed += [f"{n}: image {m}" for m in im] + [f"{n}: call-out {m}" for m in cm]
        out[n] = text
    print(f"place_rc1: {images} images and {blurbs} call-outs placed in {len(names)} chapters")
    for m in missed:
        print("place_rc1: anchor not found:", m)
    if a.dry_run:
        return
    dest = os.path.join(MAN, "resources", "images", "infographics")
    os.makedirs(dest, exist_ok=True)
    for img in sorted({q["image"] for q in placements if q["image"].startswith("resources/images/infographics/")}):
        shutil.copy2(os.path.join(RC1, "infographics", "jpg", os.path.basename(img)), dest)
    for n, text in out.items():
        with open(os.path.join(MAN, n), "w", encoding="utf-8") as f:
            f.write(text)


if __name__ == "__main__":
    main()
