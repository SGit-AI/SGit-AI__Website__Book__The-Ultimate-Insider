"""LAB 82: the pages of agents saying hi (RPP1, the editor, 14 November 2026). When a part page would fall on a left
page, the build sets one of these before it, so the part opens on the right. 156 by 200 mm, like the part pages.
The figures are the cover's own (src/static/assets/cover-a.svg), the words each agent's hello from 00-start-here."""
import os, re, sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)
NAMES = ["dev", "conductor", "deck", "ruv-sgit", "researcher", "designer"]
COLOURS = {"dev": "#3d7a3d", "conductor": "#b0481a", "deck": "#b07d12", "ruv-sgit": "#4a56a6",
           "researcher": "#2f6f8f", "designer": "#c2416b"}
# (agents, lines): the hellos in 00-start-here.md, as the team says them there
PAGES = {
    1: [("conductor", "Hi. I keep the time and the plan."), ("dev", "Hi. I build it.")],
    2: [("deck", "Hi! Next, the team arrives.")],
    3: [("ruv-sgit", "Hi from the night shift."), ("researcher", "Hi. I check every fact.")],
    4: [("designer", "Hi. Nearly at the end of the day.")],
    5: [("conductor", "Hi again."), ("dev", "Now it is your turn.")],
}


def figures():
    tree = ET.parse(os.path.join(ROOT, "src", "static", "assets", "cover-a.svg"))
    found = [g for g in tree.getroot().iter(f"{{{NS}}}g") if "scale(.45)" in g.get("transform", "")]
    if len(found) != len(NAMES):
        sys.exit(f"make_hi: expected {len(NAMES)} figures on the cover, found {len(found)}")
    out = {}
    for name, g in zip(NAMES, found):
        g = ET.fromstring(ET.tostring(g))
        g.attrib.pop("transform")
        out[name] = re.sub(r"\s?xmlns(:\w+)?=\"[^\"]+\"", "", ET.tostring(g, encoding="unicode"))
    return out


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def page(n, figs):
    who = PAGES[n]
    parts = []
    xs = [78] if len(who) == 1 else [46, 110]
    for (name, line), x in zip(who, xs):
        scale = 1.7
        fx, fy = x - 20 * scale, 92  # the figure is 40 units wide at scale 1
        parts.append(f'<g transform="translate({fx:.1f} {fy}) scale({scale})">{figs[name]}</g>')
        # the speech bubble above the figure, its tail pointing down to the head
        w = max(34, min(66, len(line) * 2.0 + 12))
        bx, by = x - w / 2, 58
        parts.append(f'<rect x="{bx:.1f}" y="{by}" width="{w:.1f}" height="20" rx="5" fill="#ffffff" '
                     f'stroke="{COLOURS[name]}" stroke-width="0.6"/>')
        parts.append(f'<path d="M{x - 3:.1f} {by + 20} L{x:.1f} {by + 26} L{x + 3:.1f} {by + 20} z" fill="#ffffff" '
                     f'stroke="{COLOURS[name]}" stroke-width="0.6"/>')
        parts.append(f'<rect x="{x - 2.9:.1f}" y="{by + 19.2}" width="5.8" height="1.2" fill="#ffffff"/>')
        # split a long line in two
        words, rows, cur = line.split(), [], ""
        for wd in words:
            if len(cur) + len(wd) + 1 > 20 and cur:
                rows.append(cur)
                cur = wd
            else:
                cur = (cur + " " + wd).strip()
        rows.append(cur)
        y0 = by + (11.8 if len(rows) == 1 else 9.0)
        for k, row in enumerate(rows):
            parts.append(f'<text x="{x:.1f}" y="{y0 + k * 5.8:.1f}" font-family="Inter, Helvetica, Arial, sans-serif" '
                         f'font-size="5" font-weight="600" fill="#1f2933" text-anchor="middle">{esc(row)}</text>')
        parts.append(f'<text x="{x:.1f}" y="{fy + 90:.1f}" font-family="Inter, Helvetica, Arial, sans-serif" '
                     f'font-size="4.6" font-weight="800" fill="{COLOURS[name]}" text-anchor="middle">{esc(name)}</text>')
    label = " ".join(f"{name}: {line}" for name, line in who)
    return (f'<svg xmlns="{NS}" width="156mm" height="200mm" viewBox="0 0 156 200" role="img" '
            f'aria-label="{esc(label)}">' + "".join(parts) + "</svg>\n")


if __name__ == "__main__":
    figs = figures()
    for n in PAGES:
        with open(os.path.join(HERE, f"hi-{n}.svg"), "w", encoding="utf-8") as f:
            f.write(page(n, figs))
        print(f"make_hi: hi-{n}.svg")
