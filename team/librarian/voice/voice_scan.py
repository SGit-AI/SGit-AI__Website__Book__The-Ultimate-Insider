#!/usr/bin/env python3
"""The checkable parts of the editor's voice, as a scan (librarian@book.the-ultimate-insider).

The rules are the newsroom writer's, published at https://newsroom.sgit.ai/team/newsroom-writer.md and
in its handbook (how-a-journalist-agent-publishes-here.md, rule 6): first person, plain words, British
spelling, no em-dashes, no superlative or hype word unless the text shows the evidence, never the
ladder metaphor, never the model's name. The superlative patterns restate the list the newsroom's own
check uses (admin/build/wording.py in SGit-AI/SGit-AI__Website__Newsroom), read, not run. A hit is a
line to reread, not a verdict. Reads only; prints to stdout. Usage:

    python3 team/librarian/voice/voice_scan.py manuscript/*.md
"""
import re, sys

RULES = [
    (r"—", "em-dash"),
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


def main(files):
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
