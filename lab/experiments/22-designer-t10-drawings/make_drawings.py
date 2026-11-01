#!/usr/bin/env python3
"""The four drawings the ten-page sample asks for (chapter-plan/first-ten-pages-outline.md; the publisher's letter 006).

    python3 lab/experiments/22-designer-t10-drawings/make_drawings.py <a read-only clone of the talk's repository>
writes cast-row.svg, day-timeline.svg, loop.svg and book-map.svg beside this file, each 120 mm wide (the sample's
text block at 6 x 9 in), one SVG unit a millimetre, all text 9 pt. Each SVG states its own size in millimetres, so
it prints at that size in any build and is never scaled up: the text inside a drawing stays at or below the body
(the editor's page 7 note, 1 November 2026). The clone is read with git only, at 298be4e.
No number is printed except the clock's hours and the hold's minute (C006); no name but the editor's.
"""
import json, subprocess, sys
from pathlib import Path

HERE, REV, W, F = Path(__file__).resolve().parent, "298be4e", 120.0, 3.18
INK, MUTED, FILL, FILL2, ACCENT, TINT = "#1f2933", "#5b6670", "#eef2f6", "#d5dce4", "#b0481a", "#f6e1d4"
SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'


def sized(svg):
    """Give the root its size in millimetres from its viewBox (one unit a millimetre)."""
    import re
    _, _, w, h = re.search(r'viewBox="([^"]+)"', svg).group(1).split()
    return svg.replace("<svg ", f'<svg width="{w}mm" height="{h}mm" ', 1)


def git(clone, *a):
    return subprocess.run(["git", "-C", clone, *a], capture_output=True, text=True, check=True).stdout


def t(x, y, s, size=F, weight=400, fill=INK, anchor="start"):
    return f'<text x="{x:.2f}" y="{y:.2f}" {SANS} font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'


def robot(x, y, s=1.0, clock=False):
    """A small cast robot: the conductor has a clock face; the others a plain face."""
    face = (f'<circle cx="{x}" cy="{y + 3.2 * s}" r="{1.9 * s}" fill="#fff" stroke="{INK}" stroke-width=".35"/>'
            f'<line x1="{x}" y1="{y + 3.2 * s}" x2="{x}" y2="{y + 2 * s}" stroke="{INK}" stroke-width=".35"/>'
            f'<line x1="{x}" y1="{y + 3.2 * s}" x2="{x + 1 * s}" y2="{y + 3.6 * s}" stroke="{ACCENT}" stroke-width=".35"/>') if clock else \
           (f'<circle cx="{x - 1 * s}" cy="{y + 3 * s}" r="{.45 * s}" fill="{INK}"/><circle cx="{x + 1 * s}" cy="{y + 3 * s}" r="{.45 * s}" fill="{INK}"/>')
    return (f'<rect x="{x - 3.2 * s}" y="{y}" width="{6.4 * s}" height="{5.6 * s}" rx="{1.2 * s}" fill="{FILL}" stroke="{INK}" stroke-width=".45"/>' + face
            + f'<rect x="{x - 2.4 * s}" y="{y + 6.2 * s}" width="{4.8 * s}" height="{3.8 * s}" rx="{.9 * s}" fill="{FILL2}" stroke="{INK}" stroke-width=".45"/>')


def cast_row(clone):
    src = git(clone, "show", f"{REV}:src/static/motion/lab/meet-the-team/v1/index.html")
    line = src[src.index("var SHORT = {"):src.index("}", src.index("var SHORT = {")) + 1]
    short = dict((k.strip().strip("'"), v.strip().strip("'")) for k, v in (p.split(":", 1) for p in line[line.index("{") + 1:-1].split(",")))
    order = ["conductor", "storyteller", "researcher", "deck", "dev", "designer", "motion", "ruv-sgit", "studio"]
    cw, ch = W / 3, 17.0
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {ch * 3:.1f}" role="img" aria-label="The talk\'s team of nine agents, one line each, in the talk\'s own words: the conductor first.">']
    for i, m in enumerate(order):
        x, y = (i % 3) * cw, (i // 3) * ch
        lead = m == "conductor"
        out.append(f'<rect x="{x + .5:.2f}" y="{y + .5:.2f}" width="{cw - 1:.2f}" height="{ch - 1:.2f}" rx="1.5" fill="{TINT if lead else "#fff"}" stroke="{ACCENT if lead else FILL2}" stroke-width="{.6 if lead else .35}"/>')
        out.append(robot(x + 6.5, y + 3, 1.0, clock=lead))
        out.append(t(x + 12.5, y + 7, m, weight=800, fill=ACCENT if lead else INK))
        out.append(t(x + 12.5, y + 11.5, short[m], fill=MUTED))
    out.append("</svg>")
    return "".join(out)


def day_timeline(clone):
    names = git(clone, "ls-tree", "-r", "--name-only", REV).split()
    wakes = []
    for f in names:
        if "/wakes/" in f and f.endswith(".json"):
            d = json.loads(git(clone, "show", f"{REV}:{f}"))
            k, s = d.get("kind", "").lower(), d.get("started", "")
            if not s.startswith("2026-10-29"):
                continue
            kind = "editor" if "editor" in k else ("follow" if "follow" in k else "scheduled")
            hh, mm = int(s[11:13]), int(s[14:16])
            wakes.append((hh * 60 + mm, kind))
    x0, x1 = 6.0, W - 4
    X = lambda m: x0 + (x1 - x0) * m / (19 * 60)
    rows = {"scheduled": 19.0, "follow": 19.0, "editor": 31.0}   # both rows stack upward, never into the axis
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 52" role="img" aria-label="29 October 2026 from midnight to 19:00: each wake of the talk team a dot, scheduled wakes in one row, wakes the editor started in the other, the night until 06:00 shaded, the hold at 18:44.">',
           f'<rect x="{X(16):.2f}" y="5.5" width="{X(360) - X(16):.2f}" height="27.5" fill="{FILL}"/>',
           t(X(16) + 1, 9.4, "night", fill=MUTED)]
    for h in (0, 6, 12, 18):
        out.append(f'<line x1="{X(h * 60):.2f}" y1="33" x2="{X(h * 60):.2f}" y2="35" stroke="{INK}" stroke-width=".35"/>' + t(X(h * 60), 39.5, f"{h:02d}:00", anchor="middle", fill=MUTED))
    out.append(f'<line x1="{x0}" y1="33" x2="{x1}" y2="33" stroke="{INK}" stroke-width=".4"/>')
    placed = []
    for m, kind in sorted(wakes):
        x, y = X(m), rows[kind]
        while any(abs(x - px) < 1.3 and abs(y - py) < 1.3 for px, py in placed):
            y -= 1.4
        placed.append((x, y))
        col = ACCENT if kind == "editor" else INK
        out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r=".6" fill="{"#fff" if kind == "follow" else col}" stroke="{col}" stroke-width=".3"/>')
    hx = X(18 * 60 + 44)
    out.append(f'<line x1="{hx:.2f}" y1="4" x2="{hx:.2f}" y2="33" stroke="{ACCENT}" stroke-width=".8"/>' + t(hx - 1, 4.5, "the hold, 18:44", weight=800, fill=ACCENT, anchor="end"))
    out.append(f'<circle cx="{x0 + 1}" cy="45" r=".9" fill="{INK}"/>' + t(x0 + 3, 46.2, "scheduled: a member's own clock"))
    out.append(f'<circle cx="{x0 + 62}" cy="45" r=".9" fill="{ACCENT}"/>' + t(x0 + 64, 46.2, "started by the editor", fill=ACCENT))
    out.append(t(x0, 51, "Hollow dots: a follow-up wake the rules asked for.", fill=MUTED))
    out.append("</svg>")
    return "".join(out), len(wakes)


def loop():
    cx, cy, r = W / 2, 34, 22
    steps = [("build", -90), ("ship", 0), ("learn", 90), ("repeat", 180)]
    import math
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 68" role="img" aria-label="A loop of four words, build, ship, learn, repeat, with the team of agents inside it.">',
           '<defs><marker id="la" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="#b0481a"/></marker></defs>']
    for i, (w, a) in enumerate(steps):
        a0, a1 = math.radians(a + 14), math.radians(a + 90 - 14)
        x0, y0, x1, y1 = cx + r * math.cos(a0), cy + r * math.sin(a0), cx + r * math.cos(a1), cy + r * math.sin(a1)
        out.append(f'<path d="M{x0:.2f} {y0:.2f} A{r} {r} 0 0 1 {x1:.2f} {y1:.2f}" fill="none" stroke="{ACCENT}" stroke-width=".9" marker-end="url(#la)"/>')
        lx, ly = cx + (r + 0.5) * math.cos(math.radians(a)), cy + (r + 0.5) * math.sin(math.radians(a))
        anchor = "middle" if a in (-90, 90) else ("start" if a == 0 else "end")
        dx = 3 if a == 0 else (-3 if a == 180 else 0)
        dy = -2.5 if a == -90 else (5 if a == 90 else 1.2)
        out.append(t(lx + dx, ly + dy, w, weight=800, anchor=anchor))
    out.append(robot(cx, cy - 10, 1.4, clock=True))
    for dx in (-9, 9):
        out.append(robot(cx + dx, cy - 6, 1.0))
    out.append(t(cx, cy + 10, "the team inside", anchor="middle", fill=MUTED))
    out.append("</svg>")
    return "".join(out)


def book_map():
    parts = ["The tour", "Start with one agent", "Grow the team", "The plumbing", "Making the talk, then containing it", "Your turn"]
    import textwrap
    x0, x1, y = 8.0, W - 8, 20.0
    step = (x1 - x0) / (len(parts) - 1)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 50" role="img" aria-label="The book as six stops on one line: the tour, start with one agent, grow the team, the plumbing, making the talk then containing it, your turn; you are here on the first.">',
           f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{INK}" stroke-width="1.2"/>']
    for i, p in enumerate(parts):
        x = x0 + i * step
        here = i == 0
        out.append(f'<circle cx="{x:.2f}" cy="{y}" r="{3.2 if here else 2.4}" fill="{ACCENT if here else "#fff"}" stroke="{ACCENT if here else INK}" stroke-width=".8"/>')
        out.append(t(x, y + 1.1, str(i + 1), size=F, weight=800, fill="#fff" if here else INK, anchor="middle"))
        for j, line in enumerate(textwrap.wrap(p, 11)):
            out.append(t(x, y + 8 + j * 4, line, weight=800 if here else 400, fill=ACCENT if here else INK, anchor="middle"))
    out.append(t(x0 - 3, 9, "you are here", weight=800, fill=ACCENT))
    out.append(f'<line x1="{x0}" y1="10.5" x2="{x0}" y2="{y - 3.6}" stroke="{ACCENT}" stroke-width=".6"/>')
    out.append("</svg>")
    return "".join(out)


if __name__ == "__main__":
    clone = sys.argv[1]
    (HERE / "cast-row.svg").write_text(sized(cast_row(clone)))
    svg, n = day_timeline(clone)
    (HERE / "day-timeline.svg").write_text(sized(svg))
    (HERE / "loop.svg").write_text(sized(loop()))
    (HERE / "book-map.svg").write_text(sized(book_map()))
    print(f"written four drawings; the timeline draws {n} wakes of 29 October (C087 counts 162)")
