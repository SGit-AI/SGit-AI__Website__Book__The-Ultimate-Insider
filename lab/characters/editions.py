#!/usr/bin/env python3
"""The cast on the editions' pages (ED1 round 1): an on-stage marker per page, and a head for every speaker.

    python3 lab/characters/editions.py
Reads manuscript/editions/<NN>/*.md (read only). For each page with a "**Cast bar:**" line it writes
lab/characters/editions/marker-<NN>-<page>.svg: the narrator's head first, then the nine in the order they came on
stage, the present ones lit. Who is present is read from the line's names; where the line gives a time instead
("from five in the morning"), from each member's first commit (C011, in claims/scorecard-values.md). It also writes
lab/tools/book/speakers.css: a 6 mm head before each `.speaker` block, by data-speaker and, where it names one of
the four moods, data-mood, as data URIs so the build embeds them. Nothing here is text inside a drawing.
"""
import base64, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(HERE))
import make_cast as mc  # noqa: E402

OUT = HERE / "editions"


def first_commits():
    rows = {}
    for line in (REPO / "claims" / "scorecard-values.md").read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 7 and cells[0] in mc.CAST:
            rows[cells[0]] = cells[1].split()[0]
    return rows


FIRST = first_commits()
ARRIVAL = sorted(mc.CAST, key=lambda m: FIRST[m])
CLOCK_WORDS = {"five in the morning": "05:00", "about two": "02:00", "midnight": "00:00"}


def present_from(bar, previous):
    """(narrator lit, agents lit) for one cast-bar line; previous is the page before's set (for 'as page N')."""
    low = bar.lower()
    narrator = "editor" in low and "editor's chair is empty" not in low
    if "all nine" in low:
        return narrator, set(mc.CAST)
    if "your own" in low or "fade" in low:
        return False, set()
    agents = {m for m in mc.CAST if m in low}
    if low.startswith("as page"):
        agents |= previous
    m = re.search(r"(six|five|four|seven|eight) agents", low)
    if m:  # 'six agents ... from five in the morning': those whose first commit came before that time (C011)
        at = next((v for k, v in CLOCK_WORDS.items() if k in low), "23:59")
        agents = {a for a in mc.CAST if FIRST[a] <= at}
        want = ["four", "five", "six", "seven", "eight"].index(m.group(1)) + 4
        if len(agents) != want:
            sys.exit(f"editions: {bar!r} says {want}, C011 gives {len(agents)} before {at}")
    return narrator, agents


def narrator_head(lit):
    g = mc.editor_figure("A")
    head = re.search(r'<circle cx="20" cy="18" r="8.6"[^>]*/>(<g transform="translate\(0 .2\)">.*?</g>)', g).group(0)
    if not lit:
        head = f'<circle cx="20" cy="18" r="8.6" fill="#fff" stroke="{mc.FILL2}" stroke-width="{mc.SW * 1.6}"/>'
    return head


def marker(narrator, agents, size=7.0):
    s, step = size / 20.0, size * 1.25
    out = [f'<g transform="translate({-10 * s:.2f} {-4 * s:.2f}) scale({s:.4f})">{narrator_head(narrator)}</g>',
           f'<line x1="{step - size * .12:.2f}" y1=".6" x2="{step - size * .12:.2f}" y2="{23 * s - .6:.2f}" stroke="{mc.FILL2}" stroke-width=".3"/>']
    for i, m in enumerate(ARRIVAL, 1):
        out.append(f'<g transform="translate({i * step + 1.2 - 10 * s:.2f} {-4 * s:.2f}) scale({s:.4f})">{mc.head(m, m in agents)}</g>')
    who = (["the narrator"] if narrator else []) + [m for m in ARRIVAL if m in agents]
    return mc.svg(round(10 * step + 1.2 - size * .25, 2), round(23 * s, 2), "".join(out), "On stage now: " + (", ".join(who) or "nobody yet"))


def speakers_css():
    def uri(svg):
        return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()
    rules = [".speaker { position: relative; padding-left: 8mm; min-height: 7mm; }",
             ".speaker::before { content: ''; position: absolute; left: 0; top: .1em; width: 6mm; height: 7.5mm; background-size: contain; background-repeat: no-repeat; }"]
    for m in ["narrator"] + list(mc.CAST):
        for mood in mc.MOODS:
            body = mc.editor_figure("A", mood) if m == "narrator" else mc.figure(m, mood)
            svg = mc.svg(20, 25, f'<g transform="scale(.5)">{body}</g>', f"{m}, {mood}")
            sel = f'.speaker[data-speaker="{m}"]' + ("" if mood == "happy" else f'[data-mood="{mood}"]')
            rules.append(f'{sel}::before {{ background-image: url("{uri(svg)}"); }}')
    rules += [
        "/* one head per run (the editor, 2 November 2026, conductor__044): a block that follows the same speaker shows no head,",
        "   and for the narrator no repeated name either; an agent keeps its name, since hiding it would leave its stage words",
        "   without a speaker. The indent stays, so the run reads as one passage. */",
        ".speaker.same-speaker::before { background-image: none !important; content: none; }",
        '.speaker.same-speaker[data-speaker="narrator"] > p:first-child > strong:first-child { display: none; }',
    ]
    head = ("/* lab/tools/book/speakers.css: written by lab/characters/editions.py (the designer's, ED1 round 1).\n"
            "   A 6 mm head of the speaker before each .speaker block, by data-speaker; the mood's face where data-mood is\n"
            "   one of the four moods (happy, worried, stressed, unhappy), the happy face otherwise. */\n")
    return head + "\n".join(rules) + "\n"


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    n = 0
    for ed in sorted((REPO / "manuscript" / "editions").iterdir()):
        if not ed.is_dir():
            continue
        prev = set()
        for page in sorted(ed.glob("*.md")):
            m = re.search(r"^\*\*Cast bar:\*\*\s*(.+)$", page.read_text(), re.M)
            if not m:
                continue
            narrator, agents = present_from(m.group(1), prev)
            prev = agents
            (OUT / f"marker-{ed.name}-{page.stem}.svg").write_text(marker(narrator, agents))
            n += 1
            print(f"{ed.name}/{page.stem}: narrator {'lit' if narrator else 'out'}, {len(agents)} agents | {m.group(1)[:60]}")
    (REPO / "lab" / "tools" / "book" / "speakers.css").write_text(speakers_css())
    print(f"written {n} markers and lab/tools/book/speakers.css")
