# RC1 against the editor's voice

By librarian@book.the-ultimate-insider, 31 October 2026, about 06:13 UTC, for the conductor's letter 004 (`comms/mail/mailroom/librarian/conductor__004-the-editors-voice.eml`): "say where a passage is not how he would say it, by those rules, with the file and the line". RC1 is locked (V2), so every finding is for RC2. The manuscript is the publisher's and is not edited here; line numbers are `manuscript/` at `f49d8b0`.

The rules are the newsroom writer's, as published: first person; honest about where he stands; the memo's order; plain words; public sources named and dated; private people never named; no em-dashes; British spelling; no superlative self-claims; never the model's name (https://newsroom.sgit.ai/team/newsroom-writer.md), and the handbook's rule 6: no superlative or hype word unless the text shows the evidence, never the ladder metaphor, plain words, no overstated feelings (https://newsroom.sgit.ai/articles/how-a-journalist-agent-publishes-here.md). Also read: https://newsroom.sgit.ai/articles/how-i-work-with-claude.md, in full.

## The one structural finding: RC1 is in the third person

The writer's first rule is the first person, and RC1 speaks of the editor as "the editor", "the speaker", "he". The scan counts the editor named in the third person in each chapter's prose (source lists and tables left out):

| Chapter | Third person | Chapter | Third person |
|---|---|---|---|
| 0 | 5 | 07 | 33 |
| 00 | 5 | 08 | 39 |
| 00b | 16 | 09 | 19 |
| 01 | 27 | 10 | 15 |
| 02 | 24 | 11 | 15 |
| 03 | 30 | 11b | 31 |
| 04 | 25 | 12 | 34 |
| 05 | 34 | 13 | 33 |
| 06 | 25 | 99 | 11 |

About 420 in all (421), against a handful of "I" anywhere. This is the revision letter 004 said was coming ("revised in place ... into his voice"), not a line-by-line fault, and it is larger than every other finding together. Two things it changes beyond pronouns:

- **The memo's order.** His articles open with where the piece comes from and what he thinks, then the evidence ("Where this comes from. A voice memo, recorded because..."). RC1's chapters open on a timestamp from the record. Chapter 10's first line is the example: "At 19:00 on 29 October the editor stood up at hack::soho ... and gave the talk."
- **Honest about where he stands.** In the third person the book can judge the editor from outside ("by the speaker's habit rather than by any check", chapter 10, line 74). In the first person the same judgement becomes his own admission, which is stronger and is what the rule asks; but each such line needs his word before it is printed as his.

## Lines to reread

| File:line | Rule | The passage | Suggestion |
|---|---|---|---|
| `03-a-mandate-you-can-read.md:67` | superlative | "The best example is late in the day." | "One example comes late in the day." |
| `03-a-mandate-you-can-read.md:81` | superlative | "The clearest case is the conductor's in the early afternoon" | "Take the conductor's, in the early afternoon" |
| `03-a-mandate-you-can-read.md:101` | superlative; repeated | "...is the clearest evidence in the record of what an agreement relayed by one agent..." | Plainer ("shows what an agreement relayed by one agent is worth"); and the same sentence appears in chapter 6, line 67: keep it in one chapter |
| `06-the-editor-signs.md:67` | superlative; repeated | "What happened to that sentence on its way into the files is the clearest evidence in the record of what a relayed signature is worth." | As above |
| `08-the-locks-that-never-closed.md:125` | superlative | "the evening is the clearest part of that evidence" | "the evening shows it most plainly" or cut |
| `09-the-team-was-the-insider.md:58` | superlative | "The clearest evidence of that came from this book's own team" | "Evidence of that came from this book's own team" |
| `09-the-team-was-the-insider.md:21`, `:29`, `:56` | the ladder | "A ladder of barriers", the figure's caption, "On the E10 ladder" | The rule bans the ladder metaphor. The talk drew E10 as a ladder, so the word is the talk's; the book can name it once as the talk's picture and otherwise say "the four barriers" or "the scale of barriers". The editor's call |
| `13-concepts-and-principles.md:47`, `:49` | the ladder | "The talk draws them as a ladder", and a figure note | As above |
| `10-the-talk-as-given.md:53` | "perfect" | "Tonight is about a perfect storm we are brewing." | Keep: his own words on stage, quoted, and the talk's title phrase |
| `99-appendix-a-every-number-rerun.md:91`, `:93` | a model's name | `git log 298be4e --author=Claude ...` | Keep: it is the author field in the record, inside a command the reader runs; a word in prose would not be allowed, a command has to match the data |

Clean across all 18 chapters: no em-dashes, no American spellings, no hype words, no model's name in prose.

## One chapter read closely: 10, the talk as given

Read whole against the rules. It is the chapter where the first person matters most, because it is about him on stage, and where it is easiest, because it already quotes him. Sentences that would read differently in his voice:

| Line | RC1 | In his voice, for his approval |
|---|---|---|
| 3 | "At 19:00 on 29 October the editor stood up at hack::soho, hosted by IOActive in London, and gave the talk. No commit marks it." | "At 19:00 on 29 October I stood up at hack::soho, hosted by IOActive in London, and gave the talk. No commit marks it." |
| 3 | "The lessons brief the editor wrote for this book says it in a line" | "I put it in one line in my brief for this book" |
| 17 | "At about 16:55 the editor had asked for the talk in three parts" | "At about 16:55 I had asked for the talk in three parts" |
| 19 | "The speaker knew some of this. Early in part one he told the room" | "I knew some of this. Early in part one I told the room" |
| 55, 62 | "The speaker used the slides, in order, and spoke in his own words." | "I used the slides, in order, and spoke in my own words." |
| 74 | "The line was not spoken, by the speaker's habit rather than by any check" | "I did not say the line, out of habit rather than because anything checked it": his admission, so his word first |

The rest of the chapter, its cautions about the edited transcript (line 7) and its plan-against-delivery reading, already keeps his other rules: plain words, sources named and dated, the room anonymous.

## How this was done

`team/librarian/voice/voice_scan.py` scans the rules a pattern can check (em-dashes, the newsroom's superlative and hype patterns, "perfect", the ladder, a model's name, common American spellings, and third-person references to the editor) over each chapter's prose before its sources. A hit is a line to reread. The superlative patterns restate the newsroom's own list (its `admin/build/wording.py`, read, not run). Chapter 10 was read whole. The other seventeen were scanned, not read for voice, so the first-person revision will turn up more than the table above.

## Where this came from

`manuscript/` at `f49d8b0`; https://newsroom.sgit.ai/team/newsroom-writer.md, https://newsroom.sgit.ai/articles/how-a-journalist-agent-publishes-here.md and https://newsroom.sgit.ai/articles/how-i-work-with-claude.md, read 31 October 2026 at about 06:11 UTC; SGit-AI/SGit-AI__Website__Newsroom `admin/build/wording.py` (dev, same time), read; `comms/mail/mailroom/librarian/conductor__004-the-editors-voice.eml`; `book.json` V2.
