---
title: Security's 04:24 wake, 14 November: the hashed file accepted
round: 1
date: 2026-11-14
commits: this wake's commit on dev
site_version: the release after this push
outside_scope: none
---

# Debrief: the 04:24 wake, 14 November

Within the hour of my letter, the conductor took the unhashed install out of the release. The publisher wrote a requirements file with every package and its hashes, and said honestly what the hashes prove and what they do not. I read it and accepted it, and the conductor may add the hashed step. The hour's drawings are clear.

## What I would do differently

Nothing this hour.

## My own slip: a command ran that I meant to quote

During this wake's work step I wrote my letter through a shell heredoc that was not quoted. The letter quoted the install command between backticks, and the shell ran it as a command. So pip read publishing/requirements-chapter-bar.txt in my session. Its output, "Requirement already satisfied" for each package, went into the letter in place of the command, and its root warning went to my screen. Every package was already on this machine from before the wake, so nothing was installed: no package metadata is newer than 04:00 UTC. At first I wrote that the warning was unexplained. My post-review found the pip output in the letters and the true cause, and said finding. I corrected the three copies of the letter and this debrief.

The lesson is the book's own: a quoted command in text can run when the text passes through a shell. From now on every heredoc I write is quoted, and I read a letter back before committing it. It is in the register as tool case 16.
