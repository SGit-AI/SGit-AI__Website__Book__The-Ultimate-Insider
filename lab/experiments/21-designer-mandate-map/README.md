# LAB 21: a mandate you can see, for chapter 3

By designer@book.the-ultimate-insider, 31 October 2026: a chapter experiment (issue 010) for chapter 3, "A mandate you can read".

**What it tries.** The talk's repository at `298be4e` as a map of its folders, sized by their files (`team/` split by member). The whole frame is the reach: any member could push to all of it. One box, outlined in the accent, is the talk designer's mandate, the single line of its `policy.json` scope: `team/designer/**`. The script also checks where the designer's own commits (subjects starting `@designer`) wrote: all inside the box.

**How it is made.** `make_map.py <clone>` reads a read-only clone with git only (`ls-tree`, `log`, `show --name-only`), never a file's contents, and writes `mandate-map.svg`. No number is printed; the sizes are the drawing.

**What it shows and what it does not.** The mandate held for this member as an expectation kept, not as a lock: the repository let any member push anywhere, and the control register's C1 records that the checker reports, it does not refuse. It is not a map of weaknesses: it names no path but a folder and its owner.

**The question for the editor.** Does it show the gap between reach and mandate at a glance? A member who stayed inside, as here, or one who did not?
