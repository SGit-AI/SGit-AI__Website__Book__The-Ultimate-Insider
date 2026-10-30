# The two and a half years: a dossier for the book

Researcher, for the conductor's RC1 work, 30 October 2026. Written for the editor's brief of 30 October 2026 (`briefs/2026-10-30__in-session/01-principles-maps-and-the-plumbing.md`): the day of 29 October 2026 as the meeting point of about two and a half years of his work, the plumbing it stood on, and Wardley maps.

**Method.** Public sources only, read on 30 October 2026: newsroom.sgit.ai (its `llms.txt`, `newsroom/wire.json` and the `.md` twins of about sixty articles), sgit.ai and its subdomains (their `llms.txt` files), diniscruz.ai, thecyberboardroom.com, PyPI's JSON release history, four LinkedIn articles whose pages carry a `datePublished`, one slide deck PDF on files.diniscruz.ai, and the public GitHub repositories owasp-sbot/OSBot-Utils, owasp-sbot/Memory-FS, owasp-sbot/Issues-FS, SGit-AI/SGit-AI__CLI, the-cyber-boardroom/myfeeds_ai and the-cyber-boardroom/cbr-investment (cloned, history read). The talk's repository was read at `298be4e`, read only, at `/home/user/sgit-ai/sgit-ai__website__presentation__the-ultimate-insider`.

**What this file is not.** It is not the claims register. Every number below carries its source, but none of them may go into a chapter until the researcher has entered it in `claims/`. Where an article is the author's own account (most newsroom articles are written from his voice memos by an agent, and say so), the entry says "his account". Where a date or link is not public, it says "not found in public sources".

**Two things the brief asked for that the public record does not give.**

- **When he went full time on The Cyber Boardroom: not found in public sources.** The public anchors are: the Athena MVP post of 17 September 2023; the company's incorporation on 8 April 2024, announced as the result of "nearly all of my spare time" (so not yet full time on that date); the first PyPI release of the website on 7 June 2024; and a slide in a deck dated 29 January 2025 that says "Last 10 months of my life. All open sourced", which points to about March or April 2024. On 18 October 2026 he wrote "I have been doing AI for the last two years and a bit". Those fit the editor's "two and a half years", but none of them names the day he went full time.
- **"SHarness was way faster compared to sgit": no public source makes that comparison.** What the sources give is the two timelines: SHarness went from a narrow problem on the morning of 24 October 2026 to a site, a design and `sharness-ai` 0.2.0 on PyPI in five days; sgit went from SG/Send's first commit on 8 February 2026 to the `sgit-ai` package on 20 March 2026, and to its present form over eight months. The comparison is the editor's.

---

## 1. Timeline, from The Cyber Boardroom to 29 October 2026

Each entry: when it started, what it is in one sentence, what it gave the day, and its source with the date the source gives. Entries before 2024 are included where the day used something that began there.

### Before the window: what was already in place

**2018: Generation Z Developers, with Wardley's pioneers, settlers and town planners in its outlines.**
- What: a book on Leanpub, 60% complete, last updated 8 October 2018, whose outlines already included "pioneers, settlers and town planners, graphs, your future self, publishing, GitHub as your CV" (his account, 18 October 2026).
- Gave the day: the vocabulary the storyteller used for map 4 of the talk (pioneers, settlers, town planners, at the editor's beat 3e), and it is the root of the Gen ZX Founders book the brief names.
- Source: https://newsroom.sgit.ai/articles/generation-z-developers-again.html (2026-10-18).

**22 February 2020: OSBot-Utils, the library underneath the estate.**
- What: the `osbot-utils` Python library in the owasp-sbot organisation; its first commit is 22 February 2020.
- Gave the day: the release scheme (next entry) and Type_Safe (below).
- Source: https://github.com/owasp-sbot/OSBot-Utils, first commit `885128d`, 2020-02-22 (repository history, read 30 October 2026).

**27 October 2023: CI owns the version, first in OSBot-Utils.**
- What: two composite GitHub Actions that fetch the tags, take the latest, bump the last number on `dev` or the middle one on `main`, write the version file and tag the commit as "GitHub Actions". A first attempt on 30 July 2021 "did not stick".
- Gave the day: the rule that nobody but CI writes the number. The talk's `.github/workflows/release.yml` opens with "CI owns the version" and a link to the newsroom article; 210 releases were numbered by CI before the talk (case study, below).
- Sources: commit `e53d055`, 2023-10-27 00:52:27 +0100, Dinis Cruz, "Added new version of .github workflows and actions (namely around the autotagging)", and commit `753ef2c`, 2023-10-27 02:02:53 UTC, author GitHub Actions, in https://github.com/owasp-sbot/OSBot-Utils (both verified in the history on 30 October 2026; the repository carries 1,129 tags); the history table in https://newsroom.sgit.ai/articles/ci-owns-the-version.html (2026-10-27), itself taken from sharness.ai's conductor's reading of 26 October 2026.

**17 September 2023: Athena, the first GenAI bot that became The Cyber Boardroom's advisor.**
- What: an MVP of a bot built on AWS serverless, Python, Flask and Hugging Face, "on top of chatGPT", following an earlier Hugging Face bot.
- Gave the day: indirectly. Athena is where he says he learnt "what personas and customised output are worth" (not-a-straight-line, below).
- Source: https://www.linkedin.com/pulse/mvp-athena-bot-built-aws-serverless-python-flask-huggingface-cruz/ (datePublished 2023-09-17).

### 2024: The Cyber Boardroom

**3 January 2024: Kwargs_To_Self, the class that became Type_Safe.**
- What: a helper class in OSBot-Utils for classes with many parameters; within days it checked types on class variables (6 January) and experimented with type safety (17 to 18 January). On 1 June 2024 it was given "this more correct name", Type_Safe (`4edb92e`); the file was renamed on 1 July 2024 (`d52dc70`); on 3 January 2025 every Type_Safe class moved into its own `type_safe` folder (`be1aaba`).
- Gave the day: not directly (see section 2, Type_Safe). It is the base of the sgit CLI, whose vaults carried the team's board and mail on the day.
- Source: https://github.com/owasp-sbot/OSBot-Utils, commits `0df0830` (2024-01-03), `c04be1e` (2024-01-06), `6d14889` (2024-01-17), `4edb92e` (2024-06-01), `d52dc70` (2024-07-01), `be1aaba` (2025-01-03).

**22 February 2024: the public writing starts.**
- What: a talk at the OWASP London chapter, "It's 2024 and, with GenAI, we can finally make AppSec work". diniscruz.ai says its writing "runs from February 2024 onwards".
- Gave the day: the habit of writing everything down in public, which the brief calls the articles that "intersect with a lot of this".
- Sources: https://diniscruz.ai/2024/02/22/its-2024-and-with-genai-we-can-finally-make-appsec-work.html (2024-02-22); https://diniscruz.ai/about/index.html (undated page, site v0.1.1).

**8 April 2024: The Cyber Boardroom Ltd incorporated.**
- What: a GenAI platform to help boards and executives with cyber security, with Athena as its advisor, serverless on AWS. The announcement says he had "devoted nearly all of my spare time" to GenAI in the preceding months. diniscruz.ai now describes The Cyber Boardroom as "The UK company behind sgit.ai and RiskMandate.ai".
- Gave the day: the company the talk was billed under (the IOActive event page's address, quoted in the talk's `BRIEF.md`, reads "dinis-cruz-founder-of-the-cyber-boardroom"), and, in his account, two lessons: personas and output shaped to the reader, and the need for somewhere to keep confidential data, which "is what I eventually built as sgit".
- Sources: https://www.linkedin.com/pulse/cyber-boardroom-ltd-has-been-created-its-official-now-dinis-cruz-oaj8e (datePublished 2024-04-08); https://diniscruz.ai/building/index.html (undated, site v0.1.1); https://newsroom.sgit.ai/articles/not-a-straight-line.html (2026-10-12, his account, "summarised from memory").

**7 June 2024: the Cyber Boardroom website and Athena on PyPI.**
- What: `cbr-website-beta`, 431 releases from 7 June 2024 to 13 December 2024; `cbr-athena`, 109 releases from 13 June 2024 to 29 January 2025. thecyberboardroom.com still serves "v0.221.0" in its footer.
- Gave the day: the release rate that CI-owned versions made cheap, the same scheme as OSBot-Utils. The repositories themselves (github.com/the-cyber-boardroom/cbr-website-beta and cbr-athena) are not public: a clone asks for credentials.
- Sources: https://pypi.org/pypi/cbr-website-beta/json and https://pypi.org/pypi/cbr-athena/json (read 2026-10-30); https://thecyberboardroom.com (read 2026-10-30).

**28 June 2024: provenance, as a talk.**
- What: "Deterministic GenAI Outputs with Provenance", delivered at the Global OWASP AppSec in Lisbon.
- Gave the day: the earliest public statement of the idea that became the talk's claims register and sources page (section 2).
- Source: https://diniscruz.ai/2024/06/28/deterministic-genai-outputs-with-provenance__owasp-appsec-lisbon__gslides.html (2024-06-28).

**15 and 30 July 2024: the first MVP, then the Community Edition.**
- What: "Why, How and What v0.4, first MVP" (15 July), then the Community Edition, "free to use and is based on a large number of open source python packages that I'm also releasing" (30 July).
- Gave the day: open source as the default, which is why the day's tools and records could be reused and read by anyone.
- Sources: https://www.linkedin.com/pulse/cyber-boardroom-why-how-what-v04-first-mvp-dinis-cruz-pbfge/ (datePublished 2024-07-15); https://www.linkedin.com/pulse/introducing-community-edition-cyber-boardroom-dinis-cruz-xsope/ (datePublished 2024-07-30).

**4 December 2024: MyFeeds.**
- What: personalised, role-aware news feeds on semantic graphs; he paused it when "the industry was silent" (his account).
- Gave the day: the graph thinking behind the newsroom and the fractal view of maps (section 3). First commit 4 December 2024; `myfeeds-ai` on PyPI from 21 December 2024 to 15 May 2025.
- Sources: https://github.com/the-cyber-boardroom/myfeeds_ai, first commit `02c6dbb`, 2024-12-04; https://pypi.org/pypi/myfeeds-ai/json; https://newsroom.sgit.ai/articles/not-a-straight-line.html (2026-10-12).

### 2025: the libraries and the writing

**29 January 2025: "My journey building a GenAI startup: the power of MVPs and CI pipelines".**
- What: a deck (delivered at the AI Security Collective meetup in London on 26 February 2025) whose slides say "Every release to main creates: PyPi, Docker Image and AWS AMI", "CI Pipeline, Git version control (autotagging)", "Auto-tag everything", "Document everything (large tech documents co-created with LLMs)", and "Last 10 months of my life. All open sourced".
- Gave the day: the earliest public statement, in his own slides, of the plumbing the day ran on: CI that releases on every push, automatic tags, and documents written with models.
- Sources: https://diniscruz.ai/2025/01/29/my-journey-building_a_genai_startup__the-power-of-mvps-and-ci-pipelines__part-1.html (2025-01-29); the PDF at https://files.diniscruz.ai/s3/pdf/2025/01/29/my-journey-building_a_genai_startup__the-power-of-mvps-and-ci-pipelines__part-1.pdf.

**2 February 2025: MGraph-DB; and the news essays.**
- What: a memory-first graph database (`mgraph-db`, 74 releases from 2 February 2025 to 10 January 2026); and the essays on monetising trust (2 February), fact provenance (5 February) and micro and nano payments (2 April 2025), which he calls "the foundations the newsroom now stands on".
- Gave the day: the newsroom, whose agents and articles the talk team copied.
- Sources: https://pypi.org/pypi/mgraph-db/json; https://diniscruz.ai/2025/02/05/the-future-of-news-building-trust-through-fact-provenance.html (2025-02-05); https://newsroom.sgit.ai/articles/not-a-straight-line.html (2026-10-12).

**26 May 2025: Memory-FS.**
- What: a file-system abstraction "used to build file-based representations of documents and standards"; first commit 26 May 2025, 39 releases to 31 January 2026; a white paper used it to represent the GDPR as files (2 July 2025).
- Gave the day: memory as versioned files rather than a store. sgit's speed-ups name "Memory-FS's reads by offset" among their sources. The talk's repository at `298be4e` does not name Memory-FS.
- Sources: https://github.com/owasp-sbot/Memory-FS, first commit `de32536`, 2025-05-26; https://pypi.org/pypi/memory-fs/json; https://diniscruz.ai/2025/07/02/using-memory_fs-to-build-a-file-based-representation-of-the-gdpr-standard.html (2025-07-02); https://newsroom.sgit.ai/articles/what-sgit-does-that-git-does-not.html (2026-10-27).

**16 June 2025: the first public trace of Claude in his commits.**
- What: a Memory-FS commit message, "adding the missing tests (using Claude to help with test creation)"; on 9 July 2025 an OSBot-Utils commit adds "detailed documentation (created by Claude based on the source code)". These are the earliest mentions of Claude found in the commit messages of the repositories read; his first experiments with Claude may be earlier and are not found in public sources.
- Gave the day: the start of the line that ends in a team of Claude agents. On 9 October 2026 he wrote that his guide to working with Claude "comes from about a year of doing this every day".
- Sources: https://github.com/owasp-sbot/Memory-FS commit `34d99ce` (2025-06-16); https://github.com/owasp-sbot/OSBot-Utils commit `9c8503d` (2025-07-09); https://newsroom.sgit.ai/articles/how-i-work-with-claude.html (2026-10-09).

**2025: ThreatModCon, Wardley maps inside a threat modelling talk.** Exact date not found in public sources; see section 3.

### 2026: Issues-FS, sgit, the network of sites, the newsroom, SHarness

**4 February 2026: Issues-FS.**
- What: "a git-native issue tracker where the issues are files and the files are a graph"; it has a lite form, Issues-FS-lite, of three folders (`issues/open/`, `issues/blocked/`, `issues/done/`) moved with four `mv` operations, where an agent may read another agent's folder and must not write into it. Its site says "the philosophy was written here in February 2026".
- Gave the day: the team's board, `<you>/issues/{open,blocked,done}/`, and the rule "read every folder, write only your own".
- Sources: https://github.com/owasp-sbot/Issues-FS, first commit `21e1f27`, 2026-02-04 (first commits by an author named Claude from 9 February 2026); https://pypi.org/pypi/issues-fs/json (4 to 15 February 2026); https://issues-fs.sgit.ai/llms.txt (site v0.1.2, 22 August 2026).

**8 February 2026: SG/Send, the service where the server holds nothing.**
- What: encrypted file sending, first commit 8 February 2026, live at send.sgraph.ai on 13 February; the first specification said "files are encrypted on the client before upload, and the decryption key is never sent to the server".
- Gave the day: the vault server (dev.send.sgraph.ai) that held the team's public board and mail vaults, and the habit of briefs and debriefs (the record counts 1,389 brief files and 268 debriefs).
- Source: https://newsroom.sgit.ai/articles/from-send-to-sgit.html (2026-10-15; his memory checked by an agent against the repositories).

**3 March 2026: sgit.**
- What: encrypted version control with Git's model; the command line started on 3 March 2026 as sg-send-cli, became `sgit` on 16 March and was published to PyPI as `sgit-ai` on 20 March (109 releases to 28 October 2026). Its first commit after the initial one is by an author named Claude: "Session 1: Bootstrap repo with Safe_* types, schemas, Vault__Crypto, and CI/CD"; 1,077 of its 1,779 commits carry that author name.
- Gave the day: the vaults (`tui-issues-public`, `tui-mail-public`, the researcher's `tui-evidence-public`), the `sgit` commands the agents ran, and the vault key discipline.
- Sources: https://github.com/SGit-AI/SGit-AI__CLI (first commit `1b01902`, 2026-03-03; `ae9f85e`, 2026-03-03); https://pypi.org/pypi/sgit-ai/json; https://newsroom.sgit.ai/articles/from-send-to-sgit.html (2026-10-15); https://newsroom.sgit.ai/articles/what-sgit-is.html (dated 2026-08-25 in the newsroom's wire).

**May 2026: the SG/Send strategy as seven Wardley maps on LinkedIn.** See section 3. Exact date not found in public sources beyond "May 2026".

**19 June 2026: the turn towards RiskMandate.**
- What: an SG/Send strategy brief that set the priority as profitability; "from then on the briefs turn towards risk acceptance and RiskMandate". RiskMandate is "the business risk layer for autonomous systems" and sells Agent Behaviour Policies and licences to operate.
- Gave the day: the talk's way out (measure the reach, write down what stands in the way, a licence to operate) and the policy shape of every agent's `policy.json`.
- Sources: https://newsroom.sgit.ai/articles/from-send-to-sgit.html (2026-10-15); https://diniscruz.ai/building/index.html. RiskMandate's founding date: not found in public sources.

**17 to 26 August 2026: the newsroom's first articles and the network of sites.**
- What: the earliest article in the newsroom's wire is dated 17 August 2026 ("Green does not mean live": a release is not done until the live site serves it); nfrs.sgit.ai and coding.sgit.ai are at v0.1.2 and v0.2.0 dated 25 August, issues-fs.sgit.ai 22 August; on 26 August, "Twenty sites in fifteen days".
- Gave the day: the site shape the talk's site copied (static pages from a build script, a gate, `.md` twins, `llms.txt`), and nfrs.sgit.ai's definition of the non-functional requirements as "the whole version control, reliability, resilience, security, backups, consistency, explainability, and documentation".
- Sources: https://newsroom.sgit.ai/newsroom/wire.json (read 2026-10-30); https://nfrs.sgit.ai/llms.txt; https://coding.sgit.ai/llms.txt; https://newsroom.sgit.ai/articles/nineteen-sites.html (2026-08-26 in the wire).

**20 September 2026: graphs.sgit.ai and fractal semantic graphs.**
- What: "a node carries no inherent meaning"; meaning is in the edges, at many altitudes; three of its documents came from Issues-FS's docs on 11 June 2026.
- Gave the day: the fractal reading of maps (section 3) and the newsroom's graph per article.
- Sources: https://graphs.sgit.ai/llms.txt (v0.6.22, 20 September 2026); https://newsroom.sgit.ai/articles/introducing-fractal-semantic-graphs.html (2026-09-20).

**24 to 30 September 2026: behaviour policies, six agents, and the talk's argument.**
- What: the first newsroom article in the wire to name a behaviour policy (24 September, a connector twin before an agent gets a connector); "Six agents, one inbox" (29 September), agents on dedicated accounts, each with a policy; and on 30 September "The ultimate insider: agents, the infrastructure that cannot hold them", the article the talk was cut from.
- Gave the day: the talk itself, and the shape of an agent with one focus and a written policy.
- Sources: https://newsroom.sgit.ai/articles/six-agents-one-inbox.html (2026-09-29); https://newsroom.sgit.ai/articles/ultimate-insider-three-collisions.html (2026-09-30).

**2 to 6 October 2026: the agent team as a recipe.**
- What: "Replicating the agentic inbox" (2 October, revised 3 October): roles that talk "in files through Email-FS lite" and "a conductor that runs every role once on a schedule with a security role first and last"; "Memory is not a spectator sport" (3 October); "The agent team as it runs" and "The mandate stack" (6 October), where the security role may send one "SECURITY HOLD" email; and sgit.ai's "Every sgit repository" guidance (written 6 October 2026): a brief published in full, a reality file, a corrections file, one version going up on every push, a gate, markdown twins and `llms.txt`.
- Gave the day: almost the whole frame. The talk's conductor wrote, on the day, that the team's shape came from "The agent team as it runs", from web-summit.sgit.ai, from newsroom.sgit.ai and from "the estate's standard" (`admin/notes/2026-10-29__first-agents-and-schedule.md`).
- Sources: https://newsroom.sgit.ai/articles/replicating-the-agentic-inbox.html (2026-10-02); https://newsroom.sgit.ai/articles/memory-is-not-a-spectator-sport.html (2026-10-03); https://newsroom.sgit.ai/articles/the-agent-team-as-it-runs.html (2026-10-06); https://newsroom.sgit.ai/articles/the-mandate-stack.html (2026-10-06); https://sgit.ai/docs/guidance/repositories.html ("first version, written 6 October 2026").

**8 to 12 October 2026: the method, written down.**
- What: "Every mistake added a rule" (8 October: map it, commoditise small chunks, rules for incidents and machines for enforcement); "A second reader the agent cannot skip" (9 October: a hook that checks a draft with a fresh model call, maker-checker); "How I work with Claude" (9 October: one session per topic, an agent is a session with a `role.md`, memory is what the session reads); "Where the vault keys live" (10 October: a registry vault run by an isolated agent); "Why I love Wardley maps" and "How the voice works" (12 October).
- Gave the day: the role files, the sub-agent reviews in every wake, the vaults manager the talk's vault keys were sealed to, and the storyteller's Wardley maps.
- Sources: the articles at https://newsroom.sgit.ai/articles/every-mistake-added-a-rule.html (2026-10-08), .../a-second-reader-the-agent-cannot-skip.html (2026-10-09), .../how-i-work-with-claude.html (2026-10-09), .../where-the-vault-keys-live.html (2026-10-10), .../why-i-love-wardley-maps.html (2026-10-12), .../how-the-voice-works.html (2026-10-12).

**16 to 24 October 2026: PKI, the rules of the game, process behaviour policies.**
- What: "Explorer coding" (16 October, Wardley's word for building to explore); pki.sgit.ai's register of people and keys (v0.2.0, 18 October); "PKI everywhere" (20 October, every message signed, an agent may make its own key); "How a memo becomes a release" (21 October); "The rules of the game" (22 October, which files an agent may change, in five zones); "Process behaviour policies" (24 October).
- Gave the day: the pinned `pki-agent.mjs` each session used to make its key; one writer per file enforced by the gate; map 2 of the talk ("explorer coding").
- Sources: https://pki.sgit.ai/llms.txt (v0.2.30, 18 October 2026); https://newsroom.sgit.ai/articles/pki-everywhere.html (2026-10-20); .../how-a-memo-becomes-a-release.html (2026-10-21); .../the-rules-of-the-game.html (2026-10-22); .../process-behaviour-policies.html (2026-10-24); .../explorer-coding.html (2026-10-16).

**24 October 2026: SHarness.**
- What: "a secure harness": Agent Behaviour Policies executed rather than read, a Process Behaviour Policy per process, hashed and enforced by the Linux kernel or a separate door. Started on the morning of 24 October 2026 "with a narrow problem in sgit"; `sharness-ai` 0.1.0 on PyPI the same day (16:27 UTC), 0.2.0 on 29 October (03:11 UTC).
- Gave the day: SHarness live in the talk (the case study lists it among "a month of innovations") and the talk's SHarness series of slides; and, through sharness.ai's version collisions of 25 October, the article that taught every site CI owns the version.
- Sources: https://newsroom.sgit.ai/articles/introducing-sharness.html (2026-10-29); https://pypi.org/pypi/sharness-ai/json; https://sharness.ai/llms.txt (v0.6.35; "design session written up with Claude, 24 October 2026").

**25 to 28 October 2026: CI owns the version everywhere, and the push becomes the authorisation.**
- What: four agents on sharness.ai pushed seven releases between 23:42 and 23:58 UTC on 25 October, three on the same tags they could see; sharness.ai moved to CI-owned versions; the PHP newsroom's six repositories on 27 October; newsroom.sgit.ai's first CI-numbered release, v0.13.116, at 23:38 UTC on 27 October. At 02:22:16 UTC on 28 October he added one sentence to the PHP newsroom's runbook: "pushing your public key to team's dev is the authorisation".
- Gave the day: both rules arrived less than two days before the talk's first commit, and both ran all day.
- Sources: https://newsroom.sgit.ai/articles/ci-owns-the-version.html (2026-10-27); https://newsroom.sgit.ai/articles/the-push-is-the-authorisation.html (2026-10-28); https://newsroom.sgit.ai/articles/agents-have-an-identity-now.html (2026-10-29).

**29 October 2026: the day.**
- What: an empty repository at 00:16 UTC; 814 commits, 210 CI releases, 162 wakes (148 ended ok), 293 notes between agents, nine agents and one editor; the conductor's hold at 18:44 (the editor's usage at 95%); v0.1.209 at 18:46; the talk at 19:00 at hack::soho, IOActive London. His own summary: "almost every innovation we have been working on this month came together in it".
- Source: https://newsroom.sgit.ai/articles/the-ultimate-insider-case-study.html (2026-10-29, his account, numbers "read from the public repository"); the talk's repository at `298be4e`.

---

## 2. The plumbing the day relied on

One entry per practice: where it came from, and where it shows in the talk's repository at `298be4e` (paths relative to its root). "Line" means the line at that commit.

### CI owns the version

- **From:** OSBot-Utils, 27 October 2023 (`e53d055`, `753ef2c`), 1,129 tags since; "Auto-tag everything" in the deck of 29 January 2025; generalised across the agent-built sites from 25 to 27 October 2026 after version races. The newsroom article: https://newsroom.sgit.ai/articles/ci-owns-the-version.html (2026-10-27).
- **In the talk:** `.github/workflows/release.yml` (line 1: "CI owns the version (https://newsroom.sgit.ai/articles/ci-owns-the-version.html)"; a guard fails the run "if any other author changed" `./version`; `dev` bumps the last number, `main` the middle one); `CLAUDE.md` ("Never write `./version` and never put a number in a commit subject"); `content/articles/introducing-this-site.md` line 49 ("This is the scheme I wrote for OSBot-Utils in 2023"). The book's own `CLAUDE.md` carries the same rule.

### The gate

- **From:** sgit.ai's "Every sgit repository" guidance (6 October 2026), section 4, "The gate": "A validator that fails the build and a release script that refuses to push until it passes"; every check listed "has each caught a real defect". The release discipline "bump, build, validate, push, verify" and "a release is not done until the live thing serves the new version" go back to "Green does not mean live" (17 August 2026 in the wire). coding.sgit.ai (25 August 2026) records the weakness: "0 linters, 0 formatters, 0 type-checkers" and four structural guards, each encoding an incident.
- **In the talk:** `admin/build/validate.py` (header: links resolve, every page has its `.md` twin and is in `llms.txt`, no script from another host, every beat has a slide, no em-dashes, a leak tripwire); `run-website-locally.sh`; the `gate` job in `.github/workflows/release.yml` ("build (pending) and gate"); `CLAUDE.md` ("Build and gate before every push").

### Markdown twins and llms.txt

- **From:** the estate standard: "On a site, a `.md` twin for every page and an `llms.txt` at the root and per section, generated from the same data as the pages" (https://sgit.ai/docs/guidance/repositories.html, 6 October 2026); every newsroom page carries "this file is generated from the same content as the page, so the two cannot drift". The reason is in "How I work with Claude" (9 October 2026): "What a session knows is what it reads", and public sites with `llms.txt` are the first part of that memory.
- **In the talk:** `admin/build/build.py` line 8 ("write a .md twin next to every page"), line 118 (`Html_To_Markdown`), line 1115 (writes `llms.txt`); `admin/build/validate.py` line 63 ("has no .md twin" fails the gate); `REALITY.md` line 10.

### Provenance and the claims register

- **From:** "Deterministic GenAI Outputs with Provenance", OWASP AppSec EU Lisbon, 28 June 2024; "The Future of News: Building Trust Through Fact Provenance", 5 February 2025; the newsroom's design line "provenance is the product" (newsroom `llms.txt`), with a provenance block on every page "enforced by the pre-release gate"; the estate rule "Every number on a page is counted, not remembered, and the page says what it does not prove" (6 October 2026); the brief kept "as written, and never edited afterwards" with a corrections file beside it. The A0 to A6 grading scale is the PHP October 2026 newsroom's fact-check desk's (talk researcher's `ROLE.md`); its origin date there is not found in public sources read for this dossier.
- **In the talk:** `team/researcher/ROLE.md` (capture and hash every source; a claims register graded A0 to A6); `evidence/sources/manifest.json` (SHA-256 per captured file); `evidence/claims/claims.json`; `evidence/METHOD.md`; `BRIEF.md`, `BRIEF-CORRECTIONS.md`, `REALITY.md`. The book's `claims/` register and "every number traced" rule are the same practice.

### The five-step wake and holds

- **From:** a conductor that runs every role on a schedule "with a security role first and last" (2 October 2026, "Replicating the agentic inbox"; 6 October, "The agent team as it runs"); maker-checker, "a second reader the agent cannot skip" (9 October 2026); the security role's single "SECURITY HOLD" email (6 October, "The mandate stack"); "Knowing when to stop" (8 October 2026). The five steps themselves were the editor's word on 29 October 2026, the day (talk `CLAUDE.md`: "Every wake runs five steps (the editor, 29 October 2026)").
- **In the talk:** `team/conductor/WAKE.md` (the five steps, with verdicts; "Stopping" lists when any member may stop); `admin/tools/wake.py` (`gate` refuses work until plan and pre-review say go); `team/conductor/reviews/` (`plan.md`, `pre_review.md`, `post_review.md`, `post_check.md`); `admin/tools/start.py` lines 13 to 14 and 59 (a `HOLD.md` makes every wake exit 3); `team/<id>/wakes/` (one record per wake); `team/conductor/HOLD.md`, committed as `867f8c2` at 18:44:13 UTC: "the editor's usage limit is at 95%; pause all actions". The case study counts 162 wakes, each "reviewed by a sub-agent before and after the work".

### Agent Behaviour Policies

- **From:** RiskMandate's Agent Behaviour Policy (mandate, grant, delta, and a barrier per capability: none, expectation, setting, boundary), published at https://abp.sgit.ai/ (v0.12.1) and https://riskmandate.ai/abp.html; first in the newsroom's wire on 24 September 2026; "The behaviour policy is the business logic" (7 October 2026); "Agent Behaviour Policies move to the Open Security Summit" (20 October 2026); "The rules of the game" (22 October 2026), which files an agent may change; executed, not read, in SHarness (24 to 29 October 2026).
- **In the talk:** every `team/<id>/policy.json` (schema `the-ultimate-insider/agent-policy/v1`, with `mandate.wanted`, `mandate.not_wanted`, `scope.writes`; the conductor's policy records the editor's agreement at about 17:40 UTC on 29 October); `admin/build/agents.py` (`check`, `overlaps`, `unowned`; its header is honest: "A scope is a setting, not a boundary: the agent can edit its own policy.json"); the slides on mandate and grant and the four barriers under `src/pages/ruv-sgit/`.

### Session keys, and the push as the authorisation

- **From:** "A directory of people and keys" (18 October 2026); pki.sgit.ai (v0.2.0, 18 October 2026, people first); "PKI everywhere" (20 October 2026); "The push is the authorisation" (02:22:16 UTC, 28 October 2026, in the PHP newsroom); "Agents have an identity now" (29 October 2026): a session makes its own key pair, publishes the public half with a fingerprint and a QR image beside its role, "and that push is the authorisation".
- **In the talk:** `team/<id>/key.json` and `key.png` for every member; `admin/tools/pki-agent.mjs` with `pki-agent.mjs.sha256` and `pki-agent.README.md` ("An unmodified copy of https://pki.sgit.ai/agents/pki-agent.mjs"); `admin/build/build.py` lines 922, 951, 959, 976 (the keys page, linking the newsroom article); `CLAUDE.md` ("the push is the authorisation. Private halves stay in `~/.sg-send/`").

### Issues-FS and Email-FS (in vaults on the day; in git in the book)

- **From:** Issues-FS (first commit 4 February 2026; Issues-FS-lite specification at https://issues-fs.sgit.ai/lite/index.html: three folders, four moves, read every folder and write only your own); Email-FS lite (2 October 2026: "talking in files through Email-FS lite"; a mailroom, an inbox and a done folder per agent, 3 October 2026); "Messaging-FS" proposed alongside them on 21 October 2026.
- **In the talk:** two public vaults, `tui-issues-public` (Issues-FS lite) and `tui-mail-public` (Email-FS lite) on dev.send.sgraph.ai (`CLAUDE.md` line 8; `REALITY.md` line 40; `team/conductor/vaults.json`); `admin/build/build.py` `build_board` (line 1042) and `build_mail` (line 1073) read them live in the visitor's browser. The book changes the carrier, not the layout: `comms/issues/` and `comms/mail/` in git, at the editor's word of 30 October 2026 (book `CLAUDE.md`).

### Vaults

- **From:** SG/Send (8 February 2026) and sgit (3 March 2026); "Seven vaults, one method" (19 August 2026 in the wire: "three vault keys submitted for publication that would have handed the world write access"); "Where the vault keys live" (10 October 2026: "a registry vault run by an isolated agent session"); "Read keys may be published; vault keys never" (6 October 2026 guidance).
- **In the talk:** `admin/tools/vault_handover.py` (seals each vault key to the vaults manager); `team/conductor/known-keys/dc-vault-registry.json`; `admin/tools/vault_check.py` (run before every vault commit; every file is public, forever); the researcher's `tui-evidence-public` vault (`team/researcher/evidence-vault.json`). The case study records the failure kept in: "a printed vault key". The book keeps the tools ported and uses no vaults (book `CLAUDE.md`, 30 October 2026).

### Type_Safe

- **From:** OSBot-Utils, Kwargs_To_Self on 3 January 2024, named Type_Safe on 1 June 2024 (`4edb92e`); coding.sgit.ai: "Type_Safe, Safe_Str and the constrained-primitive pattern come from osbot-utils"; the estate guidance: a tool or library is "Python under the Type_Safe rules with a test suite that runs against real objects".
- **In the talk:** not found. The talk's repository at `298be4e` has no reference to Type_Safe; its tools are standard-library Python (`admin/build/agents.py`: "Standard library only"). Type_Safe reached the day only through sgit, whose CLI was bootstrapped on 3 March 2026 "with Safe_* types", and which every vault command on the day ran. The book should say so rather than imply the talk's code used it.

### Tagging

The brief's word can mean two things, and the sources support both; which one he meant is for the editor to say.
- **Git tags, automatic:** "Git version control (autotagging)" and "Auto-tag everything" (deck, 29 January 2025); the release tags since 27 October 2023. **In the talk:** every release is a `vX.Y.Z` tag made by CI; `admin/build/build.py` lines 607 and 825 read the tags to build the release history.
- **Tags as vocabulary on content:** every newsroom article carries tags and the newsroom publishes a controlled vocabulary in `/articles/find.json`; "Search as navigation" (18 October 2026) builds on it; the 2025 essay "From top-down to organic evolving graphs, ontologies and taxonomies" (29 March 2025) is the earliest public statement found. **In the talk:** not found; none of the six articles in `content/articles/` has a tags field. Commit trailers (`Agent:`, `To-<id>:`) play a tagging role for routing (`team/conductor/WAKE.md`, checklist step 2).

### The newsroom's publishing flow

- **From:** every article starts as a voice memo and ends as a tagged release (https://newsroom.sgit.ai/articles/how-a-memo-becomes-a-release.html, 21 October 2026); the voice is four inputs, not a setting (https://newsroom.sgit.ai/articles/how-the-voice-works.html, 12 October 2026); "How a journalist agent publishes here" (28 October 2026: eleven steps, CI owning the version, mistakes each with the rule it produced); every page carries its provenance and says what it does not claim.
- **In the talk:** the editor's words kept verbatim in `BRIEF.md` and in `team/conductor/briefs/2026-10-29__editor/`; articles as markdown with front matter in `content/articles/`, each with "What this does not claim" (for example `introducing-this-site.md`); the team's reports on itself generated from its records (`admin/tools/night_log.py`, `admin/tools/moments.py`, `content/articles/the-night-hour-by-hour.md`, `content/articles/moments.md`); `BRIEF.md` line 11 points the first agent to "the agentic team we are using at newsroom.sgit.ai". The book's pipeline (briefs in `briefs/`, never edited; `BRIEF-CORRECTIONS.md`; chapters ending with where they came from) is the same flow.

---

## 3. Wardley maps in his work

**What a map is, to him.** "A graph with two axes of context": a value chain from a user's need down, and an evolution axis across. The axis is a choice (risk, data or governance can be one); every dot is a claim; "a map, not a measurement". What he uses them for: what is moving the needle, the right altitude, build or buy, whether a market exists, flow and attrition, where to hook, a common language, starting with the user, many maps not one, and peace ("Once a thing is on a map, placed and connected, I stop carrying it in my head"). Maps nest: "every node on a map is a map". A map is read as a story, frame by frame, with seven questions: where is the user, what is new, what does it stand on, where did the movement happen, where did we walk back, where would somebody else hook in, what is next. Source: https://newsroom.sgit.ai/articles/why-i-love-wardley-maps.html (2026-10-12).

Where he has used them, in date order:

| When | Where | How | Link |
|---|---|---|---|
| 2018 | Generation Z Developers, chapter outlines | pioneers, settlers and town planners as a career idea | https://newsroom.sgit.ai/articles/generation-z-developers-again.html (2026-10-18) |
| 2022 | Open Security Summit talk, "Why Wardley Maps changed how I think" | eleven shifts in how a problem is seen; at about the same time, a post on alternative evolution axes he could not find again (not found in public sources) | https://www.youtube.com/watch?v=6gpgnYo6M14 (date from the 12 October 2026 article) |
| 2025 | ThreatModCon 2025 | five Wardley map walkthroughs inside a threat modelling talk, "where the mapping habit and the security habit met"; now a published vault | https://sgit.ai/demos/vaults/threatmodcon-2025/index.html |
| May 2026 | LinkedIn | the SG/Send strategy as seven maps, now served from an encrypted vault | https://sgit.ai/demos/vaults/strategy-maps/index.html and https://sgit.ai/demos/strategy-maps.html |
| 6 Oct 2026 | "The mandate stack" | two maps of one agent team, from the outside and from the inside, rendered with Mermaid's `wardley-beta`, with movement arrows | https://newsroom.sgit.ai/articles/the-mandate-stack.html |
| 8 Oct 2026 | "Every mistake added a rule" | before and after: custom process in a blob on the left, then each piece made small and moved right onto files, hashes and git | https://newsroom.sgit.ai/articles/every-mistake-added-a-rule.html |
| 10 to 12 Oct 2026 | "Pay after you read", "Places of highest leverage", "Agentic cost is an engineering problem", "A Mac of the agent's own" | an afternoon as eight frames; which shoulders a feature stands on; a business plan in three frames; build or buy with a licence drawn in | linked from https://newsroom.sgit.ai/articles/why-i-love-wardley-maps.html |
| 12 Oct 2026 | "Why I love Wardley maps" | the best of them, two worked "does the market exist" cases (sgit, RiskMandate), two printable decks, and every map published as data | https://newsroom.sgit.ai/articles/why-i-love-wardley-maps.html |
| 16 Oct 2026 | "Explorer coding" | Wardley's "explorer" as a better name for vibe coding; refactor "from explorer to villager" when innovation slows | https://newsroom.sgit.ai/articles/explorer-coding.html and https://newsroom.sgit.ai/articles/explorer-to-villager-newsroom.html (2026-10-11) |
| 17 Oct 2026 | "Three decisions mapped" | each element of three agent decisions placed on a map | https://newsroom.sgit.ai/articles/three-decisions-mapped.html |
| 18 Oct 2026 | "Two years in the opposite" | maps as the source of his calm: "When you can see the board, a bad week is a move, not a verdict" | https://newsroom.sgit.ai/articles/two-years-in-the-opposite.html |
| undated | wardley-maps.sgit.ai | a research site: "Maps are claims, not pictures"; coordinates are `[visibility, evolution]`; quote every name or Mermaid fails silently; pioneers, settlers and town planners built as three literal agent teams | https://wardley-maps.sgit.ai/llms.txt (v0.1.2) |
| 29 Oct 2026 | the talk | the storyteller drew five maps with its own renderer (first pass in `df37797` at 14:19 UTC); four reached slides: beats 15 (`slides/maps/inside/`), 25 (`slides/maps/explorer/`), 54 (`slides/maps/evolution/`, the editor's beat 3e: where exploitation sits, then pioneers, settlers and town planners) and 55 (`slides/maps/next-companies/`) | talk repository at `298be4e`: `team/storyteller/maps/README.md`, `team/storyteller/tools/wardley.py`, `src/static/talk/talk.json` |

Three points the book can use from these sources, with their limits:
- **Maps for the day itself are rendered with Mermaid.** The mandate stack's maps (6 October 2026) are Mermaid `wardley-beta`, with the source in the article; wardley-maps.sgit.ai records the two silent failures (transposed coordinates, unquoted names) that an agent making them will meet. The talk's storyteller used a small Python renderer instead (`team/storyteller/tools/wardley.py`).
- **wardley-maps.sgit.ai warns against the thing the book is about to do.** "The evolution axis plausibly encodes consensus rather than objective fact. A model placing components on it is generating consensus-shaped output with no underlying evidence. Surface every placement as an explicitly contestable claim requiring human challenge." A map an agent draws for the book should say whose placement it is.
- **Licence.** Wardley mapping is CC BY-SA 4.0 and Simon Wardley's blog CC BY-SA 3.0; wardley-maps.sgit.ai quotes and links rather than adapts for that reason (https://wardley-maps.sgit.ai/llms.txt). The book should do the same with any material from that ecosystem.

---

## 4. Sources

Read on 30 October 2026 unless a different date is given.

**newsroom.sgit.ai** (each article also at the same path with `.md`)
- https://newsroom.sgit.ai/llms.txt (site v0.13.133)
- https://newsroom.sgit.ai/newsroom/wire.json
- https://newsroom.sgit.ai/articles/green-does-not-mean-live.html (2026-08-17 in the wire)
- https://newsroom.sgit.ai/articles/seven-vaults-one-method.html (2026-08-19 in the wire)
- https://newsroom.sgit.ai/articles/what-sgit-is.html (2026-08-25 in the wire)
- https://newsroom.sgit.ai/articles/nineteen-sites.html (2026-08-26 in the wire)
- https://newsroom.sgit.ai/articles/introducing-fractal-semantic-graphs.html (2026-09-20)
- https://newsroom.sgit.ai/articles/six-agents-one-inbox.html (2026-09-29)
- https://newsroom.sgit.ai/articles/ultimate-insider-three-collisions.html (2026-09-30)
- https://newsroom.sgit.ai/articles/replicating-the-agentic-inbox.html (2026-10-02, updated 2026-10-03)
- https://newsroom.sgit.ai/articles/memory-is-not-a-spectator-sport.html (2026-10-03)
- https://newsroom.sgit.ai/articles/the-agent-team-as-it-runs.html (2026-10-06)
- https://newsroom.sgit.ai/articles/the-mandate-stack.html (2026-10-06)
- https://newsroom.sgit.ai/articles/the-behaviour-policy-is-the-business-logic.html (2026-10-07)
- https://newsroom.sgit.ai/articles/every-mistake-added-a-rule.html (2026-10-08)
- https://newsroom.sgit.ai/articles/knowing-when-to-stop.html (2026-10-08)
- https://newsroom.sgit.ai/articles/how-i-work-with-claude.html (2026-10-09)
- https://newsroom.sgit.ai/articles/a-second-reader-the-agent-cannot-skip.html (2026-10-09)
- https://newsroom.sgit.ai/articles/where-the-vault-keys-live.html (2026-10-10)
- https://newsroom.sgit.ai/articles/explorer-to-villager-newsroom.html (2026-10-11)
- https://newsroom.sgit.ai/articles/not-a-straight-line.html (2026-10-12)
- https://newsroom.sgit.ai/articles/places-of-highest-leverage.html (2026-10-12)
- https://newsroom.sgit.ai/articles/why-i-love-wardley-maps.html (2026-10-12)
- https://newsroom.sgit.ai/articles/how-the-voice-works.html (2026-10-12)
- https://newsroom.sgit.ai/articles/from-send-to-sgit.html (2026-10-15)
- https://newsroom.sgit.ai/articles/explorer-coding.html (2026-10-16)
- https://newsroom.sgit.ai/articles/three-decisions-mapped.html (2026-10-17)
- https://newsroom.sgit.ai/articles/a-directory-of-people-and-keys.html (2026-10-18)
- https://newsroom.sgit.ai/articles/bringing-my-past-work-back.html (2026-10-18)
- https://newsroom.sgit.ai/articles/generation-z-developers-again.html (2026-10-18)
- https://newsroom.sgit.ai/articles/search-as-navigation.html (2026-10-18)
- https://newsroom.sgit.ai/articles/two-years-in-the-opposite.html (2026-10-18)
- https://newsroom.sgit.ai/articles/pki-everywhere.html (2026-10-20)
- https://newsroom.sgit.ai/articles/agent-behaviour-policies-move-to-the-open-security-summit.html (2026-10-20)
- https://newsroom.sgit.ai/articles/connect-your-dots-backwards.html (2026-10-21)
- https://newsroom.sgit.ai/articles/how-a-memo-becomes-a-release.html (2026-10-21)
- https://newsroom.sgit.ai/articles/messaging-fs.html (2026-10-21)
- https://newsroom.sgit.ai/articles/the-rules-of-the-game.html (2026-10-22)
- https://newsroom.sgit.ai/articles/the-sidecar-repository.html (2026-10-22)
- https://newsroom.sgit.ai/articles/process-behaviour-policies.html (2026-10-24)
- https://newsroom.sgit.ai/articles/ci-owns-the-version.html (2026-10-27)
- https://newsroom.sgit.ai/articles/what-an-agent-is.html (2026-10-27)
- https://newsroom.sgit.ai/articles/what-sgit-does-that-git-does-not.html (2026-10-27)
- https://newsroom.sgit.ai/articles/you-can-feel-good-engineering.html (2026-10-27)
- https://newsroom.sgit.ai/articles/how-a-journalist-agent-publishes-here.html (2026-10-28)
- https://newsroom.sgit.ai/articles/the-push-is-the-authorisation.html (2026-10-28)
- https://newsroom.sgit.ai/articles/agents-have-an-identity-now.html (2026-10-29)
- https://newsroom.sgit.ai/articles/introducing-sharness.html (2026-10-29)
- https://newsroom.sgit.ai/articles/the-ultimate-insider-case-study.html (2026-10-29)

**sgit.ai and its network**
- https://sgit.ai/llms.txt
- https://sgit.ai/docs/guidance/repositories.html ("first version, written 6 October 2026")
- https://issues-fs.sgit.ai/llms.txt (v0.1.2, 22 August 2026) and https://issues-fs.sgit.ai/lite/index.html
- https://pki.sgit.ai/llms.txt (v0.2.30, 18 October 2026) and https://pki.sgit.ai/agents/pki-agent.mjs
- https://graphs.sgit.ai/llms.txt (v0.6.22, 20 September 2026)
- https://abp.sgit.ai/llms.txt (v0.12.1)
- https://nfrs.sgit.ai/llms.txt (v0.1.2, 25 August 2026)
- https://coding.sgit.ai/llms.txt (v0.2.0, 25 August 2026)
- https://wardley-maps.sgit.ai/llms.txt (v0.1.2)
- https://gen-z-developers.sgit.ai/llms.txt (v0.2.45) and https://gen-z-developers.sgit.ai/v2/book/connect-the-dots-backwards.html
- https://sharness.ai/llms.txt (v0.6.35)
- https://sgit.ai/demos/vaults/strategy-maps/index.html, https://sgit.ai/demos/vaults/threatmodcon-2025/index.html (linked from the 12 October 2026 article; not opened)

**Dinis Cruz and The Cyber Boardroom**
- https://diniscruz.ai/llms.txt, https://diniscruz.ai/about/index.html, https://diniscruz.ai/building/index.html (site v0.1.1)
- https://diniscruz.ai/2024/02/22/its-2024-and-with-genai-we-can-finally-make-appsec-work.html (2024-02-22)
- https://diniscruz.ai/2024/06/28/deterministic-genai-outputs-with-provenance__owasp-appsec-lisbon__gslides.html (2024-06-28)
- https://diniscruz.ai/2025/01/29/my-journey-building_a_genai_startup__the-power-of-mvps-and-ci-pipelines__part-1.html (2025-01-29) and its PDF on files.diniscruz.ai
- https://diniscruz.ai/2025/02/05/the-future-of-news-building-trust-through-fact-provenance.html (2025-02-05)
- https://diniscruz.ai/2025/03/29/from-top-down-to-organic-evolving-graphs-ontologies-and-taxonomies.html (2025-03-29; listed, not opened)
- https://diniscruz.ai/2025/07/02/using-memory_fs-to-build-a-file-based-representation-of-the-gdpr-standard.html (2025-07-02; listed, not opened)
- https://thecyberboardroom.com (footer v0.221.0)
- https://www.linkedin.com/pulse/mvp-athena-bot-built-aws-serverless-python-flask-huggingface-cruz/ (2023-09-17)
- https://www.linkedin.com/pulse/cyber-boardroom-ltd-has-been-created-its-official-now-dinis-cruz-oaj8e (2024-04-08)
- https://www.linkedin.com/pulse/cyber-boardroom-why-how-what-v04-first-mvp-dinis-cruz-pbfge/ (2024-07-15)
- https://www.linkedin.com/pulse/introducing-community-edition-cyber-boardroom-dinis-cruz-xsope/ (2024-07-30)
- https://www.youtube.com/watch?v=6gpgnYo6M14 (2022, per the 12 October 2026 article; not opened)

**Repositories and packages**
- https://github.com/owasp-sbot/OSBot-Utils (commits `885128d`, `e53d055`, `753ef2c`, `0df0830`, `c04be1e`, `6d14889`, `4edb92e`, `d52dc70`, `be1aaba`, `9c8503d`)
- https://github.com/owasp-sbot/Memory-FS (`de32536`, `34d99ce`)
- https://github.com/owasp-sbot/Issues-FS (`21e1f27`)
- https://github.com/SGit-AI/SGit-AI__CLI (`1b01902`, `ae9f85e`)
- https://github.com/the-cyber-boardroom/myfeeds_ai (`02c6dbb`)
- https://github.com/the-cyber-boardroom/cbr-investment (first commit 2025-01-30)
- Not public (a clone asks for credentials): github.com/the-cyber-boardroom/cbr-website-beta, github.com/the-cyber-boardroom/cbr-athena
- PyPI JSON for osbot-utils, osbot-fast-api, osbot-llms, cbr-website-beta, cbr-athena, myfeeds-ai, mgraph-db, memory-fs, issues-fs, issues-fs-cli, sgit-ai, sharness-ai (https://pypi.org/pypi/<name>/json)

**The talk's repository, at `298be4e`** (read only; https://github.com/SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider)
- `CLAUDE.md`, `BRIEF.md`, `BRIEF-CORRECTIONS.md`, `REALITY.md`, `.github/workflows/release.yml`
- `admin/build/build.py`, `validate.py`, `agents.py`, `lock.py`; `admin/tools/start.py`, `wake.py`, `banner.py`, `vault_check.py`, `vault_handover.py`, `pki-agent.mjs` and its README
- `admin/notes/2026-10-29__first-agents-and-schedule.md`
- `team/conductor/WAKE.md`, `HOLD.md` (`867f8c2`), `policy.json`, `reviews/`, `known-keys/`, `vaults.json`
- `team/researcher/ROLE.md`, `evidence/` (`METHOD.md`, `sources/manifest.json`, `claims/claims.json`)
- `team/storyteller/maps/README.md`, `team/storyteller/tools/wardley.py`, `src/static/talk/talk.json`, `src/static/talk/slides/maps/`
- `content/articles/introducing-this-site.md`, `the-night-hour-by-hour.md`, `moments.md`, `running-this-agent-team.md`
