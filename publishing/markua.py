#!/usr/bin/env python3
"""Markua to pandoc: the Markua-only syntax the book uses, translated so the team's own build reads it (decision M1).

Leanpub reads the chapters as Markua and makes the official PDF and EPUB; publishing/build_book.py runs every
chapter through translate() first, so the same source builds in pandoc too. Plain Markdown passes unchanged.

What it translates (Markua 0.30, markua.com):

- asides and blurbs, one line per paragraph line: `A>` aside, `B>` blurb, and the blurb classes `I>` information,
  `T>` tip, `W>` warning, `E>` error, `Q>` question, `D>` discussion, `X>` exercise, `C>` centred;
- the same as blocks: `{aside}` ... `{/aside}` and `{blurb, class: warning}` ... `{/blurb}`;
- an attribute line before an image, a heading or a paragraph: `{width: 60%, alt: "..."}` becomes pandoc's
  attributes on the image, or a div around the block;
- `{pagebreak}`; `{frontmatter}`, `{mainmatter}` and `{backmatter}` become a marker class on the next part.

Each aside or blurb becomes `::: {.callout .<kind>}`, styled by publishing/book.css. The kinds match the call-outs
the conductor's RC1 build placed (concept, number, takeaway, warning, try): `I>` and `A>` are concept, `T>` is
takeaway, `W>` and `E>` warning, `X>` try, `{blurb, class: number}` number.

    python3 publishing/markua.py FILE   # prints the translation, to check one chapter by eye
"""
import re
import sys

BLURB = {"A": "concept", "B": "concept", "I": "concept", "T": "takeaway", "W": "warning", "E": "warning",
         "X": "try", "Q": "concept", "D": "concept", "C": "centred"}
CLASS = {"information": "concept", "tip": "takeaway", "warning": "warning", "error": "warning", "exercise": "try",
         "question": "concept", "discussion": "concept", "center": "centred", "centered": "centred"}
LINE = re.compile(r"^([ABCDEIQTWX])>(?: (.*)|$)")
ATTRS = re.compile(r"^\{\s*([a-z][a-z-]*\s*:.*)\}\s*$", re.I)
BLOCK_OPEN = re.compile(r"^\{(aside|blurb)\s*(?:,\s*(.*))?\}\s*$", re.I)
BLOCK_CLOSE = re.compile(r"^\{/(aside|blurb)\}\s*$", re.I)
IMAGE = re.compile(r"^(!\[[^\]]*\]\([^)]*\))\s*$")


def attributes(text):
    """`width: 60%, alt: "a, b", class: wide` as (key, value) pairs; quoted values may hold commas."""
    return [(k.lower(), v if v is not None and v != "" else q) for k, q, v in
            re.findall(r'([a-z][a-z-]*)\s*:\s*(?:"([^"]*)"|([^,]*))\s*(?:,|$)', text, re.I)]


def kind_of(pairs, default="concept"):
    for k, v in pairs:
        if k == "class":
            v = v.strip().lower()
            return CLASS.get(v, re.sub(r"[^a-z-]", "", v) or default)
    return default


def pandoc_attrs(pairs):
    """Pandoc's {#id .class key=value}: id and class keep their own forms, the rest become key="value"."""
    out = []
    for k, v in pairs:
        v = v.strip()
        if k == "id":
            out.append("#" + v)
        elif k == "class":
            out += ["." + c for c in v.split()]
        else:
            out.append(f'{k}="{v}"')
    return "{" + " ".join(out) + "}"


def translate(text):
    lines = text.split("\n")
    out = []
    pending = None   # an attribute line waiting for the block it belongs to
    fence = False    # inside ``` code: nothing is translated
    blurb = None     # the kind of the one-line blurb being gathered
    block = None     # the kind of an open {aside} or {blurb} block
    for line in lines:
        if line.lstrip().startswith(("```", "~~~")):
            fence = not fence
        if fence or line.lstrip().startswith(("```", "~~~")):
            out.append(line)
            continue
        m = LINE.match(line)
        if m:
            kind = BLURB[m.group(1)]
            if blurb != kind:
                if blurb:
                    out.append(":::")
                out += ["", f"::: {{.callout .{kind}}}"]
                blurb = kind
            out.append(m.group(2) or "")
            continue
        if blurb:
            out += [":::", ""]
            blurb = None
        if BLOCK_OPEN.match(line):
            rest = BLOCK_OPEN.match(line).group(2)
            block = kind_of(attributes(rest or ""))
            out += ["", f"::: {{.callout .{block}}}"]
            continue
        if BLOCK_CLOSE.match(line) and block:
            out += [":::", ""]
            block = None
            continue
        low = line.strip().lower()
        if low == "{pagebreak}":
            out += ["", '<div class="pagebreak"></div>', ""]
            continue
        if low in ("{frontmatter}", "{mainmatter}", "{backmatter}"):
            out += ["", f'<div class="{low[1:-1]}"></div>', ""]
            continue
        a = ATTRS.match(line)
        if a and not line.startswith("{{"):
            pending = attributes(a.group(1))
            continue
        if pending is not None:
            if not line.strip():
                continue
            img = IMAGE.match(line)
            if img:
                out.append(img.group(1) + pandoc_attrs(pending))
                pending = None
                continue
            if line.startswith("#"):
                out.append(line + " " + pandoc_attrs(pending))
                pending = None
                continue
            out += ["::: " + pandoc_attrs(pending), line]   # close_divs ends it at the paragraph's end
            pending = None
            continue
        out.append(line)
    if blurb or block:
        out.append(":::")
    return close_divs("\n".join(out))


def close_divs(text):
    """A div opened by an attribute line around a paragraph closes at that paragraph's first blank line."""
    out, open_div = [], False
    for line in text.split("\n"):
        if line.startswith("::: {") and not line.startswith("::: {.callout"):
            open_div = True
            out.append(line)
            continue
        if open_div and not line.strip():
            out += [":::", ""]
            open_div = False
            continue
        out.append(line)
    if open_div:
        out.append(":::")
    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__.strip().splitlines()[-1].strip())
    with open(sys.argv[1], encoding="utf-8") as f:
        sys.stdout.write(translate(f.read()))
