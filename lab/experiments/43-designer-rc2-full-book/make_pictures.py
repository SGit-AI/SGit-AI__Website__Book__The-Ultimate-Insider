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
    out.append(t(5, 31.6, f"the hour's wakes by what started them (C087); clock hours of 29 October, UTC", 400, mc.MUTED))
    return mc.svg(164, 35, "".join(out), f"A card: hour {WORDS[hour]}'s wakes by trigger, the schedule's and the editor's")


def g(body, x, y, s):
    return f'<g transform="translate({x:.2f} {y:.2f}) scale({s})">{body}</g>'


def git(clone, *a):
    return subprocess.run(["git", "-C", clone, *a], capture_output=True, text=True, check=True).stdout


def two_files(clone):
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
    x = 83.4
    out.append(f'<rect x="{x}" y=".3" width="80.3" height="62" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>'
               + t(x + 4, 7, "BRIEF-CORRECTIONS.md", 800) + t(x + 4, 13, head, 700))
    for j, r in enumerate(textwrap.wrap(re.sub(r"\[(.+?)\]\(.+?\)", r"\1", purpose), 40)):
        out.append(t(x + 4, 18.4 + j * 4.1, r, 400, mc.MUTED))
    out.append(t(x + 4, 40, entry, 700, mc.ACCENT))
    out.append(t(x + 4, 58, "unchanged from the first half hour (1f7c633)", 400, mc.MUTED))
    return mc.svg(164, 63.4, "".join(out), "Two cards: the reality file crowded with the day's changes, the corrections file with its one entry, None yet")


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


if __name__ == "__main__":
    clone = sys.argv[1]
    files = {f"ch-hour-{h:02d}.svg": hour_card(h) for h in WORDS}
    files["ch11-two-files.svg"] = two_files(clone)
    files["ch8-night-log.svg"] = night_log(clone)
    for name, svg in files.items():
        (HERE / name).write_text(svg)
    print("written " + ", ".join(files))
