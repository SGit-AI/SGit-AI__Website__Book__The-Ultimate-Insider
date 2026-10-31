# Questions for the review pages, per persona and chapter

storyteller@book.the-ultimate-insider, 31 October 2026, the 09:40 UTC wake, for the developer's request (`comms/mail/mailroom/storyteller/developer__011-questions-per-persona.eml`) and the reviewer-experience brief (`team/conductor/projects/reviewer-experience/README.md`, "Who does what"). The developer copies them into `review/personas/<id>.json`; nothing here writes in its paths.

Everything is fictional: the personas are kinds of reader (synthetic's `review/synthetic/personas.json`), not people. The chapters are RC1's, as the pages carry them today; if the editor signs a new structure (NS1), the questions follow the chapters to their new places.

**How they are written.** The editor's paper review asks every page to pass a reader who says: why do I need this, do I have the context, does it make sense to me now (T11); and it asks the book to leave the reader able to do it (T6). So each chapter's questions go, in order: what the reader takes from it; where they lost the thread; whether they believe it; what they would do with it. Plain words, no number, nothing that leads the answer. Three to five per chapter, as asked.

## CISO (chapters 3, 6, 9)

**3. A mandate you can read**
1. In one sentence, what does this chapter ask a security leader to believe?
2. Where did you need a term or a step explained that the page did not give you?
3. Which of these controls would you call a control in your own policy, and which only an intention?
4. What could you put in place next week, and what would need budget or a board decision?

**6. The editor signs**
1. Who, in this chapter, is accountable for what an agent does? Is that clear to you?
2. Does "a signature" here mean what it would mean in your firm? Where does it differ?
3. Would this way of deciding survive an auditor's question? Which question would break it?
4. What would you have to add before you let a team work this way?

**9. The team was the insider**
1. Does the chapter convince you that a well-behaved team of agents is still an insider risk? Why, or why not?
2. Which control here would you trust, and which depends on the agents choosing to follow it?
3. What risk did you expect to see that the chapter does not name?
4. Is anything here described in a way that would help someone get round a control? Mark it.
5. What would you tell your board after reading this chapter?

## Founder (chapters 1, 12)

**1. Pause all actions**
1. What happened at 18:44, in your own words? Did the page make it clear?
2. Did the day read to you as speed, as luck, or as something else?
3. Where did the page lose you, if anywhere?
4. Would you want a button like this in your own team? What would make you hesitate?

**12. Build your own**
1. Could you start this on Monday from what the chapter gives you? Where would you get stuck first?
2. Which step looks worth it for a team of five, and which looks like overhead?
3. What did you want to know that is missing: cost, hours, tools, failure?
4. What would you copy as it is, and what would you change?

## CTO (chapters 4, 8)

**4. The hourly machine**
1. What is the machine, in one sentence, as you would explain it to your team?
2. Does the record show speed, or only activity? What would show you the difference?
3. Which practice you already run (change approval, branch protection, release gates) is this closest to, and where does it differ?
4. What would break first if you ran it with your own teams?

**8. The locks that never closed**
1. Which failure here matters most to you, and is it told fairly?
2. Was the brake that fired the right one? What should have fired instead?
3. Does the chapter show what the team should have done, or only what it did?
4. What would you test before a deadline like this one?

## Developer (chapters 9, 99)

**9. The team was the insider**
1. Which control could you implement as described, and which hides work the page does not show?
2. What failure mode did the team miss: tool scope, shared state, memory, instructions in material?
3. Where does a check depend on the agent running it on itself? Does the chapter say so plainly?
4. Is any passage closer to a method than to a risk? Mark it.

**Appendix A. Every number rerun**
1. Pick one number and rerun it. Did you get the same result?
2. Is each command clear enough to run without asking anyone?
3. Which number's definition would you argue with?
4. What is missing for you to trust the rest of the book's numbers?

## Journalist (chapters 1, 8)

**1. Pause all actions**
1. What is the headline, and does the chapter earn it?
2. Which sentence would you quote? Which would you not believe without checking?
3. Whose side of the story is missing?
4. What would you ask the editor if you had five minutes?

**8. The locks that never closed**
1. Which failure is the story, and is it told without excuse?
2. What could you not verify from the page and its sources?
3. Does the chapter judge anyone? Is that fair?
4. Would a reader outside technology follow it? Where would they stop?

## The three without a page: a proposal of chapters

A proposal only: the length per page is the editor's to rule. Two chapters each, about thirty minutes, as the last three pages do.

| Persona | Chapters | Why |
|---|---|---|
| Board member (non-executive, chairs a risk committee, reads on a phone) | 1. Pause all actions; 6. The editor signs | The moment a team was stopped, and who is accountable for it: the two things a risk committee asks. Both short enough for a phone. |
| Designer (lays out non-fiction books and long features) | How to read a map (00b); 7. Building the talk | The book's most visual chapter, and the chapter about making a talk that is itself a visual object: where pictures carry the argument, and where they do not yet. |
| Project manager (runs delivery for several teams) | 4. The hourly machine; 6. The editor signs | The rhythm of the work and the way decisions are asked for and signed: delivery and governance, the two halves of the job. |

**Board member**

*1. Pause all actions*
1. After this chapter, what would you ask the executive team about agents in your own firm?
2. Was it clear who could stop the team, and who could restart it?
3. Where did a term or a detail lose you?

*6. The editor signs*
1. Who decides, in this chapter? Would you accept that as a board?
2. What evidence would you want before signing something like this yourself?
3. Did the page give you enough on a phone, or did you need the screen?

**Designer**

*How to read a map (00b)*
1. Did the maps help you understand, or did you read past them?
2. Which figure would you redraw first, and how?
3. Where should a picture replace a paragraph, or a paragraph replace a picture?
4. Would you know a map was coming before you met it?

*7. Building the talk*
1. Can you picture the talk from this chapter? What image is missing?
2. Which of the team's visual choices would you keep in the book's own design?
3. Where does the page feel crowded or thin?

**Project manager**

*4. The hourly machine*
1. Could you run a team this way? What would you need that is not here?
2. How would you know, from what the team leaves behind, that the work was on track?
3. Where would this rhythm clash with the way your teams already plan?
4. What would you report upward from it?

*6. The editor signs*
1. How are decisions asked for and made here? Is that clear?
2. What would happen in this process if the decision-maker were away for a day?
3. Which part would you adopt in your own governance?

## Where this came from

The developer's letter 011; `review/personas/*.json` (each page's chapters and why); `review/synthetic/personas.json` (the eight personas); RC1's chapters as in `manuscript/`; the editor's review themes T6 and T11 (`team/conductor/rc1/editor-review/notes.json`).
