# Appendix A: every number rerun

researcher@book.the-ultimate-insider, 30 October 2026, at the storyteller's request (`comms/mail/mailroom/researcher/storyteller__001-appendix-commands.eml`). Generated from `register.json`, where each entry's `command` field is the source; this file is a reading copy for the writer, rebuilt whenever the register changes.

**How to rerun.** Clone the talk's repository (SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider), stand in it, and run each command. Every one is read-only and names `298be4e`, so it gives the same answer whatever was added after the day. C032 to C036 run in SGit-AI/SGit-AI__Website__Graphs at `d39e717`. C043 to C062 (chapter 11b's dates) run in the public repository or against the web page each names, as read on 30 October 2026; counts there grow with time. Where no single command does it, the entry says "method" and describes the steps. Times are UTC, which was London time on 29 October 2026.

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
git rev-list --count --since=2026-10-29T15:00:00Z 298be4e; git rev-list --count --since=2026-10-29T15:00:00Z --until=2026-10-29T18:46:59Z 298be4e
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
for m in dev conductor ruv-sgit researcher deck designer storyteller motion studio; do echo $m $(git log 298be4e --reverse --format='%h %ci' -- team/$m/key.json team/keys/$m.json | head -1); done; git log 298be4e --reverse --author=Claude --format='%h %ci %s' | grep -iE ' (@?(dev|conductor|deck|ruv-sgit|researcher|designer|storyteller|motion|studio):|Conductor joins)' | awk '!s[$4]++'
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
git rev-list --merges --count 298be4e; git log 298be4e --merges --author=Claude --format=%h | wc -l; then the attribution script in team/researcher/debriefs/2026-10-30__rc1-numbers-review.md
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
git log 298be4e -1 --author=Claude --format='%h %ci %s' --grep='95%'   # 867f8c2, 18:44:13; without --author the release 7968c99 (18:44:49) prints first
```

## C022: Wake records on the day

State: checked.

```
python3 -c "import json,subprocess as s;R='298be4e';fs=[f for f in s.run(['git','ls-tree','-r','--name-only',R],capture_output=True,text=True).stdout.split() if f.startswith('team/') and '/wakes/' in f and f.endswith('.json')];import collections;print(len(fs),collections.Counter(f.split('/')[1] for f in fs))"
```

## C023: Step verdicts across the day's wake records

State: checked.

```
method: the script in team/researcher/debriefs/2026-10-30__rc1-numbers-review.md (parses every team/*/wakes/*.json at 298be4e; counts steps.<step>.verdict and history entries)
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

State: checked.

```
git log 298be4e -S'data-count="17.4"' --format='%h %ci %s' -- src/static/talk/slides/definition/index.html; git show 298be4e:evidence/proposals/deck-talk-changes.md | grep -n '19.5'; then read https://ponemon.dtex.ai/ (the public landing page; the full report is behind a form, not filled in); git show 298be4e:team/deck/requests/researcher__before-tonight.md | grep -n 'frozen'; git log 298be4e --no-merges --format='%h %ci' -- src/static/talk/slides/definition/index.html
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

## C039: The talk's claims placed on stage, matched to the talk's beats at the end of the day

State: checked.

```
method: the C038 filter, then each place's name compared with talk.json's beat ids and the slides/<name> its beats show (script in team/researcher/debriefs/, 30 October 07:32 wake)
```

## C040: The player was the editor's top priority at 13:50 and still not started at 14:53 (the lessons brief)

State: corrected.

```
git show c9ced4e --format=%b | head -12; git show 298be4e:team/conductor/briefs/2026-10-29__editor/conductor-notes.md | sed -n '5,14p'; git log 298be4e --format='%h %ci %s' --since=2026-10-29T14:07Z --until=2026-10-29T15:07:09Z -- team/dev src/static/talk/player.html; git show 298be4e:team/conductor/briefs/2026-10-29__editor/feedback-briefs.md | sed -n '3p;7p'
```

## C041: The work step's limit and the hold's release

State: checked.

```
git log -1 --format='%h %ci %s' 545a473; git log -1 --format='%ci' 867f8c2; git log -1 --format='%ci' 7968c99
```

## C042: The talk's own count on stage: 510 commits and 164 releases by five in the afternoon

State: checked.

```
git show 298be4e:src/static/talk/talk.json | grep -oE '.{40}510 commits.{40}'; git rev-list --count --until=2026-10-29T17:02:59Z 298be4e; git rev-list --count --no-merges --until=2026-10-29T17:02:26Z 298be4e; git rev-list --count --author='GitHub Actions' --until=2026-10-29T17:02:26Z 298be4e
```

## C043: OSBot-Utils began on 22 February 2020

State: checked.

```
git log --reverse --format='%h %ai %an %s' | head -1   # in a clone of github.com/owasp-sbot/OSBot-Utils
```

## C044: CI owns the version, first in OSBot-Utils, October 2023: the workflow commit, and the first release tagged by CI

State: checked.

```
git show -s --format='%h %ai %an %s' e53d055 753ef2c; git tag | wc -l   # in OSBot-Utils
```

## C045: Kwargs_To_Self (January 2024) became Type_Safe (June 2024)

State: checked.

```
git show -s --format='%h %ai %s' 0df0830 4edb92e d52dc70 be1aaba   # in OSBot-Utils
```

## C046: Athena's MVP post, 17 September 2023

State: checked.

```
curl -sL -A 'Mozilla/5.0' <url> | grep -oE '"datePublished":"[^"]{10}'
```

## C047: The public writing on generative AI starts in February 2024 (OWASP London)

State: checked.

```
curl -s -o /dev/null -w '%{http_code}' <url>
```

## C048: The Cyber Boardroom Ltd incorporated, announced 8 April 2024

State: checked.

```
curl -sL -A 'Mozilla/5.0' <url> | grep -oE '"datePublished":"[^"]{10}'
```

## C049: The Cyber Boardroom on PyPI: the website and Athena released many hundreds of times

State: checked.

```
for p in cbr-website-beta cbr-athena; do curl -s https://pypi.org/pypi/$p/json | python3 -c "import json,sys;r=json.load(sys.stdin)['releases'];t=sorted(f['upload_time'][:10] for v in r.values() for f in v[:1]);print(len(r),t[0],t[-1])"; done
```

## C050: Provenance as a talk: OWASP Global AppSec, Lisbon, 28 June 2024

State: checked.

```
curl -s -o /dev/null -w '%{http_code}' <url>
```

## C051: The first MVP (15 July 2024) and the Community Edition (30 July 2024)

State: checked.

```
curl -sL -A 'Mozilla/5.0' <url> | grep -oE '"datePublished":"[^"]{10}'
```

## C052: MyFeeds began on 4 December 2024

State: checked.

```
git log --reverse --format='%h %ai' | head -1   # in myfeeds_ai
```

## C053: The January 2025 deck on CI pipelines and auto-tagging

State: checked.

```
curl -s -o /dev/null -w '%{http_code}' <url>
```

## C054: MGraph-DB from February 2025, and the fact-provenance essay of 5 February 2025

State: checked.

```
curl -s https://pypi.org/pypi/mgraph-db/json | python3 -c "import json,sys;print(len(json.load(sys.stdin)['releases']))"
```

## C055: Memory-FS began on 26 May 2025

State: checked.

```
git log --reverse --format='%h %ai' | head -1   # in Memory-FS
```

## C056: The first public trace of the AI coding assistant in his commits: June 2025, then July 2025

State: checked.

```
git show -s --format='%h %ai %s' 34d99ce   # in Memory-FS; git show -s --format='%h %ai %s' 9c8503d   # in OSBot-Utils
```

## C057: Issues-FS began on 4 February 2026

State: checked.

```
git log --reverse --format='%h %ai' | head -1; git log --reverse --author=Claude --format='%h %ai' | head -1   # in Issues-FS
```

## C058: sgit: the command line began on 3 March 2026, bootstrapped on Safe_* types; most commits by the assistant; on PyPI from 20 March

State: checked.

```
git show -s --format='%h %ai %an %s' 1b01902 ae9f85e; git log --format=%an | sort | uniq -c   # in SGit-AI__CLI
```

## C059: SG/Send began on 8 February 2026

State: open.

```
none: read the article; the repository's first commit would settle it
```

## C060: The newsroom's articles that dossier and chapter cite, by their dates in the wire

State: checked.

```
curl -s https://newsroom.sgit.ai/newsroom/wire.json | python3 -c "import json,sys;a=sorted(json.load(sys.stdin)['articles'],key=lambda i:i['date']);print(a[0]['date'],a[0]['slug'],len(a))"
```

## C061: SHarness: began 24 October 2026, sharness-ai on PyPI

State: checked.

```
curl -s https://pypi.org/pypi/sharness-ai/json | python3 -c "import json,sys;r=json.load(sys.stdin)['releases'];print(sorted((k,v[0]['upload_time']) for k,v in r.items() if v))"
```

## C062: When the editor went full time on The Cyber Boardroom

State: open.

```
none
```

## C063: The talk's repository does not use Type_Safe or name Memory-FS; it names OSBot-Utils as the source of CI-owned versions

State: checked.

```
git grep -l 'Type_Safe' 298be4e -- '*.py' | wc -l; git grep -il 'memory-fs\|memory_fs' 298be4e | wc -l; git grep -n 'OSBot-Utils' 298be4e -- content/articles/introducing-this-site.md
```

## C064: The talk's second count: 405 commits as of 18:21, in the mini deck the prelude beat showed

State: open.

```
git show 298be4e:content/articles/how-this-talk-was-built.md | sed -n 8p; git show 298be4e:src/static/talk/talk.json | python3 -c "import json,sys;b=json.load(sys.stdin)['beats'];print(b[1]['id'],b[2]['id'],b[2]['src'])"
```

## C065: The hold's gap: the designer's work commit 82 seconds after the hold

State: checked.

```
git log -1 --format='%h %ci' 867f8c2; git log -1 --format='%h %ci' 88b8f00
```

## C066: The conductor's commits by prefix: 99 with '@conductor:', 105 with or without the @, merges excluded

State: checked.

```
git log 298be4e --no-merges --format=%s | grep -c '^@conductor:'; git log 298be4e --no-merges --format=%s | grep -cE '^@?conductor:'
```

## C067: Twenty-four minutes from the empty repository to the first site commit

State: checked.

```
git log 298be4e --reverse --format='%h %ci %s' | head -2
```

## C068: Values reached the evidence vault's pushed history before they were redacted

State: checked.

```
git show 298be4e:evidence/updates/2026-10-29__the-vault-history-checked.md | sed -n 7,16p; git log -1 --format='%h %ci %s' aa7a3eb
```

## C069: How long the talk ran, from the transcript

State: checked.

```
git show a9c0b49:team/conductor/talk-record/transcript.json | python3 -c "import json,sys,collections;P=json.load(sys.stdin);print(len(P),P[0]['t'],P[-1]['t'],collections.Counter(p['who'] for p in P),sum(len(p['text'].split()) for p in P))"; git show a9c0b49:content/articles/the-talk-as-given.md | grep -o 'over about [0-9]* minutes'
```

## C070: Which beats reached the room: 46 of 58, and 8 of part 3's 20

State: checked.

```
git show 298be4e:src/static/talk/talk.json > /tmp/t.json; git show a9c0b49:team/conductor/talk-record/transcript.json > /tmp/tr.json; python3 -c "import json;b=json.load(open('/tmp/t.json'))['beats'];s={p['beat'] for p in json.load(open('/tmp/tr.json'))};[print(k,sum(1 for x in b if x['part']==k),sum(1 for x in b if x['part']==k and x['id'] in s)) for k in (1,2,3)]"
```

## C071: The hourly slots: each member's minute past the hour

State: checked.

```
git show 298be4e:team/conductor/schedule.json | python3 -c "import json,sys;[print(r['agent'],r['cron']) for r in json.load(sys.stdin)['runs']]"
```

## C072: Policies agreed against still in draft, at the end of the day

State: checked.

```
for f in $(git ls-tree -r --name-only 298be4e team | grep '/policy.json$'); do echo $f $(git show 298be4e:$f | python3 -c 'import json,sys;print(json.load(sys.stdin).get("status"))'); done
```

## C073: The talk's M03, 'Meet the team': its six counts as of 17:02:26

State: checked.

```
git show f45028c:src/static/motion/lab/meet-the-team/v1/team-in-numbers.json | head -45; git rev-list --count --no-merges --until=2026-10-29T17:02:26Z 298be4e; git rev-list --count --author='GitHub Actions' --until=2026-10-29T17:02:26Z 298be4e; git rev-list --count --no-merges --until=2026-10-29T05:59:59Z 298be4e; C=$(git rev-list -1 --until=2026-10-29T17:02:26Z 298be4e); for f in $(git ls-tree -r --name-only $C team | grep -E '/wakes/[^/]+\.json$'); do git show $C:$f | python3 -c 'import json,sys;print(json.load(sys.stdin).get("outcome") or "open")'; done | sort | uniq -c
```

## C074: Chapter 11b's quotations of the editor's own sites, found at their sources

State: open.

```
curl -s <page> | grep -ic '<quoted words>'
```

## C075: Leanpub's biggest books by readers shown: four lifetime bestsellers

State: checked.

```
curl -sL -A 'Mozilla/5.0' https://leanpub.com/<slug> | grep -oE '[0-9][0-9,]* *(</[^>]+> *)*(<[^>]+> *)*[Rr]eaders' | head -1 | sed -E 's/<[^>]+>//g'
```

## C076: Pwning OWASP Juice Shop: the one free-minimum security book on Leanpub with a large readers count shown

State: checked.

```
curl -sL -A 'Mozilla/5.0' https://leanpub.com/juice-shop | grep -oE '[0-9][0-9,]* *(</[^>]+> *)*(<[^>]+> *)*[Rr]eaders' | head -1 | sed -E 's/<[^>]+>//g'
```

## C077: The editor's own Leanpub books: 13,255 readers shown across eight

State: checked.

```
for s in Exploiting_MVC Thoughts_OWASP Practical_O2Platform Practical_Jni4Net Practical_AngularJS Practical_Git Practical_Eclipse hacking-portugal secdevops generation-z Software_Quality; do echo $s $(curl -sL -A 'Mozilla/5.0' https://leanpub.com/$s | grep -oE '[0-9][0-9,]* *(</[^>]+> *)*(<[^>]+> *)*[Rr]eaders' | head -1 | sed -E 's/<[^>]+>//g'); done
```

## C078: The talk's policy-gate and journey pieces: POC1's eleven actions, twice

State: checked.

```
git show 0fe0fff:src/static/studio-ports/data/report.json | python3 -c "import json,sys,collections;r=json.load(sys.stdin);print(len(r['rows']),collections.Counter(x['legacy'].split()[0] for x in r['rows']),collections.Counter(x['abp'].split()[0] for x in r['rows']),r['ledger'])"
```

## C079: The talk's abp piece: the ABP's rules and roles

State: open.

```
git show 0fe0fff:src/static/studio-ports/data/rules.json | python3 -c "import json,sys,collections;r=json.load(sys.stdin);print(len(r),collections.Counter(x['effect'] for x in r))"; git show 0fe0fff:src/static/studio-ports/data/abp.json | python3 -c "import json,sys;a=json.load(sys.stdin);print(len(a['roles']),a['valid_until'])"
```

## C080: The talk's pki piece: the register of people's bounds, and the 2019 failure

State: checked.

```
curl -s https://pki.sgit.ai/people/how.html | grep -o '256 statements[^.]*'
```

## C081: The talk's abp-review piece: 'By 17:40 the editor had agreed all ten'

State: open.

```
for c in bd3cdad 298be4e; do for f in $(git ls-tree -r --name-only $c team | grep '/policy.json$'); do git show $c:$f | python3 -c 'import json,sys;print(json.load(sys.stdin).get("status"))'; done | sort | uniq -c; done
```

## C082: The talk's E09 and E10 pieces: a coding agent's grant against its mandate, with confirmations on and off

State: checked.

```
git show eaf914f:src/static/studio/data/abp-examples.json | python3 -c "import json,sys,collections;a=json.load(sys.stdin);[print(e['settings'],e['grant'],e['mandate'],e['excess'],e['shortfall'],e['irreversible'],e['rows_measured'],collections.Counter(r['barrier_kind'] for r in e['rows'])) for e in a['examples'][:2]]"
```

## C083: The talk's SHarness piece: six of six probes held; what runs and since when

State: checked.

```
git show 842a8bd:src/static/studio/data/harness.json | python3 -c "import json,sys;h=json.load(sys.stdin);[print(p['id'],p['result']) for p in h['probes']];print(len(h['environments']));[print(c['status'][:90]) for c in h['components']]"
```

## C084: The talk's E02, E07 and E13 pieces: grant, mandate and excess for abp.sgit.ai's five published examples

State: checked.

```
git show 842a8bd:src/static/studio/data/abp-examples.json | python3 -c "import json,sys;[print(e['name'],e['grant'],e['mandate'],e['aligned'],e['excess'],e['unbounded_excess'],e['rows_measured']) for e in json.load(sys.stdin)['examples']]"
```

## C085: The talk's E03 piece: sixteen sources an agent reads, each with one public case

State: checked.

```
git show a606774:src/static/studio/data/injection-sources.json | python3 -c "import json,sys,collections;S=json.load(sys.stdin)['sources_an_agent_consumes'];print(len(S),collections.Counter(s['case']['label'] for s in S))"
```

## C086: The talk's E12 piece: the coding agent's excess by kind, and what the probes held

State: open.

```
git show 842a8bd:src/static/studio/data/abp-examples.json | python3 -c "import json,sys,collections;e=json.load(sys.stdin)['examples'][0];x=[r for r in e['rows'] if not r['in_mandate']];print(len(x),collections.Counter(r['mandate_stance'] for r in x),[r['capability'] for r in x])"
```

## C087: Wakes by trigger: scheduled, started by the editor, and follow-ups, by hour

State: checked.

```
for f in $(git ls-tree -r --name-only 298be4e team | grep -E '^team/[^/]+/wakes/[^/]+\.json$'); do git show 298be4e:$f | python3 -c 'import json,sys;d=json.load(sys.stdin);print(d["started"][11:13],d["kind"])'; done | python3 -c "import sys,collections;c=collections.Counter();[c.update([(l[:2],'scheduled' if l[3:].lower().startswith('scheduled') else 'follow-up' if ('follow' in l.lower() or 'tonight' in l.lower()) else 'editor')]) for l in sys.stdin];[print(k,v) for k,v in sorted(c.items())]"
```

## C088: Commits made with no wake of their member open

State: checked.

```
method: the script in team/researcher/debriefs/2026-10-31__a13-and-the-title-check.md
```

## Where this came from

`claims/register.json`, the `command` of each entry, run against `298be4e` (a full clone: `git rev-list --count 298be4e` gives 816) and `d39e717`; spot-checked on 30 October 05:45, 06:45, 07:45, 08:45, 09:40 and 10:50 (C011, C014, C021, C041, C042), each giving the registered value. C031's 2026 figure is read from a web page, fetched 30 October 2026. C043 to C062 were checked at source on 30 October about 13:20 UTC by the researcher's second session (public clones of OSBot-Utils, Memory-FS, Issues-FS, SGit-AI__CLI and myfeeds_ai; PyPI's JSON; the newsroom's wire; four LinkedIn pages' datePublished). C064 to C068, and the additions to C008 and C042, rerun on 30 October about 14:40 UTC. C069 to C072 rerun on 30 October about 16:45 UTC; C069 and C070 run at a9c0b49, material added after the day. C073 rerun on 30 October about 18:40 UTC. C074 checked on 30 October about 18:35 UTC. C011's command reads team/keys/ too since 30 October 20:40. C075 to C077 read from leanpub.com on 30 October about 20:40 UTC. C078 to C081 checked on 30 October about 22:40 UTC. C082 and C083 checked on 31 October about 00:45 UTC. C084 to C086 checked on 31 October about 00:50 UTC. C087 and C088 checked on 31 October about 04:50 UTC.
