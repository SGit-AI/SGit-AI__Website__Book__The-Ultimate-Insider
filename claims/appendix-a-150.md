# Appendix A for the full book: every number, and how to rerun it

researcher@book.the-ultimate-insider, 3 November 2026, the 22:32 London wake, at the writer's letter 143. Every register id the full book (`manuscript/rc2/150/`, chapters 01 to 23, 90 and 91) cites, in order. Each entry gives its claim, its state, its source, the command that reproduces it, and the chapters that cite it. It is built from `claims/register.json`, which stays the only source: if this file and the register differ, the register holds.

**How to read it:**
- The commands do not all run against the same thing. Each runs against the source its entry names:
  - most run against the talk's repository at `298be4e`, the record of the day;
  - some run against material added to that repository after the day (`a9c0b49`, the transcript);
  - some run against this book's own repository;
  - some are web pages, read on the date given. A page may have changed since.
- Run the repository commands in a clone of the named repository, at the named commit.
- **Open** means the book must print the id as open, with what the record cannot show: C011, C037, C081 and C089. **Corrected** means the register corrected an earlier reading, and the book uses the corrected one.
- Nothing here is a key, a token or a contact detail.

## C001: First commit of the day

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapters 02, 04.

```
git log 298be4e --reverse --format='%h %ci %an %s' | head -1
```

## C005: Last work commit, last release of the day

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapter 16.

```
git log 298be4e --until=2026-10-29T19:00:00Z --format='%h %ci %an %s' | head -3
```

## C006: The hold

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapters 03, 15, 16, 17, 18, 90.

```
git log 298be4e --since=2026-10-29T18:44:00Z --until=2026-10-29T19:00:00Z --format='%h %ci %an %s'
```

## C011: Members of the talk's team

- **State:** open.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapters 02, 04, 05, 06, 08, 14, 90.

```
for m in dev conductor ruv-sgit researcher deck designer storyteller motion studio; do echo $m $(git log 298be4e --reverse --format='%h %ci' -- team/$m/key.json team/keys/$m.json | head -1); done; git log 298be4e --reverse --author=Claude --format='%h %ci %s' | grep -iE ' (@?(dev|conductor|deck|ruv-sgit|researcher|designer|storyteller|motion|studio):|Conductor joins)' | awk '!s[$4]++'
```

## C012: The storyteller joined about 14:12 UTC

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapters 12, 13.

```
git show 298be4e:team/storyteller/wakes/20261029T141252Z.json | head -6; git log 298be4e --reverse --format='%ci %h %s' -- team/storyteller/key.json | head -1
```

## C013: Motion and studio joined 15:30 to 16:00

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapter 14.

```
git log 298be4e --reverse --format='%ci %h %s' -- team/motion/key.json team/studio/key.json | head -2
```

## C014: Commits by member (Claude commits whose subject names a member, with or without @)

- **State:** corrected.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapters 03, 05, 09, 15, 17, 19, 90.

```
git rev-list --merges --count 298be4e; git log 298be4e --merges --author=Claude --format=%h | wc -l; then the attribution script in team/researcher/debriefs/2026-10-30__rc1-numbers-review.md
```

## C015: 58 beats in three parts

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapters 03, 90.

```
git show 298be4e:src/static/talk/talk.json | python3 -c "import json,sys,collections;b=json.load(sys.stdin)['beats'];print(len(b),collections.Counter(x['part'] for x in b))"
```

## C021: Usage reached 95% at the hold

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapter 16.

```
git log 298be4e -1 --author=Claude --format='%h %ci %s' --grep='95%'   # 867f8c2, 18:44:13; without --author the release 7968c99 (18:44:49) prints first
```

## C022: Wake records on the day

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapters 03, 06, 16, 19, 90.

```
python3 -c "import json,subprocess as s;R='298be4e';fs=[f for f in s.run(['git','ls-tree','-r','--name-only',R],capture_output=True,text=True).stdout.split() if f.startswith('team/') and '/wakes/' in f and f.endswith('.json')];import collections;print(len(fs),collections.Counter(f.split('/')[1] for f in fs))"
```

## C023: Step verdicts across the day's wake records

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapters 12, 14, 15, 18.

```
method: the script in team/researcher/debriefs/2026-10-30__rc1-numbers-review.md (parses every team/*/wakes/*.json at 298be4e; counts steps.<step>.verdict and history entries)
```

## C024: Holds written on the day

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapters 15, 16, 18.

```
git log 298be4e --diff-filter=A --format='%h %ci %s' -- 'team/*/HOLD.md'; git log 298be4e --diff-filter=D --format='%h %ci %s' -- 'team/*/HOLD.md'
```

## C025: Post-review findings and what each fixed

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapters 06, 07, 08, 09, 17, 18.

```
method: the C023 parse, selecting steps.post_review.verdict == 'finding', read with the same record's post_check comment
```

## C026: The talk's planned length

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapter 14.

```
git show 298be4e:src/static/talk/talk.json | python3 -c "import json,sys,collections;b=json.load(sys.stdin)['beats'];t=collections.Counter();[t.update({x['part']:x['dur']}) for x in b];print(sum(t.values())/60,{k:v/60 for k,v in t.items()})"
```

## C027: The part locks and their state at the hold

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapters 06, 14, 15, 16, 17, 18, 19.

```
git show 298be4e:team/conductor/HOLD.md; git ls-tree -r --name-only 298be4e | grep -i lock
```

## C028: When the player port landed

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapter 12.

```
git log 298be4e --format='%h %ci %s' -- src/static/talk/player.html | sed -n '1p;$p'; git log 298be4e --format=%h --since=2026-10-29T15:07:00Z --until=2026-10-29T18:37:03Z -- src/static/talk/player.html | wc -l
```

## C029: The talk's own claims register

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapters 11, 17.

```
git show 298be4e:evidence/claims/claims.json | python3 -c "import json,sys,collections;c=json.load(sys.stdin)['claims'];print(len(c),collections.Counter(x['grade'] for x in c),collections.Counter(x['holds'] for x in c))"
```

## C030: The talk's three claims that do not hold

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapters 11, 13, 17.

```
git show 298be4e:evidence/claims/claims.json | python3 -c "import json,sys;[print(x['id'],x['where']) for x in json.load(sys.stdin)['claims'] if x['holds']=='does not hold']"
```

## C031: $17.4M, the average annual cost of insider risk, on the talk's definition slide

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`; also web pages, as the register names them.
- **Cited in:** chapters 07, 17.

```
git log 298be4e -S'data-count="17.4"' --format='%h %ci %s' -- src/static/talk/slides/definition/index.html; git show 298be4e:evidence/proposals/deck-talk-changes.md | grep -n '19.5'; then read https://ponemon.dtex.ai/ (the public landing page; the full report is behind a form, not filled in); git show 298be4e:team/deck/requests/researcher__before-tonight.md | grep -n 'frozen'; git log 298be4e --no-merges --format='%h %ci' -- src/static/talk/slides/definition/index.html
```

## C037: What the day cost the editor, in hours and usage

- **State:** open.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapter 23.

```
git grep -n -iE 'usage[^"]{0,80}[0-9]+ ?%' 298be4e -- team ':!*.png'
```

## C065: The hold's gap: the designer's work commit 82 seconds after the hold

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapters 16, 18.

```
git log -1 --format='%h %ci' 867f8c2; git log -1 --format='%h %ci' 88b8f00
```

## C067: Twenty-four minutes from the empty repository to the first site commit

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapter 04.

```
git log 298be4e --reverse --format='%h %ci %s' | head -2
```

## C068: Values reached the evidence vault's pushed history before they were redacted

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapters 09, 17.

```
git show 298be4e:evidence/updates/2026-10-29__the-vault-history-checked.md | sed -n 7,16p; git log -1 --format='%h %ci %s' aa7a3eb
```

## C069: How long the talk ran, from the transcript

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `a9c0b49` (material added after the day).
- **Cited in:** chapter 01.

```
git show a9c0b49:team/conductor/talk-record/transcript.json | python3 -c "import json,sys,collections;P=json.load(sys.stdin);print(len(P),P[0]['t'],P[-1]['t'],collections.Counter(p['who'] for p in P),sum(len(p['text'].split()) for p in P))"; git show a9c0b49:content/articles/the-talk-as-given.md | grep -o 'over about [0-9]* minutes'
```

## C071: The hourly slots: each member's minute past the hour

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapter 05.

```
git show 298be4e:team/conductor/schedule.json | python3 -c "import json,sys;[print(r['agent'],r['cron']) for r in json.load(sys.stdin)['runs']]"
```

## C072: Policies agreed against still in draft, at the end of the day

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapters 01, 90.

```
for f in $(git ls-tree -r --name-only 298be4e team | grep '/policy.json$'); do echo $f $(git show 298be4e:$f | python3 -c 'import json,sys;print(json.load(sys.stdin).get("status"))'); done
```

## C081: The talk's abp-review piece: 'By 17:40 the editor had agreed all ten'

- **State:** open.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `bd3cdad and 298be4e`.
- **Cited in:** chapters 01, 90.

```
for c in bd3cdad 298be4e; do for f in $(git ls-tree -r --name-only $c team | grep '/policy.json$'); do git show $c:$f | python3 -c 'import json,sys;print(json.load(sys.stdin).get("status"))'; done | sort | uniq -c; done
```

## C087: Wakes by trigger: scheduled, started by the editor, and follow-ups, by hour

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapters 07, 08, 09, 10, 12, 15.

```
for f in $(git ls-tree -r --name-only 298be4e team | grep -E '^team/[^/]+/wakes/[^/]+\.json$'); do git show 298be4e:$f | python3 -c 'import json,sys;d=json.load(sys.stdin);print(d["started"][11:13],d["kind"])'; done | python3 -c "import sys,collections;c=collections.Counter();[c.update([(l[:2],'scheduled' if l[3:].lower().startswith('scheduled') else 'follow-up' if ('follow' in l.lower() or 'tonight' in l.lower()) else 'editor')]) for l in sys.stdin];[print(k,v) for k,v in sorted(c.items())]"
```

## C088: Commits made with no wake of their member open

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapters 02, 16, 17.

```
method: the script in team/researcher/debriefs/2026-10-31__a13-and-the-title-check.md
```

## C089: Why the team stopped: the editor's own account, given after the day, against the day's record

- **State:** open.
- **Source:** SGit-AI__Website__Book__The-Ultimate-Insider, at `49c701e` (this book's own record, after the day).
- **Cited in:** chapters 16, 17, 20.

```
git show 49c701e:briefs/2026-10-31__rc1-paper-review/batch-07-pages-22-to-32.md | grep -o -i '.\{100\}just a footnote.\{300\}'; git show 298be4e:team/conductor/HOLD.md | head -5   # the second in the talk's repository; git show ec1ec00:briefs/2026-10-31__in-session/02-g1-the-95-and-the-day-in-review.md | grep -o -i '.\{20\}95%, I think.\{100\}'
```

## C095: The talk's commits by member and by hour, 00:00 to 18:59 on 29 October (for the LK1 chart)

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapters 08, 09, 12.

```
git log 298be4e --no-merges --until=2026-10-29T18:59:59Z --format='%cI|%an|%s' | python3 -c "import sys,re,collections;c=collections.Counter();[c.update([(('releases' if a=='GitHub Actions' else (re.match(r'@([a-z.-]+):',s).group(1) if re.match(r'@([a-z.-]+):',s) else 'other')),t[11:13])]) for t,a,s in (l.rstrip().split('|',2) for l in sys.stdin)];[print(k,v) for k,v in sorted(c.items())]"
```

## C100: When and where the talk was to be given

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e; a9c0b49` (material added after the day).
- **Cited in:** chapters 01, 15, 16, 17, 19.

```
git grep -n 'talk starts at 19:00 London' 298be4e; git grep -n 'hack::soho' a9c0b49 -- content/articles/the-talk-as-given.md
```

## C101: What a reader pays to start: the published prices of the plans, as read

- **State:** checked.
- **Source:** web pages read on 2026-11-02: https://claude.com/pricing, https://lovable.dev/pricing.
- **Cited in:** chapter 23.

```
open https://claude.com/pricing and https://lovable.dev/pricing; read the plan prices as shown on the date
```

## C102: A moment in the talk as given where the animation carried the point (the building, M01)

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `a9c0b49 (added after the day); 298be4e for M01` (material added after the day).
- **Cited in:** chapter 01.

```
git show a9c0b49:content/articles/the-talk-as-given.md | grep -n 'id="building"'
```

## C103: Inventing on Principle: speaker, venue, year and the principle in his words

- **State:** checked.
- **Source:** web pages read on 2026-11-02: https://jamesclear.com/great-speeches/inventing-on-principle-by-bret-victor.
- **Cited in:** chapter 02.

```
open https://jamesclear.com/great-speeches/inventing-on-principle-by-bret-victor and find 'That's my principle'
```

## C104: When chapter 6's decisions of the afternoon were made and recorded, 29 October

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapters 02, 11, 12, 13, 14.

```
git show -s --format='%h %ci %s' c9ced4e 78d517d 545a473 f00734f c3f546e
```

## C105: The editor's afternoon asks that carry his own time in a commit subject, and when each came back

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapters 02, 12, 15, 16.

```
git log 298be4e --format='%h %ci %s' | grep -E 'the editor,? ([0-9]{1,2}:[0-9]{2})' | grep -v ' site v'
```

## C107: Two checks of the small hours: the researcher's dispute with its reviewer (04:11) and deck's request held by its reviewer (04:19)

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapters 08, 10.

```
git show 298be4e:team/researcher/wakes/20261029T041003Z.json | grep -o '"at": "[^"]*"'; git show 298be4e:team/deck/wakes/20261029T041822Z.json | grep -o '"at": "[^"]*"'
```

## C109: A second moment in the talk as given: the policy review page, at 58:53

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `a9c0b49` (material added after the day).
- **Cited in:** chapters 01, 90.

```
git show a9c0b49:content/articles/the-talk-as-given.md | grep -n 'id="s-port-abp-review"'
```

## C110: The day by clock hour, for the margin clock: commits, agents' commits, wakes and members on stage in and up to each clock hour

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `298be4e`.
- **Cited in:** chapters 01, 02, 04, 05, 07, 08, 09, 10, 12, 13, 14, 15, 16, 91.

```
see claims/the-clock.md, 'How to rerun' (clock-hour bounds)
```

## C111: A third moment in the talk as given: the Wardley map, at 19:27

- **State:** checked.
- **Source:** SGit-AI__Website__Presentation__The-Ultimate-Insider, at `a9c0b49` (material added after the day).
- **Cited in:** chapter 01.

```
git show a9c0b49:content/articles/the-talk-as-given.md | grep -n 'here.s a Wardley map'
```

## C112: This book's team: tool calls by review steps outside the read-only brief (TA1), as security's register counts them

- **State:** checked.
- **Source:** SGit-AI__Website__Book__The-Ultimate-Insider (this book's record), at `38b69644` (this book's own record, after the day).
- **Cited in:** chapter 18.

```
git show 38b69644:controls/index.json | python3 -c "import json,sys;d=json.load(sys.stdin)['book_team']['tool_cases'];[print(c['n'],c['tool'][:30],c.get('refused')) for c in d['cases']]"
```

## Where this came from

`claims/register.json` as on dev at the 22:32 wake, 3 November 2026; every C-id found in `manuscript/rc2/150/*.md` at that wake (42 ids, each in the register with a command). Built by the researcher on 3 November 2026, about 22:35 UTC.
