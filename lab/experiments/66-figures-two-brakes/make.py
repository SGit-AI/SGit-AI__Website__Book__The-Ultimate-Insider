"""Chapter 18's third figure: the two brakes on the value chain (designer2, LAB 66).
The chain is placed as ruv-sgit's map of it (LAB 61, map.svg: the same nodes at the same
positions, read from that file, not copied); on it, the hold marked as the brake anyone pulls
and the editor releases, and the checking agent's reads as a ring inside every piece of work. Run: python3 make.py (writes two-brakes.svg; no number in it)."""
import pathlib
INK, GREY, RULE, ACC, READ = "#1f2933", "#5b6670", "#d5dce4", "#b0481a", "#23807f"
F = 'font-family="Inter, Helvetica, Arial, sans-serif"'
def t(x, y, s, size=3.18, w=400, fill=INK, a="start"):
    return f'<text x="{x:.2f}" y="{y:.2f}" {F} font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{a}">{s}</text>'
W, H = 164, 100
o = []
# the axis, as LAB 61 draws it
for x, name in [(32.5, "new"), (69.5, "custom built"), (106.5, "product"), (143.5, "ordinary")]:
    o.append(t(x, 97.6, name, fill=GREY, a="middle"))
for x in (51, 88, 125):
    o.append(f'<line x1="{x}" y1="4" x2="{x}" y2="91" stroke="{RULE}" stroke-width=".3" stroke-dasharray="1 1"/>')
o.append(f'<line x1="14" y1="92" x2="162" y2="92" stroke="{GREY}" stroke-width=".35"/>')
o.append(f'<path d="M160.4 91 L162 92 L160.4 93" fill="none" stroke="{GREY}" stroke-width=".35"/>')
o.append(t(1, 8, "seen", fill=GREY)); o.append(t(1, 88, "unseen", fill=GREY))
N = {  # name: (x, y, label side)
    "editor": (27.32, 6.00), "talk": (24.36, 19.94), "slides": (36.20, 37.16), "site": (67.28, 37.16),
    "player": (73.20, 47.00), "agents": (49.52, 60.12), "hold": (25.84, 83.90), "brief": (111.68, 83.90),
    "check": (126.48, 76.52), "build": (135.36, 83.90), "tool": (117.60, 71.60)}
for a, b in [("editor", "talk"), ("talk", "slides"), ("talk", "site"), ("talk", "player"), ("slides", "agents"),
             ("site", "agents"), ("player", "agents"), ("agents", "tool"), ("agents", "build"), ("agents", "check"),
             ("agents", "brief"), ("agents", "hold")]:
    (x1, y1), (x2, y2) = N[a], N[b]
    o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{GREY}" stroke-width=".3"/>')
# brake two: the checking agent's reads, a ring inside every piece of work (a thread along the chain was tried and read as a second chain: dropped)
order = ["talk", "slides", "agents", "site", "player", "tool", "check", "build", "brief"]
for k in order:
    x, y = N[k]
    o.append(f'<circle cx="{x}" cy="{y}" r="2.7" fill="none" stroke="{READ}" stroke-width=".55"/>')
# the nodes and their words, as LAB 61 has them
o.append(f'<circle cx="{N["editor"][0]}" cy="{N["editor"][1]}" r="1.6" fill="{INK}"/>')
for k in order:
    x, y = N[k]
    o.append(f'<circle cx="{x}" cy="{y}" r="1.3" fill="#fff" stroke="{INK}" stroke-width=".4"/>')
L = [("editor", 3, 1.1, "the editor", 700, "start"), ("talk", 3.6, -2.2, "a talk the room understands", 700, "start"),
     ("slides", -3.6, 1.1, "the slides", 400, "end"), ("site", 3.6, 1.1, "the site", 400, "start"),
     ("player", 3.6, 1.1, "the player", 400, "start"), ("agents", -3.6, 1.1, "the agents", 400, "end"),
     ("tool", 3.6, 1.1, "the agent tool", 400, "start"), ("check", 3.6, 1.1, "the check", 400, "start"),
     ("build", 3.6, 1.1, "the build", 400, "start"), ("brief", -3.6, 1.1, "the brief", 400, "end")]
for k, dx, dy, s, w, a in L:
    o.append(t(N[k][0] + dx, N[k][1] + dy, s, w=w, a=a))
# brake one: the hold, at the new end
hx, hy = N["hold"]
o.append(f'<circle cx="{hx}" cy="{hy}" r="3.4" fill="#fff" stroke="{ACC}" stroke-width="1.1"/>')
o.append(f'<circle cx="{hx}" cy="{hy}" r="1.6" fill="{ACC}"/>')
o.append(t(hx + 5, hy - 2.4, "the hold", 3.5, 800, ACC))
o.append(t(hx + 5, hy + 1.8, "anyone stops,", fill=ACC))
o.append(t(hx + 5, hy + 5.6, "the editor restarts", fill=ACC))
# the key to the two brakes, top right, in the free space
kx, ky = 104, 10
o.append(f'<circle cx="{kx}" cy="{ky}" r="1.6" fill="{ACC}"/><circle cx="{kx}" cy="{ky}" r="3.0" fill="none" stroke="{ACC}" stroke-width="1"/>')
o.append(t(kx + 5, ky + 1.1, "brake one: the hold", 3.18, 700, ACC))
o.append(f'<circle cx="{kx}" cy="{ky+9}" r="2.7" fill="none" stroke="{READ}" stroke-width=".55"/>')
o.append(t(kx + 5, ky + 10.1, "brake two: the checking", 3.18, 700, READ))
o.append(t(kx + 5, ky + 14.3, "agent’s reads, inside every", 3.18, 700, READ))
o.append(t(kx + 5, ky + 18.5, "piece of work", 3.18, 700, READ))
label = ("The two brakes on the value chain, drawn on the factory's map: the hold at the new end, which anyone may pull "
         "and only the editor releases; and the checking agent's reads, a ring inside every piece of work.")
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}" role="img" aria-label="{label}">'
       + "".join(o) + "</svg>\n")
pathlib.Path(__file__).with_name("two-brakes.svg").write_text(svg)
