#!/usr/bin/env python3
"""The beat strip: the talk's beats in their three parts, heard or not reached, in order and in time.

    python3 lab/tools/components/beats.py <in-order.svg> <in-time.svg> [length_mm]
    from beats import read_beats, in_order, in_time

Reads claims/beat-times.md (the researcher's table for C097, on C015's 58 beats) when it runs: no value is typed
here. A beat the recording reaches is a filled cell, one it never reaches an outlined cell. In time, each heard beat
sits at the start of the transcript block it was first heard in (C097: block stamps, so beats that share a stamp
share a tick and are stacked); the unheard sit after the recording's end. One SVG unit a millimetre, size stated,
text 9 pt (3.18 mm). In the counter strip's family (counters.py).
"""
import re, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
F = 3.18
INK, MUTED, FILL2, ACCENT, PAPER = "#1f2933", "#5b6670", "#d5dce4", "#b0481a", "#ffffff"
PART_FILL = {"1": "#7a3412", "2": "#b0481a", "3": "#d9895f"}  # the accent from dark to light, one per part
SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'
MONO = 'font-family="DejaVu Sans Mono, monospace"'


def t(x, y, s, weight=400, fill=INK, anchor="start", font=SANS):
    return f'<text x="{x:.2f}" y="{y:.2f}" {font} font-size="{F}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'


def read_beats(path=REPO / "claims" / "beat-times.md"):
    """[(n, beat, part, minutes or None)] from the table's rows, in the talk's order."""
    rows = []
    for line in Path(path).read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 4 and cells[0].isdigit():
            m = re.fullmatch(r"(?:(\d+):)?(\d+):(\d\d)", cells[3])  # m:ss or h:mm:ss
            mins = int(m[1] or 0) * 60 + int(m[2]) + int(m[3]) / 60 if m else None
            rows.append((int(cells[0]), cells[1], cells[2], mins))
    if not rows:
        sys.exit("beats: no rows in claims/beat-times.md")
    check(rows)
    return rows


def check(rows):
    """The table must agree with its claims: C015's beat count and C097's beats placed. A strip that disagrees stops."""
    import json
    reg = json.loads((REPO / "claims" / "register.json").read_text())
    claims = {c["id"]: c for c in (reg["claims"] if isinstance(reg, dict) else reg)}
    heard = sum(1 for r in rows if r[3] is not None)
    if len(rows) != claims["C015"]["value"]["beats"] or heard != claims["C097"]["value"]["placed"]:
        sys.exit(f"beats: the table gives {len(rows)} beats, {heard} heard; C015 and C097 say otherwise")


def read_claims(path=REPO / "claims" / "talk-claims-per-beat.md"):
    """{beat: (hold, in part, not checked)} from the researcher's table for C099, checked against C099."""
    import json
    out = {}
    for line in Path(path).read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 7 and cells[2].isdigit():
            out[cells[0]] = (int(cells[3]), int(cells[4]), int(cells[5]))
    reg = json.loads((REPO / "claims" / "register.json").read_text())
    v = {c["id"]: c for c in (reg["claims"] if isinstance(reg, dict) else reg)}["C099"]["value"]
    if len(out) != v["beats_with_claims"] or sum(map(sum, out.values())) != v["per_beat_cells_sum"]:
        sys.exit(f"beats: the claims table gives {len(out)} beats, {sum(map(sum, out.values()))} cells; C099 says otherwise")
    return out


CLAIM_FILL = (INK, "#9aa3ad", None)  # hold, held in part, not checked (outlined)


def svg(w, h, body, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:g}mm" height="{h:g}mm" viewBox="0 0 {w:g} {h:g}" '
            f'role="img" aria-label="{label}">{body}</svg>\n')


def cell(x, y, w, h, part, heard):
    if heard:
        return f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" fill="{PART_FILL[part]}"/>'
    return f'<rect x="{x + .2:.2f}" y="{y + .2:.2f}" width="{w - .4:.2f}" height="{h - .4:.2f}" fill="{PAPER}" stroke="{MUTED}" stroke-width=".35" stroke-dasharray=".8 .6"/>'


def in_order(rows, length=164.0, claims=None):
    """Every beat one cell, parts apart, each part headed by its count of beats and of beats heard; with claims
    (read_claims), each beat's placed claims hang under its cell, one square each, by state."""
    gap, h, top = 3.0, 12.0, 6.0
    w = (length - 2 * gap) / len(rows)
    out, x, parts = [], 0.0, {}
    for i, (n, beat, part, mins) in enumerate(rows):
        if i and part != rows[i - 1][2]:
            x += gap
        parts.setdefault(part, [x, x, 0, 0])
        out.append(cell(x, top, w - .3, h, part, mins is not None))
        if claims and beat in claims:
            k = 0
            for state, n_ in enumerate(claims[beat]):
                for _ in range(n_):
                    yy = top + h + 1.2 + k * 2.0
                    if CLAIM_FILL[state]:
                        out.append(f'<rect x="{x + .3:.2f}" y="{yy:.2f}" width="{w - .9:.2f}" height="1.6" fill="{CLAIM_FILL[state]}"/>')
                    else:
                        out.append(f'<rect x="{x + .45:.2f}" y="{yy + .15:.2f}" width="{w - 1.2:.2f}" height="1.3" fill="none" stroke="{INK}" stroke-width=".3"/>')
                    k += 1
        p = parts[part]; p[1] = x + w; p[2] += 1; p[3] += mins is not None
        x += w
    for part, (x0, x1, n, heard) in parts.items():
        out.append(t(x0, 3.6, f"part {part}: {n} beats, {heard} heard", 800))
    heard = sum(1 for r in rows if r[3] is not None)
    foot = top + h + 5.2
    if claims:
        depth = max(sum(v) for v in claims.values()) * 2.0 + 2
        foot = top + h + depth + 4.4
        legend = [("held", INK), ("held in part", "#9aa3ad"), ("not checked", None)]
        lx = 0.0
        for name, fill in legend:
            out.append(f'<rect x="{lx:.2f}" y="{foot - 2.4:.2f}" width="3" height="1.6" fill="{fill or "none"}" stroke="{INK}" stroke-width="{0 if fill else .3}"/>')
            out.append(t(lx + 4, foot - .9, name, fill=MUTED))
            lx += 8 + len(name) * 1.72
        foot += 4.6
        out.append(t(0, foot, "under a beat: its placed claims (C099), each in the talk register's state at 18:20", fill=MUTED))
        foot += 4.6
        out.append(t(0, foot, "a claim on a slide that several beats show counts under each; 55 claims are unique (C039, C099)", fill=MUTED))
        foot += 4.6
    out.append(t(0, foot, f"{heard} of {len(rows)} beats heard (C097, on C015's beats); outlined: not reached", fill=MUTED))
    return svg(length, foot + 1.2, "".join(out), f"The talk's {len(rows)} beats in three parts, {heard} heard, the rest not reached")


def in_time(rows, length=164.0):
    """Each heard beat at the minute its block was first heard; the unheard after the recording's end."""
    heard = [r for r in rows if r[3] is not None]
    end = max(r[3] for r in heard)
    span = (int(end // 15) + 1) * 15  # the axis to the next quarter hour
    unheard = [r for r in rows if r[3] is None]
    tail_w = 30.0
    pad = 5.0  # room for the first tick's label
    axis_w = length - tail_w - pad - 8
    sx = lambda m: pad + m / span * axis_w
    cw, ch, base = 1.8, 2.6, 30.0
    out, stacks = [], {}
    for n, beat, part, m in heard:
        k = stacks.get(m, 0); stacks[m] = k + 1
        out.append(cell(sx(m) - cw / 2, base - (k + 1) * (ch + .4), cw, ch, part, True))
    for m in range(0, span + 1, 15):
        out.append(f'<line x1="{sx(m):.2f}" y1="{base + .4:.2f}" x2="{sx(m):.2f}" y2="{base + 1.6:.2f}" stroke="{INK}" stroke-width=".3"/>')
        out.append(t(sx(m), base + 5.2, f"{m} min", fill=MUTED, anchor="middle"))
    out.append(f'<line x1="{pad:.2f}" y1="{base + .4:.2f}" x2="{pad + axis_w:.2f}" y2="{base + .4:.2f}" stroke="{INK}" stroke-width=".35"/>')
    x0 = pad + axis_w + 10
    for i, (n, beat, part, m) in enumerate(unheard):
        out.append(cell(x0 + (i % 6) * (cw + .9), base - (i // 6 + 1) * (ch + .4), cw, ch, part, False))
    out.append(t(x0, base + 5.2, f"{len(unheard)} not reached", fill=MUTED))
    out.append(t(0, base + 10.4, "stacked: beats first heard in the same transcript block;", fill=MUTED))
    out.append(t(0, base + 14.4, "a tick is the block's stamp, not the second a beat began (C097)", fill=MUTED))
    return svg(length, base + 15.6, "".join(out), "The talk's beats placed at the minute each was first heard, stacked where they share a block; the unreached after the end")


if __name__ == "__main__":
    rows = read_beats()
    length = float(sys.argv[3]) if len(sys.argv) > 3 else 164.0
    Path(sys.argv[1]).write_text(in_order(rows, length, read_claims()))
    Path(sys.argv[2]).write_text(in_time(rows, length))
