"""Chapter 19's second figure: a card, the six, each with the chapter of this book where it now stands (designer2, LAB 72).

Each row: the number and heading as chapter 19 gives them (read from the chapter at build: the build stops if a heading
changes), where the book tells it (checked by hand against manuscript/rc2/150/ on 5 November: items 4 and 5 are told in
chapter 19 only, so the card says "this chapter"), and the timeline day file where this book applied it, from the
comparison's "Applied" line (the figure brief). No number but the six's own and chapter numbers.
Run: python3 make.py (writes the-six.svg)."""
import pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[2]
CH = (REPO / "manuscript" / "rc2" / "150" / "19-a-second-team-reading-cold.md").read_text()
heads = dict((int(n), h) for n, h in re.findall(r"^### (\d)\. (.+)$", CH, re.M))
INK, GREY, RULE, ACC, FILL = "#1f2933", "#5b6670", "#d5dce4", "#b0481a", "#eef2f6"
F = 'font-family="Inter, Helvetica, Arial, sans-serif"'
def t(x, y, s, size=3.18, w=400, fill=INK, a="start"):
    return f'<text x="{x:.2f}" y="{y:.2f}" {F} font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{a}">{s}</text>'
rows = [  # n, where the book tells it, where the timeline applied it
    (1, "chapter 17", "hours seventeen to nineteen"),
    (2, "chapter 16", "hour nineteen"),
    (3, "chapter 17", "hour nineteen"),
    (4, "this chapter", "hour eighteen"),
    (5, "this chapter", "hour three"),
    (6, "chapter 1", "after the day"),
]
for n, *_ in rows:
    if n not in heads:
        sys.exit(f"make: chapter 19 has no heading {n}")
W, RH, TOP = 164, 7.4, 11.0
H = TOP + RH * len(rows) + 3
o = [f'<rect x=".25" y=".25" width="{W - .5}" height="{H - .5:.2f}" rx="2.2" fill="#fff" stroke="{INK}" stroke-width=".45"/>']
o.append(t(16, 7.2, "what the blind team saw first", 3.18, 700, GREY))
o.append(t(93, 7.2, "in this book", 3.18, 700, GREY))
o.append(t(115, 7.2, "in its timeline", 3.18, 700, GREY))
for i, (n, book, tl) in enumerate(rows):
    y = TOP + i * RH
    if i:
        o.append(f'<line x1="4" y1="{y:.2f}" x2="{W - 4}" y2="{y:.2f}" stroke="{RULE}" stroke-width=".3"/>')
    cy = y + RH / 2
    o.append(f'<circle cx="9" cy="{cy:.2f}" r="2.3" fill="{ACC}"/>')
    o.append(t(9, cy + 1.15, str(n), 3.18, 800, "#fff", "middle"))
    o.append(t(16, cy + 1.15, heads[n], 3.18, 700))
    o.append(t(93, cy + 1.15, book, 3.18, 700 if book != "this chapter" else 400, INK if book != "this chapter" else GREY))
    o.append(t(115, cy + 1.15, tl, 3.18, 400, GREY))
label = "A card of the six things the blind team saw first, each with where this book now tells it and where its timeline applied it."
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H:.1f}mm" viewBox="0 0 {W} {H:.1f}" role="img" aria-label="{label}">'
       + "".join(o) + "</svg>\n")
(HERE / "the-six.svg").write_text(svg)
print({n: heads[n] for n in heads})
