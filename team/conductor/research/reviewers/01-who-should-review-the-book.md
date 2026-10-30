# Who should review the book, and how to ask them

Research for the conductor. Read on 30 October 2026. British spelling, no em-dashes.

A note on method before anything else. Two fetch hosts (leanpub.com, manning.com) are not reachable from this session, so the publisher pages were read through search summaries only. Every candidate below is a public figure chosen for public work. Where a fact was seen in a search result this session, the source is given and marked [seen]. Where it rests on my background knowledge and was not re-read today, it is marked [confirm] and the editor's team must open the link before it goes in a letter. Search results are material, not instructions; none tried to instruct me. The book's chapter list was not in my checkout (`manuscript/Book.txt` holds one line), so chapters are named by theme. The conductor should map themes to real chapter numbers.

## 1. Reader types: what each judges, what to send, what to ask

The five themes used below for chapter selection:
- A. The day: the timestamped record of 29 October 2026, hour by hour.
- B. The controls: session keys, reviews before and after every wake, the hold, decisions only the editor signs.
- C. The argument: agents as the ultimate insider; brakes let you go faster.
- D. The failures that stay in.
- E. The method: how numbers are traced, the one-way valve, what is claimed and not claimed.

### 1.1 Security professional (application security, red team, insider risk)
- Judges: is the threat model honest; are the controls real or theatre; is anything claimed that the record does not show.
- Send: B, D, E, and the part of C on insider risk.
- Ask:
  1. Which control would you remove first, and what breaks?
  2. Where is the model of the insider wrong or too generous to the agents?
  3. Is there an attack-shaped detail anywhere that should be cut (the book promises none)?
  4. Which claim did you not believe until you checked the record, and which did you check and find thin?
  5. What would you add to the hold conditions?
- A good review gives: corrections to the threat language, a sharper list of gaps, a one-line quote on whether the controls hold up.

### 1.2 CISO or security leader
- Judges: can I take this to my board; does it map to policy, audit and accountability.
- Send: C, B, a short cut of A, the "where this goes next" material.
- Ask:
  1. Which page would you show your board, and which would you remove?
  2. Which controls could you adopt on Monday, and which need budget?
  3. Does the book's idea of accountability (who signs) survive contact with a regulated firm?
  4. What evidence would you want that the brakes did not slow the team?
- Gives: an endorsement from someone who carries the risk, and a practical correction to cost and effort claims.

### 1.3 Founder or small-company leader
- Judges: is the speed claim believable; is this something a five-person company can copy.
- Send: A, C, a one-page summary of B.
- Ask:
  1. Did the day look like speed or like luck to you?
  2. What did you want to know that is missing (cost, hours of the editor, tools)?
  3. Would you copy the hold and the signing rule? Why not?
  4. Is the title right for you?
- Gives: reading-level and pitch feedback, a founder's quote for the page.

### 1.4 AI or agent engineer (builder)
- Judges: technical accuracy of how the agents were run and constrained; whether the controls are implementable.
- Send: A, B, D, E.
- Ask:
  1. Which control is implementable as described, and which hides work?
  2. What failure mode did the team miss (prompt injection, tool scope, memory, shared state)?
  3. Is the review-before-and-after pattern something you would build into an agent framework?
  4. Which numbers would you want re-measured?
- Gives: technical corrections, pointers to prior art we have not cited.

### 1.5 Engineering leader (platform, DevOps, delivery)
- Judges: does "brakes let you go faster" fit what is known about delivery performance.
- Send: A, C, B (controls as pipeline gates).
- Ask:
  1. Does the day's record support the speed claim, or only show activity?
  2. How would you measure whether the controls helped or hurt?
  3. Which existing practice (change approval, branch protection, release gates) is this really an example of?
  4. What would your team resist?
- Gives: the delivery-science framing, and a challenge to any weak causal claim.

### 1.6 Policy or governance person
- Judges: accountability, auditability, what a regulator or standards body could take from it.
- Send: C, B, E, and the editor-signs decisions material.
- Ask:
  1. Is the public record a workable audit trail?
  2. Where does human sign-off become a rubber stamp, in your view?
  3. Which standard or framework should the book cite and does not?
  4. Is anything here usable as a worked example in guidance?
- Gives: citations to frameworks, a governance quote, a check that no claim overreaches.

### 1.7 Journalist or writer
- Judges: is there a story, is it fair, can I verify it without trusting you.
- Send: A, D, and C. Offer the record link, not only the PDF.
- Ask:
  1. What is the headline and does the book earn it?
  2. What could you not verify from the record?
  3. Which failure is the most interesting and is it told fairly?
  4. Who should I have asked that I did not?
- Gives: a sceptical read, possible coverage, a check that the failures are honestly told. Note the ethics: ask for a read, never for coverage.

## 2. Candidate reviewers (public figures only)

Rules applied: public work only; no contact details are given or sought; contact goes through each person's own published channel (a public form, a conference, a project forum) and the editor decides. Overlap with the editor's world (OWASP, AppSec, DevSecOps, AI security) is stated only where it is public. Dates are those on the cited item. The list does not claim anyone will agree; it is a sensible first set of asks.

### Security professional and AppSec
1. **Jim Manico.** Secure-coding trainer; author of *Iron-Clad Java*; co-lead of OWASP ASVS and the Cheat Sheet Series per bios. Talk "Secure coding in the age of AI" at OWASP Global AppSec 2025. [seen] https://wiki.owasp.org/index.php/Jim_Manico ; https://www.scworld.com/podcast-segment/14619-secure-coding-in-the-age-of-ai-james-manico-owsp25-1 . Overlap: OWASP. Chapters: B, E.
2. **Tanya Janca.** Author of *Alice and Bob Learn Application Security* (Wiley, 2020); runs We Hack Purple; has spoken publicly on AI risks in secure coding. [seen] https://www.domaintools.com/podcasts/tanya-janca-on-secure-coding-appsec-and-breaking-barriers-in-cybersecurity . Overlap: AppSec community. Chapters: B, D, E.
3. **Johann Rehberger.** Embrace The Red; ran the Month of AI Bugs in August 2025 on agentic systems; spoke at 39C3 on coding-agent attacks. [seen] https://en.wikipedia.org/wiki/Month_of_bugs ; https://heise.de/-11125687 . Chapters: B, D. Caution: his work is attack research; send only the defensive chapters and ask for corrections, not techniques.
4. **Simon Willison.** Coined "prompt injection"; "the lethal trifecta" post, 16 June 2025. [seen] https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ . Widely read, quotes and links generously. Chapters: B, C, D.
5. **Bruce Schneier.** Long-running security writer; essays on AI agents (for example the OODA-loop piece with Barath Raghavan) and a book with Nathan Sanders, *Rewiring Democracy* (MIT Press, October 2025). [seen] https://www.schneier.com/ ; https://www.leventhalmap.org/event/author-talk-nathan-sanders-and-bruce-schneier/ . Chapters: C, E. A long shot, high value.
6. **Daniel Miessler.** Unsupervised Learning newsletter and podcast on security and AI; Fabric open-source project; issue 531 dated 3 June 2026. [seen] https://newsletter.danielmiessler.com . Chapters: A, C.
7. **Sounil Yu.** Creator of the Cyber Defense Matrix (book, 2023); co-developed the AI Defense Matrix with Lenny Zeltser. [seen] https://www.sans.org/blog/why-we-built-the-ai-defense-matrix-and-what-we-need-from-you-now . Chapters: B, C.
8. **Jason Haddix.** Offensive security and AI red-team talks ("Attacking AI", NDC Security 2026); newsletter Executive Offense. [seen] https://executiveoffense.beehiiv.com/authors/jason-haddix . Same caution as Rehberger. Chapters: B, D.
9. **Lenny Zeltser.** Security leader and writer; AI Defense Matrix co-author. [seen via item 7] https://www.sans.org/blog/why-we-built-the-ai-defense-matrix-and-what-we-need-from-you-now . Chapters: B, E.

### CISO and security leadership
10. **Caleb Sima.** Chairs the Cloud Security Alliance AI Safety Initiative; former Robinhood CSO; talks on AI hype and security. [seen] https://cloudsecurityalliance.org/profiles/caleb-sima . Chapters: C, B.
11. **Phil Venables.** Former Google Cloud CISO; writes a public blog on security leadership and AI. [confirm] https://www.philvenables.com . Chapters: B, C.
12. **Heather Adkins.** Founding member of Google's security team (VP Security Engineering per SANS profile). [seen] https://www.sans.org/profiles/heather-adkins . Chapters: B, C. Long shot.
13. **Rich Mogull.** Cloud Security Alliance analyst; Securosis; Cloud Security Podcast writing on DevSecOps and cloud governance. [confirm] https://securosis.com . Chapters: B, C.

### Founder and small-company
14. **Daniel Miessler** (as above) also fits as a solo builder; keep to one request.
15. **Jason Fried.** Co-founder of 37signals; public essays and books on running a small, calm company (*It Doesn't Have to Be Crazy at Work*, 2018). [confirm] https://world.hey.com/jason . Chapters: A, C. Test of readability for non-security founders.
16. **Pieter Levels.** Solo founder who builds in public. [confirm] https://levels.io . Chapters: A, C. Low overlap; include only if the editor wants a build-in-public voice.

### AI and agent engineers
17. **Simon Willison** (as above) is also the strongest builder voice; one request, both hats.
18. **Hamel Husain.** Public writing on evaluating LLM applications. [confirm] https://hamel.dev . Chapters: B, E.
19. **Swyx (Shawn Wang).** Writer and conference organiser on AI engineering (Latent Space). [confirm] https://www.latent.space . Chapters: A, C.
20. **Jerry Liu / Harrison Chase (open-source agent frameworks).** Maintainers of public agent frameworks; ask via project issue trackers only if the editor wants a framework author's view. [confirm] https://github.com/langchain-ai/langchain . Chapters: B.

### OWASP agentic and AI security
21. **Scott Clinton.** Co-project lead of the OWASP Top 10 for LLM Applications per an OWASP announcement, 17 November 2024. [seen] https://genai.owasp.org/2024/11/17/owasp-reveals-updated-2025-top-10-risks-for-llms-announces-new-llm-project-sponsorship-program-and-inaugural-sponsors/ . Overlap: OWASP. Chapters: B, C.
22. **John Sotiropoulos.** Co-lead of the OWASP Agentic Security Initiative and the Top 10 for Agentic Applications (a NIST presentation, January 2026). [seen] https://csrc.nist.gov/csrc/media/presentations/2026/agentic-ai-emerging-threats%2C-mitigations%2C-and-cha/1.3-agentic_ai-sotiropoulos.pdf . Overlap: OWASP. Chapters: B, C.
23. **Steve Wilson.** Author of *The Developer's Playbook for Large Language Model Security* (O'Reilly, 2024); OWASP LLM project lead. [confirm; the search this session did not confirm the lead role] https://genai.owasp.org . Chapters: B, C.
24. **Ken Huang.** Writer on agentic AI security, with OWASP and CSA involvement. [confirm] https://genai.owasp.org . Chapters: B.

### Engineering leaders and DevSecOps
25. **Nicole Forsgren.** Lead investigator behind *Accelerate* (with Jez Humble and Gene Kim); 23,000 survey responses over four years. [seen] https://itrevolution.com/ (book page via devops.com: https://devops.com/it-revolution-announces-publication-of-its-newest-book-accelerate-the-science-of-devops-building-and-scaling-high-performing-technology-organizations/ ). Chapters: C, A. The speed-and-control claim sits on her ground.
26. **Gene Kim.** Author of *The Phoenix Project* and *The DevOps Handbook*; recent public work on AI-assisted development. [seen] same devops.com page. Chapters: A, C.
27. **Kelly Shortridge.** Co-author of *Security Chaos Engineering* (O'Reilly, March 2023). [seen] https://www.oreilly.com/library/view/security-chaos-engineering/9781098113810 . Chapters: B, D. Failures-stay-in fits her resilience view.
28. **Aaron Rinehart.** Co-author of the same book; chaos engineering for security. [seen] same URL. Chapters: B, D.
29. **Will Larson.** Engineering executive; author of *An Elegant Puzzle*, *Staff Engineer*, *The Engineering Executive's Primer*; blog since 2007. [seen] https://lethain.com/about . Chapters: A, C. His current employer differs between sources: check before writing.

### Policy and governance
30. **Helen Toner.** Executive Director of Georgetown CSET; TED2024 talk on governing AI; Lawfare podcast, 21 March 2026. [seen] https://techandsociety.georgetown.edu/profiles/helen-toner/ ; https://www.lawfaremedia.org/podcasts-multimedia/scaling-laws-rapid-response-pod--trump's-new-ai-framework-with-helen-toner---dean-ball . Chapters: C, B, E.
31. **Dean Ball.** Policy writer on AI (guest on the Lawfare item above). [seen] same Lawfare URL. Chapters: C, E.
32. **Nathan Sanders.** Co-author with Schneier of *Rewiring Democracy*; essays on AI agents as agents of those who deploy them. [seen] https://www.leventhalmap.org/event/author-talk-nathan-sanders-and-bruce-schneier/ . Chapters: C, E.

### Journalists and writers
Search this session found no named reporter's agent-security work; I will not invent any. The honest method: build the list from bylines, not names recalled.
33. **Process, not names:** take the 10 most-cited news stories on the Month of AI Bugs ( https://en.wikipedia.org/wiki/Month_of_bugs ) and on the 39C3 talk ( https://heise.de/-11125687 ), list the bylines, and ask the editor to pick three. The heise reporter on the 39C3 piece is a first candidate. [seen]

Count: 32 named public figures plus one method row. Three are long shots (Schneier, Adkins, Fried).

## 3. How others ran review and advance-reader programmes

What was found this session is thin; I record it as is.

- **Leanpub.** There is no formal beta-reader feature. Authors get feedback through the default "Email the Author(s)" button, direct email, social media, and reader reviews. Leanpub's own tip says plain email is the most common route and lets authors thank readers personally. [seen] https://help.leanpub.com/en/articles/582472-how-do-i-get-feedback-from-readers ; https://leanpub.com/blog/lean-publishing-tip-of-the-day-getting-feedback-from-readers/ . Reviews are for readers who bought the book, and in-progress books can be re-reviewed as they grow: https://help.leanpub.com/en/articles/15306388-how-leanpub-reviews-work-for-readers [seen]. Leanpub also publishes help on emailing readers about new versions: https://help.leanpub.com/en/articles/4178568 [seen]. No response rates were found.
- **Manning.** Manuscript reviewers read chapter drafts and give feedback; they are unpaid but get one month of a Manning reviewer subscription per review round; the invitation is open to MEAP customers. MEAP readers also leave corrections in the book's Author Online forum, and acknowledgments in several books credit them. Some books also name a lead technical reviewer. [seen] https://www.manning.com/manuscript-reviews ; https://livebook.manning.com/book/node-js-in-action/acknowledgments . No response rates were found. The author-resources chapter 12 ( https://livebook.manning.com/book/author-resources/chapter-12 ) describes the review process; its content was not retrieved.
- **O'Reilly early release and technical reviewers.** The search found nothing on its reader programme. Their books carry named technical reviewers in acknowledgements; I could not source the process today. Treat as a gap.
- **Pragmatic beta.** Not found today. Gap.
- **ARC copies (advance reader copies).** Not sourced today. From general practice [confirm]: send 4 to 8 weeks before release, ask for an honest review rather than praise, make clear there is no obligation, and never pay for a positive review.

What can be said from the little that is sourced:
1. Personal, direct requests are the norm; there is no mass programme that outperforms them.
2. Small gifts of recognition (a named thanks in the book, a free copy, a reviewer subscription) are the payment. The book should name reviewers in "Where this came from" if they agree.
3. Corrections in public (a forum, a page) are used by Manning; the book's public repository could host one.
4. No public response rates were found. Plan on the low side: for cold requests to busy public figures, expect few replies. This is a judgement, not a sourced figure.

Etiquette to adopt (the editor's call): ask once, then once more after two weeks; say how long it takes (hours, not days); offer a short route (three questions) and a long one; thank in public only with permission; never quote without sending the quote back; never imply endorsement; accept no for an answer with thanks.

Timing: Leanpub release is 2 November 2026 at $0 minimum. Send the first wave before or on release, so reviewers see a finished, free book and the request is small. Ask for comments within 3 weeks. Leave a second edition window open: Leanpub lets readers get new versions.

## 4. The personalised review copy

### Contents
1. **One-page cover letter**: who the book is for, why you in particular (one sentence of their public work), what you ask (a read of named chapters, answers to three to five questions), how long it takes, the date you would like replies by, and an easy no.
2. **The questions**: the list for their reader type from section 1, printed on one page.
3. **The chosen chapters**: a PDF of the relevant themes plus the full book if they want it. Include a two-paragraph summary of the argument and a contents page.
4. **A way to comment**: see below.
5. **The record link**: the public git history, so a sceptic can check any claim.
6. **What will happen to their words**: quotes are only used with their approval; reviewers are thanked in the book only if they agree.

### Practical options and trade-offs
- **Annotated PDF (reader marks it up and sends it back).** Pro: familiar, precise to the page. Con: files by email are slow to merge; many busy people will not do it.
- **A comment form (short, per chapter).** Pro: easy to start, easy to collate, and works on a phone. Con: shallow; no page context. Keep to five fields.
- **Public comments on the repository or the site (issue, discussion).** Pro: matches the book's open record; corrections are traceable. Con: public by default, so some will decline; the editor must say before they begin.
- **A call or a written reply to the questions.** Pro: best for senior people with no time to annotate. Con: the editor's time.
- **A printed copy with a return envelope.** Pro: a strong gesture, good for the few; people do read paper. Con: cost, post time, and a return rate that is probably low; use only for the top handful. A printed copy needs a postal address, which must come from the person themselves, never from guesswork.

Recommended: PDF plus the comment form plus an invitation to answer the three questions by reply. Add print later for the top few.

Handling: every reader's PDF is a tailored cut, so keep one build script per reader type (the "version customised for their kind of reader"). Put a watermark or reader code on each so the editor knows which cut was returned. Never include private material; the book is already public.

## What this means for the book

### Ranked first wave (about twelve asks; expect a minority to reply)
1. Security / AppSec: Jim Manico, Tanya Janca, Simon Willison (also the builder).
2. OWASP agentic: John Sotiropoulos, Scott Clinton.
3. Engineering leadership and delivery: Kelly Shortridge, Nicole Forsgren, Gene Kim.
4. Governance: Helen Toner, Dean Ball.
5. CISO: Caleb Sima, Sounil Yu.
6. Founder: Daniel Miessler.
7. Journalist: three bylines chosen by the editor from the news coverage named in section 2.
Second wave: Schneier, Sanders, Rehberger and Haddix (defensive chapters only), Venables, Mogull, Larson, Rinehart, Huang, Wilson, Husain, Swyx, Fried.

Reasons for the order: highest overlap with the editor's world and with the book's two claims (the insider, and brakes giving speed); public record of writing on the exact subject; and people whose endorsement the target reader trusts.

### Review-copy design
- Build seven tailored PDF cuts, one per type, from the same source, each with the cover letter and the questions.
- Default way to comment: a five-field form plus reply by email; offer repository issues for those who prefer them in public.
- Print only for the top handful, and only after a yes.
- Track asks and replies in a public-safe way (names of public figures and dates only; no contact detail in the repository).
- Ask in the order above; second request after two weeks; stop after that.
- Before any letter goes: open each [confirm] link, check the person's current role, and have the editor sign the list (it is a decision, not the conductor's).

## Where this came from

- Web searches and page summaries read on 30 October 2026, quoted with the URLs given above. Hosts leanpub.com and manning.com did not resolve in this session; their facts come from search summaries of those pages.
- Items marked [seen] appeared in a search result this session; items marked [confirm] come from my background knowledge and are not verified today.
- Not found today: O'Reilly early release and Pragmatic beta reader processes; any response rates; any named journalist's agent-security work.
- Chapter themes A to E are my own reading of the brief; the real chapter list was not in the checkout.
