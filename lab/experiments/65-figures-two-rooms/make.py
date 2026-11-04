"""Chapter 19's last figure: the two teams as two rooms (designer2, LAB 65).
Run: python3 make.py   (writes two-rooms.svg beside this file; no input, no number)."""
import pathlib, sys
REPO = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402  read only: the cast's heads, for this book's room (designer__150)
INK, GREY, RULE, ACC, FILL = "#1f2933", "#5b6670", "#d5dce4", "#b0481a", "#eef2f6"
F = 'font-family="Inter, Helvetica, Arial, sans-serif"'
def t(x, y, s, size=3.18, w=400, fill=INK, a="middle"):
    return f'<text x="{x:.2f}" y="{y:.2f}" {F} font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{a}">{s}</text>'
o = []
W, H = 164, 74
# the record, at the top, read by both
o.append(f'<rect x="57" y="2" width="50" height="15" rx="1.5" fill="{FILL}" stroke="{INK}" stroke-width=".7"/>')
o.append(t(82, 8.6, "the record", 4.2, 800))
o.append(t(82, 13.6, "the talk\'s repository, read only", fill=GREY))
# two rooms
def room(x, title, sub, people, colour, w=800):
    o.append(f'<rect x="{x}" y="34" width="56" height="36" rx="1" fill="#fff" stroke="{colour}" stroke-width=".5"/>')
    o.append(t(x + 28, 41, title, 4.2, w, colour))
    o.append(t(x + 28, 46, sub, fill=GREY))
    for i, (px, py) in enumerate(people):
        o.append(f'<circle cx="{x+px}" cy="{py}" r="1.6" fill="{colour}"/>')
        o.append(f'<path d="M{x+px-2.6} {py+5.4} A2.6 2.6 0 0 1 {x+px+2.6} {py+5.4} Z" fill="{colour}"/>')
pts = [(12, 54), (22, 54), (32, 54), (42, 54), (17, 62), (27, 62), (37, 62)]
room(6, "this book\'s room", "its briefs, its timeline, its team", [], INK)
# this book's room reads as this team: the cast's heads of BOOK_TEAM (designer__150); the other room stays generic,
# since nothing about that team crosses the valve
for i, m in enumerate(mc.BOOK_TEAM):
    hx, hy = (9.5 + i * 17.0, 47.5) if i < 3 else (18 + (i - 3) * 17.0, 58.0)
    o.append(f'<g transform="translate({6 + hx - 3:.2f} {hy:.2f}) scale(.36)">{mc.head(m)}</g>')
room(102, "the Cold-Read room", "the record, and nothing else", pts, GREY)
o.append(f'<defs><marker id="a" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="{INK}"/></marker>'
         f'<marker id="h" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="{ACC}"/></marker></defs>')
# one arrow from the record into each room
o.append(f'<path d="M70 17 C 60 24, 40 26, 34 33" fill="none" stroke="{INK}" stroke-width=".8" marker-end="url(#a)"/>')
o.append(f'<path d="M94 17 C 104 24, 124 26, 130 33" fill="none" stroke="{INK}" stroke-width=".8" marker-end="url(#a)"/>')
o.append(t(44, 23, "read", fill=GREY, a="end"))
o.append(t(120, 23, "read", fill=GREY, a="start"))
# the hand-off, once, this room to the other
o.append(f'<path d="M62 45 H101" stroke="{ACC}" stroke-width="1.2" marker-end="url(#h)"/>')
o.append(t(82, 41.6, "the hand-off", 3.5, 800, ACC))
o.append(t(82, 50.4, "drawn once", fill=ACC))
# and nothing back: the way back drawn and shut
o.append(f'<path d="M101 60 H63" stroke="{GREY}" stroke-width=".6" stroke-dasharray="1.6 1.2"/>')
o.append(f'<path d="M79.5 57 L84.5 63 M84.5 57 L79.5 63" stroke="{ACC}" stroke-width=".9"/>')
o.append(t(82, 67.6, "never again, either way", fill=GREY))
label = ("The two teams as two rooms: the talk's record above, read by each; one arrow, the hand-off, "
         "from this book's room to the Cold-Read room, drawn once; the way back shut.")
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}" role="img" aria-label="{label}">'
       + "".join(o) + "</svg>\n")
pathlib.Path(__file__).with_name("two-rooms.svg").write_text(svg)
