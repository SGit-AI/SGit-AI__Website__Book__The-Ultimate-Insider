---
title: Porting the talk team's machinery, and the first batch
round: 0
date: 2026-10-30
commits: this wake's commit on dev
site_version: the release after v0.1.0
outside_scope: 6 folders, named: team/librarian, historian, security, researcher, storyteller, publisher
---
## What was asked

The editor, in this session: the book team's machinery "needs to be replicated as accurate as possible on both repos", starting here with the conductor's key and "the pages + prompts for the first batch of agents".

## What was done

- **Ported from the talk's repository at `298be4e`**, not redesigned: `admin/tools/` (start, banner, wake, vault check and handover, the pinned key tool), `admin/build/agents.py`, the talk's `build.py` and `validate.py` with only the talk's own parts removed, `WAKE.md`, the four review briefs, the known keys, the site's stylesheet, scripts and vendored vault readers, the admin section, and `CLAUDE.md` rule for rule.
- **The conductor's key**, made in this session with the pinned tool: `sha256:15762445fb34548e`, encryption `sha256:7b773c490ca3da15`. Private halves in `~/.sg-send/` only.
- **The first batch, proposed**: librarian, historian, security, researcher, storyteller, publisher, each with `ROLE.md`, `policy.json` (status proposed), `status.json` and an hourly slot; their prompts in `ONBOARDING.md`. No scheduled task created: the editor says go and sets the hours (Q2).
- **Decisions recorded**: S7 (the book reads the talk's repository as it grows; the Cold-Read team stays pinned) and S8 (every team runs on the talk team's machinery).

## What went wrong, and what was found

- **This wake started before the five-step machinery existed**, because building it was the work. The plan and the pre-review were recorded after the work, and say so.
- **The first pre-review said change**: the six member folders are outside the conductor's `scope.writes`. The plan was amended to name them and what covers them, and the second pre-review said go. The conductor did not widen its own policy to claim them, so `agents.py overlaps` stays clean when the members join.
- **`vault_check.py` would have flagged every one of our agent addresses** as an email, because `@book.the-ultimate-insider` has a dot after the @ and the talk's addresses did not. Fixed for our domain only.
- **The talk's markdown renderer cannot bold text that contains code**; the talk's own pages show stray asterisks for it. Worked around here by rewording, not by changing the shared renderer.
- **The post-check found three pieces not ported and not explained** (`lock.py`, `workflow_deck.py`, `pace.json`); `REALITY.md` now says why.

## For the editor

1. Confirm the first batch and its policies, then start a session per member with its prompt from `team/conductor/ONBOARDING.md`.
2. Q2, the hours; then go on the schedule.
3. `CLAUDE.md` and `WAKE.md` are now the talk team's rules for every member here: read them once.
4. The team's two public vaults and your lane, when you can create them; and re-confirm the DC Vault Registry key carried over.
