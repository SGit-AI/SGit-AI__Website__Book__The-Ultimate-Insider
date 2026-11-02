# One head per speaker, not per paragraph

The editor, Dinis Cruz, in the conductor's session (conductor@book.the-ultimate-insider), 2 November 2026, about 20:25 UTC, reading the RC2 draft on a tablet. He attached one image: page 4 of the RC2 PDF ("The creator's problem", "The old way"), three "Narrator." paragraphs in a row, each with the same head beside it. Kept here as he gave it. Never edited; where it turns out to be wrong, the finding goes in `BRIEF-CORRECTIONS.md`.

> Which is the agent writing the chapters?
>
> On pages like pic1 we shouldn't keep putting the agent card every paragraph (when it is the same)

## How the conductor reads it (not his words)

- **The question:** the writer (writer@book.the-ultimate-insider) writes RC2's chapters; the heads beside each line are the publisher's build (`publishing/edition.py` cast_lines) and the designer's stylesheet (`lab/tools/book/speakers.css`).
- **The instruction:** when the same speaker goes on for several paragraphs, the head (and the repeated name) appears once, on the first; it appears again only when the speaker changes. The publisher marks the repeat in the build, the designer's stylesheet hides it, in RC2 and in the editions alike.
