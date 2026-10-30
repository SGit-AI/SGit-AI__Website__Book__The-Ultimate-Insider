---
title: The talk's site, first pass: 303 pages, 90 screenshots, the best fifteen
round: 2
date: 2026-10-30
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none
---
## What was asked

The conductor's letter 007, relaying the editor (about 13:08 UTC): go through the talk's website properly, every page, the admin side above all; what was made, what works, what does not; the visuals the book could reuse; screenshots for the designer; all in `index/talk-site/`, with a README that leads with the twenty best things.

## What was done

- **A crawl of the published site** with a Playwright script of my own: 303 pages reachable from the home page, each with status, title, words, images and browser errors (`index/talk-site/crawl.json`).
- **`pages.md`**: every page by section, its verdict, its source file in the talk's repository and its last change. 298 work; five do not or half-work, each because of another service.
- **`visuals.md`**: 63 slides, animations, maps and ports, with source.
- **90 screenshots** in `shots/` (6 MB), for the designer.
- **README**: the best fifteen so far, from what I actually looked at; the twenty wait for watching each animation in motion.
- **Reply** to the conductor: `comms/mail/mailroom/conductor/librarian__003-talk-site-first-pass.eml`. RC1's sources: unchanged since 14:20, no rerun needed.

## What was hard

- **The local build was refused.** This session's permission check would not run the talk repository's build script, code from another repository; I did not work round it. The published site is `298be4e` plus three commits added after the day, so the crawl is close to the pin and says where it is not. A build at the pin itself needs the editor's word in a session allowed to run that code.
- **A crawler's failures are not the site's.** Four pages' GitHub panels failed on the API's rate limit, which is likely this container's address; the README says so rather than calling them broken.
- **The site is still live.** Its dashboard shows the talk team's last hold of the night: a reader today sees the state the team stopped in.

## For the editor

Nothing waits on you. If you want the site as it stood at `298be4e` exactly, built rather than browsed, that needs your word in a session that may run the talk's build code.

## Where this came from

`comms/mail/mailroom/librarian/conductor__007-talk-site-study.eml`; https://the-ultimate-insider.presentation.sgit.ai/ (release v0.2.1), crawled 30 October 2026 at about 16:20 UTC; the talk's repository at `298be4e` and `424b67a`; this wake, `team/librarian/wakes/20261030T161218Z.json`.
