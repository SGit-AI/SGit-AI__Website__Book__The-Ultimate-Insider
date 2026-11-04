# What each of the editor's afternoon asks built, and when the work landed

Kept by historian@book.the-ultimate-insider. Written 4 November 2026 at the conductor's request (`conductor__035`), for the card "His afternoon asks" in the full book's chapter 2. Read only, from the talk's repository at `298be4e` (the day's record, to 18:48; nothing after it). **These numbers are the historian's proposals: the researcher registers them, ruv-sgit draws them.** All times are UTC, to the second from the commit.

## The trap, and how the table avoids it

`lab/experiments/29-ruv-the-afternoon-loop/data/asks.json` gives, for each ask, the editor's own time (from the commit subject, to the minute) and the commit's time. For four rows (`a618b29`, `7c91afc`, `d252155`, `93f4191`) that commit is **the conductor routing his word**: a brief file, a line in `pace.json` and a wake record, with no product in it. The ask-to-routing times are 2 min 41 s, 3 min 7 s, 4 min 22 s and 3 min 46 s. The work landed later, in other members' commits, so the table measures from his ask to **the work**. For the four player rows the commit is the work itself.

## The rule for "major", stated before it is applied

A change is **major** if its commit adds a new slide or page (a new `index.html` under `src/`), or changes at least 100 lines of product files. **Product files** are everything outside `team/` and `REALITY.md`: slides, pages, the player, the build, talk data, evidence data. A brief, a wake record, a status file or a debrief is the team's record, not a feature. Evidence data is not a feature either: it is flagged "evidence". The 100-line line is the historian's choice, not the editor's; a different line moves rows 6 to 8 and the player rows, nothing else.

## The eight asks of the afternoon

| # | He asked (his time) | What the work produced | Where the work landed (UTC) | From his ask to the work | Size of the work (product files; lines) | Major |
|---|---|---|---|---|---|---|
| 1 | 17:27, "when in doubt add it" | Deck placed 11 pieces in the talk: 47 beats became 58. Eight come from the conductor's gap list (the PKI, the journey, four SHarness pieces, the brakes, the collision); two are motion's new pieces for part 1; one is studio's policy review page. Routed at 17:29:41 (`a618b29`) | `b1c9bab`, 17:52:15, deck | 25 min 15 s | 1 file (`talk.json`); +138 -6 | yes: 144 lines |
| 2 | 17:30, the team's own policies and his review page into the ABP section | Studio's showcases of the policy review page (17:47:28), then of the policy in prose and the five steps of a wake (18:11:59). Only the first was placed in the talk before the hold: deck's `b1c9bab` (17:52:15) added it. The other two (the policy in prose, the five steps) were built and not placed. Routed at 17:33:07 (`7c91afc`) | `bd3cdad`, 17:47:28 (page built); `b1c9bab`, 17:52:15 (placed); `95b09d9`, 18:11:59 (pages 2 and 3 built, not placed) | 17 min 28 s to the first page; 22 min 15 s to its place in the talk; 41 min 59 s to pages 2 and 3 | `bd3cdad`: 5 files (3 new); +69. `95b09d9`: 8 files (6 new); +132 | yes (new pages) |
| 3 | 17:35, "go build": the open source model, security products as targets, inline agents, investors | Studio's showcases "where to invest in sgit" and "the fork next door" (18:20:06), then "open source is a strategy" (18:34:32); the researcher's evidence for open source, investors and security products in PHP October (18:23:50). None of the three showcases was placed in the talk before the hold. Routed at 17:39:22 (`d252155`) | `511606d`, 18:20:06; `d7df71a`, 18:23:50 (evidence); `040233f`, 18:34:32, all built, none placed | 45 min 6 s to the first showcases; 48 min 50 s to the evidence; 59 min 32 s to the third showcase | `511606d`: 8 files (6 new); +231. `040233f`: 5 files (3 new); +139. `d7df71a`: evidence, 23 files; +3165 | showcases: yes (new pages). Evidence: not a feature |
| 4 | 17:45, how we keep it safe, in "how this was made" | The researcher checked the claims in the brief against the record: nine checked, four to correct (18:14:30). No slide or piece for it exists in the repository at `298be4e`. Routed at 17:48:46 (`93f4191`) | `7323986`, 18:14:30, the claims check only | 29 min 30 s to the check; no piece landed before the hold | 1 file (a note); +19 | no |
| 5 | 18:05, the player: back steps across slides, no countdown per slide, 90 minutes, a full reset | The player's four behaviours changed | `23739cc`, 18:04:48 | at his minute (12 s before 18:05) | 3 files; +25 -8 | no: 33 lines |
| 6 | 18:10, the player: a step never stops the play; the right arrow plays each reveal; the cache answers in 3 s | Three behaviours of the player and the cache | `12e93db`, 18:14:14 | 4 min 14 s | 2 files; +20 -6 | no: 26 lines |
| 7 | 18:15, the player: the release on the bar; the bar fits an iPad on its side again | Two fixes to the bar | `013d97e`, 18:15:58 | 58 s | 1 file; +3 -1 | no: 4 lines |
| 8 | 18:25, the player: two back steps in a row while playing; the first slide opens built | Two fixes | `dbd75ad`, 18:37:02 | 12 min 2 s | 1 file; +8 -3 | no: 11 lines |

## Two larger asks of the afternoon, from the feedback round

The round's own first line dates it "about 13:50" (committed 14:07:04, `c9ced4e`), and the record gives no minute for its separate items, so these two start from that time.

| He asked | What the work produced | Where it landed | From about 13:50 | Size | Major |
|---|---|---|---|---|---|
| a feedback pane on every page, so he could send notes from the browser (the conductor's notes of 14:05 put it first) | The pane and its lane, with voice, and a GitHub star | `9a51c28`, 14:28:47, dev | 38 min 47 s | 7 files (3 new); +372 -1 | yes (new files; 372 lines) |
| the player, from the earlier site, working on an iPad: "the main priority" | The player ported, with a countdown against his time, then its build mode for his running order at 15:16:48 (`f20cfa8`; +177 -5, 3 files) | `3314ffe`, 15:07:08, dev | 77 min 8 s | 2 files; +629 -209 (838 lines changed) | yes: the afternoon's largest change, a port that rewrote the player |

## What the table says, for the card

- **The four player rows are small** (4 to 33 lines each) and fast (under 15 minutes; row 5 inside his own minute). The four routed rows are the big ones, and slower: 17 to 45 minutes from his ask to the first work (the last showcase came 60 minutes after its ask).
- **The routed asks built six studio showcases and put eleven beats into the talk** (one of the eleven is the first of the six showcases). Five of the six (the two ABP showcases on prose and the five steps, invest, fork, open source) were built and not placed before the hold at 18:44:13; deck's 18:20 wake had recorded its plan for parts 2 and 3 and never closed.
- **The 17:45 ask built a checked list of claims, and no slide or piece.** That is a true row and the card should show it as one.
- **The commit that C105 calls "landed" for rows 1 to 4 is the routing.** The ask-to-routing times (2 to 4 minutes) are real but are not the work; the register's reading should say which it means.

## How to reproduce

For a row's size, in a clone of the talk's repository: `git show --numstat --format= <hash>`, then drop the rows under `team/` and `REALITY.md`; sum the rest. New files: `git show --name-status --format= <hash>` (lines starting `A`). Beats added by `b1c9bab`: the ids in `src/static/talk/talk.json` at `b1c9bab` against `b1c9bab^` (47 and 58). Not placed: `talk.json` at `298be4e` holds no path for `abp-prose`, `abp-enforcement`, `lab/invest`, `lab/fork` or `lab/open-source`, and holds `abp-review`. No piece for the 17:45 ask: no file under `src/` at `298be4e` is named for it, and motion's status at `298be4e` lists M01, M02 and M03 and "parts 2 and 3 next", not that piece.
