#!/usr/bin/env python3
"""Rerun the page count of past_projects_scan.py with one rule changed: the trailing slash folded.

Read only and offline. Usage: python3 past_projects_rule_diff.py <clone of the talk's repository>
Prints the count under the scan's own rule (1,116 pages on 35 hosts at cb5b996), then under the folded rule,
then a few facts about the page set (bare hosts, single-page hosts, file extensions) for diffing against
another counter's rule. It does not try to guess another counter's regex.
"""
import re,subprocess,sys
clone=sys.argv[1]; end="cb5b996"
URL=re.compile(r'((?:https?://)?(?:[a-z0-9-]+\.)*sgit\.ai)((?:/[A-Za-z0-9_.%~#?=&+-]*)*)')
def git(*a): return subprocess.run(["git","-C",clone,*a],capture_output=True,text=True,errors="replace").stdout
def page(m,fold=False):
    h=m.group(1).replace("https://","").replace("http://","")
    p=re.sub(r"[#?].*$","",m.group(2).rstrip(".,);:'\"*`>]")) or "/"
    if fold and len(p)>1: p=p.rstrip("/") or "/"
    return h,p
log=git("log","-p","--reverse","--no-color","-U0","-G",r"sgit\.ai","--format=@@C|%ad|%an|%s",end)
S={}
for name,kw in [("mine",{}),("fold",{"fold":True})]:
    s=set()
    for l in log.split("\n"):
        if l.startswith("+") and not l.startswith("+++") and "sgit.ai" in l:
            for m in URL.finditer(l): s.add(page(m,**kw))
    S[name]=s
for k,s in S.items(): print(k,len(s),len({h for h,_ in s}))
st={(h,p) for h,p in S["fold"] if not re.search(r"[%~=&+]",p) and not p.endswith(".")}
print("fold+strictchars",len(st),len({h for h,_ in st}))
dropped=[x for x in S["fold"] if x not in st]; print("dropped by strict chars:",len(dropped),dropped[:8])
print("hosts lost:",{h for h,_ in S["fold"]}-{h for h,_ in st})
import collections
c=collections.Counter(h for h,_ in S["fold"])
print("hosts with 1 page:",[h for h,n in c.items() if n==1])
bare={(h,p) for h,p in S["fold"] if p=="/"}; print("bare hosts:",len(bare))
nonbare=S["fold"]-bare; print("without bare hosts",len(nonbare))
ext=[x for x in S["fold"] if re.search(r"\.(css|js|json|svg|png|jpg|html|md|py)$",x[1])]; print("with file extension:",len(ext))
dots=[x for x in S["fold"] if x[1].endswith(("-","_"))]; print("ending - or _:",len(dots),dots[:5])
star=[x for x in S["fold"] if re.search(r"[<>{}\\]",x[1])]; print(len(star))
odd=[x for x in S["fold"] if re.search(r"(%|~|=|&|\+|\.\.)",x[1])]; print("odd chars:",len(odd),odd[:5])
