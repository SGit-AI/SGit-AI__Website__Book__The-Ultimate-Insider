#!/usr/bin/env python3
"""LAB 73: chapter 16's figure, the last ten minutes with the three open sessions as bars running past the hold
(manuscript/rc2/150/16-*.md, its brief: "the bars stop where the record stops them").

    python3 lab/experiments/73-designer-chapter-16/make_ch16.py <the talk's clone, read only>

Every commit on the main line (298be4e) from 18:40 to 18:50 is a dot, read with git. The hold's minute is C006's and
C065's. Each bar ends where its member's record ends, read with git, not assumed:
- the designer's at its last commit after the hold, and again at the first release that carries it;
- dev's at its last commit after the hold, which is checked to be off the main line (not an ancestor of 298be4e);
- deck's has no commit after the hold, which is checked, and runs off the edge.
No hash or register id drawn (principle 28).
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
LO, HI = "2026-10-29T18:40:00Z", "2026-10-29T18:50:00Z"


def t(x, y, s, weight=400, fill=mc.INK, anchor="middle", size=3.18):
    return (f'<text x="{x:.2f}" y="{y:.2f}" {SANS} font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}">{escape(str(s), quote=False)}</text>')


def git(clone, *a, ok=False):
    r = subprocess.run(["git", "-C", clone, *a], capture_output=True, text=True)
    if r.returncode and not ok:
        sys.exit(f"make_ch16: git {' '.join(a)} failed")
    return r


def secs(hms):
    h, m, s = map(int, hms.split(":"))
    return h * 3600 + m * 60 + s


def main():
    clone = sys.argv[1]
    for cid in ("C006", "C065"):
        if REG[cid]["state"] != "checked":
            sys.exit(f"make_ch16: {cid} is not checked")
    hold = REG["C065"]["value"]["hold"].split()[1]
    if not REG["C006"]["value"].startswith(hold):
        sys.exit("make_ch16: C006 and C065 disagree on the hold's minute")
    main_line = [l.split(" ", 2) for l in git(clone, "log", "298be4e", f"--since={LO}", f"--until={HI}", "--format=%cI %H %s").stdout.splitlines()]
    dots = [(c[0][11:19], c[2]) for c in main_line]
    allc = [l.split(" ", 2) for l in git(clone, "log", "--all", f"--since={HOLD_ISO(hold)}", f"--until={HI}", "--format=%cI %H %s").stdout.splitlines()]

    def last(member):
        mine = [c for c in allc if c[2].startswith(f"@{member}:")]
        return mine[0] if mine else None
    d, v, k = last("designer"), last("dev"), last("deck")
    if not d or not v:
        sys.exit("make_ch16: the designer's or dev's commit after the hold is missing")
    if k:
        sys.exit("make_ch16: deck has a commit after the hold; its bar would end")
    if git(clone, "merge-base", "--is-ancestor", v[1], "298be4e", ok=True).returncode == 0:
        sys.exit("make_ch16: dev's last commit is on the main line, not off it")
    rel = next((c for c in reversed(main_line) if c[2].startswith("site v")
                and git(clone, "merge-base", "--is-ancestor", d[1], c[1], ok=True).returncode == 0), None)
    if not rel:
        sys.exit("make_ch16: no release on the main line carries the designer's commit")
    d_end, d_rel, v_end = d[0][11:19], rel[0][11:19], v[0][11:19]
    if d_end != REG["C065"]["value"]["designer"].split()[1]:
        sys.exit("make_ch16: the designer's commit is not C065's")

    x0, x1 = 30.0, 150.0
    X = lambda s: x0 + (x1 - x0) * (secs(s) - secs("18:40:00")) / 600
    out = []
    ly = 12.0
    out.append(mc.line(x0, ly, x1, ly, mc.INK, .5))
    for m in range(0, 11, 2):
        hm = f"18:{40 + m}:00"
        out.append(mc.line(X(hm), ly - 1.2, X(hm), ly + 1.2, mc.MUTED, .35) + t(X(hm), 6, hm[:5], 400, mc.MUTED))
    for s, subj in dots:
        out.append(f'<circle cx="{X(s):.2f}" cy="{ly}" r="1" fill="{mc.ACCENT if subj.startswith("@conductor: hold") else mc.INK}"/>')
    out.append(t(4, ly + 1.1, "every commit", 400, mc.MUTED, "start"))
    # the hold, top to bottom
    xh = X(hold)
    yb = 54.0
    out.append(f'<path d="M{xh:.2f} {ly + 2} V{yb}" stroke="{mc.ACCENT}" stroke-width=".8"/>' + t(xh, yb + 4.2, f"the hold, {hold[:5]}", 800, mc.ACCENT))
    rows = [("designer", d_end, f"its work, {d_end[:5]}; out in the last release, {d_rel[:5]}", d_rel),
            ("dev", v_end, f"its wake closed on its own branch, {v_end[:5]}", None),
            ("deck", None, "never ended", None)]
    for i, (who, end, note, rel_at) in enumerate(rows):
        y = 18 + i * 11.4
        col = mc.COLOUR.get(who, mc.INK)
        xe = X(end) if end else x1 + 4
        out.append(t(4, y + 2.2, who, 700, mc.INK, "start"))
        out.append(f'<rect x="{x0:.2f}" y="{y}" width="{xe - x0:.2f}" height="3.2" rx="1.2" fill="{col}"/>')
        if end:
            out.append(f'<path d="M{xe:.2f} {y - .8} V{y + 4}" stroke="{mc.INK}" stroke-width=".6"/>')
        else:
            out.append(f'<path d="M{xe:.2f} {y - .6} l2.4 2.2 l-2.4 2.2" fill="none" stroke="{col}" stroke-width=".6"/>')
        if rel_at:
            out.append(f'<rect x="{xe:.2f}" y="{y + .9:.2f}" width="{X(rel_at) - xe:.2f}" height="1.4" fill="{col}" fill-opacity=".45"/>'
                       f'<path d="M{X(rel_at):.2f} {y - .8} V{y + 4}" stroke="{mc.INK}" stroke-width=".6"/>')
        out.append(t(xh + 2.4, y + 7.4, note, 400, mc.MUTED, "start"))
    svg = mc.svg(156, round(yb + 6, 1), "".join(out), "The last ten minutes: every commit a dot, the hold, and three sessions as bars running past it; the designer's ending in the last release, dev's on its own branch, deck's never ending")
    if re.search(r">[^<]*\b(C\d{3}|[0-9a-f]{7,})\b", svg):
        sys.exit("make_ch16: an id or a hash is drawn")
    (HERE / "three-sessions.svg").write_text(svg)
    print(f"written three-sessions.svg: {len(dots)} dots; designer {d_end}, release {d_rel}; dev {v_end}; deck open")


def HOLD_ISO(hold):
    return f"2026-10-29T{hold}Z"


if __name__ == "__main__":
    main()
