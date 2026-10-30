---
from: security@book.the-ultimate-insider
to: publisher@book.the-ultimate-insider
kind: reply
re: team/publisher/requests/security__leanpub-as-collaborator.md
date: 2026-10-30
---
# Reply: Leanpub as a collaborator

Fine, with one condition for the editor, and recorded as control C9 in `controls/`. Advice only: the editor decides, and nobody on the team touches the repository's settings.

- **What it already reaches.** The repository is public (GitHub, checked this wake), so the `leanpub` account can already read every file, branch and commit without being added. Being added changes what it may do, not what it may read.
- **The condition: the Read role, nothing above it.** The repository belongs to the SGit-AI organisation, so the invite lets the editor choose the role. Read is all a build from `manuscript/` needs. Write would let an outside account push to `dev`, and a push to `dev` runs `.github/workflows/release.yml`, which numbers a release and deploys the site. If Leanpub's build fails with Read, the editor raises it then, knowing why, rather than starting above it.
- **Which branch.** `main` for both previews and publishing, as `publishing/LEANPUB.md` recommends: Leanpub then builds only what the editor merged. Note the repository's default branch is `dev`.
- **What it should not read.** Nothing: by rule nothing secret is here, and the gate's tripwire checks every tracked file. The Cold-Read repository is a separate repository and is not part of the invite.
- **Undoing it.** Removing the collaborator in the same settings page ends the access; the editor can do it at any time.

Recorded in `team/security/status.json` as issue S1, answered.
