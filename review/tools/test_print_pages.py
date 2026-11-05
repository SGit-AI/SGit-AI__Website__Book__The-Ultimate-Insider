# The paragraph-to-page matcher of print_pages.py, as cases. Run: python3 -I review/tools/test_print_pages.py   (prints ok, or names the failing case)
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import print_pages as pp

pages = ['aaa bbb ccc ddd eee fff', 'one two three four five six', 'x y z w v u t', 'rep rep rep rep rep rep', 'tail one two three four five']


def run(texts):
    ch = [{'title': 'T', 'scenes': [{'paragraphs': [{'id': str(i), 'text': t} for i, t in enumerate(texts)]}]}]
    return pp.map_paragraphs(ch, pages)


failed = []
where, found, carried, _ = run(['rep rep rep rep rep rep', 'one two three four five six', 'x y z w v u'])   # a repeated phrase far ahead must not strand what follows
if where != {'0': 4, '1': 2, '2': 3} or carried:
    failed.append(f'back look: got {where}, carried {carried}')
where, found, carried, _ = run(['aaa bbb ccc ddd eee fff', 'one two three four five six', 'x y z w v u'])           # the plain case
if where != {'0': 1, '1': 2, '2': 3} or carried:
    failed.append(f'plain: got {where}, carried {carried}')
where, found, carried, _ = run(['aaa bbb ccc ddd eee fff', 'nothing like any page at all here'])                    # a paragraph in no page takes the page before and is carried
if where['1'] != 1 or carried != 1:
    failed.append(f'not found: got {where}, carried {carried}')
if failed:
    sys.exit('\n'.join(failed))
print('ok')
