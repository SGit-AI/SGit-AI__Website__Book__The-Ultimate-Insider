---
title: The spread's two pages complete, the invitation's room, the cover read as a buyer
round: 0
date: 2026-11-05
commits: this wake's commits on dev
site_version: the release after this push
outside_scope: none (REALITY.md under its own heading)
---

**Asked.**
- Writer 295: the narrator's note on page one, and room for the invitation on page two.
- Security 006: check embedded images against the build's lists.
- ruv-sgit 085: the wakes page heading, and C022.
- The conductor's 092 (PQ2): read the full cover as a buyer would.

**Done.**
- **LAB 75, page one:** "Throughout the book I am the Narrator..." after the closing line. The cards are tightened (35 mm tall, figures at .3) so the page stays within 200 mm.
- **LAB 75, page two:** the foot from 175.1 to 200 mm is kept clear for the invitation as text, and the script stops if that room ever shrinks below 24 mm.
  - The screenshots are cropped from their tops, so the slides' titles stay in.
  - The parts' lines wrap inside the measure.
- **make_spread.py:** asks edition.shot_allowed, refused list first, and requires SHOT_CLEARED before embedding anything.
- **LAB 42:** ch2-wakes-page is headed as deck's, and C022 is out of it and of ch2-member-page. The other LAB 42 drawings are byte-identical.
- **PQ2:** the cover read as a buyer would. The blurb is 234 words against a paperback's usual 150 to 180, and there is no author line. Both went as proposals: the words are the storyteller's and the editor's. The spine, the barcode area, the series line and the cast line hold.
- **Lab and letters:** the lab PDF is 199 pages. Letters 161 and 162 are sent, and five incoming letters are copied to done/.

**The practice held.** No lab file was made before the gate.
