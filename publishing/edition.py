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
MARKERS = os.path.join(ROOT, "lab", "characters", "editions")  # the designer's on-stage markers, marker-<edition>-<page>.svg
FIGURES = [os.path.join(ROOT, "lab", "characters", "editions", "figure-{e}-{p:02d}.svg"),  # the designer's (074)
           os.path.join(ROOT, "lab", "experiments", "25-ruv-the-cast-strips", "edition", "strip-{e}-{p:02d}.svg")]  # ruv-sgit's (029)
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


def marker(edition, number):
    """The designer's on-stage marker for this page, as an image path from manuscript/ and its own label; or None."""
    path = os.path.join(MARKERS, f"marker-{edition}-{number:02d}.svg")
    if not os.path.exists(path):
        return None
    label = re.search(r'aria-label="([^"]*)"', open(path, encoding="utf-8").read(2000))
    return os.path.relpath(path, os.path.join(ROOT, "manuscript")), label.group(1) if label else "On stage now"


def drawing(edition, number):
    """The drawing for this page's "**Figure:**" line, as a path from manuscript/; or None (a figure to come)."""
    for pattern in FIGURES:
        path = pattern.format(e=edition, p=number)
        if os.path.exists(path):
            return os.path.relpath(path, os.path.join(ROOT, "manuscript"))
    return None


def page(title, body, mark=None, figure=None):
    """One page of the script as manuscript text."""
    m = re.match(r"(?:Page \d+|At the back)\.\s*(.*)", title)
    heading = re.sub(r"\s*\(the series page[^)]*\)\s*$", "", m.group(1) if m else title)
    return f"# {heading}\n\n" + cast_lines(body, mark, figure).strip() + "\n"


LAB_SVG = re.compile(r"\b(?:lab/[A-Za-z0-9_./-]+\.svg|index/talk-site/shots/[A-Za-z0-9_.-]+\.(?:jpg|png))\b")
SHOTS = "index/talk-site/shots/"
SHOT_OK = re.compile(r"(?:slide|talk|studio|articles|ruv-sgit|index|motion)[A-Za-z0-9_.-]*\.(?:jpg|png)$")  # security, 3 Nov 2026
SHOT_NEVER = re.compile(r"admin__|qr|key|vault", re.I)
UNSAFE_SVG = re.compile(r"<script|<foreignObject|\bon[a-z]+\s*=|@import|url\((?!\s*['\"]?#)"
                        r"|<(?:animate|animateMotion|animateTransform|set)\b|\\[0-9a-f]", re.I)  # SMIL, CSS escapes
HREF = re.compile(r"""\b(?:xlink:)?href\s*=\s*(["'])(.*?)\1""", re.I | re.S)
DATA_IMAGE = re.compile(r"data:image/(png|jpeg|webp);base64,([A-Za-z0-9+/=\s]+)")
SIGNATURES = {"png": (b"\x89PNG\r\n\x1a\n",), "jpeg": (b"\xff\xd8\xff",), "webp": (b"RIFF",)}
MAX_DRAWING = 8 * 1024 * 1024  # bytes: a drawing larger than this is refused


def unsafe_svg(text):
    """Why a lab/ drawing is refused, or None (security's conditions, 2 and 3 November 2026): no script, handler,
    foreignObject, @import or url() but an internal #id; an href only as a whole data:image/png, jpeg or webp in
    base64 whose decoded bytes carry that type's signature (security__010, 011); every other href refused."""
    import base64
    if UNSAFE_SVG.search(text):
        return "a script, handler, foreignObject, @import or outside url()"
    if re.search(r"\bhref\s*=\s*[^\"'\s]", text, re.I):
        return "an unquoted href"
    for m in HREF.finditer(text):
        d = DATA_IMAGE.fullmatch(m.group(2).strip())
        if not d:
            return "an href that is not an embedded png, jpeg or webp image"
        try:
            raw = base64.b64decode(re.sub(r"\s", "", d.group(2)), validate=True)
        except ValueError:
            return "an embedded image that is not clean base64"
        if not raw.startswith(SIGNATURES[d.group(1)]) or (d.group(1) == "webp" and raw[8:12] != b"WEBP"):
            return f"an embedded {d.group(1)} whose bytes are not a {d.group(1)}"
    return None


def lab_drawing(path):
    """A drawing named by its path from the repository root: only an .svg under lab/, no "..", that exists and holds
    no script, link or handler (security's conditions, 2 November 2026). The path from manuscript/, or an exit."""
    full = os.path.normpath(os.path.join(ROOT, path))
    if path.startswith(SHOTS):  # the librarian's screenshots of the talk's site: only the named kinds, never a key
        name = path[len(SHOTS):]
        if "/" in name or ".." in name or SHOT_NEVER.search(name) or not SHOT_OK.match(name):
            print(f"edition: not placed, a screenshot outside the cleared kinds (security, 3 November): {path}",
                  file=sys.stderr)
            return None
        if not os.path.isfile(full):
            sys.exit(f"edition: no such screenshot: {path}")
        return os.path.relpath(full, os.path.join(ROOT, "manuscript"))
    if ".." in path.split("/") or os.path.isabs(path) or not path.startswith("lab/") or not path.endswith(".svg") \
            or not full.startswith(os.path.join(ROOT, "lab") + os.sep):
        sys.exit(f"edition: refused a drawing outside lab/ or not an .svg: {path}")
    if not os.path.isfile(full):
        sys.exit(f"edition: no such drawing: {path}")
    if os.path.getsize(full) > MAX_DRAWING:
        sys.exit(f"edition: refused a drawing over {MAX_DRAWING // 1048576} MB: {path}")
    why = unsafe_svg(open(full, encoding="utf-8", errors="replace").read())
    if why:
        sys.exit(f"edition: refused a drawing with {why} in it: {path}")
    return os.path.relpath(full, os.path.join(ROOT, "manuscript"))


CLOCKS = "lab/experiments/60-ruv-the-margin-clock/edition/clock-{:02d}.svg"  # ruv-sgit's float box (designer__098)
HOURS = {w: i for i, w in enumerate("one two three four five six seven eight nine ten eleven twelve thirteen fourteen "
                                     "fifteen sixteen seventeen eighteen nineteen".split(), 1)}


def figure_count(body):
    return sum(1 for line in body.split("\n") if line.strip().startswith(("**Figure:**", "**Map:**")))


def cast_lines(body, mark=None, figure=None, figures=None):
    """The cast's conventions laid out, for a script page or a whole chapter (RC2's, build_book.py --cast): the cast
    bar, the band, the words box, each speaker's line with its head, a Figure line as a drawing or a figure to come,
    and the %% marker lines and "---" rules dropped. Any other line passes unchanged.

    figures: for a chapter, the drawings for its Figure lines in order (paths from the repository root, None where not
    drawn yet); a Figure line that names a lab/ .svg itself uses that. A speaker's block that follows the same
    speaker's, with only blank lines between, gets the class same-speaker (the editor, 2 November 2026: one head for a
    run of the same speaker)."""
    lines = []
    figures = list(figures) if figures is not None else None
    last = None  # the speaker of the block just written, while only blank lines follow it
    clock = None  # the hour of the last clock box in this chapter
    for line in body.split("\n"):
        s = line.strip()
        if not s:
            lines.append(line)
            continue
        if s == "---" or re.match(r"`?%%", s):  # rules and the developer's markers: dropped, and they do not end a run
            continue
        if s.startswith(">") and last:  # a passage quoted inside the narration keeps the speaker's run (conductor__059)
            lines.append(line)
            continue
        if s.startswith("**Clock:**"):  # the writer's clock line (writer__035, CK1: clock hours); keeps the run
            said = s[len("**Clock:**"):].strip()
            one = re.fullmatch(r"Hour ([a-z]+)\.?", said, re.I)
            hour = HOURS.get(one.group(1).lower()) if one else None
            if hour and hour == clock:
                continue  # the same hour again in this chapter: once where the hour changes (designer__098)
            if hour and os.path.isfile(os.path.join(ROOT, CLOCKS.format(hour))):
                src = lab_drawing(CLOCKS.format(hour))
                lines += ["", "::: {.clock-float}", f'<img class="clock-box" src="{src}" alt="{said}">', ":::", ""]
            else:  # a span of hours lights no one hour in the drawing: the words, as a margin note
                lines += ["", "::: {.clock}", said, ":::", ""]
            clock = hour or clock
            continue
        speaker, last = last, None
        if s.startswith("**Cast bar:**"):
            if mark:  # the marker drawing at the top, the cast-bar sentence under it as its caption (designer__071, 2)
                lines += ["", "::: {.cast-bar .with-marker}", f"![{mark[1]}]({mark[0]}){{.marker}}\\",
                          s[len("**Cast bar:**"):].strip(), ":::", ""]
            else:
                lines += ["", "::: {.cast-bar}", s, ":::", ""]
            continue
        if s.startswith("Band:"):
            lines += ["", "::: {.band}", s[len("Band:"):].strip(), ":::", ""]
            continue
        if s.startswith(("**Figure:**", "**Map:**")):  # a map is laid out as a figure (the writer's 025)
            kind = "Map" if s.startswith("**Map:**") else "Figure"
            what = re.sub(r"\s*\*\(Drawing:.*?\)\*\s*$", "", s[len(kind) + 5:]).strip()
            named = LAB_SVG.search(what)
            if named:
                drawn = lab_drawing(named.group(0))
            elif figures is not None:
                drawn = figures.pop(0) if figures else None
                drawn = lab_drawing(drawn) if drawn else None
            else:
                drawn = figure
            if named and figures:  # a named drawing still takes its place in the order
                figures.pop(0)
            if drawn:  # the drawing, its description from the script as the caption and the alt text
                caption = re.sub(r"[\[\]]", "", what)
                lines += ["", f"![{caption}]({drawn}){{.edition-figure}}", ""]
            else:
                lines += ["", "::: {.figure-todo}", f"{kind} to come: " + what, ":::", ""]
            continue
        m = SPEAKER.match(s)
        if m and m.group(1).lower() in SPEAKERS:
            who = m.group(1).lower()
            mood = f' data-mood="{m.group(2)}"' if m.group(2) else ""
            # the same speaker again, in the same mood: no second head (a mood change shows it again)
            same = " .same-speaker" if speaker and speaker[0] == who and (not m.group(2) or m.group(2) == speaker[1]) else ""
            lines += ["", f'::: {{.speaker{same} data-speaker="{who}"{mood}}}', s, ":::", ""]
            last = (who, m.group(2) or (speaker[1] if speaker and speaker[0] == who else None))
            continue
        if re.match(r"\*(Words (on|for) this page:\*|How to read the scenes:\*|An \*\*agent\*\*, here, is )", s):
            lines += ["", "::: {.words-box}", s, ":::", ""]
            continue
        lines.append(line)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines))


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
    source = "\n".join(x for x in source.split("\n") if not re.match(r"\s*`?%%", x))  # the record lines stay online
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
        text = page(title, body, marker(n, i), drawing(n, i))
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
