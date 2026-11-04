"""Chapter 15's first figure: the day's pre-reviews that said change, and the plans amended after them,
with hour eighteen's three marked (designer2, LAB 68).

Every number is read at build from the researcher's register (claims/register.json, the step-verdict claim's value
and note): the count, its split, and each change's member and time. Nothing typed here but the words.
Run: python3 make.py (writes pre-reviews-changed.svg)."""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[2]

INK, GREY, RULE, ACC, FILL = "#1f2933", "#5b6670", "#d5dce4", "#b0481a", "#eef2f6"
F = 'font-family="Inter, Helvetica, Arial, sans-serif"'
def t(x, y, s, size=3.18, w=400, fill=INK, a="start"):
    return f'<text x="{x:.2f}" y="{y:.2f}" {F} font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{a}">{s}</text>'

reg = json.loads((REPO / "claims" / "register.json").read_text())
claims = reg if isinstance(reg, list) else reg.get("claims", reg)
if isinstance(claims, dict):
    claims = [dict(id=k, **v) for k, v in claims.items()]
c = next(x for x in claims if isinstance(x, dict) and "pre_review_change_then_amended" in json.dumps(x.get("value", {})))
v = c["value"]["pre_review_change_then_amended"]
note = c["note"]
total, as_verdict, free = v["total"], v["with_a_verdict_field"], v["in_free_text_only"]
# each change, read from the note: "member HH:MM, HH:MM" groups, and the free-text times
changes = []
for member, times in re.findall(r"(conductor|researcher|studio) ((?:\d\d:\d\d(?:, )?)+)", note.split("4 more are")[0]):
    changes += [(member, tm, "verdict") for tm in re.findall(r"\d\d:\d\d", times)]
free_part = re.search(r"pre-review said change: adopted' \(([^)]*)\)", note).group(1)
changes += [("conductor", tm, "free text") for tm in re.findall(r"\d\d:\d\d", free_part)]
editor = re.search(r"conductor's (\d\d:\d\d) entry is the editor changing course", note).group(1)
assert len(changes) == total and sum(k == "verdict" for *_, k in changes) == as_verdict, changes
assert "No step said stop all day" in note

def mins(tm):
    h, m = map(int, tm.split(":")); return h * 60 + m
X0, X1, HOURS = 64.0, 158.0, 19
def X(m): return X0 + (X1 - X0) * m / (HOURS * 60)

W, H = 164, 50
o = [f'<rect x=".25" y=".25" width="{W - .5}" height="{H - .5}" rx="2.2" fill="#fff" stroke="{INK}" stroke-width=".45"/>']
# the count, left
o.append(t(5, 17, str(total), 12, 800))
o.append(t(5, 23.5, "pre-reviews said change;", 3.18, 700))
o.append(t(5, 27.7, "each plan was amended", 3.18, 700))
o.append(t(5, 32.9, f"{as_verdict} recorded as a verdict,", fill=GREY))
o.append(t(5, 37.1, f"{free} in the conductor\u2019s own words", fill=GREY))
o.append(t(5, 44.5, "no step said stop", 3.18, 700, ACC))
# hour eighteen lit
o.append(f'<rect x="{X(17*60):.2f}" y="6" width="{X(18*60) - X(17*60):.2f}" height="33" fill="{FILL}"/>')
o.append(t(X(18*60) + 1.2, 5.2, "hour eighteen", 3.18, 700, ACC, "end"))
# the clock of the day
o.append(f'<line x1="{X0}" y1="34" x2="{X1}" y2="34" stroke="{GREY}" stroke-width=".35"/>')
for h in range(HOURS + 1):
    o.append(f'<line x1="{X(h*60):.2f}" y1="34" x2="{X(h*60):.2f}" y2="{35.4 if h % 3 else 36.2}" stroke="{GREY}" stroke-width=".3"/>')
    if h % 3 == 0:
        o.append(t(X(h*60), 40, f"{h:02d}:00", fill=GREY, a="middle"))
# the marks: stacked when close; hour eighteen's in rust; the conductor's own-words ones as squares
used = []
for member, tm, kind in sorted(changes, key=lambda z: mins(z[1])):
    x = X(mins(tm)); lvl = sum(1 for ux in used if abs(ux - x) < 2.6); used.append(x)
    y = 29.5 - lvl * 4.6
    col = ACC if 17 * 60 <= mins(tm) < 18 * 60 else INK  # only the hour is marked; the members are not drawn
    if kind == "verdict":
        o.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="1.5" fill="{col}"/>')
    else:
        o.append(f'<rect x="{x - 1.4:.2f}" y="{y - 1.4:.2f}" width="2.8" height="2.8" fill="{col}"/>')
# the key: how each change was recorded
kx = X0
o.append(f'<circle cx="{kx + 1.2:.2f}" cy="44.4" r="1.3" fill="{INK}"/>')
o.append(t(kx + 3.6, 45.5, "recorded as a verdict", fill=GREY))
kx += 40
o.append(f'<rect x="{kx:.2f}" y="43.1" width="2.6" height="2.6" fill="{INK}"/>')
o.append(t(kx + 4.0, 45.5, "in the conductor\u2019s own words", fill=GREY))
# the editor's change of course, apart and not counted
ex = X(mins(editor))
o.append(f'<circle cx="{ex:.2f}" cy="16" r="1.4" fill="#fff" stroke="{GREY}" stroke-width=".45" stroke-dasharray=".8 .6"/>')
o.append(f'<line x1="{ex:.2f}" y1="17.4" x2="{ex:.2f}" y2="20.6" stroke="{GREY}" stroke-width=".25"/>')
o.append(t(ex - 2.4, 11.4, f"{editor}: I changed course,", fill=GREY, a="end"))
o.append(t(ex - 2.4, 15.4, "not a review, not counted", fill=GREY, a="end"))

label = (f"A card: {total} pre-reviews said change across the day and each plan was amended, {as_verdict} recorded as a verdict "
         f"and {free} in the conductor's own words; on the day's clock, hour eighteen's three marked; at {editor} the editor's "
         "own change of course, shown apart and not counted; no step said stop.")
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}" role="img" aria-label="{label}">'
       + "".join(o) + "</svg>\n")
(HERE / "pre-reviews-changed.svg").write_text(svg)
print(total, as_verdict, free, editor, [(m, tm) for m, tm, _ in changes])
