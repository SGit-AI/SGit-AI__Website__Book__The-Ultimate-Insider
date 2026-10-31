# What Leanpub and KDP allow in a title, and how the six candidates read as listings

Kept by publisher@book.the-ultimate-insider, 31 October 2026, about 01:05 UTC, for the storyteller's study of the book's name (`chapter-plan/study-name-and-structure.md`, N1 to N6) at the conductor's letter 017 and the storyteller's letter 010. **The title is the editor's to sign**; nothing here chooses one, and `publishing/metadata.yaml` and the listing stay as they are until he does.

## The rules

| | Leanpub | Amazon KDP |
|---|---|---|
| Length | no limit found on its help pages | title and subtitle together "fewer than 200 characters" |
| Not allowed | nothing stated | repeated generic keywords; "unauthorized reference to other titles or authors"; sales rank ("bestselling"); promotions ("free") |
| Subtitle | every book should have one; longer subtitles help discoverability (its discoverability article) | counts in the 200 |
| Cover | not stated | title, subtitle and author on the cover "should match" the listing |
| URL (slug) | "short URLs that reflect the title"; "you can change your book's URL any time"; no character rule stated (examples are lowercase with hyphens) | none |
| Categories | several, from Leanpub's list, mostly programming topics | up to three, from Amazon's list |
| Keywords | none | up to seven keywords or short phrases; none that "mislead or manipulate" |

## The six candidates

Title and subtitle lengths include the ": " between them. Every slug below returned "not found" on leanpub.com on 31 October 2026 (a book at `/lean` returned a page, so the check works); not found is not a reservation, and the slug can change later anyway.

| | Title: subtitle | Characters | Leanpub slug, free | Fits KDP |
|---|---|---|---|---|
| N1 | Agentic Workflows, Shown Working: how a team of agents built a talk in a day, and how to build yours | 100 | `agentic-workflows-shown-working` | yes |
| N2 | The Agentic Team: a walkthrough of agentic workflows, from an empty repository to a talk on stage | 97 | `the-agentic-team` | yes |
| N3 | Agents That Work Together: protocols, provenance and memory for a team of agents, on one open project | 101 | `agents-that-work-together` | yes |
| N4 | Open Agentic Workflows: how a multidisciplinary team of agents stays aligned, built on one real day | 99 | `open-agentic-workflows` | yes |
| N5 | The Plumbing of Agentic Teams: the non-functional requirements that let a team of agents ship, walked through on a real project | 127 | `plumbing-of-agentic-teams` | yes, the longest |
| N6 | Brakes So We Can Go Faster: agentic workflows for a real team, walked through from its open record | 98 | `brakes-so-we-can-go-faster` | yes |

`agentic-workflows` itself is also free on Leanpub, a short slug any of the "agentic workflows" titles could use.

**What would make one fail:** none fails a rule. Three things to weigh:

- **KDP's cover rule.** The cover must carry the title and subtitle as listed, so a long subtitle (N5's 96 characters) has to be legible on the front at thumbnail size: the designer's question.
- **KDP's word rules.** None uses a forbidden word. Repeating "agentic" in title and subtitle (N2) is not the "repeated generic keywords" KDP means (that is about stuffing words like "notebook"), but the seven keywords should not repeat the title.
- **N6's hook.** "Brakes So We Can Go Faster" carries no category word, so on a store shelf the subtitle does all the finding; KDP's keywords and Leanpub's categories carry more weight for it than for N1 to N4.

## Categories

**Leanpub** (names as its store shows them; the author's list may hold more): Artificial Intelligence, Software Engineering, Software Architecture, DevOps, Cyber Security, Leadership, Management, Agile. For every candidate: Artificial Intelligence and Software Engineering first; Leadership or Management for N2 and N4 (the team and its alignment); Cyber Security for N6 (the controls), and as a third for the rest only if the editor wants the security reader found there.

**KDP**: up to three from Amazon's list, chosen in KDP at submission (the list is behind the editor's account; not read here). The same three directions: artificial intelligence, software engineering, management or security.

## Sources (read 31 October 2026)

- KDP, title and subtitle: kdp.amazon.com/en_US/help/topic/G201097560; keywords: /G201298500 (no dates shown)
- Leanpub, the book's URL: help.leanpub.com/en/articles/5986941 (3 March 2022); categories: /10070084 (31 October 2024); subtitles and discoverability: /2272344 (read from a search summary, not in full)
- Leanpub's store categories: leanpub.com/store/books, and /store/books/c/cyber_security
- The slugs: a plain fetch of leanpub.com/<slug> for each
