#!/usr/bin/env python3
"""LAB 37: RC2's pictures for chapters 1 and 2 of the thirty (the writer's Figure lines, manuscript/rc2/30/).

    python3 lab/experiments/37-designer-rc2-chapters-1-2/make_pictures.py <read-only clone of the talk's repository>
- ch1-slide.svg and ch1-loop.svg: "A slide versus a loop", its two halves.
- ch1-cast-greyed.svg: the nine cards greyed and the empty chair, each with its arrival from C011 (read at build).
- ch2-first-wake.svg: the first five-step wake as a card, its verdicts read from the talk's own record at 298be4e
  (team/conductor/wakes/20261029T021416Z.json, with git, read only), beside C022's count of the day's wake records.
- ch2-cast-bar-0400.svg: the cast bar at four in the morning, the members whose first commit (C011) came before 04:00.
One SVG unit a millimetre, sizes stated, text 9 pt; the only numbers are from claims/ or the record, with their ids.
"""
import json, math, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

F = 3.18
SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'
REG = {c["id"]: c for c in json.loads((REPO / "claims" / "register.json").read_text())["claims"]}


def t(x, y, s, weight=400, fill=mc.INK, anchor="start"):
    return f'<text x="{x:.2f}" y="{y:.2f}" {SANS} font-size="{F}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'


def g(body, x, y, s):
    return f'<g transform="translate({x:.2f} {y:.2f}) scale({s})">{body}</g>'


def first_commits():
    out = {}
    for line in (REPO / "claims" / "scorecard-values.md").read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 7 and cells[0] in mc.CAST:
            out[cells[0]] = cells[1].split()[0]
    return out  # C011's first commits, as the researcher's table holds them


def bubble(x, y, w=18, h=9):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="#fff" stroke="{mc.INK}" stroke-width=".4"/>'
            f'<path d="M{x + 3} {y + h} l-1.5 3.4 l4.4 -3.4" fill="#fff" stroke="{mc.INK}" stroke-width=".4"/>'
            + "".join(f'<circle cx="{x + w / 2 + (k - 1) * 3:.1f}" cy="{y + h / 2}" r=".7" fill="{mc.MUTED}"/>' for k in range(3)))


def slide():
    """Left half: the speaker beside a still slide, an arrow from A to B, three bubbles explaining what cannot move."""
    out = [f'<rect x="38" y="6" width="74" height="46" rx="1.5" fill="#fff" stroke="{mc.INK}" stroke-width=".6"/>',
           f'<circle cx="52" cy="34" r="3.6" fill="{mc.FILL2}"/>' + t(52, 35.1, "A", 800, anchor="middle"),
           f'<circle cx="98" cy="20" r="3.6" fill="{mc.FILL2}"/>' + t(98, 21.1, "B", 800, anchor="middle"),
           f'<path d="M56 32 L94 22" stroke="{mc.ACCENT}" stroke-width=".8" stroke-dasharray="2 1.4" marker-end="url(#a)"/>',
           bubble(4, 4), bubble(8, 16), bubble(2, 28), g(mc.editor_figure("A"), 10, 34, .62)]
    defs = f'<defs><marker id="a" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="{mc.ACCENT}"/></marker></defs>'
    return mc.svg(116, 66, defs + "".join(out), "A speaker beside a still slide with an arrow from A to B, explaining it in three speech bubbles")


def loop():
    """Right half: the same idea as a loop of three arrows, see, ask, see again; a small factory inside; the speaker outside."""
    cx, cy, r = 70, 33, 25
    out = []
    for i, word in enumerate(["see", "ask", "see again"]):
        a0, a1 = math.radians(-90 + i * 120 + 12), math.radians(-90 + (i + 1) * 120 - 12)
        out.append(f'<path d="M{cx + r * math.cos(a0):.2f} {cy + r * math.sin(a0):.2f} A{r} {r} 0 0 1 {cx + r * math.cos(a1):.2f} {cy + r * math.sin(a1):.2f}" '
                   f'fill="none" stroke="{mc.ACCENT}" stroke-width="1" marker-end="url(#b)"/>')
        am = math.radians(-90 + i * 120 + 60)
        out.append(t(cx + (r + 7) * math.cos(am), cy + (r + 7) * math.sin(am) + 1.1, word, 700, anchor="middle"))
    for i, m in enumerate(mc.CAST):  # the factory: the nine, small, in a ring
        a = math.radians(-90 + i * 40)
        out.append(g(mc.head(m), cx + 11 * math.cos(a) - 2.4, cy + 11 * math.sin(a) - 2.2, .12))
    out.append(g(mc.editor_figure("A"), 2, 30, .62))
    defs = f'<defs><marker id="b" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="{mc.ACCENT}"/></marker></defs>'
    return mc.svg(110, 66, defs + "".join(out), "The same idea as a loop of three arrows, see, ask, see again, with a small factory inside and the speaker outside looking")


def chair(x, y, s=1.0, col=None):
    c = col or mc.FILL2
    return (f'<g transform="translate({x} {y}) scale({s})">' + mc.line(4, 2, 4, 18, c, .9) + mc.line(4, 11, 14, 11, c, .9)
            + mc.line(14, 11, 14, 18, c, .9) + mc.line(4, 2, 7, 2, c, .9) + "</g>")


def cast_greyed():
    firsts = first_commits()
    order = sorted(mc.CAST, key=lambda m: firsts[m])
    w, h, out = 31.3, 22, []  # 31.3: the last card's stroke inside the 164 viewBox (synthetic__005, publisher__018)
    for i, m in enumerate(order + ["security"]):
        x, y = (i % 5) * (w + 1.5), (i // 5) * (h + 2)
        out.append(f'<rect x="{x + .3:.2f}" y="{y + .3:.2f}" width="{w}" height="{h}" rx="1.6" fill="#fff" stroke="{mc.FILL2}" stroke-width=".4"/>')
        if m == "security":
            out.append(chair(x + 8, y + 1.6, .62) + t(x + 3, y + 16.6, "security", 700, mc.MUTED) + t(x + 3, y + 20.4, "an empty chair", 400, mc.MUTED))
        else:
            out.append(g(mc.head(m, False), x + 1.6, y - .4, .3) + t(x + 3, y + 16.6, m, 700, mc.MUTED) + t(x + 3, y + 20.4, f"arrives {firsts[m]}", 400, mc.MUTED))
    return mc.svg(164, 2 * h + 3, "".join(out), "The nine cards greyed, in the order they arrive, and an empty chair for security")


def first_wake(clone):
    rec = json.loads(subprocess.run(["git", "-C", clone, "show", "298be4e:team/conductor/wakes/20261029T021416Z.json"],
                                    capture_output=True, text=True, check=True).stdout)
    steps = [(k, (v or {}).get("verdict", "")) for k, v in rec["steps"].items()]
    words = {"plan": "plan", "pre_review": "plan checked", "work": "work", "post_review": "work checked", "post_check": "checked against the plan"}
    out = [f'<rect x=".3" y=".3" width="86" height="{10 + 5.4 * len(steps) + 8}" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>',
           t(4, 7, "The first five-step wake: the conductor's", 800)]
    for i, (k, v) in enumerate(steps):
        y = 14 + i * 5.4
        out.append(t(4, y, words.get(k, k), 400, mc.MUTED) + t(82, y, v, 800, mc.ACCENT if v not in ("go", "done", "clean") else mc.INK, "end"))
    out.append(t(4, 14 + len(steps) * 5.4 + 2, f"outcome: {rec.get('outcome')}", 800))
    count = REG["C022"]["value"]["records"]
    out.append(f'<text x="100" y="22" {SANS} font-size="12" font-weight="800" fill="{mc.INK}">{count}</text>'
               + t(100, 28, "wake records the team kept", 400) + t(100, 32.2, "that day (C022)", 400, mc.MUTED))
    out.append(t(4, 10 + 5.4 * len(steps) + 14, "record: team/conductor/wakes/20261029T021416Z.json at 298be4e", 400, mc.MUTED))
    return mc.svg(164, round(10 + 5.4 * len(steps) + 16, 1), "".join(out), "The first five-step wake's verdicts, as its record holds them, beside the day's count of wake records")


def cast_bar_0400():
    firsts = first_commits()
    present = {m for m, f in firsts.items() if f < "04:00"}
    order = sorted(mc.CAST, key=lambda m: firsts[m])
    marker = mc.on_stage(present, 9.0, order)
    inner = marker[marker.index(">") + 1:marker.rindex("</svg>")]
    w = float(marker.split('width="')[1].split("mm")[0])
    body = inner + chair(w + 2, .4, .56)
    return mc.svg(round(w + 12, 1), 11, body, f"The cast bar at four in the morning: {len(present)} lit, the rest greyed, an empty chair")


if __name__ == "__main__":
    clone = sys.argv[1]
    files = {"ch1-slide.svg": slide(), "ch1-loop.svg": loop(), "ch1-cast-greyed.svg": cast_greyed(),
             "ch2-first-wake.svg": first_wake(clone), "ch2-cast-bar-0400.svg": cast_bar_0400()}
    for name, svg in files.items():
        (HERE / name).write_text(svg)
    print("written " + ", ".join(files))
