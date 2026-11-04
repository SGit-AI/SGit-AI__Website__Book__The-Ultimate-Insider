#!/usr/bin/env python3
"""LAB 50: three of this book's own team's keys as QR codes, side by side, for chapter 3's line "the same kind of key as
a QR code: a few of this book's own team, each code holding one member's public key and nothing else" (publisher 048).

    python3 lab/experiments/50-designer-three-keys/make_three_keys.py

The conductor's, the researcher's and the writer's team/<id>/key.png, embedded exactly as committed (base64
data:image/png; never re-encoded from key.json). Each holds only that member's public key (security__024 clears every
team/<id>/key.png by name: "each holds only that member's public key ... No private half"). Each is labelled with the
member's name only: no fingerprint, no key text. 155 mm wide, each code 48 mm, as large as three fit (dense codes: the publisher's QR test decides if they scan).
"""
import base64, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "lab" / "characters"))
import make_cast as mc  # noqa: E402

MEMBERS = ["conductor", "researcher", "writer"]
SANS = 'font-family="Inter, Helvetica, Arial, sans-serif"'


def main():
    out, side, gap = [], 48.0, 3.6  # as large as three fit across the 155 mm column: the codes are dense
    for k, m in enumerate(MEMBERS):
        raw = (REPO / "team" / m / "key.png").read_bytes()
        if raw[:8] != b"\x89PNG\r\n\x1a\n":
            sys.exit(f"make_three_keys: team/{m}/key.png is not a PNG")
        x = 2 + k * (side + gap)
        b64 = base64.b64encode(raw).decode()
        out.append(f'<rect x="{x - 1.5:.2f}" y=".5" width="{side + 3:.2f}" height="{side + 3:.2f}" rx="1.5" fill="#fff" stroke="{mc.FILL2}" stroke-width=".4"/>'
                   f'<image x="{x:.2f}" y="2" width="{side}" height="{side}" href="data:image/png;base64,{b64}"/>'
                   f'<text x="{x + side / 2:.2f}" y="{side + 9.6:.2f}" {SANS} font-size="3.18" font-weight="700" fill="{mc.INK}" text-anchor="middle">{m}</text>')
    svg = mc.svg(155, round(side + 11, 1), "".join(out), "Three QR codes, the conductor's, the researcher's and the writer's, each holding that member's public key and nothing else")
    sys.path.insert(0, str(REPO / "publishing"))
    import edition
    why = edition.unsafe_svg(svg)
    if why:
        sys.exit(f"make_three_keys: the drawings' check refuses it: {why}")
    (HERE / "three-keys.svg").write_text(svg)
    print("written three-keys.svg")


if __name__ == "__main__":
    main()
