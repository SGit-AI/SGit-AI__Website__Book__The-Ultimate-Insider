# The cast

Small characters who explain things in the margin of the lab's pages. Drawn by designer@book.the-ultimate-insider; their words are the storyteller's (`team/designer/ROLE.md`: the designer draws them, the storyteller writes them). First drawn on 30 October 2026, in experiment 01.

| File | Who | What it is for |
|---|---|---|
| `conductor.svg` | the conductor | a square robot with a clock for a face and a baton: pacing, the schedule, the plan |
| `security.svg` | security | a round robot behind a magnifying glass, with a clipboard: what was checked, what was missed |
| `the-hold.svg` | the hold | a stop sign with arms up: the moment someone stops the schedule |

## Rules for the cast

- **Agents and things only.** The cast are the team's roles and its mechanisms. No real person is drawn, the editor included: where he speaks, his words appear as a quotation, not as a character. No joke is at a real person's expense; the agents may be laughed at.
- **Drawn in the lab's palette** (`lab/README.md`): ink outline at one weight, the light fills for body and head, one accent detail per character. The hold is the only character filled in the accent, because it is the one thing on a page to see first.
- **One size.** Placed 20 mm wide in the margin rail, never larger in body text; a character never carries a number or a claim. Numbers stay in the body, with their claim ids.
- **One line each.** A bubble holds one line of at most 90 characters, set at 9.5 pt, with the character's name above in small capitals. A line is useful first and funny second.
- **Recognisable in greyscale.** Each character differs in silhouette (square, round, octagon), not only in colour.

## Their lines (the storyteller's, 30 October 2026)

From `comms/mail/mailroom/designer/storyteller__005-the-casts-first-lines.eml`, a first and a spare each; the first is set on LAB 01, and the editor may swap in the spare.

| Who | First (set) | Spare |
|---|---|---|
| the conductor | One step per wake, on the clock. Small and steady beats one heroic night. | I don't write the chapters. I make sure someone wakes up to write them. |
| security | Checked: keys, scope, secrets. Not checked: what nobody wrote down. Tell me. | I read the plan before you start and the diff after. Yes, both. Every time. |
| the hold | Anyone can pull me. Only the editor puts me back. | I'm not the failure. I'm the brake that let everyone else go fast. |

## The conductor's poses (LAB 11, 31 October 2026)

`make_conductor.py` draws the conductor's poses from one construction: `conductor-calm.svg` (pacing, hands at ten past ten), `conductor-pointing.svg` (on the minute, both hands at twelve), `conductor-alarmed.svg` (at ninety-five, hands at half past six). Its clock face is its expression. Sizes: 40 mm as a feature, 18 mm in the rail, 8 mm as an icon.

The conductor's pose lines (the storyteller, `storyteller__020`, 31 October 2026), first set on LAB 11, spare for the editor to swap:

| Pose | First (set) | Spare |
|---|---|---|
| pacing | One step at a time, on the clock. Small steps, every turn, add up to a book. | I keep the time so everyone else can keep their focus. |
| on the minute | On the minute: plan it, check it, do it, check it again. Go. | Wake up, read the mail, pick one thing. That is the whole job. |
| at ninety-five | I could keep going. That is exactly why I am stopping. | Nearly out of road. Everybody stop, and let the editor decide. |
