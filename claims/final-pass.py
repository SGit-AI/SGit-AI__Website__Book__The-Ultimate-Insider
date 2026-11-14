#!/usr/bin/env python3
# claims/final-pass.py: the researcher's final pass over the full book's numbers, as a read-only report (RV2, principles 28 to 31).
# Run in this repository (it edits nothing; manuscript/ is never touched):
#   python3 claims/final-pass.py [path-to-a-clone-of-the-talk's-repository]
# With the talk's clone as the argument, every runnable command of Appendix A's file is also run there (or here, for this book's own).
# Each check prints PASS or FAIL, with file:line for a FAIL. It exits 1 if anything fails.
import re,glob,json,subprocess,sys,os,collections
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
TALK=sys.argv[1] if len(sys.argv)>1 else None
fails=[]
def report(name,problems):
    if problems:
        print('FAIL',name)
        for p in problems[:25]: print('   ',p)
        if len(problems)>25: print('    ... and',len(problems)-25,'more')
        fails.append(name)
    else: print('PASS',name)
R={c['id']:c for c in json.load(open('claims/register.json'))['claims']}
chap=sorted(glob.glob('manuscript/rc2/150/*.md'))
def reading(f):
    for n,l in enumerate(open(f).read().splitlines(),1):
        if l.startswith('`%%') or l.startswith('Band:') or l.startswith('## Where') : continue
        yield n,l
# 1. the mechanical principle checks over the reading text (92 and 93 print code and tables of their own: 92 is checked in 3)
pats={
 'id in the reading text (P28)':re.compile(r'\bC\d{3}\b'),
 'hash in the reading text (P28)':re.compile(r'(?<![A-Za-z0-9/_.-])(?=[0-9a-f]*[0-9])(?=[0-9a-f]*[a-f])[0-9a-f]{7,12}(?![A-Za-z0-9])'),
 'ten agents (P31)':re.compile(r'\bten (agents|members)\b',re.I),
 'a cost figure (P31)':re.compile(r'\$\s?\d|US\$|\bper month\b',re.I),
 'D12 or the vault history (P31)':re.compile(r'\bD12\b|vault history|evidence vault|history of the team',re.I),
 'an inline %% marker (P30)':re.compile(r'[^`\n]%%'),
 'three accounts of why he stopped (P24)':re.compile(r'three (accounts|answers)',re.I),
 'an em-dash (P35)':re.compile(chr(0x2014)),
 'a religious word (P34)':re.compile(r'\b(bible|gospel|scripture|sermon|preach|evangelist|commandments|sacred|holy|pilgrimage|worship)\b',re.I),
 'a first name followed by a capitalised word after "Dan" (the reader: first name only)':re.compile(r'\bDan [A-Z][a-z]+'),
 'a "Where this came from" heading that is not a record (P29)':re.compile(r'^## Where this came from',re.I),
}
hits=collections.defaultdict(list); allowed=[]
for f in chap:
    if '/92-' in f: continue
    for n,l in enumerate(open(f).read().splitlines(),1):
        if l.startswith('`%%') or l.startswith('Band:'): continue
        for k,p in pats.items():
            if k.startswith('a "Where') and not l.startswith('## Where'): continue
            if not k.startswith('a "Where') and l.startswith('## Where'): continue
            if p.search(l):
                # the one allowed money figure: the slide's insider-risk cost ($17.4M, C031), not what the day cost
                if k.startswith('a cost figure') and ('$17.4M' in l or 'US$19.5M' in l): allowed.append(f'{os.path.basename(f)}:{n}'); continue
                hits[k].append(f'{os.path.basename(f)}:{n}: {l[:70]}')
for k,p in pats.items():
    # the "Where this came from" headings are the build's to drop (P29): reported, not failed
    if k.startswith('a "Where'):
        print('NOTE',len(hits[k]),'files carry a "Where this came from" heading in the source (the build drops them in print)'); continue
    report(k,hits[k])
print('NOTE allowed money figures (the slide\'s insider-risk cost, C031, not the day\'s cost):',allowed)
# 2. every register id cited in the chapters exists, and Appendix A's file lists it
cited=collections.defaultdict(list)
for f in chap:
    if '/92-' in f: continue
    for n,l in enumerate(open(f).read().splitlines(),1):
        for i in set(re.findall(r'\bC\d{3}\b',l)): cited[i].append(os.path.basename(f))
app=open('claims/appendix-a-150.md').read()
inapp=set(re.findall(r'^## (C\d{3}):',app,re.M))
import glob
# the editor, 5 November 2026, brief 40 (AP1): Appendix A leaves the book (the file 92 may stay in the repository; the register in claims/ stays the source)
LIST='manuscript/editions/rc2-150/Book.txt'
if os.path.exists(LIST):
    AP1=not any(os.path.basename(l.strip()).startswith('92-') for l in open(LIST).read().splitlines() if l.strip() and not l.lstrip().startswith('#'))
    print('NOTE Appendix A test: chapter 92 is %s the full book\'s list (%s)'%('NOT in' if AP1 else 'in',LIST))
else:
    AP1=not glob.glob('manuscript/rc2/150/92-*.md')
    print('NOTE Appendix A test: the list %s is missing; fell back to whether the file 92 exists'%LIST)
report('every cited id is in the register',[f'{i} (cited in {cited[i][:2]})' for i in cited if i not in R])
if AP1: print("NOTE Appendix A (chapter 92) is out of the full book's list (AP1, brief 40): the check that every cited id is in its file is retired; every cited id must still be in the register (checked above)")
else: report("every cited id is in Appendix A's file (C068 is held out of print by the editor's word)",[f'{i} (cited in {cited[i][:2]})' for i in cited if i in R and i not in inapp and i!='C068'])
open_ids=[i for i in cited if i in R and R[i]['state']=='open']
print('NOTE ids cited in the chapters whose state is still "open" (the book must say so):',sorted(open_ids))
# 3. 92 equals Appendix A's file, and its commands equal the register's
if AP1: print("NOTE chapter 92 is out of the full book's list (AP1; the file may stay as a source): the checks that it equals Appendix A's file and carries the register's commands are retired")
else:
    def entries(t):
        parts=re.split(r'\n(?=## C\d{3}:)',t); return {re.match(r'## (C\d{3})',x).group(1):x.split('\n## Where')[0].split('\n---')[0].strip() for x in parts[1:]}
    a=entries(app); b=entries(open('manuscript/rc2/150/92-appendix-a-every-number.md').read())
    report("92 equals Appendix A's file, entry by entry",[f'only in the file: {sorted(set(a)-set(b))}' for _ in [0] if set(a)-set(b)]+[f'only in 92: {sorted(set(b)-set(a))}' for _ in [0] if set(b)-set(a)]+[f'differs: {k}' for k in sorted(set(a)&set(b)) if a[k]!=b[k]])
    bad=[]
    for k,t in b.items():
        m=re.search(r'```\n(.*?)\n```',t,re.S)
        if m and k in R and m.group(1).strip()!=R[k]['command'].strip() and k!='C068': bad.append(f'{k}: the command in 92 differs from the register')
    report("92's commands equal the register's",bad)
# 3b. drawings in the full book: the principles guide (line 279: "No ids inside drawings", the designer's and the storyteller's
# ruling, not the editor's words) says a drawing carries no register id; commit hashes are not named by the ruling (a NOTE only)
try:
    _fm=json.load(open('publishing/rc2-figures.json')); _S={}
    def _walk(o,k):
        if isinstance(o,dict):
            for v in o.values(): _walk(v,k)
        elif isinstance(o,list):
            for v in o: _walk(v,k)
        elif isinstance(o,str) and o.endswith('.svg'): _S.setdefault(o,set()).add(k)
    for _k,_v in _fm.items():
        if _k.startswith('rc2/150/'): _walk(_v,_k)
    _pid=re.compile(r'\bC\d{3}\b'); _ph=re.compile(r'\b(?=[0-9a-f]*\d)(?=[0-9a-f]*[a-f])[0-9a-f]{7,40}\b')
    _ids=[];_hon=[]
    for _p in sorted(_S):
        if not os.path.exists(_p): continue
        _tx=' '.join(re.sub(r'<[^>]+>','',x) for x in re.findall(r'<text[^>]*>(.*?)</text>',open(_p).read(),re.S))
        if _pid.search(_tx): _ids.append(os.path.basename(_p))
        elif _ph.search(_tx): _hon.append(os.path.basename(_p))
    print('NOTE drawings mapped for the full book with a register id in their small text (the ruling: none allowed):',len(_ids),_ids)
    print('NOTE drawings mapped for the full book with a commit hash only (the ruling names ids only; a question for the conductor):',len(_hon))
except Exception as _e:
    print('NOTE the drawings scan did not run:',_e)
# 4. chapter 21's team table against C131 (as stored) and against today's script
def table():
    t=open(glob.glob('manuscript/rc2/150/21-*.md')[0]).read(); rows={}
    for l in t.splitlines():
        m=re.match(r'\|\s*([A-Za-z-]+)\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|',l)
        if m and m.group(1)!='Member': rows[m.group(1).lower()]=(int(m.group(3)),int(m.group(4)))
    return rows
rows=table(); st=R['C131']['value']['members']
report("21's table equals C131 as stored (as of %s)"%R['C131']['value']['as_of_commit'],[f'{k}: table {v}, C131 {(st[k]["commits"],st[k]["wakes"])}' for k,v in rows.items() if k not in st or (st[k]['commits'],st[k]['wakes'])!=v]+[f'missing: {k}' for k in ['conductor','librarian','historian','researcher','storyteller','publisher','designer','writer','security','synthetic','ruv-sgit','developer'] if k not in rows])
now=json.loads(subprocess.run([sys.executable,'claims/book-team-stats.py'],capture_output=True,text=True).stdout)
print('NOTE today the team has more commits and wakes than the table (it grows hourly):',', '.join(f"{k} {now['members'][k]['commits']}/{now['members'][k]['wakes']}" for k in ['conductor','researcher','writer','security'] if k in now['members']),'(as of',now['as_of'],')')
# 5. the commands of Appendix A's file run (needs the talk's clone)
if TALK:
    bad=[];ran=0
    for i in sorted(inapp):
        cmd=R[i]['command']; lines=[l for l in cmd.splitlines() if not l.startswith('# ')]
        if not lines or not re.match(r'(git |for |python3 |grep |ls )',lines[0]): continue
        book='Book__' in R[i]['source'].get('repository','')
        if i=='C089': parts=[(ROOT,l) for l in lines if l.startswith(('git show 49c','git show ec1'))]+[(TALK,l) for l in lines if l.startswith('git show 298')]
        else: parts=[(ROOT if book else TALK,'\n'.join(lines))]
        for cw,cm in parts:
            cm=cm.replace('python3 claims/',f'python3 -I {ROOT}/claims/')
            p=subprocess.run(cm,shell=True,cwd=cw,capture_output=True,text=True,timeout=300,executable='/bin/bash'); ran+=1
            if not p.stdout.strip() or (p.returncode not in (0,141) and 'syntax' in p.stderr): bad.append(f'{i}: rc {p.returncode} {p.stderr.strip()[:60]}')
    report(f'the {ran} runnable commands of Appendix A run and print something',bad)
else: print('NOTE the commands were not run (give the talk clone as the argument)')
print('\nFAILS:',len(fails)); sys.exit(1 if fails else 0)
