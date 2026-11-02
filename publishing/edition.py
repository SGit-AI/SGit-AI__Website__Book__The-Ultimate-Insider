#!/usr/bin/env python3
"""A short edition (ZM1) from the storyteller's script: the cast's pages as manuscript text, ready for build_book.py.

The storyteller writes each edition as a script in chapter-plan/cast/ (edition-03.md, edition-10.md): a header for
the editor and the team, then "## Page N. Title" sections, then notes for the writers and where it came from. This
turns one into chapters the build lays out, the words unchanged:

- each page a chapter (its own page in print), titled as the script titles it;
- the cast bar, the words box and the band set as styled blocks (publishing/lab-look.css);
- the developer's record and claim markers (lines starting %%, written in backticks) dropped: they belong to the
  online augmented mode, not the page;
- the series page moved to the back (SP1, the editor, 2 November 2026); an edition without one gets the series page
  of the 10-page script, the storyteller's words;
- the header and the notes for the writers left out; the script's own "Where this came from" kept, at the end, in one
  typeface (its code marks dropped, the words unchanged: synthetic__002);
- each speaker's line (a bold cast name, such as **Dev** or **Narrator.**) in a block of class speaker, with the
  speaker and the stage direction's first word as data-speaker and data-mood, for the designer's heads (designer__067);
- a "**Figure:**" line set as a figure to come (class figure-todo), the drawing's path note left out, until the
  drawing is placed;
- the script's "**Under the subtitle:**" promise written to the edition's own metadata.yaml, which build_book.py
  reads beside the Book.txt and prints on the title page.

    python3 publishing/edition.py 03       # chapter-plan/cast/edition-03.md -> manuscript/editions/03/
    python3 publishing/edition.py 10

Then: python3 publishing/build_book.py --book manuscript/editions/03/Book.txt --no-toc --name edition-03 --stamp "..."
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAST = os.path.join(ROOT, "chapter-plan", "cast")
SPEAKERS = {n.rsplit("-", 1)[0] for n in os.listdir(os.path.join(ROOT, "lab", "characters", "cast")) if n.endswith(".svg")}
SPEAKER = re.compile(r"\*\*([A-Za-z][A-Za-z-]*)\.?\*\*(?:\s*\*\(([a-z]+))?")


def sections(text):
    """The script's "## " sections, in order: (title, body)."""
    parts = re.split(r"(?m)^## ", text)
    out = []
    for part in parts[1:]:
        title, _, body = part.partition("\n")
        out.append((title.strip(), body.strip("\n")))
    return out


def page(title, body):
    """One page of the script as manuscript text."""
    m = re.match(r"(?:Page \d+|At the back)\.\s*(.*)", title)
    heading = re.sub(r"\s*\(the series page[^)]*\)\s*$", "", m.group(1) if m else title)
    lines = []
    for line in body.split("\n"):
        s = line.strip()
        if s == "---":
            continue
        if re.match(r"`?%%", s):  # the developer's markers, for the augmented mode
            continue
        if s.startswith("**Cast bar:**"):
            lines += ["", "::: {.cast-bar}", s, ":::", ""]
            continue
        if s.startswith("Band:"):
            lines += ["", "::: {.band}", s[len("Band:"):].strip(), ":::", ""]
            continue
        if s.startswith("**Figure:**"):
            what = re.sub(r"\s*\*\(Drawing:.*?\)\*\s*$", "", s[len("**Figure:**"):]).strip()
            lines += ["", "::: {.figure-todo}", "Figure to come: " + what, ":::", ""]
            continue
        m = SPEAKER.match(s)
        if m and m.group(1).lower() in SPEAKERS:
            mood = f' data-mood="{m.group(2)}"' if m.group(2) else ""
            lines += ["", f'::: {{.speaker data-speaker="{m.group(1).lower()}"{mood}}}', s, ":::", ""]
            continue
        if re.match(r"\*(Words (on|for) this page:\*|How to read the scenes:\*|An \*\*agent\*\*, here, is )", s):
            lines += ["", "::: {.words-box}", s, ":::", ""]
            continue
        lines.append(line)
    return f"# {heading}\n\n" + re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip() + "\n"


def series_page(script_sections):
    for title, body in script_sections:
        if re.match(r"(Page \d+|At the back)\..*(series|you doing it)", title, re.I):
            return title, body
    return None


def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        sys.exit(__doc__.strip().splitlines()[-3].strip())
    n = sys.argv[1].zfill(2)
    src = os.path.join(CAST, f"edition-{n}.md")
    script = sections(open(src, encoding="utf-8").read())
    pages = [(t, b) for t, b in script if t.startswith(("Page ", "At the back."))]
    source = next((b for t, b in script if t.lower().startswith("where this came from")), "")
    source = re.sub(r"`([^`]*)`", r"\1", re.sub(r"(?s)\n\*\*Read.*", "", source)).strip()
    header = open(src, encoding="utf-8").read().split("\n## ", 1)[0]
    promise = re.search(r"(?m)^\*\*Under the subtitle:\*\*\s*(.+)$", header)
    series = series_page(pages)
    if series:
        pages.remove(series)
    else:  # an edition with no series page of its own takes the 10-page script's (SP1)
        series = series_page(sections(open(os.path.join(CAST, "edition-10.md"), encoding="utf-8").read()))
    out = os.path.join(ROOT, "manuscript", "editions", n)
    os.makedirs(out, exist_ok=True)
    for f in os.listdir(out):
        if f.endswith(".md") or f == "Book.txt":
            os.unlink(os.path.join(out, f))
    names = []
    for i, (title, body) in enumerate(pages + ([series] if series else []), 1):
        name = f"{i:02d}.md"
        text = page(title, body)
        if i == len(pages) + (1 if series else 0) and source:
            text += "\n## Where this came from\n\n" + source + "\n"
        with open(os.path.join(out, name), "w", encoding="utf-8") as f:
            f.write(text)
        names.append(name)
    meta = os.path.join(out, "metadata.yaml")
    if promise:
        with open(meta, "w", encoding="utf-8") as f:
            f.write("# The edition's own title-page lines, from the script's header (publishing/edition.py)\n"
                    "abstract: |\n  " + promise.group(1).strip() + "\n")
    elif os.path.exists(meta):
        os.unlink(meta)
    with open(os.path.join(out, "Book.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(names) + "\n")
    print(f"edition: {len(names)} pages from {os.path.relpath(src, ROOT)} into {os.path.relpath(out, ROOT)}"
          f" (series page {'at the back' if series else 'none'})")


if __name__ == "__main__":
    main()
