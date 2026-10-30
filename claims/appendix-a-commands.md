# Appendix A: every number rerun

researcher@book.the-ultimate-insider, 30 October 2026, at the storyteller's request (`comms/mail/mailroom/researcher/storyteller__001-appendix-commands.eml`). Generated from `register.json`, where each entry's `command` field is the source; this file is a reading copy for the writer, rebuilt whenever the register changes.

**How to rerun.** Clone the talk's repository (SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider), stand in it, and run each command. Every one is read-only and names `298be4e`, so it gives the same answer whatever was added after the day. C032 to C036 run in SGit-AI/SGit-AI__Website__Graphs at `d39e717`. Where no single command does it, the entry says "method" and describes the steps. Times are UTC, which was London time on 29 October 2026.

## C001: First commit of the day

State: checked.

```
git log 298be4e --reverse --format='%h %ci %an %s' | head -1
```

## C002: Commits in the repository at 298be4e

State: checked.

```
git rev-list --count 298be4e
```

## C003: Commits by author at 298be4e

State: checked.

```
git log 298be4e --format=%an | sort | uniq -c
```

## C004: Commits by 18:46, the end of the day's work (decision S6)

State: checked.

```
git log 298be4e --until=2026-10-29T18:46:59Z --format=%an | sort | uniq -c
```

## C005: Last work commit, last release of the day

State: checked.

```
git log 298be4e --until=2026-10-29T19:00:00Z --format='%h %ci %an %s' | head -3
```

## C006: The hold

State: checked.

```
git log 298be4e --since=2026-10-29T18:44:00Z --until=2026-10-29T19:00:00Z --format='%h %ci %an %s'
```

## C007: Merge to main

State: checked.

```
git log 298be4e --since=2026-10-29T19:00:00Z --format='%h %ci %an %s'
```

## C008: Commits after 15:00

State: checked.

```
git rev-list --count --since=2026-10-29T15:00:00Z 298be4e
```

## C009: Site releases

State: checked.

```
git log 298be4e --author='GitHub Actions' --format=%s | grep -oE 'site v[0-9]+\.[0-9]+\.[0-9]+' | sort -uV | sed -n '1p;$p;' ; git log 298be4e --author='GitHub Actions' --format=%s | grep -c '^site v'
```

## C010: Nineteen hours

State: corrected.

```
arithmetic on C001, C005 and C007
```

## C011: Members of the talk's team

State: open.

```
for m in $(git ls-tree -d --name-only 298be4e team/ | xargs -n1 basename); do echo $m $(git log 298be4e --reverse --format='%ci %h' -- team/$m/key.json | head -1); done
```

## C012: The storyteller joined about 14:12 UTC

State: checked.

```
git show 298be4e:team/storyteller/wakes/20261029T141252Z.json | head -6; git log 298be4e --reverse --format='%ci %h %s' -- team/storyteller/key.json | head -1
```

## C013: Motion and studio joined 15:30 to 16:00

State: checked.

```
git log 298be4e --reverse --format='%ci %h %s' -- team/motion/key.json team/studio/key.json | head -2
```

## C014: Commits by member (Claude commits whose subject names a member, with or without @)

State: corrected.

```
git log 298be4e --author=Claude --format=%s | grep -oE '^@?[a-z][a-z.-]*:' | sed 's/^@//' | sort | uniq -c | sort -rn
```

## C015: 58 beats in three parts

State: checked.

```
git show 298be4e:src/static/talk/talk.json | python3 -c "import json,sys,collections;b=json.load(sys.stdin)['beats'];print(len(b),collections.Counter(x['part'] for x in b))"
```

## C016: 17 beats at 13:00

State: checked.

```
for h in $(git log 298be4e --reverse --format=%h -- src/static/talk/talk.json); do echo $h $(git log -1 --format=%ci $h) $(git show $h:src/static/talk/talk.json | python3 -c "import json,sys;print(len(json.load(sys.stdin)['beats']))"); done
```

## C017: Player 977 lines, from 236

State: checked.

```
for h in $(git log 298be4e --reverse --format=%h -- src/static/talk/player.html); do echo $h $(git log -1 --format=%ci $h) $(git show $h:src/static/talk/player.html | wc -l); done
```

## C018: The player landed with fixes at 18:37, twenty minutes before the lock

State: corrected.

```
git log 298be4e -1 --format='%h %ci %s' -- src/static/talk/player.html; git log 298be4e --format='%h %ci %s' -i --grep=lock
```

## C019: About 1,260 files outside src/

State: corrected.

```
git ls-tree -r --name-only 298be4e | wc -l; git ls-tree -r --name-only 298be4e | grep -vc '^src/'
```

## C020: team/ is 61 MB, evidence/ 14 MB

State: checked.

```
for d in team evidence; do git ls-tree -r -l 298be4e $d | awk -v d=$d '{s+=$4} END {print d, s/1e6, "MB"}'; done
```

## C021: Usage reached 95% at the hold

State: checked.

```
git log 298be4e -1 --format='%h %ci %s' --grep='95%'
```

## C022: Wake records on the day

State: checked.

```
python3 -c "import json,subprocess as s;R='298be4e';fs=[f for f in s.run(['git','ls-tree','-r','--name-only',R],capture_output=True,text=True).stdout.split() if f.startswith('team/') and '/wakes/' in f and f.endswith('.json')];import collections;print(len(fs),collections.Counter(f.split('/')[1] for f in fs))"
```

## C023: Step verdicts across the day's wake records

State: checked.

```
method, not one command: parse every team/*/wakes/*.json at 298be4e; count steps.<step>.verdict; count history entries with verdict 'change' (directly or under pre_review), and free-text entries saying 'pre-review said change' (the script in team/researcher/debriefs/ of 30 October, 02:32 wake, rerun the same way)
```

## C024: Holds written on the day

State: checked.

```
git log 298be4e --diff-filter=A --format='%h %ci %s' -- 'team/*/HOLD.md'; git log 298be4e --diff-filter=D --format='%h %ci %s' -- 'team/*/HOLD.md'
```

## C025: Post-review findings and what each fixed

State: checked.

```
method: the C023 parse, selecting steps.post_review.verdict == 'finding', read with the same record's post_check comment
```

## C026: The talk's planned length

State: checked.

```
git show 298be4e:src/static/talk/talk.json | python3 -c "import json,sys,collections;b=json.load(sys.stdin)['beats'];t=collections.Counter();[t.update({x['part']:x['dur']}) for x in b];print(sum(t.values())/60,{k:v/60 for k,v in t.items()})"
```

## C027: The part locks and their state at the hold

State: checked.

```
git show 298be4e:team/conductor/HOLD.md; git ls-tree -r --name-only 298be4e | grep -i lock
```

## C028: When the player port landed

State: checked.

```
git log 298be4e --format='%h %ci %s' -- src/static/talk/player.html | sed -n '1p;$p'; git log 298be4e --format=%h --since=2026-10-29T15:07:00Z --until=2026-10-29T18:37:03Z -- src/static/talk/player.html | wc -l
```

## C029: The talk's own claims register

State: checked.

```
git show 298be4e:evidence/claims/claims.json | python3 -c "import json,sys,collections;c=json.load(sys.stdin)['claims'];print(len(c),collections.Counter(x['grade'] for x in c),collections.Counter(x['holds'] for x in c))"
```

## C030: The talk's three claims that do not hold

State: checked.

```
git show 298be4e:evidence/claims/claims.json | python3 -c "import json,sys;[print(x['id'],x['where']) for x in json.load(sys.stdin)['claims'] if x['holds']=='does not hold']"
```

## C031: $17.4M, the average annual cost of insider risk, on the talk's definition slide

State: open.

```
git grep -n '17\.4' 298be4e -- src; git grep -c '19\.5M' 298be4e -- src/static/talk
```

## C032: graphs.sgit.ai's making-of: 88 releases in 6 days, a median of 31 minutes apart

State: checked.

```
in SGit-AI__Website__Graphs: git for-each-ref refs/tags --format='%(refname:short) %(creatordate:iso-strict)' | sort -V, then v0.1.0 to v0.5.11 and the median gap
```

## C033: graphs.sgit.ai's three books

State: checked.

```
in SGit-AI__Website__Graphs at d39e717: for b in fsg fsg-universe making-a-book; do git show d39e717:v2/books/$b/book.json | head -12; done
```

## C034: graphs.sgit.ai's agent team: seven roles, one folder each

State: checked.

```
in SGit-AI__Website__Graphs: git ls-tree -d --name-only d39e717 v2/team/
```

## C035: The making-of computed its numbers from git and re-took its figures at their tags

State: checked.

```
read: v2/books/making-a-book/content/15__appendix-c-the-harness.md at d39e717
```

## C036: The making-of's stated largest cost: six days built the machine and none of the second book's chapters

State: checked.

```
read: v2/books/making-a-book/content/12__what-it-costs.md at d39e717
```

## C037: What the day cost the editor, in hours and usage

State: open.

```
git grep -n -iE 'usage[^"]{0,80}[0-9]+ ?%' 298be4e -- team ':!*.png'
```

## C038: The talk's claims its register places on stage

State: checked.

```
git show 298be4e:evidence/claims/claims.json | python3 -c "import json,sys,collections;c=[x for x in json.load(sys.stdin)['claims'] if any(w.startswith(('talk:','slide:')) for w in x['where'])];print(len(c),collections.Counter(x['holds'] for x in c))"
```

## Where this came from

`claims/register.json`, the `command` of each entry, run in this session against `298be4e` and `d39e717`; spot-checked on 30 October 05:45 (C004, C009, C014, C019, C022, C024, C026, C029, C031) and 06:45 (C038), each giving the registered value.
