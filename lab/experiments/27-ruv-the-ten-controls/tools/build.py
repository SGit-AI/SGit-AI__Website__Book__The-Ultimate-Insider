"""LAB 25 (ruv): chapter 9's ten controls, read across (the editor's LK1; ruv.sgit's visual plan).

Reads rows.json (each row's phrases taken from the control's own section of manuscript/09-the-team-was-the-insider.md, and the
shape of its miss from the chapter's "What the controls missed, together") and writes pages.html: one grid, grouped by kind as the
chapter sorts them, with C10, the one control that refused on its own authority, marked. The team's own controls only; no number.
Usage: python3 -B -I tools/build.py
"""
import html, json
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SHAPE = {'refused on its own authority': 'background:var(--accent);color:var(--paper)',
         'reported without refusing': 'background:var(--fill-2)', 'rested on the member running it': 'background:var(--fill-2)',
         'waited on a role nobody held': 'background:var(--fill-2)', 'pulled by a person': 'background:var(--tint)'}
TD = 'padding:1.2mm 2mm;border-top:.25mm solid var(--fill-2);vertical-align:top;font:400 9pt/11.5pt var(--sans)'


def e(s):
    return html.escape(s, quote=False)


def main():
    d = json.loads((HERE / 'rows.json').read_text())
    rows = []
    for k in d['kinds']:
        rows.append(f'<tr><td colspan="4" style="padding:3mm 0 1mm;font:700 9pt/12pt var(--sans);text-transform:uppercase;letter-spacing:.06em;color:var(--muted)">'
                    f'{e(k["kind"])} <span style="text-transform:none;letter-spacing:0;font-weight:400">: {e(k["say"])}</span></td></tr>')
        for r in k['rows']:
            mark = r['shape'] == 'refused on its own authority'
            bg = ';background:var(--tint)' if mark else ''
            tag = SHAPE.get(r['shape'], 'border:.25mm solid var(--fill-2);color:var(--muted)')
            rows.append(f'<tr><td style="{TD}{bg};width:36mm"><b>{e(r["id"])}</b> {e(r["name"])}</td>'
                        f'<td style="{TD}{bg};width:44mm">{e(r["stopped"])}</td>'
                        f'<td style="{TD}{bg};width:50mm">{e(r["missed"])}</td>'
                        f'<td style="{TD}{bg}"><span style="display:inline-block;padding:.4mm 1.4mm;border-radius:1mm;{tag}">{e(r["shape"])}</span></td></tr>')
    th = 'text-align:left;padding:0 2mm 1mm;font:700 9pt/12pt var(--sans);color:var(--muted)'
    (HERE / 'pages.html').write_text(
        '<section class="page" data-claims="">\n <figure class="fig span12">\n'
        '  <p class="fig-title">The ten controls, read across</p>\n'
        f'  <table style="border-collapse:collapse;width:100%"><thead><tr><th style="{th}">Control</th><th style="{th}">What it stopped</th>'
        f'<th style="{th}">What it missed</th><th style="{th}">The shape of the miss</th></tr></thead><tbody>\n  '
        + '\n  '.join(rows) + '\n  </tbody></table>\n'
        '  <figcaption><b>Read down the last column: each miss either reported without refusing, rested on the member running it, or waited on a role nobody held. '
        'The one brake that stopped the team was pulled by a person; the one control that refused an agent on its own authority sat outside the repository.</b>'
        '<span class="src">Chapter 9: each row from its control\'s own section; the shapes from "What the controls missed, together" (C7\'s and C9\'s in the chapter\'s words).</span></figcaption>\n'
        ' </figure>\n</section>\n')


if __name__ == '__main__':
    main()
