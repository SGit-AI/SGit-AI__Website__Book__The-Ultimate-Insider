#!/usr/bin/env python3
"""LAB 74: chapter 4's figure, the sgit.ai sites the talk's repository names, newsroom.sgit.ai largest, each sized by how
often it is named (manuscript/rc2/150/04-hour-one-the-empty-project.md, its "past projects" concept).

    python3 lab/experiments/74-designer-sgit-sites/make_sites.py

Every site and count is C126's (checked; occurrences at the end of the day), read at build; the chapter's "2,666" and
"twenty-three other" are checked against it. Ranked bars on one linear scale, so the newsroom's lead is drawn as it is.
Host names and counts only; no id or hash drawn.
"""
import json, re, sys
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'
CH = (REPO / "manuscript" / "rc2" / "150" / "04-hour-one-the-empty-project.md").read_text()
WORDS = {20: "twenty", 21: "twenty-one", 22: "twenty-two", 23: "twenty-three", 24: "twenty-four", 25: "twenty-five"}


def t(x, y, s, weight=400, fill=mc.INK, anchor="start", size=3.18):
    return (f'<text x="{x:.2f}" y="{y:.2f}" {SANS} font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}">{escape(str(s), quote=False)}</text>')


def main():
    c = {x["id"]: x for x in json.loads((REPO / "claims" / "register.json").read_text())["claims"]}["C126"]
    if c["state"] != "checked":
        sys.exit("make_sites: C126 is not checked")
    sites = sorted(c["value"]["sites"], key=lambda s: -s["occurrences"])
    top, rest = sites[0], sites[1:]
    if top["site"] != "newsroom.sgit.ai" or f"mentions newsroom.sgit.ai {top['occurrences']:,} times" not in CH:
        sys.exit("make_sites: the chapter's newsroom count is not C126's")
    if f"{WORDS.get(len(rest), str(len(rest)))} other sgit.ai sites" not in CH:
        sys.exit(f"make_sites: the chapter does not say {len(rest)} other sites")
    lx, x0, x1, pitch, y0 = 44.0, 46.0, 140.0, 4.0, 4.0
    big = top["occurrences"]
    out = []
    for i, s in enumerate(sites):
        y = y0 + i * pitch
        w = max(.6, (x1 - x0) * s["occurrences"] / big)
        first = i == 0
        out.append(t(lx, y + 2.6, s["site"], 700 if first else 400, mc.INK, "end"))
        out.append(f'<rect x="{x0}" y="{y + .5:.2f}" width="{w:.2f}" height="2.8" rx=".6" fill="{mc.ACCENT if first else mc.INK}"/>')
        out.append(t(x0 + w + 1.6, y + 2.6, f"{s['occurrences']:,}", 700 if first else 400, mc.ACCENT if first else mc.MUTED))
    yb = y0 + len(sites) * pitch + 3
    out.append(t(x0, yb + 1, "times each site is named in the talk's repository at the end of the day", 400, mc.MUTED, "start"))
    svg = mc.svg(156, round(yb + 3, 1), "".join(out), "The sgit.ai sites the talk's repository names, newsroom.sgit.ai largest, each bar sized by how often it is named")
    if re.search(r">[^<]*\b(C\d{3}|[0-9a-f]{7,}|https?:)", svg):
        sys.exit("make_sites: an id, a hash or an address is drawn")
    (HERE / "sgit-sites.svg").write_text(svg)
    print(f"written sgit-sites.svg: {len(sites)} sites, newsroom {big:,}")


if __name__ == "__main__":
    main()
