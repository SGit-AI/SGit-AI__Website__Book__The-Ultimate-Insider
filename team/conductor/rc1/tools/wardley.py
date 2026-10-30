#!/usr/bin/env python3
"""Render a Wardley map from a small JSON file to SVG, sized for print (a 6 x 9 inch page).

Ported from the talk's storyteller (team/storyteller/tools/wardley.py at 298be4e) and reworked for
the book by its illustrator: larger type, wrapped labels, clean lines, notes, dark dashed evolution arrows and hatched shading that survive a black-and-white print,
inertia bars, directed flows, zones and a legend. The talk's map files still render unchanged.

The viewBox is 1000 units wide; printed at the text width (about 4.7 inches) a unit is about a
third of a point, so the 23-unit label is about 8 pt and nothing on a map is smaller than 7 pt.

A map file:
  "title"       one line (wrapped if long)
  "height"      plot height in units (default 640)
  "axes"        "full" (default) or "chain" (the value chain only: no evolution stages)
  "components"  [{"id", "label", "vis", "evo",
                  "pos": "right"|"left"|"above"|"below" (label side; omitted, the renderer picks the clearest), "dx", "dy", "w" (wrap, chars),
                  "anchor": true (the user, drawn solid), "inside": true (hatched), "fill",
                  "shape": "circle"|"square", "ghost": true (dashed: proposed, absent or never used),
                  "move": evo it is heading to (dark dashed arrow), "was": evo it came from (grey ring),
                  "inertia": evo where a bar holds the move back, "bold": true}]
                vis is 0 (invisible) to 1 (the user); evo is 0 (genesis) to 1 (commodity)
  "links"       [[from, to]]  plain dependency lines
  "flows"       [{"from", "to", "label", "color", "dash": true, "bend": -1..1, "lpos": 0..1}]  directed arrows
  "bands"       [{"label", "from", "to", "fill"}]  vertical bands across evolution
  "zones"       [{"label", "vis": [lo, hi], "evo": [lo, hi], "fill", "stroke", "hatch": true, "lpos": "top"|"bottom"}]
  "notes"       [{"text", "vis", "evo", "w", "align": "start"|"middle"|"end", "color", "size"}]
  "stage_notes" four short lines, one under each stage name (what the stage means)
  "legend"      [{"kind": "circle"|"square"|"inside"|"anchor"|"ghost"|"move"|"inertia"|"flow"|"was", "text", "fill"?}]
Usage: python3 wardley.py map.json [...]   (writes map.svg beside each)
"""
import json, sys, html, math
from pathlib import Path

W, L, R, T0 = 1000, 64, 26, 20
FONT = "Inter, 'DejaVu Sans', Arial, sans-serif"
INK, GREY, LINE, RED, BLUE = '#1a1a1a', '#5a5a5a', '#9a9a9a', '#c0392b', '#1f5f99'
MOVE = '#7a1f14'  # very dark red: reads as a red arrow in colour and as a near-black dashed arrow in grey
HATCH = 'url(#hatch)'
LABEL, NOTE, AXIS, TITLE = 23, 21, 20, 28
CHAR = 0.53  # average glyph width, as a share of the font size


def esc(s):
    return html.escape(str(s))


def wrap(text, width):
    words, lines, cur = str(text).split(), [], ''
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur); cur = w
        else:
            cur = f'{cur} {w}'.strip()
    if cur: lines.append(cur)
    return lines or ['']


def text_block(x, y, lines, size, anchor='start', extra='', valign='middle', lh=1.18):
    """Lines of text whose block is centred (or topped, or bottomed) on y."""
    step = size * lh
    total = step * (len(lines) - 1)
    if valign == 'middle': y0 = y - total / 2 + size * 0.35
    elif valign == 'top': y0 = y + size * 0.8
    else: y0 = y - total - size * 0.25
    spans = ''.join(f'<tspan x="{x:.1f}" y="{y0 + i * step:.1f}">{esc(l)}</tspan>' for i, l in enumerate(lines))
    return f'<text text-anchor="{anchor}" font-size="{size}" stroke="#fff" stroke-width="9" stroke-linejoin="round" paint-order="stroke"{extra}>{spans}</text>'


def render(m):
    title_lines = wrap(m.get('title', ''), 62)
    T = T0 + len(title_lines) * TITLE * 1.2 + 18
    PH = m.get('height', 640)
    chain_only = m.get('axes', 'full') == 'chain'
    legend = m.get('legend', [])
    stage_notes = m.get('stage_notes')
    SN = max(len(wrap(t, 17)) for t in stage_notes) * 22 + 10 if stage_notes else 0
    B = (92 + SN) if not chain_only else 40
    LEG = (24 + 36 * math.ceil(len(legend) / 2)) if legend else 0
    H = T + PH + B + LEG
    x0, x1, y0, y1 = L, W - R, T, T + PH

    def xy(vis, evo):
        return x0 + evo * (x1 - x0), y0 + (1 - vis) * (y1 - y0)

    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H:.0f}" font-family="{FONT}" fill="{INK}">',
         f'<rect width="{W}" height="{H:.0f}" fill="#fff"/>',
         '<defs>'
         f'<marker id="red" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0L10 5L0 10z" fill="{MOVE}"/></marker>'
         '<pattern id="hatch" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="7" height="7" fill="#e9d2b8"/><line x1="0" y1="0" x2="0" y2="7" stroke="#5a4030" stroke-width="2.2"/></pattern>'
         '<pattern id="zhatch" width="16" height="16" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="16" height="16" fill="#f7efe6"/><line x1="0" y1="0" x2="0" y2="16" stroke="#d8c3ad" stroke-width="2"/></pattern>'
         f'<marker id="ax" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0L10 5L0 10z" fill="{INK}"/></marker>'
         '</defs>']
    o.append(text_block(L - 40, T0 + TITLE * 0.4, title_lines, TITLE, extra=' font-weight="700"', valign='top', lh=1.2))

    # bands and zones, under everything
    for band in m.get('bands', []):
        bx0, _ = xy(0, band['from']); bx1, _ = xy(0, band['to'])
        o.append(f'<rect x="{bx0:.1f}" y="{y0}" width="{bx1 - bx0:.1f}" height="{PH}" fill="{band.get("fill", "#eef4fb")}"/>')
        o.append(text_block((bx0 + bx1) / 2, y0 + 10, [band['label']], AXIS, 'middle', f' font-weight="600" fill="{GREY}"', 'top'))
    for z in m.get('zones', []):
        zx0, zy1 = xy(z['vis'][0], z['evo'][0]); zx1, zy0 = xy(z['vis'][1], z['evo'][1])
        o.append(f'<rect x="{zx0:.1f}" y="{zy0:.1f}" width="{zx1 - zx0:.1f}" height="{zy1 - zy0:.1f}" rx="14" '
                 f'fill="{"url(#zhatch)" if z.get("hatch") else z.get("fill", "#f3f3f3")}" stroke="{z.get("stroke", "#8a8a8a")}" stroke-width="1.6" stroke-dasharray="7 5"/>')
        lines = wrap(z['label'], z.get('w', 40))
        if z.get('lpos', 'top') == 'top':
            o.append(text_block(zx0 + 14, zy0 + 8, lines, AXIS, 'start', f' font-weight="600" fill="{GREY}"', 'top'))
        else:
            o.append(text_block(zx0 + 14, zy1 - 10, lines, AXIS, 'start', f' font-weight="600" fill="{GREY}"', 'bottom'))

    # axes
    o.append(f'<line x1="{x0}" y1="{y1}" x2="{x0}" y2="{y0 - 6}" stroke="{INK}" stroke-width="2" marker-end="url(#ax)"/>')
    o.append(f'<text transform="translate({x0 - 22} {(y0 + y1) / 2:.0f}) rotate(-90)" text-anchor="middle" font-size="{AXIS}" fill="{GREY}">Value chain</text>')
    o.append(f'<text transform="translate({x0 - 22} {y0 + 4}) rotate(-90)" text-anchor="end" font-size="{AXIS - 2}" fill="{GREY}">Visible</text>')
    o.append(f'<text transform="translate({x0 - 22} {y1}) rotate(-90)" text-anchor="start" font-size="{AXIS - 2}" fill="{GREY}">Invisible</text>')
    if not chain_only:
        o.append(f'<line x1="{x0}" y1="{y1}" x2="{x1 + 6}" y2="{y1}" stroke="{INK}" stroke-width="2" marker-end="url(#ax)"/>')
        stages = [['Genesis'], ['Custom built'], ['Product', '(+rental)'], ['Commodity', '(+utility)']]
        for i, st in enumerate(stages):
            sx = x0 + i / 4 * (x1 - x0)
            if i: o.append(f'<line x1="{sx:.1f}" y1="{y0}" x2="{sx:.1f}" y2="{y1}" stroke="#c4c4c4" stroke-width="1.2" stroke-dasharray="5 6"/>')
            o.append(text_block(sx + (x1 - x0) / 8, y1 + 10, st, AXIS, 'middle', f' fill="{INK}"', 'top'))
        for i, t in enumerate(stage_notes or []):
            sx = x0 + i / 4 * (x1 - x0) + (x1 - x0) / 8
            o.append(text_block(sx, y1 + 64, wrap(t, 17), 19, 'middle', f' fill="{GREY}" font-style="italic"', 'top'))
        o.append(text_block((x0 + x1) / 2, y1 + 66 + SN, ['Evolution'], AXIS, 'middle', f' fill="{GREY}" font-style="italic"', 'top'))

    c = {x['id']: x for x in m['components']}

    def at(i):
        return xy(c[i]['vis'], c[i]['evo'])

    for lk in m.get('links', []):
        (ax, ay), (bx, by) = at(lk[0]), at(lk[1])
        o.append(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{LINE}" stroke-width="1.6"/>')

    late, flow_boxes = [], []
    # flows: directed arrows, optionally curved, stopping short of the circles
    for i, f in enumerate(m.get('flows', [])):
        (ax, ay), (bx, by) = at(f['from']), at(f['to'])
        col = f.get('color', BLUE)
        mid = f'fl{i}'
        o.append(f'<defs><marker id="{mid}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0L10 5L0 10z" fill="{col}"/></marker></defs>')
        d = math.hypot(bx - ax, by - ay) or 1
        ux, uy = (bx - ax) / d, (by - ay) / d
        sx, sy, ex, ey = ax + ux * 14, ay + uy * 14, bx - ux * 16, by - uy * 16
        bend = f.get('bend', 0)
        cx, cy = (sx + ex) / 2 - uy * bend * d * 0.5, (sy + ey) / 2 + ux * bend * d * 0.5
        dash = ' stroke-dasharray="9 6"' if f.get('dash') else ''
        o.append(f'<path d="M{sx:.1f} {sy:.1f} Q{cx:.1f} {cy:.1f} {ex:.1f} {ey:.1f}" fill="none" stroke="{col}" stroke-width="2.4"{dash} marker-end="url(#{mid})"/>')
        if f.get('label'):
            t = f.get('lpos', 0.5)
            lx = (1 - t) ** 2 * sx + 2 * (1 - t) * t * cx + t ** 2 * ex
            ly = (1 - t) ** 2 * sy + 2 * (1 - t) * t * cy + t ** 2 * ey
            lines = wrap(f['label'], f.get('w', 22))
            fx, fy = lx + f.get('dx', 8), ly + f.get('dy', 0)
            fw, fh = max(map(len, lines)) * NOTE * CHAR, len(lines) * NOTE * 1.18
            al = f.get('align', 'start')
            flow_boxes.append((fx - (fw / 2 if al == 'middle' else fw if al == 'end' else 0), fy - fh / 2, fw, fh))
            late.append(text_block(fx, fy, lines, NOTE, al, f' fill="{col}" font-style="italic" font-weight="600"'))

    # movement: previous positions, inertia, arrows
    for x in m['components']:
        px, py = at(x['id'])
        if 'was' in x:
            wx, _ = xy(x['vis'], x['was'])
            o.append(f'<circle cx="{wx:.1f}" cy="{py:.1f}" r="8" fill="#fff" stroke="#9a9a9a" stroke-width="1.8" stroke-dasharray="3 3"/>')
            o.append(f'<line x1="{wx + 11:.1f}" y1="{py:.1f}" x2="{px - 13:.1f}" y2="{py:.1f}" stroke="{MOVE}" stroke-width="3" stroke-dasharray="10 6" marker-end="url(#red)"/>')
        if 'move' in x:
            mx, _ = xy(x['vis'], x['move'])
            o.append(f'<line x1="{px + 12:.1f}" y1="{py:.1f}" x2="{mx:.1f}" y2="{py:.1f}" stroke="{MOVE}" stroke-width="3" stroke-dasharray="10 6" marker-end="url(#red)"/>')
        if 'inertia' in x:
            ix, _ = xy(x['vis'], x['inertia'])
            o.append(f'<rect x="{ix - 4:.1f}" y="{py - 20:.1f}" width="8" height="40" fill="{INK}"/>')

    # obstacles for label placement: every line drawn, every point, every note
    segs = []
    for lk in m.get('links', []):
        segs.append((at(lk[0]), at(lk[1])))
    for f in m.get('flows', []):
        segs.append((at(f['from']), at(f['to'])))
    for x in m['components']:
        px, py = at(x['id'])
        for k in ('move', 'was'):
            if k in x:
                segs.append(((px, py), (xy(x['vis'], x[k])[0], py)))
    pts = {x['id']: at(x['id']) for x in m['components']}
    for x in m['components']:
        if 'was' in x: pts[x['id'] + '~was'] = (xy(x['vis'], x['was'])[0], at(x['id'])[1])
    boxes = list(flow_boxes)
    for z in m.get('zones', []):
        zx0, zy1 = xy(z['vis'][0], z['evo'][0]); zx1, zy0 = xy(z['vis'][1], z['evo'][1])
        zl = wrap(z['label'], z.get('w', 40)); zh = len(zl) * AXIS * 1.18
        zw = max(map(len, zl)) * AXIS * CHAR
        boxes.append((zx0 + 14, zy0 + 8 if z.get('lpos', 'top') == 'top' else zy1 - 10 - zh, zw, zh))
    for b in m.get('bands', []):
        bx0, _ = xy(0, b['from']); bx1, _ = xy(0, b['to'])
        bw = len(b['label']) * AXIS * CHAR
        boxes.append(((bx0 + bx1 - bw) / 2, y0 + 8, bw, AXIS * 1.2))
    for n in m.get('notes', []):
        nx, ny = xy(n['vis'], n['evo'])
        nl = wrap(n['text'], n.get('w', 30)); sz = n.get('size', NOTE)
        bw, bh = max(map(len, nl)) * sz * CHAR, len(nl) * sz * 1.18
        bx = nx - (bw / 2 if n.get('align') == 'middle' else bw if n.get('align') == 'end' else 0)
        boxes.append((bx, ny if n.get('valign', 'bottom' if n['vis'] < 0.25 else 'top') == 'top' else ny - bh, bw, bh))

    def hits(seg, b):
        (ax, ay), (bx, by) = seg
        for i in range(41):
            t = i / 40
            qx, qy = ax + (bx - ax) * t, ay + (by - ay) * t
            if b[0] - 3 <= qx <= b[0] + b[2] + 3 and b[1] - 3 <= qy <= b[1] + b[3] + 3:
                return True
        return False

    def overlap(a, b):
        return a[0] < b[0] + b[2] and b[0] < a[0] + a[2] and a[1] < b[1] + b[3] and b[1] < a[1] + a[3]

    def candidates(px, py, bw, bh, x):
        if x.get('pos'):
            orders = [(x['pos'], x.get('dx', 0), x.get('dy', 0), 0)]
        else:
            orders = []
            for name, cost in (('right', 0), ('left', 3), ('above', 5), ('below', 6)):
                orders.append((name, 0, 0, cost))
            for d in (-1, 1):
                orders.append(('right', 0, d * (bh / 2 + 6), 4))
                orders.append(('left', 0, d * (bh / 2 + 6), 7))
                orders.append(('right', 0, d * (bh / 2 + 22), 10))
                orders.append(('left', 0, d * (bh / 2 + 22), 12))
                orders.append(('above', d * bw / 3, 0, 8))
                orders.append(('below', d * bw / 3, 0, 9))
                orders.append(('above', d * (bw / 2 + 6), 0, 11))
                orders.append(('below', d * (bw / 2 + 6), 0, 12))
        for name, dx, dy, cost in orders:
            if name == 'right': b = (px + 16 + dx, py + dy - bh / 2, bw, bh)
            elif name == 'left': b = (px - 16 + dx - bw, py + dy - bh / 2, bw, bh)
            elif name == 'above': b = (px + dx - bw / 2, py - 16 + dy - bh, bw, bh)
            else: b = (px + dx - bw / 2, py + 16 + dy, bw, bh)
            yield name, dx, dy, cost, b

    placed = []
    for x in m['components']:
        px, py = at(x['id'])
        best = None
        widths = [x.get('w', 22)] if x.get('pos') else sorted({x.get('w', 22), round(x.get('w', 22) * 1.5), max(10, round(x.get('w', 22) * 0.7))})
        for wi in widths:
          lines = wrap(x['label'], wi)
          bw, bh = max(map(len, lines)) * LABEL * CHAR, len(lines) * LABEL * 1.18
          for name, dx, dy, cost, b in candidates(px, py, bw, bh, x):
            sc = cost + (0 if wi == x.get('w', 22) else 3) + 3 * len(lines)
            if b[0] < x0 + 6 or b[0] + b[2] > W - 2 or b[1] < T - 14 or b[1] + b[3] > y1 + (40 if chain_only else -2):
                sc += 5000
            sc += 1000 * sum(overlap(b, o2) for o2 in placed + boxes)
            sc += 800 * sum(1 for k, (qx, qy) in pts.items() if k != x['id'] and b[0] - 10 <= qx <= b[0] + b[2] + 10 and b[1] - 10 <= qy <= b[1] + b[3] + 10)
            sc += 120 * sum(1 for sg in segs if hits(sg, b))
            if best is None or sc < best[0]:
                best = (sc, name, dx, dy, b, lines)
        placed.append(best[4])
        x['_label'] = best[1:4] + (best[5],)

    for x in m['components']:
        px, py = at(x['id'])
        r = 10 if x.get('anchor') else 8.5
        fill = x.get('fill') or (INK if x.get('anchor') else HATCH if x.get('inside') else '#fff')
        dash = ' stroke-dasharray="4 3"' if x.get('ghost') else ''
        if x.get('shape') == 'square':
            o.append(f'<rect x="{px - r:.1f}" y="{py - r:.1f}" width="{2 * r}" height="{2 * r}" fill="{fill}" stroke="{INK}" stroke-width="2.2"{dash}/>')
        else:
            o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r}" fill="{fill}" stroke="{INK}" stroke-width="2.2"{dash}/>')
        pos, dx, dy, lines = x.pop('_label')
        weight = ' font-weight="700"' if (x.get('anchor') or x.get('bold')) else ''
        style = weight + (' font-style="italic" fill="#555"' if x.get('ghost') else '')
        if pos == 'right':
            o.append(text_block(px + 16 + dx, py + dy, lines, LABEL, 'start', style))
        elif pos == 'left':
            o.append(text_block(px - 16 + dx, py + dy, lines, LABEL, 'end', style))
        elif pos == 'above':
            o.append(text_block(px + dx, py - 16 + dy, lines, LABEL, 'middle', style, 'bottom'))
        else:
            o.append(text_block(px + dx, py + 16 + dy, lines, LABEL, 'middle', style, 'top'))

    o.extend(late)
    for n in m.get('notes', []):
        px, py = xy(n['vis'], n['evo'])
        lines = wrap(n['text'], n.get('w', 30))
        o.append(text_block(px, py, lines, n.get('size', NOTE), n.get('align', 'start'),
                            f' fill="{n.get("color", RED)}" font-style="italic"', n.get('valign', 'bottom' if n['vis'] < 0.25 else 'top')))

    if legend:
        ly = y1 + B + 4
        o.append(f'<line x1="{x0}" y1="{ly:.0f}" x2="{x1}" y2="{ly:.0f}" stroke="#d0d0d0" stroke-width="1.2"/>')
        colw = (x1 - x0) / 2
        for i, it in enumerate(legend):
            gx = x0 + 18 + (i % 2) * colw
            gy = ly + 26 + (i // 2) * 36
            k = it['kind']
            if k in ('circle', 'inside', 'anchor', 'ghost'):
                f = it.get('fill') or (INK if k == 'anchor' else HATCH if k == 'inside' else '#fff')
                dash = ' stroke-dasharray="4 3"' if k == 'ghost' else ''
                o.append(f'<circle cx="{gx}" cy="{gy}" r="8.5" fill="{f}" stroke="{INK}" stroke-width="2.2"{dash}/>')
            elif k == 'square':
                sf = it.get('fill', '#fff')
                o.append(f'<rect x="{gx - 8.5}" y="{gy - 8.5}" width="17" height="17" fill="{sf}" stroke="{INK}" stroke-width="2.2"/>')
            elif k == 'move':
                o.append(f'<line x1="{gx - 12}" y1="{gy}" x2="{gx + 14}" y2="{gy}" stroke="{MOVE}" stroke-width="3" stroke-dasharray="10 6" marker-end="url(#red)"/>')
            elif k == 'was':
                o.append(f'<circle cx="{gx}" cy="{gy}" r="8" fill="#fff" stroke="#9a9a9a" stroke-width="1.8" stroke-dasharray="3 3"/>')
            elif k == 'inertia':
                o.append(f'<rect x="{gx - 4}" y="{gy - 14}" width="8" height="28" fill="{INK}"/>')
            elif k == 'flow':
                o.append(f'<line x1="{gx - 12}" y1="{gy}" x2="{gx + 14}" y2="{gy}" stroke="{it.get("color", BLUE)}" stroke-width="2.4" marker-end="url(#ax)"/>')
            o.append(f'<text x="{gx + 26}" y="{gy + 7}" font-size="{AXIS}" fill="{INK}">{esc(it["text"])}</text>')
    o.append('</svg>')
    return '\n'.join(o) + '\n'


if __name__ == '__main__':
    for p in sys.argv[1:]:
        p = Path(p)
        p.with_suffix('.svg').write_text(render(json.loads(p.read_text())))
        print('wrote', p.with_suffix('.svg'))
