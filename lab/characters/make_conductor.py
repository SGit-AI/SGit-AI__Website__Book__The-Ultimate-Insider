#!/usr/bin/env python3
"""The conductor's poses, drawn from one construction so every pose is the same character.

python3 lab/characters/make_conductor.py   (writes lab/characters/conductor-<pose>.svg)
The face is a clock: its hands are the expression. The baton is the one accent. Agents may be laughed at.
"""
from pathlib import Path

INK, FILL, FILL2, ACCENT = "#1f2933", "#eef2f6", "#d5dce4", "#b0481a"
HERE = Path(__file__).resolve().parent

POSES = {
    # name: (hour hand angle, minute hand angle, baton arm (x1,y1,x2,y2,x3,y3), other arm, extra, label)
    "calm":     (-60, 60, (84, 92, 100, 80, 112, 64), (36, 92, 24, 104), "", "pacing: hands at ten past ten"),
    "pointing": (0, 0, (84, 90, 104, 76, 118, 74), (36, 92, 26, 80), "", "on the minute: both hands at twelve"),
    "alarmed":  (180, 175, (84, 92, 96, 70, 102, 54), (36, 92, 22, 74),
                 f'<path d="M20 30 q-3 5 0 7 q3 -2 0 -7" fill="{FILL2}" stroke="{INK}" stroke-width="1.5"/>'
                 f'<path d="M98 26 l6 -6 M101 33 l8 -2 M94 20 l2 -8" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round"/>',
                 "the usage at ninety-five: hands at half past six"),
}


def hand(cx, cy, length, deg, colour, width):
    import math
    a = math.radians(deg - 90)
    return f'<line x1="{cx}" y1="{cy}" x2="{cx + length * math.cos(a):.1f}" y2="{cy + length * math.sin(a):.1f}" stroke="{colour}" stroke-width="{width}" stroke-linecap="round"/>'


def draw(pose):
    hh, mh, (b1x, b1y, b2x, b2y, b3x, b3y), (o1x, o1y, o2x, o2y), extra, label = POSES[pose]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 150" role="img" aria-label="The conductor, {label}">
  <line x1="60" y1="10" x2="60" y2="22" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
  <circle cx="60" cy="8" r="4" fill="{ACCENT}"/>
  <rect x="28" y="22" width="64" height="54" rx="12" fill="{FILL}" stroke="{INK}" stroke-width="3"/>
  <circle cx="60" cy="49" r="18" fill="#ffffff" stroke="{INK}" stroke-width="2.5"/>
  {''.join(f'<circle cx="{60 + 14 * __import__("math").cos(__import__("math").radians(a))}" cy="{49 + 14 * __import__("math").sin(__import__("math").radians(a))}" r="1" fill="{INK}"/>' for a in range(0, 360, 90))}
  {hand(60, 49, 9, hh, INK, 3)}{hand(60, 49, 13, mh, ACCENT, 2.5)}
  <rect x="36" y="82" width="48" height="40" rx="9" fill="{FILL2}" stroke="{INK}" stroke-width="3"/>
  <path d="M{b1x} {b1y} L{b2x} {b2y}" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
  <path d="M{b2x} {b2y} L{b3x} {b3y}" stroke="{ACCENT}" stroke-width="3" stroke-linecap="round"/>
  <path d="M{o1x} {o1y} L{o2x} {o2y}" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
  <path d="M48 122 L46 138 M72 122 L74 138" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
  <path d="M40 140 H52 M68 140 H80" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
  {extra}
</svg>
'''


if __name__ == "__main__":
    for p in POSES:
        (HERE / f"conductor-{p}.svg").write_text(draw(p))
    print("written: " + ", ".join(f"conductor-{p}.svg" for p in POSES))
