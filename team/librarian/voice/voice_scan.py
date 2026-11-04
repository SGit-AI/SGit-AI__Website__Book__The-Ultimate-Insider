#!/usr/bin/env python3
"""The checkable parts of the editor's voice, as a scan (librarian@book.the-ultimate-insider).

The rules are the newsroom writer's, published at https://newsroom.sgit.ai/team/newsroom-writer.md and
in its handbook (how-a-journalist-agent-publishes-here.md, rule 6): first person, plain words, British
spelling, no em-dashes, no superlative or hype word unless the text shows the evidence, never the
ladder metaphor, never the model's name; and, since 2 November 2026, no religious words (RW1, CLAUDE.md). The superlative patterns restate the list the newsroom's own
check uses (admin/build/wording.py in SGit-AI/SGit-AI__Website__Newsroom), read, not run. A hit is a
line to reread, not a verdict. Reads only; prints to stdout. Usage:

    python3 team/librarian/voice/voice_scan.py manuscript/*.md
    python3 team/librarian/voice/voice_scan.py --logistics manuscript/rc2/150/*.md

--logistics (the editor's guidance of 4 November 2026, brief 07: "speak as me, in the present, without the
logistics") counts, in each chapter's reading text only (not in `%%` notes, bands, lists, tables or the
"Where this came from" section), the things he said belong in the tracing: "added after the day", the
recording's clock ("on the recording"), "transcript", and a commit id. The counts are lines to reread.
"""
import re, sys

# RW1 (the editor, 2 November 2026; CLAUDE.md): no religious words. The list is CLAUDE.md's, stored reversed so this
# file does not use the words itself; each also matches a plural or a longer form of the word.
RW1 = [w[::-1] for w in ("elbib", "lepsog", "erutpircs", "nomres", "hcaerp", "tsilegnave", "tnemdnammoc", "dercas", "yloh", "egamirglip", "pihsrow")]
RULES = [
    (r"\b(" + "|".join(RW1) + r")\w*", 'a religious word (RW1: "the cast guide", not the old name)'),
    (chr(0x2014), "em-dash"),
    (r"\b(the )?(clearest|best|finest|strongest|most (complete|important|striking|powerful|elegant|honest))\b[^.;:\n]{0,60}\bI (have|'ve) (ever )?(seen|read|found|met|come across)", 'superlative + "I have seen"'),
    (r"\bI (can|could) think of\b", '"I can think of"'),
    (r"(?<!some of )\bthe (clearest|best|finest|strongest)\b[^.;:\n]{0,40}\b(ever|anyone will|anywhere|in the world|of all time)\b", 'superlative + "ever"'),
    (r"(?<!in )\bthe (clearest|best) (example|case|case study|statement|account|evidence|illustration|explanation|demonstration)\b", "superlative example"),
    (r"\bone of the (clearest|best|finest|strongest)\b", '"one of the clearest/best"'),
    (r"\b(is|are) the clearest\b", '"is the clearest"'),
    (r"\b(groundbreaking|game[- ]chang\w*|revolutionary|unprecedented|mind[- ]blowing|incredible|stunning|jaw[- ]dropping)\b", "hype word"),
    (r"(?<!not )(?<!not a )\b(perfect|perfectly)\b(?! the)", '"perfect" (the editor says "great")'),
    (r"\bladder\b", "the ladder metaphor"),
    (r"\b(Claude|Opus|Sonnet|Haiku|Fable|GPT-?\d|ChatGPT)\b", "a model's name"),
    (r"\b(color|colors|behavior|behaviors|organize\w*|organization\w*|recognize\w*|analyze\w*|center|centers|license[sd]?|defense|favorite|labeled|labeling|modeling|traveled|catalog)\b", "American spelling"),
]
RULES = [(re.compile(p, re.I if why != "a model's name" else 0), why) for p, why in RULES]
THIRD = re.compile(r"\b(the editor|Dinis Cruz|Dinis)\b")
SKIP = re.compile(r"^\s*(-|\|)|`[^`]*`")   # source lists and tables are records, not prose; code spans are names


LOGISTICS = [
    (re.compile(r"added (to the record |to the site |to the talk's repository )?after the day|after the day\)", re.I), "added after the day"),
    (re.compile(r"on the recording|recording's (own )?clock", re.I), "recording clock"),
    (re.compile(r"\btranscript\b", re.I), "transcript"),
    (re.compile(r"`[0-9a-f]{7,8}`|\b[0-9a-f]{7,8}\b(?= \()"), "a commit id"),
]


def logistics(files):
    total = 0
    for f in files:
        lines = open(f, encoding="utf-8").read().splitlines()
        end = next((i for i, l in enumerate(lines) if l.strip().lower().startswith("## where this came from")), len(lines))
        counts = {why: [] for _, why in LOGISTICS}
        for n, line in enumerate(lines[:end], 1):
            st = line.lstrip()
            if st.startswith(("`%%", "Band:", "-", "|", ">", "*Words", "**Figure", "**Map", "**Cast bar", "**Clock", "#")):
                continue
            for rx, why in LOGISTICS:
                if rx.search(line):
                    counts[why].append(n)
        parts = [f"{why} {len(v)} (line {v[0]})" for why, v in counts.items() if v]
        total += sum(len(v) for v in counts.values())
        print(f"{f}: " + ("; ".join(parts) if parts else "none"))
    print(f"voice_scan --logistics: {total} line(s) in {len(files)} file(s)")


def main(files):
    if files[:1] == ["--logistics"]:
        return logistics(files[1:])
    total = 0
    for f in files:
        lines = open(f, encoding="utf-8").read().splitlines()
        end = next((i for i, l in enumerate(lines) if l.strip().lower().startswith("## where this came from")), len(lines))
        third = 0
        for n, line in enumerate(lines[:end], 1):
            prose = SKIP.sub("", line) if not line.lstrip().startswith(("-", "|")) else ""
            third += len(THIRD.findall(prose))
            for rx, why in RULES:
                m = rx.search(prose if why != "em-dash" else line)
                if m:
                    s = max(0, m.start() - 40)
                    ctx = (prose if why != "em-dash" else line)[s:m.end() + 40].strip()
                    print(f"{f}:{n}: {why}: ...{ctx}...")
                    total += 1
        print(f"{f}: the editor in the third person {third} time(s) in its prose")
    print(f"voice_scan: {total} hit(s) in {len(files)} file(s)")


if __name__ == "__main__":
    main(sys.argv[1:])
