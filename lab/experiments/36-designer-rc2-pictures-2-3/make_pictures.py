#!/usr/bin/env python3
"""LAB 36: RC2's first pictures, the two the 30-page outline names for the designer in its chapters 2 and 3.

    python3 lab/experiments/36-designer-rc2-pictures-2-3/make_pictures.py
- chapter2-wake-clock.svg: the five-step wake as a loop, the hour's clock around it, each member's minute on the dial,
  read from C071 in claims/register.json when the picture is built.
- chapter3-sent-back.svg: three cards, who sent what back to whom (or owned it), the reason in the record's words,
  each line found verbatim in timeline/cast.md or timeline/cast-scenes.md (the script stops if not), its commit beside it.
No other number. One SVG unit a millimetre, sizes stated, text 9 pt.
"""
import json, math, sys, textwrap
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

F = 3.18
SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'
MONO = 'font-family="DejaVu Sans Mono, monospace"'
REG = {c["id"]: c for c in json.loads((REPO / "claims" / "register.json").read_text())["claims"]}


def t(x, y, s, weight=400, fill=mc.INK, anchor="start", font=SANS):
    return f'<text x="{x:.2f}" y="{y:.2f}" {font} font-size="{F}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'


def head(m, x, y, s=.3):
    return f'<g transform="translate({x - 20 * s:.2f} {y - 18 * s:.2f}) scale({s})">{mc.head(m)}</g>'


STEPS = ["plan", "plan checked", "work", "work checked", "checked against the plan"]


def wake_clock():
    slots = REG["C071"]["value"]
    cx, cy, R = 82, 60, 46
    out = [f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{mc.FILL2}" stroke-width="1.2"/>']
    for m in range(0, 60, 5):
        a = math.radians(m * 6 - 90)
        r1 = R - (3 if m % 15 == 0 else 1.6)
        out.append(mc.line(cx + r1 * math.cos(a), cy + r1 * math.sin(a), cx + R * math.cos(a), cy + R * math.sin(a), mc.MUTED, .4))
    for k, (member, mm) in enumerate(sorted(slots.items(), key=lambda kv: kv[1])):
        minute = int(mm.strip(":"))
        a = math.radians(minute * 6 - 90)
        hx, hy = cx + (R + 9) * math.cos(a), cy + (R + 9) * math.sin(a)
        out.append(f'<circle cx="{cx + R * math.cos(a):.2f}" cy="{cy + R * math.sin(a):.2f}" r="1.1" fill="{mc.CAST[member][0]}"/>')
        out.append(head(member, hx, hy))
        anchor = "start" if math.cos(a) > .2 else ("end" if math.cos(a) < -.2 else "middle")
        dx = 5.6 if anchor == "start" else (-5.6 if anchor == "end" else 0)
        dy = 1.1 if anchor != "middle" else (7.6 if math.sin(a) > 0 else -5.2)
        out.append(t(hx + dx, hy + dy, f"{member} {mm}", 700 if member == "conductor" else 400, anchor=anchor))
    r = 24  # the five steps, a loop inside the hour
    pts = [(cx + r * math.cos(math.radians(-90 + i * 72)), cy + r * math.sin(math.radians(-90 + i * 72))) for i in range(5)]
    for i in range(5):
        a0, a1 = math.radians(-90 + i * 72 + 14), math.radians(-90 + (i + 1) * 72 - 14)
        out.append(f'<path d="M{cx + r * math.cos(a0):.2f} {cy + r * math.sin(a0):.2f} A{r} {r} 0 0 1 {cx + r * math.cos(a1):.2f} {cy + r * math.sin(a1):.2f}" '
                   f'fill="none" stroke="{mc.ACCENT}" stroke-width=".7" marker-end="url(#ar)"/>')
    for i, (x, y) in enumerate(pts):
        out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="3.2" fill="{mc.ACCENT}"/>' + t(x, y + 1.1, str(i + 1), 800, "#fff", "middle"))
    out.append(t(cx, cy - 1, "one wake:", 400, mc.MUTED, "middle") + t(cx, cy + 3.4, "five steps", 800, anchor="middle"))
    key = [t(0 if i < 3 else 0, 126 + (i % 3) * 4.6, "") for i in range(0)]  # replaced below
    cols = [(0, STEPS[:3]), (82, STEPS[3:])]
    for x0, group in cols:
        for j, s in enumerate(group):
            n = STEPS.index(s) + 1
            key.append(f'<circle cx="{x0 + 2:.1f}" cy="{125.5 + j * 5:.1f}" r="2" fill="{mc.ACCENT}"/>' + t(x0 + 2, 126.6 + j * 5, str(n), 800, "#fff", "middle") + t(x0 + 6, 126.6 + j * 5, s))
    defs = f'<defs><marker id="ar" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="{mc.ACCENT}"/></marker></defs>'
    foot = t(0, 144, "each member wakes at its own minute past the hour (C071) and runs the five steps", 400, mc.MUTED)
    return mc.svg(164, 146, defs + "".join(out) + "".join(key) + foot,
                  "One wake as a loop of five steps inside the hour's clock; each member's minute past the hour on the dial")


CARDS = [  # (sender, receiver, label, the record's words, the file it is quoted from, commit)
    ("deck", "ruv-sgit", "sent back", "What it is not yet is a picture a room reads in five seconds.", "timeline/cast.md", "78b89b9"),
    ("deck", "deck", "held back by its reviewer", "My plan sent the E02 request now; the pre-review asked for a change, because B01 v1 is ruv.sgit's one request in flight.", "timeline/cast-scenes.md", "aeffbf9"),
    ("designer", "designer", "owned", "The miss is my table's as much as the build's", "timeline/cast.md", "56c680b"),
]


def sent_back():
    out = []
    for i, (frm, to, label, words, src, commit) in enumerate(CARDS):
        if words not in (REPO / src).read_text():
            sys.exit(f"make_pictures: {words[:40]!r} is not in {src}")
        x, w = i * 55.4, 52.4
        rows = textwrap.wrap(f"“{words}”", 27)
        h = 32 + 4.2 * len(rows) + 8
        out.append(f'<rect x="{x + .4:.2f}" y=".4" width="{w}" height="{h:.1f}" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>')
        out.append(head(frm, x + 10, 10, .34) + t(x + 10, 21, frm, 700, anchor="middle"))
        if to != frm:
            out.append(f'<path d="M{x + 19:.1f} 10 h14" stroke="{mc.ACCENT}" stroke-width=".8" marker-end="url(#ar2)"/>'
                       + head(to, x + 42, 10, .34) + t(x + 42, 21, to, 700, anchor="middle"))
        out.append(t(x + 3, 28, label, 800, mc.ACCENT))
        for j, r in enumerate(rows):
            out.append(t(x + 3, 33.5 + j * 4.2, r))
        out.append(t(x + 3, h - 2.4, f"record {commit}", 400, mc.MUTED, font=MONO))
    defs = f'<defs><marker id="ar2" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="{mc.ACCENT}"/></marker></defs>'
    height = max(32 + 4.2 * len(textwrap.wrap(f"“{c[3]}”", 27)) + 8 for c in CARDS) + 1
    return mc.svg(164, round(height, 1), defs + "".join(out), "Three cards: what was sent back, held back or owned, and the reason in the record's words")


if __name__ == "__main__":
    (HERE / "chapter2-wake-clock.svg").write_text(wake_clock())
    (HERE / "chapter3-sent-back.svg").write_text(sent_back())
    print("written chapter2-wake-clock.svg and chapter3-sent-back.svg")
