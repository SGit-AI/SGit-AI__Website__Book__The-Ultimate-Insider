#!/usr/bin/env python3
"""LAB 43: RC2's pictures for the full book (manuscript/rc2/150/, read only) that are its own, not the seventy's again.

    python3 lab/experiments/43-designer-rc2-full-book/make_pictures.py
- ch-hour-03.svg, ch-hour-04.svg, ch-hour-05.svg, ch-hour-15.svg: one hour's wakes by trigger as a card, the scheduled
  and editor counts read from C087's by_hour_UTC (clock hours, CK1: hour three is 02:00 to 02:59 UTC), its totals
  checked at build as the day-by-trigger drawing does.
No other number. One SVG unit a millimetre, sizes stated, text 9 pt.
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

F = 3.18
SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'
REG = {c["id"]: c for c in json.loads((REPO / "claims" / "register.json").read_text())["claims"]}
WORDS = {3: "three", 4: "four", 5: "five", 15: "fifteen"}


def t(x, y, s, weight=400, fill=mc.INK, anchor="start", size=F):
    from html import escape
    return (f'<text x="{x:.2f}" y="{y:.2f}" {SANS} font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}">{escape(str(s), quote=False)}</text>')


def by_hour():
    v = REG["C087"]["value"]
    hours = {}
    for k, s in v["by_hour_UTC"].items():
        if "to" in k:
            continue
        nums = [int(n) for n in re.findall(r"\d+", s)]
        hours[int(k)] = (nums[0], nums[1] if len(nums) > 1 and "follow" not in s.split(",")[1] else 0,
                         nums[-1] if "follow" in s else 0)
    if sum(e for _, e, _ in hours.values()) != v["editor"] or sum(f for _, _, f in hours.values()) != v["follow-up"]:
        sys.exit("make_pictures: C087's hours do not add up to its totals")
    return hours


def hour_card(hour):
    s, e, f = by_hour()[hour - 1]  # clock hour N runs from (N-1):00 UTC
    if f:
        sys.exit("make_pictures: this card shows two kinds; the hour has follow-ups too")
    W, x0 = 120.0, 40.0
    out = [f'<rect x=".3" y=".3" width="163.4" height="34" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>',
           t(5, 9, f"hour {WORDS[hour]}", 800, mc.INK, size=4.6), t(5, 14.4, f"{hour - 1:02d}:00 to {hour - 1:02d}:59", 400, mc.MUTED)]
    total = s + e
    x = x0
    for n, words, col in ((s, "started by the schedule", mc.MUTED), (e, "started by the editor", mc.ACCENT)):
        w = W * n / total
        out.append(f'<rect x="{x:.2f}" y="6" width="{w:.2f}" height="9" fill="{col}"/>')
        anchor, tx = ("start", x + 1.4) if col == mc.MUTED else ("end", x + w - 1.4)
        if col == mc.ACCENT and w < 30:
            anchor, tx = "end", x0 + W
        out.append(t(tx, 21.4, str(n), 800, mc.ACCENT if col == mc.ACCENT else mc.INK, anchor) + t(tx, 25.8, words, 400, mc.MUTED, anchor))
        x += w
    out.append(t(5, 31.6, f"the hour's wakes by what started them (C087); clock hours of 29 October, UTC", 400, mc.MUTED))
    return mc.svg(164, 35, "".join(out), f"A card: hour {WORDS[hour]}'s wakes by trigger, the schedule's and the editor's")


if __name__ == "__main__":
    files = {f"ch-hour-{h:02d}.svg": hour_card(h) for h in WORDS}
    for name, svg in files.items():
        (HERE / name).write_text(svg)
    print("written " + ", ".join(files))
