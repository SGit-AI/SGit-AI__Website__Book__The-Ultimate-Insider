# The team, read from the folders under team/<id>/. Standard library only. Apache-2.0.
#
#   python3 admin/build/agents.py check --agent dev [--base origin/dev]   files changed since base, against dev's scope; and any change to its own scope
#   python3 admin/build/agents.py overlaps                                two members claiming the same file (the gate fails)
#   python3 admin/build/agents.py unowned                                 tracked files no member writes or holds
#
# A scope is a setting, not a boundary: the agent can edit its own policy.json. It catches mistakes, not a steered agent.

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEAM = ROOT / 'team'


class Team:
    def __init__(self):
        self.members = {}
        for folder in sorted(p for p in TEAM.iterdir() if p.is_dir()) if TEAM.exists() else []:
            policy = folder / 'policy.json'
            if policy.exists():
                self.members[folder.name] = json.loads(policy.read_text())

    def pattern(self, glob):                                         # ** crosses folders, * does not
        rx = re.escape(glob).replace(r'\*\*', '\u0000').replace(r'\*', '[^/]*').replace('\u0000', '.*')
        return re.compile('^' + rx + '$')

    def owns(self, agent, path, kinds=('writes', 'holds')):
        scope = self.members[agent].get('scope', {})
        return any(self.pattern(g).match(path) for kind in kinds for g in scope.get(kind, []))

    def appends(self, agent, path):
        return any(path == a.split(':')[0].split('#')[0].strip() for a in self.members[agent].get('scope', {}).get('appends', []))

    def tracked(self):
        out = subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True).stdout
        return [f for f in out.splitlines() if f]

    def changed(self, agent, base):
        # the member's own commits only, marked the house way ("@<id>:" in the subject or "Agent: <address>" in the body), plus the
        # working tree: work carried in from another member's branch, by a merge or a fast-forward, is not counted against this one
        address = self.members[agent].get('address', agent)
        log     = subprocess.run(['git', 'log', '--no-merges', '--format=%H%x1f%s%x1f%b%x1e', f'{base}..HEAD'], cwd=ROOT, capture_output=True, text=True).stdout
        mine    = [r.split('\x1f')[0].strip() for r in log.split('\x1e') if r.strip() and (r.split('\x1f')[1].startswith(f'@{agent}:') or f'Agent: {address}' in r)]
        files   = set()
        for sha in mine:
            files |= set(subprocess.run(['git', 'show', '--name-only', '--format=', sha], cwd=ROOT, capture_output=True, text=True).stdout.split())
        # the working tree's uncommitted files count for whoever is checked: run for another member (a post-review may), read those lines with that in mind (security, 30 October 2026)
        local = subprocess.run(['git', 'status', '--porcelain'], cwd=ROOT, capture_output=True, text=True).stdout
        files |= {line[3:].split(' -> ')[-1] for line in local.splitlines()}
        return sorted(f for f in files if f and f != 'version')

    def scope_changes(self, agent, base):                            # security's proposal (30 October 2026): a member's own scope, changed since the base, is reported
        path   = f'team/{agent}/policy.json'
        before = subprocess.run(['git', 'show', f'{base}:{path}'], cwd=ROOT, capture_output=True, text=True)
        old    = json.loads(before.stdout).get('scope', {}) if before.returncode == 0 and before.stdout.strip() else {}
        new    = self.members[agent].get('scope', {})
        lines  = []
        for kind in ('writes', 'holds', 'appends'):
            a, b = set(old.get(kind, [])), set(new.get(kind, []))
            lines += [f'scope changed: +{kind} {x}' for x in sorted(b - a)] + [f'scope changed: -{kind} {x}' for x in sorted(a - b)]
        was = json.loads(before.stdout) if before.returncode == 0 and before.stdout.strip() else {}
        now = self.members[agent]                                   # security's note: a line removed from never, or a capability added, widens too
        a, b = set(was.get('never', [])), set(now.get('never', []))
        lines += [f'scope changed: +never {x}' for x in sorted(b - a)] + [f'scope changed: -never {x} (a widening)' for x in sorted(a - b)]
        for kind in ('wanted', 'not_wanted'):
            cap = lambda pol: {c.get('capability', str(c)) if isinstance(c, dict) else str(c) for c in pol.get('mandate', {}).get(kind, [])}
            a, b = cap(was), cap(now)
            lines += [f'scope changed: +mandate.{kind} {x}' for x in sorted(b - a)] + [f'scope changed: -mandate.{kind} {x}' for x in sorted(a - b)]
        return lines

    def check(self, agent, base):
        if agent not in self.members:
            sys.exit(f'no member "{agent}": its folder is team/{agent}/ with a policy.json')
        for line in self.scope_changes(agent, base):                  # a report, not a refusal: the post-review and the post-check see it
            print(line)
        outside = [f for f in self.changed(agent, base) if not self.owns(agent, f) and not self.appends(agent, f)]
        for f in outside:
            print(f'outside scope: {f}')
        print(f'{agent}: {len(outside)} file(s) outside scope since {base}')
        return len(outside)

    def overlaps(self):
        found = []
        for f in self.tracked():
            owners = [a for a in self.members if self.owns(a, f)]
            if len(owners) > 1:
                found.append(f'{f}: claimed by {", ".join(owners)}')
        return found

    def unowned(self):
        shared = {'BRIEF.md', 'BRIEF-CORRECTIONS.md', 'version'}
        return [f for f in self.tracked() if f not in shared and not any(self.owns(a, f) for a in self.members)]


if __name__ == '__main__':
    args, team = sys.argv[1:], Team()
    cmd  = args[0] if args else ''
    if cmd == 'check':
        agent = args[args.index('--agent') + 1]
        base  = args[args.index('--base') + 1] if '--base' in args else 'origin/dev'
        sys.exit(1 if team.check(agent, base) else 0)
    elif cmd == 'overlaps':
        found = team.overlaps()
        print('\n'.join(found) or 'no overlaps')
        sys.exit(1 if found else 0)
    elif cmd == 'unowned':
        print('\n'.join(team.unowned()) or 'every tracked file has an owner')
    else:
        sys.exit(__doc__ or 'usage: agents.py check --agent <id> [--base <ref>] | overlaps | unowned')
