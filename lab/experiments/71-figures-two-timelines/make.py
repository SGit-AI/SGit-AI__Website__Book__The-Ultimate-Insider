"""Chapter 19's first figure: two timelines side by side, this book's and the Cold-Read team's, agreeing down their
whole length, with six places marked where the blind one saw more (designer2, LAB 71).

Positions only, from this repository's timeline/cold-read-comparison.md ("Where they agree" and the six it lists),
read here; no time and no count is printed, and none of the Cold-Read team's counts is used (the figure brief).
Nothing from here goes to the Cold-Read repository. The six are numbered as chapter 19 numbers them.
Run: python3 make.py (writes two-timelines.svg)."""
import pathlib
INK, GREY, RULE, ACC, FILL = "#1f2933", "#5b6670", "#d5dce4", "#b0481a", "#eef2f6"
F = 'font-family="Inter, Helvetica, Arial, sans-serif"'
def t(x, y, s, size=3.18, w=400, fill=INK, a="start", rot=None):
    tr = f' transform="rotate({rot} {x:.2f} {y:.2f})"' if rot is not None else ""
    return f'<text x="{x:.2f}" y="{y:.2f}" {F} font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{a}"{tr}>{s}</text>'
def hm(s):
    h, m = s.split(":")[:2]; return int(h) + int(m) / 60
X0, X1 = 8.0, 160.0
def X(s): return X0 + (X1 - X0) * hm(s) / 24
W, H = 164, 62
YB, YC = 26.0, 40.0  # this book's line, the Cold-Read line
o = []
# the moments both cite, from "Where they agree": a rung between the lines at each
agree = [("00:16", "the first commit"), ("14:07", "the briefs"), ("15:21", "the step limit"), ("16:59", "three parts"),
         ("18:44", "the hold"), ("23:19", "the last commit")]
o.append(f'<rect x="{X("17:16"):.2f}" y="{YB}" width="{X("17:48") - X("17:16"):.2f}" height="{YC - YB}" fill="{FILL}"/>')
for s, words in agree + [("17:48", "my run of chat")]:
    x = X(s)
    o.append(f'<line x1="{x:.2f}" y1="{YB}" x2="{x:.2f}" y2="{YC}" stroke="{GREY}" stroke-width=".35"/>')
    if words == "the last commit":
        o.append(t(x - 1.2, YB + 4.6, words, 3.18, 400, GREY, "end"))
    else:
        o.append(t(x + .8, YB - 2.0, words, 3.18, 400, GREY, "start", -45))
# the two lines
for y, name in ((YB, "this book’s timeline"), (YC, "the Cold-Read team’s")):
    o.append(f'<line x1="{X("00:16"):.2f}" y1="{y}" x2="{X("23:19"):.2f}" y2="{y}" stroke="{INK}" stroke-width=".8"/>')
    o.append(f'<circle cx="{X("00:16"):.2f}" cy="{y}" r=".9" fill="{INK}"/><circle cx="{X("23:19"):.2f}" cy="{y}" r=".9" fill="{INK}"/>')
o.append(t(X("00:16") + 1.5, YB + 4.6, "this book’s timeline", 3.18, 700))
o.append(t(X("00:16") + 1.5, YC - 2.0, "the Cold-Read team’s", 3.18, 700))
o.append(t(X("08:30"), (YB + YC) / 2 + 1.1, "agree to the second", 3.18, 700, GREY, "middle"))
# the six, where the blind one saw more, on its own line, numbered as chapter 19 numbers them
six = {5: "02:07", 4: "17:08", 2: "18:20", 3: "18:45", 6: "19:00"}
slot = {5: X("02:07"), 1: 100.0, 4: 110.0, 2: 120.0, 3: 130.0, 6: 140.0}
YM = 51.0
# 1: the unnamed commits, a span: the comparison applies it in day files 16 to 18, the clock hours 16:00 to 18:59
a, b = X("16:00"), X("18:59")
o.append(f'<path d="M{a:.2f} {YC + 1.6} V{YC + 3.2} H{b:.2f} V{YC + 1.6}" fill="none" stroke="{ACC}" stroke-width=".45"/>')
o.append(f'<line x1="{(a + b) / 2:.2f}" y1="{YC + 3.2}" x2="{slot[1]:.2f}" y2="{YM - 2.3}" stroke="{ACC}" stroke-width=".3"/>')
for n, s in six.items():
    x = X(s)
    o.append(f'<circle cx="{x:.2f}" cy="{YC}" r=".9" fill="{ACC}"/>')
    o.append(f'<line x1="{x:.2f}" y1="{YC + .9}" x2="{slot[n]:.2f}" y2="{YM - 2.3}" stroke="{ACC}" stroke-width=".3"/>')
for n, x in slot.items():
    o.append(f'<circle cx="{x:.2f}" cy="{YM}" r="2.3" fill="{ACC}"/>')
    o.append(t(x, YM + 1.15, str(n), 3.18, 800, "#fff", "middle"))
o.append(t(95.5, YM - 0.9, "where the blind one saw more,", 3.18, 400, ACC, "end"))
o.append(t(95.5, YM + 3.3, "numbered as in this chapter", 3.18, 400, ACC, "end"))
# the clock, by hour only
o.append(f'<line x1="{X0}" y1="{H - 4.5}" x2="{X1}" y2="{H - 4.5}" stroke="{RULE}" stroke-width=".3"/>')
for h in range(0, 25, 3):
    x = X0 + (X1 - X0) * h / 24
    o.append(f'<line x1="{x:.2f}" y1="{H - 5.3}" x2="{x:.2f}" y2="{H - 3.7}" stroke="{GREY}" stroke-width=".3"/>')
o.append(t(X1, H - 0.6, "the day of 29 October, by the hour", 3.18, 400, GREY, "end"))
label = ("Two timelines of the day side by side, this book's and the Cold-Read team's, joined where both cite the same "
         "moments, from the first commit to the last; on the Cold-Read line, six places numbered where it saw more.")
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}" role="img" aria-label="{label}">'
       + "".join(o) + "</svg>\n")
pathlib.Path(__file__).with_name("two-timelines.svg").write_text(svg)
