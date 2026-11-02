#!/usr/bin/env python3
"""LAB 39: RC2's pictures for the thirty's chapter 4 (the stop) that are the designer's (manuscript/rc2/30/04, read only).

    python3 lab/experiments/39-designer-rc2-chapter-4/make_pictures.py <read-only clone of the talk's repository>
- ch4-last-ten-minutes.svg: every commit at 298be4e from 18:36 to 18:46 a dot (read with git at build); the named moments
  labelled with their claim ids where the register has them (C006, C065, C005) and their commits where it has none.
- ch4-clock-stopped.svg: the wake clock from chapter 2 greyed, one small file on top; a card: what landed after the hold,
  its gap computed from the two commits and checked against C065.
- ch4-did-not-work.svg: five cards, each with its id (none where the record line gives none).
The three speech cards wait: C089 is open in the register. No other number; sizes stated; text 9 pt.
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


def commits(clone):
    out = subprocess.run(["git", "-C", clone, "log", "298be4e", "--since=2026-10-29T18:36:00Z", "--until=2026-10-29T18:47:00Z",
                          "--format=%h %ct %s"], capture_output=True, text=True, check=True, env={"TZ": "UTC", "PATH": "/usr/bin:/bin"}).stdout
    rows = []
    for line in out.splitlines():
        h, ts, subj = line.split(" ", 2)
        rows.append((h, int(ts), subj))
    return sorted(rows, key=lambda r: r[1])


# the named moments: commit, words (from its subject or the register), the id shown
NAMED = [("dbd75ad", "the player's last fix", "dbd75ad"),
         ("2ed6427", "part 1 not yet locked; lock asked for", "2ed6427, C027"),
         ("867f8c2", "the hold", "C006"),
         ("88b8f00", "work after the hold", "C065"),
         ("cb5b996", "the last release", "C005")]


def last_ten(clone):
    rows = commits(clone)
    t0 = min(r[1] for r in rows) // 60 * 60  # 18:36:00
    t0 = t0 - (t0 % 60)
    span = 11 * 60
    x0, x1, base = 6.0, 158.0, 40.0
    sx = lambda ts: x0 + (ts - t0) / span * (x1 - x0)
    out = [f'<line x1="{x0}" y1="{base}" x2="{x1}" y2="{base}" stroke="{mc.INK}" stroke-width=".4"/>']
    for m in range(0, 11, 2):
        x = sx(t0 + m * 60)
        out.append(mc.line(x, base, x, base + 1.4, mc.INK, .35) + t(x, base + 5.4, f"18:{36 + m:02d}", 400, mc.MUTED, "middle"))
    named = {h: (w, i) for h, w, i in NAMED}
    stacks = {}
    for h, ts, subj in rows:
        k = round(sx(ts) / 1.6)
        n = stacks.get(k, 0); stacks[k] = n + 1
        fill = mc.ACCENT if h in named else mc.MUTED
        out.append(f'<circle cx="{sx(ts):.2f}" cy="{base - 2 - n * 2.4:.2f}" r="1" fill="{fill}"/>')
    place = {"dbd75ad": (18, 9), "2ed6427": (52, 16), "867f8c2": (98, 9), "88b8f00": (118, 23), "cb5b996": (150, 9)}
    by_hash = {h: ts for h, ts, _ in rows}
    for h, (words, ids) in named.items():
        if h not in by_hash:
            sys.exit(f"make_pictures: {h} not in the window")
        lx, ly = place[h]
        x = sx(by_hash[h])
        out.append(mc.line(x, base - 3, lx, ly + 1.4, mc.FILL2, .3))
        out.append(t(lx, ly - 2.6, words, 700, anchor="middle") + t(lx, ly + 1.2, ids, 400, mc.MUTED, "middle"))
    out.append(t(x0, base + 11, "every commit from 18:36 to 18:46 at 298be4e, one dot each; the named ones in the accent", 400, mc.MUTED))
    return mc.svg(164, base + 13, "".join(out), "The last ten minutes before the talk was due, every commit a dot, the named moments labelled")


def clock_stopped(clone):
    slots = REG["C071"]["value"]
    hold, work = REG["C065"]["value"]["hold"].split(), REG["C065"]["value"]["designer"].split()
    times = {h: ts for h, ts, _ in commits(clone)}
    gap = times[work[0]] - times[hold[0]]
    if gap != REG["C065"]["value"]["gap_seconds"]:
        sys.exit(f"make_pictures: the commits give {gap} s, C065 says {REG['C065']['value']['gap_seconds']}")
    cx, cy, R = 44, 40, 30
    out = [f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{mc.FILL2}" stroke-width="1"/>']
    for member, mm in slots.items():
        a = math.radians(int(mm.strip(":")) * 6 - 90)
        out.append(f'<g transform="translate({cx + (R + 6) * math.cos(a) - 2.8:.2f} {cy + (R + 6) * math.sin(a) - 2.5:.2f}) scale(.14)">{mc.head(member, False)}</g>')
    out.append(f'<path d="M{cx - 8} {cy - 10} h12 l4 4 v16 h-16 z" fill="#fff" stroke="{mc.INK}" stroke-width=".6"/>'
               f'<path d="M{cx + 4} {cy - 10} v4 h4" fill="none" stroke="{mc.INK}" stroke-width=".5"/>'
               + t(cx, cy + 1.2, "HOLD", 800, mc.ACCENT, "middle"))
    out.append(f'<rect x="92" y="18" width="70" height="40" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>'
               + t(96, 26, "what landed after the hold", 800)
               + f'<text x="96" y="40" {SANS} font-size="11" font-weight="800" fill="{mc.ACCENT}">{gap} seconds</text>'
               + t(96, 47, "the designer's work, already in flight", 400)
               + t(96, 53, f"{hold[0]} to {work[0]} (C065)", 400, mc.MUTED))
    return mc.svg(164, 80, "".join(out), "The wake clock greyed, the hold on top of it, and what landed after it")


CARDS = [("the lock never turned", "C027"), ("two parts of three unfinished", "C027"), ("the moment missed", "the storyteller's debrief"),
         ("the correction lost in the freeze", "C031"), ("the three claims that did not hold", "C029, C030")]


def did_not_work():
    for _, ids in CARDS:
        for cid in [i.strip() for i in ids.split(",") if i.strip().startswith("C")]:
            if REG[cid]["state"] != "checked":
                sys.exit(f"make_pictures: {cid} is {REG[cid]['state']}")
    out = []
    for i, (words, ids) in enumerate(CARDS):
        x, y = (i % 3) * 54.6, (i // 3) * 22
        out.append(f'<rect x="{x + .3:.1f}" y="{y + .3}" width="52.6" height="19.6" rx="1.8" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>'
                   f'<path d="M{x + 3} {y + 4} l3.4 3.4 M{x + 6.4} {y + 4} l-3.4 3.4" stroke="{mc.ACCENT}" stroke-width=".8"/>'
                   + t(x + 9, y + 7, "did not work", 800, mc.ACCENT) + t(x + 3, y + 12.8, words) + t(x + 3, y + 17.4, ids, 400, mc.MUTED))
    return mc.svg(164, 44, "".join(out), "Five cards: what did not work on the day, each with where it rests")


if __name__ == "__main__":
    clone = sys.argv[1]
    for name, svg in {"ch4-last-ten-minutes.svg": last_ten(clone), "ch4-clock-stopped.svg": clock_stopped(clone),
                      "ch4-did-not-work.svg": did_not_work()}.items():
        (HERE / name).write_text(svg)
    print("written ch4-last-ten-minutes.svg, ch4-clock-stopped.svg, ch4-did-not-work.svg")
