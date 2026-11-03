#!/usr/bin/env python3
"""LAB 42: RC2's pictures for the seventy (manuscript/rc2/70/, read only) that are new, not the thirty's drawings again.

    python3 lab/experiments/42-designer-rc2-seventy/make_pictures.py <read-only clone of the talk's repository>
- ch10-hold-file.svg: the hold file as a page, its title line and its last line large ("No member lifts it."), both read
  at build from team/conductor/HOLD.md at 298be4e (with git, read only), its bold and bullet marks dropped as the
  chapter's record line says; the lines between drawn as grey bars, not text (C006).
- ch12-state-machine.svg: the day as three states, running, held, released; "anyone" on the arrow into held, "the
  editor only" on the arrow out; released dashed, never reached by 298be4e (C024).
- ch8-register-bar.svg: the talk's register as one stacked bar, its four counts from C029 at build (checked to add up to
  its total), the three that do not hold marked from C030.
- ch15-six-principles.svg: six cards in a row, each principle's heading as chapter 15 gives it, and under it the times and
  chapters its own "Where it came from" line names, parsed at build (nothing it does not name).
- ch16-checklist.svg: the checklist as one page, each line a box to tick, its chapter and its first sentence, parsed from
  chapter 16 at build (its chapters from 1 in order, or the build stops; fourteen since chapter 15 was folded in).
- ch2-dashboard.svg: the team's dashboard, drawn (never shot): the wake clock's minutes (C071), the hold's title (read
  from HOLD.md at 298be4e), what waits on the editor as grey lines (nothing invented), and every wake as a grid, one
  square per wake record per member (C022's column in claims/scorecard-values.md, checked to its total at build).
- ch2-site-building.svg: the site as a building, one floor per kind of page, each lit by the members whose policy at
  298be4e lets them write that floor's source paths (scope.writes, read with git at build).
- ch2-wakes-page.svg: the wakes page, drawn: deck's three newest wake records at 298be4e, newest first, each step's
  verdict as the record gives it (a step not run drawn empty); the comments drawn as grey lines, not quoted. The build
  checks deck's records against C022's count for deck.
- ch2-member-page.svg: deck's member page, drawn: its title, its role's first line and two of its rules with the
  mistake behind each, verbatim from its ROLE.md at 298be4e (two that carry no number); status and debriefs as grey
  lines; a square per wake record (C022); the key section shown only as a dashed band saying it is not shown.
- ch7-wakes-card.svg: the day's wakes by trigger as a card: the total and its three parts from C087, checked to add up.
- ch3-team-pattern.svg: the team pattern as a card: one brief, one board, one hold, a page of rules per member, and each
  member's round in the Figure line's own words (checked in chapter 3 at build).
- ch3-first-rules.svg: the first page of rules as a card, its six lines exactly as chapter 3 quotes them (backticks
  dropped, the chapter's own ellipses kept), each tagged with what it protects; the last one marked; checked at build.
- ch11-five-misses.svg: the five misses as five cards on one page, each its heading and its "What it cost:" line read
  from chapter 11 at build, its id in small type as the thirty's cards gave them (each C id checked in the register).
- ch3-first-two-hours.svg: the project's first two hours as a stack, oldest at the bottom: four commits, each with who
  wrote it and the files it added, read with git at 298be4e (no times printed).
- ch8-check-card.svg and ch8-two-companions.svg: chapter 8's two cards, their words parsed from the Figure lines
  themselves at build: what the check looked at that first night, and the brief's two companions.
No number is printed but the hold's time, ids, C029's and C087's counts and the chapters' own times. One SVG unit a millimetre, sizes stated, text 9 pt.
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


def t(x, y, s, weight=400, fill=mc.INK, anchor="start", size=F):
    from html import escape
    s = escape(str(s), quote=False)
    return f'<text x="{x:.2f}" y="{y:.2f}" {SANS} font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'


def hold_file(clone):
    for cid in ("C006", "C024"):
        if REG[cid]["state"] != "checked":
            sys.exit(f"make_pictures: {cid} is {REG[cid]['state']}")
    text = subprocess.run(["git", "-C", clone, "show", "298be4e:team/conductor/HOLD.md"], capture_output=True, text=True, check=True).stdout
    title = text.splitlines()[0].lstrip("# ").strip()
    m = re.search(r"\*\*What lifts it:\*\*\s*(.+?)\s*(No member lifts it\.)", text)
    if not m or not title.startswith("HOLD:"):
        sys.exit("make_pictures: the hold file's title or its 'What lifts it' line is not as expected")
    lifts, last = m.group(1), m.group(2)
    x, w = 22, 120
    out = [f'<path d="M{x} 2 h{w - 12} l12 12 v76 h-{w} z" fill="#fff" stroke="{mc.INK}" stroke-width=".6"/>',
           f'<path d="M{x + w - 12} 2 v12 h12" fill="none" stroke="{mc.INK}" stroke-width=".5"/>']
    head, rest = title.split(";", 1)
    out.append(t(x + 7, 15, head + ";", 800, mc.ACCENT, size=4.6) + t(x + 7, 21.4, rest.strip(), 800, mc.ACCENT, size=4.6))
    for k, (dy, ww) in enumerate([(30, 92), (35, 70), (41, 100), (46, 96), (51, 60), (57, 98), (62, 84)]):
        out.append(f'<rect x="{x + 7}" y="{dy}" width="{ww}" height="2" rx="1" fill="{mc.FILL2}"/>')
    out.append(t(x + 7, 72, "What lifts it: " + lifts, 400, mc.INK))
    out.append(t(x + 7, 84.6, last, 800, mc.INK, size=7.4))
    out.append(t(x, 97.4, "team/conductor/HOLD.md at 298be4e, written 18:44:13 (C006); never lifted that day (C024)", 400, mc.MUTED))
    return mc.svg(164, 100, "".join(out), "The hold file as a page: its title, and its last line large: No member lifts it.")


def state_machine():
    if REG["C024"]["value"]["lifted_by_298be4e"] is not False:
        sys.exit("make_pictures: C024 no longer says the hold was not lifted")
    out = []
    defs = (f'<defs><marker id="s" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="{mc.INK}"/></marker>'
            f'<marker id="s2" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="{mc.MUTED}"/></marker></defs>')
    # running: where the day spent its time; held: where it ended; released: drawn, never reached
    out.append(f'<ellipse cx="26" cy="24" rx="22" ry="15" fill="{mc.FILL}" stroke="{mc.INK}" stroke-width=".7"/>'
               + t(26, 25.2, "running", 800, mc.INK, "middle", 4.2) + t(26, 31, "the day", 400, mc.MUTED, "middle"))
    out.append(f'<ellipse cx="88" cy="24" rx="17" ry="13" fill="#fff" stroke="{mc.ACCENT}" stroke-width="1.2"/>'
               + t(88, 25.2, "held", 800, mc.ACCENT, "middle", 4.2) + t(88, 31, "from 18:44", 400, mc.MUTED, "middle"))
    out.append(f'<ellipse cx="142" cy="24" rx="17" ry="13" fill="#fff" stroke="{mc.MUTED}" stroke-width=".6" stroke-dasharray="1.6 1.2"/>'
               + t(142, 25.2, "released", 800, mc.MUTED, "middle", 4.2) + t(142, 31, "not reached", 400, mc.MUTED, "middle"))
    out.append(f'<path d="M49 24 H69" stroke="{mc.INK}" stroke-width=".8" marker-end="url(#s)"/>' + t(59, 19.6, "anyone", 700, mc.INK, "middle"))
    out.append(f'<path d="M106 24 H123" stroke="{mc.MUTED}" stroke-width=".8" stroke-dasharray="1.6 1.2" marker-end="url(#s2)"/>'
               + t(114.5, 10.6, "the editor", 700, mc.INK, "middle") + t(114.5, 15, "only", 700, mc.INK, "middle"))
    out.append(t(0, 46, "the hold at 18:44:13 (C006); by the end of the day's record it was not lifted (C024)", 400, mc.MUTED))
    return mc.svg(164, 48, defs + "".join(out), "The day as three states: running, held, released; anyone may hold, only the editor releases; released never reached")


R70 = REPO / "manuscript" / "rc2" / "70"


def scorecard():
    rows = {}
    for line in (REPO / "claims" / "scorecard-values.md").read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 7 and cells[0] in mc.CAST:
            rows[cells[0]] = {"first": cells[1].split()[0], "wakes": int(cells[4])}
    return rows


def dashboard(clone):
    import math
    sc = scorecard()
    if sum(r["wakes"] for r in sc.values()) != REG["C022"]["value"]["records"]:
        sys.exit("make_pictures: C022's per-member wake records do not add up to its total")
    title = subprocess.run(["git", "-C", clone, "show", "298be4e:team/conductor/HOLD.md"], capture_output=True, text=True,
                           check=True).stdout.splitlines()[0].lstrip("# ").strip()
    order = sorted(mc.CAST, key=lambda m: sc[m]["first"])
    out = [f'<rect x=".3" y=".3" width="163.4" height="{{H}}" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".5"/>',
           f'<rect x=".3" y=".3" width="163.4" height="7" rx="2" fill="{mc.FILL}"/>',
           "".join(f'<circle cx="{4 + k * 3}" cy="3.8" r=".9" fill="{mc.FILL2}"/>' for k in range(3)),
           t(14, 5.1, "the dashboard, drawn from the page", 700, mc.MUTED)]
    # the clock: every member's minute on the dial (C071)
    cx, cy, R = 18, 26, 11
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#fff" stroke="{mc.INK}" stroke-width=".5"/>')
    for m, mm in REG["C071"]["value"].items():
        a = math.radians(int(mm.strip(":")) * 6 - 90)
        out.append(f'<circle cx="{cx + (R - 2) * math.cos(a):.2f}" cy="{cy + (R - 2) * math.sin(a):.2f}" r=".9" fill="{mc.CAST[m][0]}"/>')
    out.append(mc.line(cx, cy, cx, cy - 6, mc.INK, .6) + mc.line(cx, cy, cx + 4, cy + 1.5, mc.INK, .6) + t(cx, cy + R + 4.4, "the clock", 400, mc.MUTED, "middle"))
    # the hold banner, its title as the file gives it
    out.append(f'<rect x="36" y="13" width="74" height="17" rx="1.4" fill="{mc.ACCENT}"/>' + t(39, 18.6, "HOLD", 800, "#fff")
               + t(39, 23.2, title.split(";")[0].replace("HOLD: ", ""), 400, "#fff") + t(39, 27.6, title.split(";")[1].strip(), 400, "#fff"))
    # what waits on the editor: lines, no items invented
    out.append(f'<rect x="114" y="13" width="46" height="24" rx="1.4" fill="{mc.FILL}"/>' + t(117, 18.6, "waits on the editor", 700)
               + "".join(f'<rect x="117" y="{22 + k * 4}" width="{36 - k * 6}" height="1.6" rx=".8" fill="{mc.FILL2}"/>' for k in range(3)))
    # every wake as a grid: a square per wake record
    y = 48.0
    out.append(t(4, y, "every wake, one square each", 700))
    y += 4
    for m in order:
        n = sc[m]["wakes"]
        out.append(t(4, y + 2.6, m, 400, mc.INK))
        for k in range(n):
            out.append(f'<rect x="{26 + k * 2.9:.2f}" y="{y}" width="2.3" height="2.6" rx=".3" fill="{mc.CAST[m][0]}"/>')
        y += 4.2
    H = y + 2
    out[0] = out[0].replace("{H}", f"{H:.1f}")
    out.append(t(0, H + 4.6, "drawn from the page, not shot; minutes C071; wake records C022; the hold's title from the file at 298be4e", 400, mc.MUTED))
    return mc.svg(164, round(H + 6.2, 1), "".join(out), "The team's dashboard, drawn: the clock, the hold, what waits on the editor, and every wake as a square")


STEPS = [("plan", "plan"), ("pre_review", "plan checked"), ("work", "work"), ("post_review", "work checked"), ("post_check", "to plan")]


def deck_records(clone):
    names = subprocess.run(["git", "-C", clone, "ls-tree", "--name-only", "298be4e", "team/deck/wakes/"], capture_output=True,
                           text=True, check=True).stdout.split()
    if len(names) != scorecard()["deck"]["wakes"]:
        sys.exit(f"make_pictures: deck has {len(names)} wake records at 298be4e, C022 says {scorecard()['deck']['wakes']}")
    return sorted(names)


def wakes_page(clone):
    names = deck_records(clone)[-3:][::-1]
    out = [f'<rect x=".3" y=".3" width="163.4" height="{{H}}" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".5"/>',
           f'<rect x=".3" y=".3" width="163.4" height="7" rx="2" fill="{mc.FILL}"/>',
           "".join(f'<circle cx="{4 + k * 3}" cy="3.8" r=".9" fill="{mc.FILL2}"/>' for k in range(3)),
           t(14, 5.1, "the wakes page, drawn: every member's wakes, newest first", 700, mc.MUTED),
           g(mc.head("deck"), 2, 9, .3) + t(13, 14.6, "deck", 800)]
    y = 21.0
    for i, name in enumerate(names):
        rec = json.loads(subprocess.run(["git", "-C", clone, "show", f"298be4e:{name}"], capture_output=True, text=True, check=True).stdout)
        out.append(t(4, y + 3.6, ["newest", "before it", "before that"][i], 400, mc.MUTED))
        for k, (key, words) in enumerate(STEPS):
            v = (rec["steps"].get(key) or {}).get("verdict")
            x = 28 + k * 27
            if v:
                warm = v not in ("go", "done", "clean", "as-planned")
                out.append(f'<rect x="{x}" y="{y}" width="25.6" height="10" rx="1.2" fill="{mc.FILL if not warm else "#fbe9df"}" stroke="{mc.ACCENT if warm else mc.FILL2}" stroke-width=".35"/>'
                           + t(x + 1.6, y + 4, words, 400, mc.MUTED) + t(x + 1.6, y + 8.4, v, 800, mc.ACCENT if warm else mc.INK))
            else:
                out.append(f'<rect x="{x}" y="{y}" width="25.6" height="10" rx="1.2" fill="#fff" stroke="{mc.FILL2}" stroke-width=".35" stroke-dasharray="1 .7"/>'
                           + t(x + 1.6, y + 4, words, 400, mc.MUTED) + t(x + 1.6, y + 8.4, "not reached", 400, mc.MUTED))
        out.append("".join(f'<rect x="28" y="{y + 12.4 + k * 2.6:.1f}" width="{132 - k * 40}" height="1.4" rx=".7" fill="{mc.FILL2}"/>' for k in range(2)))
        y += 20.5
    H = y
    out[0] = out[0].replace("{H}", f"{H:.1f}")
    out.append(t(0, H + 4.6, "deck's three newest wake records at 298be4e; each step's comment drawn as lines; deck's records checked against C022", 400, mc.MUTED))
    return mc.svg(164, round(H + 6.2, 1), "".join(out), "The wakes page, drawn: deck's three newest wakes, each step's verdict, the newest stopped by the hold before its review")


RULES_SHOWN = ["Check each changed slide in the player", "A brief states the job, the material and the sources"]


def member_page(clone):
    import textwrap
    role = subprocess.run(["git", "-C", clone, "show", "298be4e:team/deck/ROLE.md"], capture_output=True, text=True, check=True).stdout
    first = [l for l in role.splitlines()[1:] if l.strip()][0]
    first = re.match(r"(.+?:)", first).group(1).rstrip(":")
    rules = []
    for start in RULES_SHOWN:
        line = next(l for l in role.splitlines() if l.startswith("- " + start))[2:]
        rule, mistake = line.split(": ", 1)
        if re.search(r"\d", rule + mistake):
            sys.exit("make_pictures: a rule chosen for deck's page carries a number")
        rules.append((rule.strip(), mistake.strip().rstrip(".")))
    n = scorecard()["deck"]["wakes"]
    out = [f'<rect x=".3" y=".3" width="163.4" height="{{H}}" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".5"/>',
           f'<rect x=".3" y=".3" width="163.4" height="7" rx="2" fill="{mc.FILL}"/>',
           "".join(f'<circle cx="{4 + k * 3}" cy="3.8" r=".9" fill="{mc.FILL2}"/>' for k in range(3)),
           t(14, 5.1, "a member's page, drawn: deck's", 700, mc.MUTED),
           g(mc.figure("deck"), 3, 9, .42) + t(24, 17, "deck", 800, mc.INK, size=4.6)]
    for j, line in enumerate(textwrap.wrap(first, 70)):
        out.append(t(24, 22 + j * 4.1, line, 400))
    y = 36.0
    out.append(t(4, y, "rules, and the mistake behind each", 700))
    y += 5
    for rule, mistake in rules:
        for j, line in enumerate(textwrap.wrap(rule, 90)):
            out.append(t(4, y, line, 700)); y += 4.1
        for j, line in enumerate(textwrap.wrap(mistake, 90)):
            out.append(t(8, y, line, 400, mc.MUTED)); y += 4.1
        y += 1.6
    for label, bars in (("status", 2), ("debriefs", 3)):
        out.append(t(4, y + 1, label, 700))
        out.append("".join(f'<rect x="28" y="{y - 1.6 + k * 2.8:.1f}" width="{120 - k * 30}" height="1.4" rx=".7" fill="{mc.FILL2}"/>' for k in range(bars)))
        y += 3 + 2.8 * bars
    out.append(t(4, y + 1, "wakes", 700) + "".join(f'<rect x="{28 + k * 2.9:.2f}" y="{y - 1.6}" width="2.3" height="2.6" rx=".3" fill="{mc.CAST["deck"][0]}"/>' for k in range(n)))
    y += 6
    out.append(f'<rect x="4" y="{y}" width="156" height="8" rx="1" fill="none" stroke="{mc.MUTED}" stroke-width=".4" stroke-dasharray="1.6 1"/>'
               + t(82, y + 5.2, "the key section: not shown", 400, mc.MUTED, "middle"))
    H = y + 11
    out[0] = out[0].replace("{H}", f"{H:.1f}")
    out.append(t(0, H + 4.6, "deck's role and two of its rules as its ROLE.md gives them at 298be4e; a square per wake record (C022)", 400, mc.MUTED))
    return mc.svg(164, round(H + 6.2, 1), "".join(out), "Deck's member page, drawn: its role, two rules with the mistake behind each, its wakes; its key section not shown")


def wakes_card():
    v = REG["C087"]["value"]
    parts = [("scheduled", "started by the schedule", mc.MUTED), ("editor", "started by the editor", mc.ACCENT), ("follow-up", "follow-ups", mc.FILL2)]
    if sum(v[k] for k, _, _ in parts) != v["wakes"]:
        sys.exit("make_pictures: C087's parts do not add up to its wakes")
    out = [f'<rect x=".3" y=".3" width="163.4" height="46" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>',
           f'<text x="5" y="17" {SANS} font-size="12" font-weight="800" fill="{mc.INK}">{v["wakes"]}</text>',
           t(5, 23.4, "wakes on the day", 400, mc.MUTED)]
    x, W = 40.0, 119.0
    for k, words, col in parts:
        w = W * v[k] / v["wakes"]
        out.append(f'<rect x="{x:.2f}" y="8" width="{w:.2f}" height="9" fill="{col}"/>')
        out.append(t(x + 1.4, 23.4, str(v[k]), 800, mc.ACCENT if k == "editor" else mc.INK) + t(x + 1.4, 27.8, words, 400, mc.MUTED)
                   if k != "follow-up" else mc.line(x + w / 2, 17, x + w / 2, 29.6, mc.FILL2, .4)
                   + t(x + w, 34, str(v[k]), 800, mc.INK, "end") + t(x + w, 38.4, words, 400, mc.MUTED, "end"))
        x += w
    out.append(t(5, 42.4, "the day's wakes by what started them (C087)", 400, mc.MUTED))
    return mc.svg(164, 47, "".join(out), "A card: the day's wakes by trigger, the schedule's, the editor's and the follow-ups")


ROUND = ["wakes on its own minute", "reads the brief, the board and its mail", "does one step", "writes down what it did"]


def team_pattern():
    line = next(l for l in (R70 / "03-one-account-one-project-one-conductor.md").read_text().splitlines() if l.startswith("**Figure:** a card, the team pattern"))
    for w in ["one brief, one board, one hold", "a page of rules per member"] + ROUND:
        if w not in line:
            sys.exit(f"make_pictures: {w!r} is not in chapter 3's team pattern line")
    out = [f'<rect x=".3" y=".3" width="163.4" height="62" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>',
           t(5, 8, "the team pattern", 800)]
    # the three shared things
    for i, (label, draw) in enumerate([("one brief", "brief"), ("one board", "board"), ("one hold", "hold")]):
        x = 8 + i * 22
        if draw == "brief":
            out.append(f'<rect x="{x}" y="13" width="9" height="11" rx=".5" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>'
                       + "".join(mc.line(x + 1.6, 16 + k * 1.9, x + 7.4, 16 + k * 1.9, mc.MUTED, .35) for k in range(4)))
        elif draw == "board":
            out.append(f'<rect x="{x - 2}" y="13" width="14" height="11" rx=".5" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>'
                       + "".join(f'<rect x="{x - .6 + c * 4.6:.1f}" y="{14.6 + r * 3:.1f}" width="3.4" height="2" fill="{f}"/>' for c, r, f in ((0, 0, mc.FILL2), (1, 0, mc.FILL2), (2, 1, mc.ACCENT))))
        else:
            out.append(f'<path d="M{x - 1} 13 h8 l2.4 2.4 v8.6 h-10.4 z" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>' + t(x + 4.2, 20.6, "HOLD", 800, mc.ACCENT, "middle"))
        out.append(t(x + 4.5, 29, label, 700, mc.INK, "middle"))
    # a page of rules per member
    for i, m in enumerate(mc.CAST):
        out.append(g(mc.head(m), 1 + i * 7.2, 33, .3) + f'<rect x="{6 + i * 7.2:.1f}" y="42" width="4.6" height="5.6" rx=".3" fill="#fff" stroke="{mc.INK}" stroke-width=".3"/>')
    out.append(t(5, 54, "a page of rules per member", 700))
    # each member's round
    cx, cy, r = 112, 33, 16
    import math
    for i, words in enumerate(ROUND):
        a = math.radians(-90 + i * 90)
        a0, a1 = math.radians(-90 + i * 90 + 14), math.radians(-90 + (i + 1) * 90 - 14)
        out.append(f'<path d="M{cx + r * math.cos(a0):.2f} {cy + r * math.sin(a0):.2f} A{r} {r} 0 0 1 {cx + r * math.cos(a1):.2f} {cy + r * math.sin(a1):.2f}" fill="none" stroke="{mc.ACCENT}" stroke-width=".7" marker-end="url(#tp)"/>')
    labels = [(cx, cy - r - 2.4, "middle"), (cx + r - 2, cy - 3, "start"), (cx, cy + r + 4.6, "middle"), (cx - r - 1.6, cy - 3, "end")]
    for (x, y, anc), words in zip(labels, ROUND):
        import textwrap
        rows = textwrap.wrap(words, 17)
        if y < cy - r:  # the top label grows upward, clear of the circle
            y -= 4.1 * (len(rows) - 1)
        for j, row in enumerate(rows):
            out.append(t(x if anc != "start" else x + 4, y + j * 4.1, row, 400, mc.INK, anc if anc != "start" else "start"))
    out.append(t(cx, cy + 1.2, "each member", 700, mc.MUTED, "middle"))
    defs = f'<defs><marker id="tp" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="{mc.ACCENT}"/></marker></defs>'
    return mc.svg(164, 63, defs + "".join(out), "A card, the team pattern: one brief, one board, one hold, a page of rules per member, and each member's round")


FIRST_TAGS = ["roles", "the brief", "the check", "the version", "secrets", "instructions"]


def first_rules():
    import textwrap
    text = (R70 / "03-one-account-one-project-one-conductor.md").read_text()
    quoted = [l[4:].replace("`", "") for l in text.splitlines() if l.startswith("> - ")]
    line = next(l for l in text.splitlines() if l.startswith("**Figure:** the first page of rules as a card"))
    if len(quoted) != len(FIRST_TAGS) or ": " + ", ".join(FIRST_TAGS) not in line:
        sys.exit("make_pictures: chapter 3's quoted rules or its tags are not as the card expects")
    out = [f'<rect x=".3" y=".3" width="163.4" height="{{H}}" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>',
           t(5, 8, "CLAUDE.md, the first page of rules", 800), t(159, 8, "dev's first commit, hour one", 400, mc.MUTED, "end")]
    y = 15.0
    for i, (tag, rule) in enumerate(zip(FIRST_TAGS, quoted)):
        last = i == len(quoted) - 1
        rows = textwrap.wrap(rule, 76)
        h = 4.1 * len(rows) + 2.6
        if last:
            out.append(f'<rect x="2.6" y="{y - 3.6:.1f}" width="158.8" height="{h + .6:.1f}" rx="1" fill="#fbe9df"/>')
        out.append(f'<rect x="5" y="{y - 2.9:.1f}" width="21" height="4.2" rx="2.1" fill="{mc.ACCENT if last else mc.FILL}"/>'
                   + t(15.5, y, tag, 700, "#fff" if last else mc.INK, "middle"))
        for j, r in enumerate(rows):
            out.append(t(30, y + j * 4.1, r, 700 if last else 400))
        y += h + 1.4
    H = y - 1
    out[0] = out[0].replace("{H}", f"{H:.1f}")
    out.append(t(0, H + 4.6, "the six lines as chapter 3 quotes them; the last, there from the first half hour, the one this book leans on", 400, mc.MUTED))
    return mc.svg(164, round(H + 6.2, 1), "".join(out), "The first page of rules as a card, each line tagged with what it protects, the last marked")


MISS_IDS = {"The lock never turned": "C027", "Two parts of three unfinished": "C027", "The moment missed": "the storyteller's debrief",
            "The correction lost in the freeze": "C031", "The claims that did not hold": "C029, C030"}


def five_misses():
    import textwrap
    text = (R70 / "11-what-did-not-work.md").read_text()
    misses = re.findall(r"^### (.+?)$.*?^\*What it cost:\* (.+?)$", text, re.M | re.S)
    if [h for h, _ in misses] != list(MISS_IDS):
        sys.exit("make_pictures: chapter 11's five misses are not the five the card expects")
    for ids in MISS_IDS.values():
        for cid in re.findall(r"C\d{3}", ids):
            if REG[cid]["state"] != "checked":
                sys.exit(f"make_pictures: {cid} is {REG[cid]['state']}")
    out, y = [], 0.3
    for head, cost in misses:
        rows = textwrap.wrap(cost, 80)
        h = 9.4 + 4.1 * len(rows)
        out.append(f'<rect x=".3" y="{y:.1f}" width="163.4" height="{h:.1f}" rx="1.8" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>'
                   + f'<path d="M4 {y + 2.6:.1f} l3.2 3.2 M7.2 {y + 2.6:.1f} l-3.2 3.2" stroke="{mc.ACCENT}" stroke-width=".8"/>'
                   + t(10.4, y + 5.6, head, 800) + t(159.6, y + 5.6, MISS_IDS[head], 400, mc.MUTED, "end"))
        for j, r in enumerate(rows):
            out.append(t(10.4, y + 10.2 + j * 4.1, r, 400))
        y += h + 2.2
    out.append(t(0, y + 3, "each heading and its cost as chapter 11 gives them; the failures stay in", 400, mc.MUTED))
    return mc.svg(164, round(y + 4.6, 1), "".join(out), "The five misses as five cards, each with its cost in a line and where it rests")


LAYERS = [("2e4b1f4", "the first commit, the editor's", None, ["README.md", "LICENSE", ".gitignore"]),
          ("1f7c633", "dev's first pass, with its four files", "dev", ["CLAUDE.md", "BRIEF.md", "REALITY.md", "BRIEF-CORRECTIONS.md"]),
          ("97b98d9", "the conductor's roster", "conductor", ["data/team.json", "data/schedule.json"]),
          ("09f13d5", "the schedule and the hold", "conductor", ["team/conductor/WAKE.md", "team/conductor/schedule.json"])]


def first_two_hours(clone):
    out = []
    n = len(LAYERS)
    lh, gap = 16.0, 3.0
    for i, (h, words, who, files) in enumerate(LAYERS):
        changed = subprocess.run(["git", "-C", clone, "show", "--name-only", "--format=", h], capture_output=True, text=True, check=True).stdout.split()
        missing = [f for f in files if f not in changed]
        if missing:
            sys.exit(f"make_pictures: {h} does not add {missing}")
        if who is None and subprocess.run(["git", "-C", clone, "log", "-1", "--format=%an", h], capture_output=True, text=True,
                                          check=True).stdout.strip() != "Dinis Cruz":
            sys.exit(f"make_pictures: {h} is not the editor's commit")
        y = (n - 1 - i) * (lh + gap)  # oldest at the bottom
        x = i * 6.0
        top = i == n - 1
        out.append(f'<rect x="{x + .3:.1f}" y="{y + .3:.1f}" width="{163.4 - x - .3 - (n - 1 - i) * 0:.1f}" height="{lh}" rx="1.6" fill="{"#fbe9df" if top else "#fff"}" stroke="{mc.ACCENT if top else mc.INK}" stroke-width=".45"/>')
        if who:
            out.append(g(mc.head(who), x + 1, y + 1.4, .34))
        else:
            out.append(g(narrator_head_small_42(), x + .4, y + 1.2, .3))
        out.append(t(x + 13, y + 6, words, 800) + t(163.4 - 2, y + 6, h, 400, mc.MUTED, "end")
                   + t(x + 13, y + 11.6, " \u00b7 ".join(files), 400, mc.INK))
        if i < n - 1:
            out.append(f'<path d="M{x + 9} {y - .6:.1f} v-{gap - 1.2:.1f}" stroke="{mc.FILL2}" stroke-width=".6"/>')
    H = n * (lh + gap) - gap
    out.append(t(0, H + 5, "one commit a layer, oldest at the bottom; each layer's files read from its commit at 298be4e", 400, mc.MUTED))
    return mc.svg(164, round(H + 6.8, 1), "".join(out), "The project's first two hours as a stack of files, one commit a layer, each labelled with who wrote it")


def narrator_head_small_42():
    return (f'<circle cx="20" cy="18" r="8.6" fill="{mc.FILL}" stroke="{mc.INK}" stroke-width="{mc.SW * 1.6}"/>'
            f'<g transform="translate(0 .2)">{mc.face("happy")}</g>')


def ch8_line(start):
    return next(l for l in (R70 / "08-the-plumbing.md").read_text().splitlines() if l.startswith("**Figure:** " + start))


def check_card():
    import textwrap
    line = ch8_line("a card, what the check looked at that first night: ")
    items = [i.strip().rstrip(".") for i in line.split(": ", 1)[1].split(";")]
    if len(items) != 7:
        sys.exit(f"make_pictures: chapter 8's check card lists {len(items)} things, the card expects seven")
    out = [f'<rect x=".3" y=".3" width="163.4" height="{{H}}" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>',
           g(mc.head("dev"), 3, 1.2, .34) + t(15, 7.6, "what the check looked at, that first night", 800)]
    y = 16.0
    for it in items:
        rows = textwrap.wrap(it, 84)
        out.append(mc.path(f"M6 {y - 1.6:.1f} l1.4 1.4 l2.8 -2.8", "none", mc.ACCENT, .8))
        for j, r in enumerate(rows):
            out.append(t(14, y + j * 4.1, r, 400))
        y += 4.1 * len(rows) + 1.6
    H = y - 1
    out[0] = out[0].replace("{H}", f"{H:.1f}")
    out.append(t(0, H + 4.6, "the seven things as chapter 8 lists them; the same test for every change", 400, mc.MUTED))
    return mc.svg(164, round(H + 6.2, 1), "".join(out), "A card: what the check looked at that first night, seven things, each ticked")


def two_companions():
    import textwrap
    line = ch8_line("a card, the brief's two companions: ")
    m = re.match(r".*?: (the reality file), (.+?); and (the corrections file), (.+?)\.?$", line)
    if not m:
        sys.exit("make_pictures: chapter 8's companions line is not as the card expects")
    cards = [(m.group(1), m.group(2)), (m.group(3), m.group(4))]
    out = []
    h = max(22 + 4.1 * len(textwrap.wrap(d, 38)) for _, d in cards)
    for i, (name, desc) in enumerate(cards):
        x = i * 82.4
        rows = textwrap.wrap(desc, 38)
        out.append(f'<rect x="{x + .3:.1f}" y=".3" width="80.6" height="{h:.1f}" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>'
                   + f'<path d="M{x + 4} 4 h7 l2.4 2.4 v9 h-9.4 z" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>'
                   + "".join(mc.line(x + 5.4, 8 + k * 1.9, x + 11.6, 8 + k * 1.9, mc.ACCENT if i == 0 else mc.MUTED, .35) for k in range(4))
                   + t(x + 17, 10.6, name, 800))
        for j, r in enumerate(rows):
            out.append(t(x + 4, 22 + j * 4.1, r, 400))
    H = max(22 + 4.1 * len(textwrap.wrap(d, 38)) for _, d in cards)
    out.append(t(0, H + 5, "beside the brief, which nobody edits; each description as chapter 8 gives it", 400, mc.MUTED))
    return mc.svg(164, round(H + 6.8, 1), "".join(out), "A card: the brief's two companions, the reality file and the corrections file")


FLOORS = [("the talk", ("src/static/talk/",)),
          ("the workshop of animations", ("src/static/ruv-sgit/", "src/pages/ruv-sgit/", "src/static/motion/", "src/pages/motion/")),
          ("the studio", ("src/pages/studio/", "src/static/studio/", "src/static/studio-ports/", "src/pages/studio-ports/")),
          ("the team's own records", ("team/", "src/pages/admin/"))]


def site_building(clone):
    import fnmatch
    scopes = {}
    for m in mc.CAST:
        pol = json.loads(subprocess.run(["git", "-C", clone, "show", f"298be4e:team/{m}/policy.json"], capture_output=True,
                                        text=True, check=True).stdout)
        scopes[m] = pol.get("scope", {}).get("writes", [])
    sc = scorecard()
    order = sorted(mc.CAST, key=lambda m: sc[m]["first"])
    out = [mc.path("M10 22 L82 4 L154 22 Z", mc.FILL, mc.INK, .5)]
    fh, y = 17.0, 22.0
    for name, prefixes in FLOORS:
        lit = [m for m in order if any(w.startswith(p) or p.startswith(w.rstrip("*")) for w in scopes[m] for p in prefixes)]
        out.append(f'<rect x="10" y="{y}" width="144" height="{fh}" fill="#fff" stroke="{mc.INK}" stroke-width=".5"/>'
                   + t(14, y + 9.6, name, 700))
        if len(lit) == len(mc.CAST):
            for k, m in enumerate(lit):
                out.append(g(mc.head(m), 58 + k * 9.6, y + .6, .4))
            out.append(t(149, y + 15, "all nine", 400, mc.MUTED, "end"))
        else:
            for k, m in enumerate(lit):
                out.append(g(mc.head(m), 62 + k * 24, y + .6, .4) + t(70 + k * 24, y + 15, m, 400, mc.INK, "middle"))
        y += fh
    out.append(mc.line(4, y, 160, y, mc.INK, .7))
    out.append(t(0, y + 5, "each floor lit by the members whose policy at 298be4e lets them write its pages (scope.writes)", 400, mc.MUTED))
    return mc.svg(164, round(y + 6.8, 1), "".join(out), "The site as a building, one floor per kind of page, each lit by the members who could write it")


def g(body, x, y, s):
    return f'<g transform="translate({x:.2f} {y:.2f}) scale({s})">{body}</g>'


def register_bar():
    v = REG["C029"]["value"]
    parts = [("holds", "held", mc.INK), ("holds in part", "held in part", "#6b7680"), ("not checked", "not checked", mc.FILL2),
             ("does not hold", "did not hold", mc.ACCENT)]
    if sum(v["holds"][k] for k, _, _ in parts) != v["claims"]:
        sys.exit("make_pictures: C029's four counts do not add up to its total")
    if len(REG["C030"]["value"]) != v["holds"]["does not hold"]:
        sys.exit("make_pictures: C030 does not list C029's count of claims that do not hold")
    # C030 gives "on_stage" only where the claim reached the talk's own files (one, marked "no"); the other two sit in
    # "the article only" and "the story tree only", never in the talk, so they stop the build if that ever changes
    for c in REG["C030"]["value"]:
        if "on_stage" not in c and c["where"] not in ("the article only", "the story tree only"):
            sys.exit(f"make_pictures: C030's {c['id']} gives no on_stage and is not article- or tree-only")
    on_stage = [c for c in REG["C030"]["value"] if c.get("on_stage", "no").startswith("yes")]
    x0, W, y, h = 0.0, 164.0, 10.0, 12.0
    out, x = [], x0
    for k, words, col in parts:
        n = v["holds"][k]
        w = W * n / v["claims"]
        out.append(f'<rect x="{x:.2f}" y="{y}" width="{max(w, .8):.2f}" height="{h}" fill="{col}"/>')
        if w > 14:
            fill = "#fff" if col in (mc.INK, "#6b7680", mc.ACCENT) else mc.INK
            out.append(t(x + 2, y + 7.6, str(n), 800, fill))
        x += w
    # labels above, in order; the last segment is narrow, so its label sits at the right with a leader
    xs, x = [], x0
    for k, words, col in parts:
        w = W * v["holds"][k] / v["claims"]
        xs.append((x, w, k, words, col)); x += w
    for x, w, k, words, col in xs[:3]:
        out.append(t(x + 1, y - 2.4, words, 700, mc.INK))
    x, w, k, words, col = xs[3]
    out.append(t(W, y + h + 5.6, f"{v['holds'][k]} {words}", 800, mc.ACCENT, "end")
               + t(W, y + h + 9.8, "none of them said on stage (C030)" if not on_stage else "", 400, mc.MUTED, "end")
               + mc.line(x + w / 2, y + h, x + w / 2, y + h + 2, mc.ACCENT, .5))
    out.append(t(0, y + h + 5.6, f"{v['claims']} claims, built at {v['built'][11:16]} (C029)", 400, mc.MUTED))
    return mc.svg(164, round(y + h + 11.6, 1), "".join(out), "The talk's register as one bar: held, held in part, not checked, did not hold")


def six_principles():
    import textwrap
    text = (R70 / "15-principles.md").read_text()
    blocks = re.findall(r"^## (\d)\. (.+?)$(.*?)\*Where it came from:\* (.+?)$", text, re.M | re.S)
    if [int(b[0]) for b in blocks] != list(range(1, 7)):
        sys.exit("make_pictures: chapter 15 does not give six numbered principles")
    w, gap, out = 26.2, 1.12, []
    heads = [textwrap.wrap(b[1], 12) for b in blocks]
    hh = max(len(x) for x in heads)
    H = 9 + 4.1 * hh + 16
    for i, (num, head, _, where) in enumerate(blocks):
        x = i * (w + gap)
        times = re.findall(r"\b\d\d:\d\d\b", where)
        chapters = re.findall(r"chapter (\d+)", where)
        out.append(f'<rect x="{x + .3:.2f}" y=".3" width="{w}" height="{H:.1f}" rx="1.8" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>'
                   + f'<rect x="{x + .3:.2f}" y=".3" width="{w}" height="1.8" rx=".9" fill="{mc.ACCENT}"/>'
                   + t(x + 2.4, 7.4, num, 800, mc.ACCENT))
        for j, line in enumerate(heads[i]):
            out.append(t(x + 2.4, 12.6 + j * 4.1, line, 700))
        foot = []
        if times:
            foot.append(", ".join(times))
        foot += ["chapters", " and ".join(chapters)] if len(chapters) > 1 else [f"chapter {chapters[0]}"]
        for j, line in enumerate(foot):
            out.append(t(x + 2.4, H - 2.7 - 4.1 * (len(foot) - 1 - j), line, 400, mc.MUTED))
    return mc.svg(164, round(H + 1, 1), "".join(out), "The six principles as six cards, each with the time or chapter it came from")


def checklist():
    import textwrap
    text = (R70 / "16-build-your-own.md").read_text()
    items = re.findall(r"^- \[ \] \*Chapter (\d+):\* (.+)$", text, re.M)
    if not items or [int(c) for c, _ in items] != list(range(1, len(items) + 1)):
        sys.exit("make_pictures: chapter 16's checklist does not run from chapter 1 in order")
    out = [f'<rect x=".3" y=".3" width="163.4" height="{{H}}" rx="1.6" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>',
           t(5, 8.6, "The checklist", 800, mc.INK, size=4.6)]
    y = 16.0
    for c, line in items:
        first = re.match(r"(.+?\.)(\s|$)", line).group(1)
        rows = textwrap.wrap(first, 78)
        out.append(f'<rect x="5" y="{y - 2.9:.2f}" width="3.2" height="3.2" rx=".4" fill="#fff" stroke="{mc.INK}" stroke-width=".4"/>'
                   + t(11, y, f"chapter {c}", 700, mc.ACCENT))
        for j, r in enumerate(rows):
            out.append(t(31, y + j * 4.1, r, 400))
        y += 4.1 * len(rows) + 2.2
    H = y + 1
    out[0] = out[0].replace("{H}", f"{H:.1f}")
    return mc.svg(164, round(H + 1, 1), "".join(out), "The checklist as one page: a box to tick, the chapter, and its first sentence, for each of chapters 1 to 15")


if __name__ == "__main__":
    clone = sys.argv[1]
    files = {"ch10-hold-file.svg": hold_file(clone), "ch12-state-machine.svg": state_machine(),
             "ch8-register-bar.svg": register_bar(), "ch16-checklist.svg": checklist(),
             "ch2-dashboard.svg": dashboard(clone), "ch2-site-building.svg": site_building(clone),
             "ch2-wakes-page.svg": wakes_page(clone), "ch2-member-page.svg": member_page(clone),
             "ch7-wakes-card.svg": wakes_card(), "ch3-team-pattern.svg": team_pattern(), "ch3-first-rules.svg": first_rules(), "ch11-five-misses.svg": five_misses(),
             "ch3-first-two-hours.svg": first_two_hours(clone),
             "ch8-check-card.svg": check_card(), "ch8-two-companions.svg": two_companions()}
    if (R70 / "15-principles.md").exists():
        files["ch15-six-principles.svg"] = six_principles()
    else:  # chapter 15 was folded into 16 and removed: the drawing stays as last built from it, not rebuilt
        print("ch15-six-principles.svg kept as built: manuscript/rc2/70/15-principles.md is gone")
    for name, svg in files.items():
        (HERE / name).write_text(svg)
    print("written " + ", ".join(files))
