#!/usr/bin/env python3
"""LAB 38: RC2's pictures for the thirty's chapters 2 and 3 that are the designer's (manuscript/rc2/30/, read only).

    python3 lab/experiments/38-designer-rc2-chapters-2-3/make_pictures.py
- ch2-four-cards.svg: the four lit on arrival (dev, conductor, deck, ruv-sgit): on stage from (C011), slot (C071), and the
  line each arrives with, verbatim from chapter 2 and marked dramatised; the five greyed and the empty chair beside them.
- ch3-day-by-trigger.svg: the day's wakes, hour by hour, by what started them (C087, read at build): the factory's own
  clock, the editor, the follow-ups. Where C087 gives only a range (05 to 13) it is drawn as a band in its words. The
  build stops unless the hours it does give add up to C087's totals.
- ch3-relayed-word.svg: one request relayed from one agent to another, stopped at studio's door; in its place a question
  straight to the editor. Its only words are fragments of chapter 3, checked there.
- ch3-map-of-the-day.svg: chapter 3's map, who was on stage when: a row per agent in the order they came on stage, a tick
  at its first commit (C011), each hour shaded by its commits that hour (C095's table, read at build; three shades, no
  count printed); the editor's row on top, shaded in the hours C087 counts wakes he started; C087's 05 to 13 band in its
  own words, and the hours it has no entry for marked so.
"""
import json, re, sys, textwrap
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

F = 3.18
SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'
REG = {c["id"]: c for c in json.loads((REPO / "claims" / "register.json").read_text())["claims"]}
CH2 = REPO / "manuscript" / "rc2" / "30" / "02-the-factory-is-assembled.md"
CH3 = next((REPO / "manuscript" / "rc2" / "30").glob("03-*.md"))


def t(x, y, s, weight=400, fill=mc.INK, anchor="start", size=F):
    return f'<text x="{x:.2f}" y="{y:.2f}" {SANS} font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'


def g(body, x, y, s):
    return f'<g transform="translate({x:.2f} {y:.2f}) scale({s})">{body}</g>'


def first_commits():
    out = {}
    for line in (REPO / "claims" / "scorecard-values.md").read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 7 and cells[0] in mc.CAST:
            out[cells[0]] = cells[1].split()[0]
    return out


def arrival_line(member):
    """The member's first line in chapter 2, as written (the chapter's dramatised scene)."""
    name = {"dev": "Dev", "conductor": "Conductor", "deck": "Deck", "ruv-sgit": "ruv-sgit"}[member]
    m = re.search(rf"^\*\*{re.escape(name)}\*\* \*\([^)]*\)\*: (.+)$", CH2.read_text(), re.M)
    if not m:
        sys.exit(f"make_pictures: no line for {member} in chapter 2")
    return m.group(1).strip()


def four_cards():
    firsts, slots = first_commits(), REG["C071"]["value"]
    order = sorted(mc.CAST, key=lambda m: firsts[m])
    out = []
    lit = order[:4]
    for i, m in enumerate(lit):
        x, w = i * 41, 39.6
        rows = textwrap.wrap(arrival_line(m), 22)
        h = 31 + 4.1 * len(rows) + 6
        col = mc.CAST[m][0]
        out.append(f'<rect x="{x + .3}" y=".3" width="{w}" height="{h:.1f}" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>'
                   f'<rect x="{x + .3}" y=".3" width="{w}" height="11" rx="2" fill="{col}"/><rect x="{x + .3}" y="8.3" width="{w}" height="3" fill="{col}"/>'
                   f'<rect x="{x + 1.6}" y="1.4" width="9" height="8.6" rx="1.1" fill="#fff"/>' + g(mc.head(m), x + 1.3, 1.1, .235)
                   + t(x + 12.5, 7.4, m, 800, "#fff"))
        out.append(t(x + 2.4, 16.6, "on stage from", 400, mc.MUTED) + t(x + w - 2, 16.6, firsts[m], 800, anchor="end"))
        out.append(t(x + 2.4, 21.4, "slot", 400, mc.MUTED) + t(x + w - 2, 21.4, slots[m], 800, anchor="end"))
        for j, r in enumerate(rows):
            out.append(t(x + 2.4, 27.4 + j * 4.1, (r), 400))
        out.append(t(x + 2.4, h - 2.2, "dramatised; C011 C071", 400, mc.MUTED))
    top = max(31 + 4.1 * len(textwrap.wrap(arrival_line(m), 22)) + 6 for m in lit) + 3
    for i, m in enumerate(order[4:] + ["security"]):
        x = i * 27.5
        out.append(f'<rect x="{x + .3}" y="{top}" width="26" height="13" rx="1.6" fill="#fff" stroke="{mc.FILL2}" stroke-width=".4"/>')
        if m == "security":
            out.append(f'<g transform="translate({x + 2} {top + 1.4}) scale(.5)">' + mc.line(4, 2, 4, 18, mc.FILL2, .9) + mc.line(4, 11, 14, 11, mc.FILL2, .9)
                       + mc.line(14, 11, 14, 18, mc.FILL2, .9) + "</g>" + t(x + 11, top + 8.4, "security", 700, mc.MUTED))
        else:
            out.append(g(mc.head(m, False), x + .6, top + 1.2, .22) + t(x + 10, top + 8.4, m, 700, mc.MUTED))
    return mc.svg(164, round(top + 14, 1), "".join(out), "The four lit on arrival with their scorecards and first lines; the five greyed and the empty chair")


def day_by_trigger():
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
    band_sched = v["scheduled"] - sum(s for s, _, _ in hours.values())
    if not (5 * 9 <= band_sched <= 6 * 9):
        sys.exit("make_pictures: C087's 05 to 13 band does not fit its words")
    x0, bw, unit, base = 8.0, 7.6, 1.6, 52.0
    out = [mc.line(x0, base, 160, base, mc.INK, .4)]
    for h in range(0, 19):
        x = x0 + h * 8.0
        out.append(t(x + bw / 2, base + 4.6, f"{h:02d}", 400, mc.MUTED, "middle"))
        if h in hours:
            s, e, f = hours[h]
            y = base
            for n, fill, stroke in ((s, mc.MUTED, "none"), (e, mc.ACCENT, "none"), (f, "#fff", mc.INK)):
                if n:
                    y -= n * unit
                    out.append(f'<rect x="{x:.1f}" y="{y:.2f}" width="{bw}" height="{n * unit:.2f}" fill="{fill}" stroke="{stroke}" stroke-width=".35"/>')
            out.append(t(x + bw / 2, y - 1.2, str(s + e + f), 700, anchor="middle"))
    bx0, bx1 = x0 + 5 * 8.0, x0 + 13 * 8.0 + bw
    out.append(f'<rect x="{bx0}" y="{base - 6 * unit:.1f}" width="{bx1 - bx0:.1f}" height="{6 * unit:.1f}" fill="{mc.FILL}" stroke="{mc.FILL2}" stroke-width=".35"/>')
    out.append(t((bx0 + bx1) / 2, base - 6 * unit + 3.8, "the register gives these hours as:", 400, mc.MUTED, "middle")
               + t((bx0 + bx1) / 2, base - 6 * unit + 8, v["by_hour_UTC"]["05 to 13"], 700, mc.INK, "middle"))
    key = [(mc.MUTED, "none", "the factory's own clock"), (mc.ACCENT, "none", "started by the editor"), ("#fff", mc.INK, "follow-ups")]
    for i, (fill, stroke, words) in enumerate(key):
        out.append(f'<rect x="{x0 + i * 52}" y="{base + 8}" width="3" height="3" fill="{fill}" stroke="{stroke}" stroke-width=".35"/>' + t(x0 + i * 52 + 4.6, base + 10.8, words))
    out.append(t(x0, base + 16.6, f"{v['wakes']} wakes: {v['scheduled']} by the clock, {v['editor']} by the editor, {v['follow-up']} follow-ups; hours in UTC (C087)", 400, mc.MUTED))
    return mc.svg(164, round(base + 18.5, 1), "".join(out), "The day's wakes hour by hour: by the factory's clock, by the editor, and follow-ups")


def relayed_word():
    text = CH3.read_text()
    frags = ["Another agent passed on what the editor had said.", "so I asked him myself."]
    for f in frags:
        if f not in text:
            sys.exit(f"make_pictures: {f!r} not in chapter 3")
    out = [g(mc.reviewer_figure(None), 0, 14, .5),  # another agent, neutral
           f'<path d="M22 30 H58" stroke="{mc.MUTED}" stroke-width=".8" stroke-dasharray="2 1.4" marker-end="url(#r)"/>',
           t(40, 26, "a relayed word", 400, mc.MUTED, "middle"),
           f'<rect x="61" y="12" width="3" height="30" fill="{mc.INK}"/>',
           f'<path d="M55 25 l6 6 M61 25 l-6 6" stroke="{mc.ACCENT}" stroke-width="1"/>',
           g(mc.figure("studio"), 66, 14, .5),
           f'<path d="M88 20 C100 6 116 4 128 10" fill="none" stroke="{mc.ACCENT}" stroke-width=".9" marker-end="url(#r2)"/>',
           t(108, 5, "a question, straight to him", 700, mc.ACCENT, "middle"),
           g(mc.editor_figure("A"), 128, 6, .5),
           t(0, 48, frags[0], 400, mc.MUTED), t(0, 52.4, "Studio: “...so I asked him myself.” (chapter 3)", 400, mc.MUTED)]
    defs = (f'<defs><marker id="r" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="{mc.MUTED}"/></marker>'
            f'<marker id="r2" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="{mc.ACCENT}"/></marker></defs>')
    return mc.svg(164, 54, defs + "".join(out), "A word relayed from one agent stops at studio's door; studio asks the editor himself")


def c095_table():
    rows = {}
    for line in (REPO / "claims" / "talk-commits-by-member-hour.md").read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 21 and cells[0] in mc.CAST:
            rows[cells[0]] = [int(c) for c in cells[1:20]]
    for m, n in REG["C095"]["value"]["by_@member"].items():
        if sum(rows[m]) != n:
            sys.exit(f"make_pictures: C095's table gives {sum(rows[m])} for {m}, the register {n}")
    return rows


def map_of_the_day():
    firsts, table = first_commits(), c095_table()
    order = sorted(mc.CAST, key=lambda m: firsts[m])
    x0, cw, rh, top = 27.0, 7.0, 6.2, 6.0
    out = []
    for h in range(19):
        x = x0 + h * cw
        out.append(t(x + cw / 2, 3.6, f"{h:02d}", 400, mc.MUTED, "middle"))
        out.append(mc.line(x, top, x, top + rh * 10.4, "#e6eaef", .25))
    out.append(mc.line(x0 + 19 * cw, top, x0 + 19 * cw, top + rh * 10.4, "#e6eaef", .25))
    # the editor's row: C087's wakes he started, by hour
    v = REG["C087"]["value"]["by_hour_UTC"]
    y = top
    out.append(g(narrator_head_small(), -1.2, y - 1, .25) + t(7.4, y + 4.3, "the editor", 800))
    for h in range(19):
        x = x0 + h * cw
        key = f"{h:02d}"
        if key in v:
            nums = [int(n) for n in re.findall(r"\d+", v[key])]
            editor = nums[1] if len(nums) > 1 and "follow" not in v[key].split(",")[1] else 0
            if editor:
                out.append(f'<rect x="{x + .3:.2f}" y="{y + .6:.2f}" width="{cw - .6}" height="{rh - 1.2}" rx=".6" fill="{mc.ACCENT}"/>')
        elif 5 <= h <= 13:
            continue
        else:
            out.append(f'<rect x="{x + .3:.2f}" y="{y + .6:.2f}" width="{cw - .6}" height="{rh - 1.2}" rx=".6" fill="none" stroke="{mc.FILL2}" stroke-width=".3" stroke-dasharray=".8 .6"/>')
    out.append(t(x0 + 9 * cw + cw / 2, y + 4.3, v["05 to 13"], 400, mc.MUTED, "middle"))
    y += rh * 1.4
    for m in order:
        col = mc.CAST[m][0]
        out.append(g(mc.head(m), -1.4, y - 1.4, .25) + t(7.4, y + 4.3, m, 700))
        for h, n in enumerate(table[m]):
            if n:
                op = .3 if n <= 2 else (.62 if n <= 6 else 1)
                out.append(f'<rect x="{x0 + h * cw + .3:.2f}" y="{y + .6:.2f}" width="{cw - .6}" height="{rh - 1.2}" rx=".6" fill="{col}" fill-opacity="{op}"/>')
        hh, mm = (int(p) for p in firsts[m].split(":"))
        fx = x0 + (hh + mm / 60) * cw
        out.append(mc.line(fx, y - .2, fx, y + rh + .2, mc.INK, .7))
        y += rh
    ky = y + 5.4
    out.append(t(0, ky, "fewer", 400, mc.MUTED))
    for k, op in enumerate((.3, .62, 1)):
        out.append(f'<rect x="{10 + k * 6.6:.1f}" y="{ky - 3}" width="6" height="3.6" rx=".6" fill="{mc.INK}" fill-opacity="{op}"/>')
    out.append(t(31, ky, "more commits that hour (C095)", 400, mc.MUTED)
               + mc.line(84, ky - 3.2, 84, ky + .6, mc.INK, .7) + t(86, ky, "first commit (C011)", 400, mc.MUTED))
    out.append(f'<rect x="121" y="{ky - 3}" width="5" height="3.6" rx=".6" fill="none" stroke="{mc.FILL2}" stroke-width=".3" stroke-dasharray=".8 .6"/>'
               + t(127.6, ky, "not counted", 400, mc.MUTED))
    out.append(t(0, ky + 6, "hours UTC, 29 October; the editor's row: the hours he started wakes (C087)", 400, mc.MUTED)
               + t(0, ky + 10.2, "C095 counts commits whose subject names the member; C011 is still open", 400, mc.MUTED))
    return mc.svg(164, round(ky + 12, 1), "".join(out), "The map of the day: who was on stage when, hour by hour, and the hours the editor started work")


def narrator_head_small():
    return (f'<circle cx="20" cy="18" r="8.6" fill="{mc.FILL}" stroke="{mc.INK}" stroke-width="{mc.SW * 1.6}"/>'
            f'<g transform="translate(0 .2)">{mc.face("happy")}</g>')


if __name__ == "__main__":
    for name, svg in {"ch2-four-cards.svg": four_cards(), "ch3-day-by-trigger.svg": day_by_trigger(), "ch3-relayed-word.svg": relayed_word(),
                      "ch3-map-of-the-day.svg": map_of_the_day()}.items():
        (HERE / name).write_text(svg)
    print("written ch2-four-cards.svg, ch3-day-by-trigger.svg, ch3-relayed-word.svg, ch3-map-of-the-day.svg")
