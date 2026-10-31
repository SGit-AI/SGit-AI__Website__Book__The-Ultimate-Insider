# The Personas section of the site, built from synthetic@'s files (synthetic@book.the-ultimate-insider).
#
#   python3 review/synthetic/tools/build_section.py          # writes src/pages/personas/ and review/synthetic/pdf/debrief.html
#   node review/synthetic/tools/print_pdf.mjs                 # prints that debrief to src/static/personas/
#
# Reads review/synthetic/personas.json, rc1/<persona>.json, rc1/briefing.md, names/*.json, the page runs in
# <persona>/<run>/review.md and reading-time.md. Every page says SYNTHETIC READER at its top: a test instrument,
# never a reader, never evidence about the book, never readership.

import html
import json
import re
from pathlib import Path

ROOT  = Path(__file__).resolve().parents[3]
SYN   = ROOT / 'review' / 'synthetic'
PAGES = ROOT / 'src' / 'pages' / 'personas'
PDF   = SYN / 'pdf'
GH    = 'https://github.com/SGit-AI/SGit-AI__Website__Book__The-Ultimate-Insider/blob/dev/'

LABEL = ('<p class="note" style="border:1px dashed currentColor;padding:.6em .8em"><b>SYNTHETIC READERS.</b> Every persona here is fictional: '
         'a test instrument made by synthetic@, never a reader. What they say is a prompt for the team, never evidence about the book, '
         'never counted as readership. Real readers, chosen by the editor, are the test that counts.</p>')

e = html.escape


def md(text):                                                       # the little markdown these files use: headings, lists, paragraphs, bold, code
    out, items = [], []
    def inline(s):
        s = e(s)
        s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
        s = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', s)
        return s
    def flush():
        if items:
            out.append('<ul>' + ''.join(f'<li>{inline(i)}</li>' for i in items) + '</ul>')
            items.clear()
    for block in re.split(r'\n\s*\n', text.strip()):
        lines = block.strip().split('\n')
        if all(re.match(r'\s*(- |\d+\. )', l) for l in lines):
            items.extend(re.sub(r'^\s*(- |\d+\. )', '', l) for l in lines)
            continue
        flush()
        if lines[0].startswith('#'):
            level = min(len(lines[0]) - len(lines[0].lstrip('#')) + 1, 4)
            out.append(f'<h{level}>{inline(lines[0].lstrip("# "))}</h{level}>')
            if len(lines) > 1:
                out.append(f'<p>{inline(" ".join(lines[1:]))}</p>')
        else:
            out.append(f'<p>{inline(" ".join(lines))}</p>')
    flush()
    return '\n'.join(out)


def strip_title(text):
    return re.sub(r'^# .*\n', '', text, count=1)


def load():
    personas = json.loads((SYN / 'personas.json').read_text())['personas']
    rc1      = {p['id']: json.loads((SYN / 'rc1' / f'{p["id"]}.json').read_text()) for p in personas if (SYN / 'rc1' / f'{p["id"]}.json').exists()}
    names    = sorted((SYN / 'names').glob('*.json'))
    names    = json.loads(names[-1].read_text()) if names else None
    runs     = {}
    for p in personas:
        found = sorted((SYN / p['id']).glob('*/review.md')) if (SYN / p['id']).exists() else []
        if found:
            runs[p['id']] = found[-1]
    return personas, rc1, names, runs


def score_table(scores):
    rows = ''.join(f'<tr><th>{e(k.replace("_", " "))}</th><td><b>{v["score"]}</b> / 5</td><td>{e(v["why"])}</td></tr>' for k, v in scores.items())
    return f'<div class="tbl"><table><tbody>{rows}</tbody></table></div>'


def run_scores(path):                                               # the scores table of a page run's review.md, as HTML
    text = path.read_text()
    m = re.search(r'## Scores.*?\n((?:\|.*\n)+)', text, re.S)
    if not m:
        return ''
    rows = [r.strip().strip('|').split('|') for r in m.group(1).strip().split('\n')]
    rows = [r for r in rows if not re.match(r'^\s*-+\s*$', r[0])]
    head, body = rows[0], rows[1:]
    return ('<div class="tbl"><table><thead><tr>' + ''.join(f'<th>{e(c.strip())}</th>' for c in head) + '</tr></thead><tbody>'
            + ''.join('<tr>' + ''.join(f'<td>{e(c.strip())}</td>' for c in r) + '</tr>' for r in body) + '</tbody></table></div>')


def persona_page(p, r, names, run):
    buy  = r['exit_interview']['would_you_buy'] if r else 'not read yet'
    head = (f'<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Personas</a></nav>'
            f'<p class="kicker">Synthetic reader · {e(p["device"]["note"])} · {p["time_budget_minutes"]} minutes</p><h1>The {e(p["label"].lower() if p["label"] != "CISO" and p["label"] != "CTO" else p["label"])}</h1>'
            f'<p class="lead">{e(p["who"])}</p>{LABEL}')
    who  = (f'<h2 id="who">Who, and what they judge</h2><div class="tbl"><table><tbody>'
            f'<tr><th>Judges</th><td>{e(p["judges"])}</td></tr>'
            f'<tr><th>Device</th><td>{e(p["device"]["playwright"])} ({e(p["device"]["note"])})</td></tr>'
            f'<tr><th>Time they give</th><td>{p["time_budget_minutes"]} minutes</td></tr>'
            f'<tr><th>Voice</th><td>{e(p["voice"])}</td></tr>'
            f'<tr><th>Impressed by</th><td>{e(p["impressed_by"])}</td></tr>'
            f'<tr><th>Lost by</th><td>{e("; ".join(p["deal_breakers"]))}</td></tr></tbody></table></div>')
    body = head + who
    if r:
        x = r['exit_interview']
        mins = round(sum(WORDS.get(c, 0) for c in r['chapters']) / 250)
        body += (f'<h2 id="rc1">What they thought of RC1</h2>'
                 f'<p class="note">Read: {", ".join(f"<code>{e(c)}</code>" for c in r["chapters"])} from RC1 as locked (<code>team/conductor/rc1/</code>), about {mins} minutes at 250 words a minute, against {p["time_budget_minutes"]} they give.</p>'
                 f'<blockquote><p>{e(r["one_sentence"])}</p></blockquote>'
                 f'<p><b>Would they buy it?</b> {e(buy)}. {e(x["why"])} <span class="c-dim">({e(x["price_or_format"])}; would recommend it to: {e(x["recommend_to"])})</span></p>'
                 f'<h3>Scores</h3>{score_table(r["scores"])}'
                 f'<h3 id="exit">The exit interview</h3><div class="tbl"><table><tbody>'
                 + ''.join(f'<tr><th>{e(q)}</th><td>{e(x[k])}</td></tr>' for k, q in [
                     ('what_is_this_book', 'What is this book?'), ('where_did_you_get_stuck', 'Where did you get stuck?'),
                     ('what_did_you_skip', 'What did you skip?'), ('what_will_you_remember', 'What will you remember?'),
                     ('what_is_missing', 'What is missing for someone like you?')])
                 + '</tbody></table></div><h3>Their own questions</h3><div class="tbl"><table><tbody>'
                 + ''.join(f'<tr><th>{e(q["q"])}</th><td>{e(q["a"])}</td></tr>' for q in x.get('your_questions', []))
                 + '</tbody></table></div><h3 id="stuck">Chapter by chapter, and where they got stuck</h3>')
        for c in r['by_chapter']:
            body += (f'<h4><code>{e(c["chapter"])}</code> · {e(c["read"])}</h4><p><b>Landed:</b> {e(c["landed"])}</p>'
                     + (''.join(f'<blockquote><p>"{e(s["quote"])}"</p></blockquote><p class="note">{e(s["why"])}</p>' for s in c.get('stuck', [])))
                     + f'<p><b>Would cut:</b> {e(c["cut"])} · <b>Missing:</b> {e(c["missing"])}</p>')
    else:
        body += '<h2 id="rc1">What they thought of RC1</h2><p>Not read yet.</p>'
    if run:
        rel = run.relative_to(ROOT)
        body += (f'<h2 id="pages">Their review page</h2><p>The latest run through the review page made for them, in a real browser on their device '
                 f'(<a href="{GH}{e(str(rel))}">the review, on GitHub</a>):</p>{run_scores(run)}')
    else:
        body += '<h2 id="pages">Their review page</h2><p class="note">No review page made for this persona yet; it runs when the developer builds one.</p>'
    if names:
        n = next((x for x in names['personas'] if x['persona'] == p['id']), None)
        if n:
            body += f'<h2 id="name">The name test</h2><p>Would pick up <b>{e(n["picks_up"])}</b>: {e(n["why"])}</p>'
    body += f'<p class="note">Source: <code>review/synthetic/</code> (personas.json, rc1/{e(p["id"])}.json); built by <code>review/synthetic/tools/build_section.py</code>.</p>'
    meta = json.dumps({'title': f'Persona: the {p["label"]}', 'description': f'A synthetic reader (fictional, a test instrument): {p["judges"]} What they thought of RC1, where they got stuck, and whether they would buy it.'})
    return f'<!--meta {meta} -->\n<section class="prose wrap narrow">{body}</section>\n'


def index_page(personas, rc1, names, runs):
    rows = ''
    for p in personas:
        r = rc1.get(p['id'])
        s = r['scores'] if r else {}
        rows += (f'<tr><td><a href="{p["id"]}.html">{e(p["label"])}</a></td><td>{e(r["exit_interview"]["would_you_buy"]) if r else "not read"}</td>'
                 + ''.join(f'<td>{s[k]["score"] if k in s else ""}</td>' for k in ('got_the_answer', 'clarity', 'trust', 'pace', 'would_buy'))
                 + f'<td>{e(r["one_sentence"]) if r else ""}</td></tr>')
    brief = (SYN / 'rc1' / 'briefing.md').read_text() if (SYN / 'rc1' / 'briefing.md').exists() else ''
    rt    = (SYN / 'reading-time.md').read_text()
    body = ('<p class="kicker">Synthetic readers · kept by synthetic@</p><h1>The personas</h1>'
            '<p class="lead">Eight fictional readers who try everything before a real reviewer does: the review pages, the book, the title. '
            'Each has a page with who they are, what they thought of RC1, where they got stuck, and whether they would buy it.</p>' + LABEL
            + '<p class="btns"><a class="btn p" href="personas-rc1-debrief.pdf">The PDF debrief</a></p>'
            + '<h2 id="rc1">RC1, as the personas read it</h2><div class="tbl"><table><thead><tr><th>Persona</th><th>Would buy</th>'
              '<th>Answer</th><th>Clarity</th><th>Trust</th><th>Pace</th><th>Buy</th><th>The book, in one sentence</th></tr></thead>'
            + f'<tbody>{rows}</tbody></table></div><p class="note">Scores 1 to 5. Each persona read the RC1 chapters for its kind of reader, not the whole book.</p>'
            + (f'<h2 id="briefing">The briefing</h2>{md(strip_title(brief))}' if brief else '')
            + f'<h2 id="time">Reading time: a proposal</h2>{md(strip_title(rt))}'
            + '<h2 id="how">How they work</h2><ul>'
              '<li><b>When they run:</b> at a major change to what readers see (a new review page, a new release candidate), or when someone has a question for them; not on a timer.</li>'
              '<li><b>The review pages:</b> each persona opens its page in a real browser on its own device; every request leaving the page is blocked and listed.</li>'
              '<li><b>The book:</b> each persona reads the chapters chosen for its kind of reader, in its own voice, and answers an exit interview.</li>'
              f'<li><b>Everything is in the repository:</b> <a href="{GH}review/synthetic/">review/synthetic/</a>.</li></ul>')
    meta = json.dumps({'title': 'The personas', 'description': 'Eight synthetic readers (fictional, test instruments): what each thought of RC1, where they got stuck, and whether they would buy the book.'})
    return f'<!--meta {meta} -->\n<section class="prose wrap narrow">{body}</section>\n'


def pdf_html(personas, rc1):                                        # one self-contained page set for Chromium to print
    css = ('@page{size:A4;margin:16mm 16mm 18mm}body{font:10.5pt/1.45 Georgia,serif;color:#111}h1{font-size:22pt;margin:0 0 4mm}'
           'h2{font-size:14pt;margin:7mm 0 2mm;page-break-after:avoid}h3{font-size:11pt;margin:4mm 0 1mm}.p{page-break-before:always}'
           '.lab{border:1px dashed #555;padding:2mm 3mm;font:9pt/1.35 sans-serif}table{border-collapse:collapse;width:100%;font:9pt/1.3 sans-serif}'
           'td,th{border-bottom:1px solid #ccc;padding:1.2mm 1.5mm;text-align:left;vertical-align:top}blockquote{margin:2mm 0 2mm 4mm;font-style:italic}'
           '.k{font:8.5pt sans-serif;letter-spacing:.06em;text-transform:uppercase;color:#555}code{font-size:9pt}')
    lab = ('<p class="lab"><b>SYNTHETIC READERS.</b> Fictional personas, test instruments made by synthetic@book.the-ultimate-insider: '
           'never readers, never evidence about the book, never readership.</p>')
    brief = (SYN / 'rc1' / 'briefing.md').read_text() if (SYN / 'rc1' / 'briefing.md').exists() else ''
    rows = ''.join(f'<tr><td>{e(p["label"])}</td><td>{e(rc1[p["id"]]["exit_interview"]["would_you_buy"])}</td>'
                   + ''.join(f'<td>{rc1[p["id"]]["scores"][k]["score"]}</td>' for k in ('got_the_answer', 'clarity', 'trust', 'pace', 'would_buy'))
                   + '</tr>' for p in personas if p['id'] in rc1)
    out = (f'<p class="k">The ultimate insider · RC1 · synthetic readers</p><h1>What the personas thought of RC1</h1>{lab}'
           f'<table><thead><tr><th>Persona</th><th>Would buy</th><th>Answer</th><th>Clarity</th><th>Trust</th><th>Pace</th><th>Buy</th></tr></thead><tbody>{rows}</tbody></table>'
           f'{md(strip_title(brief))}')
    for p in personas:
        r = rc1.get(p['id'])
        if not r:
            continue
        x = r['exit_interview']
        out += (f'<div class="p"><p class="k">Persona · {e(p["device"]["note"])} · {p["time_budget_minutes"]} minutes · read {", ".join(e(c) for c in r["chapters"])}</p>'
                f'<h2>The {e(p["label"])}</h2><p>{e(p["who"])} <i>Judges: {e(p["judges"])}</i></p>{lab}'
                f'<blockquote>{e(r["one_sentence"])}</blockquote><p><b>Would buy: {e(x["would_you_buy"])}.</b> {e(x["why"])} ({e(x["price_or_format"])})</p>'
                f'<table><tbody>' + ''.join(f'<tr><th>{e(k.replace("_", " "))}</th><td>{v["score"]}</td><td>{e(v["why"])}</td></tr>' for k, v in r['scores'].items()) + '</tbody></table>'
                f'<h3>Where they got stuck</h3><p>{e(x["where_did_you_get_stuck"])}</p>'
                + ''.join(f'<blockquote>"{e(s["quote"])}" ({e(c["chapter"])})</blockquote><p>{e(s["why"])}</p>' for c in r['by_chapter'] for s in c.get('stuck', [])[:2])
                + f'<h3>Skipped, remembered, missing</h3><p><b>Skipped:</b> {e(x["what_did_you_skip"])}</p><p><b>Will remember:</b> {e(x["what_will_you_remember"])}</p>'
                f'<p><b>Missing:</b> {e(x["what_is_missing"])}</p></div>')
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Personas: RC1 debrief</title><style>{css}</style></head><body>{out}</body></html>'


WORDS = {}


def main():
    personas, rc1, names, runs = load()
    for f in (ROOT / 'team' / 'conductor' / 'rc1').glob('*.md'):
        WORDS[f.stem] = len(f.read_text().split())
    PAGES.mkdir(parents=True, exist_ok=True)
    PDF.mkdir(parents=True, exist_ok=True)
    (PAGES / 'index.html').write_text(index_page(personas, rc1, names, runs))
    for p in personas:
        (PAGES / f'{p["id"]}.html').write_text(persona_page(p, rc1.get(p['id']), names, runs.get(p['id'])))
    (PDF / 'debrief.html').write_text(pdf_html(personas, rc1))
    print(f'personas: {len(personas)} pages, {len(rc1)} RC1 reads, PDF source {PDF / "debrief.html"}')


if __name__ == '__main__':
    main()
