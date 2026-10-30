# The market on Leanpub, as it looks to a book like ours

Read on 30 October 2026, directly from leanpub.com (book pages, store category pages, store search) through curl, plus web search to find titles. Author of this note: research sub-agent for the conductor.

## How to read this note

- Every price, completeness figure, update date and page count below was read from the book's own Leanpub page (https://leanpub.com/<slug>) on 30 October 2026. "Not shown" means the page did not show it. Nothing is guessed.
- **Readers counts are almost never shown.** Of about 40 book pages read, only one showed a count: Pwning OWASP Juice Shop, 18,411 readers (https://leanpub.com/juice-shop). None of the new AI and security books shows a count. So I can say nothing about sales; I can only say who is listed first.
- Category order on Leanpub store pages defaults to "Bestsellers Last Week" (the sort menu also offers Bestsellers All Time, New Releases, Free Minimum Price, Free With Membership, Free For Everyone, Recently Updated). The order is shown without numbers.
- Cover images were not examined. Blurbs and subtitles were.
- "Steve Publications" appears as the author name on a large number of 2026 titles across the AI, security and Claude shelves (it is the public author name on the page). I report it as shown and draw no conclusion about who is behind it.
- No fetched page contained instructions aimed at me.

## Leanpub's own categories relevant here

Top categories on every store page: Computers and Programming, Artificial Intelligence, Software, Software Engineering, Agile, Software Architecture, Management, Python, Leadership, Self-Help, Web Development, DevOps, JavaScript, Lean, Cloud Computing, Data Science, Education, Testing, Personal Transformation, Computer Science. Narrower category pages that exist and are populated (all under https://leanpub.com/store/books/c/):

- `ai` (Artificial Intelligence): the main shelf. (`artificial_intelligence` is a 404.)
- `agentic_engineering`: 18 pages of results on 30 October 2026 (the last page link read "page=18").
- `harness_engineering`: a small shelf of agent-control books.
- `ai_governance`: small (about eight titles on its first page).
- `computer_security` and `cyber_security`: large; dominated by exam guides and offensive technique.
- `leadership`, `software_engineering`, `devops`: general shelves.
- `devsecops`: 404 (no such category; DevSecOps books sit under Security Engineering, Computer Security, DevOps).

Authors choose categories on their own pages, so books carry several (see the "Categories" column below).

Bestseller lists seen (by sort order, no numbers):
- Artificial Intelligence, bestsellers all time: The Hundred-Page Machine Learning Book, The Hundred-Page Language Models Book (both Andriy Burkov), Super Study Guide: Transformers & Large Language Models (Afshine and Shervine Amidi), Patterns of Application Development Using AI (Obie Fernandez), Machine Learning Engineering (Burkov). These are older, technical, data and model books. (https://leanpub.com/store/books/c/ai?sort=bestsellers_lifetime)
- Artificial Intelligence, bestsellers last week: Super Study Guide again, then a run of new agent and Claude titles (Bulletproof Knowledge, Agentic Programming, Claude Code Handbook for Software Engineers, Running Local LLMs on Your Own Hardware, Reverse Engineering with Claude Code, The Art of Harness Engineering, The Agentic AI Book, The Claude Skills Handbook). (https://leanpub.com/store/books/c/ai)
- Computer Security, bestsellers all time: CISSP: The Last Mile, JavaScript for Hackers, CISM: The Last Mile, Breaking into Information Security, Pwning OWASP Juice Shop, CISA: The Last Mile. Exam prep and hacking technique. No AI-agent title in the top ten. (https://leanpub.com/store/books/c/computer_security?sort=bestsellers_lifetime)
- Computer Security, bestsellers last week: the same exam guides, then Reverse Engineering with Claude Code, BlackHat C, Intelligent Discovery. (https://leanpub.com/store/books/c/computer_security)
- Agentic Engineering, bestsellers last week: Harness Engineering (Ian Johnson), Claude Code: From Basics to Mastery, Claude Code Handbook for Software Engineers, Microsoft Agent Framework in .NET, The Art of Harness Engineering, The Agentic AI Book. (https://leanpub.com/store/books/c/agentic_engineering)
- AI Governance: When AI Takes Action first. (https://leanpub.com/store/books/c/ai_governance)
- I found no featured list in these areas; I did not open the store's Featured tab.

## The books (36, each read on its own page)

Price is minimum / suggested in US dollars. Completeness is the page's "% complete" line and last-update date. Samples: "sample" means a Download Free Sample button is present. Readers: not shown unless stated.

### A. AI agents and agentic workflows

| Title (subtitle) | Author | URL | Price | Status, last update | Length | Notes |
|---|---|---|---|---|---|---|
| The Agentic AI Book (language models to production-ready multi-agent systems) | Dr. Ryan Rad | https://leanpub.com/TheAgenticAIbook | $23 / $45 | 100%, 2026-10-01 | not shown | no sample; links to paperback on Amazon; highest suggested price in the AI set |
| Agentic Engineering (From Execution to Orchestration) | not read | https://leanpub.com/agenticengineeringv1 | $24 / $48 | 100%, 2026-05-03 | 28 chapters | sample; categories Software Engineering, AI, Agentic Engineering |
| Agentic Engineering (production-grade agentic systems) | Atanu (surname cut off on page) | https://leanpub.com/agentic-engineering | price not shown on page text | not shown | 20 chapters (from search text) | categories LLMs, Agentic Engineering, Systems Engineering |
| Agentic Programming (From Prompts to Production: A Path to AI Fluency) | Jerod W. Wilkerson | https://leanpub.com/agenticprogramming | $33 / $38 | 100%, 2026-10-24 | not shown | sample; "AI Fluency Ladder" framing |
| Agentic Coding: Building Reliable Software with AI Agents | not read | https://leanpub.com/agenticcoding | not shown | not shown | 24 chapters | |
| Understanding Agentic AI | not read | https://leanpub.com/understanding_agentic_ai | $19 / $29 | not shown | not shown | sample; a free sign-up edition also exists |
| Build Intelligent Agents | not read | https://leanpub.com/buildintelligentagents | $19 / $29 | not shown | not shown | sample; category AI |
| The Autonomous Operator | not read | https://leanpub.com/the-autonomous-operator | $19 / $29 | 100%, 2026-09-22 | 17 chapters | no sample |
| Microsoft Agent Framework in .NET | Daniel Costea | https://leanpub.com/agentframework | $29.99 / $39.99 | 82%, 2026-10-06 | not shown | sample; code-first, C# |
| Building Autonomous Coding Agents (Design, Safety, and Local-First Operation of Unattended AI Development Systems) | Yohan J. Rodriguez | https://leanpub.com/building-autonomous-coding-agents | $19.99 / $29.99 | not shown | 622 manuscript pages (blurb) | sample; the "safety" angle is nearest to ours among builder books |
| Confidently Wrong | not read | https://leanpub.com/confidentlywrong | $19 / $24 | not shown | not shown | sample; business humour and satire plus AI and Agentic Engineering; a story-form entry |
| AI Development Team (A CTO's Playbook ...) | not read | https://leanpub.com/theaidevelopmentteam | $6 / $9 | not shown | not shown | cheapest of the "AI team" titles |
| The Meta-Engineer (10x Was the Floor) | not read | https://leanpub.com/the-meta-engineer | $19 / $29 | not shown | not shown | |

### B. Claude and coding-agent books

| Title | Author | URL | Price | Status, last update | Length | Notes |
|---|---|---|---|---|---|---|
| Claude Code: From Basics to Mastery (The Complete Guide to Agentic Software Development in 2026) | Steve Publications | https://leanpub.com/masteringclaudecode | $25 / $35 | 100%, 2026-10-13 | 210 pages | sample |
| Claude Code Handbook for Software Engineers (An Engineering Reference for Agentic Development) | Steve Publications | https://leanpub.com/claudecodehandbookforsoftwareengineers | $25 / $35 | 100%, 2026-10-28 | 180 pages | sample; covers security and team adoption |
| Building with Claude Code: The Agentic Development Handbook | not read | https://leanpub.com/buildingwithclaudecode | $10 / $20 | not shown | 16 chapters | no sample |
| Building Complex Software with GenAI (Build effectively with Claude AI) | David Cornelson | https://leanpub.com/building_complex_software_with_genai | $19 / $29 | not shown | not shown | no sample; closest to a making-of; category Computers and Programming only |
| Reverse Engineering with Claude Code | Steve Publications | https://leanpub.com/reverseengineeringwithclaudecode | not read | not read | not read | top of both Security and AI weekly lists; stresses "evidence, accuracy and reproducibility" |
| Claude Skills Handbook | Steve Publications | https://leanpub.com/theclaudeskillshandbook | not read | not read | not read | |

### C. Harness, reliability and engineering management

| Title | Author | URL | Price | Status, last update | Length | Notes |
|---|---|---|---|---|---|---|
| Harness Engineering (Building Reliable Workflows Around Non-Deterministic Agents) | Ian Johnson | https://leanpub.com/harness-engineering | $20 / $30 | 100%, 2026-07-22 | not shown | no sample; first in the Agentic Engineering bestseller order |
| The Art of Harness Engineering (... Testing, and Governing AI Systems in Production) | Steve Publications | https://leanpub.com/theartofharnessengineering | $29 / $39 | 100%, 2026-10-01 | 224 pages | sample; "testing, guardrails, observability and governance" |
| Leading Engineering Teams in the AI Era | Caio Incau | https://leanpub.com/engineering-leadership-ai | $14.99 / $24.99 | 100%, 2026-06-15 | not shown | blurb claims "the first book that addresses engineering management specifically for the AI-native era"; every chapter produces an artifact (rubric, budget template, rollout plan) |

### D. AI security, agent security, governance

| Title | Author | URL | Price | Status, last update | Length | Notes |
|---|---|---|---|---|---|---|
| The AI-Era CISO (A Strategic Guide to Security Leadership in the Age of AI) | Steve Publications | https://leanpub.com/theai-eraciso | $25 / $35 | 100%, 2026-10-03 | 151 pages | sample; also a Reader Membership credit; top of cyber_security |
| AI Security Governance and Assurance | Steve Publications | https://leanpub.com/aisecuritygovernanceandassurance | $19 / $29 | 100%, 2026-10-03 | 175 pages | sample |
| The CISO's AI Firewall | Steve Sharma | https://leanpub.com/cisos-ai-firewall | $19 / $29 | 100%, 2026-07-13 | 14 chapters (blurb) | five-stage "Decision Journey" |
| When AI Takes Action (A Practical Guide to Securing and Governing AI Agents) | Igor van der Burgh | https://leanpub.com/whenaitakesaction | $19 / $29 | not shown | not shown | no sample; follows "a fictional enterprise team"; AI Governance category; first in that category |
| Zero Trust AI (Architecting Defenses in the Age of LLMs) | Peter Isberg | https://leanpub.com/zero-trust-ai | $19 / $29 | not shown | not shown | sample; opens with a short prompt-injection story |
| The Agentic Security Playbook | not read | https://leanpub.com/the-agentic-security-playbook | $9 / $19 | 100%, 2026-10-17 | not shown | no sample; same price pair as ours |
| AI Security for Developers | not read | https://leanpub.com/ai-security-for-developers | $9 / $15 | not shown | 14 chapters | sample |
| Agent SecOps | not read | https://leanpub.com/agentsecops | $19 / $29 | not shown | not shown | sample |
| AI Agent Security | not read | https://leanpub.com/aiagentsecurity | $19 / $29 | not shown | not shown | no sample |
| AI Agent Security: A Field Manual | Shugo Nozaki | https://leanpub.com/agent-security | suggested $9 (minimum read as free/blank) | 100%, 2026-09-04, "+15,445 words in the last 90 days" | not shown | Leanpub shows recent word growth on in-progress books |
| The Prompt Injection Bible | not read | https://leanpub.com/the-prompt-injection-bible | $9.99 / $9.99 | not shown | not shown | |
| Governance Before Decision (A Field Guide to Proof, Permission, and Human-Controlled AI Execution) | Kari Hyotyla | https://leanpub.com/governancebeforedecisi | $59 / $69 | not shown | 86 pages | the highest price seen; a Spanish edition exists |
| Cyberattacks and the Organization | Igor van der Burgh | https://leanpub.com/cyberattacksandtheorganization | $19 / $29 | not shown | not shown | board and leader audience |
| Cognitive Trust Architect | Sourena Khanzadeh | https://leanpub.com/cognitivetrustarchitect | not shown | not shown | not shown | |

### E. Application security, DevSecOps, practitioner security

| Title | Author | URL | Price | Status, last update | Notes |
|---|---|---|---|---|---|
| DevSecOps: A Complete Visual Guide | not read | https://leanpub.com/devsecops-visual-guide | $8 / $19 | 100%, 2026-10-26 | sample |
| App Security for Vibe Coders | Justin Farmer | https://leanpub.com/appsecurityforvibecoders | $9 / $12 | 100%, 2026-10-28 | sample; "copy-paste prompts" |
| Intelligent Discovery (AI in finding and fixing vulnerabilities) | Steve Publications | https://leanpub.com/intelligentdiscovery | $25 / $35 | 100%, 2026-10-17 | 193 pages; sample |
| Pwning OWASP Juice Shop | Bjorn Kimminich | https://leanpub.com/juice-shop | free / $19.99 | not shown | 440 pages; **18,411 readers shown**; the only count seen; a free-minimum security book with a large audience |
| CISSP / CISM / CISA / CRISC / CCSP: The Last Mile | Pete Zerger | e.g. https://leanpub.com/cissplastmile | not read | not read | exam guides; fill the top of Computer Security |

### F. The editor's own Leanpub record

Author page https://leanpub.com/u/DinisCruz (search text, 30 October 2026): ten published books and one unpublished; titles include Generation Z Developers (60% complete, last updated October 2018, $10), Practical Git and GitHub (free draft), Measure Software Quality using Application Security (free with membership), and a "Practical" bundle (https://leanpub.com/b/Practical, suggested total $37.98, bundle $10). I did not open the author page. Takeaway: an existing author page and bundle precedent, with stale in-progress titles that a reader may see next to the new book.

### G. Name check

Leanpub store search for "ultimate insider", "insider threat" and "agent insider" (https://leanpub.com/store/books?search=ultimate+insider and the other two) returned no book with "The Ultimate Insider" as a title and no insider-risk book on AI agents. The results were unrelated (a fiction series by an author called Lefty Insider, and a short guide "Understanding AI Agents in 15 Minutes" by Ultimate Dimensions, whose blurb mentions running three agents together). The title is free on Leanpub.

## The landscape

**Crowded.**
- "Learn Claude Code / build agents" (groups A and B): dozens of new titles in October 2026 alone, many 100% complete within weeks of starting, several from the same author name. Price band $19 to $35 minimum.
- Agentic engineering and harness engineering: 18 pages of the first, a smaller but fast-growing second.
- Agent security as technique: prompt injection, MCP, sandboxing, zero trust. Roughly ten titles, mostly $9 to $19 minimum.
- Exam prep dominates Computer Security bestsellers.

**Thin.**
- Governance and leadership for agents: AI Governance has about eight titles; three or four CISO-facing books ($19 to $25 minimum). They are frameworks and guides. One uses a fictional team (When AI Takes Action); none read is built on a real, dated, checkable case.
- Engineering management for agent teams: one clear title (Leading Engineering Teams in the AI Era), which says it is the first.
- DevSecOps/AppSec: few, recent ones are visual or beginner guides at $8 to $12 minimum.

**Empty, as far as I could find.**
- A book that treats the agent as the insider and shows the controls working on a real day: no title matched, and store search for insider returned nothing relevant.
- A real, git-evidenced account of a team of agents doing a security job in a day.
- "Brakes make you faster" as a thesis. Harness Engineering (Ian Johnson) and The Art of Harness Engineering are the nearest, but they teach reliability engineering, not an insider-control record.
- A making-of in the security shelf. Building Complex Software with GenAI is the only making-of seen, and it is about a game platform.

**Naming patterns.** Title is short and subtitle is long and descriptive: "X: A Practical Guide to ...", "From A to B", "A Strategic Guide to ...", "A Field Manual", "Playbook", "Handbook", "Bible". Leadership books name a role (CISO, CTO, engineering leader). Story titles are rare (Confidently Wrong). Blurbs often open with a scenario ("Your agent reads a web page...", "Your board just asked...").

**Price bands (read from pages).** Minimum: $0 (Juice Shop, sign-up editions), $6 to $12 (cheap guides and playbooks), $14.99 to $19.99 (middle), $19 (the commonest minimum in AI and security), $23 to $33 (premium handbooks), $59 (one outlier). Suggested: $9 to $19 low, $29 the commonest, $35 to $48 premium, $69 outlier. Most security-leadership books ask $19 to $25 minimum and $29 to $35 suggested. Our $0 / $19.99 is lower than that and is the same shape as Juice Shop's free minimum.

**How in-progress books are positioned.** Leanpub shows "% complete" and last-updated date, and on active books "+N words in the last 90 days". Complete books show "100% complete" with a recent date; in this sample almost every finished book was updated in 2026. Partial books carry 82% (Microsoft Agent Framework). Old partial books (Dinis Cruz's 2018 title) read as stale. All readers get free updates (page text). Many listings add "Also available for 1 book credit with a Reader Membership".

**Presentation patterns.** Free sample PDF and EPUB (about half of the books); chapter count or page count in the page (151 to 622 pages); named audience in the blurb; "Key benefits" bullets (When AI Takes Action); format badges PDF, EPUB, WEB APP; reader-membership credit; a paperback link on Amazon (The Agentic AI Book); packages on textbook-style titles; bundles (Claude specials bundle at https://leanpub.com/b/claudespecialsbundle, translated bundles). Leanpub also posts "Book LAUNCH" posts on its blog for some titles (for example https://leanpub.com/blog/leanpub-book-launch-claude-code-building-production-agents-that-actually-scale-by-thomas-de-vos/); I do not know how titles are chosen.

## Where this book would sit

**What it has that none read has.** One dated case with a git record anyone can check; the controls shown working (session keys, reviews before and after each wake, a hold, decisions only the editor signs); the insider framing; failures left in; an editor with a long application security record and an existing Leanpub author page.

**What it lacks.** No hands-on code or attack labs (by team rule it will have none); no tool name in the title (Claude, MCP, OWASP), which is how most buyers search; no reviews or readers on day one; the books at the top of the lists are exam guides, hacking technique and tool how-tos, which ours is not; fewer pages than the handbooks (151 to 224 pages is the norm for finished titles; our length is for the plan to settle).

## What this means for the book

These are options for the editor to sign, not decisions.

- **Positioning.** Take the empty slot: "the agent as insider, shown on one real day". Sell it as the governance book that has evidence, the case the CISO guides lack. Do not enter the Claude-how-to or prompt-injection technique shelves. Lead with CISOs and security leaders; builders second.
- **Title and subtitle.** "The Ultimate Insider" is free on Leanpub. Competitors pair a short title with a descriptive subtitle that carries the search words; do the same. Shape: *The Ultimate Insider* / "How one person and a team of AI agents built a security talk in a day, and the controls that kept them in check". Put "AI agents", "security" and "controls" in the first line of the blurb. A scenario opening ("Your agent..." style) fits the pattern; open on the day and the git record.
- **Category.** Choose several, as every competitor does: Artificial Intelligence (the main shelf), Computer Security, AI Governance (small, so a good ranking is easier), and Agentic Engineering or Harness Engineering (close in theme to the "brakes" thesis). Cyber Security is crowded with exam and offensive titles; use it last.
- **Price.** $0 minimum, $19.99 suggested sits under the common $19 / $29 pair and matches the one free-minimum security book with a large audience (Juice Shop, 18,411 readers). It also matches the editor's earlier free and low-price titles. Raising the suggested price to $29 would match what most security-leadership books ask; that is the editor's call. Note that other books with the same $9 / $19 pair exist (The Agentic Security Playbook).
- **Presentation.** Publish a free sample chapter (about half of the competitors do); show a chapter count and page count; name the audiences; keep "% complete" at 100% with a recent update date, or, if launched in progress, say what is missing and keep adding words (the page shows the growth; stale partial books look abandoned); state plainly that it was written with AI agents and how it was checked (the one competitor that discloses AI help does so on its page); link the repository record; consider a launch post on Leanpub's blog and a Reader Membership listing; leave out a bundle with the older titles unless there is a reason.
- **Not yet known.** Readers and sales for any competitor except Juice Shop; Leanpub's Featured list; cover norms; how Leanpub search ranks. The bestseller order is visible but has no numbers.

## Where this came from

Everything below was read on 30 October 2026.

- Store category pages, default and bestseller sorts, at https://leanpub.com/store/books/c/ai, /c/ai?sort=bestsellers_lifetime, /c/agentic_engineering, /c/ai_governance, /c/computer_security (default and bestsellers_lifetime), /c/cyber_security, /c/harness_engineering. 404 for /c/artificial_intelligence and /c/devsecops.
- Store search pages https://leanpub.com/store/books?search=ultimate+insider, insider+threat, agent+insider.
- Book pages at https://leanpub.com/<slug> for each slug in the tables above (prices, completeness, dates, page and chapter counts, samples, categories, readers where shown).
- Web search ("site:leanpub.com" queries on agents, agent security, AI governance and CISO, DevSecOps, the editor's name, written-with-AI, agentic engineering, insider threat) to find titles and, for a few rows marked "not read", the descriptions; those rows are search text only.
- Leanpub's terms (free updates for all readers, 60-day refund) are from page footers and search text.
