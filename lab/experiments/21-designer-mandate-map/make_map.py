#!/usr/bin/env python3
"""LAB 21's drawing: the talk's repository at 298be4e as a map of its folders, sized by their files, with the talk
designer's mandate (its policy.json scope.writes) shaded and the folders its own commits touched outlined.

    python3 lab/experiments/21-designer-mandate-map/make_map.py <a read-only clone of the talk's repository>
writes mandate-map.svg beside this file. Reads the clone with git only (ls-files, log, show --name-only); no file
contents. One SVG unit is one millimetre; labels are 9 pt; no number is printed.
"""
import json, subprocess, sys
from collections import Counter
from pathlib import Path

REV, W, H, FONT = "298be4e", 163.0, 118.0, 3.18
INK, MUTED, FILL, FILL2, ACCENT, TINT = "#1f2933", "#5b6670", "#eef2f6", "#d5dce4", "#b0481a", "#f6e1d4"


def git(clone, *args):
    return subprocess.run(["git", "-C", clone, *args], capture_output=True, text=True, check=True).stdout


def main(clone):
    files = git(clone, "ls-tree", "-r", "--name-only", REV).split()
    top = Counter(f.split("/")[0] if "/" in f else "(files at the root)" for f in files)
    team = Counter(f.split("/")[1] for f in files if f.startswith("team/") and f.count("/") >= 2)
    scope = json.loads(git(clone, "show", f"{REV}:team/designer/policy.json"))["scope"]["writes"]
    commits = [l.split()[0] for l in git(clone, "log", REV, "--format=%H %s").splitlines() if l.split(" ", 1)[1].startswith("@designer")]
    touched = {"/".join(f.split("/")[:2]) for c in commits for f in git(clone, "show", "--name-only", "--format=", c).split()}
    big = [k for k, _ in top.most_common() if k in ("team", "src", "evidence")]
    other = sum(v for k, v in top.items() if k not in big)
    cols = [(k, top[k]) for k in big] + [("everything else", other)]
    total = sum(v for _, v in cols)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H + 12}" class="mandate" role="img" aria-label="The talk repository at 298be4e as a map of its folders, sized by their files. The whole of it is what any member could push to. One small box, team/designer, is shaded: the talk designer\'s mandate. Every folder its own commits touched lies inside that box.">']
    x = 0.0
    for name, n in cols:
        w = W * n / total
        if name == "team":
            y = 0.0
            for member, m in team.most_common():
                h = H * m / sum(team.values())
                mine = f"team/{member}/**" in scope
                out.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" fill="{TINT if mine else FILL}" stroke="#fff" stroke-width=".6"/>')
                if mine:
                    out.append(f'<rect x="{x + .5:.2f}" y="{y + .5:.2f}" width="{w - 1:.2f}" height="{h - 1:.2f}" fill="none" stroke="{ACCENT}" stroke-width="1"/>')
                if h > FONT * 1.6:
                    out.append(f'<text x="{x + 1.5:.2f}" y="{y + FONT + 0.6:.2f}" font-family="Inter, Helvetica, Arial, sans-serif" font-size="{FONT}" fill="{ACCENT if mine else MUTED}"{" font-weight=\"800\"" if mine else ""}>team/{member}</text>')
                y += h
        else:
            out.append(f'<rect x="{x:.2f}" y="0" width="{w:.2f}" height="{H}" fill="{FILL2}" stroke="#fff" stroke-width=".6"/>')
            if w > len(name) * 1.75 + 2:
                out.append(f'<text x="{x + 1.5:.2f}" y="{FONT + 1:.2f}" font-family="Inter, Helvetica, Arial, sans-serif" font-size="{FONT}" fill="{INK}">{name}/' if name != "everything else" else f'<text x="{x + 1.5:.2f}" y="{FONT + 1:.2f}" font-family="Inter, Helvetica, Arial, sans-serif" font-size="{FONT}" fill="{INK}">rest</text>')
                if name != "everything else":
                    out[-1] += "</text>"
                else:
                    out[-1] += ""
        x += w
    out.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="none" stroke="{INK}" stroke-width=".6"/>')
    out.append(f'<text x="0" y="{H + 5}" font-family="Inter, Helvetica, Arial, sans-serif" font-size="{FONT}" fill="{INK}">The whole frame: what any member could push to (reach).</text>')
    out.append(f'<text x="0" y="{H + 9.5}" font-family="Inter, Helvetica, Arial, sans-serif" font-size="{FONT}" fill="{ACCENT}" font-weight="800">The outlined box: what the designer was allowed to write (mandate).</text>')
    out.append("</svg>")
    svg = "".join(out).replace('fill="#1f2933">rest', 'fill="#1f2933">rest</text>')
    (Path(__file__).parent / "mandate-map.svg").write_text(svg)
    inside = all(t.startswith("team/designer") for t in touched)
    print(f"written mandate-map.svg; the designer's commits touched only its mandate: {inside}")


if __name__ == "__main__":
    main(sys.argv[1])
