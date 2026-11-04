"""The margin clock's boxes laid side by side (ruv), for the full book's chapter 8 (hours one to five) and chapter 9 (hours
six to fourteen), at the designer's 111.

Hours are the clock hours of 29 October (hour one is 00:00 to 00:59). Each box carries its hour's commits only, read at
build from C095's "all" row through clock.py's own reader. Wakes by trigger come from C087's by_hour_UTC, in its own words:
  chapter 8: hours three to five have an entry each (scheduled, then the editor's), shown under their boxes; hours one and
             two have none, and carry no wake mark; the caption says so.
  chapter 9: C087 gives one range for every hour from 05 to 13 UTC; it is shown once, as a band over the nine boxes, never
             as a count in a box.
No other number. Each box's bar is its commits against the day's busiest hour; the key says so, with no number. Text from
the register is escaped for XML. Pure vector: no image, href, script or handler; the drawing is checked with
publishing/edition.py's own unsafe_svg, and the tool refuses itself if it would be refused. Writes edition/strip-01-05.svg and edition/strip-06-14.svg only.
Usage: python3 -B -I tools/strip.py
"""
import importlib.util, json, sys
from html import escape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from clock import commits_by_hour, WORDS, INK, MUTED, FILL, FILL2, ACCENT, PAPER, SANS  # noqa: E402

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
PT = 9 * 25.4 / 72
SMALL = 7.5 * 25.4 / 72
_spec = importlib.util.spec_from_file_location('edition', ROOT / 'publishing' / 'edition.py')
_edition = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_edition)
unsafe_svg = _edition.unsafe_svg
W = 164.0


def t(x, y, s, size=PT, weight=400, fill=INK, anchor='start', style=''):
    st = f' font-style="{style}"' if style else ''
    return (f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{size:.3f}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}"{st}>{escape(str(s), quote=False)}</text>')


def claims():
    reg = json.loads((ROOT / 'claims' / 'register.json').read_text())
    c = {x['id']: x for x in (reg['claims'] if isinstance(reg, dict) else reg)}
    assert c['C087']['state'] == 'checked' and c['C022']['state'] == 'checked'
    return c['C087']['value']['by_hour_UTC'], c['C022']['value']['first_started'][:5]


def boxes(hours, vals, y0, bh, gap):
    """One box per hour across the width: the hour in words, its clock span, its commits, a bar against the day's peak."""
    n = len(hours)
    bw = (W - gap * (n - 1)) / n
    peak = max(vals)
    s = []
    for i, h in enumerate(hours):
        x = i * (bw + gap)
        s.append(f'<rect x="{x + .2:.2f}" y="{y0:.2f}" width="{bw - .4:.2f}" height="{bh:.2f}" rx="1.4" fill="{PAPER}" stroke="{FILL2}" stroke-width=".3"/>')
        s.append(t(x + 1.6, y0 + 4.6, 'HOUR', SMALL, 700, MUTED))
        s.append(t(x + 1.6, y0 + 9.4, WORDS[h - 1], PT, 800, ACCENT))
        s.append(t(x + 1.6, y0 + 13.2, f'{h - 1:02d}:00', SMALL, 400, MUTED))
        s.append(t(x + 1.6, y0 + 19.6, f'{vals[h - 1]}', 12 * 25.4 / 72, 800, INK))
        s.append(t(x + 1.6, y0 + 23.2, 'commits', SMALL, 400, MUTED))
        full = bw - 3.2
        s.append(f'<rect x="{x + 1.6:.2f}" y="{y0 + bh - 3.2:.2f}" width="{full:.2f}" height="1.4" fill="{FILL}"/>')
        s.append(f'<rect x="{x + 1.6:.2f}" y="{y0 + bh - 3.2:.2f}" width="{full * vals[h - 1] / peak:.2f}" height="1.4" fill="{ACCENT}"/>')
    return s, bw


def strip_01_05(vals, wk, first):
    hours = [1, 2, 3, 4, 5]
    y0, bh, gap = 8.0, 28.0, 2.0
    H = 58.0
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H:g}mm" viewBox="0 0 {W:g} {H:g}" role="img" '
         'aria-label="Hours one to five on the margin clock: each hour\'s commits, and under hours three to five the wakes by '
         'trigger, scheduled and the editor\'s; hours one and two have no wake records.">',
         t(0, 5.0, 'Hours one to five: commits each hour, and wakes where the register has them', PT, 700, INK)]
    b, bw = boxes(hours, vals, y0, bh, gap)
    s += b
    for i, h in enumerate(hours):
        x = i * (bw + gap)
        key = f'{h - 1:02d}'
        if key not in wk:
            s.append(t(x + 1.6, y0 + bh + 5.0, 'no wake records', SMALL, 400, MUTED, 'start', 'italic'))
            continue
        nums = [p.strip().split()[0] for p in wk[key].split(',')]
        assert len(nums) == 2 and all(n.isdigit() for n in nums), wk[key]
        s.append(t(x + 1.6, y0 + bh + 5.0, f'wakes: {nums[0]} scheduled,', SMALL, 400, INK))
        s.append(t(x + 1.6, y0 + bh + 8.4, f'{nums[1]} the editor\'s', SMALL, 400, INK))
    s.append(t(0, H - 5.6, f'Commits: the "all" row of the day\'s counts; the bar: this hour against the day\'s busiest hour. Wakes by trigger:', SMALL, 400, MUTED))
    s.append(t(0, H - 2.2, f'the register has no entry for hours one and two: wake records began at {first}, in hour three.', SMALL, 400, MUTED))
    return s, H


def strip_06_14(vals, wk, first):
    hours = list(range(6, 15))
    y0, bh, gap = 8.0, 28.0, 1.2
    H = 56.0
    band = wk['05 to 13']
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H:g}mm" viewBox="0 0 {W:g} {H:g}" role="img" '
         f'aria-label="Hours six to fourteen on the margin clock, side by side: each hour\'s commits; over all nine, one band '
         f'for the wakes in the register\'s words: {escape(band, quote=True)}.">',
         t(0, 5.0, 'Hours six to fourteen: commits each hour', PT, 700, INK)]
    b, bw = boxes(hours, vals, y0, bh, gap)
    s += b
    by = y0 + bh + 2.0
    s.append(f'<rect x="0" y="{by:.2f}" width="{W:g}" height="6.4" rx="1.4" fill="{FILL}" stroke="{ACCENT}" stroke-width=".35"/>')
    s.append(t(W / 2, by + 4.4, f'wakes in these nine hours, in the register\'s words: "{band}"', SMALL, 700, INK, 'middle'))
    s.append(t(0, H - 5.6, 'Commits: the "all" row of the day\'s counts; the bar: this hour against the day\'s busiest hour. Wakes: one range', SMALL, 400, MUTED))
    s.append(t(0, H - 2.2, 'for 05:00 to 13:59, not a count for each hour; every wake that started in those hours was scheduled.', SMALL, 400, MUTED))
    return s, H


def main():
    vals = commits_by_hour()
    wk, first = claims()
    for name, fn in (('strip-01-05.svg', strip_01_05), ('strip-06-14.svg', strip_06_14)):
        s, _ = fn(vals, wk, first)
        svg = '\n'.join(s + ['</svg>']) + '\n'
        why = unsafe_svg(svg)
        if why:
            sys.exit(f"refused by the build's rule: {why}")
        (HERE / 'edition' / name).write_text(svg)
        print(name, 'written')


if __name__ == '__main__':
    main()
