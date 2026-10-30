# Makes one review page per persona from review/personas/<id>.json and the edition it names (RC1: team/conductor/rc1/),
# written to src/pages/review/<id>.html, so the site's build wraps it like any page; and places the hand-written sources,
# review/pages/ and review/static/, in src/pages/review/ and src/static/review/. Every paragraph, quote, list item and table
# gets a stable anchor, <chapter>-<first 6 hex of the sha256 of its text>: it survives a paragraph moving and changes when
# the words change, which is what the diffs need. The anchors are also written to review/anchors/<edition>.json.
# The placed files are committed too, so the site's build needs no step of its own: run this after changing review/.
# Standard library only; reads admin/build/build.py's Markdown, writes only review/, src/pages/review/ and src/static/review/.
# Kept by developer@book.the-ultimate-insider. Run: python3 review/tools/make_review.py [<persona> ...]
import hashlib, html, json, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'admin' / 'build'))
from build import Markdown                                          # noqa: E402

PERSONAS = ROOT / 'review' / 'personas'
ANCHORS  = ROOT / 'review' / 'anchors'
PAGES    = ROOT / 'src' / 'pages' / 'review'
STATIC   = ROOT / 'src' / 'static' / 'review'
WPM      = 230                                                      # reading speed for the time estimates
MARKS    = ['agree', 'unclear', 'wrong', 'cut', 'more']


def plain(fragment):                                                # the words of a block, as the anchor hashes them (an image by its alt text)
    fragment = re.sub(r'<img [^>]*alt="([^"]*)"[^>]*>', r' \1 ', fragment)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', fragment))).strip()


def anchored(chapter_html, ch, seen, register, chapter_file):
    out = []
    for line in chapter_html.split('\n'):
        m = re.match(r'<h(\d) id="([^"]*)">(.*)</h\d>$', line)
        if m:                                                       # headings one level down, ids made unique per chapter
            level = min(int(m.group(1)) + 1, 6)
            out.append(f'<h{level} id="c{ch}-{m.group(2)}">{m.group(3)}</h{level}>')
            continue
        m = re.match(r'<(ul|ol)>(.*)</\1>$', line)
        if m:
            items = re.findall(r'<li>(.*?)</li>', m.group(2))
            lis = ''.join(f'<li{attrs(a)}>{body}</li>' for body in items for a in [anchor(body, ch, seen, register, chapter_file)])
            out.append(f'<{m.group(1)}>{lis}</{m.group(1)}>')
            continue
        m = re.match(r'<(p|blockquote|div class="tbl")>(.*)</(p|blockquote|div)>$', line)
        if m:
            a = anchor(m.group(2), ch, seen, register, chapter_file)
            tag = m.group(1).split()[0]
            cls = ' class="tbl"' if tag == 'div' else ''
            out.append(f'<{tag}{cls}{attrs(a)}>{m.group(2)}</{tag}>')
            continue
        out.append(line)                                            # code blocks and raw html pass through unanchored
    return '\n'.join(out)


def anchor(fragment, ch, seen, register, chapter_file):
    text = plain(fragment)
    base = f'{ch}-{hashlib.sha256(text.encode()).hexdigest()[:6]}'
    seen[base] = seen.get(base, 0) + 1
    aid = base if seen[base] == 1 else f'{base}-{seen[base]}'
    register.append({'id': aid, 'chapter': chapter_file, 'n': len([r for r in register if r['chapter'] == chapter_file]) + 1,
                     'sha256': hashlib.sha256(text.encode()).hexdigest(), 'starts': text[:80]})
    return aid


def attrs(aid):
    return f' id="{aid}" data-a="{aid}" tabindex="0"'


def chapter(source, file, register):
    text = (source / file).read_text()
    ch = file.split('-')[0]
    title = re.match(r'# (.*)', text).group(1)
    body = text.split('\n', 1)[1]
    body = re.sub(r'\]\(resources/', '](../book/resources/', body)  # the chapters' images, where the site publishes them
    words = len(re.findall(r'\S+', body))
    return ch, title, words, anchored(Markdown().to_html(body), ch, {}, register, file)


def page(p):
    e = p['edition']
    source = ROOT / e['source']
    register, parts, toc, total = [], [], [], 0
    for c in p['chapters']:
        ch, title, words, body = chapter(source, c['file'], register)
        minutes = round(words / WPM)
        total += minutes
        esc = html.escape(title)
        toc.append(f'<li><a href="#c{ch}">{esc}</a> <span class="c-dim">about {minutes} minutes · {html.escape(c["why"])}</span></li>')
        qs = [q for q in p['questions'] if q['after'] == c['file']]
        qhtml = ''
        if qs:
            items = ''.join(f'<li><p>{html.escape(q["q"])}</p><textarea data-q="{ch}-q{i}" rows="3" aria-label="Your answer"></textarea></li>'
                            for i, q in enumerate(qs, 1))
            qhtml = (f'<section class="rv-qs" aria-label="Questions on this chapter"><h3>Questions on this chapter</h3><ol>{items}</ol>'
                     f'<p class="note">Placeholder questions, from the reviewers study; the storyteller writes the final ones.</p></section>')
        parts.append(f'<article class="rv-ch" id="c{ch}" data-ch="{ch}"><h2>{esc}</h2>\n{body}\n{qhtml}</article>')
    gets = ''.join(f'<li>{html.escape(g)}</li>' for g in p['gets'])
    marks = ''.join(f'<li><b>{m}</b></li>' for m in MARKS)
    n = ['no', 'one', 'two', 'three', 'four', 'five'][len(p['chapters'])] if len(p['chapters']) <= 5 else str(len(p['chapters']))
    count = f'{n} chapter' + ('' if len(p['chapters']) == 1 else 's')
    meta = {'title': f'Review: {p["title"].lower()}',
            'description': f'A first review page of {e["name"]} for one kind of reader, {p["reader"]}: {count} with a pen on every paragraph. '
                           'A prototype with fictional data; nobody has been sent it.'}
    head = f'''<!--meta {json.dumps(meta)} -->
<link rel="stylesheet" href="{{{{root}}}}review/pen.css">
<div class="rv wrap" data-no-third-party data-review="{p['persona']}" data-edition="{e['name']}" data-commit="{e['commit']}">
<p class="rv-proto">Prototype, fictional data. Nobody has been sent this page; a kind of reader, not a person, is named here. Made by <code>review/tools/make_review.py</code> from <code>review/personas/{p['persona']}.json</code>.</p>
<div class="rv-grid">
<div class="rv-main">
<section class="rv-intro" id="intro">
<p class="kicker">{html.escape(e['name'])} · a review copy {html.escape(p['title'].lower())}</p>
<h1>Dear <span data-to>reader</span>, would you read {count}?</h1>
<p class="lead">From the editor of <em>The ultimate insider</em>, a book about one day in which one person and a team of AI agents built a talk, with the record to prove it.</p>
<dl class="rv-facts">
<dt>Why you</dt><dd>{html.escape(p['why_you'])}</dd>
<dt>What we would like</dt><dd>{count[0].upper() + count[1:]}, about {total} minutes, by {html.escape(p['ask']['by'])} <span class="c-dim">({html.escape(p['ask']['by_note'])})</span>, and your answers to a few questions at the end of each.</dd>
<dt>What you get back</dt><dd><ul>{gets}</ul></dd>
</dl>
<ol class="rv-toc">{''.join(toc)}</ol>
<p class="rv-how1"><b>To comment</b>, click any paragraph: pick a mark, add a line, or both. Your comments stay in this browser until you send them.</p>
</section>
'''
    tail = f'''<section class="rv-send" id="send">
<h2>Sending it back</h2>
<p><span data-tally>No comments yet.</span></p>
<p class="btns"><button type="button" class="btn p" data-export>Save my comments as a file</button> <button type="button" class="btn" data-clear>Clear my comments</button></p>
<p class="note">This first version only saves a file on your own machine. The next sends it sealed to the editor's key, so only he can open it (see How this works).</p>
</section>
</div>
<aside class="rv-side" aria-label="How this works">
<details open><summary>How this works</summary>
<ol>
<li><b>Your link.</b> Anything after the <code>#</code> in your link (here, the name in the greeting) stays in your browser: browsers never send that part to a server. Try <a href="#to=Sam%20Example">#to=Sam Example</a>.</li>
<li><b>Exact words.</b> Every paragraph has an anchor made from its own words. A comment points at those words, and when a revision changes them, the anchor changes too, so we can show you what your comment changed.</li>
<li><b>Your pen.</b> Five marks:<ul class="rv-marks">{marks}</ul></li>
<li><b>Nothing leaves.</b> Comments are kept in this browser only (<code>localStorage</code>), and the pen makes no network call. Nor does the rest of the page: the site's scripts ask no third party on review pages.</li>
<li><b>Sealed, next.</b> Sending will encrypt your comments to the editor's public key before they leave your machine.</li>
</ol>
</details>
</aside>
</div>
</div>
<nav class="rv-jump" aria-label="On this page"><a href="#intro">Chapters</a><a href="#send">Send it back</a></nav>
<script src="{{{{root}}}}review/pen.js" defer></script>
'''
    return head + '\n'.join(parts) + '\n' + tail, register


def main(ids):
    ids = ids or sorted(p.stem for p in PERSONAS.glob('*.json'))
    PAGES.mkdir(parents=True, exist_ok=True)
    ANCHORS.mkdir(parents=True, exist_ok=True)
    for src, dst in ((ROOT / 'review' / 'pages', PAGES), (ROOT / 'review' / 'static', STATIC)):
        dst.mkdir(parents=True, exist_ok=True)
        for f in sorted(src.glob('*')):
            shutil.copyfile(f, dst / f.name)
    for pid in ids:
        p = json.loads((PERSONAS / f'{pid}.json').read_text())
        text, register = page(p)
        (PAGES / f'{pid}.html').write_text(text)
        ed = p['edition']
        reg_path = ANCHORS / f'{ed["name"].lower()}.json'
        reg = json.loads(reg_path.read_text()) if reg_path.exists() else {'edition': ed['name'], 'commit': ed['commit'], 'source': ed['source'], 'anchors': {}}
        for r in register:
            reg['anchors'][r['id']] = {k: v for k, v in r.items() if k != 'id'}
        reg['anchors'] = dict(sorted(reg['anchors'].items()))
        reg_path.write_text(json.dumps(reg, indent=1, ensure_ascii=False) + '\n')
        print(f'review: {pid} -> src/pages/review/{pid}.html ({len(register)} anchors)')


if __name__ == '__main__':
    main(sys.argv[1:])
