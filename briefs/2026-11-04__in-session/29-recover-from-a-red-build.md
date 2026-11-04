# Delete the hold, and recover from a red build instead of stopping

The editor, Dinis Cruz, in the conductor's session (conductor@book.the-ultimate-insider), about 16:30 UTC on 4 November 2026, after asking why the team was on hold. Kept as given. Never edited.

> can you delete that file, and that feels quite a fragile setup, since the team should be able to recover from that, and at least continue work for a couple rounds while that fix happens, since the agents local state survives runs

## How the conductor reads it (not his words)

- **The hold**: team/writer/HOLD.md (12:34 UTC, a developer's status entry that broke the build; `dev` green again since 13:28) deleted at his word. The commit that did it (343ae69a) dates his words "about 16:10 UTC": an estimate; they came at about 16:30. The conductor also re-enabled the writer's paused task (trig_01XcHwiizLtkXBLL6Z1xmq2X): the conductor's reading of his word as a full lift under WAKE.md ("the editor lifts a hold by deleting the file and re-enabling the paused tasks"), not his words.
- **Decision HR1**: a red `dev` no longer stops the team. Members keep working and commit locally, do not push while it is red, tell the owner once, and push when it is green; "a couple rounds" is read as two wakes, a hold at the third. The build forgives a member's malformed status or policy file with a warning. Holds for secrets, instructions in material, foreign changes and harm are unchanged.
