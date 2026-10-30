"""Preview an experiment folder as the lab would set it: the designer's lab.css, header() and page() (lab/tools, read only),
then this folder's pages.html with {{dir}} set to the folder. Writes page.html; print it with tools/print.js to page.pdf.
Usage: python3 -I lab/experiments/03-ruv-could-have-been-worse-frames/tools/preview.py <experiment folder>
"""
import html, importlib.util, json, re, sys
from pathlib import Path

d = Path(sys.argv[1]).resolve()
LAB = d.parents[1]
spec = importlib.util.spec_from_file_location('build_lab', LAB / 'tools' / 'build_lab.py')
bl = importlib.util.module_from_spec(spec); spec.loader.exec_module(bl)
meta = json.loads((d / 'experiment.json').read_text())
secs = re.findall(r'<section class="page"(?: data-claims="([^"]*)")?>(.*?)</section>', (d / 'pages.html').read_text().replace('{{dir}}', '.'), re.S)
assert len(secs) == meta['pages'], f'{len(secs)} pages, experiment.json says {meta["pages"]}'
pages = [bl.page((bl.header(meta) if i == 0 else '') + inner, meta['id'], claims) for i, (claims, inner) in enumerate(secs)]
body = ''.join(p.replace('{n}', str(i + 1)).replace('{N}', str(len(pages))) for i, p in enumerate(pages))
(d / 'page.html').write_text(f'<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>{html.escape(meta["title"])}</title>'
                             f'<style>{(LAB / "tools" / "lab.css").read_text()}</style></head><body>{body}</body></html>\n')
