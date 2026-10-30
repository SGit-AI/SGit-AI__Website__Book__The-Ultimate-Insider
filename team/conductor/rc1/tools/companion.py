#!/usr/bin/env python3
"""Render the annotated companion to RC1 as a printable A4 PDF.

    python3 -I companion.py --rc1-pdf RC1.pdf --annotations DIR --out OUT.pdf [--order a,b,c]

Finds each annotation's page in the RC1 PDF by its anchor sentence (pdftotext),
takes a small shot of that page (pdftoppm), and lays out one card per item with
the excerpt, the comment, a checkbox per option and lines for the editor's answer.
"""
import argparse, base64, glob, html, json, os, re, subprocess, sys, tempfile

CHROMES = (sorted(glob.glob("/opt/pw-browsers/chromium_headless_shell-*/*/chrome-headless-shell"))
           + ["/opt/pw-browsers/chromium", "chromium", "google-chrome"])

ROLE_NAMES = {"conductor": "The conductor", "storyteller": "The storyteller", "historian": "The historian",
              "librarian": "The librarian", "researcher": "The researcher", "security": "Security",
              "publisher": "The publisher", "gen-zx": "The Gen ZX Founders team"}


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("ﬁ", "fi").replace("ﬂ", "fl").replace("-\n", "")
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def pages_text(pdf):
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout).group(1))
    out = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True).stdout
    pages = out.split("\f")[:n]
    return [norm(p) for p in pages]


def find_page(pages, anchor, chapter_hint=None):
    a = norm(anchor)
    if not a:
        return None
    for size in (len(a), 80, 50, 32):
        key = a[:size]
        hits = [i for i, p in enumerate(pages) if key in p]
        if hits:
            return hits[0] + 1
        # the anchor may break across a page: try its tail too
        key = a[-size:]
        hits = [i for i, p in enumerate(pages) if key in p]
        if hits:
            return hits[0] + 1
    return None


def shot(pdf, page, tmp):
    base = os.path.join(tmp, f"p{page}")
    subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", "55", "-jpeg", "-jpegopt", "quality=70",
                    "-singlefile", pdf, base], check=True)
    with open(base + ".jpg", "rb") as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()


def e(s):
    return html.escape(s or "")


CSS = """
@page { size: A4; margin: 16mm 16mm 18mm 16mm; }
* { box-sizing: border-box; }
body { font-family: Charter, 'Bitstream Charter', 'DejaVu Serif', serif; font-size: 10.5pt; line-height: 1.42; color: #1a1a1a; }
h1 { font-size: 26pt; margin: 0 0 6pt; line-height: 1.1; }
h2 { font-size: 17pt; margin: 0 0 4pt; break-after: avoid; }
.sans, .kind, .meta, .opts, .rec, .lbl, table { font-family: Inter, 'DejaVu Sans', sans-serif; }
.titlepage { height: 250mm; display: flex; flex-direction: column; justify-content: center; }
.titlepage .sub { font-size: 13pt; color: #444; margin-bottom: 18pt; }
.titlepage .how { font-size: 10.5pt; max-width: 150mm; }
.role { break-before: page; }
.role .summary { font-style: italic; color: #333; margin: 0 0 10pt; padding: 6pt 9pt; border-left: 3pt solid #9a6a00; background: #faf6ec; }
.role .drafted { font-family: Inter, sans-serif; font-size: 8pt; color: #777; margin-bottom: 8pt; }
.card { border: 0.8pt solid #bbb; border-radius: 3pt; padding: 8pt 10pt 9pt; margin: 0 0 9pt; break-inside: avoid; display: flow-root; }
.card .head { display: flex; gap: 8pt; align-items: baseline; margin-bottom: 4pt; }
.card .id { font-family: Inter, sans-serif; font-size: 8pt; color: #666; }
.kind { font-size: 7.5pt; text-transform: uppercase; letter-spacing: .06em; padding: 1pt 5pt; border-radius: 2pt; color: #fff; }
.k-decision { background: #9a2e00; } .k-question { background: #1f4e8c; } .k-comment { background: #555; } .k-rationale { background: #2f6b3a; }
.card .title { font-weight: bold; font-size: 11.5pt; }
.meta { font-size: 8pt; color: #555; margin-bottom: 5pt; }
.thumb { float: right; width: 34mm; margin: 0 0 4pt 9pt; border: 0.6pt solid #999; }
.excerpt { font-size: 9.5pt; color: #333; margin: 0 0 6pt; padding: 3pt 8pt; border-left: 2.5pt solid #ccc; background: #f6f6f6; }
.body { margin: 0 0 6pt; }
.opts { list-style: none; padding: 0; margin: 4pt 0 6pt; font-size: 9.5pt; }
.opts li { margin: 3pt 0; padding-left: 17pt; text-indent: -17pt; }
.box { display: inline-block; width: 9pt; height: 9pt; border: 1pt solid #222; margin-right: 6pt; vertical-align: -1pt; text-indent: 0; }
.status { font-family: Inter, sans-serif; font-size: 9pt; color: #fff; background: #2f6b3a; padding: 3pt 6pt; border-radius: 2pt; margin: 0 0 6pt; }
.rec { font-size: 9pt; color: #2f4f2f; margin: 0 0 6pt; }
.lbl { font-size: 7.5pt; color: #777; text-transform: uppercase; letter-spacing: .05em; }
.lines { margin-top: 2pt; }
.lines div { border-bottom: 0.6pt solid #aaa; height: 17pt; }
.clear { clear: both; }
table { width: 100%; border-collapse: collapse; font-size: 8.8pt; }
th, td { border-bottom: 0.5pt solid #ccc; padding: 3pt 4pt; text-align: left; vertical-align: top; }
th { font-size: 7.5pt; text-transform: uppercase; color: #555; }
.footnote { font-family: Inter, sans-serif; font-size: 8pt; color: #666; margin-top: 12pt; }
"""


def card(it, pages, shots, pdf, tmp, role):
    page = find_page(pages, it.get("anchor", ""))
    thumb = ""
    if page:
        if page not in shots:
            shots[page] = shot(pdf, page, tmp)
        thumb = f'<img class="thumb" src="{shots[page]}" alt="RC1 page {page}">'
    kind = (it.get("kind") or "comment").split()[0].lower()
    where = e(it.get("chapter", "")) + (f", RC1 page {page}" if page else ", page not found")
    claims = it.get("claim_ids") or []
    if claims:
        where += " &middot; claims " + e(", ".join(claims))
    h = [f'<div class="card">{thumb}<div class="head"><span class="kind k-{e(kind)}">{e(kind)}</span>'
         f'<span class="title">{e(it.get("title"))}</span><span class="id">{e(it.get("id"))}</span></div>',
         f'<div class="meta">{where}</div>']
    if it.get("anchor"):
        h.append(f'<div class="excerpt">{e(it["anchor"])}</div>')
    h.append(f'<div class="body">{e(it.get("body"))}</div>')
    opts = it.get("options") or []
    if opts:
        h.append('<ul class="opts">' + "".join(f'<li><span class="box"></span>{e(o)}</li>' for o in opts)
                 + '<li><span class="box"></span>Something else (below)</li></ul>')
    if it.get("status"):
        h.append(f'<div class="status"><b>Done in this RC1:</b> {e(it["status"])}</div>')
    if it.get("recommendation"):
        h.append(f'<div class="rec"><b>Recommended:</b> {e(it["recommendation"])}</div>')
    if it.get("answer_space", "lines") != "none" or opts:
        n = 3 if kind in ("question", "decision") else 2
        h.append('<div class="lbl">Your answer or note</div><div class="lines">' + "<div></div>" * n + "</div>")
    else:
        h.append('<div class="lbl"><span class="box"></span>Agreed &nbsp;&nbsp; <span class="box"></span>Not agreed (note below)</div>'
                 '<div class="lines"><div></div></div>')
    h.append('<div class="clear"></div></div>')
    return "".join(h), page, kind


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rc1-pdf", required=True)
    ap.add_argument("--annotations", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--order", default="conductor,storyteller,historian,librarian,researcher,security,publisher,gen-zx")
    ap.add_argument("--date", default="30 October 2026")
    a = ap.parse_args()

    pages = pages_text(a.rc1_pdf)
    files = {os.path.splitext(os.path.basename(p))[0]: p for p in glob.glob(os.path.join(a.annotations, "*.json"))}
    order = [r for r in a.order.split(",") if r in files] + sorted(r for r in files if r not in a.order.split(","))
    tmp = tempfile.mkdtemp(prefix="companion-")
    shots, sections, decisions, missing, counts = {}, [], [], [], {}
    for role in order:
        d = json.load(open(files[role]))
        name = ROLE_NAMES.get(role, role.title())
        body = [f'<section class="role"><h2>{e(name)}</h2>',
                f'<div class="drafted">{e(d.get("drafted_by", ""))}</div>']
        if d.get("summary"):
            body.append(f'<div class="summary">{e(d["summary"])}</div>')
        for it in d.get("items", []):
            c, page, kind = card(it, pages, shots, a.rc1_pdf, tmp, role)
            body.append(c)
            counts[kind] = counts.get(kind, 0) + 1
            if not page:
                missing.append(it.get("id"))
            if kind == "decision":
                decisions.append((it.get("id"), name, it.get("title"), page))
        body.append("</section>")
        sections.append("".join(body))

    total = sum(counts.values())
    summary = ", ".join(f"{v} {k}{'s' if v != 1 else ''}" for k, v in sorted(counts.items()))
    title = f"""<div class="titlepage"><h1>The Ultimate Insider<br>Release candidate 1: the companion</h1>
<div class="sub">Questions, comments, decisions and rationale from the team, for the editor, {e(a.date)}</div>
<div class="how"><p>Read this beside the RC1 PDF. Every card points at a sentence in RC1 and gives its page, with a small picture of that page so you can find it at a glance.</p>
<p><b>Decisions</b> have a box per option: tick one, or tick "something else" and write it. <b>Questions</b> have lines for your answer. <b>Comments</b> and <b>rationale</b> have two boxes, agreed or not agreed. Nothing here is decided until you sign it: when you are back, the conductor turns your ticks into open decisions in <span class="sans">book.json</span> for you to sign.</p>
<p>The role sections were drafted by the conductor's sub-agents, each reading RC1 as that role. They are not the members' own words; each member reviews its section at its next wake. Every number comes from the researcher's register.</p>
<p class="sans" style="font-size:9pt;color:#555">{total} cards: {e(summary)}. The last pages list every decision on one sheet.</p></div></div>"""
    rows = "".join(f"<tr><td>{e(i)}</td><td>{e(n)}</td><td>{e(t)}</td><td>{p or ''}</td><td><span class='box'></span></td></tr>"
                   for i, n, t, p in decisions)
    sheet = (f'<section class="role"><h2>Every decision on one sheet</h2><table><tr><th>Card</th><th>From</th><th>Decision</th>'
             f'<th>RC1 page</th><th>Done</th></tr>{rows}</table>'
             f'<div class="footnote">Made from team/conductor/rc1/annotations/ in the book repository; the cards and RC1 are both release candidate 1.</div></section>')
    doc = f"<!doctype html><html lang='en-GB'><head><meta charset='utf-8'><title>RC1 companion</title><style>{CSS}</style></head><body>{title}{''.join(sections)}{sheet}</body></html>"
    htmlp = os.path.join(tmp, "companion.html")
    open(htmlp, "w").write(doc)
    chrome = next((c for c in CHROMES if os.path.exists(c) or subprocess.run(["which", c], capture_output=True).returncode == 0), None)
    if not chrome:
        sys.exit("companion: no Chrome found")
    subprocess.run([chrome, "--headless", "--no-sandbox", "--disable-gpu", f"--user-data-dir={tmp}/profile",
                    "--no-pdf-header-footer", f"--print-to-pdf={os.path.abspath(a.out)}", "file://" + htmlp],
                   check=True, capture_output=True)
    print(f"companion: {total} cards, {len(decisions)} decisions, {len(shots)} page shots -> {a.out}")
    if missing:
        print("companion: anchors not found in RC1:", ", ".join(missing))


if __name__ == "__main__":
    main()
