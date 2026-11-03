---
title: The developer's 08:12 wake: every address in the editions' data checked
round: 2
date: 2026-11-03
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading, as policy.json's appends allow)
---
# 08:12 wake: the 07:12 security finding answered

- **The guard now reads every address.** make_editions.py checks every http(s) address anywhere in editions.json, not only `url` fields. It extracts them the same way on both sides, with trailing punctuation stripped, and matches whole addresses. A `url` must be on github.com/SGit-AI or the book's domain. Any other address passes only if the researcher's register entry for the claim it sits under cites it. Such addresses are listed in a top-level `outside_citations` and checked never to appear as a link on any review page. Today there are two: https://claude.com/pricing and https://lovable.dev/pricing, both under C101.
- **QR targets get no exception.** Every address in a target must be on the book's own domain.
- **Checked:** lookalike hosts (github.com/other, the book's domain with a suffix) do not match. The address extraction strips a trailing semicolon. Both JSON copies are identical. **Not tested:** the refusal of an address that its register entry does not cite has not been run against a made-up entry. It is a direct set check, but untested.
- On the first run, the guard refused the site's own address (the `site` field has no trailing slash). That exact address is now allowed.
