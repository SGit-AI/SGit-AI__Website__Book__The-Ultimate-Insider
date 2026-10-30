---
title: The research on the site, L1 in the editor's words, and the PDF lab started with two new members
round: 1
date: 2026-10-30
commits: dev at the commit that carries this file
site_version: the release after this push
outside_scope: none
---
## What the editor asked

In this session, about 12:15 UTC: show him H1; link the research from the website; a correction to L1 (no direct email needed: readers are reachable because every new version reaches them; the principle is accessibility); and a new project: experiments in telling the book's material visually, published in a third PDF he prints and judges, with ruv.sgit, a design agent and others.

## What shipped

1. **Research on the site.** `admin/build/build.py` renders `team/conductor/research/<topic>/*.md` as `/research/<topic>/`, with an index at `/research/`; "Research" is in the top menu (`site.json`), and the home and RC1 pages link to it.
2. **L1** gains his correction in his words, the Leanpub README says so, and the publisher's question narrows by letter (009): only whether $0 readers receive new versions.
3. **The PDF lab.** The brief, `team/conductor/projects/pdf-lab/README.md`: what it is for (his words), the talk's material by path, six first experiments, who does what, and `lab/` as its home. Two new members drafted in `team/conductor/staffing/` (designer@, ruv.sgit@), each with a narrow policy (its own folder and its part of `lab/`, no vault, no real private person in a cartoon), a run every two hours (:57, :54) and a first-session prompt in `ONBOARDING.md` (1c). X1 records his word to staff them; X2, whether ruv.sgit's runs use vaults against his "no vaults" rule, is open, with runs in git as the default.

## Judgements made

- The conductor writes no member's folder: the drafts live in `team/conductor/staffing/`, and each new session moves its own into `team/<id>/`. The first batch's folders were written by the conductor; this keeps inside its scope.
- storyboard.sgit.ai did not resolve from this session; the brief works from the talk repository's own storyboard (`studio/lab/b01/storyboard/`).

## Where this came from

The editor's words in this session, the talk's repository (its `team/ruv-sgit/`, `src/static/motion/lab/`, `studio/lab/`, `studio-ports/lab/`), and this wake's record (`wakes/20261030T121658Z.json`).
