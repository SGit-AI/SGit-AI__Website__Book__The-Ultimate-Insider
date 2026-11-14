#!/usr/bin/env python3
"""Bring the designer's list of the full book's figure slots (lab/tools/book/rc2-150-figures.json) into line with the
chapters' Figure and Map lines as they stand (publisher 045, ruv-sgit 067, conductor 075).

    python3 lab/tools/book/resync_150.py [--write]

For every chapter in manuscript/editions/rc2-150/Book.txt (read only), each Figure or Map line in order becomes a slot. A
slot keeps the drawing and note of the closest old slot (difflib on the line's first 80 characters, 0.6 or more, each
old slot used once); a line with no match is "to draw". PLACED sets a drawing by hand
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
    "rc2/150/00-start-here.md": {
        # OS1 (the opening spread, writer 277): the role cards move here from 00b and the house joins them; the four
        # screenshots are the publisher's, held until security clears them by name
        "the whole team on one page": ("lab/experiments/27-designer-the-cast/cast-row-personas.svg",
                                       "LAB 27's role cards, moved here from 00b (OS1, writer 277)"),
        "the talk's repository as a house": ("lab/experiments/47-designer-the-house/the-house.svg", "the designer's house (LAB 47), OS1"),
    },
    "rc2/150/00b-who-is-telling-this-story.md": {
        "the whole team on one page": ("lab/experiments/27-designer-the-cast/cast-row-personas.svg",
                                       "LAB 27's role cards, moved here from 06 (storyteller 149, writer 228)"),
        "two voices on the page": ("lab/experiments/54-designer-first-pages/two-voices.svg", "the designer's two voices (LAB 54)"),
        "the two voices: the narrator": ("lab/experiments/54-designer-first-pages/two-voices.svg",
                                         "the designer's two voices (LAB 54), under the line as reworded for PEN1 note 22"),
        "the experiments that led to the day": ("lab/experiments/80-designer-experiments-timeline/timeline.svg",
                                                "the designer's experiments timeline (LAB 80), PEN1 note 24, researcher 045's chain"),
    },
    "rc2/150/03b-the-day-at-a-glance.md": {
        "the talk's day as one picture": ("lab/experiments/57-designer-day-at-a-glance/day-at-a-glance.svg", "the designer's day (LAB 57), C095"),
        "the same day by member": ("lab/experiments/57-designer-day-at-a-glance/day-by-member.svg", "the designer's day by member (LAB 57), C095"),
    },
    "rc2/150/10-talking-through-git.md": {
        "the three notes as three cards on a line of time": ("lab/experiments/58-designer-three-notes/three-notes.svg", "the designer's three notes (LAB 58)"),
    },
    "rc2/150/13-the-story-before-the-slides.md": {
        "one of the storyteller's maps as it went into the talk": ("lab/experiments/59-designer-chapter-13/storyteller-map.svg", "the designer's map 1 (LAB 59)"),
        "the objection's path in one line of time": ("lab/experiments/59-designer-chapter-13/objection-path.svg", "the designer's objection's path (LAB 59)"),
    },
    "rc2/150/14-port-not-rebuild.md": {
        "a card, the three decisions on one line of time": ("lab/experiments/67-designer-chapter-14/three-decisions.svg", "the designer's card (LAB 67), C104"),
        "the plan of three parts, drawn as three gates": ("lab/experiments/67-designer-chapter-14/three-gates.svg", "the designer's gates (LAB 67), C027"),
    },
    "rc2/150/23-principles-and-build-your-own.md": {
        "the five steps as a path": ("lab/experiments/40-designer-rc2-chapter-5/ch23-five-steps.svg",
                                     "the designer's five steps with this book's Something to try cards (ruv-sgit 091)"),
    },
    "rc2/150/04-hour-one-the-empty-project.md": {
        "one banner, as a session prints it": ("lab/experiments/55-designer-findings-cards/ch4-banner-pair.svg",
                                               "the writer's own banners (its debrief of 4 November), drawn (LAB 55)"),
        "the brief and the reality file as they stood": ("lab/experiments/70-designer-brief-and-reality/brief-and-reality.svg", "the designer's weight (LAB 70), C125"),
        "the sgit.ai sites the talk's repository names": ("lab/experiments/74-designer-sgit-sites/sgit-sites.svg", "the designer's sites (LAB 74), C126"),
        "one member's folder, opened": ("lab/experiments/54-designer-first-pages/member-folder.svg", "the designer's folder (LAB 54)"),
    },
    "rc2/150/06-roles-as-a-cast-you-can-read.md": {
        "a card, each member's wake records": ("lab/experiments/54-designer-first-pages/wake-records.svg", "the designer's card (LAB 54), C022"),
    },
    "rc2/150/02-inventing-on-principle.md": {
        "my last ask for the player drawn to the clock": ("lab/experiments/29-ruv-the-afternoon-loop/edition/round-trip-clock.svg",
                                                     "ruv-sgit's round-trip clock (its 066), as the line's brief names it"),
        "\"a slide versus a loop\" (right half)": ("lab/experiments/37-designer-rc2-chapters-1-2/ch2-loop-wordless.svg",
                                                  "the loop wordless here, its names in chapter 12 (the storyteller's 130, writer2 022)"),
        "the factory in action": ("lab/experiments/64-ruv-one-wake-on-the-clock/edition/factory-clock.svg",
                                  "ruv-sgit's factory clock, the designer's choice (127), the storyteller's yes (124)"),
    },
    "rc2/150/03-the-tour.md": {
        "the same kind of key as a qr code": ("lab/experiments/50-designer-three-keys/three-keys.svg",
                                              "the designer's three QR codes (LAB 50, publisher 048), cleared by name (security__024)"),
        "the team's house": ("lab/experiments/47-designer-the-house/the-house.svg", "the designer's house (LAB 47, conductor 067)"),
    },
    "rc2/150/12-the-creator-comes-back.md": {
        "the player, first": ("index/talk-site/shots/talk__player.jpg",
                              "the librarian's screenshot, cleared (security 024), cited in the chapter's record line"),
        "the loop from chapter 2": ("lab/experiments/37-designer-rc2-chapters-1-2/ch1-loop.svg",
                                    "the named cycle, think, explain, create, review (writer2 022)"),
    },
    "rc2/150/16-hour-nineteen-minute-by-minute.md": {
        "the hold file as a page": ("lab/experiments/42-designer-rc2-seventy/ch10-hold-file.svg", "the designer's hold file"),
        "the last ten minutes as a line": ("lab/experiments/73-designer-chapter-16/three-sessions.svg",
                                           "the designer's three sessions past the hold (LAB 73; replaces LAB 39's dots, ruv-sgit 081)"),
        "the team's tally": ("lab/experiments/53-designer-team-tally/team-tally.svg", "the designer's tally (LAB 53), from C119"),
        "the dashboard after the stop": ("lab/experiments/42-designer-rc2-seventy/ch2-dashboard.svg", "the designer's dashboard"),
    },
    "rc2/150/17-what-did-not-work.md": {
        "the misses as cards on one page": ("lab/experiments/43-designer-rc2-full-book/ch17-nine-misses.svg",
                                             "the designer's nine misses, read from chapter 17 at build (critic3 007)"),
    },
    "rc2/150/94-the-making-of-this-book.md": {
        "this book's team arriving": ("lab/experiments/51-designer-book-team-arriving/book-team-arriving.svg",
                                      "the designer's twelve arriving (LAB 51), from C131"),
    },
    "rc2/150/05-hour-two-the-rules-written.md": {
        "the publishing flow": ("lab/experiments/56-designer-rule-and-flow/publishing-flow.svg", "the callout's picture (LAB 56), 56 mm"),
    },
    "rc2/150/07-hour-three-the-five-steps.md": {
        "one rule's journey in an hour": ("lab/experiments/56-designer-rule-and-flow/rule-journey.svg", "the designer's line of the hour (LAB 56)"),
    },
    "rc2/150/08-hours-four-and-five-before-dawn.md": {
        "a card, the researcher's two findings": ("lab/experiments/55-designer-findings-cards/ch8-two-findings.svg", "LAB 55, C025 under the rail"),
    },
    "rc2/150/09-nine-hours-with-nobody-starting-work.md": {
        "one picture's three rounds side by side": ("lab/experiments/63-ruv-three-rounds/edition/three-rounds.svg",
                                                    "ruv-sgit's three rounds (its 074), as the seventy places it"),
        "a card, the researcher's three findings": ("lab/experiments/55-designer-findings-cards/ch9-three-findings.svg", "LAB 55, C025 under the rail"),
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
        gone = [x for x in old_s if x and x not in slots]
        if gone:  # a drawing that was placed and is placed no longer: say so, so a reworded line never drops one silently
            report.append(f"  DROPPED from {k}: " + ", ".join(Path(x).name for x in gone))
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
