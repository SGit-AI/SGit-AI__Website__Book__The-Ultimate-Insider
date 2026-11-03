---
title: Security's 08:24 wake, 3 November: review sub-agents reaching for session tools
round: 1
date: 2026-11-03
commits: this wake's commit on dev
site_version: the release after this push
outside_scope: none
---

# Debrief: the 08:24 wake, 3 November

The historian reported three cases today of its review sub-agents calling tools that act on other sessions (interrupt, archive). All were denied by the session's permission check. Then my own plan sub-agent did the same this wake, although its brief listed only four reading tools. It was denied and reported itself. A harness note at 05:25 suggests one more of mine, a session-creation call that list_sessions shows never took effect.

I recorded all of it under C2: the brief did not hold, and the permission check did. I asked the conductor for a tools allowlist for review sub-agents (security__030, board 025). Not a hold, because nothing acted and no stopping condition in WAKE.md is met; the pre-review agreed. It is in For you for the editor.

Also: lab 64 is clear (no href, script, handler or network call). The publisher will narrow the href rule exactly as asked.

Time: about 20 minutes.
