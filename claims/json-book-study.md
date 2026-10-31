# A7: a book's content natively in JSON, with Markdown as a projection

researcher@book.the-ultimate-insider, 31 October 2026, for the editor's RC1 review (task A7, `team/conductor/rc1/editor-review/notes.json`; the conductor's letter `comms/mail/mailroom/researcher/conductor__021-rc1-review-5-to-9.eml`). A report for the editor's decision: nothing in the manuscript moves before it.

**The ask, in the conductor's reading of his words:** "the book's content natively in JSON (every chapter, section, infographic), with Markdown as a projection; a separation of content from formatting, many projections, everything hyperlinked".

## What I read

- **graphs.sgit.ai**, read on 31 October 2026 at about 06:55 UTC: its `llms.txt`, and `/v2/books/fsg/book.json`. This is the estate's three-book commission of August 2026, written by agents.
- **books.sgraph.ai: not read.** The container's proxy refused the connection (HTTP 502, "CONNECT tunnel failed") from this session, so I cannot say what it does. A session whose network allows the host, or the editor, should read it before the decision.

## What graphs.sgit.ai actually does: the opposite way round

- **Markdown is the source of truth, in every book.** Its own words: "The markdown under /v2/books/fsg/content/ is the source of truth"; for all three books, "Markdown is the source of truth in every case, the web edition renders it, and one print PDF carries each book offline."
- **JSON is the machine surface, generated from the Markdown.** `/v2/books/<slug>/book.json` holds the version, the chapter list (18 files for *Fractal Semantic Graphs*), word counts and the SHA-256 of every chapter's Markdown. It is an index and a seal, not the content.
- **The rich JSON is an extraction, not the source.** The Universe volume's `universe.json` holds nodes and edges, each "anchored to a verbatim quote at recorded byte offsets" in sources that are "byte-frozen" under `/v1/`. The graph points into the frozen text; it does not replace it.
- **Pages render their own file**, client-side, "so a page cannot describe a chapter it did not render": one source, many projections (web page, PDF, graph reader). That much matches the ask.
- **Versioning is per book**: a book's version moves only when its content moves, with v1.0.0 kept for the final release.

So the estate already separates content from its projections. The content it keeps is Markdown, with JSON for structure, hashes and extracted graphs.

## What this book does now

- Chapters are Markdown in `manuscript/` (RC1 drafts in `team/conductor/rc1/`).
- The plan and decisions are JSON (`book.json`), and the numbers are JSON (`claims/register.json`), each cited by id from the prose.
- So it is already the graphs.sgit.ai shape: prose as Markdown, structure and data as JSON.

## The options, for the decision

1. **Keep the estate's way: Markdown source, JSON surfaces.** Add a `book.json`-style manifest (chapters, sections, figures, claim ids, hashes) built from the Markdown at every release. Cheapest. Proven on three books. Every tool already reads it.
2. **JSON source, Markdown projection (the ask as worded).** Every chapter, section, paragraph and infographic as JSON objects with ids, and Markdown, HTML and PDF generated from them. It gives stable ids for every paragraph (links, comments, the reviewer experience), but every writer and tool on the team works in Markdown today, and a converter both ways would be needed. Nothing in the estate does this yet that I could read.
3. **Both, by id.** Markdown stays the source, and the build gives every heading, paragraph and figure a stable id and emits a JSON graph of them with byte offsets, as `universe.json` does for its sources. It gets most of what the ask wants (hyperlinks, many projections, machine-readable sections) without changing how anyone writes.

My reading, for the editor to overrule: option 3 is what the estate's own practice points to. What would settle it is reading books.sgraph.ai, which I could not do from here.

## Where this came from

https://graphs.sgit.ai/llms.txt and https://graphs.sgit.ai/v2/books/fsg/book.json, read 31 October 2026; this repository's `book.json`, `claims/register.json`, `manuscript/`; `team/conductor/rc1/editor-review/notes.json` (A7). No number from here is in the register: none is meant for the book.
