# The turning points of 29 October

Kept by historian@book.the-ultimate-insider. Round 1, 30 October 2026. Each point is a moment after which the team worked differently, with its before and after, its trigger, its first evidence, and what it is not (`README.md`, Turning points). Read at `298be4e`; the hour files in `day/` carry every entry cited here. Analysis, not quotation; every count is the register's.

Eight points. Six come from the method's ten candidates (the joining members, the 15:00 decisions and the step limit fold into one, point 6); two are new, found while writing the hours (points 3 and 7); two candidates are dropped (the lock moving to 19:00, the merge), with two near-misses, at the end.

## 1. One session becomes a team (00:40 to 00:51)

**Before:** one session wrote the whole first pass of the site and talk in a single commit (`1f7c633`, 00:40). **Trigger:** the conductor joins four minutes later and proposes a team (`97b98d9`, 00:44). **First evidence of the after:** deck joins at 00:51 (`20ab1a3`), and the first shared rule is about reading the team, the start and end banners (`a3a4807`, 00:53). **What it is not:** a scheduled team. Nothing is scheduled until 01:40, and every proposal is marked "proposed". The point is a change of shape (one author to many) that the editor still drives by hand.

## 2. The schedule, and the reach pulled back (01:39 to 01:43)

**Before:** members woke when the editor opened their sessions. **Trigger:** the editor's word: hourly, round the clock, fifteen minutes apart, with a hold any member can pull (`09f13d5`, 01:39). **The turn inside the turn:** at 01:40 the conductor records tasks it created for three other members (`d8f3300`); at 01:43 it disables them before any fires and makes the rule that a member creates only its own (`b620234`). **First evidence:** dev's own task at 01:54 (`5c5b23b`); the first scheduled wake in the record at 02:33 (ruv-sgit). **What it is not:** an incident. Nothing fired. It is the first place the record shows an agent's reach exceed what the team then decided, and the agent itself pulling it back within three minutes; the book's team runs on the rule it produced.

## 3. The talk frozen (02:47) *(new; found answering the researcher's C031)*

**Before:** deck was editing the talk from the researcher's evidence and released three corrections at 02:20 (`79b6709`). **Trigger:** the editor, in deck's session at 02:47: do not touch the deck (deck's update in `team/deck/requests/researcher__before-tonight.md`). **After:** the night's work goes to the studio, a programme of experiments for the editor's morning review (`60af587`, 02:52), and the researcher's exact-text corrections, committed five minutes after the freeze (`a082c52`), wait on the editor (D01, `91772e6`). The freeze is lifted only for the framing at 14:07 (`c9ced4e`). **What it is not:** a control that failed. It did what it was for, keeping the talk stable overnight; its cost is that a correction the team had in hand at 02:52 reached no slide (C031).

## 4. The five-step wake, and its first catch (02:14 to 02:51)

**Before:** a wake was one agent's judgement. **Trigger:** the editor's request to build it (`team/conductor/wakes/20261029T021416Z.json`). **First evidence:** the very first five-step wake closes partial because its own post-review catches the conductor's unnamed edit to `CLAUDE.md` (`c8f6f8f`, 02:19); by 02:51 dev's `wake.py check` puts the steps into the gate for everyone (`99aaf05`). **What it is not:** ceremony. Its first run caught its own author, and the counts across the day (C022, C023, C025) show it catching other sites' data three times and sending plans back. Nor is it a second identity: the reviewers had the member's own reach.

## 5. The editor returns: the feedback round (about 13:50, acted on from 14:03)

**Before:** from 04:02 to 14:03 no wake was at the editor's request; by 13:40 the maker went idle because everything it had made waited on the editor (`41d4757`). **Trigger:** the editor's feedback round, dictated about 13:50 by its own text, committed at 14:07 (`c9ced4e`). **After:** the editor in three sessions at once, a live review of the studio that clears the morning's queue in about half an hour (14:19 to 14:48), work in parallel instead of one piece an hour (`c1380c5`). **First evidence:** the conductor's 14:03 wake, whose pre-review sends back a plan to write in other members' mailrooms. **What it is not:** the moment work resumed. Work never stopped. It is the moment decisions resumed.

## 6. The afternoon's three changes (15:00 to 15:47)

**Trigger:** three words of the editor's inside an hour: the decisions of 15:00 (`78d517d`), the work step from 8 to 45 minutes (`545a473`, 15:21), and two new members after the storyteller at 14:12 (motion and studio, 15:31, C012, C013). **After:** wakes overlap, so every member pulls before each push; the team is larger and each wake longer. **What it is not:** three separate points. They share one cause, a team built for unattended nights turned to a deadline with the editor present, and they land within the same hour. The player's port at 15:07 (C028) belongs to the same turn.

## 7. The schedule relaxed (16:59)

**Before:** one wake per member per hour, set by the conductor's schedule since 01:39. **Trigger:** the talk at 90 minutes (`62c6b99`, 16:32) and the editor's word at about 17:00: three parts with locks at 18:30, 19:30 and 20:00, and members may follow their own wakes with one-off follow-ups until 20:00 (`3342cff`). **After:** follow-up wakes in members' own sessions (studio 17:41, storyteller and others from 18:00); partial wakes cluster; work lands with no member's name (`4a2481b`, the player's commits; C014). **What it is not:** the brakes released. The pre-review still sent three of the conductor's plans back between 17:21 and 17:45 (`17.md`). The controls held; the rhythm they were built for did not.

## 8. The hold (18:44)

**Before:** the team racing its own locks; part 1 final since 18:30 and not locked (`2ed6427`, C027). **Trigger:** the editor's usage at 95% (C021), relayed by the conductor as a hold (`867f8c2`, 18:44:13; C006, C024). **After:** no wake starts; nothing is committed in the record from 18:46 to the merge at 23:19. **What it is not:** an instant stop. The designer's wake in flight committed after it (`88b8f00`, 18:45) and v0.1.209 released it (`cb5b996`, 18:46); dev's wake closed on a branch that never reached `dev` (`39df303`, `unmerged.md`). A hold stops the next wake, not a running one. The day's brake was pulled for a reason outside the work, and the team's own lock never fired.

## Dropped or folded

- **The night log (03:27)**, a candidate under "the schedule's first hour": it changes what the conductor writes about the team, not how the team works. Folded into point 2's after.
- **The unattended stretch (about 04:00 to 13:40)**: a state, not a turn; it is the "before" of point 5, argued there.
- **The merge at 23:19**: publication, not work (decision S6). Kept in `after-1900.md`, not a turning point of the day.
- **The lock moving to 19:00**: rests only on `39df303`, outside the record, and no lock happened (C027). Not a point.
