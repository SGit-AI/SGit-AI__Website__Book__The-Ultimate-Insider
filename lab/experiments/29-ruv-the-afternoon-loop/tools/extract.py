"""LAB 29 (ruv), proposed: the afternoon loop (RC2's chapter 3, page 4; chapter-plan/edition-30-outline.md: "the loop drawn over
the afternoon: each of his asks, and what came back, on one line of time; for ruv-sgit, from the commits that carry his time
in their subject").

Reads the talk repository's history at 298be4e (read only) and keeps every commit whose subject carries the editor's time,
"(the editor, HH:MM)" or "the editor, HH:MM:", leaving out the release commits ("site v...") that repeat a subject. For each:
the time he asked (from the subject), the commit's own time, its hash, and the subject. Nothing is drawn from this until the
researcher registers it: every number on a page comes from the register.
Usage: python3 -B -I tools/extract.py --talk <clone of the talk's repository>
"""
import json, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
AT = '298be4e'
PAT = re.compile(r'the editor,? (\d{1,2}:\d{2})')


def main():
    clone = sys.argv[sys.argv.index('--talk') + 1]
    log = subprocess.run(['git', '-C', clone, 'log', AT, '--format=%h\t%ad\t%s', '--date=format-local:%H:%M:%S'],
                         capture_output=True, text=True, check=True, env={'TZ': 'UTC', 'PATH': '/usr/bin:/bin'}).stdout
    rows = []
    for line in log.splitlines():
        h, t, s = line.split('\t', 2)
        if s.startswith('site v') or s.startswith('Merge'):
            continue
        m = PAT.search(s)
        if m:
            rows.append({'asked': m.group(1).zfill(5), 'landed': t, 'commit': h, 'subject': s})
    rows.sort(key=lambda r: r['landed'])
    (HERE / 'data' / 'asks.json').write_text(json.dumps({'source': f'the talk repository\'s commit subjects at {AT} (read only), UTC',
                                                         'pattern': PAT.pattern, 'rows': rows}, indent=1, ensure_ascii=False) + '\n')
    print(f'{len(rows)} commits carry the editor\'s time')


if __name__ == '__main__':
    main()
