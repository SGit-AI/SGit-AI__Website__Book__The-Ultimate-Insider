#!/usr/bin/env python3
"""The editor's comparison (P2, conductor__024): the ten-page sample at Crown Quarto in type A and type B, colour.

    python3 lab/tools/book/compare_types.py <a scratch folder outside the repository>
Runs the publisher's own build, as it now is (its book.css, its copy of the lab's look, its --type sets), on a
scratch copy of publishing/ and manuscript/, once per type. On the copy only, it adds the designer's changes the
publisher has not yet taken (PENDING below, and LAB 22's four drawings at their stated size), so the editor sees
his page 7 note answered. Writes lab/pdf/sample-lab-look-A.pdf and -B.pdf and
their lines in lab/pdf/SHA256SUMS. Changes nothing outside lab/.
"""
import hashlib, shutil, subprocess, sys
from pathlib import Path

LAB = Path(__file__).resolve().parents[2]
REPO = LAB.parent
PENDING = 'figure img[src$=".svg"], figure img[src^="data:image/svg"] { border: none; width: auto; }\n'
DRAWINGS = ("cast-row", "day-timeline", "loop", "book-map")
STAMP = "RC2 sample, Crown Quarto, type {t}: for the editor's comparison, 1 November 2026"


def build(scratch, t):
    root = scratch / f"type-{t}"
    if root.exists():
        shutil.rmtree(root)
    shutil.copytree(REPO / "publishing", root / "publishing", ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copytree(REPO / "manuscript", root / "manuscript")
    css = root / "publishing" / "lab-look.css"
    css.write_text(css.read_text() + "\n/* the designer's, not yet taken (compare_types.py) */\n" + PENDING)
    for d in DRAWINGS:
        shutil.copy(LAB / "experiments" / "22-designer-t10-drawings" / f"{d}.svg", root / "manuscript" / "sample" / "images")
    out = root / "out"
    name = f"sample-lab-look-{t}"
    subprocess.run([sys.executable, str(root / "publishing" / "build_book.py"), "--book", "manuscript/sample/Book.txt",
                    "--name", name, "--no-epub", "--out", str(out), "--type", t,
                    "--subtitle", "A book in the Generation ZX Founders (GenAI Edition) series",
                    "--stamp", STAMP.format(t=t)], check=True, cwd=root)
    dest = LAB / "pdf" / f"{name}.pdf"
    shutil.copy(next(out.glob("*.pdf")), dest)
    return dest


def main(scratch):
    scratch = Path(scratch).resolve()
    if REPO in scratch.parents or scratch == REPO:
        sys.exit("the scratch folder must be outside the repository")
    sums = LAB / "pdf" / "SHA256SUMS"
    for t in ("A", "B"):
        dest = build(scratch, t)
        lines = [l for l in sums.read_text().splitlines() if not l.endswith("  " + dest.name)]
        lines.append(f"{hashlib.sha256(dest.read_bytes()).hexdigest()}  {dest.name}")
        sums.write_text("\n".join(sorted(lines, key=lambda l: l.split("  ")[1])) + "\n")
        print(f"built {dest.relative_to(REPO)}")


if __name__ == "__main__":
    main(sys.argv[1])
