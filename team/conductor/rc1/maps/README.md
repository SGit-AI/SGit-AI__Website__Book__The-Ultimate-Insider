# The book's Wardley maps

The illustrator, for RC1, 30 October 2026. The editor asked for "a lot of Wardley maps ... from simple to more complex", rendered as images and introduced early, because they underpin the book (`briefs/2026-10-30__in-session/01-principles-maps-and-the-plumbing.md`). There are sixteen maps here, in reading order. Each one has a JSON source in this folder and a PNG at `../resources/images/maps/<nn>-<slug>.png`, 1600 px wide and sized to read at the 6 x 9 inch text width. No chapter has been edited: the writers place the maps. A suggested place is given for each one.

**How to read them.** The vertical axis is the value chain: the user at the top, and lower down whatever the user relies on without seeing it. The horizontal axis is evolution: genesis, custom built, product, commodity. Lines mean "needs". A dark dashed arrow shows where a part is heading. A dashed grey ring with an arrow shows where a part stood before. A black bar on an arrow is inertia. A hatched dot is "inside", and the legend on each map says inside what. A square is a setting (enforced by a tool) and a circle is an expectation. Positions are readings of the record, not measurements, and every map says so where that matters.

**Rules kept.** No number appears on a map unless it comes from the register or the chapters. The only count used is "nine staffed agents" (C011). Times and commits come from the record. No vendor or model is named, at the conductor's word: the maps say "AI coding agents", "agent sessions", "the code host" and "hosted CI". git and pandoc are named because they are open tools, not vendors. The talk's own maps keep their labels, which name only the editor's projects (SGit, Sharness.ai). Arrows and shading are dark dashes and hatching, so they survive a black-and-white print. Red is used only for the italic notes.

**Rebuild.** `python3 team/conductor/rc1/tools/wardley.py <map>.json` writes the SVG (the renderer is improved for print: larger type, wrapped labels placed clear of lines, a white halo behind text, notes, inertia, flows, zones, bands, legends). Then `node team/conductor/rc1/tools/wardley_png.js <svg> <png>` writes the PNG with Playwright.

## Part 1. Learning to read a map (chapter 0, a new section "How to read a map", after "Explorer, villager, town planner"; or a short chapter of its own between 0 and 1)

| # | File | What it shows | Where |
|---|---|---|---|
| 1 | `01-a-need-and-two-parts` | The value chain alone. The user (the editor), the need (a talk on stage at 19:00, London) and two parts that meet it (slides, a player). There is no evolution axis yet. | Chapter 0, the first map in the book |
| 2 | `02-the-two-axes` | The same world with evolution added: the talk is genesis, the slides (made from the talk as data) and the site are custom built, the player was ported from ruv.sgit.ai, and CI, hosting and git are product and commodity. Each stage has a short line saying what it means. | Chapter 0 |
| 3 | `03-everything-moves` | Movement. An agent team with mandates, the gate and release pipeline, and AI coding agents all move right. The note says the team's machinery was ported, rule for rule, to two more teams after the day (S8; chapter 12). | Chapter 0 |
| 4 | `04-build-buy-and-inertia` | Build in genesis and custom, buy or rent in product and commodity. Inertia is shown with the editor's own word for it, "attrition", from his answers of 17:15 in the talk's record: changing how people work is hard. The example is behaviour policies, the team's mandates. | Chapter 0; chapter 3 may point back to it |

## Part 2. The day, and the years behind it

| # | File | What it shows | Where |
|---|---|---|---|
| 5 | `05-the-day-as-a-value-chain` | 29 October as one value chain: the editor; the talk; the site and player; nine staffed agents (C011) with the security member drawn as a ghost (proposed, never staffed); the rules and record; the five-step wake, holds and signed decisions; the tools written on the day; the gate and release pipeline; the public vaults; session keys; scheduled tasks, agent sessions and the editor's usage; the code host and git. Note: what the editor saw was new on the day, and what it all stood on was rented. | Chapter 1, where the camera pulls back to the whole day |
| 6 | `06-the-plumbing-under-the-day` | The plumbing, split three ways. Hatched: what the editor made before the day and brought to it (the newsroom's way of working, start and end banners, CI owns the version, the Issues-FS board and Email-FS mail, the sgit vaults, pki-agent keys). White on the left: written on the day (the five-step wake, start.py, wake.py, agents.py, lock.py, the gate). Right: rented. | Chapter 2 (what went into the empty repository first), or the plumbing section the editor asked for |
| 7 | `07-one-piece-leads-to-the-next` | The years before the day, read from the editor's brief of 30 October. The Cyber Boardroom is where the work began. The newsroom flow, Issues-FS and tagging, and the gate with CI owns the version all moved from genesis to custom built. First experiments with AI coding agents led to sgit, and sgit led to SHarness ("far faster to build"). Memory-FS and Type_Safe are shown without links, because they are not in the day's record: they reached it as learnings. AI coding agents are shown moving towards commodity. No span of years appears on the map, because that number is not in the register. | Chapter 2, or the plumbing and principles section the editor asked for |

## Part 3. The argument, beside the workflow (the talk's maps, rendered fresh for print)

Maps 8, 9, 10, 15 and 16 are the talk storyteller's five maps (`team/storyteller/maps/*.json` at `298be4e`). Their labels and positions are unchanged. Each JSON carries a `source` field naming its original.

| # | File | What it shows | Where |
|---|---|---|---|
| 8 | `08-talk-the-protection-stack` | The talk's map 3. Roles and permissions are a commodity built for limited insiders. What agents need is in genesis: measured reach, the Agent Behaviour Policy (reach, mandate, gap), behaviour policies and a suspendable licence to operate. | Chapter 3 (the ABP), with a pointer from chapter 6 (licence) |
| 9 | `09-talk-outside-and-inside` | The talk's map 1. The outside is mature and the inside is not; agents are the new insider. The storyteller's own second pass (R5) asked that "attacked for decades, evolved" be read as "attacked hard, so watched and patched". | Chapter 5, replacing `05-map-outside-inside.jpg` at print quality; also chapter 9 (the `inside` beat) |
| 10 | `10-talk-spreadsheets-to-applications` | The talk's map 2. Explorer coding swaps a commodity spreadsheet for a genesis app, many times over. Security for each new app starts in genesis. | Chapter 7 (the `spreadsheets` beat) |

## Part 4. The controls, and the teams after the day (the most complex maps)

| # | File | What it shows | Where |
|---|---|---|---|
| 11 | `11-two-brakes` | The evening's brakes. The editor's usage limit leads to the hold (18:44), and through start.py the hold stops the next wake. The talk in three parts leads to part locks (lock.py, 17:54), which never closed, and a dashed arrow shows the hold stopping the lock too. Also shown: the overnight freeze (02:47), which held and cost a correction; the hourly rhythm, relaxed for the night; the five steps and the gate, which held. | Chapter 8 |
| 12 | `12-the-controls-on-one-map` | Control register C1 to C10 on one map. Settings are squares and expectations are circles, placed below the team's reach (any file, a push to dev, a key in any name). C1 to C8 sit inside the repository, where a member's commit can change them. C9 and C10 sit outside it. C2 is shown moving right because it was ported to two more teams. Kinds follow chapter 9's table and `controls/index.json`. | Chapter 9, after "The register" |
| 13 | `13-the-book-team-and-the-cold-read-team` | Two teams and one record. The book's team (hatched) reads the record, its own register and the material added after the day (`a9c0b49`). The Cold-Read team reads the record and nothing else. Cold-Read findings flow to the book one way only. The hand-off crossed once (`team/conductor/handoffs/`). Both teams run the talk team's machinery, ported. The horizontal gap between the two teams is there to make the map readable: both sit in genesis and custom built. | Chapter 11, near the opening; chapter 12 may reuse it for "the second run" |
| 14 | `14-the-second-run` | The method moves from explorer to villager (chapter 0's three stages as bands). The talk is day one. The machinery was ported rule for rule on 30 October, moving from genesis to custom built. This book's RC1 is the villager's edition, heading for a publisher's edit (the town planner's). New in the second run: security staffed from round 0, a definition of done, scope changes reported. Publishing rests on pandoc, a headless browser and publishing platforms. | Chapter 12, "Staff a conductor, then security, then the rest" or its opening |
| 15 | `15-talk-evolution-and-the-opportunity` | The talk's map 4 (beat 3e). Exploitation at the edge and its defences are commodity. What an agent-trusting business needs is in genesis and moving. Pioneers, settlers and town planners are shown as bands. | Chapter 12, "Brakes, and go build" (replacing half of `12-go-build.jpg`) |
| 16 | `16-talk-security-products-evolve` | The talk's map 5 (beat 3f). Models are a commodity, and agent teams with mandates, evidence vaults, a harness and behaviour policies are in genesis. The notes say "augmenting people, not replacing them" and "the capability is the orchestration, not the model". | Chapter 12 beside map 15, or chapter 7 (the `team` beat) |

## Where this came from

- The editor's brief: `briefs/2026-10-30__in-session/01-principles-maps-and-the-plumbing.md`. The RC1 brief: `team/conductor/rc1/BRIEF.md`. The chapters: `team/conductor/rc1/*.md`. The plan: `chapter-plan/plan.md`, draft 5.
- The talk's repository at `298be4e`: `team/storyteller/maps/` and its README (the five maps; "attrition", in the editor's answers of 17:15, `team/conductor/briefs/2026-10-29__editor/6-answers-1715.md`); `REALITY.md` and `.github/workflows/release.yml` (the site on hosted pages).
- `controls/index.json` (kinds, what each control stopped and missed); `claims/register.json` (C011 only); `book.json` (S8, the machinery ported); `team/conductor/handoffs/2026-10-30__cold-read/` (the hand-off).
- Renderer: `team/conductor/rc1/tools/wardley.py`, ported from the talk's storyteller and reworked for print. PNG step: `team/conductor/rc1/tools/wardley_png.js`.
