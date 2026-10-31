#!/usr/bin/env python3
"""The counter strip: a row of registered numbers, each with its words and its claim id, in the lab's language.

    python3 lab/tools/components/counters.py <spec.json> [length_mm] > out.svg
    from counters import render; render(spec_dict, length=163)

The spec: {"items": [{"value": "816", "label": "commits in the talk's repository", "claim": "C002", "accent": false}]}.
Each number is 28 pt, its words 9 pt wrapped to the tile, its claim id 9 pt in the monospace. One item may carry the
accent. Only numbers from claims/register.json, each with its claim id; a claim not yet checked does not belong here.
"""
import html, json, sys

FONT, BIG, CHAR = 3.18, 9.88, 1.72          # 9 pt and 28 pt in millimetres; mean character width at 9 pt
MIN_TILE = 28.0                              # a tile narrower than this would crowd its number: the strip wraps instead
INK, MUTED, ACCENT, FILL2 = "#1f2933", "#5b6670", "#b0481a", "#d5dce4"
SANS, MONO = "Inter, Helvetica, Arial, sans-serif", "DejaVu Sans Mono, monospace"


def wrap(text, width):
    lines, line = [], ""
    for word in text.split():
        if line and len(line) + 1 + len(word) > width:
            lines.append(line); line = word
        else:
            line = f"{line} {word}".strip()
    return lines + [line] if line else lines


def render(spec, length=163.0):
    items, gap, length = spec["items"], 5.0, float(length)
    cols = max(1, min(len(items), int((length + gap) // (MIN_TILE + gap))))   # tiles never narrower than MIN_TILE: they wrap
    w = (length - gap * (cols - 1)) / cols
    per_line = max(8, int((w - 1) / CHAR))
    wrapped = [wrap(i["label"], per_line) for i in items]
    tile_h = 2 + BIG + 2 + FONT * 1.3 * max(len(l) for l in wrapped) + FONT * 1.4 + 2
    rows = -(-len(items) // cols)
    height = rows * tile_h + (rows - 1) * 3
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {length:g} {height:.1f}" class="counters" role="img" '
           f'aria-label="{html.escape(spec.get("alt", "A row of counts"))}">']
    for n, (i, lines) in enumerate(zip(items, wrapped)):
        x, y0 = (n % cols) * (w + gap), (n // cols) * (tile_h + 3)
        col = ACCENT if i.get("accent") else INK
        out.append(f'<rect x="{x:.2f}" y="{y0:.2f}" width="{w:.2f}" height="1.2" fill="{ACCENT if i.get("accent") else FILL2}"/>')
        out.append(f'<text x="{x:.2f}" y="{y0 + 2 + BIG * 0.85:.2f}" font-family="{SANS}" font-size="{BIG}" font-weight="800" fill="{col}">{html.escape(i["value"])}</text>')
        y = y0 + 2 + BIG + 2 + FONT
        for line in lines:
            out.append(f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{FONT}" fill="{INK}">{html.escape(line)}</text>')
            y += FONT * 1.3
        out.append(f'<text x="{x:.2f}" y="{y + 0.4:.2f}" font-family="{MONO}" font-size="{FONT}" fill="{MUTED}">{html.escape(i["claim"])}</text>')
    out.append("</svg>")
    return "".join(out)


if __name__ == "__main__":
    print(render(json.load(open(sys.argv[1])), sys.argv[2] if len(sys.argv) > 2 else 163))
