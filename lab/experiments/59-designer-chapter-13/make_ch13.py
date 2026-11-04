#!/usr/bin/env python3
"""LAB 59: chapter 13's two figures (manuscript/rc2/150/13-the-story-before-the-slides.md).

    python3 lab/experiments/59-designer-chapter-13/make_ch13.py <the talk's clone, read only>

1. objection-path.svg: the objection's path in one line of time: the researcher's finding, the storyteller's letter, the
   editor's answer, each with its own words from the record beneath. The words and times are read from the talk's commits
   with git at build and checked against the chapter's brief; the times in the picture only, no hash drawn.
2. storyteller-map.svg: map 1, "the outside is mature, the inside is not", as the storyteller's tool drew it into the
   talk's maps slide: its components, links, moves and notes from team/storyteller/maps/1-outside-and-inside.json at
   298be4e, the axis words from its SVG, and the slide's own small line, "positions, not measurements".
"""
import json, re, subprocess, sys
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'
CH = (REPO / "manuscript" / "rc2" / "150" / "13-the-story-before-the-slides.md").read_text()


def t(x, y, s, weight=400, fill=mc.INK, anchor="middle", size=3.18):
    return (f'<text x="{x:.2f}" y="{y:.2f}" {SANS} font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}">{escape(str(s), quote=False)}</text>')


def git(clone, *a):
    return subprocess.run(["git", "-C", clone, *a], capture_output=True, text=True, check=True).stdout


def objection(clone):
    if "the finding 14:33 (2726f0e), the letter 15:02 (b208a16), the answer committed 15:16 (78d517d)" not in CH:
        sys.exit("make_ch13: chapter 13's brief for the objection's path has changed")
    marks = []
    for sha, who, pick in [("2726f0e", "the researcher's finding", lambda b: re.search(r"R5 contradicted by the data", b).group(0)),
                           ("b208a16", "the storyteller's letter", lambda b: b.splitlines()[0].split(": ", 1)[1].split("; ", 1)[1]),
                           ("78d517d", "the editor's answer", None)]:
        when = git(clone, "show", "-s", "--format=%cI", sha)[11:16]
        body = git(clone, "show", "-s", "--format=%B", sha)
        if pick is None:
            words = "The outside is in balance: he keeps the claim."
            files = git(clone, "show", "--format=", sha)
            if words not in files.replace("**", "") or f'> "{words}" *(record)*' not in CH:
                sys.exit("make_ch13: the answer's line is not in its commit or no longer quoted in the chapter")
        else:
            words = pick(body)
        marks.append((when, who, words))
    if [m[0] for m in marks] != ["14:33", "15:02", "15:16"]:
        sys.exit(f"make_ch13: the times are not the brief's: {[m[0] for m in marks]}")
    import textwrap
    x0, x1 = 8.0, 148.0
    lo, hi = 14 * 60 + 25, 15 * 60 + 25

    def X(hm):
        h, m = map(int, hm.split(":"))
        return x0 + (x1 - x0) * (h * 60 + m - lo) / (hi - lo)
    out = [mc.line(x0, 10, x1, 10, mc.INK, .5)]
    for hm in ("14:30", "15:00"):
        out.append(mc.line(X(hm), 8.8, X(hm), 11.2, mc.MUTED, .35) + t(X(hm), 6.6, hm, 400, mc.MUTED))
    # three columns of words, each under its own mark; the mark's place on the line is its time
    cols = [8.0, 58.0, 108.0]
    ymax = 0
    for k, (when, who, words) in enumerate(marks):
        x = X(when)
        out.append(f'<circle cx="{x:.2f}" cy="10" r="1.6" fill="{mc.ACCENT if k == 2 else mc.INK}"/>')
        cx = cols[k]
        out.append(f'<path d="M{x:.2f} 11.6 L{x:.2f} 14 L{cx + 2:.2f} 16.6" stroke="{mc.MUTED}" stroke-width=".35" fill="none"/>')
        out.append(t(cx, 21, when, 800, mc.ACCENT if k == 2 else mc.INK, "start", size=4.2) + t(cx, 25.6, who, 700, mc.INK, "start"))
        for j, r in enumerate(textwrap.wrap(f"“{words}”", 26)):
            out.append(t(cx, 30 + j * 4.1, r, 400, mc.INK, "start"))
            ymax = max(ymax, 30 + j * 4.1)
    svg = mc.svg(156, round(ymax + 2.4, 1), "".join(out), "The objection's path in one line of time: the researcher's finding, the storyteller's letter and the editor's answer, each with its own words beneath")
    return svg


def storymap(clone):
    if "positions, not measurements" not in CH:
        sys.exit("make_ch13: the chapter no longer quotes the map's small line")
    m = json.loads(git(clone, "show", "298be4e:team/storyteller/maps/1-outside-and-inside.json"))
    src = git(clone, "show", "298be4e:team/storyteller/maps/1-outside-and-inside.svg")
    stages = ["Genesis", "Custom built", "Product (+rental)", "Commodity (+utility)"]
    for w in stages + ["Evolution", "Value chain (visible to invisible)"]:
        if f">{w}<" not in src:
            sys.exit(f"make_ch13: the storyteller's map no longer reads '{w}'")
    if "positions, not measurements" not in git(clone, "show", "298be4e:src/static/talk/slides/maps/inside/index.html"):
        sys.exit("make_ch13: the talk's map slide no longer carries its small line")
    L, R, T, B = 8.0, 154.0, 6.0, 88.0
    X = lambda e: L + (R - L) * e
    Y = lambda v: B - (B - T) * v
    title = m["title"].split(" (")[0]
    out = [t(0, 3.2, title, 700, mc.INK, "start")]
    # behind the firewall, as the title says: shaded where the inside components sit
    ins = [c for c in m["components"] if c.get("inside")]
    ex, ey = max(c["evo"] for c in ins) + .03, max(c["vis"] for c in ins) + .05
    out.append(f'<rect x="{L:.2f}" y="{Y(ey):.2f}" width="{X(ex) - L:.2f}" height="{B - Y(ey):.2f}" fill="{mc.FILL}"/>')
    out.append(t(L + 1.5, Y(.74), "shaded: behind the firewall", 400, mc.MUTED, "start"))
    for k in range(1, 4):
        out.append(f'<path d="M{X(k / 4):.2f} {T} V{B}" stroke="{mc.FILL2}" stroke-width=".3" stroke-dasharray="1 1"/>')
    out.append(mc.line(L, B, R, B, mc.INK, .5) + mc.line(L, T, L, B, mc.INK, .5))
    for k, s in enumerate(stages):
        out.append(t(X(k / 4 + .125), B + 4.2, s, 400, mc.MUTED))
    out.append(t((L + R) / 2, B + 8.4, "Evolution", 700, mc.INK))
    out.append(t(L + 1.5, T + 3.6, "Value chain (visible to invisible)", 400, mc.MUTED, "start"))
    pos = {c["id"]: (X(c["evo"]), Y(c["vis"])) for c in m["components"]}
    for a, b in m["links"]:
        (x1, y1), (x2, y2) = pos[a], pos[b]
        out.append(mc.line(x1, y1, x2, y2, mc.MUTED, .35))
    for c in m["components"]:
        x, y = pos[c["id"]]
        if "move" in c:
            xm = X(c["move"])
            out.append(f'<path d="M{x + 1.4:.2f} {y} H{xm - 1:.2f}" stroke="{mc.ACCENT}" stroke-width=".5" stroke-dasharray="1.2 .8"/>'
                       f'<path d="M{xm - 2:.2f} {y - 1:.2f} L{xm:.2f} {y} L{xm - 2:.2f} {y + 1:.2f}" stroke="{mc.ACCENT}" stroke-width=".5" fill="none"/>')
    for c in m["components"]:
        x, y = pos[c["id"]]
        out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="1.3" fill="#fff" stroke="{mc.INK}" stroke-width=".5"/>')
        right = c["evo"] < .5 or c["id"] in ("edge",)
        anchor = "end" if c["evo"] > .7 else "start"
        dx = -2.2 if anchor == "end" else 2.2
        out.append(t(x + dx, y + (4.4 if c["id"] == "edge" else -1.6), c["label"], 700 if c["id"] == "agent" else 400, mc.INK, anchor))
    for n in m["notes"]:  # the notes at their own corners: outside top right, inside bottom left, clear of the components
        if n["vis"] > .5:
            out.append(t(R, Y(n["vis"]) + 5, n["text"], 700, mc.ACCENT, "end"))
        else:
            out.append(t(L + 1.5, B - 1.8, n["text"], 700, mc.ACCENT, "start"))
    out.append(t(R, B + 8.4, "positions, not measurements", 400, mc.MUTED, "end"))
    return mc.svg(156, round(B + 10.4, 1), "".join(out), "One of the storyteller's maps as it went into the talk: map 1, the outside is mature, the inside is not; positions, not measurements")


def main():
    clone = sys.argv[1]
    for name, svg in {"objection-path.svg": objection(clone), "storyteller-map.svg": storymap(clone)}.items():
        if re.search(r">[^<]*\b(C\d{3}|[0-9a-f]{7,})\b", svg):
            sys.exit(f"make_ch13: {name} draws an id or a hash")
        (HERE / name).write_text(svg)
        print("written", name)


if __name__ == "__main__":
    main()
