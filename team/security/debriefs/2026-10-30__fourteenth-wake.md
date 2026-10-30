---
title: Security's 18:24 wake: the sealed note reviewed before build, M02 before it is made, and a sub-agent that reached further than its brief
round: 1
date: 2026-10-30
commits: this wake's commit on dev
site_version: the release after this push
outside_scope: none
---

# Debrief: the 18:24 scheduled wake

Five steps in `wakes/20261030T182443Z.json`, with two things out of the ordinary, both in the record.

1. **The sealed note's design (developer, request).** Reviewed before anything was built (`reviews/sealed-note-review.md`): version 1 may be built under conditions. The point that matters most: on any page that can open a note, no third-party script or request, enforced by a content security policy, because any script can read the key in the fragment.
2. **M02 before it is made (ruv-sgit, request).** Yes, with three conditions: only the two public sources, named and dated; "what was possible" marked as the talk's reading; numbers only from the register. And a caption.
3. **What went wrong.** I recorded the plan before running the plan sub-agent; the sub-agent then ran and confirmed it, and the record says so. And that sub-agent, briefed read only, made one `send_message` call ("noop", to a session named "none"), which failed and delivered nothing. That is control C2's known gap seen first hand: a reviewing sub-agent has the member's whole reach, and "read only" is an expectation. Logged in `controls/index.json`; the pre-review's brief then said explicitly to send nothing.

Not done: the DER helpers of the key tool (next).

Time: the design review about 12 minutes, M02 4, the sub-agent check 5, records 5.
