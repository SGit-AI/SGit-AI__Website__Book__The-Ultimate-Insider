# claims/talk-repo-by-hour.py: the talk's repository at the end of each clock hour of 29 October 2026 (C124).
# Run in a clone of SGit-AI__Website__Presentation__The-Ultimate-Insider (read only):
#   python3 /path/to/this/repository/claims/talk-repo-by-hour.py
# For each hour H (00 to 18): the last commit on the first-parent line of cb5b996 (the day's last release, v0.1.209, 18:46:22)
# made at or before H:59:59 UTC (London time that day); its tree's files by kind, and its size in bytes.
import subprocess,json,collections
END='cb5b996'
def sh(*a): return subprocess.run(a,capture_output=True,text=True).stdout
def kind(p):
    e=p.rsplit('.',1)[-1].lower() if '.' in p.rsplit('/',1)[-1] else ''
    return e if e in ('md','json','html','svg','js','css') else 'other'
def tree(c):
    k=collections.Counter(); b=collections.Counter(); n=0; size=0
    for l in sh('git','ls-tree','-r','-l',c).splitlines():
        meta,p=l.split('\t',1); parts=meta.split(); s=0 if parts[3]=='-' else int(parts[3])
        kk=kind(p); k[kk]+=1; b[kk]+=s; n+=1; size+=s
    return dict(files=n,bytes=size,by_kind=dict(k),bytes_by_kind=dict(b))
rows=[]
for h in range(0,19):
    c=sh('git','rev-list','-1','--first-parent',f'--before=2026-10-29 {h:02d}:59:59 +0000',END).strip()
    if not c: rows.append(dict(hour=f'{h:02d}',commit=None)); continue
    t=sh('git','log','-1','--format=%ad','--date=format:%H:%M:%S',c).strip()
    rows.append(dict(hour=f'{h:02d}',commit=c[:7],commit_time=t,**tree(c)))
end=dict(commit=END,**tree(END))
final=dict(commit='298be4e',**tree('298be4e'))
print(json.dumps(dict(hours=rows,day_end=end,final_state=final),indent=1))
