# Tests for print_check.chapters_json_starts: the chapters file the build writes beside its PDF is untrusted data (security__011 to 013: no guard
# turned off; this tool never fetches). It is read as JSON only, checked for shape and size, and ignored on any fault. Prints ok.
# Run: python3 -I review/tools/test_print_check_json.py

import json, sys, tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import print_check as pc   # noqa: E402

CH = [{'file': 'manuscript/rc2/150/00-start-here.md'}, {'file': 'manuscript/rc2/150/01-a.md'}, {'file': 'manuscript/rc2/150/02-b.md'}]
BY_TITLE = [3, 9, 14]            # what the title finder found


def run(data, n=50, raw=None, size=None):
    with tempfile.TemporaryDirectory() as d:
        f = Path(d) / 'c.json'
        f.write_text(raw if raw is not None else json.dumps(data))
        return pc.chapters_json_starts(f, n, CH, BY_TITLE)


def rows(*pages, names=('01-a.md', '02-b.md')):
    return {'pdf': 'x.pdf', 'chapters': [{'file': 'manuscript/rc2/150/' + nm, 'title': 'T', 'part': 1, 'page': pg} for nm, pg in zip(names, pages)]}


# a good file: the two chapters it names take its pages, the unnamed one keeps the title finder's; one disagrees
s, c, why = run(rows(7, 14))
assert why is None and s == [3, 7, 14], (s, c, why)
assert c == {'in_file': 2, 'matched': 2, 'disagree_with_the_title_finder': 1}, c

# every fault: ignored, with a fixed sentence that quotes nothing from the file
for bad in (rows(7, 7),                           # pages that do not increase
            rows(9, 99),                          # a page outside the PDF
            rows(0, 5),                           # page 0
            {'chapters': []}, {'chapters': 'x'}, {'nope': 1}, [1, 2],       # no usable list
            {'chapters': [{'file': 'x' * 300, 'page': 5}]},               # file name too long
            {'chapters': [{'file': 'a.md', 'page': True}]},               # a bool is not a page
            {'chapters': [{'file': 7, 'page': 5}]},                       # file not a string
            {'chapters': [1, 2, 3]},                                       # entries not objects
            {'chapters': [{'file': 'a.md', 'page': 1}] * 201}):            # too many entries
    s, c, why = run(bad)
    assert s is None and c is None and why and 'ignored' in why, (bad, s, why)

s, c, why = run(None, raw='{not json')
assert s is None and why and 'ignored' in why
s, c, why = run(None, raw='\xff')
assert s is None and why

# a file whose pages do not fit the chapters' order (the second chapter would start before the first): ignored
s, c, why = run(rows(5, 8, names=('02-b.md', '01-a.md')))
assert s is None and why, (s, why)

# the fault sentences quote nothing from the file
s, c, why = run({'chapters': [{'file': 'SECRET-NAME.md', 'page': True}]})
assert 'SECRET' not in why

# a path-like file value is only ever compared by its base name, never opened
s, c, why = run({'chapters': [{'file': '../../etc/01-a.md', 'page': 8}]})
assert why is None and s == [3, 8, 14], (s, why)

# an oversize file
with tempfile.TemporaryDirectory() as d:
    f = Path(d) / 'big.json'
    f.write_text(' ' * 1_000_001)
    s, c, why = pc.chapters_json_starts(f, 50, CH, BY_TITLE)
    assert s is None and why
    s, c, why = pc.chapters_json_starts(Path(d) / 'missing.json', 50, CH, BY_TITLE)
    assert s is None and why

# the cap on entries, with pages that do increase (so only the cap can refuse it)
s, c, why = run({'chapters': [{'file': f'{i}.md', 'page': i + 1} for i in range(201)]}, n=500)
assert s is None and why and 'ignored' in why

# deeply nested JSON (post-review finding): ignored, not a crash
s, c, why = run(None, raw='[' * 100000)
assert s is None and why and 'ignored' in why, (s, why)

print('ok')
