#!/usr/bin/env python3
"""LAB 35: chapter 6's picture, the half that does not wait on registered times: decided, and open at 19:00.

    python3 lab/experiments/35-designer-chapter-6-decided-and-open/make_panel.py
Every word on the panel is a fragment of manuscript/06-the-editor-signs.md, checked here against its line before
drawing (the script stops if a fragment is not in its line). The only number is the section's own 19:00, the end of
the day in C037's span (C037 is open in the register; it is cited for the span only). A proposal: the fragments go to
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
