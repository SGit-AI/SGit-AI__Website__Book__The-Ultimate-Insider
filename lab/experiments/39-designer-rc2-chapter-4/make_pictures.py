#!/usr/bin/env python3
"""LAB 39: RC2's pictures for the thirty's chapter 4 (the stop) that are the designer's (manuscript/rc2/30/04, read only).

    python3 lab/experiments/39-designer-rc2-chapter-4/make_pictures.py <read-only clone of the talk's repository>
- ch4-last-ten-minutes.svg: every commit at 298be4e from 18:36 to 18:46 a dot (read with git at build); the named moments
  labelled with their claim ids where the register has them (C006, C065, C005) and their commits where it has none.
- ch4-clock-stopped.svg: the wake clock from chapter 2 greyed, one small file on top; a card: what landed after the hold,
  its gap computed from the two commits and checked against C065.
- ch4-did-not-work.svg: five cards, each with its id (none where the record line gives none).
- ch4-speech-cards.svg: three equal cards, the signed narrator figure (DR1) on each, its date and the editor's words
  verbatim (the researcher's letter 006), each checked at build against its source: the hold file at 298be4e (with git,
  read only), and the two briefs in this repository. In the Figure line's order, none larger: C089 is open on which
  account the book leads with. No other number; sizes stated; text 9 pt.
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
        # the moment's words only: its hashes and ids live on the record line (P28, convention 8; critic3 007)
        out.append(t(lx, ly - .6, words, 700, anchor="middle"))
    return mc.svg(164, base + 7, "".join(out), "The last ten minutes before the talk was due, every commit a dot, the named moments labelled")


def clock_stopped(clone):
    slots = REG["C071"]["value"]
    hold, work = REG["C065"]["value"]["hold"].split(), REG["C065"]["value"]["designer"].split()
    times = {h: ts for h, ts, _ in commits(clone)}
    gap = times[work[0]] - times[hold[0]]
    if gap != REG["C065"]["value"]["gap_seconds"]:
        sys.exit(f"make_pictures: the commits give {gap} s, C065 says {REG['C065']['value']['gap_seconds']}")
    # sized to its content (conductor 055): 134 mm wide, the dial smaller, the gap at 18 pt so it sits inside its card
    cx, cy, R = 32, 32, 23
    out = [f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{mc.FILL2}" stroke-width=".9"/>']
    for member, mm in slots.items():
        a = math.radians(int(mm.strip(":")) * 6 - 90)
        out.append(f'<g transform="translate({cx + (R + 5) * math.cos(a) - 2.8:.2f} {cy + (R + 5) * math.sin(a) - 2.5:.2f}) scale(.14)">{mc.head(member, False)}</g>')
    out.append(f'<path d="M{cx - 7} {cy - 9} h10 l4 4 v14 h-14 z" fill="#fff" stroke="{mc.INK}" stroke-width=".55"/>'
               f'<path d="M{cx + 3} {cy - 9} v4 h4" fill="none" stroke="{mc.INK}" stroke-width=".45"/>'
               + t(cx, cy + 1.2, "HOLD", 800, mc.ACCENT, "middle"))
    out.append(f'<rect x="70" y="14" width="63.5" height="36" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>'
               + t(74, 21.5, "what landed after the hold", 800)
               + f'<text x="74" y="32" {SANS} font-size="6.4" font-weight="800" fill="{mc.ACCENT}">{gap} seconds</text>'
               + t(74, 39.5, "the designer's work, already in flight", 400)
               + t(74, 45.5, f"{hold[0]} to {work[0]} (C065)", 400, mc.MUTED))
    return mc.svg(134, 64, "".join(out), "The wake clock greyed, the hold on top of it, and what landed after it")


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


# date, the words (verbatim), the caption, and where the build finds them: ("git", path at 298be4e) or ("repo", path)
SPEECH = [("29 October, 18:44", "actually we are at 95% so it is better to pause all actions", "as the hold file gives it",
           ("git", "team/conductor/HOLD.md")),
          ("31 October, early hours", "the 95%, it's an interesting point, but it's just a footnote", "dictated review, after the day",
           ("repo", "briefs/2026-10-31__rc1-paper-review/batch-07-pages-22-to-32.md")),
          ("31 October, evening", "The 95%, I think, was the tokens usage.", "in session, after the day",
           ("repo", "briefs/2026-10-31__in-session/02-g1-the-95-and-the-day-in-review.md"))]


def speech_cards(clone):
    import textwrap
    for _, words, _, (kind, path) in SPEECH:
        src = (subprocess.run(["git", "-C", clone, "show", f"298be4e:{path}"], capture_output=True, text=True, check=True).stdout
               if kind == "git" else (REPO / path).read_text())
        if words not in src:
            sys.exit(f"make_pictures: {words!r} not in {path}")
    if REG["C089"]["state"] == "checked":
        sys.exit("make_pictures: C089 is checked now: see whether the lead is signed before the cards stay equal")
    w, gap, out = 52.2, 3.3, []
    rows = [textwrap.wrap(f"\u201c{words}\u201d", 27) for _, words, _, _ in SPEECH]
    h = 34 + 4.1 * max(len(r) for r in rows) + 9
    for i, ((date, _, cap, _), r) in enumerate(zip(SPEECH, rows)):
        x = i * (w + gap)
        out.append(f'<rect x="{x + .3:.1f}" y=".3" width="{w}" height="{h:.1f}" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>'
                   + f'<g transform="translate({x + 2:.1f} 2) scale(.56)">{mc.editor_figure("A")}</g>'
                   + t(x + 26, 12, "the editor", 800) + t(x + 26, 16.6, date.split(", ")[0] + ",", 400, mc.MUTED)
                   + t(x + 26, 20.8, date.split(", ")[1], 400, mc.MUTED))
        for j, line in enumerate(r):
            out.append(t(x + 3, 34 + j * 4.1, line, 400))
        out.append(t(x + 3, h - 2.6, cap, 400, mc.MUTED))
    out.append(t(0, h + 5, "three accounts, equal and in the order given: which one leads is the editor's to sign (C089, open)", 400, mc.MUTED))
    return mc.svg(164, round(h + 6.6, 1), "".join(out), "Three speech cards from the editor, each dated, his words verbatim, none larger")


def book_team_figures():
    out = []
    for i, m in enumerate(["librarian", "historian", "publisher", "writer"]):  # chapter 5's four speakers, as first drawn
        x = i * 41
        out.append(f'<g transform="translate({x + 6} 0) scale(.7)">{mc.figure(m)}</g>' + t(x + 20, 39.4, m, 700, anchor="middle")
                   + t(x + 20, 43.8, mc.BOOK_TEAM[m][2], 400, mc.MUTED, "middle"))
    return mc.svg(164, 46, "".join(out), "This book's four speakers drawn in the cast's style: the librarian, the historian, the publisher, the writer")


if __name__ == "__main__":
    clone = sys.argv[1]
    for name, svg in {"ch4-last-ten-minutes.svg": last_ten(clone), "ch4-clock-stopped.svg": clock_stopped(clone),
                      "ch4-did-not-work.svg": did_not_work(), "ch4-speech-cards.svg": speech_cards(clone),
                      "book-team-figures.svg": book_team_figures()}.items():
        (HERE / name).write_text(svg)
    print("written ch4-last-ten-minutes.svg, ch4-clock-stopped.svg, ch4-did-not-work.svg, ch4-speech-cards.svg, book-team-figures.svg")
