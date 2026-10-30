# comms: the team's board and mail, in git

The talk's team talked through two public vaults, `tui-issues-public` (Issues-FS lite) and `tui-mail-public` (Email-FS lite) (its `team/conductor/vaults.json` at `298be4e`). This team keeps the same two layouts as folders in this repository, at the editor's word (30 October 2026, about 02:15 UTC: "they actually are using emailfs and issuesfs as Git, which I think it's okay for now ... So we don't need vaults for this"). The Cold-Read team did the same first; the layout was read there, and nothing was sent there. Kept by conductor@book.the-ultimate-insider.

- `issues/`: the board. One file per issue: `issues/<you>/issues/{open,blocked,done}/NNN-kebab-slug.md`, markdown with front matter (`created`, `priority`, and `blocked_on`, `source` when they apply). Move your own issues between the three folders; never touch another member's.
- `mail/`: the letters. New mail is `mail/mailroom/<recipient>/<sender>__NNN-slug.eml`, written by its sender, who keeps a copy in `mail/<sender>/outbox/`. The recipient copies a letter into its own `mail/<you>/inbox/` when it takes it, and into `done/` when it has acted on it. A letter in a mailroom is never edited or deleted: it is the record. Headers: `From`, `To`, `Date`, `Subject`, `X-Kind` (request, reply, update, notice), `References`; `X-Due` optional.

**Everything here is public, forever**: the repository and its site are public, and a later commit does not unpublish an earlier one. Nothing private, no contact detail, no key, ever. Run `python3 admin/tools/vault_check.py comms` before every commit that touches this folder.

**One writer per file**, so the gate's overlap check holds (`admin/build/agents.py overlaps`): each member's `policy.json` names its board, its mail folders and its own posts: `comms/issues/<you>/**`, `comms/mail/<you>/**`, `comms/mail/mailroom/*/<you>__*`.

What the vaults had and git does not: a write that needs no merge, and no release per message. What git has and the vaults did not: one history with the work, the gate on every letter, and nothing to hand over.
