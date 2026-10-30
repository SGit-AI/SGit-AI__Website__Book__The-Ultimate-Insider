#!/usr/bin/env python3
"""Build the lab PDF: lab/experiments/*/ in order, a cover, a header per experiment, checked, hashed.

python3 lab/tools/build_lab.py [--html-only]
Rules: lab/README.md. Renders with Chromium through render.mjs (Playwright); refuses text under 9 pt,
overflowing pages, and a page count other than the cover's plus each experiment's declared pages.
"""
import hashlib, html, json, os, re, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

LAB = Path(__file__).resolve().parent.parent
OUT = LAB / "pdf" / "the-ultimate-insider-lab.pdf"
STAGE = LAB / "pdf" / "_build.html"          # not committed (.gitignore)
SERIES = "The ultimate insider · lab · first round"
COVER_PAGES = 1


def esc(s):
    return html.escape(s, quote=False)


def mono_paths(s):
    """Set paths and commits in the monospace."""
    return re.sub(r"(\b[\w.-]+/[\w./*-]+|\b[0-9a-f]{7}\b)", r'<span class="mono">\1</span>', esc(s))


def characters():
    out = {}
    for f in sorted((LAB / "characters").glob("*.svg")):
        out[f.stem] = f.read_text()
    return out


def experiments():
    found = []
    for d in sorted(p for p in (LAB / "experiments").iterdir() if p.is_dir()):
        if not (d / "experiment.json").exists():
            # not in the lab's format yet: it goes in after the designer's verdict (lab/README.md, The build)
            print(f"left out: {d.name} (no experiment.json; waiting for the design verdict)")
            continue
        meta = json.loads((d / "experiment.json").read_text())
        for k in ("id", "title", "tries", "made_from", "question", "pages"):
            if k not in meta:
                sys.exit(f"{d.name}: experiment.json has no {k}")
        found.append((d, meta))
    return found


def header(meta):
    made = "".join(f"<li>{mono_paths(m)}</li>" for m in meta["made_from"])
    return (f'<div class="head"><div class="id">{esc(meta["id"])}</div><h1>{esc(meta["title"])}</h1><dl>'
            f'<dt>Tries</dt><dd>{esc(meta["tries"])}</dd>'
            f'<dt>Made from</dt><dd><ul>{made}</ul></dd>'
            f'<dt>The question</dt><dd>{esc(meta["question"])}'
            f'<div class="verdict"><span><i class="box"></i>keep</span><span><i class="box"></i>change</span>'
            f'<span><i class="box"></i>drop</span><span class="note">note</span></div></dd></dl></div>')


def page(inner, ident, claims=""):
    c = f'<div class="claims">{esc(claims)}</div>' if claims else ""
    return (f'<section class="page"><div class="block">{inner}</div>{c}'
            f'<div class="foot"><span>{SERIES}</span><span class="mid">{esc(ident)}</span>'
            f'<span class="r">page {{n}} of {{N}}</span></div></section>')


def assemble():
    chars = characters()
    exps = experiments()
    when = datetime.now(timezone.utc).strftime("%d %B %Y, %H:%M UTC")
    rows = "".join(f'<tr><td class="mono">{esc(m["id"])}</td><td>{esc(m["title"])}</td><td>{m["pages"]}</td></tr>' for _, m in exps)
    cover = page(f'<div class="cover"><div class="rule"></div><h1>The ultimate insider: the lab</h1>'
                 f'<p class="sub">Experiments in telling the story on paper. First round, for printing.</p>'
                 f'<table><tr><th>Id</th><th>Experiment</th><th>Pages</th></tr>{rows}</table>'
                 f'<p class="how">Each experiment opens with what it tries, what it is made from, and one question. '
                 f'Tick keep, change or drop on paper and write a note; the conductor puts each verdict into book.json. '
                 f'Built {when} by lab/tools/build_lab.py; the rules are in lab/README.md.</p></div>', "LAB")
    pages = [cover]
    for d, meta in exps:
        src = (d / "pages.html").read_text()
        src = re.sub(r"\{\{char:([\w-]+)\}\}", lambda m: chars[m.group(1)], src)
        secs = re.findall(r'<section class="page"(?: data-claims="([^"]*)")?>(.*?)</section>', src, re.S)
        if len(secs) != meta["pages"]:
            sys.exit(f'{d.name}: declares {meta["pages"]} pages, pages.html has {len(secs)}')
        for i, (claims, inner) in enumerate(secs):
            pages.append(page((header(meta) if i == 0 else "") + inner, meta["id"], claims))
    total = len(pages)
    body = "".join(p.replace("{n}", str(i + 1)).replace("{N}", str(total)) for i, p in enumerate(pages))
    css = (LAB / "tools" / "lab.css").read_text()
    STAGE.write_text(f'<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>The ultimate insider: the lab</title>'
                     f'<style>{css}</style></head><body>{body}</body></html>')
    return COVER_PAGES + sum(m["pages"] for _, m in exps)


def main():
    expected = assemble()
    if "--html-only" in sys.argv:
        print(f"assembled {STAGE}")
        return
    env = dict(os.environ)
    r = subprocess.run(["node", str(LAB / "tools" / "render.mjs"), str(STAGE), str(OUT), str(expected)], env=env)
    if r.returncode:
        sys.exit("lab build refused (see above)")
    sums = f"{hashlib.sha256(OUT.read_bytes()).hexdigest()}  {OUT.name}\n"
    (LAB / "pdf" / "SHA256SUMS").write_text(sums)
    STAGE.unlink()
    print(f"built {OUT.relative_to(LAB.parent)}: {expected} pages; SHA256SUMS written")


if __name__ == "__main__":
    main()
