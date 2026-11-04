# claims/talk-weight.py: the weight of the team's documents, and the sgit.ai references, at cb5b996 (C125, C126).
# Run in a clone of SGit-AI__Website__Presentation__The-Ultimate-Insider (read only):
#   python3 /path/to/this/repository/claims/talk-weight.py
import subprocess,json,re,collections
C='cb5b996'
def sh(*a): return subprocess.run(a,capture_output=True,text=True).stdout
def doc(p):
    t=sh('git','show',f'{C}:{p}'); return dict(path=p,bytes=len(t.encode()),words=len(t.split()),lines=t.count('\n')+(0 if t.endswith('\n') or not t else 1))
named=[doc(p) for p in ['BRIEF.md','REALITY.md','BRIEF-CORRECTIONS.md','CLAUDE.md']]
arts=[doc(p) for p in sh('git','ls-tree','-r','--name-only',C,'content/articles').split()]
tree=[l.split('\t',1) for l in sh('git','ls-tree','-r','-l',C).splitlines()]
md=sorted(((int(m.split()[3]) if m.split()[3]!='-' else 0,p) for m,p in tree if p.endswith('.md')),reverse=True)[:10]
top=[doc(p) for _,p in md]
team=[(int(m.split()[3]) if m.split()[3]!='-' else 0,p) for m,p in tree if p.startswith('team/')]
team_md=[p for _,p in team if p.endswith(('.md','.json'))]
teamdoc=dict(files=len(team),bytes=sum(b for b,_ in team))
refs_lines={};refs_occ=collections.Counter()
for l in sh('git','grep','-h','-o','-E',r'[A-Za-z0-9-]+\.sgit\.ai',C).splitlines(): refs_occ[l]+=1
for s in sorted(refs_occ):
    refs_lines[s]=len(sh('git','grep','-h','-F',s,C).splitlines())
refs=[dict(site=s,occurrences=refs_occ[s],matching_lines=refs_lines[s]) for s in sorted(refs_occ,key=lambda k:-refs_occ[k])]
print(json.dumps(dict(commit=C,named=named,articles=arts,top_md_by_bytes=top,team_folder=teamdoc,references=refs,reference_total_occurrences=sum(refs_occ.values())),indent=1))
