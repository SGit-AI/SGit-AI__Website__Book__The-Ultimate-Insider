# A team of agents made a talk in a day

At 00:16 on 29 October 2026 I created an empty repository (C001). By the evening a team of nine agents and one person, me, had built a talk of 58 beats, the slides that carry it, the player that runs it and the site around it (C011, C015). By 18:46 the repository held 814 commits, 603 of them by the agents (C004, C003). At seven that evening I walked on stage in London and gave the talk, for about 87 minutes, with questions from the room (C069).

What the team made is open, so you can look at it and copy it.

{width: 38%}
![The talk's player: 58 slides as web pages, with a timer and the speaker's notes behind one key](sample/images/talk__player.jpg)

{blurb, class: information}
**Words on this page**

An *agent* is an AI that works in a loop: it reads, decides, acts with tools, and reads the result. A *repository* is a folder that remembers every change. A *commit* is one saved change, with who made it and when.
{/blurb}

{width: 15mm}
![Scan to open the talk's site](sample/images/qr-talk-site.svg)

*Where this came from:* the talk's repository at `298be4e`; C001, C003, C004, C011, C015, C069; the length from the transcript, added after the day.

# A book about you doing it

This book is one of a series: *Generation ZX Founders (GenAI Edition)*, Gen ZX Founders for short, and its line is "For the ones already up at three in the morning building".

The series has one idea. You start, and you build. Every book in it is a working example you can copy, not a story you only read. This one is about an agentic team: a presentation, made by agents, that you can make too.

Generation ZX is not a range of birth years. It is the people building because finally they can. We see it most in Generation Z and Generation X, side by side in the same room, as they were in Faro: the youngest and the most experienced, building together.

So read this book as a book about you doing it. It is about you starting, and building what I built here.

*Where this came from:* the series' own site, gen-z-developers.sgit.ai (its name, its line and the sentence on Generation ZX are mine, from there; read on 31 October 2026); my brief of 31 October to the book's team.

# What they made

The talk is a website. Every slide is a page that moves. The player has a timer, a slide grid and the notes I read from. The home page puts the whole argument in one picture: three circles, the insider, the infrastructure and the decision, with the scenario where they overlap.

Around the talk the team built the things a talk usually does not have. Maps of the argument, drawn as Wardley maps. Animations, each with an explanation, frame by frame. Articles that tell the night hour by hour. A studio where every slide was tried in several versions, side by side, and the best one promoted into the talk.

None of it was planned that way at midnight. It grew because each agent had a job, and the jobs asked for it.

{width: 80%}
![The talk site's home page: the argument in three circles](sample/images/index.jpg)

*Where this came from:* the talk's site at `298be4e`, read page by page by the book's librarian (the book's `index/talk-site/`).

# How you can see everything they did

The team left a record of every step. Not because I asked for a diary, but because the way it worked made one. Every turn of work wrote down its plan, its review and its result. Every release was numbered by the build, not by a person. Every note one agent left another sits in the history, with its time.

Here is one, from 18:39, minutes before I went on stage. The conductor wrote: "part 1 not yet locked, unchanged since 18:30; dev asked to lock it now", and to dev: "run lock.py --part 1 now" (`2ed6427`).

That is the whole of it. You do not need to trust what I tell you about the day. You can open the day.

By 18:46 there were 814 commits and 210 releases, each one a version you can open and check (C004, C009).

![The team's dashboard, as the talk's site shows it](sample/images/admin__dashboard-top.jpg)

{blurb, class: information}
**Words on this page**

A *release* is a numbered version of the site, made by the build every time a change passes its checks. A *wake* is one turn of work by one agent.
{/blurb}

*Where this came from:* commit `2ed6427` (18:39:16), its subject and its note to dev, quoted as written; the claims C004 and C009. The pages that show keys are left out on purpose.

# Meet the team

Each agent had one job, written down, like a cast. The conductor came first: it kept the time and the plan, and it was the one that stopped everything at the end.

Nine agents (C011). And me: I wrote the briefs, I made the decisions that mattered, and I gave the talk. Nobody else in this book speaks for me.

![The cast: nine members, one line each, in the talk's own words](sample/images/cast-row.svg)

*Where this came from:* each member's role file in the talk's repository at `298be4e`, and its Meet the team piece; the claim C011. The drawing is the designer's (the book's `lab/experiments/22-designer-t10-drawings/`).

# How a day runs

The team worked in turns, on a clock, and through the night. Some turns started on their own schedule; some started because I asked for something.

In the night, before six in the morning, 182 commits were made, 61 of them the build's releases (C092, C095). Over the whole day there were 162 wakes: 105 on the schedule, 47 started by me, and 10 follow-ups (C087). From five in the morning to two in the afternoon I started none of them: every wake ran on its own schedule (C087).

Every turn went the same way, in five steps. Plan the work. Have the plan checked. Do the work. Have the work checked. Check it went to plan. A turn that skipped a step was not meant to close.

![Every wake of 29 October as a dot, by what started it; the night shaded to 06:00; the hold at 18:44](sample/images/day-timeline.svg)

{blurb, class: information}
**The five steps of a wake**

Plan; review the plan; work; review the work; check against the plan. The reviews are done by two more agents, each briefed for its check, and each writes its verdict down.
{/blurb}

*Where this came from:* the claims C006, C073, C087 and C092; the team's wake protocol (`team/conductor/WAKE.md` in the talk's repository). The timeline is the designer's, drawn from the record.

# The rule that let them go fast

Anyone on the team could stop everything. Only I could start it again.

At 18:44, sixteen minutes before the talk, the conductor did, at my word: it wrote a short file called a hold, and every wake that started after it stopped at once (C006, C024). The work already in flight still landed: one commit eighty-two seconds later, and the last release of the day (C005, C065). Then the day was done. It was the only hold of the day.

That is the talk's argument in one rule. Brakes are what let you go faster. A team you can stop with one file is a team you can let run through the night.[^why]

[^why]: Three accounts, all kept. On the day, the hold gives my usage limit, at 95%, as the reason. Two days later I said the 95% was just a footnote: the real reason was that there was no tested way to take in changes during the talk. The same evening I remembered the 95% as the token usage; the record holds the percentage, not what it measured (C089, C021).

{blurb, class: warning}
**Watch for this**

A brake only works if it is easy to pull and nobody can take it off but you. Write down who may stop the work, and who may restart it, before you need to.
{/blurb}

*Where this came from:* the hold, committed at 18:44:13 (the claims C006 and C024); what landed after it (C005, C065); the accounts of why (C089), the later two given on 31 October.

# What did not work

It was not magic, and it was not finished. The talk needed more rounds than one day gave it.

Some of the talk's own claims did not hold. The team kept a register of every claim the talk made: 320 in all. 52 were never checked. 210 held whole. 3 did not hold, and none of those three reached the stage (C029, C030). But one figure the register had already found out of date did reach a slide (C031).

That is in the book on purpose. The checks worked, and they also missed. Saying where they missed is part of the method, not a footnote to it.

{blurb, class: discussion}
**The number: the talk's own register**

320 claims; 52 not checked; 210 held whole; 3 did not hold, none on stage; one out-of-date figure did reach a slide. (C029, C030, C031)
{/blurb}

*Where this came from:* the claims C029, C030 and C031 in the book's register.

# Why this matters to you

You do not need to write code to work like this. You need a clear brief, rules in plain words, a loop, and the habit of shipping something somebody else can use.

That is what I told a room in Faro on 31 October, at the Vibathon Algarve, a sold-out day of building with AI (C091): "build something that somebody else can use, and then you rinse and repeat. That's it. That's literally the loop."

The team in this book ran that loop again and again, all day, with agents doing most of the building. My job was the brief, the decisions, and the brakes.

![The loop: build, ship, learn, repeat, with the team inside it](sample/images/loop.svg)

*Where this came from:* the newsroom's article "Vibathon Algarve 2026" (newsroom.sgit.ai, 31 October 2026), which quotes my words to the room; the claim C091.

# Start tomorrow

Five steps.

1. **An account and an empty repository.** A public repository is public forever, so nothing private goes in it: no password, no key, no personal detail. And give the agent only the access it needs.
2. **One agent first, the conductor**, with one page of rules in your own words: what it is for, what it may change, and when it must stop and ask you.
3. **One brief**: what you want made, for whom, and by when.
4. **Ship something end to end on the first day**, however small, that somebody else can use.
5. **Add a second agent only when the first is busy.**

{blurb, class: exercise}
**Try this**

Write the one page of rules for your first agent tonight. Three headings are enough: what it is for, what it may touch, and when it stops.
{/blurb}

*Where this came from:* the order the team itself was set up in on 29 October, from the talk's repository; the safety line is the lesson of the team's own first night.

# Where this book goes next

The rest of the book walks the same path, in detail. The tour of what the team made. One agent, and how it was set up. A team that grows. The plumbing that keeps it true. The talk, and how a team like this was contained. And then your turn.

![The book's six parts as stops on a line, and where these pages sit](sample/images/book-map.svg)

Every number in it comes from one register, each with its id, and each can be checked against the repository. You do not have to trust the book. You can check it.

{width: 18mm}
![Scan to open the book's site](sample/images/qr-book-site.svg)

*Where this came from:* the book's plan as it stands on 31 October 2026 (its structure is still open); the register of claims in the book's repository. The talk's repository is pinned at commit `298be4e`; this sample was written on 31 October 2026.
