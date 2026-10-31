#!/usr/bin/env python3
"""Build the lab PDF: lab/experiments/*/ in order, a cover, a header per experiment, checked, hashed.

python3 lab/tools/build_lab.py [--html-only]
Rules: lab/README.md. Renders with Chromium through render.mjs (Playwright) at the book's trim, Crown Quarto; refuses text under 9 pt
and anything wider than the text block. Each authored page starts a page and may flow onto the next.
"""
import hashlib, html, json, os, re, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

LAB = Path(__file__).resolve().parent.parent
OUT = LAB / "pdf" / "the-ultimate-insider-lab.pdf"
STAGE = LAB / "pdf" / "_build.html"          # not committed (.gitignore)
SERIES = "The ultimate insider · lab · first round"
TRIM = (7.44, 9.69, "Crown Quarto 7.44 x 9.69 in")     # the book's trim, the editor's choice (31 October 2026)


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


def component_timeline(m):
    """{{timeline:<spec, from lab/>:<mode>:<length mm>}}: lab/tools/components/timeline.py, drawn at its own size."""
    sys.path.insert(0, str(LAB / "tools" / "components"))
    from timeline import render
    svg = render(json.loads((LAB / m.group(1)).read_text()), m.group(2), float(m.group(3)))
    w = re.search(r'viewBox="0 0 ([\d.]+)', svg).group(1)
    return svg.replace('class="timeline"', f'class="timeline" style="width: {w}mm; max-width: none"', 1)


def component_mapnotes(m):
    """{{mapnotes:<spec, from lab/>}}: lab/tools/components/mapnotes.py, a map image with numbered side notes."""
    sys.path.insert(0, str(LAB / "tools" / "components"))
    from mapnotes import render
    return render(json.loads((LAB / m.group(1)).read_text()), LAB.parent)


def component_counters(m):
    """{{counters:<spec, from lab/>:<length mm>}}: lab/tools/components/counters.py, drawn at its own size."""
    sys.path.insert(0, str(LAB / "tools" / "components"))
    from counters import render
    svg = render(json.loads((LAB / m.group(1)).read_text()), float(m.group(2)))
    w = re.search(r'viewBox="0 0 ([\d.]+)', svg).group(1)
    return svg.replace('class="counters"', f'class="counters" style="width: {w}mm; max-width: none; display: block"', 1)


def experiments():
    found = []
    for d in sorted(p for p in (LAB / "experiments").iterdir() if p.is_dir()):
        if not (d / "experiment.json").exists():
            if any(e["folder"] == d.name for e in json.loads((LAB / "tools" / "external.json").read_text())["experiments"]):
                continue
            # not in the lab's format yet: it goes in after the designer's verdict (lab/README.md, The build)
            print(f"left out: {d.name} (no experiment.json; waiting for the design verdict)")
            continue
        meta = json.loads((d / "experiment.json").read_text())
        for k in ("id", "title", "tries", "made_from", "question", "pages"):
            if k not in meta:
                sys.exit(f"{d.name}: experiment.json has no {k}")
        meta["_pages"] = d / "pages.html"
        meta["_dir"] = f"../experiments/{d.name}"
        found.append((d, meta))
    ext = json.loads((LAB / "tools" / "external.json").read_text())["experiments"]
    for meta in ext:
        d = LAB / "experiments" / meta["folder"]
        if not d.is_dir():
            sys.exit(f'external.json: {meta["folder"]} is not in lab/experiments/')
        if (d / "experiment.json").exists():
            continue                     # its member moved it into the lab's format: its own header wins
        meta["_pages"] = d / "pages.html" if meta["layout"] == "@folder" else LAB / "tools" / meta["layout"]
        meta["_dir"] = f"../experiments/{d.name}"
        found.append((d, meta))
    ids_path = LAB / "tools" / "ids.json"
    ids_file = json.loads(ids_path.read_text())
    printed, held = ids_file.setdefault("printed", {}), ids_file.get("held", {})
    for d, meta in [e for e in found if e[0].name in held]:
        print(f"held: {d.name} ({held[d.name]})")
    found = [e for e in found if e[0].name not in held]
    taken = set(printed.values())
    for d, meta in sorted(found, key=lambda e: e[0].name):    # the ledger first: a printed id never moves
        if d.name in printed:
            if meta["id"] != printed[d.name]:
                print(f"{d.name}: declares {meta['id']}, prints as {printed[d.name]} (the ledger)")
            meta["id"] = printed[d.name]
    folders = {p.name for p in (LAB / "experiments").iterdir() if p.is_dir()}
    vanished = {i: f for f, i in printed.items() if f not in folders}   # a ledger folder that is gone: renamed, most likely
    reserved = {i: who for who, ids in ids_file.get("reserved", {}).items() for i in ids}
    for d, meta in sorted(found, key=lambda e: e[0].name):    # then new folders
        if d.name in printed:
            continue
        if meta["id"] in vanished:                            # a rename keeps its printed id
            print(f"{d.name}: takes over {meta['id']} from {vanished[meta['id']]} (renamed)")
            del printed[vanished.pop(meta["id"])]
        elif meta["id"] in taken or (meta["id"] in reserved and f'-{reserved[meta["id"]].split("-")[0]}-' not in d.name):
            n = 1
            while f"LAB {n:02d}" in taken or f"LAB {n:02d}" in reserved:
                n += 1
            print(f"{d.name}: declares {meta['id']}, which is printed or reserved; prints as LAB {n:02d}")
            meta["id"] = f"LAB {n:02d}"
        printed[d.name] = meta["id"]
        taken.add(meta["id"])
    ids_path.write_text(json.dumps(ids_file, indent=1) + "\n")
    return sorted(found, key=lambda e: e[1]["id"])


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
    return f'<section class="sheet" style="page: {pname(ident)}">{inner}{c}</section>'


def pname(ident):
    return "p" + re.sub(r"\W", "", ident).lower()


def page_rules(idents):
    """One named page per experiment, so its footer carries its id: series, id and trim on the outside, the page number."""
    out = [f"@page {{ size: {TRIM[0]}in {TRIM[1]}in; margin: 0.5in 0.375in 0.625in 0.625in }}",           # gutter 0.625 in (the editor, 31 October 2026)
           "@page :left { margin-left: 0.375in; margin-right: 0.625in }"]
    box = "font: 400 9pt Inter, Helvetica, Arial, sans-serif; color: #5b6670"
    for i in idents:
        foot = f"{SERIES} · {i} · {TRIM[2]}"
        out.append(f'@page {pname(i)}:right {{ @bottom-left {{ content: "{foot}"; {box} }} @bottom-right {{ content: "page " counter(page) " of " counter(pages); {box} }} }}')
        out.append(f'@page {pname(i)}:left {{ @bottom-left {{ content: "page " counter(page) " of " counter(pages); {box} }} @bottom-right {{ content: "{foot}"; {box} }} }}')
    return "\n".join(out)


def assemble(counts=None):
    chars = characters()
    exps = experiments()
    when = datetime.now(timezone.utc).strftime("%d %B %Y, %H:%M UTC")
    counts = counts or {}
    rows = "".join(f'<tr><td class="mono">{esc(m["id"])}</td><td>{esc(m["title"])}</td><td>{counts.get(m["id"], "")}</td></tr>' for _, m in exps)
    cover = page(f'<div class="cover"><div class="rule"></div><h1>The ultimate insider: the lab</h1>'
                 f'<p class="sub">Experiments in telling the story on paper. First round, for printing, at the book\'s size: {TRIM[2]}.</p>'
                 f'<table><tr><th>Id</th><th>Experiment</th><th>Pages</th></tr>{rows}</table>'
                 f'<p class="how">Each experiment opens with what it tries, what it is made from, and one question. '
                 f'Tick keep, change or drop on paper and write a note; the conductor puts each verdict into book.json. '
                 f'Print at actual size (100%), not "fit to page". '
                 f'Built {when} by lab/tools/build_lab.py; the rules are in lab/README.md.</p></div>', "LAB")
    pages = [cover]
    for d, meta in exps:
        src = meta["_pages"].read_text().replace("{{dir}}", meta["_dir"])
        if meta["_pages"].parent == d:   # a page in its own folder: its relative images are found there
            src = re.sub(r'src="(?!data:|https?:|/|\.\./|\{\{)([^"]+)"', lambda m: f'src="{meta["_dir"]}/{m.group(1)}"', src)
        src = re.sub(r"\{\{char:([\w-]+)\}\}", lambda m: chars[m.group(1)], src)
        src = re.sub(r"\{\{mapnotes:([\w./-]+\.json)\}\}", component_mapnotes, src)
        src = re.sub(r"\{\{counters:([\w./-]+\.json):([\d.]+)\}\}", component_counters, src)
        src = re.sub(r"\{\{timeline:([\w./-]+\.json):(horizontal|vertical):([\d.]+)\}\}", component_timeline, src)
        secs = re.findall(r'<section class="page"(?: data-claims="([^"]*)")?>(.*?)</section>', src, re.S)
        if len(secs) != meta["pages"]:
            sys.exit(f'{d.name}: declares {meta["pages"]} pages, pages.html has {len(secs)}')
        for i, (claims, inner) in enumerate(secs):
            pages.append(page((header(meta) if i == 0 else "") + inner, meta["id"], claims))
    css = (LAB / "tools" / "lab.css").read_text() + (LAB / "tools" / "crown-quarto.css").read_text() + page_rules(["LAB"] + [m["id"] for _, m in exps])
    STAGE.write_text(f'<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>The ultimate insider: the lab</title>'
                     f'<style>{css}</style></head><body>{"".join(pages)}</body></html>')
    return exps


def page_counts(exps):
    """Where each experiment starts in the rendered PDF (its title on the page), so the cover can say how long it runs."""
    from pypdf import PdfReader
    texts = [" ".join((pg.extract_text() or "").split()) for pg in PdfReader(str(OUT)).pages]
    starts, after = [], 0                         # page 0 is the cover, which lists every title: search past it, in order
    for _, m in exps:
        at = next((n for n, t in enumerate(texts) if n > after and m["title"] in t and "tries" in t.lower()), None)
        if at is None:
            sys.exit(f'{m["id"]}: its header was not found in the PDF')
        starts.append(at)
        after = at
    ends = starts[1:] + [len(texts)]
    return {m["id"]: e - s for (_, m), s, e in zip(exps, starts, ends)}, len(texts)


def main():
    exps = assemble()
    if "--html-only" in sys.argv:
        print(f"assembled {STAGE}")
        return
    render = lambda expected: subprocess.run(["node", str(LAB / "tools" / "render.mjs"), str(STAGE), str(OUT), str(expected)]).returncode
    if render("any"):
        sys.exit("lab build refused (see above)")
    counts, total = page_counts(exps)             # a second pass prints each experiment's length on the cover
    assemble(counts)
    if render(total):
        sys.exit("lab build refused on its second pass (see above)")
    sums = LAB / "pdf" / "SHA256SUMS"         # one line per PDF in lab/pdf/; keep the others' lines
    lines = [l for l in (sums.read_text().splitlines() if sums.exists() else []) if not l.endswith("  " + OUT.name)]
    lines.append(f"{hashlib.sha256(OUT.read_bytes()).hexdigest()}  {OUT.name}")
    sums.write_text("\n".join(sorted(lines, key=lambda l: l.split("  ")[1])) + "\n")
    STAGE.unlink()
    print(f"built {OUT.relative_to(LAB.parent)}: {total} pages at {TRIM[2]}; SHA256SUMS written")


if __name__ == "__main__":
    main()
