# claims/book-team-stats.py: this book's team in numbers, as of a stated commit (C131).
# Run in a clone of SGit-AI__Website__Book__The-Ultimate-Insider (read only):
#   python3 claims/book-team-stats.py [commit]      (default HEAD)
# Attribution is C014's: the subject's "@member:" or "member:" prefix, else the commit's "Agent: member@" trailer.
# A commit by Claude with neither prefix nor trailer is the first session's, before the "@" convention (30 October, 00:35 to 01:17): it is counted for the conductor, the session that was staffed as the conductor at 00:56:04. Releases (author GitHub Actions) and the editor's own commit are counted apart.
# Times are UTC. "Wakes" are the wake records under team/<member>/wakes/ at that commit. These numbers grow every hour.
import subprocess,re,collections,json,sys
C=sys.argv[1] if len(sys.argv)>1 else 'HEAD'
def sh(*a): return subprocess.run(a,capture_output=True,text=True).stdout
head=sh('git','rev-parse','--short',C).strip()
out=sh('git','log',C,'--no-merges','--format=%x1e%h%x1f%ad%x1f%an%x1f%s%x1f%B','--date=format:%d %b %H:%M:%S')
other=collections.Counter(); early=0
M=collections.defaultdict(list)
for r in out.split('\x1e')[1:]:
    h,t,an,s,b=r.split('\x1f',4)
    m=re.match(r'^@?([a-z][a-z0-9.-]*):',s.strip()); ag=re.findall(r'^Agent:\s*([a-z0-9.-]+)@',b,re.M)
    who=m.group(1) if m else ag[0] if ag else '?'
    if who=='?':
        if an=='Claude': who='conductor'; early+=1
        else: other[an]+=1; continue
    M[who].append(t)
files=sh('git','ls-tree','-r','--name-only',C).split()
wakes=collections.Counter(f.split('/')[1] for f in files if f.startswith('team/') and '/wakes/' in f and f.endswith('.json'))
members=sorted(d for d in {f.split('/')[1] for f in files if f.startswith('team/') and f.endswith('/policy.json')})
res={}
for m in members:
    ts=M.get(m,[])
    res[m]=dict(commits=len(ts),first_commit=ts[-1] if ts else None,last_commit=ts[0] if ts else None,wakes=wakes.get(m,0))
tot=sum(len(v) for v in M.values())
print(json.dumps(dict(as_of=head,members=res,member_commits=tot,counted_apart=dict(other),early_first_session_counted_for_the_conductor=early,merges=len(sh('git','log',C,'--merges','--format=%h').split())),indent=1))
