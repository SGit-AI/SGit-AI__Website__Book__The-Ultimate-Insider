#!/usr/bin/env python3
"""The timeline component: a JSON file in, an SVG in the lab's language out, horizontal or vertical.

    python3 lab/tools/components/timeline.py <spec.json> [horizontal|vertical] [length_mm] > out.svg
    from timeline import render; render(spec_dict, mode="horizontal", length=164)

The spec: {"events": [{"t": "HH:MM", "label": "...", "claim": "C001", "accent": false}], "break_after_minutes": 180}.
Times are drawn to scale; a gap longer than break_after_minutes is drawn as a marked break of fixed size, never
silently squeezed. Labels that would collide stack on further levels with a leader line. One event may be the
accent. Text is 9 pt at the size given (one SVG unit is one millimetre). Only registered times belong in a spec.
"""
import html, json, sys

FONT = 3.18            # 9 pt in millimetres: the lab's floor
CHAR = 1.72            # mean width of a character at that size, for collision only
BREAK = 9.0            # the drawn length of a break, in millimetres
INK, MUTED, ACCENT, FILL = "#1f2933", "#5b6670", "#b0481a", "#d5dce4"


def minutes(t):
    h, m = t.split(":")
    return int(h) * 60 + int(m)


def positions(events, length, break_after):
    """Each event's place along the axis, to scale between breaks; and where the breaks fall."""
    ts = [minutes(e["t"]) for e in events]
    spans, breaks = [], []
    for a, b in zip(ts, ts[1:]):
        if b - a > break_after:
            breaks.append(len(spans))
            spans.append(None)
        else:
            spans.append(b - a)
    linear = sum(s for s in spans if s is not None) or 1
    scale = (length - BREAK * len(breaks)) / linear
    xs, x, marks = [0.0], 0.0, []
    for i, s in enumerate(spans):
        if s is None:
            marks.append(x + BREAK / 2)
            x += BREAK
        else:
            x += s * scale
        xs.append(x)
    return xs, marks


def esc(s):
    return html.escape(str(s), quote=False)


def _label(e):
    return f"{e['t']}  {e['label']}"


def horizontal(spec, length):
    ev = sorted(spec["events"], key=lambda e: minutes(e["t"]))
    pad = 2.0
    xs, marks = positions(ev, length - 2 * pad - CHAR * 6, spec.get("break_after_minutes", 180))
    xs = [x + pad for x in xs]
    # levels alternate above and below the axis; each label takes the first level where it does not collide
    order = [(1, 1), (-1, 1), (1, 2), (-1, 2), (1, 3), (-1, 3), (1, 4), (-1, 4)]
    taken, placed = {k: [] for k in order}, []
    for x, e in zip(xs, ev):
        w = max(len(e["t"]), len(e["label"]), len(e.get("claim", ""))) * CHAR + 2
        x0 = x if x + w <= length else x - w + 1   # near the right edge the label sits to the left of its point
        for k in order:
            if all(x0 > b + 1.5 or x0 + w < a - 1.5 for a, b in taken[k]):
                taken[k].append((x0, x0 + w)); placed.append((x, x0, k, e)); break
        else:
            raise SystemExit(f"timeline: no room for '{e['label']}' at {length} mm")
    up = max([k[1] for _, _, k, _ in placed if k[0] == 1] or [0])
    down = max([k[1] for _, _, k, _ in placed if k[0] == -1] or [0])
    row = FONT * 1.25 * 3 + 2.5                    # three lines: time, label, claim
    axis = 4 + up * row
    height = axis + down * row + 4
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {length:g} {height:.1f}" class="timeline" role="img" aria-label="{esc(spec.get("alt", "A timeline"))}">',
           f'<line x1="0" y1="{axis}" x2="{length}" y2="{axis}" stroke="{INK}" stroke-width=".5"/>']
    for m in marks:
        m += pad
        out.append(f'<rect x="{m - BREAK / 2 + 1}" y="{axis - 2.5}" width="{BREAK - 2}" height="5" fill="#fff"/>')
        out += [f'<line x1="{m - 2 + d}" y1="{axis + 2.5}" x2="{m + d}" y2="{axis - 2.5}" stroke="{MUTED}" stroke-width=".5"/>' for d in (-1, 1)]
    for x, x0, (side, lvl), e in placed:
        col = ACCENT if e.get("accent") else INK
        top = axis - lvl * row if side == 1 else axis + (lvl - 1) * row + 3
        out.append(f'<circle cx="{x:.2f}" cy="{axis}" r="1.3" fill="{col}"/>')
        y_end = top + row - 2 if side == 1 else top
        if x0 < x:
            y_end = top + FONT * 0.3              # a label left of its point: the leader runs up beside its first line
        out.append(f'<line x1="{x:.2f}" y1="{axis}" x2="{x:.2f}" y2="{y_end:.2f}" stroke="{col}" stroke-width=".3"/>')   # the leader is always vertical
        tx = x0 + 1 if x0 >= x else x0 - 0.5
        out.append(f'<text x="{tx:.2f}" y="{top + FONT:.2f}" font-family="Inter, Helvetica, Arial, sans-serif" font-size="{FONT}" font-weight="800" fill="{col}">{esc(e["t"])}</text>')
        out.append(f'<text x="{tx:.2f}" y="{top + FONT * 2.25:.2f}" font-family="Inter, Helvetica, Arial, sans-serif" font-size="{FONT}" fill="{col}">{esc(e["label"])}</text>')
        if e.get("claim"):
            out.append(f'<text x="{tx:.2f}" y="{top + FONT * 3.5:.2f}" font-family="DejaVu Sans Mono, monospace" font-size="{FONT}" fill="{MUTED}">{esc(e["claim"])}</text>')
    out.append("</svg>")
    return "".join(out)


def vertical(spec, length):
    ev = sorted(spec["events"], key=lambda e: minutes(e["t"]))
    xs, marks = positions(ev, length - 8, spec.get("break_after_minutes", 180))
    ys = [y + 4 for y in xs]
    row = FONT * 1.25 * 2 + 2                       # two lines: time and label, claim on the time line
    placed, last = [], -99.0
    for y, e in zip(ys, ev):
        ly = max(y - FONT, last + row)               # labels move down, never up, when they would collide
        placed.append((y, ly, e)); last = ly
    height = max(length, last + row + 2)
    width = 14 + max(max(len(e["label"]), len(e["t"]) + 1 + len(e.get("claim", ""))) for e in ev) * CHAR
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.1f} {height:.1f}" class="timeline" role="img" aria-label="{esc(spec.get("alt", "A timeline"))}">',
           f'<line x1="4" y1="0" x2="4" y2="{ys[-1] + 2:.1f}" stroke="{INK}" stroke-width=".5"/>']
    for m in marks:
        m += 4
        out.append(f'<rect x="1.5" y="{m - BREAK / 2 + 1}" width="5" height="{BREAK - 2}" fill="#fff"/>')
        out += [f'<line x1="1.5" y1="{m + 2 + d}" x2="6.5" y2="{m + d}" stroke="{MUTED}" stroke-width=".5"/>' for d in (-1, 1)]
    for y, ly, e in placed:
        col = ACCENT if e.get("accent") else INK
        out.append(f'<circle cx="4" cy="{y:.2f}" r="1.3" fill="{col}"/>')
        out.append(f'<path d="M5.3 {y:.2f} L8 {y:.2f} L10 {ly + FONT * 0.7:.2f} L11 {ly + FONT * 0.7:.2f}" fill="none" stroke="{col}" stroke-width=".3"/>')
        out.append(f'<text x="12" y="{ly + FONT:.2f}" font-family="Inter, Helvetica, Arial, sans-serif" font-size="{FONT}" fill="{col}"><tspan font-weight="800">{esc(e["t"])}</tspan>'
                   + (f'<tspan font-family="DejaVu Sans Mono, monospace" fill="{MUTED}"> {esc(e["claim"])}</tspan>' if e.get("claim") else "") + '</text>')
        out.append(f'<text x="12" y="{ly + FONT * 2.25:.2f}" font-family="Inter, Helvetica, Arial, sans-serif" font-size="{FONT}" fill="{col}">{esc(e["label"])}</text>')
    out.append("</svg>")
    return "".join(out)


def render(spec, mode="horizontal", length=164.0):
    return (vertical if mode == "vertical" else horizontal)(spec, float(length))


if __name__ == "__main__":
    spec = json.load(open(sys.argv[1]))
    print(render(spec, sys.argv[2] if len(sys.argv) > 2 else "horizontal", sys.argv[3] if len(sys.argv) > 3 else 164))
