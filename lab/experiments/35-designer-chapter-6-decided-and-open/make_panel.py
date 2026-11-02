#!/usr/bin/env python3
"""LAB 35: chapter 6's picture, the half that does not wait on registered times: decided, and open at 19:00.

    python3 lab/experiments/35-designer-chapter-6-decided-and-open/make_panel.py
Every word on the panel is a fragment of manuscript/06-the-editor-signs.md, checked here against its line before
drawing (the script stops if a fragment is not in its line). The only number is the section's own 19:00, when the talk was
scheduled (C100, at the researcher's check). A proposal: the fragments go to
the researcher before anything goes to the book; the timeline half waits on the signature times.
"""
import sys, textwrap
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

CHAPTER = REPO / "manuscript" / "06-the-editor-signs.md"
DECIDED = [("the framing", 95), ("the beats", 95), ("the parts", 95), ("the members", 95), ("the policies once the slide needed them", 95)]
OPEN = [("Item 4", 93, "the choice between two wordings for a line on a slide about which of its incidents were attacks"),
        ("D12", 93, "whether to do anything about other sites' tokens left in a pushed, public history the night before"),
        ("D02", 93, "what his signed answer would mean"),
        ("The vault handovers", 93, "The handover files that held the team's vault keys, sealed for him to store, were waiting too")]
LINES = [("The decisions he made were the ones the work was waiting for", 95),
         ("The ones left were governance", 95),
         ("no word yet; nobody waits on them for part 1", 93),
         ("the conductor recorded the state of all of them in one line", 93)]
F = 3.18
SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'


def check():
    text = CHAPTER.read_text().splitlines()
    for frag, ln in [(f, l) for f, l in DECIDED] + [(d, l) for _, l, d in OPEN] + LINES:
        if frag not in text[ln - 1]:
            sys.exit(f"make_panel: {frag!r} is not in line {ln} of the chapter")


def t(x, y, s, weight=400, fill=mc.INK, anchor="start"):
    return f'<text x="{x:.2f}" y="{y:.2f}" {SANS} font-size="{F}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'


def panel():
    col_w, x2 = 78.0, 86.0
    out = [t(0, 4, "Decided", 800), t(x2, 4, "Open at 19:00", 800, fill=mc.ACCENT), t(x2, 8.4, LINES[1][0] + ".", fill=mc.MUTED)]
    for j, r in enumerate(textwrap.wrap(LINES[0][0] + ".", 44)):
        out.append(t(0, 8.4 + j * 4.1, r, fill=mc.MUTED))
    y = 17
    for i, (what, _) in enumerate(DECIDED):
        out.append(f'<rect x="0" y="{y:.1f}" width="{col_w}" height="10" rx="1.5" fill="#fff" stroke="{mc.INK}" stroke-width=".4"/>'
                   f'<path d="M3.6 {y + 5.2:.1f} l2 2 l3.6 -4" fill="none" stroke="{mc.INK}" stroke-width=".7" stroke-linecap="round"/>')
        out.append(t(12, y + 6.4, what[0].upper() + what[1:]))
        y += 12.4
    y2 = 17
    for name, _, words in OPEN:
        rows = textwrap.wrap(words + ("." if not words.endswith(".") else ""), 44)
        h = 6.8 + 4.1 * len(rows)
        out.append(f'<rect x="{x2}" y="{y2:.1f}" width="{col_w}" height="{h:.1f}" rx="1.5" fill="#fff" stroke="{mc.ACCENT}" stroke-width=".5" stroke-dasharray="1.6 1"/>')
        out.append(t(x2 + 3, y2 + 5.2, name, 800, fill=mc.ACCENT))
        for j, r in enumerate(rows):
            out.append(t(x2 + 3, y2 + 9.4 + j * 4.1, r))
        y2 += h + 2.4
    bottom = max(y, y2) + 4
    out.append(f'<rect x="0" y="{bottom:.1f}" width="164" height="14" rx="1.5" fill="{mc.FILL}"/>')
    out.append(t(4, bottom + 5.6, f"{LINES[3][0][0].upper() + LINES[3][0][1:]}:", 400, fill=mc.MUTED))
    out.append(t(4, bottom + 10.4, f"“{LINES[2][0]}”", 800))
    return mc.svg(164, round(bottom + 15, 1), "".join(out),
                  "Chapter 6: the decisions the work waited on, made; the governance ones, open at the end of the day")


if __name__ == "__main__":
    check()
    (HERE / "panel.svg").write_text(panel())
    print("panel.svg written; every fragment found in its line")


# ---- the timeline half (C104, C072), added 2 November 2026 at the researcher's registration ----
import json, re

TIMELINE = [("feedback_round", "the feedback round"), ("decisions_round", "the decisions round"),
            ("longer_work_step", "the longer work step"), ("two_members_brought_on", "two members brought on"),
            ("policies_agreed", "the policies agreed")]


def hm(s):
    m = re.search(r"(\d\d):(\d\d)", s)
    return int(m[1]) * 60 + int(m[2]), f"{m[1]}:{m[2]}"


def timeline():
    reg = {c["id"]: c for c in json.loads((REPO / "claims" / "register.json").read_text())["claims"]}
    v, end = reg["C104"]["value"], reg["C072"]["value"]
    t0, t1, x0, x1, base = 13 * 60 + 30, 18 * 60, 6.0, 158.0, 30.0
    sx = lambda m: x0 + (m - t0) / (t1 - t0) * (x1 - x0)
    out = [f'<line x1="{x0}" y1="{base}" x2="{x1}" y2="{base}" stroke="{mc.INK}" stroke-width=".4"/>']
    for h in range(14, 19):
        out.append(mc.line(sx(h * 60), base, sx(h * 60), base + 1.6, mc.INK, .35) + t(sx(h * 60), base + 5.6, f"{h}:00", 400, mc.MUTED, "middle"))
    rows = []
    for i, (key, words) in enumerate(TIMELINE):
        d = v[key]
        m, label = hm(d["recorded"])
        x = sx(m)
        if "given" in d:  # the time he gave it, the record's own 'about', lighter
            g, glabel = hm(d["given"])
            out.append(f'<circle cx="{sx(g):.2f}" cy="{base}" r="1.5" fill="#fff" stroke="{mc.MUTED}" stroke-width=".4" stroke-dasharray=".6 .5"/>')
        out.append(f'<circle cx="{x:.2f}" cy="{base}" r="1.7" fill="{mc.ACCENT}"/>')
        rows.append((x, words, label, d.get("given")))
    # labels on alternating levels above the line, the 15:16 to 15:25 cluster spread out
    # (label x, label y): the 15:16 to 15:25 cluster spread left, below and right, so no two labels touch
    place = [(None, 15.0), (40.0, 6.5), (None, 23.5), (100.0, 6.5), (None, 15.0)]
    for i, (x, words, label, given) in enumerate(rows):
        px, y = place[i]
        lx = min(max(px if px is not None else x, 22), 142)
        out.append(mc.line(x, base - 2, lx, y + 1.4, mc.FILL2, .3))
        extra = f", about {hm(given)[1]}" if given else ""
        out.append(t(lx, y - 3.4, words, 700, anchor="middle") + t(lx, y + .6, f"recorded {label}{extra}", 400, mc.MUTED, "middle"))
    out.append(t(x1, base + 11, f"at the end of the day: {end['agreed']} policies agreed (C072)", 400, mc.MUTED, "end"))
    out.append(f'<circle cx="{x0 + 1.5}" cy="{base + 9.8:.1f}" r="1.5" fill="#fff" stroke="{mc.MUTED}" stroke-width=".4" stroke-dasharray=".6 .5"/>'
               + t(x0 + 4.4, base + 11, "about: when he gave it, in the record's own words", 400, mc.MUTED)
               + f'<circle cx="{x0 + 1.5}" cy="{base + 14.8:.1f}" r="1.7" fill="{mc.ACCENT}"/>'
               + t(x0 + 4.4, base + 16, "recorded: the commit that carries it (C104)", 400, mc.MUTED))
    return mc.svg(164, round(base + 18, 1), "".join(out), "The afternoon's five decisions on one line of time, each at the commit that recorded it")


if __name__ == "__main__":
    (HERE / "timeline.svg").write_text(timeline())
    print("timeline.svg written from C104 and C072")
