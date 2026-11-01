#!/usr/bin/env python3
"""Preview the ten-page sample in the lab's look (LK1), in colour and in black and white, with the publisher's own build.

    python3 lab/tools/book/preview.py <a scratch folder outside the repository>
Copies publishing/ and manuscript/ into the scratch folder, adds lab/tools/book/lab-look.css (and, for the second
build, lab-look-bw.css) after the copy's book.css, and runs the copy's build_book.py on the sample as the publisher
does. Writes lab/pdf/sample-lab-look.pdf and sample-lab-look-bw.pdf and their lines in lab/pdf/SHA256SUMS. Changes
nothing outside lab/: the publisher's book.css is untouched; it can take the fragment when it chooses.
"""
import hashlib, shutil, subprocess, sys
from pathlib import Path

LAB = Path(__file__).resolve().parents[2]
REPO = LAB.parent


def build(scratch, name, sheets):
    root = scratch / name
    if root.exists():
        shutil.rmtree(root)
    shutil.copytree(REPO / "publishing", root / "publishing", ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copytree(REPO / "manuscript", root / "manuscript")
    css = root / "publishing" / "book.css"
    css.write_text(css.read_text() + "\n" + "\n".join((LAB / "tools" / "book" / s).read_text() for s in sheets))
    out = root / "out"
    subprocess.run([sys.executable, str(root / "publishing" / "build_book.py"), "--book", "manuscript/sample/Book.txt",
                    "--name", name, "--no-epub", "--out", str(out),
                    "--subtitle", "A book in the Generation ZX Founders (GenAI Edition) series",
                    "--stamp", "RC2 sample in the lab's look (LK1): a preview, 31 October 2026"], check=True, cwd=root)
    pdf = next(out.glob("*.pdf"))
    dest = LAB / "pdf" / f"{name}.pdf"
    shutil.copy(pdf, dest)
    return dest


def main(scratch):
    scratch = Path(scratch).resolve()
    if REPO in scratch.parents or scratch == REPO:
        sys.exit("the scratch folder must be outside the repository")
    sums = LAB / "pdf" / "SHA256SUMS"
    for name, sheets in (("sample-lab-look", ["lab-look.css"]), ("sample-lab-look-bw", ["lab-look.css", "lab-look-bw.css"])):
        dest = build(scratch, name, sheets)
        lines = [l for l in sums.read_text().splitlines() if not l.endswith("  " + dest.name)]
        lines.append(f"{hashlib.sha256(dest.read_bytes()).hexdigest()}  {dest.name}")
        sums.write_text("\n".join(sorted(lines, key=lambda l: l.split("  ")[1])) + "\n")
        print(f"built {dest.relative_to(REPO)}")


if __name__ == "__main__":
    main(sys.argv[1])
