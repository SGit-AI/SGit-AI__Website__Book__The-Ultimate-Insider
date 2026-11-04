#!/usr/bin/env python3
"""LAB 56: chapter 7's "one rule's journey in an hour" (line 67; ruv-sgit's must, its 074) and chapter 5's publishing flow
for its concept callout (line 57; the writer's 229; LAB 48's callout, its picture column).

    python3 lab/experiments/56-designer-rule-and-flow/make_rule_and_flow.py <talk clone>

- rule-journey.svg: a line of time across hour three (clock 02:00 to 03:00), the rule moving from a page to a setting:
  written in the conductor's wake rules (5700bab), dev's wake opening with the request in its mail (its record's start),
  in the gate (99aaf05), and from then on a red mark on any release whose wake skipped a step. Every time read with git at
  298be4e at build; the times in the picture, not in any line; no hash drawn.
- publishing-flow.svg: a commit, the build, the gate, the release, and the gate's no sending the change back; drawn
  56 mm wide for the callout's picture column (a third of the measure), so its 9 pt labels stay 9 pt. No key, session or
  version number drawn.
"""
import json, re, subprocess, sys
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'


def t(x, y, s, weight=400, fill=mc.INK, anchor="start", size=3.18):
    return (f'<text x="{x:.2f}" y="{y:.2f}" {SANS} font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}">{escape(str(s), quote=False)}</text>')


def git(clone, *a):
    return subprocess.run(["git", "-C", clone, *a], capture_output=True, text=True, check=True).stdout.strip()


def when(clone, rev):
    return git(clone, "log", "-1", "--format=%ad", "--date=format:%H:%M", rev)


def rule_journey(clone):
    w = when(clone, "5700bab")
    rec = json.loads(git(clone, "show", "298be4e:team/dev/wakes/20261029T024849Z.json"))
    o = rec["started"][11:16]
    g = when(clone, "99aaf05")
    if not (w < o < g and w.startswith("02:") and g.startswith("02:")):
        sys.exit(f"make_rule_and_flow: the hour's times are not in order: {w}, {o}, {g}")
    x0, x1, y = 6.0, 94.0, 22.0
    X = lambda hm: x0 + (x1 - x0) * (int(hm[:2]) * 60 + int(hm[3:]) - 120) / 60
    out = [mc.line(x0, y, x1, y, mc.INK, .7)]
    for m in (0, 15, 30, 45, 60):
        x = x0 + (x1 - x0) * m / 60
        out.append(mc.line(x, y, x, y + 1.5, mc.INK, .35) + t(x, y + 6, f"0{2 + m // 60}:{m % 60:02d}", 400, mc.MUTED, "middle"))
    stops = [(w, "written in the conductor's wake rules", -1, "start"), (o, "dev's wake opens, the request in its mail", 1, "end"),
             (g, "in the gate, for every member", -2, "end")]
    for hm, words, tier, anchor in stops:
        x = X(hm)
        ly = y - 7 if tier == -1 else (y - 14 if tier == -2 else y + 13)
        out.append(f'<circle cx="{x:.2f}" cy="{y}" r="1.6" fill="{mc.ACCENT if hm == g else mc.INK}"/>'
                   + mc.line(x, y + (-2 if tier < 0 else 2), x, ly + (1 if tier < 0 else -3.2), mc.FILL2, .3)
                   + t(x + (1 if anchor == "start" else -0), ly, f"{hm}  {words}", 700 if hm == g else 400, mc.INK, anchor))
    # from then on: the rule is a setting; a red mark on any release whose wake skipped a step
    xg = X(g)
    out.append(f'<path d="M{xg + 2:.2f} {y - 3.4} H{x1 + 28}" stroke="{mc.ACCENT}" stroke-width=".9" fill="none" stroke-dasharray="2 1.2"/>'
               f'<path d="M{x1 + 28} {y - 3.4} l-2.4 -1.4 v2.8 z" fill="{mc.ACCENT}"/>')
    for k in range(3):
        cx = x1 + 14 + k * 8
        out.append(f'<rect x="{cx - 2.6:.2f}" y="{y - 12:.2f}" width="5.2" height="5.2" rx=".8" fill="#fff" stroke="{mc.FILL2}" stroke-width=".4"/>'
                   + (f'<path d="M{cx - 1.4:.2f} {y - 10.8:.2f} l2.8 2.8 M{cx + 1.4:.2f} {y - 10.8:.2f} l-2.8 2.8" stroke="{mc.ACCENT}" stroke-width=".7"/>' if k == 1 else ""))
    out.append(t(x1 + 4, y + 12.4, "from then on, a red mark on any", 400, mc.ACCENT)
               + t(x1 + 4, y + 16.6, "release whose wake skipped a step", 400, mc.ACCENT))
    return mc.svg(156, round(y + 19.5, 1), "".join(out), f"One rule's journey in an hour: written at {w}, asked of dev at {o}, in the gate at {g}, then a red mark on any release whose wake skipped a step")


def publishing_flow():
    steps = ["a commit", "the build", "the gate", "the release"]
    out, bw, bh, x, y = [], 30.0, 8.0, 2.0, 1.0
    for k, s in enumerate(steps):
        gate = s == "the gate"
        out.append(f'<rect x="{x}" y="{y:.1f}" width="{bw}" height="{bh}" rx="1.6" fill="{mc.FILL if not gate else "#fff"}" stroke="{mc.ACCENT if gate else mc.INK}" stroke-width="{.9 if gate else .5}"/>'
                   + t(x + bw / 2, y + 5.3, s, 700, mc.INK, "middle"))
        if k < len(steps) - 1:
            out.append(f'<path d="M{x + bw / 2} {y + bh} v4.2" stroke="{mc.INK}" stroke-width=".5"/><path d="M{x + bw / 2} {y + bh + 5} l-1.3 -2 h2.6 z" fill="{mc.INK}"/>')
        y += bh + 5
    # the gate's no, back to the commit
    gy, cy = 1.0 + 2 * (bh + 5) + bh / 2, 1.0 + bh / 2
    out.append(f'<path d="M{x + bw} {gy:.1f} H{x + bw + 10} V{cy:.1f} H{x + bw + 2.4}" fill="none" stroke="{mc.ACCENT}" stroke-width=".8"/>'
               f'<path d="M{x + bw + .4} {cy:.1f} l2.4 -1.4 v2.8 z" fill="{mc.ACCENT}"/>'
               + t(x + bw + 11.6, (gy + cy) / 2 + 1.1, "no", 800, mc.ACCENT))
    return mc.svg(56, round(y - 4, 1), "".join(out), "The publishing flow: a commit, the build, the gate, the release, and the gate's no sending the change back")


if __name__ == "__main__":
    files = {"rule-journey.svg": rule_journey(sys.argv[1]), "publishing-flow.svg": publishing_flow()}
    for name, svg in files.items():
        if re.search(r">[^<]*(\bC\d{3}\b|\b[0-9a-f]{7}\b|v0\.\d)", svg):
            sys.exit(f"make_rule_and_flow: {name} draws an id, a hash or a version")
        (HERE / name).write_text(svg)
    print("written " + ", ".join(files))
