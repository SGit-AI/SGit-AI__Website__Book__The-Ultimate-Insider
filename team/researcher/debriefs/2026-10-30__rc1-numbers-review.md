---
title: RC1's numbers reviewed, and the register corrected where RC1's drafting found it wrong
round: 1
date: 2026-10-30
commits: this wake's commit on dev
site_version: the release after this push
outside_scope: none; comms/ paths added to my policy by the conductor at the editor's decision C10b (e7d3d3d)
---

researcher@book.the-ultimate-insider, 30 October 2026, the 10:32 scheduled wake. The editor signed the plan at about 10:00 and wants RC1 to read on a flight today.

## What shipped

- **RC1's numbers, checked mechanically.** Every line of the thirteen chapters that carries a number was matched against the register entries it cites. Every count but a dozen cites an id, and the numbers match their entries, apart from the ones listed in my letter to the conductor (`comms/mail/mailroom/conductor/researcher__001-rc1-numbers.eml`).
- **The register corrected** at the RC1 drafting's findings, each checked in a full clone (816 commits at `298be4e`; my clone was never shallow). C011 now gives join times by both methods. C014 is redone: conductor 106, dev 64, 164 merges, none unattributed. C018's time and C021's command are fixed, and the C023 script is below. C041 and C042 are new.

## What I got wrong, again

C014 was wrong three ways: it missed the bare prefix, it counted merges by subject, and it did not read the trailers. Each time the method note named the limit, and each time a reader trusted the number anyway. From now on a count with a known limit stays `open` until the limit is removed.

## The scripts

C014, from the talk's repository:

```
git log 298be4e --author=Claude --no-merges --format='%x1e%s%x1f%B' | python3 -c "
import sys,re,collections
c=collections.Counter()
for r in sys.stdin.read().split('\x1e'):
    if not r.strip(): continue
    s,_,b=r.partition('\x1f'); s=s.strip()
    m=re.match(r'^@?([a-z][a-z.-]*):',s); a=re.findall(r'^Agent:\s*([a-z.-]+)@',b,re.M)
    c[m.group(1) if m else a[0] if a else ('conductor' if s.startswith('Conductor') else '?')]+=1
print(sum(c.values()),c.most_common())"
```

C023 and C022, from the talk's repository:

```
python3 - <<'PY'
import json,subprocess as s,collections
R='298be4e'; fs=[f for f in s.run(['git','ls-tree','-r','--name-only',R],capture_output=True,text=True).stdout.split() if f.startswith('team/') and '/wakes/' in f and f.endswith('.json')]
V=collections.defaultdict(collections.Counter); ch=0
for f in fs:
    d=json.loads(s.run(['git','show',R+':'+f],capture_output=True,text=True).stdout)
    for k,v in (d.get('steps') or {}).items(): V[k][v.get('verdict')]+=1
    for h in d.get('history') or []:
        if h.get('verdict')=='change' or (h.get('pre_review') or {}).get('verdict')=='change' or 'pre-review said change' in h.get('what',''): ch+=1
print(len(fs),{k:dict(v) for k,v in V.items()},'changes',ch)
PY
```

It prints 162 records and 11 changes.

## Not done this wake

The Cold-Read analyst's numbers against the register, beyond C014 and C042. The editor's voice review. The rest of the drafting's list: the 16:44 backlog, the transcript's counts in `a9c0b49`, and the 26% usage reading.
