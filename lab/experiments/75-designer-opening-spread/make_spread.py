#!/usr/bin/env python3
"""LAB 75: the opening spread as two placed pages (OS3, conductor 091; the editor's brief 44: "the formatting is all
over the place"). Each page is one drawing the size of the text block, so the build places it whole, not flowed.

    python3 lab/experiments/75-designer-opening-spread/make_spread.py

Every word is read at build from manuscript/rc2/150/00-start-here.md (read, never edited) and checked there; the
writer's words stay as they are. Page one: the headline, the narrator's opening with one narrator mark in the book's
serif at its size, ten cards in two rows of five (each member's figure, name and hello; security greyed as the empty
chair), and the closing line in italics. No id or hash drawn; the feedback address is never drawn (FB2: print only,
security's pre-review of 03:58), so the invitation stays text in the build.
"""
import re, sys, textwrap
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'
SERIF = 'font-family="Georgia, \'DejaVu Serif\', serif"'
SRC = (REPO / "manuscript" / "rc2" / "150" / "00-start-here.md").read_text()
W, H = 156.0, 200.0
PT = 0.3528  # mm per point


def t(x, y, s, weight=400, fill=mc.INK, anchor="start", size=3.18, fam=SANS, italic=False):
    st = ' font-style="italic"' if italic else ""
    return (f'<text x="{x:.2f}" y="{y:.2f}" {fam} font-size="{size:.2f}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}"{st}>{escape(str(s), quote=False)}</text>')


def strip_md(s):
    return re.sub(r"\*\*?([^*]+)\*\*?", r"\1", s).strip()


def parse():
    lines = SRC.splitlines()
    title = next(l[2:] for l in lines if l.startswith("# "))
    head = next(l[3:] for l in lines if l.startswith("## "))
    i0 = lines.index(f"## {head}")
    i1 = next(i for i, l in enumerate(lines) if l.startswith("**Figure:**"))
    opening = [strip_md(l.replace("**Narrator.**", "")) for l in lines[i0 + 1:i1] if l.startswith("**Narrator.**")]
    hellos = [(m.group(1), m.group(2)) for m in (re.match(r"^\*\*([\w-]+):\*\* (.+)$", l) for l in lines) if m and m.group(1) != "Figure"]
    closing = next(l.strip("*") for l in lines if l.startswith("*And one chair"))
    if len(opening) != 3 or len(hellos) != 9 or {n.lower() for n, _ in hellos} != set(mc.CAST):
        sys.exit("make_spread: 00's opening or hellos are not as the spread expects")
    return title, head, opening, hellos, closing


def page_one():
    title, head, opening, hellos, closing = parse()
    out = [f'<rect x="0" y="0" width="13" height="1.2" fill="{mc.ACCENT}"/>',
           t(0, 9.4, title, 800, mc.INK, size=17 * PT), t(0, 17.6, head, 700, mc.INK, size=12 * PT)]
    # the narrator's opening: one mark, the book's serif at its size (10 pt, leading 1.42)
    size, lead = 10 * PT, 10 * PT * 1.42
    out.append(f'<g transform="translate(0 21.4) scale(.28)">{mc.editor_figure("A")}</g>')
    y = 25.8
    for k, p in enumerate(opening):
        for j, r in enumerate(textwrap.wrap(p, 73)):
            out.append(t(14, y, r, 700 if (k == 0 and j == 0 and False) else 400, mc.INK, size=size, fam=SERIF))
            y += lead
        y += 1.6
    # ten cards in two rows of five: the nine with their hellos, and security's empty chair
    cw, ch, gap = 30.0, 40.0, 1.5
    y0 = y + 2.6
    cards = [(n, h) for n, h in hellos] + [("security", None)]
    if "*Dramatised.*" not in SRC.split("**Narrator.** Throughout")[0]:
        sys.exit("make_spread: the hellos are no longer marked as dramatised in 00")
    out.append(t(W, y0 - 1.6, "DRAMATISED", 600, "#6b7280", "end"))
    for i, (name, hello) in enumerate(cards):
        x = (i % 5) * (cw + gap)
        cy = y0 + (i // 5) * (ch + gap)
        m = name.lower()
        empty = m == "security"
        lead_c = m == "conductor"
        out.append(f'<rect x="{x + .3:.2f}" y="{cy:.2f}" width="{cw - .6:.2f}" height="{ch:.2f}" rx="1.6" '
                   f'fill="{mc.FILL if empty else ("#f6e1d4" if lead_c else "#fff")}" stroke="{mc.MUTED if empty else (mc.ACCENT if lead_c else mc.FILL2)}" '
                   f'stroke-width="{.5 if lead_c else .35}"' + (' stroke-dasharray="1.6 1"' if empty else "") + "/>")
        if empty:
            src = (REPO / "lab" / "characters" / "cast" / "security-worried.svg").read_text()
            inner = src[src.index(">", src.index("<svg")) + 1: src.rindex("</svg>")]
            out.append(f'<g transform="translate({x + cw / 2 - 7.2:.2f} {cy + 1.4:.2f}) scale(.72)" opacity=".38">{inner}</g>')
        else:
            out.append(f'<g transform="translate({x + cw / 2 - 7.2:.2f} {cy + 1.4:.2f}) scale(.36)">{mc.figure(m, "happy")}</g>')
        out.append(t(x + cw / 2, cy + 22.4, m, 800, mc.MUTED if empty else (mc.ACCENT if lead_c else mc.INK), "middle"))
        words = hello if hello else "the empty chair"
        for j, r in enumerate(textwrap.wrap(words, 17)):
            out.append(t(x + cw / 2, cy + 26.8 + j * 3.9, r, 400, mc.MUTED, "middle", italic=empty))
    y = y0 + 2 * ch + gap + 6
    for j, r in enumerate(textwrap.wrap(closing, 73)):
        out.append(t(0, y + j * lead, r, 400, mc.INK, size=size, fam=SERIF, italic=True))
    end = y + lead * len(textwrap.wrap(closing, 73))
    if end > H:
        sys.exit(f"make_spread: page one runs to {end:.1f} mm, past the {H} mm text block")
    return mc.svg(W, H, "".join(out), f"{title}: {head} The narrator's opening, the nine members' cards with their hellos, security's empty chair, and the closing line")


SHOTS = REPO / "index" / "talk-site" / "shots"
CLEARED = ["index.jpg", "talk__slides__loop.jpg", "talk.jpg", "studio-ports__abp-review__masked.jpg", "articles__the-night-hour-by-hour.jpg"]


def figures():
    """00's Figure lines in order, each with the image its brief names (only the five security cleared by name)."""
    out, lines = [], SRC.splitlines()
    for i, l in enumerate(lines):
        if l.startswith("**Figure:**"):
            brief = next((x for x in lines[i + 1:i + 6] if x.startswith("`%% figure brief")), "")
            img = re.search(r"index/talk-site/shots/([\w.-]+\.jpg)", brief)
            out.append((l.replace("**Figure:**", "").strip(), img.group(1) if img else None))
    return out


def shot(name, x, y, w, aspect=1.6):
    import base64
    if name not in CLEARED:
        sys.exit(f"make_spread: {name} is not one of the five cleared by name")
    h = w / aspect
    data = base64.b64encode((SHOTS / name).read_bytes()).decode()
    return (f'<rect x="{x - .2:.2f}" y="{y - .2:.2f}" width="{w + .4:.2f}" height="{h + .4:.2f}" rx=".8" fill="none" stroke="{mc.FILL2}" stroke-width=".4"/>'
            f'<image x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" preserveAspectRatio="xMidYMid slice" href="data:image/jpeg;base64,{data}"/>'), h


def g_head(m, x, y):
    return f'<g transform="translate({x:.2f} {y:.2f}) scale(.13)">{mc.head(m)}</g>'


def caption(x, y, s, width_chars):
    rows = textwrap.wrap(s[0].upper() + s[1:], width_chars)
    return "".join(t(x, y + j * 3.9, r, 400, mc.MUTED) for j, r in enumerate(rows)), len(rows) * 3.9


def page_two():
    lines = SRC.splitlines()
    heads = [l[3:] for l in lines if l.startswith("## ")]
    nums = [re.match(r"^- \*\*([^*]+)\*\*: (.+)$", l) for l in lines]
    nums = [(m.group(1), m.group(2)) for m in nums if m]
    parts = [re.match(r"^(\d)\. \*\*([^*]+)\*\* (.+)$", l) for l in lines]
    parts = [(m.group(1), m.group(2), m.group(3)) for m in parts if m]
    read = next(strip_md(l.replace("**Narrator.**", "")) for l in lines if l.startswith("**Narrator.** Read it in order"))
    figs = figures()
    if len(nums) != 4 or len(parts) != 5 or len(figs) != 7:
        sys.exit("make_spread: 00's numbers, parts or figures are not as page two expects")
    out, y = [], 4.6
    # the day in four numbers, as a strip of four
    out.append(t(0, y, heads[1], 800, mc.INK, size=12 * PT)); y += 3
    bw = (W - 3 * 2) / 4
    for i, (n, label) in enumerate(nums):
        x = i * (bw + 2)
        out.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{bw:.2f}" height="18" rx="1.6" fill="{mc.FILL}"/>'
                   + t(x + 3, y + 8.4, n, 800, mc.ACCENT if i == 3 else mc.INK, size=7.4))
        for j, r in enumerate(textwrap.wrap(label, 21)):
            out.append(t(x + 3, y + 12.6 + j * 3.6, r, 400, mc.MUTED))
    y += 18 + 8
    # what a factory of agents made in a day: three shots in a row, captions under
    out.append(t(0, y, heads[2], 800, mc.INK, size=12 * PT)); y += 3
    sw, hmax = (W - 2 * 3) / 3, 0
    for i, (cap, img) in enumerate(figs[1:4]):
        x = i * (sw + 3)
        s_, h = shot(img, x, y, sw, 1.9)
        c, ch = caption(x, y + h + 4.2, cap, 30)
        out.append(s_ + c); hmax = max(hmax, h + 4.2 + ch)
    y += hmax + 2
    # the house on the left, the policy and the night-log cards stacked to its right
    # the house, compact: LAB 47's rooms and members (its ROOMS, so its placements and their checks are the same),
    # redrawn at this size so its type stays at 9 pt; heads, not figures
    sys.path.insert(0, str(REPO / "lab" / "experiments" / "47-designer-the-house"))
    import make_house as mh
    hw, sx = 84.0, 84.0 / 155
    floors = sorted({r[5] for r in mh.ROOMS})
    fh = {f: (11.6 if f != floors[-1] else 7.6) for f in floors}
    fy, acc = {}, y + 8
    for f in floors:
        fy[f] = acc; acc += fh[f]
    out.append(f'<path d="M0 {y + 8:.2f} L{hw / 2:.2f} {y:.2f} L{hw} {y + 8:.2f} Z" fill="{mc.FILL}" stroke="{mc.INK}" stroke-width=".45"/>'
               + t(hw / 2, y + 7, "the talk's repository, as a house", 400, mc.INK, "middle"))
    short = {"the story and the look": "story and look", "the evidence room": "evidence", "the guard room": "guard room"}
    for title, note, members, _, x, ry, w, h in mh.ROOMS:
        X, Y, Wd, Hd = (x - 2) * sx + .5, fy[ry], w * sx, fh[ry]
        guard = title == "the guard room"
        out.append(f'<rect x="{X:.2f}" y="{Y:.2f}" width="{Wd:.2f}" height="{Hd:.2f}" fill="{mc.FILL if guard else "#fff"}" stroke="{mc.INK}" stroke-width=".4"' + (' stroke-dasharray="1.6 1"' if guard else "") + "/>")
        name = short.get(title, title.replace("the ", "", 1))
        out.append(t(X + 1.2, Y + 3.5, name, 400, mc.MUTED))
        for k, m in enumerate(members):
            label = "empty chair" if m == "security" else m
            if Hd < 10:  # the foundations: the name beside the title
                out.append(t(X + Wd / 2, Y + 3.5, label, 700, mc.INK, "middle"))
            else:
                cx = X + Wd * (k + 1) / (len(members) + 1)
                yy = Y + (7.4 if len(members) > 1 and k % 2 == 0 else 10.2) if len(members) > 1 else Y + 8.6
                out.append(t(cx, yy, label, 400 if m == "security" else 700, mc.MUTED if m == "security" else mc.INK, "middle"))
    hh = acc - y
    c, ch = caption(0, y + hh + 4.2, figs[4][0], 52)
    out.append(c)
    rx, rw, yy = hw + 4, W - hw - 4, y
    for cap, img in figs[5:7]:  # a small card each: the shot, its caption beside it
        iw = 36.0
        s_, h = shot(img, rx, yy, iw)
        c, ch2 = caption(rx + iw + 2.4, yy + 3.2, cap, 18)
        out.append(s_ + c); yy += max(h, ch2) + 4
    y = max(y + hh + 4.2 + ch, yy) + 3.4
    # the story, in five parts
    out.append(t(0, y, heads[3], 800, mc.INK, size=12 * PT)); y += 6
    for n, lead, rest in parts:
        out.append(f'<circle cx="2.6" cy="{y - 1.1:.2f}" r="2.5" fill="{mc.ACCENT}"/>' + t(2.6, y, n, 800, "#fff", "middle"))
        rows = textwrap.wrap(f"{lead} {rest}", 94)
        first = rows[0][len(lead):]
        out.append(f'<text x="7" y="{y:.2f}" {SANS} font-size="3.18" fill="{mc.INK}"><tspan font-weight="800">{escape(lead, quote=False)}</tspan>{escape(first, quote=False)}</text>')
        for j, r in enumerate(rows[1:], 1):
            out.append(t(7, y + j * 3.9, r, 400, mc.INK))
        y += 3.9 * len(rows) + .8
    out.append(t(0, y + 2.6, read, 400, mc.INK, size=10 * PT, fam=SERIF))
    end = y + 4
    if end > H:
        sys.exit(f"make_spread: page two runs to {end:.1f} mm, past the {H} mm text block")
    return mc.svg(W, H, "".join(out), "The opening spread, page two: the day in four numbers, what a factory of agents made in a day, the house, and the story in five parts")


def main():
    two = page_two()
    svg = page_one()
    if re.search(r">[^<]*\b(C\d{3}|[0-9a-f]{7,})\b", svg) or "@" in re.sub(r"<[^>]+>", "", svg):
        sys.exit("make_spread: an id, a hash or an address is drawn")
    (HERE / "spread-page-1.svg").write_text(svg)
    sys.path.insert(0, str(REPO / "publishing"))
    import edition
    why = edition.unsafe_svg(two)
    if why or re.search(r">[^<]*\b(C\d{3}|[0-9a-f]{7,})\b", re.sub(r'href="[^"]+"', "", two)) or "@" in re.sub(r"<[^>]+>", "", two):
        sys.exit(f"make_spread: page two refused: {why or 'an id, a hash or an address is drawn'}")
    (HERE / "spread-page-2.svg").write_text(two)
    print("written spread-page-1.svg, spread-page-2.svg")


if __name__ == "__main__":
    main()
