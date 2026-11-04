# The guards of make_editions.py, as cases: what the review pages may and may not carry (security__005, 006, 007).
# Run: python3 -I review/tools/test_make_editions_guards.py   (prints "ok" and exits 0, or names the case that failed)
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import make_editions as m

GOOD_TAGS = ['<a href="{{root}}x.html">x</a>', "<a href='#a'>x</a>", '<a href=../y.html>', '<a href="https://github.com/SGit-AI/foo">x</a>',
             "<a href='" + m.SITE + "/a'>x</a>", '<p class="c-dim" data-a="r01-a">x &amp; y</p>', '<div style="background:url(img.png)">',
             '<a href={{root}}z.html class=b>t</a>', '<img src="a.png" alt="the // double slash in text">']
BAD_TAGS = ['<a href="//evil.example/p">', '<a href="HTTPS://evil.example/p">', '<a href="javascript:alert(1)">', '<img src="//h/x.png">',
            '<img src="data:image/png;base64,AA">', '<a href="mailto:a@b">', '<div style="background:url(//h/x)">',
            '<img srcset="a.png 1x, //h/b.png 2x">', '<a title="see https://evil.example/q">', '<a href="http://github.com/SGit-AI/x">',
            "<a href='//evil.example/p'>", '<a href=//evil.example/p>', '<a href=javascript:x>', "<img src='//evil/x'>", '<a href=HtTpS://evil.example/p>',
            "<a href = 'https://evil.example/p' >", '<a\nhref="//evil">', '<a href=&#x2F;&#x2F;evil.example/p>',
            '<a title=x href="jav&#x61;script:alert(1)">', '<a data-x=`//evil`>']
BAD_TAGS += ['<a href="java&amp;#9;script:alert(1)">', '<a href="java&Tab;script:alert(1)">', '<a href="jav&NewLine;ascript:x">', '<a href="java\tscript:x">',
             '<a href="javascript\n:x">', '<a href="\x01javascript:x">', '<a href="/&#9;/h">', '<a href="/\\h">', '<a href="\\\\h">', '<a href="\\/h">',
             '<a href="&bsol;&bsol;h">', '<meta http-equiv=refresh content="0;url=\\\\h">',
             '<style>@import "//h/x.css";</style>', '<style>@import "https://evil.com/x.css";</style>', '<div style="background:image-set(\'http://h/x\' 1x)">',
             '<div style="background:u\\72l(//h/x)">']
CLAIMS = {'C001': {'source': 'web https://example.org/a'}, 'C002': {'source': 'nothing'}}


def gate(raw):
    try:
        return m.text_address_gate(raw, CLAIMS, Path('t.md'))
    except SystemExit:
        return 'refused'


failed = []
for t in GOOD_TAGS:
    if m.page_attribute_problem(t) is not None:
        failed.append(f'a clean tag was refused: {t!r}')
for t in BAD_TAGS:
    if m.page_attribute_problem(t) is None:
        failed.append(f'a bad tag passed: {t!r}')
cases = [('an address under its own claim passes', '# T\n\n## C001: x\n\nread https://example.org/a now\n', 'pass'),
         ('also inside a backtick fence', '# T\n\n## C001: x\n\n```\n# read https://example.org/a\n```\n', 'pass'),
         ('also inside a tilde fence', '# T\n\n## C001: x\n\n~~~\n# C999: fake\n~~~\n\nhttps://example.org/a\n', 'pass'),
         ('under a claim whose entry does not list it', '# T\n\n## C002: y\n\nread https://example.org/a\n', 'refused'),
         ('in no claim section', '# T\n\nplain https://example.org/a\n', 'refused'),
         ('after another heading', '# T\n\n## C001: x\n\n## Another heading\n\nhttps://example.org/a\n', 'refused'),
         ('a different address under the right claim', '# T\n\n## C001: x\n\nhttps://example.org/b\n', 'refused'),
         ('a fake claim heading inside a fence', '# T\n\n~~~\n## C001: fake\n~~~\n\nhttps://example.org/a\n', 'refused'),
         ('a writers\' note is not read', '# T\n\n`%% record: https://example.org/zzz`\n', 'pass')]
for name, raw, want in cases:
    got = gate(raw)
    if (want == 'refused') != (got == 'refused'):
        failed.append(f'text_address_gate: {name}: wanted {want}, got {got!r}')
if failed:
    sys.exit('\n'.join(failed))
print('ok')
