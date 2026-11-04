# Researcher's claims/talk-pages-rule.py with its two faults repaired, for the historian's diff of 4 November 2026 (read only).
# Repairs: (1) the host may be the bare apex sgit.ai (the original needs a character before "sgit.ai"); (2) trailing . , : ; * ) are stripped from a path. Result at cb5b996: 1,110 pages on 35 hosts, the same as past_projects_scan.py with the trailing slash folded.
# claims/talk-pages-rule.py: the distinct sgit.ai pages in the lines the talk's commits added (C127, "distinct_pages_by_my_rule").
# Run in a clone of SGit-AI__Website__Presentation__The-Ultimate-Insider (read only):
#   python3 /path/to/this/repository/claims/talk-pages-rule.py [--list]
# Rule: for every non-merge commit reachable from cb5b996, the added lines (git log -p -U0 -G 'sgit\.ai'); in each, every match of
#   (https?://)? HOST PATH   with HOST = [A-Za-z0-9][A-Za-z0-9.-]*sgit\.ai  and PATH = (/[^\s)"'<>\]\\,;`|}]*)?
# A page is (HOST, PATH) with the query and fragment dropped (everything from the first ? or #) and the trailing slash dropped.
# A bare host (no scheme) counts. Case is not folded. A bare host and the same host with "/" are one page.
import subprocess,re,sys
out=subprocess.run(['git','log','-p','--reverse','-U0','--no-merges','-G','sgit\\.ai','cb5b996','--format=%x1e%h'],capture_output=True,text=True,errors='replace').stdout
pat=re.compile(r'(?:https?://)?((?<![A-Za-z0-9.-])(?:[A-Za-z0-9][A-Za-z0-9.-]*\.)?sgit\.ai)(/[^\s)"\'<>\]\\,;`|}]*)?')
pages=set(); added=0
for blk in out.split('\x1e')[1:]:
    for l in blk.splitlines()[1:]:
        if l.startswith('+') and not l.startswith('+++'):
            for m in pat.finditer(l):
                added+=1
                h,p=m.group(1),(m.group(2) or '')
                p=re.split(r'[?#]',p)[0].rstrip('/.,:;*)')
                pages.add((h,p))
if '--list' in sys.argv:
    for h,p in sorted(pages): print(h+p)
else:
    print('distinct pages',len(pages),'hosts',len({h for h,_ in pages}),'mentions in added lines',added)
