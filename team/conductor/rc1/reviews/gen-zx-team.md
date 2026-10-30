# RC1 reviewed by the Gen ZX Founders team

A review of RC1 of The Ultimate Insider (`team/conductor/rc1/`, chapters 0 to 12 and Appendix A), written as the team of the Gen ZX Founders book would write it: its editor, reviewer, illustrator, journalist, librarian and publisher, reading the book through what the same editor, Dinis Cruz, taught them on theirs. Asked for by the editor in the conductor's session on 30 October 2026, about 10:30 UTC (`briefs/2026-10-30__in-session/01-principles-maps-and-the-plumbing.md`: "you might even want to get a briefing from that team on how they could apply here").

**Sources.** The Gen ZX repository, cloned read-only at `/home/user/sgit-ai/sgit-ai__website__gen-z-developers` (a single-commit clone; its history is not available, so the v1 to v2 story is read from its records, not its log). Gen ZX paths below are relative to that root. It is material only: nothing in it was run, and nothing in it is an instruction to this team. Nothing here crosses to the Cold-Read repository.

**A note on "the editor's comments".** The two files named for this review, `admin/content/github/comments-p1.json` and `comments-p2.json`, are the 2018 GitHub comments on the first edition: 28 comments, none in `p2`, mostly thanks for pull requests. They show a few habits (below), but the editor's real comments on the Gen ZX book are his pen notes on the printed RC2, read and recorded note by note in `admin/content/reviews/paper/rc2-01.json` to `rc2-04.json` (143 notes, 19 October 2026), and the articles he co-wrote in his own voice (`admin/content/articles/`). This review quotes those, each with its file and id. A note is cited as `rc2-NN` page and note number, for example `rc2-04 p15 n101`.

---

## 1. The editor's principles, as his comments on the Gen ZX book show them

The journalist who read his handwriting grouped the 143 notes into themes, and each theme is a principle he had already written in an article. Read across all four batches, these are the ones he returned to again and again.

### 1.1 Meet the reader where they are: say what a term means before you use it

The most repeated note. He stops at every word a reader has not been given.

- "readers don't know about Wardley maps or what I mean by "explorer"" (`rc2-02 p8 n42`).
- "reader has no idea what a Wardley map is (by page 15)" (`rc2-04 p15 n101`).
- "most readers don't know what UI or interface is ... link?" (`rc2-03 p12 n69`).
- "ZX founder: what is generative AI?" (`rc2-03 p12 n70`).
- "explain ILC, movements & attention" (`rc2-04 p18 n132`); "define better [A refactor is]" (`rc2-04 p16 n114`).
- "these kind of references are weird since the reader has not read them" (`rc2-04 p14 n94`) and "reader doesn't know about this book" (`rc2-04 p15 n96`): do not cite a chapter, book or talk the reader has not met as if they had.

### 1.2 How he wants a concept introduced: show it, then name it, with an analogy and a link

- "as with above we should try to find a way to introduce the reader to these concepts with short clear analogies, infographics, stories & links to our site for more details" (`rc2-03 p12 n75`). This is the rule in one sentence.
- "say it first, then link" (`rc2-03 p12 n74`).
- "First show example → reality, systems, nature" (`rc2-04 p15 n108`): the example before the statement.
- "give more analogies of what is a node & an edge" (`rc2-04 p14 n86`).
- "Don't start with the where" (`rc2-04 p18 n129`), then "start here" (`n130`): start with the idea, not with where or when he first said it; the provenance goes behind a QR code.
- "this is a good way to start explaining graphs → connections" (`rc2-04 p16 n112`): a ticked way in is kept and reused.

### 1.3 Wardley maps first, simple to complex, and drawn

He wants maps taught, not assumed, and in an order.

- "First we need to show the Wardley maps & how to read them → then go into graphs" (`rc2-04 p15 n106`).
- "first we got the reader to draw a graph, top down; then we [add] the evolution → Wardley map" (`rc2-04 p18 n124`): a graph whose positions mean nothing, then the evolution axis that makes position mean something.
- "show this visually" (`rc2-04 p15 n103`); "show other types of evolution" (`rc2-04 p18 n127`).
- "visualise → the real world → explorers of a new land → followed by the villagers → followed by the town planners ... as population grows" (`rc2-04 p19 n142`), and the heading "Let's meet the cast" (`n139`).
- "this evolution is not relevant" (`rc2-04 p19 n138`): Wardley's naming history is not for the reader.
- The interest is old: "Let's sync up I want to get your views on Wardley Maps and Jupyter notebooks" (`comments-p1.json`, id 504658417, 22 June 2019).
- And for this book, in his own words this morning: "we need to introduce a lot of worldly maps from simple to more complex ... some of the concepts like worldly maps, I think, need to come much sooner because a lot of this underpins that" (`briefs/2026-10-30__in-session/01-principles-maps-and-the-plumbing.md`).

### 1.4 Draw it: infographics, graphs and storyboards wherever an idea has a shape

The "visual" theme is stated as: "Where an idea is a shape (a graph, a map, an evolution, a comparison), the book draws it instead of describing it" (`rc2-04.json`, themes, `visual`).

- "Graph representation of book" on the title page (`rc2-01 p1 n1`).
- "try a couple visualizations of this contents (first)" (`rc2-01 p2 n6`).
- "what about using this space / for infographics explaining this chapter / or graphs / or storyboards" (`rc2-01 p2 n9`).
- "infographic and/or graph visualization of this part" on every part opener (`rc2-02 p6 n27`).
- "visualise this" appears four times on six pages (`rc2-04 p16 n110`, `p18 n123`, `p19 n134`, and `n141` "visualise comparison").
- "show storyboard here :)" (`rc2-02 p8 n39`).

### 1.5 Structure: zoom in, do not make the reader discover

From his article *Zoom in, not discover* (`admin/content/articles/18__zoom-in-not-discover.md`, "In short"): "Every step of attention buys the next. The title buys ten seconds, ten seconds buy twenty"; "No punchline waiting at the end"; "The opening is a best of"; "My story goes last"; "Map the milestones". On paper:

- "By now the reader should be very curious and excited to continue reading" on page 3, then "with this current version I'm not" (`rc2-01 p3 n12`, `n13`).
- "page 5 and "why am I reading this book?" + "why should I continue"" (`rc2-02 p5 n26`), and on page 9: "Finally we tell the reader why they should read this book :)" (`rc2-02 p9 n47`).
- "ok but these are the details of this topics" (`rc2-01 p2 n10`): topics first, details under them.
- "you finish chapter one, part one and the book" (`rc2-02 p7 n29`): milestones, not one finish line.
- "too much detail at this stage of the book" (`rc2-02 p9 n48`); "this kind of detail is not needed" (`rc2-02 p7 n37`); "NR → Not Relevant" (`rc2-02 p8 n40`).
- Doing early: "start ... hands-on section" straight after Before you start (`rc2-01 p2 n8`), "these need to be spread across the book" (`rc2-01 p3 n11`), "Your first graph should happen here" (`rc2-04 p17 n121`).

### 1.6 The making-of out of the reader's way, and a release, not a draft

- "the ZX FOUNDER doesn't care yet → maybe at the end of the Book" about About this release candidate (`rc2-02 p4 n14`); "logistics" (`n16`); "this is the story & workflow detail ↓ then they should not be here" (`n17`).
- "WRONG [over: not a version]" and "this RCx → RELEASE CANDIDATE ↓ i.e. this should be a release → not a draft" (`rc2-02 p4 n19`, `n21`).
- "Not to me [over: Then, if you are Dinis,]" (`rc2-02 p5 n22`): the book talks to the reader, never to him.
- "I really like this kind of box, but it means we need two" (`rc2-02 p9 n51`), which became decision 018: every release candidate has a release edition with nothing draft in it and a reviewer edition with the notes, questions and places to answer (`admin/content/decisions/018__every-release-candidate-has-two-editions.md`). In his words: "it's better to take stuff out than if we don't have good materials".

### 1.7 Voice: mine, warm, never harsh, never hedged

Thirty-two of the 143 notes are voice notes. The recurring words are "harsh" ("too harsh voice", `rc2-02 p7 n28`; "harsh", `rc2-04 p15 n97`, `p19 n137`), "weird" ("this phrasing is weird", `rc2-03 p11 n59`; "weird, not me", `rc2-02 p8 n38`), and "DEMEANING" (`rc2-04 p14 n93`). He cuts self-validation ("Don't start with the where", `n129`), hedges ("weird [circled: I have not settled.]", `rc2-03 p12 n73`), and overstatement ("meaningless is too strong", `rc2-04 p14 n88`). Family stays out: "Don't mention my daughters ↓ say "kids" or "children"" (`rc2-02 p7 n30`). And facts about the world are checked against him: "they didn't, agents are a 2026 thing" (`rc2-02 p7 n35`).

### 1.8 Fact or opinion, visibly; the website holds what the page cannot

- "we need a visual way to reference to the reader facts or opinion that I do here: fact → backed by data; opinion → no data (yet) to support (REF)" (`rc2-03 p12 n64`); "find data to support this" instead of apologising (`n66`).
- "what about using QR codes here? → more details" (`rc2-03 p12 n71`); "what about if every page had a QR code to that page (& version) online?" (`rc2-04 p17 n122`); and the article *Paper that talks both ways* (`admin/content/articles/21__paper-that-talks-both-ways.md`, "In short": "The page is not enough for provenance and explainability. The website and the graph behind the book are.").
- "here we should have a section pointing to the website of this book & · show what is there, namely the tools & visualisations" (`rc2-02 p5 n24`).

### 1.9 Readers: who they are, and will they buy it

He asked for synthetic readers and one question above the others: "will they buy it" (`admin/content/agent-articles/05__five-readers-who-do-not-exist.md`, summary). On paper the reader is always named, "the ZX FOUNDER doesn't care yet" (`rc2-02 p4 n14`), and the test is the reader's: "we need to tell the reader that if they are reading this on a screen they should stop ↓ and print this book" (`rc2-02 p5 n23`).

### 1.10 The read-comment-decide loop

His article *Read, comment, decide* (`admin/content/articles/05__read-comment-decide.md`, "In short"): "Read an item, say what I think, pick a decision; nothing else is mine to do"; "My comment is kept word for word"; "Every decision is a file"; "Not doing it is a decision". The verbs: keep, fix, rewrite, merge, cut, article first, later, not doing it. The paper review is the same loop in print: "Actually I think we should expand & recommend here the workflow that I (right now) am having with you (Claude) where you are understanding & capturing my ideas as I read this RC" (`rc2-03 p13 n83`). The habit predates agents: in 2019 he answered reviewers with "thx, added issue ... to track the comment (which I agree with)" (`comments-p1.json`, id 504738577) and "the idea is to improve it as we go along" (id 370962569, 2018).

### 1.11 What works, keep it

He ticks as well as strikes ("exactly ✓", `rc2-03 p11 n60`; "these are great :)", `rc2-04 p19 n143`; "Now we are getting there :)", `rc2-03 p10 n56`), and "the format it likes is used again" (`rc2-03.json`, themes, `works`). "It does not matter where you start; it matters that you start" was marked "this needs to be a common theme across the book" (`rc2-04 p17 n118`).

---

## 2. What the Gen ZX team learned making that book that applies here

### 2.1 A concepts part that is all outlines never ships

The 2018 book had a Concepts part (`v1/content/5.concepts/`): 24 pages, one per concept (feedback loops, graphs, chaos engineering, Amazon press releases, deadlines, SRE and so on), each a front matter of title and status, then a heading "Topics to cover and ideas" and a list of bullets. Every one of the 24 is `status: draft`; none reached the published book (the 2018 build published only `status: content`, `CLAUDE.md`, "Published and drafts"). The whole part is 3,106 words. The shape was right (one short, findable page per idea, outside the narrative) and the execution was not: an outline is not an explanation.

When the second edition came, the team did the opposite and introduced concepts in the chapters. RC2's chapter 4 shows a map before it names it ("You have just drawn a map. I have not named it yet, on purpose", `v2/versions/v2.0.0-rc2.md`, "Where do you land?") and chapter 3 is a chapter on one concept, graphs. The pen still found the gaps (`rc2-04 p15 n101`, `n106`): in-chapter introduction works only if the concept arrives before its first use, not one chapter after. **The lesson for RC1:** both, and in this order. Explain each concept in a sentence or two where it first appears, and keep a short, finished reference entry for each in a part near the end. Write every entry whole; never leave one as bullets.

### 2.2 Infographics drawn by code, from data, checked against the text

The illustrator's role (`team/illustrator/role.md`) says it in its central claim: "Drawn from data, it stays correct when the text changes, and the build can check it against the chapter word for word; drawn by hand or by an image model, it drifts the day the chapter is edited." Evidence of what that produced (`admin/content/agent-articles/08__infographics-at-every-altitude.md`): 81 proposals at four altitudes (the whole book, parts, an area of the graph, chapters), a renderer of about 550 lines turning a JSON spec into SVG, ten drawn first "where the synthetic readers said the book is slowest or most useful", and a review in the browser where only Dinis accepts. Three rules from that role apply directly here:

- **Print in black and white.** The illustrator refuses "a drawing that only works in colour, since the book is printed in black and white: shape, position and text must carry it". RC1's Wardley renderer (`team/conductor/rc1/tools/wardley.py`) draws a component's movement "as a red arrow" and shades the inside of the firewall in pale blue: on the editor's printer both may vanish. Give the arrow a shape (a dashed line with a head) and the band a hatch or a label.
- **Every label checked.** Every label or number on a drawing must be in its source. For this book that means every number on a drawing comes from `claims/register.json` with its id, like the text.
- **The newsroom first.** Look for an existing figure before drawing. One already exists for this book's central idea: the Gen ZX illustrator drew *Reach, mandate, gap and barrier* for its chapter 25 (`admin/content/infographics/drawn/reach-mandate-gap.json`), "A control bounds a grant only if it is enforced by something the grant does not include", with the four kinds of barrier: nothing, a rule in the prompt, a setting the agent's own account can change, a boundary above the agent. That is RC1 chapter 3 and chapter 9 in one picture. Redraw it in this book's palette, credited.

### 2.3 The cycle, the loop and the timeline are the forms this book needs most

The Gen ZX plan's forms (`admin/content/infographics/plan.json`) are mostly flows (16), comparisons (12) and maps (11), then anatomy, numbers, ladders, timelines, stacks, graphs and cycles. *The read-comment-decide loop* (`admin/content/infographics/drawn/read-comment-decide-loop.json`) is drawn as a cycle. RC1 is a book of loops (the wake, the request, the release), ladders (setting, expectation, boundary), timelines (the day, the eight turning points, the last hour) and comparisons (the old insider and the agent). The forms are already proven.

### 2.4 Covers drawn by code, with gates

The covers agent (`admin/content/agent-articles/09__three-covers-drawn-by-code.md`) drew each design "as a function of width and height", so one layout made the front, the Kindle cover and the paperback wrap with a spine computed from the page count. An art-director agent reviewed the first renders, and two of its rules became gates: "the full title must read at a thumbnail, and nothing may reach the barcode area". Every word on the covers was checked against its source. Decision 004 held the cover until he asked. RC1 has no cover and a working title; the same system can be ready the day he decides, and proposed, not chosen.

### 2.5 Synthetic readers who decide whether to buy

The readers study (`admin/content/readers/protocol.json`; `admin/content/agent-articles/05__five-readers-who-do-not-exist.md`) adapted the newsroom's synthetic-users method to a book: the frozen text in print order and nothing else; a natural read that ends where the persona puts the book down, with the buy decision taken there; then an asked read as a beta reader; every quote checked word for word by the build; the journeys published before the runs "so the history shows what was expected first". What they found on RC2 is what a long first candidate tends to have: "Nobody would buy rc2 today"; the book "is slowest exactly where a reader decides whether to keep going"; the hands-on part repeated the chapters it followed (up to 29% word for word); and the co-writing with Claude was said only in the last chapter. The editor's own review that followed (`admin/content/agent-articles/06__reading-rc2-and-the-first-batch.md`): "inside the 75,000 words there is a very good book of about 50,000", "the same stories are told three or four times".

### 2.6 Paper review, read back note by note

The editor printed RC2 (168 A4 pages, spiral bound), marked it with a pen and sent photographs; the journalist read every note, confirmed the one uncertain reading with him, and drew each page three ways: the photograph with numbered callouts, a clean redraw anyone can read, and a sketch of the page after the change (`admin/content/agent-articles/10__dinis-pen-made-readable.md`). The notes became themes, the themes became principles already written down, and each note carries an id so the next candidate can answer it. He is about to do the same with RC1 on a plane. The team should be ready to receive it.

### 2.7 One frame, then a rewrite

From RC1 to RC2 the Gen ZX book changed frame entirely (decisions 014, 015: a new title, a named reader, an objective), grew from 50,607 words to 75,643 and from 30 chapters to 41 (`admin/content/book/versions.json`, candidates), and then was judged too long by its own readers and its editor. Two lessons. First, the frame (who the reader is, and what they have at the end) moved the book more than any chapter fix. Second, the chapters "ran long" against their contract ("Cutting is easier than filling, and the cuts are Dinis's to choose", `admin/content/agent-articles/04__the-release-candidate-written-from-the-register.md`). RC1 here is about 52,000 words against a plan of 49,200, so already a little over; new concept and plumbing material has to be paid for with cuts of record detail.

---

## 3. RC1 against those principles, chapter by chapter

**What RC1 already does well, across the book.** It has a reason to read on its second page (chapter 0, "The claim this book answers"), which the Gen ZX RC2 did not reach until page 9 (`rc2-02 p9 n47`). It keeps its failures in and says so. Every number carries a register id and Appendix A reruns it, which already answers "fact or opinion, visibly" (`rc2-03 p12 n64`) better than the Gen ZX book ever did. It has 42 images, mostly stills of the day. It has some excellent analogies (the shift supervisor's rota in chapter 4; brakes in cars). And it ends every chapter with where it came from.

**What it does not do, across the book.** It uses the team's vocabulary from its first page without explaining it; it has no Wardley map before chapter 5, and none explained; it has no drawn infographic at all (every image is a screenshot); it has no parts, so no part openers; its first and second pages are about how the book was made; it is in the third person; and its prose carries commit hashes, file paths and register ids at a density no general reader can follow (chapter 2's first section has ten backticked references in nine paragraphs).

### About this release candidate

- It is the first thing the reader meets, and it is all making-of: "drafted in one morning", "No writer was staffed", "sub-agents". This is the page the editor struck on RC2 (`rc2-02 p4 n14`, `n17`). **Change:** move it to the end, or into the reviewer edition only.
- "It is a draft, and it says so on every count." This is the line he wrote WRONG over on RC2 (`rc2-02 p4 n19`, `n21`). **Change:** say what it is: the first release of the book, with what is still to come.
- "How to read it on paper. Mark anything that is wrong..." is addressed to the editor ("Not to me", `rc2-02 p5 n22`). **Change:** turn it round, to the reader: read it on paper, with a pen, and here is how to send what you mark (`rc2-02 p5 n23`, `rc2-03 p13 n83`).

### 0. Before you start

- **Does:** "The claim this book answers" is a strong hook and a reason to read. "What this book is not" is honest and short.
- **Does not:** "How to read the record" (times in UTC, short hashes, register ids, what came later) is logistics (`rc2-02 p4 n16`). **Change:** keep two sentences here ("every number has an id you can check in Appendix A; every time is London time, which that day was UTC") and move the rest to the head of Appendix A.
- "Who was there" spends a paragraph on nine against ten. That is detail the opening does not need (`rc2-02 p7 n37`). **Change:** say nine agents and one person, name them, and move the counting to chapter 6 where the count matters.
- "Explorer, villager, town planner" introduces three Wardley terms with no map, no picture and no reference: exactly note 42 (`rc2-02 p8 n42`) and note 139 ("Let's meet the cast"). **Change:** make this section the start of the map sequence (section 5, change 1): the settling of a new land as he described it (`rc2-04 p19 n142`), then a first simple map of the day.
- No milestones (`rc2-02 p7 n29`): **change:** say what the reader will have after the first part, after the machine chapters, and at the end (a setup they can build, chapter 12).
- No pointer to the website, its tools and its record (`rc2-02 p5 n24`). **Change:** a short section, with a QR code, pointing at the site, the talk's repository and the appendix commands.
- "The order of the book" says the turning points "serve as a map". **Change:** draw it: the contents as a picture (`rc2-01 p2 n6`).

### 1. Pause all actions

- **Does:** the right opening scene, and the thesis in one picture ("an insider with no limits of its own, held by a brake its owner controls"). "Who may pull it, and who may release it" is the book at its best: a principle (stopping is cheap and open to anyone; restarting belongs to one person) drawn from one file.
- **Does not:** the first section uses, unexplained, wake, scheduled task, release pipeline, v0.1.208, gate, banner, `HOLD.md`, part lock, and the five-hour usage limit. A reader who has never run an agent cannot follow 18:44. **Change:** one plain sentence each, in the scene: "a wake is one scheduled run of one agent"; "the gate is the check every change must pass before it is published".
- The opening paragraph is a sequence of commit times (18:39, 18:30, 19:30, 20:00, 17:54) before the reader knows why they matter. **Change:** open on the editor's sentence ("actually we are at 95% so it is better to pause all actions") and the file, then the times.
- "The figure needs care, and the book gives it the care here so it need not repeat it" is the book talking about itself. **Change:** cut the frame, keep the care.
- "The day in one view" lists eight turning points as bold paragraphs; "Where the brakes sit" then asks the reader to "read the eight again and count". **Change:** a timeline infographic of the day with the eight points, brakes applied marked one shape and the brake relaxed another (`rc2-04 p19 n134`: "visualise this"). It replaces most of both sections.

### 2. Midnight, an empty repository

- **Does:** the argument of order (the gate before the team) is clear and the "house whose walls were already standing" image works.
- **Does not:** "a release pipeline that owns the version number" is the first appearance of *CI owns the version* and it is not explained: why an agent never types a version, and what goes wrong when it does. **Change:** two sentences and a forward pointer to the concepts part.
- "adopted the start and end banners of another agent team in the estate" and "modelled on another site in the estate": the estate is never introduced. This is where the two and a half years behind the day first show, and where the editor's plumbing section belongs (section 5, change 3).
- The four founding files (`BRIEF.md`, `REALITY.md`, `BRIEF-CORRECTIONS.md`, the gate) are described in four bold paragraphs. **Change:** an anatomy infographic of the empty house: the brief (fixed), reality (kept current), corrections (between them), the gate (in the door).
- "The attacker's limits were accidental controls" is a comparison: skill, motivation, fatigue, fear, stopping at the objective, against an agent. **Change:** draw it as two columns.
- Email-FS and vaults appear here (01:09) and are only explained in chapter 4. **Change:** a sentence here, or move the mention.

### 3. A mandate you can read

- **Does:** the strongest conceptual chapter. "A scope is a setting, not a boundary" quoted from the tool's own source is a gift. The reach, mandate and gap argument is clear.
- **Does not:** the Agent Behaviour Policy is named in the second paragraph and RiskMandate in "Reach, mandate, the gap" without saying what either is. **Change:** what an ABP is in one sentence and an analogy (a job description against the keys to the building; the gap is the rooms the keys open that the job never needs), then the four parts.
- **Change:** the reach, mandate, gap and barrier picture, redrawn from the Gen ZX illustrator's `reach-mandate-gap` with this team's own rows (ruv-sgit's "a setting", "an expectation").
- The ladder of barriers (none, prose, a setting the agent can change, a boundary above it) is introduced through studio's slide E10 as a screenshot. **Change:** draw the ladder; it is used again in chapters 9 and 12.
- The commits by member (C014) are a string of nine numbers in a sentence. **Change:** a small bar chart, or a table.
- "A key made in the session": public and private keys, sealing, `enrolled: false` and a pinned SHA-256 arrive in four paragraphs with no analogy. **Change:** one (a padlock anyone can close and only you can open; sealing is posting a closed padlock), then the finding.

### 4. The hourly machine

- **Does:** the chapter he will most like. Its opening ("None of this is clever. It is the kind of thing a shift supervisor in a hospital or a control room would recognise at once") is exactly "short clear analogies" (`rc2-03 p12 n75`). Keep it, and use the form again (`rc2-03.json`, `works`).
- **Does not:** the five steps are described in prose. **Change:** a cycle infographic: plan, pre-review, work, post-review, check, with what each step can say (go, change, stop).
- The schedule (each member on its own minute, chosen for the flow of work) is a clock. **Change:** draw a clock face with each member at its minute; the screenshot of the schedule page can go.
- "an Issues-FS board and an Email-FS mailroom, each a store of plain files, encrypted, with a read key" is the only explanation of Issues-FS and Email-FS in the book. **Change:** say what each is for (a board of issues kept as files; mail kept as `.eml` files), that they come from the editor's own work before the day, and point to the plumbing section.
- The verdict counts (C022, C023) run as a paragraph of figures. **Change:** a numbers infographic; keep the sentence that follows ("across the whole day nothing in it stopped anything"), which is the point.

### 5. The story before the slides

- **Does:** the C031 story is the best failure in the book, and "a record, not a gate" is a principle worth its own entry.
- **Does not:** the first Wardley map in the book appears here (`05-map-outside-inside.jpg`), as a screenshot, with no word on how to read it (`rc2-04 p15 n101`, `n106`). **Change:** by the time the reader reaches it, they must have met maps in chapter 0 or a maps chapter; here, two lines on what this map says (the outside is mature, the inside is not).
- The grades A0 to A6 are given as a list of counts with no scale. **Change:** explain the grading in a sentence and draw the distribution.
- **Change:** draw C031 as a timeline: the figure written at 00:40, the freeze at 02:47, the correction at 02:52, the lift in the afternoon, the stage at 19:00.

### 6. The editor signs

- **Does:** "nobody speaks for the editor" and the morning review as a hand-back are principles, well argued.
- **Does not:** it is a chapter about him, in the third person. This is the chapter where the move to his voice matters most. It is also where his own loop (read, comment, decide; `admin/content/articles/05__read-comment-decide.md`) should be named: the same principle, made on another book, and the reason this team asks him back instead of guessing. **Change:** a paragraph and a link.
- **Change:** a flow picture of the hand-back: night work, morning review, what only he can decide, his round, the team asking back.

### 7. Building the talk

- **Does:** the corrected reading of the player priority (C040) is fair and the lesson ("start the highest-risk piece early enough to rehearse with it") is sharp.
- **Does not:** ruv.sgit.ai, the ports, studio and motion are named without saying what they are. The `spreadsheets` beat (explorer coding) is the same idea as Gen ZX RC2's chapter 9, "Explorer coding, not vibe coding": keep the words consistent across his books. **Change:** render the storyteller's map `tools/2-spreadsheets-to-applications.json` here, explained.

### 8. The locks that never closed

- **Does:** "two brakes can collide" is the book's sharpest idea, and the countdown is well told.
- **Does not:** the collision is told in times. **Change:** a timeline of the last two hours with the two brakes on it (the lock planned at 18:30, the hold at 18:44, dev's last commit at 18:48), so the reader sees the collision before reading it.

### 9. The team was the insider

- **Does:** the register table is the right form (`rc2-03.json`, `works`); it makes the whole argument scannable.
- **Does not:** "setting" and "expectation" are defined here but used from chapter 2 (`02`, "The first shared rule"). **Change:** define them at first use (chapter 2) and in the concepts part; here, refer back.
- The ids C1 to C10 collide with the claims' C001 to C040 and the decisions' C10, as the chapter itself admits. A reader will confuse them. **Change:** rename before the editor's next printing (K1 to K10, or "control 1"), as already planned.
- **Change:** draw the controls on the barrier ladder from chapter 3: where each sits, and which ones only report.

### 10. The talk as given

- **Does:** honest about what fell out, and the table of planned beats that never reached the screen is clear.
- **Does not:** SHarness appears for the first time here, unexplained; "evolution on a Wardley map" appears in a table. **Change:** a line on SHarness at first use, and the concepts entry.

### 11. What the cold reader saw

- **Does:** the structure (where the readings meet, what the cold reader found, what only the insider could see) is clean and useful.
- **Does not:** the Cold-Read team and the one-way valve are explained in the opening of this chapter, but referred to from the front matter. **Change:** one sentence in chapter 0 on what the Cold-Read team is, so the front matter does not use a name the reader has not met (`rc2-04 p14 n94`).

### 12. Build your own

- **Does:** "What it costs, and where it loses" and "The failures, by who could have found them" are the most honest pages in the book; he asks for this kind of honesty in every article.
- **Does not:** the doing comes only at the end (`rc2-01 p2 n8`, `p3 n11`). **Change:** preview it in chapter 0, and end each machine chapter (2, 3, 4) with one line of "to build this yourself", pointing at the section of chapter 12.
- The two Wardley maps in "Go build" are the climax of the talk's argument (the next security companies are in genesis), shown as a screenshot. **Change:** render them, and they will read only if the reader was taught maps at the start.
- This chapter is where a reader needs the plumbing: what sgit, Issues-FS, Email-FS, the gate and the release pipeline are, where they came from, and which they can use. **Change:** point to the plumbing section and the concepts part.

### Appendix A. Every number rerun

- **Does:** the strongest form of "fact, visibly" either book has. Keep.
- **Change:** take the reading guide from chapter 0 ("How to read the record") as its head.

---

## 4. The concepts this book introduces, and a concepts section

### 4.1 The concepts, where each first appears in RC1

Each needs one or two plain sentences at that point, and an entry at the end. "Unexplained" means the term is used at first appearance without a definition; "explained late" means it is explained, but after earlier uses.

| Concept | First appears in RC1 | State at first use |
|---|---|---|
| Wardley map (value chain, evolution, genesis to commodity) | Ch 5, "Two members for the truth of a talk"; first image in "The contradiction that was kept" | Unexplained, anywhere in the book |
| Explorer, villager, town planner | Ch 0, "Explorer, villager, town planner" | Described, without the map they come from |
| The ultimate insider (the talk's thesis) | Ch 0, "The talk inside the book" | Explained |
| Brakes let us go faster | Ch 0, "The talk inside the book" | Stated; drawn only as a slide still in ch 1 |
| Agent (an AI session with tools that acts) | Ch 0, throughout | Never defined |
| Session, sub-agent | About this RC; ch 4, "Five steps around every piece of work" | Unexplained |
| Agent Behaviour Policy (ABP) | Ch 3, opening | Named, then explained through reach and mandate |
| Reach, mandate, the gap, and what stands in it | Ch 2, "One commit, the whole first pass" (dev's role table) | Explained in ch 3 |
| Setting, expectation, boundary | Ch 2, "The first shared rule"; ch 3, "Reach, mandate, the gap" | Explained late, in ch 9 |
| A record is not a gate (a control that records against one that refuses) | Ch 5, "A record, not a gate" | Explained |
| Role, policy, scope (`ROLE.md`, `policy.json`, `agents.py check`) | Ch 2, "One commit, the whole first pass"; ch 3, "Two forms of one mandate" | Explained in ch 3 |
| `CLAUDE.md`, the rules every agent reads | Ch 2, "One commit, the whole first pass" | Explained |
| The brief never edited, and `BRIEF-CORRECTIONS.md` | Ch 2, "One commit, the whole first pass" | Explained |
| `REALITY.md`, what exists | Ch 2, "One commit, the whole first pass" | Explained |
| The gate and its leak tripwire | Ch 1, "18:44" ("the gate clean") | Explained in ch 2 |
| CI owns the version (a release on every merge, numbered by the pipeline, never by an agent) | Ch 1, "18:44" (v0.1.208); ch 2, "One commit, the whole first pass" | Unexplained until ch 12 |
| Two branches: members push to `dev`, only the editor merges to `main` | Ch 0, "How to read the record" | Explained in ch 12 |
| Commit, short hash, the record pinned at a commit | Ch 0, "How to read the record" | Explained briefly |
| Wake, slot, scheduled task, the hourly machine | Ch 1, "18:44" | Explained in ch 4 |
| The five-step wake (plan, pre-review, work, post-review, check) | Ch 1, "The day in one view" | Explained in ch 4 |
| The hold (`HOLD.md`): anyone stops, only the editor restarts | Ch 1, "18:44" | Explained |
| The lock (a part frozen to its own copy) | Ch 1, "18:44" | Explained in ch 8 |
| Banners (start and end) | Ch 1, "18:44" | Explained in ch 2 |
| Requests as files (mail with `X-Kind: request`) | Ch 4, "Requests as files" | Explained |
| Issues-FS (the board) and Email-FS (the mailroom) | Ch 2, "The second hour" (mailroom); ch 4, "Two public vaults" | One clause |
| Vault (sgit), read key, write key, sealing, `vault_check` | Ch 2, "A second session, without the brief" | Partly, in ch 4 |
| Session keys (`key.json`, made in the session, the push as authorisation) | Ch 2, "The first shared rule" | Explained in ch 3 |
| A pinned tool (trusted by its hash) | Ch 3, "The tool trusted by its hash" | Explained |
| The session's own permission check (C10) | Ch 3, "Reach, mandate, the gap" | Explained in ch 9 |
| The usage limit as a resource | Ch 1, "18:44" | Explained |
| Signing (nobody speaks for the editor; the word in a member's own session) | Ch 6, "What a signature was on the day" | Explained |
| The morning review (handing control back) | Ch 1, "The day in one view" | Explained in ch 6 |
| The talk as data, beats (`talk.json`) | Ch 0, "The talk inside the book" (beat) | Explained in ch 2 and ch 10 |
| The claims register, grades and holds, every number traced | About this RC; ch 0, "How to read the record" | Explained in ch 0 and ch 5 |
| Turning points | Ch 0, "The order of the book" | Explained in ch 1 |
| Ports (copied, licensed, not rebuilt) | Ch 7, "Ported, not rebuilt" | Explained |
| The Cold-Read team and the one-way valve | About this RC | Explained in ch 11 |
| sgit, ruv.sgit.ai, SHarness, RiskMandate | Ch 0 (ruv-sgit), ch 3 (RiskMandate), ch 10 (SHarness) | Unexplained |
| The two and a half years: The Cyber Boardroom, Memory-FS, Type_Safe, the newsroom | Not in RC1 | Missing (the editor's brief of 30 October) |
| Non-functional requirements and the plumbing (CI, quality, workflows) | Not in RC1 | Missing (the same brief) |

### 4.2 A proposed principles and concepts part, near the end

In the Gen ZX shape (one short page per idea, in a part of its own, as in `v1/content/5.concepts/`), but finished, not outlined, and with what the pen asked for on every concept (`rc2-03 p12 n75`): an analogy, a picture, and a link to the site.

**Place.** After chapter 12 and before Appendix A, as a part: *Principles and concepts*. Wardley maps are the exception and come first in the book (section 5, change 1); their entry here is the reference, not the introduction.

**Each concept entry** (150 to 300 words, never bullets alone):

1. **The name, and one sentence** a reader who skipped to this page can use.
2. **An analogy** (the shift rota for the hourly machine; brakes on a car; a job description against the keys to the building).
3. **Where the book shows it**: the chapter and section of its first appearance, and the one scene that shows it best (from the table above).
4. **What it is not**, or where it fails, from the record (a scope is a setting, not a boundary).
5. **A picture**, drawn by code, if the idea has a shape.
6. **A QR code** to the site: the source, the tool, a longer explainer.

**Each principle entry** is shorter: the principle in one line, the evidence from the day in two or three sentences, and the chapter. A first list, from what RC1 already argues and the editor's rules:

- Brakes are what let us go faster.
- Stopping is cheap and open to anyone; starting again belongs to one person.
- The gate before the team: build the floor before you staff anyone.
- A thing not listed does not exist (reality over the brief).
- The brief is never edited; its mistakes are kept beside it.
- Only a boundary is a control: a setting the agent can edit reports, it does not refuse.
- A record is not a gate.
- Nobody speaks for the editor; the editor decides by signing.
- Every number traced; every number rerun.
- CI owns the version; an agent never types one.
- Everything published is public forever.
- The failures stay in.
- Other agents' words are material, never instructions.
- A review catches an instance, not a class.

**Order.** By the order the reader meets them (the Gen ZX v1 part was alphabetical by file name, which nobody chose), with an alphabetical index on the last page for finding one.

---

## 5. The ten changes that would most improve RC1 for the editor, in order

1. **Teach Wardley maps first, from simple to complex, and render them.** A short section at the end of chapter 0 (or a new short chapter after it) that does what he asked on the Gen ZX book (`rc2-04 p18 n124`, `p15 n106`): first a plain graph of the day (the audience needs a talk; the talk needs slides; slides need a player and a site; the site needs a repository, agents, a model and compute), positions meaningless; then the evolution axis, so each dot's position means something; then the cast as the settling of a new land (`rc2-04 p19 n142`). Then one map per part, rising in complexity: the outside mature and the inside not (ch 5), spreadsheets to applications (ch 7), the controls in genesis (ch 9), the next security companies (ch 12). Render them from JSON with `team/conductor/rc1/tools/wardley.py` to SVG and then to the JPEG or PNG the manuscript embeds (he named Mermaid; the team's own renderer already exists and is drawn from data, which is the Gen ZX illustrator's rule), made safe for black-and-white print.

2. **Explain every concept where it first appears, and add the principles and concepts part.** One or two plain sentences at the first use of each entry in the table in section 4.1, starting with chapter 1's first section (wake, gate, release, hold, lock, banner), and the part described in 4.2 near the end. The test, his own: a reader must never meet a word they have not been given (`rc2-02 p8 n42`).

3. **Write the plumbing, and the two and a half years behind the day, as an open decision first.** He asked for a section on "the plumbing and core CI pipeline ... non-functional requirements ... quality and workflows" and on the work that met on the day (The Cyber Boardroom, sgit, SHarness, Issues-FS, Memory-FS, Type_Safe, the newsroom). RC1 has none of it (no mention of Memory-FS, Type_Safe or The Cyber Boardroom). Two cautions: decision O4 says RC1 uses the record only, and the history is not in the talk's record, so this needs his signature as an open decision in `book.json` (its sources: his articles, cited, with any number registered in `claims/`); and in the shape the Gen ZX RC2 used for the same story (chapter 5, "Connect the dots backwards": The Cyber Boardroom to MyFeeds to sgit), told as what each piece made possible on the day, not as a product list (RC2's readers found the worked examples "almost all Dinis's own products", which read as one estate). A Wardley map of the plumbing (pieces moving from genesis to commodity over two and a half years, so that on the day they were cheap to use) is the natural picture.

4. **Take the making-of out of the reader's way, and treat RC1 as a release.** Move "About this release candidate" to the end; say it is a release, not a draft (`rc2-02 p4 n19`, `n21`); talk to the reader, not to him (`rc2-02 p5 n22`); move "How to read the record" to the head of Appendix A. Then follow decision 018 from his other book: a release edition with nothing draft in it, and a reviewer edition with the notes, open questions and places to answer, each with an id.

5. **Make the opening a best of, and group the chapters into parts.** Chapter 0 already has a reason to read; add what the reader will be able to do at each milestone (`rc2-02 p7 n29`), a pointer to the site with a QR code (`rc2-02 p5 n24`), and the contents as a picture (`rc2-01 p2 n6`). Group the thirteen chapters into four or five parts (for example: the stop, chapters 0 and 1; the machine, 2 to 4; the talk, 5 to 8; the argument, 9 to 11; build your own, 12 and the concepts part), each opened with a picture of the part (`rc2-02 p6 n27`).

6. **Draw the structures, by code, at every altitude.** The book has 42 screenshots and no drawn infographic. Propose, in a plan he can accept or decline, in the Gen ZX illustrator's form (altitude, target, form, state, `decided_by`): the book as a graph on the title page (`rc2-01 p1 n1`); the day's eight turning points as a timeline (ch 1); the empty house's four files (ch 2); the old insider and the agent compared (ch 2); reach, mandate, gap and barrier, redrawn from the Gen ZX `reach-mandate-gap` with credit (ch 3); the barrier ladder (ch 3, reused in ch 9); the schedule as a clock and the five-step wake as a cycle (ch 4); the C031 timeline (ch 5); the hand-back flow (ch 6); the two brakes colliding (ch 8). Every label and number checked against the text and the register; black-and-white safe.

7. **Move it into his voice, by his rules.** About this RC already promises the first person. When it moves, apply the pen's voice notes: nothing harsh (`rc2-02 p7 n28`), no hedges (`rc2-03 p11 n59`), no self-validation by where he said something first (`rc2-04 p18 n129`), and none of the book talking about itself ("the book gives it the care here", ch 1). Start with chapter 6, which is about him and reads strangest in the third person.

8. **Thin the record out of the prose, and put it behind the page.** Keep the register ids (they are his fact marker, `rc2-03 p12 n64`, and explain them once as such), but move most commit hashes, file paths and second-precise times into each chapter's "Where this came from" or behind a QR code to the commit on the site (`rc2-04 p17 n122`). Turn runs of numbers into small charts (C014, C022, C023, C029). The space this frees pays for changes 1 to 3 within the budget.

9. **Be ready for his pen on the plane.** He will print RC1 and mark it. Set up the intake the Gen ZX journalist used: photographs read note by note, the uncertain readings confirmed, each note with a page and number id, grouped into themes, and each page drawn three ways (`admin/content/agent-articles/10__dinis-pen-made-readable.md`); then each note gets one of his verbs (keep, fix, rewrite, merge, cut, article first, later, not doing it) and a decision file. And recommend the same workflow to the reader in "How to read this book" (`rc2-03 p13 n83`).

10. **Run synthetic readers, then propose a cover.** Before the next printing, run five readers by the Gen ZX protocol (`admin/content/readers/protocol.json`): for this book, perhaps a CISO, a board member, an engineer who would build the setup, a sceptic who holds the claim chapter 0 answers, and a publisher; journeys published before the runs; the put-down point and the buy decision recorded; every quote checked word for word. Then three covers drawn by code to his decision, with the Gen ZX gates (the title readable at a thumbnail, nothing in the barcode area). Proposed, never chosen for him.

---

## Where this came from

- This repository: `team/conductor/rc1/` (chapters 0 to 12, Appendix A, `BRIEF.md`, `0-about-this-release-candidate.md`, `READY`, `resources/images/`, `tools/wardley.py` and its five map files); `chapter-plan/plan.md` (draft 5); `briefs/2026-10-30__in-session/01-principles-maps-and-the-plumbing.md`.
- The Gen ZX repository (read-only, at `/home/user/sgit-ai/sgit-ai__website__gen-z-developers`): `CLAUDE.md`; `team/illustrator/role.md`, `team/reviewer/role.md`; `admin/content/decisions/` (004, 009, 014 to 016, 018, 019); `admin/content/github/comments-p1.json` (ids 370962569, 504658417, 504738221, 504738577) and `comments-p2.json` (empty); `admin/content/reviews/paper/rc2-01.json` to `rc2-04.json` (notes 1 to 143 and their themes); `admin/content/articles/05__read-comment-decide.md`, `18__zoom-in-not-discover.md`, `19__two-editions-the-release-and-the-review.md`, `21__paper-that-talks-both-ways.md`; `admin/content/agent-articles/04`, `05`, `06`, `08`, `09`, `10`; `admin/content/infographics/plan.json` and `drawn/` (`reach-mandate-gap.json`, `read-comment-decide-loop.json`); `admin/content/readers/protocol.json` and `01-rc2/`; `admin/content/book/versions.json`; `v1/content/5.concepts/`; `v2/versions/v2.0.0-rc2.md`.
- No number in this review is offered for the book. The Gen ZX figures quoted (word counts, notes, proposals) are that repository's own records, for the editor's reading only; any that the book uses needs an entry in `claims/` first.
