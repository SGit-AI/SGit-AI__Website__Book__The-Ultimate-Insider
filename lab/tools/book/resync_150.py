#!/usr/bin/env python3
"""Bring the designer's list of the full book's figure slots (lab/tools/book/rc2-150-figures.json) into line with the
chapters' Figure and Map lines as they stand (publisher 045, ruv-sgit 067, conductor 075).

    python3 lab/tools/book/resync_150.py [--write]

For every chapter in manuscript/editions/rc2-150/Book.txt (read only), each Figure or Map line in order becomes a slot. A
slot keeps the drawing and note of the old slot whose line opened with the same words (the first 40 characters after
the label), as the publisher's own map matches them; a line with no match is "to draw". PLACED sets a drawing by hand
where a line is new and the designer has chosen. Without --write it only reports what would change.
"""
import difflib, json, re, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
LIST = REPO / "lab" / "tools" / "book" / "rc2-150-figures.json"
BOOK = REPO / "manuscript" / "editions" / "rc2-150" / "Book.txt"
LABEL = re.compile(r"^\*\*(Figure|Map):\*\*\s*(.*)$")
# chapter: {opening words of the line: (drawing, note)}, the designer's choices for new lines
PLACED = {
    "rc2/150/02-inventing-on-principle.md": {
        "my last afternoon ask drawn to the clock": ("lab/experiments/29-ruv-the-afternoon-loop/edition/round-trip-clock.svg",
                                                     "ruv-sgit's round-trip clock (its 066), as the line's brief names it"),
        "the factory in action": ("lab/experiments/64-ruv-one-wake-on-the-clock/edition/factory-clock.svg",
                                  "ruv-sgit's factory clock, the designer's choice (127), the storyteller's yes (124)"),
    },
    "rc2/150/11-the-plumbing.md": {
        "the repository at the end of each hour": ("lab/experiments/60-ruv-the-margin-clock/edition/repo-growth.svg",
                                                   "ruv-sgit's repository by the hour (its 066), as the line names it"),
    },
}


def key(text):
    return re.sub(r"\s+", " ", text.strip())[:40].lower()


def key80(text):
    return re.sub(r"\s+", " ", text.strip())[:80].lower()


def lines(path):
    return [(i + 1, m.group(2)) for i, l in enumerate(path.read_text().splitlines()) if (m := LABEL.match(l))]


def main(write):
    d = json.loads(LIST.read_text())
    chapters = [l.strip() for l in BOOK.read_text().splitlines() if l.strip() and not l.startswith("#")]
    report, new_slots, new_notes = [], {}, {}
    for rel in chapters:
        path = (BOOK.parent / rel).resolve()
        k = "rc2/150/" + path.name
        old_s, old_n = d["slots"].get(k, []), d["notes"].get(k, [])
        old = {}
        for s, n in zip(old_s, old_n):
            text = n.split("| ", 1)[1] if "| " in n else n
            m = LABEL.match(text)
            old[key80(m.group(2) if m else text)] = (s, n.split(" | ", 1)[0].split(". ", 1)[-1])
        slots, notes, used = [], [], set()
        for j, (ln, text) in enumerate(lines(path)):
            hand = next((v for w, v in PLACED.get(k, {}).items() if text.lower().startswith(w)), None)
            if hand:
                drawing, status = hand
            else:
                best = max(((difflib.SequenceMatcher(None, key80(text), w).ratio(), w) for w in old if w not in used), default=(0, None))
                if best[0] >= .6:
                    used.add(best[1])
                    drawing, status = old[best[1]]
                    if best[0] < .95:
                        report.append(f"  {k} line {ln}: matched at {best[0]:.2f} to '{best[1][:50]}'")
                else:
                    drawing, status = None, "to draw"
            slots.append(drawing)
            notes.append(f"{j + 1}. {status} | **Figure:** {text[:60]}")
        if slots != old_s or len(notes) != len(old_n):
            report.append(f"{k}: {len(old_s)} slots -> {len(slots)}; " +
                          "; ".join(f"{i + 1} {Path(s).name if s else '-'}" for i, s in enumerate(slots)))
        new_slots[k], new_notes[k] = slots, notes
    print("\n".join(report) or "no change")
    drawn = sum(1 for v in new_slots.values() for s in v if s)
    todo = sum(1 for v in new_notes.values() for n in v if "to draw |" in n)
    print(f"{sum(len(v) for v in new_slots.values())} lines, {drawn} with a drawing, {todo} to draw")
    if write:
        d["slots"], d["notes"] = new_slots, new_notes
        LIST.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main("--write" in sys.argv)
