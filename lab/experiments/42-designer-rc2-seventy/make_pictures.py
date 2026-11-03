#!/usr/bin/env python3
"""LAB 42: RC2's pictures for the seventy (manuscript/rc2/70/, read only) that are new, not the thirty's drawings again.

    python3 lab/experiments/42-designer-rc2-seventy/make_pictures.py <read-only clone of the talk's repository>
- ch10-hold-file.svg: the hold file as a page, its title line and its last line large ("No member lifts it."), both read
  at build from team/conductor/HOLD.md at 298be4e (with git, read only), its bold and bullet marks dropped as the
  chapter's record line says; the lines between drawn as grey bars, not text (C006).
- ch12-state-machine.svg: the day as three states, running, held, released; "anyone" on the arrow into held, "the
  editor only" on the arrow out; released dashed, never reached by 298be4e (C024).
No number is printed but the hold's time and ids. One SVG unit a millimetre, sizes stated, text 9 pt.
"""
import json, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

F = 3.18
SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'
REG = {c["id"]: c for c in json.loads((REPO / "claims" / "register.json").read_text())["claims"]}


def t(x, y, s, weight=400, fill=mc.INK, anchor="start", size=F):
    return f'<text x="{x:.2f}" y="{y:.2f}" {SANS} font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'


def hold_file(clone):
    for cid in ("C006", "C024"):
        if REG[cid]["state"] != "checked":
            sys.exit(f"make_pictures: {cid} is {REG[cid]['state']}")
    text = subprocess.run(["git", "-C", clone, "show", "298be4e:team/conductor/HOLD.md"], capture_output=True, text=True, check=True).stdout
    title = text.splitlines()[0].lstrip("# ").strip()
    m = re.search(r"\*\*What lifts it:\*\*\s*(.+?)\s*(No member lifts it\.)", text)
    if not m or not title.startswith("HOLD:"):
        sys.exit("make_pictures: the hold file's title or its 'What lifts it' line is not as expected")
    lifts, last = m.group(1), m.group(2)
    x, w = 22, 120
    out = [f'<path d="M{x} 2 h{w - 12} l12 12 v76 h-{w} z" fill="#fff" stroke="{mc.INK}" stroke-width=".6"/>',
           f'<path d="M{x + w - 12} 2 v12 h12" fill="none" stroke="{mc.INK}" stroke-width=".5"/>']
    head, rest = title.split(";", 1)
    out.append(t(x + 7, 15, head + ";", 800, mc.ACCENT, size=4.6) + t(x + 7, 21.4, rest.strip(), 800, mc.ACCENT, size=4.6))
    for k, (dy, ww) in enumerate([(30, 92), (35, 70), (41, 100), (46, 96), (51, 60), (57, 98), (62, 84)]):
        out.append(f'<rect x="{x + 7}" y="{dy}" width="{ww}" height="2" rx="1" fill="{mc.FILL2}"/>')
    out.append(t(x + 7, 72, "What lifts it: " + lifts, 400, mc.INK))
    out.append(t(x + 7, 84.6, last, 800, mc.INK, size=7.4))
    out.append(t(x, 97.4, "team/conductor/HOLD.md at 298be4e, written 18:44:13 (C006); never lifted that day (C024)", 400, mc.MUTED))
    return mc.svg(164, 100, "".join(out), "The hold file as a page: its title, and its last line large: No member lifts it.")


def state_machine():
    if REG["C024"]["value"]["lifted_by_298be4e"] is not False:
        sys.exit("make_pictures: C024 no longer says the hold was not lifted")
    out = []
    defs = (f'<defs><marker id="s" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="{mc.INK}"/></marker>'
            f'<marker id="s2" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="{mc.MUTED}"/></marker></defs>')
    # running: where the day spent its time; held: where it ended; released: drawn, never reached
    out.append(f'<ellipse cx="26" cy="24" rx="22" ry="15" fill="{mc.FILL}" stroke="{mc.INK}" stroke-width=".7"/>'
               + t(26, 25.2, "running", 800, mc.INK, "middle", 4.2) + t(26, 31, "the day", 400, mc.MUTED, "middle"))
    out.append(f'<ellipse cx="88" cy="24" rx="17" ry="13" fill="#fff" stroke="{mc.ACCENT}" stroke-width="1.2"/>'
               + t(88, 25.2, "held", 800, mc.ACCENT, "middle", 4.2) + t(88, 31, "from 18:44", 400, mc.MUTED, "middle"))
    out.append(f'<ellipse cx="142" cy="24" rx="17" ry="13" fill="#fff" stroke="{mc.MUTED}" stroke-width=".6" stroke-dasharray="1.6 1.2"/>'
               + t(142, 25.2, "released", 800, mc.MUTED, "middle", 4.2) + t(142, 31, "not reached", 400, mc.MUTED, "middle"))
    out.append(f'<path d="M49 24 H69" stroke="{mc.INK}" stroke-width=".8" marker-end="url(#s)"/>' + t(59, 19.6, "anyone", 700, mc.INK, "middle"))
    out.append(f'<path d="M106 24 H123" stroke="{mc.MUTED}" stroke-width=".8" stroke-dasharray="1.6 1.2" marker-end="url(#s2)"/>'
               + t(114.5, 10.6, "the editor", 700, mc.INK, "middle") + t(114.5, 15, "only", 700, mc.INK, "middle"))
    out.append(t(0, 46, "the hold at 18:44:13 (C006); by the end of the day's record it was not lifted (C024)", 400, mc.MUTED))
    return mc.svg(164, 48, defs + "".join(out), "The day as three states: running, held, released; anyone may hold, only the editor releases; released never reached")


if __name__ == "__main__":
    clone = sys.argv[1]
    files = {"ch10-hold-file.svg": hold_file(clone), "ch12-state-machine.svg": state_machine()}
    for name, svg in files.items():
        (HERE / name).write_text(svg)
    print("written " + ", ".join(files))
