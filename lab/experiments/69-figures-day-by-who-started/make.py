"""Chapter 15's third figure: the day by who started each session, the schedule's and mine, hours one to nineteen,
with part three's hours lit (designer2, LAB 69). In the construction of the designer's LAB 38 day by trigger
(read for the look, not changed).

Every number is read at build from claims/register.json: the by-hour split of wakes by trigger (C087) and, for the
hours that claim gives only as a range in words, the wakes opened in each clock hour (C110). The build stops unless the
two agree. Hour N is the margin clock's: (N-1):00 to (N-1):59 UTC on 29 October (C110's rule). Part three is hours six
to eighteen (chapter-plan/edition-150-outline.md, Part 3). Run: python3 make.py (writes day-by-who-started.svg)."""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402  read only: the cast's ink, grey, fill and accent

F = 'font-family="Inter, Helvetica, Arial, sans-serif"'
def t(x, y, s, size=3.18, w=400, fill=mc.INK, a="start"):
    return f'<text x="{x:.2f}" y="{y:.2f}" {F} font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{a}">{s}</text>'

reg = json.loads((REPO / "claims" / "register.json").read_text())
cl = reg if isinstance(reg, list) else reg.get("claims", reg)
if isinstance(cl, dict):
    cl = [dict(id=k, **v) for k, v in cl.items()]
R = {c["id"]: c for c in cl if isinstance(c, dict) and "id" in c}
v = R["C087"]["value"]
rows = R["C110"]["value"]["rows"]  # hour, span, ..., wakes opened that hour at index 6
woke = {r[0]: r[6] for r in rows}

split = {}  # hour (1-19) -> (scheduled, editor, follow-up)
for k, s in v["by_hour_UTC"].items():
    if "to" in k:
        lo, hi = map(int, re.findall(r"\d+", k))
        if "no editor" not in s:
            sys.exit("make: the range in words no longer says 'no editor'")
        for u in range(lo, hi + 1):
            n = woke[u + 1]
            if not 5 <= n <= 6:
                sys.exit(f"make: hour {u + 1} has {n} wakes, outside the range's '5 or 6'")
            split[u + 1] = (n, 0, 0)
        continue
    nums = [int(n) for n in re.findall(r"\d+", s)]
    follow = nums[-1] if "follow" in s else 0
    editor = nums[1] if len(nums) > 1 and "follow" not in s.split(",")[1] else 0
    split[int(k) + 1] = (nums[0], editor, follow)
for h in range(1, 20):
    split.setdefault(h, (0, 0, 0))
    if sum(split[h]) != woke[h]:
        sys.exit(f"make: hour {h}: the trigger split {split[h]} does not add up to the hour's wakes {woke[h]}")
tot = [sum(x[i] for x in split.values()) for i in range(3)]
if tot != [v["scheduled"], v["editor"], v["follow-up"]] or sum(tot) != v["wakes"]:
    sys.exit(f"make: totals {tot} do not match the register's")

W = 164
x0, step, bw, unit, base = 6.0, 8.2, 6.4, 1.45, 44.0
P3 = (6, 18)
o = []
# part three lit
lx0, lx1 = x0 + (P3[0] - 1) * step - .9, x0 + (P3[1] - 1) * step + bw + .9
o.append(f'<rect x="{lx0:.2f}" y="2" width="{lx1 - lx0:.2f}" height="{base + 6.6 - 2:.2f}" fill="{mc.FILL}"/>')
o.append(t(lx0 + 1.6, 6.2, "part three", 3.5, 800, mc.ACCENT))
o.append(f'<line x1="{x0 - 1}" y1="{base}" x2="{W - 1.5}" y2="{base}" stroke="{mc.INK}" stroke-width=".4"/>')
for h in range(1, 20):
    x = x0 + (h - 1) * step
    o.append(t(x + bw / 2, base + 4.6, str(h), 3.18, 700 if P3[0] <= h <= P3[1] else 400,
               mc.INK if P3[0] <= h <= P3[1] else mc.MUTED, "middle"))
    s, e, f = split[h]
    y = base
    for n, fill, stroke in ((s, mc.MUTED, "none"), (e, mc.ACCENT, "none"), (f, "#fff", mc.INK)):
        if n:
            y -= n * unit
            o.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{bw}" height="{n * unit:.2f}" fill="{fill}" stroke="{stroke}" stroke-width=".35"/>')
    if s + e + f:
        o.append(t(x + bw / 2, y - 1.2, str(s + e + f), 3.18, 700, a="middle"))
o.append(t(x0 - 1, base + 9.4, "hour", 3.18, 400, mc.MUTED))
key = [(mc.MUTED, "none", f"the schedule’s, {tot[0]}"), (mc.ACCENT, "none", f"mine, {tot[1]}"),
       ("#fff", mc.INK, f"follow-ups, {tot[2]}")]
kx = 24.0
for fill, stroke, words in key:
    o.append(f'<rect x="{kx:.2f}" y="{base + 6.9:.2f}" width="3" height="3" fill="{fill}" stroke="{stroke}" stroke-width=".35"/>')
    o.append(t(kx + 4.6, base + 9.4, words, 3.18, 400, mc.INK)); kx += 9 + len(words) * 1.7
o.append(t(W - 1.5, base + 9.4, f"{v['wakes']} sessions in all", 3.18, 700, mc.INK, "end"))
H = round(base + 12, 1)
label = (f"The day's {v['wakes']} sessions by who started them, hour by hour from hour one to hour nineteen: {tot[0]} by the "
         f"schedule, {tot[1]} by the editor, {tot[2]} follow-ups; part three, hours six to eighteen, lit.")
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}" role="img" aria-label="{label}">'
       + "".join(o) + "</svg>\n")
(HERE / "day-by-who-started.svg").write_text(svg)
print(tot, {h: split[h] for h in range(1, 20)})
