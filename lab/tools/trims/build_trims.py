#!/usr/bin/env python3
"""The trim study: the same sample pages as real book pages at each KDP trim the editor is choosing between.

python3 lab/tools/trims/build_trims.py
Writes lab/pdf/trim-study-<trim>.pdf for each trim, and their lines in lab/pdf/SHA256SUMS. The pages flow as a
book does (mirrored margins, the gutter inside, a folio in the outer margin, one full-bleed page), in the lab's
type at the lab's sizes, so only the page changes. Checked by lab/tools/render.mjs: nothing under 9 pt.
A study for the editor's choice of trim; the book's build is the publisher's.
"""
import hashlib, html, re, subprocess, sys
from pathlib import Path

LAB = Path(__file__).resolve().parents[2]
REPO = LAB.parent
FROM_PDF = "../.."                         # the staged page sits in lab/pdf/; paths below are from the repository root
TRIMS = [("6x9", 6.0, 9.0), ("7.5x9.25", 7.5, 9.25), ("7.44x9.69", 7.44, 9.69), ("8x10", 8.0, 10.0)]   # 7.44 x 9.69: Crown Quarto, the editor's choice (31 October 2026)
GUTTER, OUTSIDE, TOP, BOTTOM = 0.625, 0.375, 0.5, 0.625  # inches: a 0.625 in gutter (the editor, 31 October 2026; KDP's minimum is 0.5 for 151 to 300 pages); 0.375 in outside


def usable(w, h):
    return (w - GUTTER - OUTSIDE) * 25.4, (h - TOP - BOTTOM) * 25.4


def esc(s):
    return html.escape(s, quote=False)


def img(path, alt, cls=""):
    return f'<img class="{cls}" src="{FROM_PDF}/{path}" alt="{esc(alt)}">'


def flow_svg():
    """The five-steps figure, from LAB 01's own page."""
    s = (LAB / "experiments" / "01-designer-visual-language" / "pages.html").read_text()
    return re.search(r'<svg viewBox="0 0 131 46".*?</svg>', s, re.S).group(0)


def character(name):
    return (LAB / "characters" / f"{name}.svg").read_text()


def book(name, w, h):
    uw, uh = usable(w, h)
    rows = "".join(f'<tr class="{"on" if n == name else ""}"><td>{n.replace("x", " x ")} in</td><td>{tw * 25.4:.0f} x {th * 25.4:.0f} mm</td>'
                   f'<td>{usable(tw, th)[0]:.0f} x {usable(tw, th)[1]:.0f} mm</td></tr>' for n, tw, th in TRIMS)
    strip = "".join(f'<div>{img(f"lab/experiments/04-designer-condensed-storyboard/frames/b01-frame-{i}.jpg", f"B01 frame {i}")}<p>{i}</p></div>' for i in range(1, 9))
    body = f'''
<section class="title">
 <div class="rule"></div>
 <p class="kick">The ultimate insider · a trim study</p>
 <h1>{name.replace("x", " x ")} in{" · Crown Quarto" if name == "7.44x9.69" else ""}</h1>
 <p class="sub">The same pages at four book sizes. Print at actual size (100%), not "fit to page", and lay the three side by side.</p>
 <table><tr><th>Trim</th><th>Page</th><th>Text block</th></tr>{rows}</table>
 <p class="note">Margins as the book will have them: a 0.625 in gutter on the inside (KDP's minimum is 0.5 in for 151 to 300 pages), 0.375 in outside, 0.5 in at the top and 0.625 in at the foot, where the folio sits. The type is the lab's, at the lab's sizes; only the page changes. A study for the editor's choice of trim; the book's build is the publisher's. The full-bleed page would carry 0.125 in of bleed in the file sent to KDP.</p>
</section>

<section>
 <h2>A worked page</h2>
 <aside class="rail">
  <div class="tile"><b class="t-num">816</b><span>commits in the talk's repository at 298be4e</span><span class="cid">C002</span></div>
  <div class="char">{character("the-hold")}<p class="who">the hold</p><p class="bubble">Anyone can pull me. Only the editor puts me back.</p></div>
 </aside>
 <p>This is LAB 01's worked page, set in a book. The argument runs in the text block; the rail on the outside holds what a reader can skip: a number, a character, a short note. The talk's repository held 816 commits at 298be4e (C002); its team had nine staffed members (C011) and wrote one hold on the day (C024). A page about that hold shows the hold first, in the accent, and everything else in ink.</p>
 <p>The type does not change between the three sizes: body text at 10 pt, call-outs at 9.5, captions at 9, nothing smaller. What changes is how much fits beside it: on the narrowest page the rail squeezes the text, and on the widest the figures can run the full width of the text block.</p>
 <figure class="fig">
  <p class="fig-title">Five steps, and the one way out</p>
  {flow_svg()}
  <figcaption><b>One accent, one thing to see: the way out.</b> The figure is drawn at the width of the text block, so its labels grow and shrink with the page. <span class="src">team/conductor/WAKE.md, The five steps</span></figcaption>
 </figure>
 <aside class="callout concept"><p class="kind">Concept</p><p class="co-title">The rail is for what a reader may skip</p><p class="co-text">If the page still argues its point with the rail covered, the rail is doing its job.</p></aside>
</section>

<section>
 <h2>An infographic at the width of the text block</h2>
 <figure class="fig">
  {img("team/conductor/rc1/infographics/jpg/ig14-five-step-wake.jpg", "RC1 infographic: the five-step wake", "wide")}
  <figcaption><b>RC1's own infographic, as placed at each size.</b> It was drawn for a 4.75 in placement; its smallest text is 9 pt there and larger on a wider page. <span class="src">team/conductor/rc1/infographics/jpg/ig14-five-step-wake.jpg</span></figcaption>
 </figure>
 <figure class="fig">
  {img("team/conductor/rc1/infographics/jpg/ig01-the-day.jpg", "RC1 infographic: the day, vertical", "tall")}
  <figcaption><b>A vertical infographic, at the full height left on the page.</b> <span class="src">team/conductor/rc1/infographics/jpg/ig01-the-day.jpg</span></figcaption>
 </figure>
</section>

<section class="bleed">
 {img("lab/experiments/01-ruv-the-building-three-frames/frames/m01-light-t43.png", "The talk's M01 at 43 seconds, edge to edge", "edge")}
 <div class="bleed-text">
  <p class="fig-title">A full-bleed image: to the edges of the page</p>
  <p>The talk's animation M01 at its last frame, printed to the trim on three sides. On paper the image runs off the page; only the words keep to the margins. <span class="src mono">ruv.sgit's frame, lab/experiments/01-ruv-the-building-three-frames/frames/</span></p>
 </div>
</section>

<section>
 <h2>Screenshots, at the width of the text block</h2>
 <figure class="fig">{img("index/talk-site/shots/index.jpg", "The talk site's home page")}
  <figcaption><b>The talk site's home page.</b> Can you read the page inside the screenshot at this size? <span class="src">index/talk-site/shots/index.jpg, the librarian's</span></figcaption></figure>
 <figure class="fig">{img("index/talk-site/shots/studio-ports__journey.jpg", "One action's journey")}
  <figcaption><b>One action's journey.</b> <span class="src">index/talk-site/shots/studio-ports__journey.jpg</span></figcaption></figure>
</section>

<section>
 <h2>A storyboard strip</h2>
 <figure class="fig"><div class="strip">{strip}</div>
  <figcaption><b>LAB 04's eight frames at the width of the text block.</b> On the narrowest page each frame is about a third smaller than on the widest. <span class="src">B01 storyboard at ecdcdf9 in the talk's repository, by ruv.sgit</span></figcaption></figure>
</section>
'''
    css = (LAB / "tools" / "lab.css").read_text() + f'''
@page {{ size: {w}in {h}in; margin: {TOP}in {OUTSIDE}in {BOTTOM}in {GUTTER}in;
  @bottom-right {{ content: counter(page); font: 400 9pt var(--sans); color: #5b6670 }} }}
@page :left {{ margin-left: {OUTSIDE}in; margin-right: {GUTTER}in;
  @bottom-left {{ content: counter(page) "  ·  The ultimate insider · trim study {name.replace("x", " x ")} in"; font: 400 9pt var(--sans); color: #5b6670 }}
  @bottom-right {{ content: none }} }}
@page :first {{ @bottom-right {{ content: none }} }}
@page bleed {{ margin: 0; @bottom-right {{ content: none }} @bottom-left {{ content: none }} }}
html, body {{ background: #fff }}
section {{ break-after: page }}
section:last-child {{ break-after: auto }}
.title .rule {{ width: 18mm; height: 1.2mm; background: var(--accent); margin-top: 20mm }}
.title .kick {{ font: 700 9pt/12pt var(--sans); letter-spacing: .12em; text-transform: uppercase; color: var(--accent); margin: 6mm 0 0 }}
.title h1 {{ font: 800 30pt/34pt var(--sans); margin: 2mm 0 4mm }}
.title .sub {{ font: 400 12pt/16pt var(--sans); color: var(--muted) }}
.title table {{ border-collapse: collapse; width: 100%; margin: 6mm 0 }}
.title td, .title th {{ text-align: left; padding: 2mm; border-bottom: .3mm solid var(--fill-2); font-size: 10pt }}
.title th {{ font: 700 9pt/12pt var(--sans); text-transform: uppercase; color: var(--muted) }}
.title tr.on td {{ font-weight: 800; background: var(--tint) }}
.title .note {{ font-size: 9.5pt; line-height: 13pt; color: var(--muted) }}
.rail {{ float: right; width: 34%; margin: 0 0 4mm 5mm }}
.rail .char svg {{ width: 18mm }}
.fig {{ break-inside: avoid; clear: both }}
.callout {{ break-inside: avoid; clear: both }}
img.wide, .fig img {{ width: 100%; display: block; border: .3mm solid var(--fill-2) }}
img.tall {{ width: auto; max-width: 100%; height: {uh * 0.62:.0f}mm; margin: 0 auto }}
.bleed {{ page: bleed }}
img.edge {{ width: {w}in; display: block; border: 0 }}
.bleed-text {{ margin: 6mm {OUTSIDE}in 0 {GUTTER}in }}
.strip {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 3mm }}
.strip img {{ width: 100%; border: .3mm solid var(--fill-2) }}
.strip p {{ font: 700 9pt/12pt var(--sans); color: var(--accent); margin: .5mm 0 0 }}
'''
    return f'<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>Trim study {name}</title><style>{css}</style></head><body>{body}</body></html>'


def main():
    sums = LAB / "pdf" / "SHA256SUMS"
    for name, w, h in TRIMS:
        stage = LAB / "pdf" / f"_trim-{name}.html"
        out = LAB / "pdf" / f"trim-study-{name}.pdf"
        stage.write_text(book(name, w, h))
        r = subprocess.run(["node", str(LAB / "tools" / "render.mjs"), str(stage), str(out), "any"])
        if r.returncode:
            sys.exit(f"trim study {name} refused (see above)")
        stage.unlink()
        lines = [l for l in sums.read_text().splitlines() if not l.endswith("  " + out.name)]
        lines.append(f"{hashlib.sha256(out.read_bytes()).hexdigest()}  {out.name}")
        sums.write_text("\n".join(sorted(lines, key=lambda l: l.split("  ")[1])) + "\n")
    print("trim study built: " + ", ".join(f"lab/pdf/trim-study-{n}.pdf" for n, _, _ in TRIMS))


if __name__ == "__main__":
    main()
