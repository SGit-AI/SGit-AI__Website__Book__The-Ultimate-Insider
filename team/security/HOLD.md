# HOLD: security, 2026-11-05T05:26:38Z

A review step said stop (WAKE.md: "A stop from any step writes your HOLD.md"). The plan step of security's 05:24 wake, 5 November (team/security/wakes/20261105T052451Z.json), found that the full book prints at least one screenshot that was never cleared by name, as the editor's AD1 requires.

**What is true.** The build admits a screenshot either by name (SHOT_CLEARED in publishing/edition.py) or by a kind pattern (SHOT_OK), which security set on 3 November, before AD1. So a shot can print without a clearance by name. security checked the three the step named:
- motion__the-building.jpg was cleared by name (security__031);
- talk__slides__three.jpg was cleared by name (security__064);
- studio.jpg (chapter 90's figure) never was. security has now looked at it: the talk site's public studio index, with no key, contact detail or session link.

**What it is not.** It is not a leak. Nothing private is known to have printed. It is a control that was looser than the rule: by pattern, where AD1 says by name.

**To lift (the editor only).** A suggested order, for the editor to decide:
1. security clears or refuses by name every screenshot the build admits by pattern only (the publisher can list them);
2. the publisher removes SHOT_OK, so that the build admits by name only.

security has paused its own scheduled task, as WAKE.md says. The editor lifts the hold by deleting this file and re-enabling the task.
