#!/usr/bin/env python3
"""LAB 47: the house as the talk team's structure (the conductor's 067; the editor, brief 2026-11-04 16: "I really like
this idea of having a house ... name the agents ... you can have multiple rooms"; the newsroom's proposal, 071, as a draft).

    python3 lab/experiments/47-designer-the-house/make_house.py <talk clone>

Each of the nine staffed agents is drawn once, in the room where its scope.writes at 298be4e lets it write (read here
from team/<m>/policy.json at 298be4e and checked against the ROOMS below; the build stops if a placement no longer holds).
The storyteller and the designer could write only their own folders, and their commits that day touched nothing else
(also checked), so they share a room by the talk, placed by what they worked on: that placement is my reading. Security
is the guard room's empty chair: proposed, never staffed (C011). Everyone writing its own records is drawn once, as the
ground the house stands on. Role names and paths only: no session id, key or prompt.
"""
import json, subprocess, sys
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'
F = 3.18
# room: (title, what the paths say, members, the path each member must hold for the placement, x, y, w, h)
ROOMS = [
    ("the talk", "the slides and talk.json", ["deck"], {"deck": "src/static/talk/slides/**"}, 4, 11, 84, 25),
    ("the story and the look", "own folders only: placed by their work", ["storyteller", "designer"], {}, 88, 11, 63, 25),
    ("the workshop", "the animations", ["motion", "ruv-sgit"], {"motion": "src/static/motion/**", "ruv-sgit": "src/static/ruv-sgit/**"}, 4, 36, 96, 25),
    ("the studio", "the ported pages", ["studio"], {"studio": "src/static/studio-ports/**"}, 100, 36, 51, 25),
    ("the evidence room", "evidence", ["researcher"], {"researcher": "evidence/**"}, 4, 61, 52, 25),
    ("the office", "the team's tools and notes", ["conductor"], {"conductor": "admin/tools/**"}, 56, 61, 56, 25),
    ("the guard room", "planned, never staffed", ["security"], {}, 112, 61, 39, 25),
    ("the foundations", "the build, the workflows, the engine", ["dev"], {"dev": "admin/build/**"}, 4, 86, 147, 16),
]


def git(clone, *a):
    return subprocess.run(["git", "-C", clone, *a], capture_output=True, text=True, check=True).stdout


def check(clone):
    placed = [m for r in ROOMS for m in r[2] if m != "security"]
    if sorted(placed) != sorted(mc.CAST):
        sys.exit("make_house: every staffed member must be drawn exactly once")
    for r in ROOMS:
        for m, need in r[3].items():
            writes = json.loads(git(clone, "show", f"298be4e:team/{m}/policy.json")).get("scope", {}).get("writes", [])
            if need not in writes:
                sys.exit(f"make_house: {m}'s scope.writes at 298be4e no longer holds {need}")
    for m in ("storyteller", "designer"):
        writes = json.loads(git(clone, "show", f"298be4e:team/{m}/policy.json")).get("scope", {}).get("writes", [])
        paths = {p for p in git(clone, "log", "298be4e", "--format=", "--name-only", f"--grep=^@{m}:").split() if p}
        if writes != [f"team/{m}/**"] or any(not p.startswith(f"team/{m}/") for p in paths):
            sys.exit(f"make_house: {m} wrote outside its own folder; place it by those paths")


def t(x, y, s, weight=400, fill=mc.INK, anchor="start", size=F):
    return (f'<text x="{x:.2f}" y="{y:.2f}" {SANS} font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}">{escape(s, quote=False)}</text>')


def chair(x, y, s):
    c = mc.MUTED
    return (f'<g transform="translate({x:.2f} {y:.2f}) scale({s})" fill="none" stroke="{c}" stroke-width="1" stroke-dasharray="1.6 1">'
            '<path d="M4 2 V18 M4 11 H14 V18 M4 2 H7"/></g>')


def house():
    out = []
    # the roof: a shallow gable over the top floor, the house's name under it
    out.append(mc.path("M2 11 L77.5 1 L153 11 Z", mc.FILL, mc.INK, .5))
    out.append(t(77.5, 9.4, "the talk's repository, as a house", 700, mc.INK, "middle"))
    for title, note, members, _, x, y, w, h in ROOMS:
        guard = title == "the guard room"
        fill = "#fff" if not guard else mc.FILL
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{mc.INK}" stroke-width=".5"'
                   + (' stroke-dasharray="2 1.2"' if guard else "") + "/>")
        out.append(t(x + 3, y + 5.2, title, 800) + t(x + 3, y + 9.4, note, 400, mc.MUTED))
        n = len(members)
        slot = (w - 6) / n
        for k, m in enumerate(members):
            cx = x + 3 + slot * k + slot / 2
            if m == "security":
                out.append(chair(cx - 4, y + 10.4, .5) + t(cx, y + h - 1.3, "security", 700, mc.MUTED, "middle"))
            else:
                s = .22
                out.append(f'<g transform="translate({cx - 20 * s:.2f} {y + 3:.2f}) scale({s})">{mc.figure(m)}</g>'
                           + t(cx + 8, y + 9.4, m, 700, mc.INK, "start") if title == "the foundations" else
                           f'<g transform="translate({cx - 20 * s:.2f} {y + 9.8:.2f}) scale({s})">{mc.figure(m)}</g>'
                           + t(cx, y + h - 1.3, m, 700, mc.INK, "middle"))
    # the ground: the record, drawn once
    out.append(f'<rect x="0" y="102" width="155" height="10" fill="{mc.INK}"/>'
               + t(77.5, 108.4, "the ground: every member writes its own records, team/<name>/, in one repository", 700, "#fff", "middle"))
    # no caption drawn in: one caption per figure, set by the publisher at the top (cast guide convention 8); the
    # source line it needs is in LAB 47's pages.html and the designer's letter
    return mc.svg(155, 112, "".join(out), "The talk's team as a house: the talk and the story at the top, the workshop and the studio, the evidence room, the office and an empty guard room, dev in the foundations, and every member's records as the ground")


if __name__ == "__main__":
    check(sys.argv[1])
    (HERE / "the-house.svg").write_text(house())
    print("written the-house.svg")
