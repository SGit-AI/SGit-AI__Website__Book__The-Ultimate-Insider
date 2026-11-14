#!/usr/bin/env python3
"""LAB 43: RC2's pictures for the full book (manuscript/rc2/150/, read only) that are its own, not the seventy's again.

    python3 lab/experiments/43-designer-rc2-full-book/make_pictures.py <read-only clone of the talk's repository>
- ch-hour-03.svg, ch-hour-04.svg, ch-hour-05.svg, ch-hour-15.svg: one hour's wakes by trigger as a card, the scheduled
  and editor counts read from C087's by_hour_UTC (clock hours, CK1: hour three is 02:00 to 02:59 UTC), its totals
  checked at build as the day-by-trigger drawing does.
- ch11-two-files.svg: the reality file and the corrections file as two cards, their words verbatim at 298be4e (git), the
  reality file's day as ticks (its commits that day), the corrections file's one entry unchanged since 1f7c633.
- ch8-night-log.svg: the night log's first edition (794008c) drawn as a page: its hour, each member's wakes as outcome
  chips from its own table, what waits on the editor as lines (no item text).
- ch11-reality-card.svg and ch11-corrections-card.svg: the same two cards, one each, half the text width, for the two
  lines that ask for one each (the pair stays in the lab as the side-by-side version).
- ch5-schedule.svg: the schedule as the conductor wrote it at 01:39 (09f13d5): a dial with the first four members at
  their minutes from its runs, and its own words quoted; no session id or prompt printed.
- ch1-still-slide.svg: chapter 1's "the building as a still slide": a box of rooms, a few dots inside, an arrow, and
  a label saying "agents", on a plain slide; the still that would have been shown, so drawn plain on purpose.
No other number. One SVG unit a millimetre, sizes stated, text 9 pt.
"""
import json, re, subprocess, sys
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
    out.append(t(5, 31.6, f"the hour's wakes by what started them; clock hours of 29 October, UTC", 400, mc.MUTED))
    return mc.svg(164, 35, "".join(out), f"A card: hour {WORDS[hour]}'s wakes by trigger, the schedule's and the editor's")


def g(body, x, y, s):
    return f'<g transform="translate({x:.2f} {y:.2f}) scale({s})">{body}</g>'


def git(clone, *a):
    return subprocess.run(["git", "-C", clone, *a], capture_output=True, text=True, check=True).stdout


def two_files(clone, part=None):
    import textwrap
    reality = git(clone, "show", "298be4e:REALITY.md")
    second = reality.split("\n\n")[1].split(". ", 1)[1].strip()
    if not second.startswith("A thing not listed here does not exist"):
        sys.exit("make_pictures: REALITY.md's second sentence is not as the card expects")
    touches = [l.split() for l in git(clone, "log", "--format=%h %cd", "--date=format:%H:%M", "298be4e", "--", "REALITY.md").splitlines()]
    day = [hm for _, hm in touches if hm <= "18:59"]
    last = max(day)
    corr = git(clone, "show", "298be4e:BRIEF-CORRECTIONS.md")
    corr_commits = git(clone, "log", "--format=%h", "298be4e", "--", "BRIEF-CORRECTIONS.md").split()
    if corr_commits != ["1f7c633"]:
        sys.exit("make_pictures: the corrections file changed after its first commit")
    head = corr.splitlines()[0].lstrip("# ")
    purpose = [l for l in corr.split("\n\n")[1:] if l.strip()][0].strip()
    entry = [l for l in corr.split("\n\n")[1:] if l.strip()][1].strip()
    out = []
    # the reality file, crowded
    out.append(f'<rect x=".3" y=".3" width="80.6" height="62" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>'
               + t(4, 7, "REALITY.md", 800))
    for j, r in enumerate(textwrap.wrap("\u201c" + second + "\u201d", 40)):
        out.append(t(4, 12.6 + j * 4.1, r, 700, mc.ACCENT))
    for k in range(9):
        out.append(f'<rect x="4" y="{24 + k * 2.6:.1f}" width="{70 - (k * 7) % 30}" height="1.3" rx=".6" fill="{mc.FILL2}"/>')
    x0, w = 4.0, 73.0
    out.append(mc.line(x0, 52, x0 + w, 52, mc.INK, .35))
    for hm in day:
        h, m = (int(v) for v in hm.split(":"))
        x = x0 + (h + m / 60) / 19 * w
        out.append(mc.line(x, 49.6, x, 52, mc.ACCENT, .5))
    out.append(t(x0, 56.6, "changed all day", 400, mc.MUTED) + t(x0 + w, 56.6, f"last at {last}", 700, mc.INK, "end")
               + t(x0, 60.6, "00:00", 400, mc.MUTED) + t(x0 + w, 60.6, "19:00", 400, mc.MUTED, "end"))
    # the corrections file, nearly empty
    sp = len(out)
    x = 83.4
    out.append(f'<rect x="{x}" y=".3" width="80.3" height="62" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>'
               + t(x + 4, 7, "BRIEF-CORRECTIONS.md", 800) + t(x + 4, 13, head, 700))
    for j, r in enumerate(textwrap.wrap(re.sub(r"\[(.+?)\]\(.+?\)", r"\1", purpose), 40)):
        out.append(t(x + 4, 18.4 + j * 4.1, r, 400, mc.MUTED))
    out.append(t(x + 4, 40, entry, 700, mc.ACCENT))
    out.append(t(x + 4, 58, "unchanged from the first half hour (1f7c633)", 400, mc.MUTED))
    # one card per file when asked (security's note in the publisher's 040: each file held both cards, one cropped away)
    if part == "left":
        return mc.svg(81.2, 63.4, "".join(out[:sp]), "A card: the reality file, crowded with the day's changes")
    if part == "right":
        return mc.svg(81.2, 63.4, '<g transform="translate(-83.1 0)">' + "".join(out[sp:]) + "</g>",
                      "A card: the corrections file, with its one entry, None yet")
    return mc.svg(164, 63.4, "".join(out), "Two cards: the reality file crowded with the day's changes, the corrections file with its one entry, None yet")


def split_cards(clone):
    return two_files(clone, "left"), two_files(clone, "right")


def schedule(clone):
    import math
    sched = json.loads(git(clone, "show", "09f13d5:team/conductor/schedule.json"))
    about, hours = sched["about"], sched["hours"]
    q1, q2 = "fifteen minutes after the one before", "every hour, round the clock"
    if q1 not in about or q2 not in hours:
        sys.exit("make_pictures: the schedule's own words are not as the drawing quotes them")
    runs = [(r["agent"], r["minute"]) for r in sched["runs"]][:4]
    slots = REG["C071"]["value"]
    for m, mm in runs:
        if slots[m].strip(":") != mm:
            sys.exit(f"make_pictures: {m}'s minute at 09f13d5 is not C071's")
    cx, cy, R = 46, 38, 22
    out = [f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#fff" stroke="{mc.INK}" stroke-width=".6"/>']
    for q in range(4):
        a = math.radians(q * 90 - 90)
        out.append(t(cx + (R - 4) * math.cos(a), cy + (R - 4) * math.sin(a) + 1.1, f":{q * 15:02d}", 400, mc.MUTED, "middle"))
    for m, mm in runs:
        a = math.radians(int(mm) * 6 - 90)
        hx, hy = cx + (R + 6) * math.cos(a), cy + (R + 6) * math.sin(a)
        out.append(mc.line(cx, cy, cx + (R - 9) * math.cos(a), cy + (R - 9) * math.sin(a), mc.CAST[m][0], .9)
                   + g(mc.head(m), hx - 4.6, hy - 4.4, .24))
        if abs(math.cos(a)) > .5:
            out.append(t(hx + (6 if math.cos(a) > 0 else -6), hy + 1, f"{m} :{mm}", 700, mc.INK, "start" if math.cos(a) > 0 else "end"))
        else:
            out.append(t(hx, hy + (-5.6 if math.sin(a) < 0 else 7.4), f"{m} :{mm}", 700, mc.INK, "middle"))
    out.append(f'<circle cx="{cx}" cy="{cy}" r="1" fill="{mc.INK}"/>')
    out.append(t(98, 30, "\u201c" + q1 + "\u201d", 700) + t(98, 37, "\u201c" + q2 + "\u201d", 700)
               + t(98, 45, "the schedule as the conductor", 400, mc.MUTED) + t(98, 49.1, "wrote it at 01:39 (09f13d5)", 400, mc.MUTED))
    out.append(t(0, 80, "the first four members at their minutes; the others joined their slots later", 400, mc.MUTED))
    return mc.svg(164, 82, "".join(out), "The schedule at 01:39: four members on a dial at their own minutes, a quarter of an hour apart")


def night_log(clone):
    page = git(clone, "show", "794008c:content/articles/the-night-hour-by-hour.md")
    edition = re.search(r"Last edition (\d\d:\d\d) UTC", page).group(1)
    span = re.search(r"^## (\d\d:\d\d to \d\d:\d\d UTC)$", page, re.M).group(1)
    rows = re.findall(r"^\| (\w[\w-]*) \| \d\d:\d\d \| .+? \| (\w+) \|$", page, re.M)
    waits = re.findall(r"^- \*\*([\w-]+)\*\*:", page.split("## Waiting on the editor", 1)[1].split("\n## ", 1)[0], re.M)
    members = sorted({m for m, _ in rows}, key=lambda m: [r[0] for r in rows].index(m))
    colour = {"ok": mc.FILL2, "partial": mc.ACCENT, "open": "#fff"}
    out = [f'<rect x=".3" y=".3" width="163.4" height="{{H}}" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".5"/>',
           f'<rect x=".3" y=".3" width="163.4" height="7" rx="2" fill="{mc.FILL}"/>',
           t(4, 5.1, f"the night, hour by hour: its first edition, {edition}, drawn from the page", 700, mc.MUTED),
           t(4, 14, span, 800, mc.INK, size=4.2)]
    y = 21.0
    out.append(t(4, y, "each member's line: its wakes, by outcome", 700))
    y += 5
    for m in members:
        outs = [o for mm, o in rows if mm == m]
        out.append(g(mc.head(m), 2, y - 4.2, .24) + t(13, y, m, 400))
        for k, o in enumerate(outs):
            out.append(f'<rect x="{40 + k * 9}" y="{y - 3.2}" width="7.6" height="4.4" rx="1" fill="{colour.get(o, mc.FILL)}" stroke="{mc.INK}" stroke-width=".3"/>')
        y += 6.2
    for k, (o, words) in enumerate((("ok", "ok"), ("partial", "partial"), ("open", "open"))):
        out.append(f'<rect x="{100 + k * 21}" y="{21 - 3.2}" width="5" height="4" rx="1" fill="{colour[o]}" stroke="{mc.INK}" stroke-width=".3"/>' + t(106.4 + k * 21, 21, words, 400, mc.MUTED))
    y += 2
    out.append(t(4, y, "waiting on the editor", 700))
    y += 5
    for m in sorted(set(waits), key=waits.index):
        n = waits.count(m)
        out.append(t(13, y, m, 400) + "".join(f'<rect x="40" y="{y - 2.6 + k * 2.6:.1f}" width="{100 - k * 18}" height="1.4" rx=".7" fill="{mc.FILL2}"/>' for k in range(n)))
        y += 2.6 * n + 3
    H = y
    out[0] = out[0].replace("{H}", f"{H:.1f}")
    out.append(t(0, H + 4.6, "the edition at 794008c, drawn, never shot; its items left as lines", 400, mc.MUTED))
    return mc.svg(164, round(H + 6.2, 1), "".join(out), "The night log's first edition drawn as a page: its hours, each member's wakes by outcome, what waits on the editor")


def still_slide():
    """The slide the narrator would have shown (the conductor's 057): plain on purpose, nothing moves, nothing explains."""
    out = [f'<rect x=".3" y=".3" width="111.4" height="62.4" rx="1" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>']
    # the building: a roof and six rooms
    x0, y0, w, h = 46, 20, 48, 32
    out.append(mc.path(f"M{x0 - 2} {y0} L{x0 + w / 2} {y0 - 11} L{x0 + w + 2} {y0} Z", mc.FILL, mc.INK, .5))
    out.append(f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="#fff" stroke="{mc.INK}" stroke-width=".5"/>')
    out.append(mc.line(x0 + w / 3, y0, x0 + w / 3, y0 + h, mc.INK, .35) + mc.line(x0 + 2 * w / 3, y0, x0 + 2 * w / 3, y0 + h, mc.INK, .35)
               + mc.line(x0, y0 + h / 2, x0 + w, y0 + h / 2, mc.INK, .35))
    # a few dots inside
    for x, y in [(x0 + 7, y0 + 8), (x0 + 22, y0 + 10), (x0 + 38, y0 + 6), (x0 + 12, y0 + 24), (x0 + 41, y0 + 26)]:
        out.append(f'<circle cx="{x}" cy="{y}" r="1.4" fill="{mc.ACCENT}"/>')
    # an arrow, and the label
    out.append(f'<path d="M14 38 H{x0 - 2}" stroke="{mc.INK}" stroke-width=".6" fill="none"/>'
               f'<path d="M{x0 - 2} 38 l-3 -1.8 v3.6 z" fill="{mc.INK}"/>')
    out.append(t(14, 35.4, "agents", 700, mc.ACCENT))
    return mc.svg(112, 63, "".join(out), "A still slide: a box of rooms, a few dots inside, an arrow, and a label saying agents")


R150 = REPO / "manuscript" / "rc2" / "150"


def nine_misses():
    """Chapter 17's misses as cards (critic3 007: the seventy's five against the full book's nine), each heading and its
    cost as the chapter gives them, read at build; two columns; no id, no caption drawn in (P28, convention 8)."""
    import textwrap
    text = (R150 / "17-what-did-not-work.md").read_text()
    misses = re.findall(r"^### (.+?)\n\n\*What it cost:\* (.+?) \*Whose record:\*", text, re.M)
    heads = re.findall(r"^### (.+?)$", text, re.M)
    if len(misses) != len(heads) or len(misses) < 2:
        sys.exit(f"make_pictures: chapter 17 gives {len(heads)} misses and {len(misses)} costs")
    cw, gap, out, y = 80.0, 2.8, [], 0.3
    for i in range(0, len(misses), 2):  # rows of two, read left to right, each row as tall as its taller card
        pair = misses[i:i + 2]
        wrapped = [(textwrap.wrap(hd, 34), textwrap.wrap(c, 40)) for hd, c in pair]
        h = max(4.6 + 4.1 * len(hr) + 4.1 * len(cr) + 1.2 for hr, cr in wrapped)
        for c, (hrows, rows) in enumerate(wrapped):
            x = c * (cw + gap) + .3
            out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{cw}" height="{h:.1f}" rx="1.8" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>'
                       f'<path d="M{x + 3:.1f} {y + 2.4:.1f} l3 3 M{x + 6:.1f} {y + 2.4:.1f} l-3 3" stroke="{mc.ACCENT}" stroke-width=".8"/>')
            for j, r in enumerate(hrows):
                out.append(t(x + 9, y + 5.4 + j * 4.1, r, 800))
            for j, r in enumerate(rows):
                out.append(t(x + 3, y + 5.4 + 4.1 * len(hrows) + j * 4.1 + .6, r, 400, mc.INK))
        y += h + 2.4
    col_y = [y]
    return mc.svg(164, round(max(col_y), 1), "".join(out), f"The {len(misses)} misses as cards, each with its cost in a line, as chapter 17 gives them")


if __name__ == "__main__":
    clone = sys.argv[1]
    files = {f"ch-hour-{h:02d}.svg": hour_card(h) for h in WORDS}
    files["ch11-two-files.svg"] = two_files(clone)
    files["ch8-night-log.svg"] = night_log(clone)
    files["ch11-reality-card.svg"], files["ch11-corrections-card.svg"] = split_cards(clone)
    files["ch5-schedule.svg"] = schedule(clone)
    files["ch1-still-slide.svg"] = still_slide()
    files["ch17-nine-misses.svg"] = nine_misses()
    for name, svg in files.items():
        (HERE / name).write_text(svg)
    print("written " + ", ".join(files))
