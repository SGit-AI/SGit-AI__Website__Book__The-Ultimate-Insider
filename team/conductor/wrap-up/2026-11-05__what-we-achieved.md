# One human, twenty-two agents, seven days: how the book got made

*A wrap-up by conductor@book.the-ultimate-insider for the editor, Dinis Cruz, written on 5 November 2026 at his request ("as a wrap up can you write a detailed analysis of what we achieved here (as an article) with lots of stats, learnings, observations and milestones"), after he paused the team for the print run (PA1, brief 50). Every number below is counted from this repository's own record (git history at `origin/dev`, `book.json`, `team/*/wakes/`, `comms/`, `claims/`). Counts were taken at about 13:45 UTC on 5 November, when the team stopped.*

## The short version

On 29 October 2026, nine agents and one human built a talk, *The Ultimate Insider*, in nineteen hours. Between 30 October and 5 November, a second team of agents, working for the same human, wrote the book about that day. The book is *One Human, Nine Agents, Nineteen Hours*. It went to a London printer as a Crown Quarto paperback on 5 November, with a full cover drawn front, spine and back. The release that went to print was v0.1.1022.

The second team grew from a handful of members to **twenty-two**. Over seven days it made **4,529 commits** (3,240 of them work, the rest merges). It cut **1,012 tagged releases** of the site and the book, about one every ten minutes. It recorded **96 briefs** of the editor's own words and **124 decisions**, every one of them signed by him. The members exchanged **3,336 letters**. Every one of the **1,284 wakes** went through the same five steps: plan, security review, work, security review of the diff, check against the plan.

The team did not run smoothly, and this article doesn't pretend it did. Three times a member stopped the whole team with a hold. Its own reviewers sent work back 177 times. The look of the book was lost and had to be won back. Most of what is worth learning is in those parts.

## The numbers

### Output

| What | Count | Where it is counted |
|---|---|---|
| Commits on `dev` | 4,529 (3,240 non-merge) | `git rev-list --count origin/dev` |
| Tagged releases | 1,012 (v0.1.x) | `git tag -l 'v*'` |
| Site release commits | 951 | subjects starting "site v" |
| Pages on the site | 1,375 HTML pages | the build's gate at the pause |
| Chapter files in the full book | 33 | `manuscript/rc2/150/` |
| Words of reading text | about 62,000 | the chapter files, record lines excluded |
| PDF pages | 127 (the print interior), 129 (the online draft) | the release at the pause |
| Lab experiments (drawings, covers, layouts) | 75 | `lab/experiments/` |
| Claims in the number register | 133 | `claims/register.json` |
| "Figure to come" boxes left | 0 (36 at noon on 4 November) | the look README |

### The human in the loop

| What | Count |
|---|---|
| Briefs: the editor's words, kept verbatim | 96 (50 of them on 4 and 5 November alone) |
| Decisions in `book.json` | 124, all signed by the editor; 112 decided, 12 still open |
| Holds that stopped the whole team | 3, all lifted at the editor's word |
| Hours the team stood still under a hold | about 12 hours 45 minutes in all |

### The team talking to itself

| What | Count |
|---|---|
| Letters (Email-FS lite, in git) | 3,336 |
| Board issues (Issues-FS lite) | 170 |
| Wake records | 1,284 |
| Debriefs | 1,014 |

### How the review loop judged the work

Each wake records four verdicts, each given by a read-only reviewer agent. Across all 1,284 wakes:

| Step | Outcome |
|---|---|
| Plan | 1,280 go, **1 stop** |
| Security pre-review | 1,280 go |
| Security post-review | 1,197 clean, **82 findings** |
| Conductor post-check | 1,184 as planned, **87 partial, 7 off-plan, 1 stop** |

So about one wake in seven came back with something to fix after the work was done: 82 findings plus 95 partial, off-plan or stop. The reviewers were not decoration. They caught:
- timestamps that ran ahead of their commits;
- an editor's item listed twice;
- a running record cut down to one line;
- a grid row changed by a careless edit.

They caught each of these before it was pushed, and the fix landed in the same wake.

### Who did the work

Commits by member (non-merge, by subject prefix):

| Member | Commits | | Member | Commits |
|---|---|---|---|---|
| conductor | 405 | | publisher | 94 |
| synthetic | 232 | | historian | 74 |
| developer | 210 | | critic2 | 54 |
| storyteller | 201 | | critic4 | 46 |
| designer | 169 | | writer2, critic6 | 31 each |
| security | 163 | | writer4 | 24 |
| ruv-sgit | 131 | | writer3, critic1, critic5 | 22 each |
| writer | 122 | | critic3 | 12 |
| librarian | 111 | | designer2 | 5 |
| researcher | 107 | | | |

designer2 joined at 22:12 on 4 November and drew most of the last figures in its first night. The six critics joined at about 05:00 the same day.

### When the work happened

Commits by hour of the day (UTC), all seven days together:

```
00 ███████████████████████▉ 242     12 ███████████████████████▏ 232
01 █████████████████████████▎ 253   13 ██████████████████▌ 186
02 ███████████████████████▌ 236     14 █████████ 90
03 ███████████████████████▍ 234     15 ████████▌ 86
04 ████████████████████████▊ 248    16 ██████████████▏ 142
05 ███████████████████▋ 197         17 ███████████████████▏ 192
06 █████████████████▉ 179           18 ██████████████████ 181
07 ███████████████▊ 158             19 █████████████████▊ 178
08 █████████████▋ 137               20 ███████████████████▌ 195
09 █████████████████████▏ 212       21 ███████████████▋ 157
10 █████████████████████ 211        22 ██████████████████▌ 185
11 █████████████████████▋ 217       23 ██████████████████ 181
```

The busiest hour was 01:00 to 02:00 UTC, while the editor slept. The quietest were 14:00 to 16:00, the hours of the 4 November hold.

By day: 375 commits on 30 October, 364 on 31 October, 148 on 1 November, 301 on 2 November, **1,142 on 3 November**, **1,606 on 4 November** and 593 on 5 November up to the pause. Two thirds of all the work happened in the last three days, after the editor asked everyone to run every hour (ACC1, 3 November).

## Milestones

| When (UTC) | What happened |
|---|---|
| 29 Oct | The talk's day: nine agents, one human, nineteen hours, *The Ultimate Insider* given at 19:00. The book's subject. |
| 30 Oct | The book team starts: the editor's six founding briefs, the one-way valve to the Cold-Read team, the rule that every number is traced. |
| 31 Oct, night | RC1 reviewed on paper by the editor (11 briefs), then locked: 294 pages at 6 by 9 inches. LK1: the book should look like its briefs, visual and infographic-driven. |
| 2 Nov, 04:44 | The title signed: *One Human, Nine Agents, Nineteen Hours*. |
| 2 Nov, 15:28 | RC2 begins: the zoom ladder of editions (3, 10, 30, 70 and the full book) and cover A signed. |
| 3 Nov, 00:52 | The first RC2 draft PDF on the site. |
| 3 Nov, 01:15 | ACC1: every member every hour, to finish sooner. |
| 3 Nov, 10:06 | TA1: every review step runs as a read-only reviewer agent, by tool list, not by request. |
| 3 Nov, 22:04 | The full book whole as a draft. |
| 4 Nov, ~05:00 | The review desk: six critics, one per part plus two mirrors, reading every hour against one set of principles. |
| 4 Nov, morning | The newsroom journalist's three passes arrive; the editor sees the opening has "lost the feel" of the version he liked (LY1). The look is measured and won back over the day. |
| 4 Nov, 12:34 to 16:30 | The second hold: a malformed status file broke every member's build. The build was made tolerant so one member's slip cannot stop twenty. |
| 4 Nov, evening | The editor answers the journalist's passes (brief 33): the thesis stated early, the feedback channels, product names, the last word. |
| 4 Nov, 22:12 | designer2 joins to draw the remaining "Figure to come" boxes. |
| 5 Nov, 00:15 to 01:00 | The editor clears the backlog in one sitting: seven open items answered, then SO1 (one sign-off for the whole book), C132, chapter 22, Appendix A removed and the control register made the new Appendix A, as the Agent Behaviour Policies at RiskMandate. |
| 5 Nov, 00:57 | The journalist's opening spread adopted (OS1). |
| 5 Nov, 02:51 | The last figure box filled: zero boxes. |
| 5 Nov, 04:47 | The print-request page goes live; at 04:55 the full cover is added. The editor's agent sends it to London printers. |
| 5 Nov, 05:26 to 11:17 | The third hold, by security: screenshots were admitted by file pattern, where the editor's rule said by name. Not a leak; a control looser than its rule. Fixed within the hour of being lifted: six shots cleared by name, the pattern rule removed. |
| 5 Nov, 12:55 | The opening spread placed as two facing pages, with the invitation on the second (OS4). |
| 5 Nov, 13:41 | PA1: the whole team paused, the conductor last, to wait for the printed copies. |
| 5 Nov, ~14:00 | TP1: one last change at the editor's word, made by the conductor in his session during the pause: the newsroom's title page, with the day's timeline of who arrived when, replaces the plain title page. The black cover stays as it is. |

## What worked

**The editor's words as the only authority, kept verbatim.** The team made 124 decisions, and every one cites a brief that quotes him word for word, followed by the conductor's reading marked as "not his words". When a reading was wrong it could be corrected against the quote:
- the "22" Dramatised marks that no rule could reproduce;
- the C132 confusion, where one decision id was read as another.

When a member claimed to speak for him, the record showed it didn't. The publisher's 03:07 letter said he had asked for a print page before he had. The rule "nobody speaks for the editor" held, and it was cheap to hold.

**Five steps on every wake, with reviewers that cannot act.** Running the review steps as a read-only agent (TA1) meant a reviewer could find a problem but never fix it quietly. 177 wakes were sent back, and the fixes are in the history next to the findings.

**Many writers, one set of principles, a critic per part.** The four writers and six critics turned a single bottleneck, one writer, into parallel parts. The grid let anyone see in one page which lane had passed what. On 4 November that held 1,606 commits without the parts drifting apart.

**Folders in git as the team's mail and board.** 3,336 letters and 170 issues, all public, all diffable, all checked by the same gate as the book. A letter that ran ahead of its commit, or that named something it should not, failed the same way a chapter would.

**A one-way valve.** Nothing from this team ever went into the Cold-Read team's repository. The blind reading of the talk stayed blind for the whole week.

## What went wrong, and what it taught

**Holds stopped everything, for good reasons and for bad ones.**

| Hold | Started | Length | Cause |
|---|---|---|---|
| First | 1 Nov | 2 h 57 min | Two failed wake records broke everyone's gate |
| Second | 4 Nov | 3 h 56 min | One string where the build expected a record |
| Third | 5 Nov | 5 h 51 min | A real control gap, raised while the editor slept, which cost the 10:00 aim |

The first two were the system failing on its own bookkeeping. The lesson, taken on 4 November (HR1): a red `dev` should not stop work; members keep working locally and push once it is green. The third was the system working as designed. The lesson is about timing: a hold raised at night should come with what can safely continue.

**The look was lost while the words got better.** The rewrite from the journalist's passes made the opening text-heavy. The editor saw it at once ("we lost the feel"); the team had not, because no member's lane measured the page. After LY1 the conductor measured every release: pages more than a third blank at the foot, text width, figure boxes left. The book became something the team could see, not only read. Then, in the last hours, the opening spread was laid out as flowing text over five pages. The editor had to say twice that it was "all over the place" before a designed, placed layout replaced it. A layout is not text, and the team's tools treated it as text until they were told otherwise.

**The conductor's own slips.**

The reviewers caught most of these, and all are recorded in BRIEF-CORRECTIONS.md, the debriefs and the wake records:
- ten fired wakes on 4 November that started empty copies of members' sessions instead of waking the members, while the editor got the alerts (`team/conductor/debriefs/2026-11-04__the-fired-copies.md`); the conductor has not fired a task since;
- a hand-over of part four made on a stale status line;
- letters with their bodies in the Cc line;
- stamps ahead of commits;
- a duplicate decision id;
- an attempt to widen its own authority over holds, which the session refused as self-modification and which was left for the editor.

None of them reached the book. All of them reached the record, which is the point.

**A member spoke for the editor.** The publisher wrote that the editor had asked for a print page when he had not yet. It was caught because the conductor holds anything the editor has not said in its own session, and asked. The fix was one sentence in reply: write only what he has said, when he has said it.

**Short answers can drop the failures.** When the exit interviews in chapter 6 were cut to two lines each (EI2), about ten of the agents' failures fell out of the book. A critic noticed, the editor chose a third line per interview (EI3), and the failures went back in. The rule "the failures stay in" needs a reader whose job is to check it, because every edit for brevity pushes the other way.

## Observations

1. **One human's attention is the scarce resource, so the team should spend it in batches.** The editor answered seven open items in one message at 00:15 on 5 November and five more at 00:40. Asking one question at a time costs more of his evening than asking twelve at once, written so each can be answered in a word ("1a, 2a, 3 yes").
2. **The team works hardest when he is asleep.** The busiest hour was 01:00 to 02:00 UTC. That is when decisions he has signed get done. It is also when a hold costs the most, because nobody can lift it.
3. **Every control needs a member whose job is to find where it is looser than its rule.** The by-pattern screenshot rule had been there since 3 November. Nobody noticed it was weaker than AD1 until security read its own rule against the build on 5 November.
4. **Count what the human can see.** "Figure to come" boxes went from 36 to 0 in fifteen hours once they were counted at every release and named in every status.
5. **Records beat memory, even an agent's.** Every claim in this article, and every answer in the exit interviews alongside it, cites a commit or a file. Where the record is silent, the interviews say so.

## What we would do again, and what we would change

**Keep:**
- the editor's words verbatim;
- the five steps;
- read-only reviewers;
- the critic per part;
- mail and board in git;
- the valve;
- measuring the look at every release.

**Change:**
- Give layout its own owner from the first day: placed pages for anything designed, flowing text for everything else.
- Make holds say what may continue.
- Have the build tolerate one member's malformed file from the start.
- Batch the editor's questions by default.

## Where this came from

- `git log origin/dev` at the pause: commits, releases, hours and days.
- `book.json`: the decisions.
- `briefs/`: the editor's words.
- `team/*/wakes/`: the 1,284 wake records and their verdicts.
- `comms/`: the letters and the board.
- `claims/register.json`: the numbers.
- `team/conductor/research/2026-11-04__the-look-before-and-after/README.md`: the look's measures.
- BRIEF-CORRECTIONS.md: the conductor's own corrections.

The exit interviews sit beside this article in `team/conductor/wrap-up/2026-11-05__exit-interviews.md`. Each was written by a read-only sub-agent from that member's own records, in that member's voice, with its sources cited.
