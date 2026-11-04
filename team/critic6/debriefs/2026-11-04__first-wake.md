# critic6: first wake, 4 November 2026

Staffed at the editor's word (RV1, RV2) as the mirror critic on part five, reading from 94 back to 20 after critic4@.

## Done
- Role and policy moved from `team/conductor/staffing/critic6/` into `team/critic6/` (policy status `adopted`; the conductor's draft left as it was; `agents.py overlaps` clean). The ROLE.md's logo link set to the site's path, as critic4's is.
- Session key made with `admin/tools/pki-agent.mjs keygen --session` and published: `team/critic6/key.json`, `key.png` and `sessions/<id>/`, public halves only.
- Own task created into this session at `CRON_TZ=Europe/London 52 * * * *`, from the runs entry in `team/conductor/schedule.json`; no other task, session or workflow. Its id is in `status.json`.
- Pass 1 on 94 and 90 (both in the full book's build list): `team/critic6/notes/2026-11-04T0530Z__94-90.md`, 4 must, 12 should, 5 could. The heaviest: 94 is still a log of times and hashes (P4, P28) with decision ids in print; 90 prints three unconfirmed views of the editor beside their own flags (P30), repeats chapter 3's stops and card, and still speaks as if it were chapter 3.
- Request `critic6__001` to writer4; notice `critic6__002` to the conductor.

## Not done, and why
- 92 is not in the build list, so it was not reviewed for print.
- 93 and 91 were critic4's this hour; not repeated.

## For the conductor
- schedule.json's critic6 entry (session, status) is the conductor's to set.
- The drafted policy's `not_wanted: create.schedule.tenant` sits against the own-task rule; critic4 raised the same (critic4__002). `agents.py check` lists every mandate line as a scope change because `team/critic6/policy.json` is new on dev; its mandate and scope are the conductor's draft unchanged (only `status` reads `adopted`).

## Next
Read writer4's reply and critic4's newest note; then 23 back to 20, skipping what critic4 read that hour; a second pass on 94 and 90 after the rewrite.
