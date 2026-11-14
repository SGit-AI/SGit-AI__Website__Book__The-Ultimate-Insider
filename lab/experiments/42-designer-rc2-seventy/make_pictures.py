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
- ch8-plumbing.svg: the plumbing as a building's services: four pipes into the factory floor, each labelled with what
  it carries, the words from the chapter's figure brief (checked there at build).
- ch8-release-row.svg: one row of the release history, drawn: the day's last release (C005), the commits in it (read
  with git as those after the release before), the files they changed (names only), the page they make.
- ch-security-card.svg: security's cast card, as this book's member (conductor__054): its figure and moods, its mission
  verbatim from team/security/ROLE.md, and its label: the second factory's; on the talk's day an empty chair.
- ch4-three-greyed.svg: the storyteller, motion and studio greyed, each with its job words from chapter 4's Figure line
  and one rule verbatim from its ROLE.md at 298be4e (read with git).
- ch4-security-proposed.svg: the talk's security page as a card with nothing on it but its title and its status, both
  read from team/security/ROLE.md at 298be4e.
- ch6-two-commits.svg: two commits as cards, each with its time (git at 298be4e), its "To-" line as chapter 6 quotes it
  (checked against the commit) highlighted, and the wake that read both (its record checked to exist).
- ch6-letter-path.svg: a letter's path on two dials (C071), the letter as a file with its header names only, and one
  board folder with open, blocked and done.
- ch9-story-tree.svg: the storyteller's tree as it was at 14:19 (df37797), every node verbatim from its own mermaid
  block, read with git; no turn marked (the tree marks none; asked of the writer and the storyteller).
- ch9-where-from.svg: each afternoon piece with an arrow back to where it came from, each source checked by git.
- ch12-empty-chair.svg: the talk's nine at a table, security's seat an empty chair; beside it one wake's five steps, the
  two reviews each a reviewer inside it; the debrief's line as chapter 12 quotes it (checked there).
- ch12-book-table.svg: the same table for this book's team, its members read from team/, security's seat filled;
  members with no figure drawn as labelled seats.
- ch13-two-sessions.svg: one member's two sessions, from team/storyteller/sessions/*/SESSION.json (state and times only;
  no session id, fingerprint or account printed, and key files never read), and the key register as rows of blank tags.
- ch1b-start-sheet.svg: the start-here page as one printable sheet, its five steps read from 01b, a box beside each.
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
    # sized to its content (conductor 055, the editor's "too big and out of proportion"): 140 mm wide, the title at
    # 11 pt and the last line at 13 pt against the body's 9.5 pt (type A), four ruled lines standing for the body
    x, w = .5, 139
    out = [f'<path d="M{x} .5 h{w - 10} l10 10 v46 h-{w} z" fill="#fff" stroke="{mc.INK}" stroke-width=".5"/>',
           f'<path d="M{x + w - 10} .5 v10 h10" fill="none" stroke="{mc.INK}" stroke-width=".45"/>']
    head, rest = title.split(";", 1)
    out.append(t(x + 6, 9.4, head + ";", 800, mc.ACCENT, size=3.9) + t(x + 6, 14.4, rest.strip(), 800, mc.ACCENT, size=3.9))
    for dy, ww in [(20, 86), (24, 64), (28, 92), (32, 74)]:
        out.append(f'<rect x="{x + 6}" y="{dy}" width="{ww}" height="1.6" rx=".8" fill="{mc.FILL2}"/>')
    out.append(t(x + 6, 41.5, "What lifts it: " + lifts, 400, mc.INK))
    out.append(t(x + 6, 50.5, last, 800, mc.INK, size=4.6))
    # no source line drawn in: the record line carries the file, the time and the ids (P28, convention 8; critic3 007)
    return mc.svg(140, 57, "".join(out), "The hold file as a page: its title, and its last line large: No member lifts it.")


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
    out.append(t(0, 46, "the hold at 18:44:13; by the end of the day's record it was not lifted", 400, mc.MUTED))
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
    cx, cy, R = 14, 19, 9
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#fff" stroke="{mc.INK}" stroke-width=".5"/>')
    for m, mm in REG["C071"]["value"].items():
        a = math.radians(int(mm.strip(":")) * 6 - 90)
        out.append(f'<circle cx="{cx + (R - 2) * math.cos(a):.2f}" cy="{cy + (R - 2) * math.sin(a):.2f}" r=".9" fill="{mc.CAST[m][0]}"/>')
    out.append(mc.line(cx, cy, cx, cy - 5, mc.INK, .6) + mc.line(cx, cy, cx + 3.4, cy + 1.3, mc.INK, .6) + t(cx, cy + R + 4.2, "the clock", 400, mc.MUTED, "middle"))
    # the hold banner, its title as the file gives it
    out.append(f'<rect x="30" y="10" width="80" height="15.6" rx="1.4" fill="{mc.ACCENT}"/>' + t(33, 14.8, "HOLD", 800, "#fff")
               + t(33, 19, title.split(";")[0].replace("HOLD: ", ""), 400, "#fff") + t(33, 23.2, title.split(";")[1].strip(), 400, "#fff"))
    # what waits on the editor: lines, no items invented
    out.append(f'<rect x="114" y="10" width="46" height="15.6" rx="1.4" fill="{mc.FILL}"/>' + t(117, 14.8, "waits on the editor", 700)
               + "".join(f'<rect x="117" y="{17.4 + k * 2.6}" width="{36 - k * 6}" height="1.4" rx=".7" fill="{mc.FILL2}"/>' for k in range(3)))
    # every wake as a grid: a square per wake record
    out.append(t(30, 31.6, "every wake, one square each", 700))
    y = 34.4
    for m in order:
        n = sc[m]["wakes"]
        out.append(t(4, y + 2.4, m, 400, mc.INK))
        for k in range(n):
            out.append(f'<rect x="{26 + k * 2.9:.2f}" y="{y:.2f}" width="2.3" height="2.4" rx=".3" fill="{mc.CAST[m][0]}"/>')
        y += 3.7
    H = y + 1.4
    out[0] = out[0].replace("{H}", f"{H:.1f}")
    # no source line drawn in: the record line carries C071, C022 and the commit (P28, convention 8; critic3 007)
    return mc.svg(164, round(H + .6, 1), "".join(out), "The team's dashboard, drawn: the clock, the hold, what waits on the editor, and every wake as a square")


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
           t(14, 5.1, "the wakes page, drawn: deck's wakes, newest first", 700, mc.MUTED),
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
    out.append(t(0, H + 4.6, "deck's three newest wake records; each step's comment drawn as lines; deck's records checked against the register", 400, mc.MUTED))
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
    out.append(t(0, H + 4.6, "deck's role and two of its rules as its ROLE.md gives them; a square per wake record", 400, mc.MUTED))
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
    out.append(t(5, 42.4, "the day's wakes by what started them", 400, mc.MUTED))
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


PIPES = [("the site", "the work"), ("the check", "the yes or no"), ("the register", "the source"), ("the brief", "what was asked and what is real")]


def plumbing():
    text = (R70 / "08-the-plumbing.md").read_text()
    brief = next(l for l in text.splitlines() if l.startswith("`%% figure brief: For the designer. Four pipes"))
    if "the work, the yes or no, the source, what was asked and what is real" not in brief or not all(n in ch8_line("the plumbing") for n, _ in PIPES):
        sys.exit("make_pictures: chapter 8's plumbing line or its brief is not as the drawing expects")
    out = [mc.path("M4 14 L82 3 L160 14", "none", mc.INK, .5), mc.line(4, 14, 160, 14, mc.INK, .5)]
    import textwrap
    for i, (name, carries) in enumerate(PIPES):
        x = 14 + i * 38
        out.append(f'<rect x="{x}" y="14" width="6" height="40" fill="{mc.FILL}" stroke="{mc.INK}" stroke-width=".45"/>'
                   + f'<rect x="{x - 1.4}" y="14" width="8.8" height="2.6" rx=".6" fill="{mc.ACCENT}"/>'
                   + t(x + 9, 22, name, 800))
        for j, r in enumerate(textwrap.wrap(carries, 16)):
            out.append(t(x + 9, 27 + j * 4.1, r, 400, mc.MUTED))
        out.append(f'<path d="M{x + 3} 50 v6" stroke="{mc.ACCENT}" stroke-width=".8" marker-end="url(#pl)"/>')
    out.append(f'<rect x="4" y="60" width="156" height="14" rx="1" fill="{mc.FILL}" stroke="{mc.INK}" stroke-width=".5"/>')
    for k, m in enumerate(mc.CAST):
        out.append(g(mc.head(m), 40 + k * 10, 60.4, .34))
    out.append(t(7, 68.6, "the factory floor", 700))
    defs = f'<defs><marker id="pl" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="{mc.ACCENT}"/></marker></defs>'
    out.append(t(0, 79, "four services into the floor, each labelled with the one thing it carries (chapter 8's figure brief)", 400, mc.MUTED))
    return mc.svg(164, 81, defs + "".join(out), "The plumbing as a building's services: the site, the check, the register and the brief, four pipes into the factory floor")


def release_row(clone):
    v = REG["C005"]["value"]
    m = re.search(r"last release (v[\d.]+) at [\d:]+ \((\w+)\)", v)
    if REG["C005"]["state"] != "checked" or not m:
        sys.exit("make_pictures: C005 does not give the last release as expected")
    version, release = m.groups()
    before = subprocess.run(["git", "-C", clone, "log", "--format=%h %s", f"{release}~1", "-60"], capture_output=True, text=True, check=True).stdout
    prev = next(l.split()[0] for l in before.splitlines() if l.split(" ", 1)[1].startswith("site v"))
    commits = [l.split(" ", 1) for l in subprocess.run(["git", "-C", clone, "log", "--no-merges", "--format=%h %s", f"{prev}..{release}"],
                                                       capture_output=True, text=True, check=True).stdout.splitlines()
               if not l.split(" ", 1)[1].startswith("site v")]
    files = sorted({f for h, _ in commits for f in subprocess.run(["git", "-C", clone, "show", "--name-only", "--format=", h],
                                                                  capture_output=True, text=True, check=True).stdout.split()})
    folders = sorted({"/".join(f.split("/")[:2]) + "/" for f in files if f.startswith("team/")})
    if not commits or not files:
        sys.exit("make_pictures: the last release carries no commit")
    shown = [f.split("/", 2)[2] for f in files if not f.endswith(".jpg")]
    out = [f'<rect x=".3" y=".3" width="163.4" height="{{H}}" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".5"/>',
           f'<rect x=".3" y=".3" width="163.4" height="7" rx="2" fill="{mc.FILL}"/>',
           "".join(f'<circle cx="{4 + k * 3}" cy="3.8" r=".9" fill="{mc.FILL2}"/>' for k in range(3)),
           t(14, 5.1, "the release history, drawn: one row", 700, mc.MUTED)]
    cols = [(4, "release"), (30, "its commits"), (76, "the files changed"), (130, "the page they make")]
    for x, head in cols:
        out.append(t(x, 13.6, head, 700, mc.MUTED))
    out.append(mc.line(3, 15.6, 161, 15.6, mc.FILL2, .4))
    out.append(t(4, 21, version, 800, mc.ACCENT) + t(4, 25.2, release, 400, mc.MUTED))
    y = 21.0
    for h, subj in commits:
        out.append(t(30, y, h, 800) + t(30, y + 4.2, subj.split(":")[0], 400, mc.MUTED))
        y += 9
    fy = 21.0
    for f in shown:
        out.append(t(76, fy, f if len(f) < 28 else f[:25] + "...", 400)); fy += 4.1
    if any(f.endswith(".jpg") for f in files):
        out.append(t(76, fy, "and its images", 400, mc.MUTED)); fy += 4.1
    for k, fo in enumerate(folders):
        out.append(t(130, 21 + k * 8.4, fo, 800) + t(130, 25.2 + k * 8.4, "a member's page", 400, mc.MUTED))
    H = max(y, fy) + 2
    out[0] = out[0].replace("{H}", f"{H:.1f}")
    out.append(t(0, H + 4.6, f"the day's last release; its commits and files read with git; drawn, never shot", 400, mc.MUTED))
    return mc.svg(164, round(H + 6.2, 1), "".join(out), "One row of the release history, drawn: the day's last release, its commit, the files it changed, the page they make")


def security_card():
    import textwrap
    role = (REPO / "team" / "security" / "ROLE.md").read_text()
    mission = re.search(r"^- \*\*Mission:\*\* (.+)$", role, re.M).group(1).strip()
    out = [f'<rect x=".3" y=".3" width="163.4" height="68" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".5"/>',
           f'<rect x=".3" y=".3" width="163.4" height="3" rx="1.5" fill="{mc.COLOUR["security"]}"/>',
           g(mc.figure("security"), 3, 7, .9),
           t(44, 13, "security", 800, mc.INK, size=4.6), t(44, 18.6, "this book's team, the second factory", 700, mc.COLOUR["security"])]
    for j, r in enumerate(textwrap.wrap(mission, 56)):
        out.append(t(44, 25.4 + j * 4.1, r, 400))
    for k, mood in enumerate(mc.MOODS):
        out.append(g(mc.figure("security", mood), 44 + k * 16, 39, .26) + t(44 + k * 16 + 5.2, 56.4, "firm" if mood == "stressed" else mood, 400, mc.MUTED, "middle"))
    # on the talk's day: the empty chair
    out.append(g(mc.line(4, 2, 4, 18, mc.FILL2, .9) + mc.line(4, 11, 14, 11, mc.FILL2, .9) + mc.line(14, 11, 14, 18, mc.FILL2, .9) + mc.line(4, 2, 7, 2, mc.FILL2, .9), 112, 39, .7)
               + t(125, 45, "on the day of", 400, mc.MUTED) + t(125, 49.1, "the talk:", 400, mc.MUTED) + t(125, 53.2, "an empty chair", 700, mc.MUTED))
    out.append(t(4, 65, "as the cast guide gives it: \u201cLevel to firm; never alarmed on the page.\u201d", 400, mc.MUTED))
    return mc.svg(164, 69, "".join(out), "Security's cast card, as this book's member: its figure and moods, its mission; on the talk's day an empty chair")


GREYED = [("storyteller", "Nothing goes into the talk until the editor has seen it."), ("motion", "One owner per file."),
          ("studio", "A port keeps its source.")]


def three_greyed(clone):
    import textwrap
    line = next(l for l in (R70 / "04-roles-as-a-cast-you-can-read.md").read_text().splitlines() if l.startswith("**Figure:** three greyed cards: "))
    jobs = [p.strip().rstrip(".") for p in line.split(": ", 1)[1].split(";")]
    out = []
    for i, ((m, rule), job) in enumerate(zip(GREYED, jobs)):
        role = subprocess.run(["git", "-C", clone, "show", f"298be4e:team/{m}/ROLE.md"], capture_output=True, text=True, check=True).stdout
        if f"- **{rule}**" not in role:
            sys.exit(f"make_pictures: {m}'s rule {rule!r} is not in its ROLE.md at 298be4e")
        if job.startswith("the " + m + ", "):
            job = job[4:]
        if not job.startswith(m + ", "):
            sys.exit(f"make_pictures: chapter 4's line does not give {m}'s job where expected")
        x = i * 54.6
        rows_job = textwrap.wrap(job.split(", ", 1)[1], 26)
        rows_rule = textwrap.wrap("\u201c" + rule + "\u201d", 26)
        out.append(f'<rect x="{x + .3:.1f}" y=".3" width="52.4" height="{{H}}" rx="1.8" fill="#fff" stroke="{mc.FILL2}" stroke-width=".45"/>'
                   + g(mc.head(m, False), x + 1, 1.2, .3) + t(x + 11, 7.6, m, 800, mc.MUTED))
        y = 15
        for r in rows_job:
            out.append(t(x + 3, y, r, 400, mc.MUTED)); y += 4.1
        y += 1.6
        for r in rows_rule:
            out.append(t(x + 3, y, r, 700, mc.INK)); y += 4.1
        out.append(("H", y))
    H = max(v for kind, v in [o for o in out if isinstance(o, tuple)]) + 1
    out = [o.replace("{H}", f"{H:.1f}") for o in out if isinstance(o, str)]
    out.append(t(0, H + 5, "greyed: on stage only from the afternoon; each with one rule from its own page", 400, mc.MUTED))
    return mc.svg(164, round(H + 6.8, 1), "".join(out), "Three greyed cards: the storyteller, motion and studio, each with its job and one rule from its page")


def security_proposed(clone):
    role = subprocess.run(["git", "-C", clone, "show", "298be4e:team/security/ROLE.md"], capture_output=True, text=True, check=True).stdout
    m = re.match(r"# (\S+) \((proposed)\)", role.splitlines()[0])
    if not m:
        sys.exit("make_pictures: security's page at 298be4e does not open with its title and 'proposed'")
    title, status = m.groups()
    out = [f'<path d="M30 .5 h92 l12 12 v74 h-104 z" fill="#fff" stroke="{mc.FILL2}" stroke-width=".6"/>',
           f'<path d="M122 .5 v12 h12" fill="none" stroke="{mc.FILL2}" stroke-width=".5"/>',
           t(36, 12, title, 800, mc.MUTED), f'<rect x="36" y="16" width="26" height="5.4" rx="2.7" fill="{mc.FILL}"/>',
           t(49, 19.8, status, 700, mc.MUTED, "middle"),
           t(82, 92, "nothing on it but its title and its status", 400, mc.MUTED, "middle")]
    return mc.svg(164, 94, "".join(out), "Security's role page as a card: its title and its status, proposed, and nothing else")


NOTES = [("09317d9", "conductor", "not followed"), ("36e382b", "deck", "followed")]
READ_BY = ("ruv-sgit", "20261029T103411Z")


def two_commits(clone):
    import textwrap
    text = (R70 / "06-talking-through-git.md").read_text()
    quotes = re.findall(r'^> "(To-ruv-sgit: .+?)" \*\(record\)\*$', text, re.M)
    if len(quotes) != len(NOTES):
        sys.exit("make_pictures: chapter 6 does not quote the two To- lines the cards expect")
    wake = subprocess.run(["git", "-C", clone, "cat-file", "-e", f"298be4e:team/{READ_BY[0]}/wakes/{READ_BY[1]}.json"])
    if wake.returncode:
        sys.exit("make_pictures: the reading wake's record is not at 298be4e")
    read_at = f"{READ_BY[1][9:11]}:{READ_BY[1][11:13]}"
    out = []
    for i, ((h, who, tag), q) in enumerate(zip(NOTES, quotes)):
        msg = subprocess.run(["git", "-C", clone, "log", "-1", "--format=%cd%n%B", "--date=format:%H:%M:%S", h], capture_output=True, text=True, check=True).stdout
        when, body = msg.split("\n", 1)
        if q.rstrip(" .").rstrip(".").replace(" ...", "") not in body.replace("\n", " ") and q.split(" ...")[0] not in body:
            sys.exit(f"make_pictures: the quote for {h} is not in its commit")
        x = i * 82.4
        rows = textwrap.wrap(q, 40)
        hh = 26 + 4.1 * len(rows)
        warm = tag == "not followed"
        out.append(f'<rect x="{x + .3:.1f}" y=".3" width="80.6" height="{{H}}" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>'
                   + g(mc.head(who), x + 1.4, 1.4, .3) + t(x + 12, 7.6, h, 800) + t(x + 78, 7.6, when, 400, mc.MUTED, "end")
                   + t(x + 12, 12, "@" + who, 400, mc.MUTED))
        out.append(f'<rect x="{x + 2.6:.1f}" y="15" width="76" height="{4.1 * len(rows) + 2.6:.1f}" rx="1" fill="#fff3c4"/>')
        for j, r in enumerate(rows):
            out.append(t(x + 4, 19 + j * 4.1, r, 400))
        y = 19 + 4.1 * len(rows) + 4
        out.append(t(x + 4, y, f"read at {READ_BY[0]}'s wake at {read_at}", 400, mc.MUTED)
                   + f'<rect x="{x + 52:.1f}" y="{y + 2}" width="26" height="5" rx="2.5" fill="{mc.ACCENT if warm else mc.FILL}"/>'
                   + t(x + 65, y + 5.6, tag, 700, "#fff" if warm else mc.INK, "middle"))
        out.append(("H", y + 9))
    H = max(v for _, v in [o for o in out if isinstance(o, tuple)])
    out = [o.replace("{H}", f"{H:.1f}") for o in out if isinstance(o, str)]
    out.append(t(0, H + 5, "each note checked against its commit, shortened where marked; times from git", 400, mc.MUTED))
    return mc.svg(164, round(H + 6.8, 1), "".join(out), "Two commits as cards, each with its To- line highlighted, both read at one wake; one note followed, one not")


def letter_path():
    import math
    slots = REG["C071"]["value"]
    a, b = "conductor", "dev"
    out = []
    for k, (m, cx) in enumerate(((a, 22), (b, 142))):
        cy, R = 24, 15
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#fff" stroke="{mc.INK}" stroke-width=".5"/>')
        ang = math.radians(int(slots[m].strip(":")) * 6 - 90)
        out.append(mc.line(cx, cy, cx + (R - 3) * math.cos(ang), cy + (R - 3) * math.sin(ang), mc.CAST[m][0], 1)
                   + f'<circle cx="{cx}" cy="{cy}" r="1" fill="{mc.INK}"/>'
                   + g(mc.head(m), cx - 5, cy + R + 1, .26) + t(cx + 4, cy + R + 6, f"{m}, {slots[m]}", 700))
    # the letter as a file
    lx, ly = 58, 4
    out.append(f'<path d="M{lx} {ly} h40 l6 6 v34 h-46 z" fill="#fff" stroke="{mc.INK}" stroke-width=".5"/>'
               + f'<path d="M{lx + 40} {ly} v6 h6" fill="none" stroke="{mc.INK}" stroke-width=".4"/>')
    for j, hname in enumerate(["From", "To", "Date", "Subject", "X-Kind"]):
        out.append(t(lx + 3, ly + 9 + j * 5.2, hname + ":", 700) + f'<rect x="{lx + 20}" y="{ly + 6.6 + j * 5.2:.1f}" width="{22 - j * 2}" height="1.6" rx=".8" fill="{mc.FILL2}"/>')
    defs = f'<defs><marker id="lp" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="{mc.ACCENT}"/></marker></defs>'
    out.append(f'<path d="M38 18 C46 12 50 14 56 16" fill="none" stroke="{mc.ACCENT}" stroke-width=".7" marker-end="url(#lp)"/>'
               + t(22, 51.4, "written in its outbox", 400, mc.MUTED, "middle"))
    out.append(f'<path d="M106 16 C114 14 118 12 126 18" fill="none" stroke="{mc.ACCENT}" stroke-width=".7" marker-end="url(#lp)"/>'
               + t(142, 51.4, "dropped in its mailroom", 400, mc.MUTED, "middle"))
    out.append(t(82, 51.4, "read at its next minute,", 400, mc.MUTED, "middle") + t(82, 55.5, "answered, and filed", 400, mc.MUTED, "middle"))
    # one board folder
    bx, by = 34, 61
    for j, name in enumerate(["open", "blocked", "done"]):
        x = bx + j * 34
        out.append(mc.path(f"M{x} {by + 2} h9 l1.6 -2 h20 v14 h-30.6 z", mc.FILL, mc.INK, .4) + t(x + 15, by + 10, name, 700, mc.INK, "middle"))
    out.append(t(0, by + 21, "a letter is a file in git; the board is three folders; the minutes are each member's slot", 400, mc.MUTED))
    return mc.svg(164, round(by + 23, 1), defs + "".join(out), "A letter's path on two dials, the letter as a file with its headers, and one board folder with open, blocked and done")


def story_tree(clone):
    import textwrap
    src = subprocess.run(["git", "-C", clone, "show", "df37797:team/storyteller/story/tree.md"], capture_output=True, text=True, check=True).stdout
    block = src.split("```mermaid", 1)[1].split("```", 1)[0]
    later = subprocess.run(["git", "-C", clone, "show", "2afe0d7:team/storyteller/story/tree.md"], capture_output=True, text=True, check=True).stdout
    if "the turn" in block or '|"the turn:' not in later:
        sys.exit("make_pictures: the tree's turn is not as the caption says (none at 14:19, one from 16:04)")
    nodes = {k: v.replace("<br/>", " ") for k, v in re.findall(r'(\w+)\["(.+?)"\]', block)}
    edges = re.findall(r"^\s*(\w+) --> (\w+)", block, re.M)
    dotted = re.findall(r"^\s*(\w+) -\.-> (\w+)", block, re.M)
    kids = {}
    for a, b in edges:
        kids.setdefault(a, []).append(b)
    root = "P"
    parts = kids[root]
    out = []
    rows = textwrap.wrap(nodes[root], 60)
    out.append(f'<rect x="20" y=".3" width="124" height="{4.1 * len(rows) + 3:.1f}" rx="2" fill="{mc.INK}"/>')
    for j, r in enumerate(rows):
        out.append(t(82, 4.4 + j * 4.1, r, 700, "#fff", "middle"))
    top = 4.1 * len(rows) + 7
    H = top
    for c, p_ in enumerate(parts):
        x = c * 55
        y = top
        prow = textwrap.wrap(nodes[p_], 28)
        ph = 4.1 * len(prow) + 3
        out.append(mc.line(82, top - 3.7, x + 26.5, y, mc.FILL2, .5))
        out.append(f'<rect x="{x + .3:.1f}" y="{y:.1f}" width="53" height="{ph:.1f}" rx="1.6" fill="{mc.ACCENT}"/>')
        for j, r in enumerate(prow):
            out.append(t(x + 2.4, y + 4 + j * 4.1, r, 700, "#fff"))
        y += ph + 2
        for k in kids.get(p_, []):
            krow = textwrap.wrap(nodes[k], 29)
            kh = 4.1 * len(krow) + 2.4
            out.append(f'<rect x="{x + 2:.1f}" y="{y:.1f}" width="51.3" height="{kh:.1f}" rx="1.2" fill="#fff" stroke="{mc.INK}" stroke-width=".35"/>')
            for j, r in enumerate(krow):
                out.append(t(x + 3.6, y + 3.8 + j * 4.1, r, 400))
            y += kh + 1.4
            for gk in kids.get(k, []):
                grow = textwrap.wrap(nodes[gk], 27)
                gh = 4.1 * len(grow) + 2.2
                out.append(f'<rect x="{x + 6:.1f}" y="{y:.1f}" width="47.3" height="{gh:.1f}" rx="1" fill="{mc.FILL}"/>')
                for j, r in enumerate(grow):
                    out.append(t(x + 7.6, y + 3.7 + j * 4.1, r, 400, mc.MUTED))
                y += gh + 1
        H = max(H, y)
    out.append(t(0, H + 4, "the tree's own nodes at 14:19, verbatim, its dotted links left out; no turn marked at 14:19 (from 16:04 the tree names one)", 400, mc.MUTED))
    return mc.svg(164, round(H + 5.8, 1), "".join(out), "The storyteller's story tree as it was at 14:19: the premise, three parts and their beats")


WHERE_FROM = [("the player", "ruv.sgit.ai's talk player", "3314ffe", "ported from ruv.sgit.ai"),
              ("the slide engine", "dev's first pass", "1f7c633", "first pass of the site and the talk"),
              ("the studio's ports", "ruv.sgit.ai's pieces", "team/studio/ROLE.md", "brings ruv.sgit.ai's best pieces"),
              ("motion's animations", "new, on the same engine", "team/motion/ROLE.md", "into animations he can start, stop and step through")]


def where_from(clone):
    out = []
    defs = f'<defs><marker id="wf" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="{mc.ACCENT}"/></marker></defs>'
    for i, (piece, source, ref, words) in enumerate(WHERE_FROM):
        if ref.startswith("team/"):
            txt = subprocess.run(["git", "-C", clone, "show", f"298be4e:{ref}"], capture_output=True, text=True, check=True).stdout
            when = "its role, as its page gives it"
        else:
            txt = subprocess.run(["git", "-C", clone, "log", "-1", "--format=%s", ref], capture_output=True, text=True, check=True).stdout
            when = ref
        if words not in txt:
            sys.exit(f"make_pictures: {words!r} is not in {ref}")
        y = i * 15
        new = source.startswith("new")
        out.append(f'<rect x=".3" y="{y + .3:.1f}" width="56" height="12" rx="1.6" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>' + t(4, y + 7.6, piece, 800))
        if new:
            out.append(t(64, y + 7.6, "new, made on the same slide engine (not a port)", 400, mc.MUTED) + t(64, y + 11.4, when, 400, mc.MUTED))
        else:
            out.append(f'<path d="M57 {y + 6.3:.1f} H96" stroke="{mc.ACCENT}" stroke-width=".7" marker-end="url(#wf)"/>'
                       + f'<rect x="98" y="{y + .3:.1f}" width="65.7" height="12" rx="1.6" fill="{mc.FILL}" stroke="{mc.FILL2}" stroke-width=".4"/>'
                       + t(101, y + 5.6, source, 700) + t(101, y + 9.8, when, 400, mc.MUTED))
    H = len(WHERE_FROM) * 15
    out.append(t(0, H + 3, "each arrow points back to where the piece came from, each source checked by git at build", 400, mc.MUTED))
    return mc.svg(164, round(H + 4.8, 1), defs + "".join(out), "Where the afternoon's pieces came from: the player and the ports from ruv.sgit.ai, the engine from dev's first pass")


def table(seats, cx=50, cy=34, rx=34, ry=18):
    """A table seen from above, a seat per entry: (kind, member, label), kind one of head, figure, chair, blank."""
    import math
    out = [f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{mc.FILL}" stroke="{mc.INK}" stroke-width=".5"/>']
    n = len(seats)
    for i, (kind, m, label) in enumerate(seats):
        a = math.radians(-90 + i * 360 / n)
        x, y = cx + (rx + 8) * math.cos(a), cy + (ry + 8) * math.sin(a)
        if kind == "head":
            out.append(g(mc.head(m), x - 5, y - 5.6, .25))
        elif kind == "chair":
            out.append(g(mc.line(4, 2, 4, 18, mc.ACCENT, .9) + mc.line(4, 11, 14, 11, mc.ACCENT, .9) + mc.line(14, 11, 14, 18, mc.ACCENT, .9)
                         + mc.line(4, 2, 7, 2, mc.ACCENT, .9), x - 4.5, y - 5.4, .55))
        else:
            out.append(f'<rect x="{x - 4:.1f}" y="{y - 3.6:.1f}" width="8" height="6.4" rx="1.4" fill="#fff" stroke="{mc.FILL2}" stroke-width=".4" stroke-dasharray="1 .6"/>')
        if label:  # outward from the table, clear of its rim
            ly = y - 6.6 if y < cy else y + 6.4
            out.append(t(x, ly, label, 400, mc.ACCENT if kind == "chair" else mc.MUTED, "middle"))
    return "".join(out)


def empty_chair():
    text = (R70 / "12-how-do-we-contain-this.md").read_text()
    quote = "The reviewers share the session's reach: a second reading, not a second identity."
    if quote not in text:
        sys.exit("make_pictures: the debrief's line is not in chapter 12 as quoted")
    sc = scorecard()
    order = sorted(mc.CAST, key=lambda m: sc[m]["first"])
    if len(order) != REG["C011"]["value"]["staffed"]:
        sys.exit("make_pictures: the cast is not C011's staffed number")
    seats = [("head", m, None) for m in order] + [("chair", "security", "security")]
    out = [table(seats)]
    # one member's wake, its two reviews each a reviewer inside it
    x0, y0 = 104, 6
    out.append(f'<rect x="{x0}" y="{y0}" width="58" height="60" rx="2" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>'
               + t(x0 + 3, y0 + 6, "one member's wake", 800))
    for k, (key, words) in enumerate(STEPS):
        y = y0 + 10 + k * 9.6
        rev = key in ("pre_review", "post_review")
        out.append(f'<rect x="{x0 + 3}" y="{y}" width="52" height="8" rx="1" fill="{mc.FILL if rev else "#fff"}" stroke="{mc.FILL2}" stroke-width=".35"/>'
                   + t(x0 + 5, y + 5.4, words, 700 if rev else 400))
        if rev:
            out.append(g(mc.reviewer_figure(None), x0 + 44, y - .6, .2))
    out.append(t(0, 74, "\u201c" + quote + "\u201d (the conductor's debrief)", 400, mc.MUTED))
    return mc.svg(164, 76, "".join(out), "The talk's nine at a table with security's chair empty, and one wake with its two reviews inside it")


def book_table():
    members = sorted(p.name for p in (REPO / "team").iterdir() if p.is_dir() and (p / "ROLE.md").exists())
    drawn = set(mc.CAST) | set(mc.BOOK_TEAM)
    seats = []
    for m in members:
        if m == "security":
            seats.append(("figure", m, "security"))
        elif m in drawn:
            seats.append(("head", m, None))
        else:
            seats.append(("blank", m, m))
    # a long table, half the seats along each side, every seat named (ruv-sgit 083: the round table could not name
    # twenty-two at 9 pt); names staggered on two lines so neighbours never touch
    n = len(seats)
    top, bottom = seats[: (n + 1) // 2], seats[(n + 1) // 2:]
    x0, x1, ty, by = 8.0, 156.0, 22.0, 38.0
    out = [f'<rect x="{x0 - 2}" y="{ty + 4}" width="{x1 - x0 + 4}" height="{by - ty - 6}" rx="3" fill="{mc.FILL}" stroke="{mc.INK}" stroke-width=".5"/>']
    for row, side in ((top, -1), (bottom, 1)):
        step = (x1 - x0) / max(1, len(row))
        for i, (kind, m, _) in enumerate(row):
            cx = x0 + step * (i + .5)
            y = ty - 4 if side < 0 else by + 1.4
            if kind == "blank":
                out.append(f'<rect x="{cx - 5:.2f}" y="{y:.2f}" width="10" height="7" rx="1.4" fill="#fff" stroke="{mc.FILL2}" stroke-width=".4" stroke-dasharray="1 .7"/>')
            else:
                out.append(g(mc.head(m), cx - 5.2, y - 2.6, .26))
            lift = 4.2 * (i % 2)
            ly = (y - 2.6 - lift) if side < 0 else (y + 11.2 + lift)
            col = mc.COLOUR["security"] if m == "security" else (mc.INK if kind != "blank" else mc.MUTED)
            out.append(t(cx, ly, m, 700 if kind != "blank" else 400, col, "middle"))
    out.append(t(0, 66, "this book's team at its table, every member as its team/ folder names it;", 400, mc.MUTED)
               + t(0, 70.2, "security's seat filled; a dashed seat: a member not drawn yet", 400, mc.MUTED))
    return mc.svg(164, 72, "".join(out), "This book's team at one table, every member named, with security's seat filled")


def two_sessions():
    import datetime
    sess = [json.loads(p.read_text()) for p in sorted((REPO / "team" / "storyteller" / "sessions").glob("*/SESSION.json"))]
    old = next(x for x in sess if x["state"] == "superseded")
    new = next(x for x in sess if x["state"] == "current")
    if old["until"] != new["from"]:
        sys.exit("make_pictures: the storyteller's sessions do not hand over at one time")
    at = datetime.datetime.fromisoformat(old["until"].replace("Z", "+00:00"))
    when = f"{at:%H:%M}, {at.day} {at:%B}"
    out = []
    for i, (label, state, line1, tags) in enumerate([("the old session", "superseded", f"ended {when}", ["its key", "its debriefs"]),
                                                     ("the new session", "current", f"from {when}", ["its own key", "its first debrief"])]):
        x = i * 82.4
        warm = state == "superseded"
        out.append(f'<rect x="{x + .3:.1f}" y=".3" width="80.6" height="34" rx="2" fill="#fff" stroke="{mc.FILL2 if warm else mc.INK}" stroke-width=".5"/>'
                   + g(mc.figure("storyteller", "happy"), x + 2, 3, .5) + t(x + 25, 8, label, 800, mc.MUTED if warm else mc.INK)
                   + f'<rect x="{x + 25}" y="11" width="26" height="5" rx="2.5" fill="{mc.FILL if warm else mc.ACCENT}"/>'
                   + t(x + 38, 14.6, state, 700, mc.MUTED if warm else "#fff", "middle") + t(x + 25, 21.6, line1, 400, mc.MUTED))
        for k, tag in enumerate(tags):
            out.append(f'<rect x="{x + 25 + k * 27}" y="25" width="25" height="6" rx="1" fill="#fff" stroke="{mc.FILL2}" stroke-width=".4" stroke-dasharray="1 .6"/>'
                       + t(x + 26.4 + k * 27, 29.4, tag, 400, mc.MUTED))
        if warm:
            out.append(mc.line(x + 3, 33, x + 78, 2, mc.FILL2, .4))
    # the key register: each member's public key against its session, drawn as rows of blank tags
    members = sorted(p.name for p in (REPO / "team").iterdir() if p.is_dir() and (p / "ROLE.md").exists())
    y0 = 40
    out.append(t(0, y0 + 3, "the key register, described: each member's public key against its session", 700))
    for i, m in enumerate(members):
        x, y = (i % 3) * 55, y0 + 7 + (i // 3) * 7
        out.append(t(x, y + 3.6, m, 400, mc.INK) + "".join(f'<rect x="{x + 24 + k * 14}" y="{y}" width="12" height="4.6" rx=".8" fill="{mc.FILL}" stroke="{mc.FILL2}" stroke-width=".3"/>' for k in range(2)))
    H = y0 + 7 + ((len(members) + 2) // 3) * 7
    out.append(t(0, H + 4, "the role carries on; the key does not. No key, fingerprint or session id printed; the tags are blank on purpose", 400, mc.MUTED))
    return mc.svg(164, round(H + 5.8, 1), "".join(out), "Two sessions of one member, the old superseded and the new with its own key; the key register as blank tags")


def start_sheet():
    import textwrap
    text = (R70 / "01b-start-here.md").read_text()
    steps = re.findall(r"^- \[ \] \*\*(.+?)\*\*(.*)$", text, re.M)
    if len(steps) != 5:
        sys.exit(f"make_pictures: the start-here page gives {len(steps)} steps, the sheet expects five")
    out = [f'<rect x=".3" y=".3" width="163.4" height="{{H}}" rx="1.6" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>',
           t(5, 9, "Start here", 800, mc.INK, size=4.6)]
    y = 18.0
    from html import escape
    for bold, rest in steps:
        # one run per step: the bold title and its rest wrap together, so ", in your own words" stays on the title's line;
        # no drawn-in caption, the book's own Figure line is the caption (conductor 056)
        words = [(w, 700) for w in bold.split()] + [(w, 400) for w in rest.split()]
        lines, cur, width = [], [], 0
        for w, wgt in words:
            if cur and width + 1 + len(w) > 94:
                lines.append(cur)
                cur, width = [], 0
            width += len(w) + (1 if cur else 0)
            cur.append((w, wgt))
        lines.append(cur)
        out.append(f'<rect x="5" y="{y - 3.4:.1f}" width="4.2" height="4.2" rx=".5" fill="#fff" stroke="{mc.INK}" stroke-width=".5"/>')
        for j, line in enumerate(lines):
            runs = []
            for w, wgt in line:
                if runs and runs[-1][1] == wgt:
                    runs[-1][0].append(w)
                else:
                    runs.append(([w], wgt))
            # a run that opens on punctuation (", in your own words") follows the bold with no space
            spans = "".join((" " if k and not ws[0][0] in ",.;:" else "")
                            + f'<tspan font-weight="{wgt}">{escape(" ".join(ws), quote=False)}</tspan>'
                            for k, (ws, wgt) in enumerate(runs))
            out.append(f'<text x="13" y="{y + j * 4.1:.2f}" {SANS} font-size="{F}" fill="{mc.INK}">{spans}</text>')
        y += 4.1 * len(lines) + 3
    H = y
    out[0] = out[0].replace("{H}", f"{H:.1f}")
    return mc.svg(164, round(H + .6, 1), "".join(out), "The start-here page as one printable sheet: the five steps, a box beside each")


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
    out.append(t(0, y + 5, "each floor lit by the members whose policy lets them write its pages (scope.writes)", 400, mc.MUTED))
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
               + t(W, y + h + 9.8, "none of them said on stage" if not on_stage else "", 400, mc.MUTED, "end")
               + mc.line(x + w / 2, y + h, x + w / 2, y + h + 2, mc.ACCENT, .5))
    out.append(t(0, y + h + 5.6, f"{v['claims']} claims, built at {v['built'][11:16]}", 400, mc.MUTED))
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
             "ch8-check-card.svg": check_card(), "ch8-two-companions.svg": two_companions(),
             "ch8-plumbing.svg": plumbing(), "ch8-release-row.svg": release_row(clone),
             "ch-security-card.svg": security_card(),
             "ch4-three-greyed.svg": three_greyed(clone), "ch4-security-proposed.svg": security_proposed(clone),
             "ch6-two-commits.svg": two_commits(clone), "ch6-letter-path.svg": letter_path(),
             "ch9-story-tree.svg": story_tree(clone), "ch9-where-from.svg": where_from(clone),
             "ch12-empty-chair.svg": empty_chair(), "ch12-book-table.svg": book_table(),
             "ch13-two-sessions.svg": two_sessions(), "ch1b-start-sheet.svg": start_sheet()}
    if (R70 / "15-principles.md").exists():
        files["ch15-six-principles.svg"] = six_principles()
    else:  # chapter 15 was folded into 16 and removed: the drawing stays as last built from it, not rebuilt
        print("ch15-six-principles.svg kept as built: manuscript/rc2/70/15-principles.md is gone")
    for name, svg in files.items():
        (HERE / name).write_text(svg)
    print("written " + ", ".join(files))
