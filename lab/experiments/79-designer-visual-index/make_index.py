#!/usr/bin/env python3
"""LAB 79: the visual index (PEN1 note 7, the editor: "We kinda need an (visual) index here (or on next page)").
One placed page the size of the text block (156 by 200 mm), as the spread and the part pages are: the whole book as
one bar, its length in pages split by part and chapter, then each part with its chapters and the page each starts on.

    python3 lab/experiments/79-designer-visual-index/make_index.py [--chapters <build's chapters JSON> [--pages <its page count>]]

Read at build, never edited: the order from manuscript/editions/rc2-150/Book.txt, each title from its chapter's first
heading, the five parts from 00's "The story, in five parts" (as LAB 78 reads them). With --chapters (the JSON
publishing/build_book.py writes beside its PDF) the bar is drawn to the pages and every page number is printed, each
as right-aligned text at x 156, the shape the publisher's build already refreshes on the spread (its 067). Without it
the bar is drawn one unit per chapter and no number is printed.
Writes index.svg.
"""
import json, re, sys, textwrap
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
sys.path.insert(0, str(REPO / "lab" / "experiments" / "78-designer-part-pages"))
import make_cast as mc  # noqa: E402
import make_parts as mp  # noqa: E402

SANS, SERIF, PT = mp.SANS, mp.SERIF, mp.PT
W, H = 156.0, 200.0
BOOK = REPO / "manuscript" / "editions" / "rc2-150" / "Book.txt"
# Where each part starts: its first chapter, as the part pages are placed in Book.txt ("#! part-page:")
FIRST = {}
TINT = ["#f6e3da", "#ecc6b3"]  # two tints of the accent, alternating chapter by chapter inside a part


def t(x, y, s, weight=400, fill=mc.INK, size=3.18, fam=SANS, anchor="", extra=""):
    a = f' text-anchor="{anchor}"' if anchor else ""
    return (f'<text x="{x:.2f}" y="{y:.2f}" {fam} font-size="{size:.2f}" font-weight="{weight}" fill="{fill}"{a}{extra}>'
            f'{escape(str(s), quote=False)}</text>')


def chapters():
    """[(file, title, part or None)] in Book.txt order; part is 1 to 5, None for what is before and after."""
    text = BOOK.read_text()
    for l in text.splitlines():
        m = re.match(r"^#! part-page: \.\./\.\./rc2/150/(\S+) \| .*part-(\d)\.svg$", l)
        if m:
            FIRST[m.group(1)] = int(m.group(2))
    if sorted(FIRST.values()) != [1, 2, 3, 4, 5]:
        sys.exit("make_index: Book.txt no longer places five part pages")
    out, part, back = [], None, False
    for l in text.splitlines():
        if l.startswith("# Back matter"):
            back = True
        m = re.match(r"^\.\./\.\./rc2/150/(\S+\.md)$", l)
        if not m:
            continue
        f = m.group(1)
        if f in FIRST:
            part = FIRST[f]
        if back:
            part = None
        head = re.search(r"^# (.+)$", (BOOK.parent / l).read_text(), re.M)
        if not head:
            sys.exit(f"make_index: {f} has no title")
        out.append((f, head.group(1).strip(), part))
    return out


def main():
    pages = {}
    if "--chapters" in sys.argv:
        js = json.loads(Path(sys.argv[sys.argv.index("--chapters") + 1]).read_text())
        pages = {c["file"]: c["page"] for c in js["chapters"]}
        total = js.get("pages") or 0
        if "--pages" in sys.argv:
            total = int(sys.argv[sys.argv.index("--pages") + 1])
    chs = chapters()
    if chs[0][0].startswith("00-"):
        chs = chs[1:]  # 00 is the spread this page follows
    parts = {n: (name, line) for n, name, line in mp.parts()}
    body = [t(0, 9, "The book on one page", 800, mc.INK, size=20 * PT),
            t(0, 15.5, "The five parts, and before and after them. Each band is a chapter, as wide as its pages.",
              400, mc.MUTED, size=10 * PT, fam=SERIF)]

    # the bar: the whole book, each chapter as wide as its pages (one unit each without the numbers)
    starts = [pages.get(f) for f, _, _ in chs]
    if pages and all(starts) and starts == sorted(starts):
        end = max(total, starts[-1] + 2) if total else starts[-1] + 2
        span = [b - a for a, b in zip(starts, starts[1:] + [end])]
    else:
        span = [1] * len(chs)
    unit = W / sum(span)
    x, y0, bh = 0.0, 24.5, 7.0
    k = 0
    for (f, title, part), s in zip(chs, span):
        w = s * unit
        fill = mc.FILL2 if part is None else TINT[k % 2]
        k = k + 1 if part else 0
        body.append(f'<rect x="{x:.2f}" y="{y0:.2f}" width="{max(w - .3, .2):.2f}" height="{bh}" fill="{fill}"/>')
        if f in FIRST:
            n = FIRST[f]
            body.append(f'<rect x="{x:.2f}" y="{y0 - 1.2:.2f}" width=".5" height="{bh + 2.4}" fill="{mc.INK}"/>')
            body.append(t(x + 1.2, y0 + bh + 4.2, mp.WORDS[n].capitalize(), 700, mc.ACCENT, size=9 * PT))
        x += w
    body.append(t(0, y0 - 1.8, "Before", 400, mc.MUTED, size=9 * PT))
    body.append(t(W, y0 - 1.8, "After", 400, mc.MUTED, size=9 * PT, anchor="end"))

    # the list, in two columns: the front and parts one to three, then parts four and five and the back
    top = y0 + bh + 12.5
    front = chs[:chs.index(next(c for c in chs if c[2] == 1))]
    back = [c for c in chs if c[2] is None and c not in front]
    cols = [[("front", front)] + [(n, [c for c in chs if c[2] == n]) for n in (1, 2, 3)],
            [(n, [c for c in chs if c[2] == n]) for n in (4, 5)] + [("back", back)]]
    row, gap, cw = 10 * PT * 1.3, 7.0, (W - 7.0) / 2
    ends = []
    for ci, groups in enumerate(cols):
        x0 = ci * (cw + gap)
        x1 = x0 + cw
        y = top
        for g, items in groups:
            if isinstance(g, int):
                name, _ = parts[g]
                body.append(f'<rect x="{x0:.2f}" y="{y - 3.3:.2f}" width="3.2" height="3.2" fill="{mc.ACCENT}"/>')
                body.append(t(x0 + 4.6, y, f"Part {mp.WORDS[g]}", 700, mc.ACCENT, size=10 * PT))
                y += row
                for r in textwrap.wrap(name, 34):
                    body.append(t(x0 + 4.6, y, r, 800, mc.INK, size=11 * PT)); y += 11 * PT * 1.3
                y += 1.2
            elif g == "back":
                body.append(t(x0 + 4.6, y, "After the story", 700, mc.MUTED, size=10 * PT))
                y += row + 1.2
            for f, title, part in items:
                lines = textwrap.wrap(title, 34)
                body.append(f'<rect x="{x0 + 4.6:.2f}" y="{y - 2.6:.2f}" width=".5" height="{2.9 + row * (len(lines) - 1):.2f}"'
                            f' fill="{mc.FILL2 if part is None else mc.ACCENT}"/>')
                for i, r in enumerate(lines):
                    body.append(t(x0 + 6.6, y, r, 400, mc.INK, size=10 * PT, fam=SERIF))
                    if i == len(lines) - 1 and pages.get(f):
                        body.append(t(x1, y, pages[f], 400, mc.INK, size=10 * PT, anchor="end",
                                      extra=f' data-file="{escape(f)}"'))
                    y += row
                y += .3
            y += 3.2
        ends.append(y)
    y = max(ends)
    if y > H:
        sys.exit(f"make_index: the list runs to {y:.1f} mm, past the page")
    svg = mc.svg(W, H, "".join(body), "The book on one page: the five parts and their chapters, with the page each starts on.")
    if re.search(r">[^<]*\b(C\d{3}|[0-9a-f]{7,})\b", svg) or "@" in re.sub(r"<[^>]+>", "", svg):
        sys.exit("make_index: an id, a hash or an address is drawn")
    (HERE / "index.svg").write_text(svg)
    print(f"written index.svg ({len(chs)} chapters, list ends at {y:.1f} mm)")


if __name__ == "__main__":
    main()
