# The reviewer experience: feedback that impresses, on our own technology

Started by the editor (Dinis Cruz) in the conductor's session on 30 October 2026, about 13:30 UTC. Kept by conductor@book.the-ultimate-insider. It widens the review programme (`../review-programme/README.md`) from "send a PDF and ask questions" to a product. Nothing here is built yet; no real person is contacted, and no vault is made, until the editor signs R1 and R2 in `book.json`.

## Why

RC1 is locked as the version people review. The editor will read it and form opinions; he wants them calibrated by readers ("I kind of want to be calibrated by the community"): which parts, paragraphs and sections make sense, and how the writing and pacing land. And a side objective, stated plainly: the review is a way to show the team's technology and get others to use it. "It's very important that they are visibly impressed with what we do, not just with the content", because the people asked are time-poor, some have written books, and they know publishers.

## The reviewer's first ten minutes (what we design for)

1. **A link that is theirs.** One URL. It opens a page that already knows who they are and why we asked them, without a login and without anything private on the server: the personal part travels in the URL's fragment, which the browser never sends.
2. **Thirty seconds to decide.** Who it is from, why them, what we would like (three chapters, about forty minutes, by a date), and what they get back (their name in the acknowledgements if they want it, the final book, and a reply to every comment).
3. **Reading, with a pen.** The chapters chosen for their kind of reader, on screen or as a PDF made for them (the companion's build), every paragraph with a stable anchor, so a comment points at exact words. A comment is one click on a paragraph: a mark (agree, unclear, wrong, cut, more), a line of text, or both.
4. **The questions, at the end of each chapter.** Three to five, for their kind of reader.
5. **Sending it back, safely.** Comments go to the editor encrypted to his key, never through a public channel unless they choose one.
6. **The loop closes.** When a revision ships, they get a page showing what their comments changed: the paragraph before and after, and the comments that were declined, with a reason.
7. **"How this works", one line at a time.** A side panel that explains each piece of technology as they use it (the link's fragment, the key, the sealed message, the vault), with a link to try it on their own work. That is the showcase.

## The pieces, and how they could work

| Piece | First version (no vault) | With the editor's signature |
|---|---|---|
| **Identity** | A per-person token in the link's fragment | The reader's own PKI key (pki.sgit.ai, `admin/tools/pki-agent.mjs`): onboarding starts with "make your key", and every comment they send is signed (R2) |
| **Personalisation** | Pages pre-computed at build time per persona (`/review/<persona>/`), plus a sealed note per person: an encrypted blob in the site, opened by a key in the fragment; the site holds no name or address in clear | The note sealed to the reader's public key, so only they can open it |
| **The pen lane** | Comments encrypted to the editor's key and sent with SG/Send (pki.sgit.ai/send), or a public issue if they prefer | A vault per reviewer, shared by reader and editor: their marks, our replies, the revision's diff (R1) |
| **The editor's review** | His paper notes become pen notes like the Gen ZX book's (`admin/content/reviews/paper/rc2-0*.json` there), on the same anchors | The same lane as every reviewer, so he tests it first |
| **Diffs** | Per revision: each paragraph before and after, each comment's fate (changed, declined, open), and per reviewer, "what you changed" | |

All of it is deterministic: every page and every sealed note is made by the build from files in the repository; the only thing that varies is the fragment the reader holds. Nothing private is stored in clear in the repository or on the site; names and addresses live only in what the editor keeps himself, or sealed.

## The readers we simulate first

Synthetic readers, in the shape of the PHP newsroom's (`admin/synthetic/` there): fictional people, each a test instrument and never readership, who go through the whole experience in a real browser and say what worked. They are run by synthetic@ (drafted in `team/conductor/staffing/synthetic/`):

| Persona | Who (fictional) | What they judge |
|---|---|---|
| Board member | A non-executive director, not technical, reads on a phone | Can I tell in thirty seconds why this matters and what to ask? |
| CISO | Security leader at a large company | Do the controls hold up; would I trust this team? |
| CTO | Runs engineering at a SaaS company using agents | Is the workflow real, what does it cost, what would I copy? |
| Developer | Builds with AI agents daily | Is it accurate, can I reproduce it, is it too slow? |
| Designer | Reads for clarity and pacing | Do the pages, maps and pictures carry the argument? |
| Project manager | Plans work with teams | Could my team run this; where does it break? |
| Journalist | Covers AI and security | Is there a story, is every claim sourced, what is new? |
| Founder | Building a company on agents | Does this change how I build; would I recommend it? |

Each persona gets the chapters and questions for its kind of reader (from the reviewers study, `../../research/reviewers/`), and each run scores the experience the way the newsroom's do (got the answer, clarity, trust, design, navigation).

## Phases

0. **Design and simulate.** developer@ builds the first version (no vault, no real person); synthetic@ runs the eight personas through it; security reviews the cryptography; designer@ gives it a look. The editor reads the runs.
1. **The editor reviews RC1 with it.** He is the first real reviewer; his notes on paper go in as pen notes.
2. **One friendly reviewer**, chosen by the editor, with his go.
3. **The first wave**, from the reviewers study, each name checked by hand and signed by the editor.

## Who does what

- **developer@** (new, `team/conductor/staffing/developer/`): the review pages, the sealed notes, the pen lane, the diffs.
- **synthetic@** (new, `team/conductor/staffing/synthetic/`): the eight personas, run in a real browser, scored and published.
- **designer@**: the look of the review pages and the review PDFs.
- **security**: the design of keys, sealing and the pen lane, before anything real is sent.
- **publisher**: the review editions of the book (the build).
- **storyteller**: the questions per persona, and the cover letter's words.
- **conductor**: this brief, the decisions, and every outward step put to the editor first.

## What waits on the editor

- **R1**: a vault per reviewer, against the rule "no vaults for now".
- **R2**: onboarding every reviewer with their own PKI key.
- The personas (keep, change, add).
- Who the friendly first reviewer is, and when.
