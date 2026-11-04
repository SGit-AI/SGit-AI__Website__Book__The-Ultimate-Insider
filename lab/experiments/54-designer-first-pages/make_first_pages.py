#!/usr/bin/env python3
"""LAB 54: three of the front pages' empty boxes (the conductor's 079, LY1: the editor reads from the front).

    python3 lab/experiments/54-designer-first-pages/make_first_pages.py

- wake-records.svg (06, line 56): each member's wake records on the day, from the conductor's to motion's, as bars with
  the member's head, its count at the bar's end and the total, read from C022 at build. Counts on the card only.
- member-folder.svg (04, line 54): one member's folder opened, this book's writer's: its page of rules, its policy, its
  status, its notes and its session records, each with what it is for, Markdown and JSON told apart. File and folder
  names only, read from the folder at build; sessions/ and the key files are left out (their names and contents are
  ids), as security's pre-review asks.
- two-voices.svg (00b, line 17): the narrator, looking back, beside an agent, on the day, as the page sets them.
No register id inside a drawing; no caption drawn in.
"""
import json, re, sys
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'
SERIF = 'font-family="Bitstream Charter, Charter, DejaVu Serif, Georgia, serif"'
MONO = 'font-family="DejaVu Sans Mono, monospace"'


def t(x, y, s, weight=400, fill=mc.INK, anchor="start", size=3.18, font=SANS, extra=""):
    return (f'<text x="{x:.2f}" y="{y:.2f}" {font} font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}"{extra}>{escape(str(s), quote=False)}</text>')


def wake_records():
    reg = {c["id"]: c for c in json.loads((REPO / "claims" / "register.json").read_text())["claims"]}
    c = reg["C022"]
    if c["state"] != "checked":
        sys.exit("make_first_pages: C022 is not checked")
    v = c["value"]
    by = sorted(v["by_member"].items(), key=lambda kv: -kv[1])
    if sum(n for _, n in by) != v["records"] or by[0][0] != "conductor" or by[-1][0] != "motion":
        sys.exit("make_first_pages: C022's counts do not add up, or do not run from the conductor's to motion's")
    x0, x1, rh, out = 33.0, 146.0, 7.2, []
    top = max(n for _, n in by)
    for k, (m, n) in enumerate(by):
        y = 2 + k * rh
        w = (x1 - x0) * n / top
        out.append(f'<g transform="translate(0 {y - 1.2:.2f}) scale(.3)">{mc.head(m)}</g>'
                   + t(13.4, y + 4.2, m, 700)
                   + f'<rect x="{x0}" y="{y}" width="{w:.2f}" height="4.6" rx="1" fill="{mc.CAST[m][0]}"/>'
                   + t(x0 + w + 1.6, y + 3.8, n, 800))
    H = 2 + len(by) * rh
    out.append(mc.line(x0, H + 1, x1 + 8, H + 1, mc.FILL2, .4) + t(x1 + 8, H + 6.4, f"{v['records']} in all", 800, mc.ACCENT, "end", 4.2))
    return mc.svg(156, round(H + 8, 1), "".join(out), f"Each member's wake records on the day, from the conductor's to motion's, {v['records']} in all")


FOLDER = [("ROLE.md", "md", "its page of rules: who it is and what it does"),
          ("policy.json", "json", "its policy: what it may write"),
          ("status.json", "json", "its status: what it is doing now"),
          ("debriefs/", "md", "its notes, one for each round of work"),
          ("wakes/", "json", "its session records, one for each wake")]


def member_folder():
    root = REPO / "team" / "writer"
    for name, _, _ in FOLDER:
        if not (root / name.rstrip("/")).exists():
            sys.exit(f"make_first_pages: team/writer has no {name}")
    out = [mc.path("M2 4 h22 l3 3.4 h30 v6.2 h-55 z", mc.FILL, mc.INK, .5) + t(6, 11.2, "team/writer/", 800, mc.INK, font=MONO)]
    y = 21.0
    for name, kind, what in FOLDER:
        out.append(mc.line(8, y - 8, 8, y - 1.4, mc.FILL2, .5) + mc.line(8, y - 1.4, 13, y - 1.4, mc.FILL2, .5))
        tag_fill = mc.INK if kind == "json" else "#fff"
        out.append(f'<rect x="15" y="{y - 4.6:.2f}" width="9.6" height="4.8" rx="1" fill="{tag_fill}" stroke="{mc.INK}" stroke-width=".4"/>'
                   + t(19.8, y - 1.2, kind, 700, "#fff" if kind == "json" else mc.INK, "middle", 3.18)
                   + t(28, y - 1, name, 700, mc.INK, font=MONO) + t(66, y - 1, what, 400, mc.MUTED))
        y += 8.4
    out.append(t(15, y + 1.2, "md: written for people to read; json: data, for the team's tools and pages to read", 400, mc.MUTED))
    return mc.svg(156, round(y + 3, 1), "".join(out), "One member's folder opened: its page of rules, its policy, its status, its notes and its session records, Markdown and JSON told apart")


def two_voices():
    page = (REPO / "manuscript" / "rc2" / "150" / "00b-who-is-telling-this-story.md").read_text()
    if "two voices on the page" not in page:
        sys.exit("make_first_pages: 00b no longer asks for the two voices")
    out = []
    for i, (who, label, note) in enumerate([("narrator", "Narrator.", "looking back, in his own words"),
                                            ("dev", "dev:", "on the day, in the present tense")]):
        x = i * 79
        out.append(f'<rect x="{x + .3:.1f}" y=".3" width="76" height="30" rx="2" fill="#fff" stroke="{mc.FILL2}" stroke-width=".45"/>')
        if who == "narrator":
            head = (f'<circle cx="20" cy="17" r="8.6" fill="{mc.FILL}" stroke="{mc.INK}" stroke-width="{mc.SW * 1.6}"/>'
                    f'<g transform="translate(0 -.8)">{mc.face("happy")}</g>')
        else:
            head = mc.head(who)
        out.append(f'<g transform="translate({x + 1:.1f} 1.6) scale(.38)">{head}</g>')
        out.append(t(x + 17, 8.6, label, 800, mc.INK, font=SERIF if who == "narrator" else SANS, size=3.6))
        for k, w in enumerate([52, 48, 34]):
            out.append(f'<rect x="{x + 17}" y="{12 + k * 3.6:.1f}" width="{w}" height="1.5" rx=".7" fill="{mc.FILL2}"/>')
        out.append(t(x + 5, 27.4, note, 400, mc.MUTED))
    return mc.svg(156, 31, "".join(out), "Two voices on the page: the narrator, looking back, and an agent, on the day")


if __name__ == "__main__":
    for name, svg in (("wake-records.svg", wake_records()), ("member-folder.svg", member_folder()), ("two-voices.svg", two_voices())):
        if re.search(r">[^<]*\bC\d{3}\b", svg) or "session_" in svg:
            sys.exit(f"make_first_pages: {name} draws an id")
        (HERE / name).write_text(svg)
    print("written wake-records.svg, member-folder.svg, two-voices.svg")
