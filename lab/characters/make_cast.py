#!/usr/bin/env python3
"""The cast as personas (CH1 and NR1, signed 1 November 2026): the talk's nine agents, one construction, four moods.

    python3 lab/characters/make_cast.py   (writes lab/characters/cast/<member>-<mood>.svg and on-stage-<n>.svg)
Every member is the same small robot as the cast row (LAB 22) and the conductor (LAB 11), told apart by one colour,
one thing on the head and one thing in the hand, each from the member's job on the day: a little stereotypical, like
an icon. The face carries the mood; the conductor's face is its clock, so its hands carry it. One SVG unit is a
millimetre; each file states its size, so no build scales it up. No text inside a figure. The editor is not drawn:
he is drawn only as himself and only at his word. A mood is the book's reading, never a claim of the record.
"""
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
INK, MUTED, FILL, FILL2, ACCENT, PAPER = "#1f2933", "#5b6670", "#eef2f6", "#d5dce4", "#b0481a", "#ffffff"
SW = 0.7  # stroke width at scale 1

# member: (colour, the look in a few words, the job it comes from). Order: the cast row's.
CAST = {
    "conductor":   (ACCENT,    "a clock for a face, a baton",          "kept the time and the plan; stopped everything at the end"),
    "storyteller": ("#7a4f9a", "wavy hair, a long scarf, an open book", "the story"),
    "researcher":  ("#2f6f8f", "round glasses, a lab coat, a magnifier", "the facts"),
    "deck":        ("#b07d12", "a bow tie, a slide on a stick",         "what the talk says"),
    "dev":         ("#3d7a3d", "a hard hat, a spanner",                 "build and release"),
    "designer":    ("#c2416b", "a beret, a pencil",                     "how it looks"),
    "motion":      ("#23807f", "a cap on backwards, a clapperboard",    "story animations"),
    "ruv-sgit":    ("#4a56a6", "a headband, a stopwatch",               "animations in runs"),
    "studio":      ("#8a5a2b", "big headphones, a plug on a cable",     "ports"),
}
MOODS = ("happy", "worried", "stressed", "unhappy")
FIG_W, FIG_H = 40.0, 50.0  # a figure's box at scale 1


def line(x1, y1, x2, y2, c=INK, w=SW):
    return f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>'


def path(d, fill="none", c=INK, w=SW):
    return f'<path d="{d}" fill="{fill}" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'


def face(mood):
    """Eyes, brows and mouth on the head's screen, centred on (20, 18)."""
    if mood == "happy":
        eyes = f'<circle cx="17" cy="18" r=".9" fill="{INK}"/><circle cx="23" cy="18" r=".9" fill="{INK}"/>'
        return eyes + path("M17.4 21.3 Q20 23.9 22.6 21.3")
    if mood == "worried":
        eyes = f'<circle cx="17" cy="18.3" r=".9" fill="{INK}"/><circle cx="23" cy="18.3" r=".9" fill="{INK}"/>'
        return eyes + path("M15.6 16.2 L18.2 15.2") + path("M24.4 16.2 L21.8 15.2") + path("M17.4 22.2 q1.3 -1 2.6 0 t2.6 0")
    if mood == "stressed":
        eyes = "".join(f'<circle cx="{x}" cy="18.2" r="1.35" fill="{PAPER}" stroke="{INK}" stroke-width=".45"/>'
                       f'<circle cx="{x}" cy="18.2" r=".5" fill="{INK}"/>' for x in (17, 23))
        return (eyes + path("M15.6 15.2 L18.3 16.1") + path("M24.4 15.2 L21.7 16.1")
                + path("M16.8 22.3 l1.1 -.8 l1.1 .8 l1.1 -.8 l1.1 .8 l1.1 -.8"))
    return path("M16.1 18.4 h1.8") + path("M22.1 18.4 h1.8") + path("M17.4 22.7 Q20 20.6 22.6 22.7")


def hand(cx, cy, length, deg, colour, width):
    a = math.radians(deg - 90)
    return line(cx, cy, cx + length * math.cos(a), cy + length * math.sin(a), colour, width)


CLOCK = {"happy": (-60, 60), "worried": (240, 120), "stressed": (180, 175), "unhappy": (210, 150)}


def clock_face(mood):
    """The conductor's: hands at ten past ten when all is well, at half past six at the usage's ninety-five."""
    h, m = CLOCK[mood]
    ticks = "".join(f'<circle cx="{20 + 4.9 * math.cos(math.radians(a)):.2f}" cy="{18 + 4.9 * math.sin(math.radians(a)):.2f}" r=".35" fill="{INK}"/>'
                    for a in range(0, 360, 90))
    return (f'<circle cx="20" cy="18" r="6" fill="{PAPER}" stroke="{INK}" stroke-width=".6"/>' + ticks
            + hand(20, 18, 3.2, h, INK, .9) + hand(20, 18, 4.6, m, ACCENT, .7))


def headgear(member, col):
    return {
        "conductor": line(20, 10, 20, 6.4) + f'<circle cx="20" cy="5.2" r="1.6" fill="{ACCENT}"/>',
        "storyteller": path("M10.6 11.6 q2.4 -4.4 4.8 -.6 q2.4 -4.2 4.8 -.4 q2.4 -4.2 4.8 -.4 q2.2 -3.4 4.4 .8", col, INK, .5),
        "researcher": "",
        "deck": "",
        "dev": path("M11.2 11.4 a8.8 6.4 0 0 1 17.6 0 z", col, INK, .5) + line(8.6, 11.4, 31.4, 11.4, INK, 1.1),
        "designer": f'<ellipse cx="18.6" cy="9.9" rx="8.6" ry="2.7" fill="{col}" stroke="{INK}" stroke-width=".5"/>' + line(18.6, 7.2, 18.9, 5.9, INK, .9),
        "motion": path("M11.4 11.2 a8.6 5.6 0 0 1 17.2 0 z", col, INK, .5) + path("M11.6 11.2 h-4.6 q-.6 -1.4 .8 -1.4 h3.8", col, INK, .5),
        "ruv-sgit": f'<rect x="9.6" y="12.2" width="20.8" height="1.9" fill="{col}" stroke="{INK}" stroke-width=".4"/>' + path("M30.4 13.2 l2.4 -1.6 M30.4 13.4 l2.6 .8", "none", col, .7),
        "studio": path("M9.4 16.4 Q9.4 5.6 20 5.6 Q30.6 5.6 30.6 16.4", "none", INK, .9)
                  + f'<rect x="7.2" y="14.2" width="3.2" height="6.6" rx="1.2" fill="{col}" stroke="{INK}" stroke-width=".5"/>'
                  + f'<rect x="29.6" y="14.2" width="3.2" height="6.6" rx="1.2" fill="{col}" stroke="{INK}" stroke-width=".5"/>',
    }[member]


def over_face(member, col):
    """What sits on the face, over the mood: the researcher's glasses."""
    if member == "researcher":
        return ("".join(f'<circle cx="{x}" cy="18.2" r="2.3" fill="none" stroke="{INK}" stroke-width=".55"/>' for x in (17, 23))
                + line(19.3, 18.0, 20.7, 18.0, INK, .5))
    return ""


def neckwear(member, col):
    if member == "storyteller":
        return (f'<rect x="12.4" y="26.4" width="15.2" height="2.6" rx="1.2" fill="{col}" stroke="{INK}" stroke-width=".45"/>'
                f'<rect x="23.4" y="28" width="2.8" height="8.6" rx="1" fill="{col}" stroke="{INK}" stroke-width=".45"/>')
    if member == "deck":
        return path("M20 28.4 l-3.2 -1.8 v3.6 z M20 28.4 l3.2 -1.8 v3.6 z", col, INK, .45)
    return ""


def body(member, col):
    if member == "researcher":  # a white lab coat, its lapels in the member's colour
        return (f'<rect x="12" y="28" width="16" height="14" rx="3" fill="{PAPER}" stroke="{INK}" stroke-width="{SW}"/>'
                + path("M16.4 28.2 L20 33.6 L23.6 28.2", col, INK, .45) + line(20, 33.6, 20, 41.6, INK, .45))
    return f'<rect x="12" y="28" width="16" height="14" rx="3" fill="{col}" stroke="{INK}" stroke-width="{SW}"/>'


def prop(member, col):
    """In the right hand (about 32, 34); the storyteller's book in the left."""
    return {
        "conductor": line(32, 34, 36.2, 27.4) + line(36.2, 27.4, 38.6, 23.6, ACCENT, .9),
        "storyteller": path("M2.6 33.6 l3.6 -1.2 l3.6 1.2 v4.6 l-3.6 -1.2 l-3.6 1.2 z", PAPER, INK, .5) + line(6.2, 32.4, 6.2, 37, INK, .4),
        "researcher": line(32, 34, 34.4, 30.8, INK, 1) + f'<circle cx="35.9" cy="28.6" r="2.7" fill="{FILL}" stroke="{INK}" stroke-width=".7"/>',
        "deck": line(32, 34, 34.4, 26.6, INK, .6) + f'<rect x="30.4" y="19.8" width="8.6" height="6.8" rx=".6" fill="{PAPER}" stroke="{INK}" stroke-width=".55"/>'
                + f'<rect x="31.6" y="21.2" width="5.4" height="1.2" fill="{col}"/>' + line(31.6, 23.6, 37.6, 23.6, MUTED, .5) + line(31.6, 25, 36, 25, MUTED, .5),
        "dev": line(32, 34, 36.6, 28.2, INK, 1.1) + path("M35.4 27.2 a1.9 1.9 0 1 1 2.6 2.2 l-.9 -.9 l.8 -.8 z", FILL2, INK, .5),
        "designer": f'<g transform="rotate(-38 32 34)"><rect x="31.2" y="24.6" width="1.8" height="9.4" fill="{col}" stroke="{INK}" stroke-width=".4"/>'
                    + path("M31.2 24.6 L32.1 22.4 L33 24.6 z", "#e8c9a0", INK, .4) + "</g>",
        "motion": f'<rect x="31.4" y="29.4" width="7.8" height="5.4" rx=".4" fill="{INK}"/>'
                  + f'<g transform="rotate(-16 31.4 29.4)"><rect x="31.4" y="27.4" width="7.8" height="1.8" fill="{PAPER}" stroke="{INK}" stroke-width=".4"/>'
                  + line(33.4, 27.4, 32.6, 29.2, INK, .5) + line(35.6, 27.4, 34.8, 29.2, INK, .5) + line(37.8, 27.4, 37, 29.2, INK, .5) + "</g>",
        "ruv-sgit": f'<circle cx="35.4" cy="31.4" r="2.9" fill="{PAPER}" stroke="{INK}" stroke-width=".6"/>'
                    + f'<rect x="34.8" y="27.4" width="1.2" height="1.1" fill="{INK}"/>' + line(35.4, 31.4, 36.6, 29.9, col, .6),
        "studio": path("M32 34 q4 4 6.4 1 q2 -2.6 -.6 -4.6", "none", INK, .5)
                  + f'<rect x="36" y="28.2" width="3.2" height="2.6" rx=".5" fill="{col}" stroke="{INK}" stroke-width=".4"/>'
                  + line(36.8, 28.2, 36.8, 26.8, INK, .4) + line(38.4, 28.2, 38.4, 26.8, INK, .4),
    }[member]


def figure(member, mood="happy"):
    """One member at scale 1 in a 40 x 50 box, as SVG elements (no root)."""
    col = CAST[member][0]
    screen = clock_face(mood) if member == "conductor" else face(mood)
    sweat = path("M30.6 9.6 q-1.5 2.2 0 3 q1.5 -.8 0 -3", "#bcd3e6", INK, .4) if mood == "stressed" else ""
    return "".join([
        line(12, 31, 7, 36.6), line(28, 31, 32, 34),  # arms
        line(16, 42, 15.4, 47.4), line(24, 42, 24.6, 47.4), line(13.6, 47.8, 17, 47.8), line(23, 47.8, 26.4, 47.8),  # legs
        body(member, col), neckwear(member, col),
        f'<rect x="10" y="10" width="20" height="16" rx="3.2" fill="{FILL}" stroke="{INK}" stroke-width="{SW}"/>',
        screen, over_face(member, col), headgear(member, col), prop(member, col), sweat,
    ])


def head(member, lit=True):
    """The head alone (the screen, the headgear), for the on-stage marker: a 40 x 27 box at scale 1."""
    col = CAST[member][0] if lit else FILL2
    g = (f'<rect x="10" y="10" width="20" height="16" rx="3.2" fill="{FILL if lit else PAPER}" stroke="{INK if lit else FILL2}" stroke-width="{SW * 1.6}"/>'
         + (clock_face("happy") if member == "conductor" and lit else (face("happy") if lit else ""))
         + (headgear(member, col) if member != "conductor" else line(20, 10, 20, 6.4, INK if lit else FILL2, 1.2)
            + f'<circle cx="20" cy="5.2" r="1.6" fill="{ACCENT if lit else FILL2}"/>'))
    if not lit:  # the absent: an outline, nothing on the face
        g = g.replace(f'stroke="{INK}"', f'stroke="{FILL2}"')
    return g


def svg(w, h, body_, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:g}mm" height="{h:g}mm" viewBox="0 0 {w:g} {h:g}" '
            f'role="img" aria-label="{label}">{body_}</svg>\n')


def on_stage(present, size=7.0):
    """The 'on stage now' marker: the nine heads in the cast's order, the present ones lit. size = a head's width (mm)."""
    s = size / 20.0  # the head is 20 units wide in its 40-unit box
    step = size * 1.25
    out = []
    for i, m in enumerate(CAST):
        x = i * step - 10 * s
        out.append(f'<g transform="translate({x:.2f} {-4 * s:.2f}) scale({s:.4f})">{head(m, m in present)}</g>')
    return svg(round(len(CAST) * step - size * 0.25, 2), round(23 * s, 2), "".join(out),
               "On stage now: " + (", ".join(m for m in CAST if m in present) or "no agent yet"))


if __name__ == "__main__":
    out = HERE / "cast"
    out.mkdir(exist_ok=True)
    for m, (col, look, job) in CAST.items():
        for mood in MOODS:
            (out / f"{m}-{mood}.svg").write_text(svg(20, 25, f'<g transform="scale(.5)">{figure(m, mood)}</g>',
                                                     f"The {m}, {mood} (the book's reading): {look}"))
    print(f"written {len(CAST) * len(MOODS)} figures in lab/characters/cast/")
