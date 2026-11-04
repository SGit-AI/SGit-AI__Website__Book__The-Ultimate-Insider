#!/usr/bin/env python3
"""LAB 55: the researcher's findings of the night as cards (chapter 8, line 161; chapter 9, line 50: ruv-sgit's 073 and
074, the writer's 229), and chapter 4's banner pair (line 147).

    python3 lab/experiments/55-designer-findings-cards/make_cards.py

The cards read C025 at build: when each finding was found against the 02:22 push, and what was fixed, with the counts
the briefs allow. Under the briefs' rail and the editor's D12: nothing of what was captured, how, or from where; no
value, site, field, pattern or kind of value; nothing of C068's own times. The wording on the cards is the designer's,
from those counts and times only.

The banner pair reads the writer's own start and end banner from its debrief (team/writer/debriefs/
2026-11-04__after-the-hold.md), as the writer gave them for this figure: no model line, key, token or session id. The
build stops if either banner carries "model", "session_" or a key-like run.
"""
import json, re, sys
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'
MONO = 'font-family="DejaVu Sans Mono, monospace"'
PUSH = "02:22"


def t(x, y, s, weight=400, fill=mc.INK, anchor="start", size=3.18, font=SANS):
    return (f'<text x="{x:.2f}" y="{y:.2f}" {font} font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}" xml:space="preserve">{escape(str(s), quote=False)}</text>')


def findings():
    reg = {c["id"]: c for c in json.loads((REPO / "claims" / "register.json").read_text())["claims"]}
    if reg["C025"]["state"] != "checked":
        sys.exit("make_cards: C025 is not checked")
    v = reg["C025"]["value"]
    night = [e for e in v if e["wake"].startswith("researcher ")]
    times = [e["wake"].split()[1] for e in night]
    if times != ["03:05", "04:10", "06:14"] or not all(PUSH in json.dumps(v) for _ in [0]):
        sys.exit("make_cards: C025's night findings are not the three the cards expect")
    if "28" not in night[1]["finding"] or "30 files" not in night[1]["fixed"] or "10 " not in night[2]["finding"]:
        sys.exit("make_cards: C025's counts are not as the cards give them")
    # the designer's wording, counts and times only (the rail: no kind of value, no site, field or pattern)
    return [(times[0], "the first, found after the push", "redacted in the files; the push stays in the history; the editor told"),
            (times[1], "the second, found before the close", "28 values counted; 30 files redacted in the same wake; 0 left"),
            (times[2], "the third, missed by the first check", "10 pages redacted in the same wake; 0 left")]


def card(x, y, w, when, head, fixed):
    import textwrap
    rows = textwrap.wrap(fixed, int(w / 1.75))
    heads = textwrap.wrap(head, int(w / 1.95))
    hy = 4.1 * len(heads)
    h = 10.9 + hy + 4.1 * len(rows)
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w}" height="{h:.1f}" rx="1.8" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>'
            + t(x + 3, y + 7, f"found at {when}", 800, mc.ACCENT, size=4.2)
            + "".join(t(x + 3, y + 11.6 + j * 4.1, r, 700) for j, r in enumerate(heads))
            + "".join(t(x + 3, y + 11.9 + hy + j * 4.1, r, 400, mc.MUTED) for j, r in enumerate(rows))), h


def cards_08():
    f = findings()[:2]
    out, hs = [], []
    for k, (when, head, fixed) in enumerate(f):
        s, h = card(k * 79.5 + .3, 9, 76, when, head, fixed)
        out.append(s); hs.append(h)
    out.insert(0, t(0, 4.6, f"against the push at {PUSH}", 700, mc.INK))
    return mc.svg(156, round(9 + max(hs) + .6, 1), "".join(out), "The researcher's two findings of the small hours, side by side")


def cards_09():
    f = findings()
    out, hs = [], []
    for k, (when, head, fixed) in enumerate(f):
        s, h = card(k * 52.5 + .3, 9, 50, when, head, fixed)
        out.append(s); hs.append(h)
    out.insert(0, t(0, 4.6, f"against the push at {PUSH}", 700, mc.INK))
    return mc.svg(158, round(9 + max(hs) + .6, 1), "".join(out), "The researcher's three findings of the night in a row, each with when it was found against the push and what was fixed")


def banners():
    text = (REPO / "team" / "writer" / "debriefs" / "2026-11-04__after-the-hold.md").read_text()
    sec = text.split("## Banners, for the designer", 1)
    if len(sec) < 2:
        sys.exit("make_cards: the writer's debrief has no banners for the designer")
    blocks = re.findall(r"```\n(.+?)\n```", sec[1], re.S)[:2]
    if len(blocks) != 2 or "SESSION START" not in blocks[0] or "SESSION END" not in blocks[1]:
        sys.exit("make_cards: the writer's start and end banners are not as expected")
    for b in blocks:
        if re.search(r"model|session_|[A-Za-z0-9+/]{24,}", b):
            sys.exit("make_cards: a banner carries a model line, a session id or a key-like run")
    out, y, size, lh = [], 4.0, 3.5, 4.3
    for b in blocks:
        for line in b.splitlines():
            out.append(t(0, y, line, 400, mc.INK, size=size, font=MONO))
            y += lh
        y += 3
    return mc.svg(156, round(y - 2, 1), "".join(out), "One banner as a session prints it, and its end twin: the writer's own, from 4 November")


if __name__ == "__main__":
    files = {"ch8-two-findings.svg": cards_08(), "ch9-three-findings.svg": cards_09(), "ch4-banner-pair.svg": banners()}
    for name, svg in files.items():
        if re.search(r">[^<]*\bC\d{3}\b", svg) or re.search(r"cookie|token|vault|anti-forgery|hex", svg, re.I):
            sys.exit(f"make_cards: {name} draws an id or a word the rail keeps out")
        (HERE / name).write_text(svg)
    print("written " + ", ".join(files))
