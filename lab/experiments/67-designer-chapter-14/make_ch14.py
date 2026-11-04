#!/usr/bin/env python3
"""LAB 67: chapter 14's two figures (manuscript/rc2/150/14-port-not-rebuild.md).

    python3 lab/experiments/67-designer-chapter-14/make_ch14.py <the talk's clone, read only>

1. three-decisions.svg: a card, the three decisions on one line of time: the talk's frame (the decisions round), the
   work step's new length, the two new members. Every time and length is read from C104 (checked) at build.
2. three-gates.svg: the plan of three parts as three gates on the clock, each with its lock time, as planned (C027,
   checked), and the minute the plan was set, read with git from the talk's commit. Drawn as planned, not as it turned
   out (the brief). Times in the picture only; no register id or hash drawn.
"""
import json, re, subprocess, sys
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'
REG = {c["id"]: c for c in json.loads((REPO / "claims" / "register.json").read_text())["claims"]}


def t(x, y, s, weight=400, fill=mc.INK, anchor="middle", size=3.18):
    return (f'<text x="{x:.2f}" y="{y:.2f}" {SANS} font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}">{escape(str(s), quote=False)}</text>')


def hm(s):
    m = re.search(r"\b(\d\d):(\d\d)", s)
    if not m:
        sys.exit(f"make_ch14: no time in '{s}'")
    return m.group(0)


def mins(x):
    h, m = map(int, x.split(":"))
    return h * 60 + m


def checked(cid):
    c = REG.get(cid)
    if not c or c.get("state") != "checked":
        sys.exit(f"make_ch14: {cid} is missing or not checked")
    return c["value"]


def decisions():
    v = checked("C104")
    d, w, m = v["decisions_round"], v["longer_work_step"], v["two_members_brought_on"]
    lengths = re.search(r"limit is (\d+) minutes.*\(it was (\d+)\)", w["recorded"])
    who = re.search(r"for (\w+) and (\w+)", m["recorded"])
    if not lengths or not who:
        sys.exit("make_ch14: C104 no longer gives the step's lengths or the two members")
    marks = [(hm(d["recorded"]), "the talk's frame", [f"the decisions round, given {d['given'].split(' (')[0]}"]),
             (hm(w["recorded"]), "the work step's new length", [f"{lengths.group(1)} minutes; it was {lengths.group(2)}"]),
             (hm(m["given"]), "two new members", [f"{who.group(1)} and {who.group(2)}, {m['given'].split(',')[0]}"])]
    lo, hi = mins("15:00"), mins("15:30")
    x0, x1 = 8.0, 148.0
    X = lambda s: x0 + (x1 - x0) * (mins(s) - lo) / (hi - lo)
    out = [f'<rect x=".3" y=".3" width="155.4" height="{{H}}" rx="1.8" fill="#fff" stroke="{mc.INK}" stroke-width=".45"/>',
           t(4, 6, "the afternoon's three decisions", 800, mc.INK, "start"),
           mc.line(x0, 14, x1, 14, mc.INK, .5)]
    for s in ("15:00", "15:10", "15:20", "15:30"):
        out.append(mc.line(X(s), 12.8, X(s), 15.2, mc.MUTED, .35) + t(X(s), 11.2, s, 400, mc.MUTED))
    cols = [6.0, 57.0, 108.0]
    for k, (when, head, rows) in enumerate(marks):
        x = X(when)
        out.append(f'<circle cx="{x:.2f}" cy="14" r="1.6" fill="{mc.ACCENT}"/>'
                   f'<path d="M{x:.2f} 15.6 L{x:.2f} 17.4 L{cols[k] + 2:.2f} 19.6" stroke="{mc.MUTED}" stroke-width=".35" fill="none"/>')
        out.append(t(cols[k], 25, when, 800, mc.ACCENT, "start", size=4.2) + t(cols[k], 29.6, head, 700, mc.INK, "start"))
        import textwrap
        lines = [w for r in rows for w in textwrap.wrap(r, 27)]
        for j, r in enumerate(lines):
            out.append(t(cols[k], 33.8 + 4.1 * j, r, 400, mc.MUTED, "start"))
        nmax = max(locals().get("nmax", 0), len(lines))
    H = 33.8 + 4.1 * (nmax - 1) + 3.8
    out[0] = out[0].replace("{H}", f"{H}")
    return mc.svg(156, round(H + .6, 1), "".join(out), "A card: the three decisions on one line of time, the talk's frame, the work step's new length, and the two new members")


def gates(clone):
    v = checked("C027")
    plan = v["planned"]
    locks = [("part one", plan["part_1"]), ("part two", plan["part_2"]), ("part three", plan["part_3"])]
    sha = "3342cff"
    subj = subprocess.run(["git", "-C", clone, "show", "-s", "--format=%cI %s", sha], capture_output=True, text=True, check=True).stdout
    set_at = subj[11:16]
    if not all(l[1] in subj for l in locks):
        sys.exit("make_ch14: the plan's commit no longer names C027's lock times")
    lo, hi = mins("16:30"), mins("20:30")
    x0, x1 = 8.0, 150.0
    X = lambda s: x0 + (x1 - x0) * (mins(s) - lo) / (hi - lo)
    base = 42.0
    out = [mc.line(x0, base, x1, base, mc.INK, .5)]
    for h in ("17:00", "18:00", "19:00", "20:00"):
        out.append(mc.line(X(h), base - 1.2, X(h), base + 1.2, mc.MUTED, .35) + t(X(h), base + 5, h, 400, mc.MUTED))
    # the minute the plan was set
    xs = X(set_at)
    out.append(f'<circle cx="{xs:.2f}" cy="{base}" r="1.5" fill="{mc.INK}"/>' + t(xs, base - 4, f"set at {set_at}", 700, mc.INK))
    for k, (name, at) in enumerate(locks):
        x = X(at)
        lift = 8.4 if k == 2 else 0  # the last gate's words above the one before it, half an hour apart
        out.append(f'<path d="M{x - 6:.2f} {base} V{base - 15} M{x + 6:.2f} {base} V{base - 15}" stroke="{mc.INK}" stroke-width="1"/>'
                   f'<path d="M{x - 7.4:.2f} {base - 15} H{x + 7.4:.2f}" stroke="{mc.INK}" stroke-width="1.4"/>'
                   f'<path d="M{x - 6:.2f} {base - 3} H{x + 6:.2f} M{x - 6:.2f} {base - 7.5} H{x + 6:.2f} M{x - 6:.2f} {base - 12} H{x + 6:.2f}" stroke="{mc.FILL2}" stroke-width=".7"/>'
                   # a lock, open: planned, not yet closed
                   f'<rect x="{x - 2:.2f}" y="{base - 9.6:.2f}" width="4" height="3.4" rx=".5" fill="{mc.ACCENT}"/>'
                   f'<path d="M{x - 1.2:.2f} {base - 9.6:.2f} v-1.6 a1.2 1.2 0 0 1 2.4 0" stroke="{mc.ACCENT}" stroke-width=".5" fill="none"/>')
        if lift:
            out.append(mc.line(x, base - 15.8, x, base - 18 - lift + 1.4, mc.MUTED, .35))
        out.append(t(x, base - 22.2 - lift, name, 700, mc.INK) + t(x, base - 18 - lift, f"locks at {at}", 700, mc.ACCENT))
    out.append(t(x0, base + 11, "the plan as drawn at the minute it was set: three parts, each done, timed, then locked", 400, mc.MUTED, "start"))
    return mc.svg(156, round(base + 13, 1), "".join(out), "The plan of three parts, drawn as three gates on the clock, each with its lock time, as planned")


def main():
    clone = sys.argv[1]
    for name, svg in {"three-decisions.svg": decisions(), "three-gates.svg": gates(clone)}.items():
        if re.search(r">[^<]*\b(C\d{3}|[0-9a-f]{7,})\b", svg):
            sys.exit(f"make_ch14: {name} draws an id or a hash")
        (HERE / name).write_text(svg)
        print("written", name)


if __name__ == "__main__":
    main()
