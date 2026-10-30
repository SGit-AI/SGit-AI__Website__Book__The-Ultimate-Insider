#!/usr/bin/env python3
"""Build a debrief PDF in the lab's visual language (not a lab experiment).

python3 lab/tools/debrief/build_debrief.py talk-site
Reads lab/tools/debrief/<name>.json, writes lab/pdf/<name>-debrief.pdf and its line in lab/pdf/SHA256SUMS.
Renders and checks with lab/tools/render.mjs: no text under 9 pt, no overflowing page, the page count.
"""
import hashlib, html, json, re, subprocess, sys
from pathlib import Path

LAB = Path(__file__).resolve().parents[2]
SHOTS = "../../index/talk-site/shots"        # from lab/pdf/, where the staged page sits
PER_PAGE = 2


def esc(s):
    return html.escape(s, quote=False)


def title_of(shot):
    """The visual's title from the librarian's visuals.md, or its path when the title carries a number."""
    for line in (LAB.parent / "index" / "talk-site" / "visuals.md").read_text().splitlines():
        if f"shots/{shot}.jpg" in line:
            t = line.split("|")[2].strip()
            return shot.replace("__", "/") if re.search(r"\d", t) else t
    return shot.replace("__", "/")


def build(name):
    d = json.loads((LAB / "tools" / "debrief" / f"{name}.json").read_text())
    series = "The ultimate insider · debrief"
    pages = []

    def page(inner, mid):
        pages.append((inner, mid))

    page(f'<div class="cover compact"><div class="rule"></div><h1>{esc(d["title"])}</h1><p class="sub">{esc(d["sub"])}</p>'
         f'<p>{esc(d["made_from"])}</p><p class="how">{esc(d["how"])}</p>'
         f'<table><tr><th></th><th>Highlight</th><th>Where it lives</th></tr>'
         + "".join(f'<tr><td class="mono">{i + 1:02d}</td><td>{esc(h["title"])}</td><td class="mono">{esc(h["where"].split(" (")[0])}</td></tr>'
                   for i, h in enumerate(d["highlights"])) + '</table></div>', "DEBRIEF")
    hs = d["highlights"]
    for k in range(0, len(hs), PER_PAGE):
        rows = ""
        for i, h in enumerate(hs[k:k + PER_PAGE], start=k + 1):
            img = (f'<img src="{SHOTS}/{h["shot"]}.jpg" alt="{esc(h["title"])}">' if h["shot"]
                   else '<div class="noshot">Described, not shown:<br>this page prints keys.</div>')
            rows += (f'<div class="hl">{img}<div><p class="n">{i:02d}</p><p class="ht">{esc(h["title"])}</p>'
                     f'<p><b>What it is.</b> {esc(h["what"])}</p><p><b>Why it matters to the book.</b> {esc(h["why"])}</p>'
                     f'<p class="mono where">{esc(h["where"])}</p></div></div>')
        last = min(k + PER_PAGE, len(hs))
        span = f"{k + 1:02d}" if last == k + 1 else f"{k + 1:02d} to {last:02d}"
        page(f'<h2>The highlights, {span}</h2>{rows}', "DEBRIEF")
    br = "".join(f'<tr><td class="mono">{esc(p)}</td><td>{esc(w)}</td></tr>' for p, w in d["broken"])
    tiles = "".join(f'<div class="tilev"><img src="{SHOTS}/{s}.jpg" alt=""><p>{esc(title_of(s))}</p></div>' for s in d["reuse"])
    page(f'<h2>What does not work</h2><p>Almost every page loads with content and no error. The ones that do not all depend on another service; nothing on the site itself is broken.</p>'
         f'<table class="plain">{br}</table>'
         f'<h2 class="mt">Visuals the book could reuse or redraw</h2><p>A sample from the librarian\'s list (<span class="mono">index/talk-site/visuals.md</span>). Reuse waits on the licence question: the talk\'s repository is Apache-2.0, the book CC BY 4.0, and some images carry third-party credits.</p>'
         f'<div class="reuse">{tiles}</div>', "DEBRIEF")

    total = len(pages)
    body = "".join(f'<section class="page"><div class="block">{inner}</div><div class="foot"><span>{esc(series)}</span>'
                   f'<span class="mid">{mid}</span><span class="r">page {n} of {total}</span></div></section>'
                   for n, (inner, mid) in enumerate(pages, start=1))
    css = (LAB / "tools" / "lab.css").read_text() + (LAB / "tools" / "debrief" / "debrief.css").read_text()
    stage = LAB / "pdf" / f"_{name}-debrief.html"
    out = LAB / "pdf" / f"{name}-debrief.pdf"
    stage.write_text(f'<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>{esc(d["title"])}</title>'
                     f'<style>{css}</style></head><body>{body}</body></html>')
    r = subprocess.run(["node", str(LAB / "tools" / "render.mjs"), str(stage), str(out), str(total)])
    if r.returncode:
        sys.exit("debrief build refused (see above)")
    stage.unlink()
    sums = LAB / "pdf" / "SHA256SUMS"
    lines = [l for l in sums.read_text().splitlines() if not l.endswith("  " + out.name)]
    lines.append(f"{hashlib.sha256(out.read_bytes()).hexdigest()}  {out.name}")
    sums.write_text("\n".join(sorted(lines, key=lambda l: l.split("  ")[1])) + "\n")
    print(f"built {out.relative_to(LAB.parent)}: {total} pages; SHA256SUMS updated")


if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "talk-site")
