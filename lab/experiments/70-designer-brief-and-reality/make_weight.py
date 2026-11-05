#!/usr/bin/env python3
"""LAB 70: chapter 4's figure, the brief and the reality file as they stood at the end of the day, a few of their pages
in a collage, each with its size (manuscript/rc2/150/04-hour-one-the-empty-project.md; the cast guide's convention 9).

    python3 lab/experiments/70-designer-brief-and-reality/make_weight.py <the talk's clone, read only>

The sizes are C125's (checked), and must be the chapter's; the line counts are checked against the files at 298be4e
with git. What is set on the pages is the files' own headings and first lines, read with git: the brief's title, its
status line's opening and its first heading; the reality file's title and section headings. The rest of each page is
grey lines: no address, no request text, nothing of the team's keys or vaults (security's pre-review of 23:59).
"""
import json, re, subprocess, sys
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'
CH = (REPO / "manuscript" / "rc2" / "150" / "04-hour-one-the-empty-project.md").read_text()
REG = {c["id"]: c for c in json.loads((REPO / "claims" / "register.json").read_text())["claims"]}


def t(x, y, s, weight=400, fill=mc.INK, anchor="start", size=3.18):
    return (f'<text x="{x:.2f}" y="{y:.2f}" {SANS} font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}">{escape(str(s), quote=False)}</text>')


def sizes(clone):
    c = REG["C125"]
    if c.get("state") != "checked":
        sys.exit("make_weight: C125 is not checked")
    named = {n["path"]: n for n in c["value"]["named"]}
    out = {}
    for path in ("BRIEF.md", "REALITY.md"):
        n = named[path]
        text = subprocess.run(["git", "-C", clone, "show", f"298be4e:{path}"], capture_output=True, text=True, check=True).stdout
        if len(text.splitlines()) != n["lines"]:
            sys.exit(f"make_weight: {path} has {len(text.splitlines())} lines at 298be4e, C125 says {n['lines']}")
        out[path] = (n["words"], n["lines"], text)
    if f"the brief {out['BRIEF.md'][0]} words, the reality file {out['REALITY.md'][0]:,}" not in CH:
        sys.exit("make_weight: the chapter's sizes are not C125's")
    return out


def page(x, y, w, h, name, lines, size):
    words, nlines = size
    out = [f'<rect x="{x + 1.2:.2f}" y="{y + 1.2:.2f}" width="{w}" height="{h}" rx="1.2" fill="{mc.FILL2}"/>',
           f'<rect x="{x:.2f}" y="{y:.2f}" width="{w}" height="{h}" rx="1.2" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>',
           t(x + 4, y + 6.4, name, 700, mc.MUTED)]
    yy = y + 12.6
    for kind, s in lines:
        if kind == "h1":
            out.append(t(x + 4, yy, s, 800, mc.INK)); yy += 5.2
        elif kind == "h2":
            out.append(t(x + 4, yy, s, 700, mc.INK)); yy += 4.4
        elif kind == "p":
            out.append(t(x + 4, yy, s, 400, mc.MUTED)); yy += 4.4
        else:  # the rest of the text, as grey lines
            for k in range(s):
                out.append(f'<rect x="{x + 4:.2f}" y="{yy - 2:.2f}" width="{(w - 8) * (.94 - .17 * (k % 3)):.2f}" height="1.3" rx=".65" fill="{mc.FILL2}"/>')
                yy += 2.6
            yy += 1.6
    out.append(t(x, y + h + 6.4, f"{words:,} words", 800, mc.ACCENT, "start", size=4.2)
               + t(x + w, y + h + 6.4, f"{nlines} lines", 400, mc.MUTED, "end"))
    return "".join(out)


def main():
    s = sizes(sys.argv[1])
    brief = s["BRIEF.md"][2].splitlines()
    real = s["REALITY.md"][2].splitlines()
    title = brief[0].lstrip("# ")
    status = brief[2].split(". Date")[0] + "."
    first_h2 = next(l for l in brief if l.startswith("## ")).lstrip("# ")
    if not status.startswith("Status: accepted"):
        sys.exit("make_weight: the brief's status line has changed")
    heads = [l.lstrip("# ").split(" (")[0] for l in real if l.startswith("## ")]
    import textwrap
    bl = [("h1", r) for r in textwrap.wrap(title, 34)] + [("p", status), ("h2", first_h2), ("bars", 5), ("bars", 4), ("bars", 5)]
    rl = [("h1", real[0].lstrip("# "))]
    for h in heads:
        rl += [("h2", h), ("bars", 1)]
    out = [page(2, 2, 70, 80, "BRIEF.md", bl, s["BRIEF.md"][:2]),
           page(82, 2, 70, 80, "REALITY.md", rl, s["REALITY.md"][:2])]
    svg = mc.svg(156, 92, "".join(out), "The brief and the reality file as they stood at the end of the day, a page of each, with its size in words and lines")
    if re.search(r">[^<]*\b(C\d{3}|[0-9a-f]{7,}|https?:)", svg):
        sys.exit("make_weight: an id, a hash or an address is drawn")
    (HERE / "brief-and-reality.svg").write_text(svg)
    print("written brief-and-reality.svg")


if __name__ == "__main__":
    main()
