#!/usr/bin/env python3
"""LAB 58: chapter 10's three notes (manuscript/rc2/150/10-talking-through-git.md, its "three notes as three cards on a
line of time" figure). The notes word for word, as the chapter quotes them from their commits, each card with an arrow to
the mailroom it pointed at; beneath, deck's and the researcher's dials with the minutes they wrote at. The times are the
chapter's record line's, and appear in the picture only; no hash and no register id is drawn (storyteller 143).

    python3 lab/experiments/58-designer-three-notes/make_notes.py <the talk's clone, read only>

Since the newsroom's pass 2 the chapter quotes one note and draws the three (writer2 055), so each note is checked word
for word against its own commit's message, read with git, and the record line's times against the chapter.
"""
import re, subprocess, sys, math, textwrap
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'
CH = (REPO / "manuscript" / "rc2" / "150" / "10-talking-through-git.md").read_text()
# (time as the record line gives it, who wrote, [(note word for word, the mailroom it pointed at)])
CARDS = [("09:21", "deck", [("To-ruv-sgit: E03 kept (/studio/reviews/e03.html); E04 over-enthusiastic-agent in your mailroom.", "ruv-sgit"),
                            ("To-researcher: a plain description per capability in the grant rows, in your mailroom.", "researcher")]),
         ("10:14", "researcher", [("To-deck: delivered: evidence/studio/studio-e02-e09-capabilities.json; reply 013 in your mailroom", "deck")]),
         ("10:21", "deck", [("To-ruv-sgit: E09 mandate-and-grant in your mailroom; E04 again (/studio/reviews/e04.html), after E09.", "ruv-sgit")])]
RECORD = "6b55cff (09:21:26) 3f094f2 (10:14:39) 36e382b (10:21:12)"


def t(x, y, s, weight=400, fill=mc.INK, anchor="middle", size=3.18, mono=False):
    fam = 'font-family="JetBrains Mono, Menlo, monospace"' if mono else SANS
    return (f'<text x="{x:.2f}" y="{y:.2f}" {fam} font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}">{escape(str(s), quote=False)}</text>')


SHAS = ["6b55cff", "3f094f2", "36e382b"]  # one per card, in RECORD's order; used to read, never drawn


def check(clone):
    if RECORD not in CH:
        sys.exit("make_notes: the chapter's record line for the three notes has changed")
    for sha, (when, _, notes) in zip(SHAS, CARDS):
        msg = subprocess.run(["git", "-C", clone, "show", "-s", "--format=%cI%n%B", sha], capture_output=True, text=True, check=True).stdout
        if msg[11:16] != when:
            sys.exit(f"make_notes: the commit for the {when} card is not at {when}")
        lines = [l.strip() for l in msg.splitlines()]
        for note, _ in notes:
            if note not in lines:
                sys.exit(f"make_notes: '{note[:40]}...' is not word for word a note on its commit")


def folder(x, y, who):
    name = {"researcher": "the researcher's", "deck": "deck's", "ruv-sgit": "ruv-sgit's"}[who]
    col = mc.COLOUR.get(who, mc.INK) if hasattr(mc, "COLOUR") else mc.INK
    return (f'<path d="M{x - 6:.2f} {y} h4 l1.2 -1.6 h6.8 v7 h-12 z" fill="#fff" stroke="{col}" stroke-width=".6" stroke-linejoin="round"/>'
            + t(x, y + 11, name, 700, mc.INK) + t(x, y + 14.8, "mailroom", 400, mc.MUTED))


def arrow(x1, y1, x2, y2):
    return (f'<path d="M{x1:.2f} {y1:.2f} L{x2:.2f} {y2 - 1.6:.2f}" stroke="{mc.MUTED}" stroke-width=".45" fill="none"/>'
            f'<path d="M{x2 - 1.2:.2f} {y2 - 2.2:.2f} L{x2:.2f} {y2:.2f} L{x2 + 1.2:.2f} {y2 - 2.2:.2f}" stroke="{mc.MUTED}" stroke-width=".45" fill="none"/>')


def dial(cx, cy, r, who, minutes, label):
    col = mc.COLOUR.get(who, mc.INK)
    out = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="{mc.INK}" stroke-width=".5"/>']
    for m in range(0, 60, 5):
        a = math.radians(m * 6 - 90)
        out.append(mc.line(cx + (r - 1.2) * math.cos(a), cy + (r - 1.2) * math.sin(a), cx + r * math.cos(a), cy + r * math.sin(a), mc.MUTED, .35))
    for m in sorted(set(minutes)):
        a = math.radians(m * 6 - 90)
        out.append(f'<path d="M{cx} {cy} L{cx + (r - 2) * math.cos(a):.2f} {cy + (r - 2) * math.sin(a):.2f}" stroke="{col}" stroke-width="1" stroke-linecap="round"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r=".9" fill="{mc.INK}"/>')
    out.append(t(cx + r + 3, cy - 1, label[0], 700, mc.INK, "start"))
    out.append(t(cx + r + 3, cy + 3.4, label[1], 400, mc.MUTED, "start"))
    return "".join(out)


def main():
    check(sys.argv[1])
    cw, gap, x0 = 49.6, 3.0, .3
    out = []
    # the line of time, the three minutes on it
    out.append(mc.line(2, 6.2, 154, 6.2, mc.INK, .5))
    out.append(t(0, 3.4, "the morning of the day", 400, mc.MUTED, "start"))
    tops, bottoms = [], []
    for k, (when, who, notes) in enumerate(CARDS):
        x = x0 + k * (cw + gap)
        rows = []
        for j, (note, _) in enumerate(notes):
            rows += [("q", r) for r in [r.replace("/ ", "/").replace("- ", "-") for r in textwrap.wrap(f"“{note}”".replace("/", "/ ").replace("-", "- "), 27, break_long_words=False)]]
            if j < len(notes) - 1:
                rows.append(("gap", ""))
        h = 11 + 3.9 * len(rows) + 2
        out.append(f'<circle cx="{x + cw / 2:.2f}" cy="6.2" r="1.3" fill="{mc.ACCENT}"/>' + mc.line(x + cw / 2, 7.5, x + cw / 2, 10, mc.ACCENT, .45))
        out.append(f'<rect x="{x:.2f}" y="10" width="{cw}" height="{h:.2f}" rx="1.8" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>')
        out.append(t(x + 3, 15.6, when, 800, mc.ACCENT, "start", size=4.2) + t(x + 18, 15.6, f"from {"the " if who == "researcher" else ""}{who}", 700, mc.INK, "start"))
        yy = 20.4
        for kind, r in rows:
            if kind == "q":
                out.append(t(x + 3, yy, r, 400, mc.INK, "start"))
            yy += 3.9
        bottoms.append((x, 10 + h, notes))
    fy = max(b[1] for b in bottoms) + 9
    for x, bot, notes in bottoms:
        n = len(notes)
        for j, (_, to) in enumerate(notes):
            fx = x + (13 + 24 * j if n > 1 else cw / 2)
            out.append(arrow(fx, bot + .4, fx, fy - 1.9))
            out.append(folder(fx, fy, to))
    dy = fy + 28
    out.append(dial(14, dy, 9, "deck", [21], ("deck's dial", "it wrote at 09:21 and 10:21")))
    out.append(dial(92, dy, 9, "researcher", [14], ("the researcher's dial", "it answered at 10:14")))
    out.append(t(0, dy + 15.5, "each note waited in a mailroom until its reader's next session", 400, mc.MUTED, "start"))
    svg = mc.svg(156, round(dy + 17.5, 1), "".join(out), "Chapter 10's three notes on a line of time: each card a commit's notes word for word, an arrow to the mailroom it pointed at, and deck's and the researcher's dials beneath")
    if re.search(r">[^<]*\b(C\d{3}|[0-9a-f]{7})\b", svg):
        sys.exit("make_notes: an id or a hash is drawn")
    (HERE / "three-notes.svg").write_text(svg)
    print("written three-notes.svg")


if __name__ == "__main__":
    main()
