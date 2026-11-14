#!/usr/bin/env python3
"""LAB 80: the experiments that led to the day, as a timeline (PEN1 note 24, the editor on 00b's paragraph about
Black Hat Europe, VoiceDebrief and ruv.sgit.ai: "This deserves a timeline infographic").

    python3 lab/experiments/80-designer-experiments-timeline/make_timeline.py

Drawn from one chain only, the researcher's 045 (with 046), and its three conditions (the conductor's 096):
- it is labelled as the editor's own account, the article "The scripted talk" (15 October 2026), not the day's record;
- 15 October is drawn as "due", never "given" (the article, written that day, says "It has not been given yet");
- nothing dated after 29 October 2026.
Each node keeps its register id here, never on the page. Writes timeline.svg.
"""
import re, sys
from datetime import date
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'
SERIF = 'font-family="Georgia, \'DejaVu Serif\', serif"'
PT = 0.3528
W, H = 156.0, 114.0
LAST = date(2026, 10, 29)

# (date, heading, what it tried, register ids): researcher 045, items 1 to 4
CHAIN = [
    (date(2025, 12, 9), "Black Hat Europe keynote", ["Slides as one JSON file:", "26 slides, seven layouts,", "fully generated from scripts"], "C116"),
    (date(2026, 9, 2), "VoiceDebrief pitch", ["To Founder Institute: a presenter", "with per-slide timings, a three-", "minute countdown, speaker notes"], "C116"),
    (date(2026, 10, 14), "The first talk.json", ["A five-minute demo", "built for ruv.sgit.ai"], "C116"),
    (date(2026, 10, 15), "Agentic Engineering Live, London", ["The event the demo was due at"], "C116"),
    (date(2026, 10, 29), "The day", ["00:16  the empty project", "15:07  the player ported from ruv.sgit.ai", "19:00  the talk, due"], "C001 C028 C100"),
]


def t(x, y, s, weight=400, fill=mc.INK, size=3.18, fam=SANS, anchor=""):
    a = f' text-anchor="{anchor}"' if anchor else ""
    return (f'<text x="{x:.2f}" y="{y:.2f}" {fam} font-size="{size:.2f}" font-weight="{weight}" fill="{fill}"{a}>'
            f'{escape(str(s), quote=False)}</text>')


def dot(x, y, filled=True, r=1.5):
    if filled:
        return f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="{mc.ACCENT}"/>'
    return f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="{mc.PAPER}" stroke="{mc.ACCENT}" stroke-width=".5"/>'


def day(d):
    return f"{d.day} {d.strftime('%b')} {d.year}"


def main():
    if any(d > LAST for d, *_ in CHAIN):
        sys.exit("make_timeline: a node is dated after 29 October 2026")
    b = [t(0, 7, "Before the day: from slides as data to the day", 800, mc.INK, size=15 * PT),
         t(0, 12.5, "As the editor tells it in the article “The scripted talk” (15 October 2026),",
           400, mc.MUTED, size=9 * PT, fam=SERIF),
         t(0, 16.6, "not the record of the day.", 400, mc.MUTED, size=9 * PT, fam=SERIF)]

    # the long view: December 2025 to the end of October 2026, to scale
    y = 33.0
    d0, d1 = date(2025, 12, 1), date(2026, 11, 1)
    x0, x1 = 2.0, W - 2.0
    X = lambda d: x0 + (d - d0).days / (d1 - d0).days * (x1 - x0)
    b.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{mc.FILL2}" stroke-width=".8"/>')
    for yr, mo in [(2026, m) for m in range(1, 12)]:
        xm = X(date(yr, mo, 1))
        b.append(f'<line x1="{xm:.2f}" y1="{y - 1}" x2="{xm:.2f}" y2="{y + 1}" stroke="{mc.FILL2}" stroke-width=".4"/>')
    b.append(t(x0, y + 5, "Dec 2025", 400, mc.MUTED, size=9 * PT))
    b.append(t(x1, y + 5, "Oct 2026", 400, mc.MUTED, size=9 * PT, anchor="end"))
    for d, head, lines, _ in CHAIN[:2]:
        x = X(d)
        b.append(dot(x, y))
        anchor = "" if x < W / 2 else "end"
        tx = x - 1 if anchor == "" else x + 1.5
        tx = max(tx, 0)
        b.append(t(tx, y - 9.5, day(d), 700, mc.ACCENT, size=9 * PT, anchor=anchor))
        b.append(t(tx, y - 5, head, 800, mc.INK, size=10 * PT, anchor=anchor))
        for i, l in enumerate(lines):
            b.append(t(tx, y + 10 + i * 4.1, l, 400, mc.INK, size=9 * PT, fam=SERIF, anchor=anchor))
    # the last fortnight, gathered at the right end, opens below
    xa, xb = X(date(2026, 10, 14)), X(LAST)
    b.append(f'<rect x="{xa - 1:.2f}" y="{y - 2.2}" width="{xb - xa + 2:.2f}" height="4.4" rx="1" fill="none" stroke="{mc.ACCENT}" stroke-width=".4"/>')
    for d, *_ in CHAIN[2:]:
        b.append(dot(X(d), y, d != date(2026, 10, 15), r=1.0))

    # October, closer: 13 to 30 October, to scale
    yz = 86.0
    z0, z1 = date(2026, 10, 13), date(2026, 10, 31)
    u0, u1 = 2.0, W - 2.0
    Z = lambda d: u0 + (d - z0).days / (z1 - z0).days * (u1 - u0)
    b.append(t(u0, y + 24.5, "October 2026, closer: the last fortnight, boxed above", 700, mc.MUTED, size=9 * PT))
    b.append(f'<line x1="{u0}" y1="{yz}" x2="{u1}" y2="{yz}" stroke="{mc.FILL2}" stroke-width=".8"/>')
    for k in range(13, 31):
        xk = Z(date(2026, 10, k))
        b.append(f'<line x1="{xk:.2f}" y1="{yz - .8}" x2="{xk:.2f}" y2="{yz + .8}" stroke="{mc.FILL2}" stroke-width=".3"/>')
    # 14 and 15 October: one above, one below, so the two days do not collide
    d, head, lines, _ = CHAIN[2]
    x = Z(d)
    b.append(dot(x, yz))
    b.append(t(x - 1, yz - 18.2, day(d), 700, mc.ACCENT, size=9 * PT))
    b.append(t(x - 1, yz - 13.8, head, 800, mc.INK, size=10 * PT))
    for i, l in enumerate(lines):
        b.append(t(x - 1, yz - 9 + i * 4.2, l, 400, mc.INK, size=9 * PT, fam=SERIF))
    d, head, lines, _ = CHAIN[3]
    x = Z(d)
    b.append(dot(x, yz, filled=False))
    b.append(t(x - 1, yz + 7, f"{day(d)}: due, not given", 700, mc.ACCENT, size=9 * PT))
    b.append(t(x - 1, yz + 11.4, head, 800, mc.INK, size=10 * PT))
    b.append(t(x - 1, yz + 15.8, lines[0], 400, mc.INK, size=9 * PT, fam=SERIF))
    # 14 days, from 15 to 29 October
    d, head, lines, _ = CHAIN[4]
    xd = Z(d)
    yb = yz + 22
    b.append(f'<path d="M{x:.2f},{yb - 1.5} L{x:.2f},{yb} L{xd:.2f},{yb} L{xd:.2f},{yb - 1.5}" stroke="{mc.MUTED}" stroke-width=".35" fill="none"/>')
    b.append(t((x + xd) / 2, yb + 4.2, "14 days", 700, mc.MUTED, size=9 * PT, anchor="middle"))
    b.append(dot(xd, yz, r=2.0))
    b.append(t(xd + 1.5, yz - 22.6, day(d), 700, mc.ACCENT, size=9 * PT, anchor="end"))
    b.append(t(xd + 1.5, yz - 18.2, head, 800, mc.INK, size=10 * PT, anchor="end"))
    for i, l in enumerate(lines):
        b.append(t(xd + 1.5, yz - 13.4 + i * 4.2, l, 400, mc.INK, size=9 * PT, fam=SERIF, anchor="end"))

    svg = mc.svg(W, H, "".join(b), "Before the day, as the editor tells it: Black Hat Europe on 9 December 2025, "
                 "the VoiceDebrief pitch on 2 September 2026, the first talk.json on 14 October, due at Agentic "
                 "Engineering Live on 15 October, and the day itself, 14 days later, on 29 October 2026.")
    if re.search(r">[^<]*\b(C\d{3}|[0-9a-f]{7,})\b", svg) or "@" in re.sub(r"<[^>]+>", "", svg):
        sys.exit("make_timeline: an id, a hash or an address is drawn")
    if "\u2014" in svg or re.search(r">[^<]*\bgiven\b", svg.replace("not given", "")):
        sys.exit("make_timeline: an em-dash, or 15 October drawn as given")
    (HERE / "timeline.svg").write_text(svg)
    print("written timeline.svg")


if __name__ == "__main__":
    main()
