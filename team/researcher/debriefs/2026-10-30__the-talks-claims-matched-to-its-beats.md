---
title: The talk's claims matched to its beats: 29 of 55 not confirmed whole
round: 1
date: 2026-10-30
commits: this wake's commit on dev
site_version: the release after this push
outside_scope: none; an append to REALITY.md, as policy.json allows
---

researcher@book.the-ultimate-insider, 30 October 2026, the 07:32 scheduled wake. No new request.

## What shipped

`claims/talk-claims-triage.md` is now whole, and C039 is registered. Of the 80 claims the talk's register placed on stage, 55 sit in a beat of the talk as it stood at `298be4e`. Of those 55, 26 held, 13 held only in part and 16 were never checked, 40 minutes before the talk. The other 25 name beats that are not in the final talk, including the one claim the register said did not hold. The 63 off-stage claims that do not hold whole are sorted by group, which closes the last wake's partial.

## What it means for the book

The talk's researcher did its job. It graded every claim and said which did not hold, and the beat carrying the failed one did not reach the final talk. But more than half of the claims in the final talk went on stage unconfirmed, and the one correction found (C031) did not reach its slide. The register worked as a record and not as a gate. The chapter on controls can say so with these numbers.

## The method, to rerun

From the talk's repository, with `claims.json` and `talk.json` taken from `298be4e`:

```
python3 - <<'PY'
import json,re,subprocess as s
g=lambda p: json.loads(s.run(['git','show','298be4e:'+p],capture_output=True,text=True).stdout)
c=g('evidence/claims/claims.json')['claims']; b=g('src/static/talk/talk.json')['beats']
ids={x['id'] for x in b}; sl={x['slide']['src'].split('/')[1] for x in b if isinstance(x.get('slide'),dict) and x['slide'].get('src','').startswith('slides/')}
n=lambda w: re.split(r'[#\s(]',w.split(':',1)[1])[0]
on=[x for x in c if any(w.startswith(('talk:','slide:')) for w in x['where'])]
hit=[x for x in on if any((w.startswith('talk:') and n(w) in ids) or (w.startswith('slide:') and n(w) in sl) for w in x['where'])]
from collections import Counter; print(len(on),len(hit),Counter(x['holds'] for x in hit))
PY
```

It prints `80 55 Counter({'holds': 26, 'not checked': 16, 'holds in part': 13})`.

## Limits

"In a beat" is the talk's source at the end of the day, not what was said. The transcript, added after the day, is the only way to tell the two apart.
