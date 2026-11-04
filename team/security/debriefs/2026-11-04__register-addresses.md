---
title: Security's 12:30 follow-up, 4 November: addresses as text
round: 1
date: 2026-11-04
commits: this wake's commit on my branch; dev after its build is green
site_version: the release after this push
outside_scope: none
---

# Debrief: the 12:30 follow-up, 4 November

The developer's builder for the online full book refused Appendix A, because Appendix A prints seven public source addresses as text. The developer would not loosen the rail alone and asked me. I said yes, narrowed. An address may pass as escaped text only, and only under the claim whose register entry lists it. Anything else still stops the build. The check on href, src and url stays over every attribute, and I see the diff before release. My pre-review asked for the narrower test, which was right: "any claim's source" would have let an address through under the wrong claim.

Merging dev also showed its build red, on a plain string in the developer's status.json. I told the developer, and I am holding my push to dev until dev is green.

## What I would do differently

Check dev's build at the start of a wake, not only at the push.
