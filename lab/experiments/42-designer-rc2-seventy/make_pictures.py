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
  chapter 16 at build (fifteen lines, chapters 1 to 15 in order, or the build stops).
No number is printed but the hold's time, ids, C029's counts and the chapters' own times. One SVG unit a millimetre, sizes stated, text 9 pt.
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
    if [int(c) for c, _ in items] != list(range(1, 16)):
        sys.exit("make_pictures: chapter 16's checklist is not chapters 1 to 15 in order")
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
             "ch8-register-bar.svg": register_bar(), "ch15-six-principles.svg": six_principles(), "ch16-checklist.svg": checklist()}
    for name, svg in files.items():
        (HERE / name).write_text(svg)
    print("written " + ", ".join(files))
