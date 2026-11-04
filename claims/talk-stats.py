# claims/talk-stats.py: per-agent and team stats from the talk's record at 298be4e (C119, C120).
# Run it in a clone of SGit-AI__Website__Presentation__The-Ultimate-Insider (read only):
#   python3 /path/to/this/repository/claims/talk-stats.py
# Attribution is C014's: the subject's "@member:" or "member:" prefix, else the commit's "Agent: member@" trailer.
# Times are UTC, which was London time on 29 October 2026. "Product" files are everything outside team/ and REALITY.md.
import subprocess,re,collections,json,sys
R='298be4e'
out=subprocess.run(['git','log',R,'--no-merges','--numstat','--format=%x1e%h%x1f%an%x1f%ad%x1f%s%x1f%B%x1d','--date=format:%H:%M:%S'],capture_output=True,text=True).stdout
recs=out.split('\x1e')[1:]
M=collections.defaultdict(lambda: dict(commits=0,add=0,rem=0,padd=0,prem=0,files=set(),pfiles=set(),times=[],hours=set(),binary=0))
T=dict(commits=0,add=0,rem=0,files=set(),authors=collections.Counter())
for r in recs:
    head,_,rest=r.partition('\x1d')
    h,an,t,s,b=head.split('\x1f',4)
    stats=rest.strip().splitlines()
    T['authors'][an]+=1; T['commits']+=1
    for l in stats:
        a,rm,p=l.split('\t',2); T['files'].add(p)
        if a!='-': T['add']+=int(a); T['rem']+=int(rm)
    if an!='Claude': continue
    m=re.match(r'^@?([a-z][a-z.-]*):',s.strip()); ag=re.findall(r'^Agent:\s*([a-z.-]+)@',b,re.M)
    mem=m.group(1) if m else ag[0] if ag else ('conductor' if s.strip().startswith('Conductor') else '?')
    d=M[mem]; d['commits']+=1; d['times'].append(t); d['hours'].add(t[:2])
    for l in stats:
        a,rm,p=l.split('\t',2); d['files'].add(p)
        prod=not(p.startswith('team/') or p=='REALITY.md')
        if prod: d['pfiles'].add(p)
        if a=='-': d['binary']+=1; continue
        d['add']+=int(a); d['rem']+=int(rm)
        if prod: d['padd']+=int(a); d['prem']+=int(rm)
res={}
for k,d in sorted(M.items(),key=lambda x:-x[1]['commits']):
    ts=sorted(d['times'])
    res[k]=dict(commits=d['commits'],first=ts[0],last=ts[-1],hours_with_a_commit=len(d['hours']),files_touched=len(d['files']),lines_added=d['add'],lines_removed=d['rem'],product_files_touched=len(d['pfiles']),product_lines_added=d['padd'],product_lines_removed=d['prem'])
tot=dict(claude_commits=sum(v['commits'] for v in res.values()),non_merge_commits=T['commits'],by_author=dict(T['authors']),lines_added=T['add'],lines_removed=T['rem'],files_touched=len(T['files']))
# wakes: the wake records under team/<member>/wakes/ at 298be4e (C022), by member, with first and last start
W=collections.defaultdict(list)
for f in subprocess.run(['git','ls-tree','-r','--name-only',R],capture_output=True,text=True).stdout.split():
    if f.startswith('team/') and '/wakes/' in f and f.endswith('.json'):
        d=json.loads(subprocess.run(['git','show',R+':'+f],capture_output=True,text=True).stdout)
        W[f.split('/')[1]].append(d.get('started','')[11:19])
wakes={k:dict(wakes=len(v),first_start=min(v),last_start=max(v)) for k,v in W.items()}
tree=subprocess.run(['git','ls-tree','-r','-l',R],capture_output=True,text=True).stdout.splitlines()
tot['final_tree_files']=len(tree); tot['final_tree_bytes']=sum(int(l.split()[3]) for l in tree if l.split()[3]!='-')
tot['merges']=len(subprocess.run(['git','log',R,'--merges','--format=%h'],capture_output=True,text=True).stdout.split())
print(json.dumps(dict(members=res,wakes=wakes,team=tot),indent=1))
