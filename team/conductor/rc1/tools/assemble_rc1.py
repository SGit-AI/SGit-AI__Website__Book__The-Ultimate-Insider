#!/usr/bin/env python3
"""Assemble RC1 from team/conductor/rc1/ into the scratch build and make the illustrated PDF.

Copies the chapters (sorted by file name, so 00b- sits after 00-) and their images, adds the
call-outs from infographics/callouts.json as fenced divs (build only: the sources stay clean
until the publisher settles the Markua form), builds, and puts cover-1 in front.
"""
import glob, json, os, re, shutil, subprocess, sys, tempfile

REPO = "/home/user/SGit-AI__Website__Book__The-Ultimate-Insider"
RC1 = os.path.join(REPO, "team/conductor/rc1")
HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "bookbuild")
MAN = os.path.join(BUILD, "manuscript")
OUT = os.path.join(HERE, "the-ultimate-insider-RC1.pdf")
CHROME = "/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell"

CALLOUT_CSS = """
/* call-outs (scratch build; asked of the publisher) */
.callout { break-inside: avoid; page-break-inside: avoid; margin: 0.9em 0 1em; padding: 0.55em 0.8em 0.6em;
  border-left: 3pt solid #1f3a5f; background: #eef2f7; font-family: Inter, "DejaVu Sans", sans-serif; font-size: 8.8pt; line-height: 1.4; }
.callout p { text-align: left; margin: 0 0 0.35em; hyphens: none; }
.callout .label { font-size: 7pt; letter-spacing: 0.08em; text-transform: uppercase; color: #1f3a5f; margin-bottom: 0.2em; }
.callout .label strong { font-weight: 700; }
.callout.number { border-left-color: #9a6a00; background: #faf4e6; } .callout.number .label { color: #7a5200; }
.callout.warning { border-left-color: #8c2a00; background: #f8ece6; } .callout.warning .label { color: #8c2a00; }
.callout.takeaway { border-left-color: #2f6b3a; background: #ecf4ee; } .callout.takeaway .label { color: #2f6b3a; }
.callout.try { border-left-color: #444; background: #f1f1f1; } .callout.try .label { color: #333; }
"""


def chapters():
    return sorted(f for f in os.listdir(RC1) if re.match(r"\d+[a-z]?-.*\.md$", f))


def add_callouts(name, text, callouts):
    placed, missed = 0, []
    for c in [c for c in callouts if c.get("chapter") == name]:
        a = c.get("anchor", "")
        i = text.find(a) if a else -1
        if i < 0:
            missed.append(c.get("title"))
            continue
        end = text.find("\n\n", i)
        end = len(text) if end < 0 else end
        kind = re.sub(r"[^a-z]", "", (c.get("kind") or "concept").lower()) or "concept"
        label = {"concept": "Concept", "number": "The number", "takeaway": "Take away", "warning": "Watch for", "try": "Try this"}.get(kind, kind.title())
        ids = c.get("claim_ids") or []
        tail = f" ({', '.join(ids)})" if ids and not any(x in c["text"] for x in ids) else ""
        div = f"\n\n::: {{.callout .{kind}}}\n[{label}: **{c['title']}**]{{.label}}\n\n{c['text']}{tail}\n:::\n"
        text = text[:end] + div + text[end:]
        placed += 1
    return text, placed, missed


def add_images(name, text, placements):
    """Infographics and maps after their anchor's paragraph; a map with "replace" swaps an image path."""
    placed, missed = 0, []
    for p in [p for p in placements if p.get("chapter") == name]:
        img = p["image"]
        if p.get("replace"):
            if p["replace"] in text:
                text = text.replace(p["replace"], img)
                placed += 1
            else:
                missed.append(img)
            continue
        a = p.get("anchor", "")
        i = text.find(a) if a else -1
        if i < 0:
            missed.append(img)
            continue
        end = text.find("\n\n", i)
        end = len(text) if end < 0 else end
        while text.startswith("\n\n![", end):  # keep placements that share an anchor in file order
            nl = text.find("\n", end + 3)
            end = len(text) if nl < 0 else nl
        text = text[:end] + f"\n\n![{p['caption']}]({img})" + text[end:]
        placed += 1
    return text, placed, missed


def main():
    callouts = []
    cj = os.path.join(RC1, "infographics/callouts.json")
    if os.path.exists(cj):
        d = json.load(open(cj))
        callouts = d if isinstance(d, list) else d.get("callouts", [])
    for f in glob.glob(os.path.join(MAN, "*.md")):
        os.unlink(f)
    if os.path.isdir(os.path.join(MAN, "resources")):
        shutil.rmtree(os.path.join(MAN, "resources"))
    shutil.copytree(os.path.join(RC1, "resources"), os.path.join(MAN, "resources"))
    ig = os.path.join(RC1, "infographics/jpg")
    if os.path.isdir(ig):  # chapters reference them as resources/images/infographics/<file>
        shutil.copytree(ig, os.path.join(MAN, "resources/images/infographics"), dirs_exist_ok=True)
    placements = []
    mf = os.path.join(RC1, "infographics/manifest.json")
    if os.path.exists(mf):
        placements += [{"chapter": m["chapter"], "anchor": m["anchor"], "caption": m["caption"],
                        "image": "resources/images/infographics/" + os.path.basename(m["file"])} for m in json.load(open(mf)) if not m.get("withdrawn")]
    pf = os.path.join(RC1, "maps/placements.json")
    if os.path.exists(pf):
        placements += json.load(open(pf))
    total, allmissed = 0, []
    names = chapters()
    for n in names:
        t = open(os.path.join(RC1, n), encoding="utf-8").read()
        t, ip, imissed = add_images(n, t, placements)
        allmissed += [f"{n}: image {m}" for m in imissed]
        t, placed, missed = add_callouts(n, t, callouts)
        total += ip
        total += placed
        allmissed += [f"{n}: {m}" for m in missed]
        open(os.path.join(MAN, n), "w", encoding="utf-8").write(t)
    open(os.path.join(MAN, "Book.txt"), "w").write("\n".join(names) + "\n")
    css = open(os.path.join(BUILD, "publishing/book.css")).read()
    if "call-outs (scratch build" not in css:
        open(os.path.join(BUILD, "publishing/book.css"), "a").write(CALLOUT_CSS)
    print(f"assemble: {len(names)} chapters, {total} images and call-outs placed")
    for m in allmissed:
        print("assemble: call-out anchor not found:", m)
    r = subprocess.run([sys.executable, "publishing/build_book.py", "--out", os.path.join(BUILD, "out"), "--no-epub", "--chrome", CHROME], cwd=BUILD)
    if r.returncode:
        sys.exit("assemble: build failed")
    book = glob.glob(os.path.join(BUILD, "out", "*.pdf"))[0]
    cover = os.path.join(RC1, "cover/cover-1.jpg")
    with tempfile.TemporaryDirectory() as tmp:
        h = os.path.join(tmp, "c.html")
        open(h, "w").write(f"<!doctype html><style>@page{{size:6in 9in;margin:0}}html,body{{margin:0}}img{{width:6in;height:9in;display:block}}</style><img src='file://{cover}'>")
        cpdf = os.path.join(tmp, "cover.pdf")
        try:
            subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", f"--user-data-dir={tmp}/p", "--no-pdf-header-footer",
                            f"--print-to-pdf={cpdf}", "file://" + h], timeout=90, capture_output=True)
        except subprocess.TimeoutExpired:
            pass
        subprocess.run(["pdfunite", cpdf, book, OUT], check=True)
    pages = re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", OUT], capture_output=True, text=True).stdout).group(1)
    print(f"assemble: {OUT} ({pages} pages, {os.path.getsize(OUT) // 1024} KB)")


if __name__ == "__main__":
    main()
