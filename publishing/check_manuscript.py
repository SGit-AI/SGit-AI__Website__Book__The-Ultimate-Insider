#!/usr/bin/env python3
"""What in manuscript/ would break the print, the EPUB or Markua, or the house rules a machine can check: file and line.

Read only. The publisher's lane of the RC1 review (board 003): it finds, it does not fix; the text is the writer's and
the conductor's. Checks, each named in the report:

- em-dash: the house rule, no em-dashes in prose
- spelling: American spellings with a common British form (a short list; a hit is a question, not a verdict)
- html: raw HTML tags, which Markua does not promise to pass through
- comment: an HTML comment; both pandoc and Markua drop it (markua.com, section 1.4: raw HTML is removed), so it is
  harmless, but a "figure:" comment is a figure still to be drawn
- heading: a chapter must open with one level-1 heading, and have no other
- link: a link to a local file or an anchor, which is dead on paper
- alt: an image whose only text is its caption (Markua uses the bracket text as both: rc1-cards.md, card 14)
- long-code: a code line over 80 characters, which wraps in the PDF and the EPUB

    python3 publishing/check_manuscript.py [--only CHECK]
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANUSCRIPT = os.path.join(ROOT, "manuscript")
SPELLINGS = {  # American: British
    "color": "colour", "behavior": "behaviour", "organize": "organise", "organization": "organisation",
    "recognize": "recognise", "analyze": "analyse", "center": "centre", "favorite": "favourite", "honor": "honour",
    "labor": "labour", "license": "licence (noun)", "defense": "defence", "catalog": "catalogue", "realize": "realise",
    "prioritize": "prioritise", "summarize": "summarise", "emphasize": "emphasise", "minimize": "minimise",
    "authorize": "authorise", "authorization": "authorisation", "fulfill": "fulfil", "traveled": "travelled",
    "modeled": "modelled", "canceled": "cancelled", "gray": "grey",
}
SPELL = re.compile(r"\b(" + "|".join(SPELLINGS) + r")(s|d|ed|ing)?\b", re.I)


def chapters():
    with open(os.path.join(MANUSCRIPT, "Book.txt"), encoding="utf-8") as f:
        return [n.strip() for n in f if n.strip() and not n.startswith("#")]


def check(name):
    found, fence, h1 = [], False, 0
    path = os.path.join(MANUSCRIPT, name)
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        line = line.rstrip("\n")
        if line.lstrip().startswith(("```", "~~~")):
            fence = not fence
            continue
        if fence:
            if len(line) > 80:
                found.append((n, "long-code", f"{len(line)} characters"))
            continue
        prose = re.sub(r"`[^`]*`", "", line)  # code spans are names and commands, not prose
        if "\u2014" in prose:
            found.append((n, "em-dash", prose.strip()[:70]))
        for m in SPELL.finditer(re.sub(r"\]\([^)]*\)|https?://\S+", "", prose)):
            word = m.group(1).lower()
            found.append((n, "spelling", f"{m.group(0)} (British: {SPELLINGS[word]})"))
        if "<!--" in prose:
            found.append((n, "comment", prose.strip()[:70]))
        if re.search(r"</?(div|span|br|p|img|a|table|sup|sub|details|summary|iframe)\b", prose, re.I):
            found.append((n, "html", prose.strip()[:70]))
        if re.match(r"#\s", line):
            h1 += 1
            if n > 1 and h1 > 1:
                found.append((n, "heading", "a second level-1 heading"))
        elif n == 1:
            found.append((n, "heading", "the chapter does not open with a level-1 heading"))
        for m in re.finditer(r"(?<!!)\[[^\]]+\]\(([^)\s]+)", prose):
            target = m.group(1)
            if not re.match(r"https?://|mailto:", target):
                found.append((n, "link", f"{target} (dead on paper)"))
        m = re.match(r"\s*!\[([^\]]*)\]\(([^)\s]+)(\s+\"[^\"]*\")?\)", line)
        if m and not m.group(3):
            found.append((n, "alt", f"{os.path.basename(m.group(2))}: caption and alt text are the same"))
    return found


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--only", help="report one check: em-dash, spelling, html, comment, heading, link, alt, long-code")
    a = p.parse_args()
    totals = {}
    for name in chapters():
        for n, kind, what in check(name):
            totals[kind] = totals.get(kind, 0) + 1
            if not a.only or a.only == kind:
                print(f"{name}:{n}: {kind}: {what}")
    print("check_manuscript: " + (", ".join(f"{k} {v}" for k, v in sorted(totals.items())) or "nothing found"),
          file=sys.stderr)


if __name__ == "__main__":
    main()
