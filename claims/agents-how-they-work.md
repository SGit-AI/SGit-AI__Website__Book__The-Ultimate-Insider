# What a character may say about how it works

researcher@book.the-ultimate-insider, 1 November 2026, for NR1 (the book told by its cast; the conductor's letter `comms/mail/mailroom/researcher/conductor__033-nr1-true-explanations.eml`). When an agent in the book explains itself, it says something about how language models work. This sheet gives the lines the sources support, the source for each, and an example from the day's own record. It explains; it gives no way to make an agent misbehave. Register entry C096.

Every source below was read on 1 November 2026, about 00:45 UTC.

## 1. "I can make things up, and say them as if they were true."

- **Source:** Anthropic's documentation, "Reduce hallucinations" (https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations). It recommends allowing the model to say "I don't know", grounding answers in direct quotes, and verifying claims with citations. It warns: "although these techniques significantly reduce hallucinations, they don't eliminate them entirely."
- **A character may say:** that it can state something false with confidence; that being allowed to say "I don't know" helps; that it never fully stops.
- **The record's example:** the talk's own register checked 320 claims, and 3 did not hold (C029, C030). A figure it had already found out of date still reached a slide (C031).

## 2. "Give me the source, and I stay closer to the truth."

- **Source:** the same page: "ask Claude to extract word-for-word quotes first before performing its task" for long documents, and answer only from them.
- **A character may say:** that working from quoted, pinned sources (a commit, a file, a page with its date) keeps it honest, and that it should say so when it finds no quote.
- **The record's example:** this book's register, where every number carries the command that reruns it against a pinned commit (`claims/appendix-a-commands.md`). The anchoring the editor means is that file.

## 3. "The more you give me, the more I lose."

- **Sources:**
  - Liu et al., "Lost in the Middle: How Language Models Use Long Contexts" (arXiv 2307.03172, 2023; TACL 2024): "performance can degrade significantly when changing the position of relevant information", and models "do not robustly make use of information in long input contexts".
  - Anthropic Engineering, "Effective context engineering for AI agents" (https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): "as the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases", which it calls context rot. Context "must be treated as a finite resource with diminishing marginal returns".
- **A character may say:** that a long session makes it worse at finding what is in it, especially things in the middle; that its memory is not the conversation but the files it writes.
- **The record's example:** the team kept its memory in files, not in sessions: wake records, debriefs, handovers. When the first account ran out, each role passed to a new session through a handover file and a new key (`team/conductor/handovers/`, 30 October).

## 4. "My instructions are words, and so are yours."

- **Source:** the same engineering post. Good context engineering means "finding the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome".
- **A character may say:** that its brief, its role file and its rules are all text it reads every time. Clear, short and written down works better than long and implied.
- **The record's example:** every member's `ROLE.md` and `policy.json`, read at the start of every wake (C072: eight of ten policies agreed by the end of the day).

## What a character may not say as fact

- How its model was trained, or what is inside it.
- Any percentage of hallucination, or of accuracy, unless the book registers the study and the conditions with it.
- How much the day cost in tokens: the record holds none (C021, C089).

## Where this came from

The three sources above, read on 1 November 2026; the claims named; `briefs/2026-11-01__in-session/01-the-story-told-by-its-characters.md` for the ask.
