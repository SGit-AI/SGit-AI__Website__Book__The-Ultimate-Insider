"""Experiment 02 (ruv): the talk's M01 as one long image.

Reads paths.json (written by sample.js from the animation itself) and writes:
  long.svg     the strip: the plan as M01 draws it, twice, with every walk drawn as a trail and the time down the left
  pages.html   the experiment's one page, in the lab's format (lab/README.md), the strip spanning all twelve columns
  page.html    a preview: lab.css, the header from experiment.json, then pages.html (printed to page.pdf)

Usage: python3 -I tools/build.py   (from anywhere; paths are relative to this file)
"""
import html, importlib.util, json, re
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
LAB  = HERE.parents[1]
INK, MUTED, FILL, FILL2, ACCENT, PAPER = '#1f2933', '#5b6670', '#eef2f6', '#d5dce4', '#b0481a', '#ffffff'
VARS = {'var(--bg2)': FILL, 'var(--bg)': PAPER, 'var(--panel)': PAPER, 'var(--line2)': MUTED, 'var(--gold)': FILL2}

W, LEFT = 178, 86                                   # mm: the strip spans the twelve columns; the left 82 mm carry time and words
CROP = (70, 140, 1140, 572)                         # M01's canvas pixels: the building, its labels and the way in
K = (W - LEFT) / CROP[2]                            # mm per canvas pixel
PH = CROP[3] * K                                    # one plan's height in mm
PT9 = 3.18                                          # 9 pt in mm, the lab's floor


def plan(svg):
    """M01's own plan, labels and split arrow, with its colour variables set to the lab's palette."""
    for v, c in VARS.items():
        svg = svg.replace(v, c)
    svg = re.sub(r' (data-in|data-out|style|class)="[^"]*"', '', svg)
    svg = svg.replace('<text ', f'<text font-family="Inter, Helvetica, Arial, sans-serif" font-weight="700" font-size="{PT9 / K:.1f}" fill="{MUTED}" ')
    svg = svg.replace(f'fill="{FILL2}"', f'fill="{FILL2}" stroke="{INK}" stroke-width="1.5"')   # the gold: greyscale-safe
    return svg


def thin(pts, d=1.5):
    out = [pts[0]]
    for p in pts[1:]:
        if abs(p['x'] - out[-1]['x']) + abs(p['y'] - out[-1]['y']) >= d or p['red'] != out[-1]['red']:
            out.append(p)
    return out


def trail(pts, colour_before, width, opacity):
    pts = thin(pts)
    before = [p for p in pts if not p['red']]
    after = [p for p in pts if p['red']]
    if before and after:
        after = [before[-1]] + after
    line = lambda ps, c: (f'<polyline points="{" ".join(f"{p["x"]:.0f},{p["y"]:.0f}" for p in ps)}" fill="none" stroke="{c}" '
                          f'stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round" opacity="{opacity}"/>') if len(ps) > 1 else ''
    return line(before, colour_before) + line(after, ACCENT)


def glyph(p, colour):
    return (f'<g transform="translate({p["x"]:.0f} {p["y"]:.0f})" fill="{colour}"><circle cx="0" cy="-15" r="6.5"/>'
            f'<rect x="-6" y="-7" width="12" height="17" rx="5"/></g>')


def words(x, y, lines, size=PT9, weight=400, colour=INK, lead=1.33):
    out = []
    for i, ln in enumerate(lines):
        out.append(f'<text x="{x}" y="{y + i * size * lead:.2f}" font-family="Inter, Helvetica, Arial, sans-serif" '
                   f'font-size="{size:.2f}" font-weight="{weight}" fill="{colour}">{ln}</text>')
    return '\n'.join(out)


def strip(d):
    people, agents = d['people'], d['agents']
    p1, p2 = 16, 16 + PH + 8                         # where the two plans start, mm from the top
    end = p2 + PH + 22
    g = lambda y: f'<g transform="translate({LEFT} {y:.2f}) scale({K:.5f}) translate({-CROP[0]} {-CROP[1]})">'
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {end:.2f}" role="img" aria-label="M01, the building, as one '
         'long image: the plan twice, top to bottom. Above, every person who got in, each walk a line from the one way in to the '
         'room where they stopped; three lines go on to the gold and turn red. Below, every agent, each walk a line that turns red '
         'where it starts doing damage and goes room after room, most ending round the gold.">']
    # the time spine: one line down the left, with the four stops of M01 on it
    s.append(f'<line x1="3" y1="4" x2="3" y2="{end - 6:.2f}" stroke="{MUTED}" stroke-width=".4"/>')
    for y, t in ((4, '0:00'), (p1, '0:05'), (p2, '0:23'), (end - 15, '0:37 to 0:43')):
        s.append(f'<circle cx="3" cy="{y:.2f}" r="1.1" fill="{INK}"/>')
        s.append(words(7, y + 1.1, [t], weight=700))
    s.append(words(7, 4 + 1.1 + 4.6, ['A building. One way in. A corridor that splits.']))
    # 1: the people
    s.append(words(7, p1 + 1.1 + 4.6, ['Most turned left.', '<tspan fill="%s" font-weight="700">Now and then</tspan>, one' % ACCENT,
                                       'found the gold.']))
    s.append(words(7, p1 + 20, ['Each line: one person,', 'from the way in to', 'where they stopped.'], colour=MUTED))
    s.append(g(p1) + plan(d['plan']) + ''.join(trail(f, INK, 2.2, .75) for f in people)
             + ''.join(glyph(f[-1], ACCENT if f[-1]['red'] else INK) for f in people) + '</g>')
    # 2: the agents, with the people still where they stopped
    s.append(words(7, p2 + 1.1 + 4.6, ['Agents: more of them,', '<tspan fill="%s" font-weight="700">and they keep going.</tspan>' % ACCENT]))
    s.append(words(7, p2 + 16, ['Each line: one agent.', 'It turns red where', 'it starts doing damage.'], colour=MUTED))
    s.append(g(p2) + plan(d['plan']) + ''.join(trail(f, MUTED, 2.2, .55) for f in agents)
             + ''.join(glyph(f[-1], INK) for f in people) + ''.join(glyph(f[-1], ACCENT) for f in agents) + '</g>')
    # the still
    y = end - 15 + 1.1 + 4.6
    s.append(words(7, y, ['People stop at a room. <tspan fill="%s" font-weight="700">Agents don\'t stop.</tspan>' % ACCENT]))
    s.append(words(7, y + 4.6, ['Red: doing damage. A pattern, not a count.', 'Red shows capability, not intent: the talk\'s agents were a benign team.'],
                   colour=MUTED))
    s.append('</svg>')
    return '\n'.join(s)


def main():
    d = json.loads((HERE / 'paths.json').read_text())
    (HERE / 'long.svg').write_text(strip(d) + '\n')
    (HERE / 'pages.html').write_text(
        '<section class="page" data-claims="">\n <figure class="fig span12">\n'
        '  <img src="{{dir}}/long.svg" alt="M01 as one long image: the people\'s walks above, the agents\' below" style="width:178mm;display:block">\n'
        '  <figcaption><b>See it in two looks: the short lines above stop in rooms; the red lines below do not.</b>'
        '<span class="src">M01 v1, src/static/motion/lab/the-building/v1/index.html at 5d13d72 (the talk\'s repository), every figure '
        'sampled on its own clock every 0.1 s by tools/sample.js</span></figcaption>\n </figure>\n</section>\n')
    spec = importlib.util.spec_from_file_location('build_lab', LAB / 'tools' / 'build_lab.py')
    bl = importlib.util.module_from_spec(spec); spec.loader.exec_module(bl)       # the designer's header and page, read only
    meta = json.loads((HERE / 'experiment.json').read_text())
    inner = re.search(r'<section class="page"[^>]*>(.*)</section>', (HERE / 'pages.html').read_text(), re.S).group(1).replace('{{dir}}', '.')   # the lab build sets {{dir}}
    css = (LAB / 'tools' / 'lab.css').read_text()
    (HERE / 'page.html').write_text(f'<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>{html.escape(meta["title"])}</title>'
                                    f'<style>{css}</style></head><body>{bl.page(bl.header(meta) + inner, meta["id"])}</body></html>\n')


if __name__ == '__main__':
    main()
