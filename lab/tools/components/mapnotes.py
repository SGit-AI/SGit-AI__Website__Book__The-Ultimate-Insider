#!/usr/bin/env python3
"""A Wardley map with side notes: numbered markers over an RC1 map image, the notes beside it, in the lab's language.

    from mapnotes import render; render(spec_dict, root=Path("."))  -> HTML for a lab page

The spec: {"map": "<the map's JSON, from the repository root>", "image": "<its PNG>", "width_mm": 114,
           "notes": [{"at": "<component id>", "text": "<optional; by default the map's own words>"}]}.
Each marker sits where the map's own JSON puts the component, computed with the same geometry as the map's
renderer (team/conductor/rc1/tools/wardley.py, imported read-only). A note says, by default, the component's
label and the evolution stage it sits in, both from the map's JSON, so the notes add no claim of their own.
The editor's T8: small, simple maps early, side notes on the page.
"""
import html, importlib.util, json, math
from pathlib import Path


def _geometry(root, m):
    spec = importlib.util.spec_from_file_location("wardley", root / "team/conductor/rc1/tools/wardley.py")
    w = importlib.util.module_from_spec(spec); spec.loader.exec_module(w)
    title_lines = w.wrap(m.get("title", ""), 62)
    T = w.T0 + len(title_lines) * w.TITLE * 1.2 + 18
    PH = m.get("height", 640)
    chain_only = m.get("axes", "full") == "chain"
    legend, stage_notes = m.get("legend", []), m.get("stage_notes")
    SN = max(len(w.wrap(t, 17)) for t in stage_notes) * 22 + 10 if stage_notes else 0
    B = (92 + SN) if not chain_only else 40
    LEG = (24 + 36 * math.ceil(len(legend) / 2)) if legend else 0
    H = T + PH + B + LEG
    x0, x1, y0, y1 = w.L, w.W - w.R, T, T + PH
    return lambda vis, evo: ((x0 + evo * (x1 - x0)) / w.W * 100, (y0 + (1 - vis) * (y1 - y0)) / H * 100)


def render(spec, root, src_prefix="../.."):
    root = Path(root)
    m = json.loads((root / spec["map"]).read_text())
    xy = _geometry(root, m)
    comps = {c["id"]: c for c in m["components"]}
    stages = m.get("stage_notes") or []
    markers, notes = [], []
    for n, note in enumerate(spec["notes"], 1):
        c = comps[note["at"]]
        x, y = xy(c["vis"], c["evo"])
        markers.append(f'<span class="mk" style="left:{x:.2f}%;top:{y:.2f}%">{n}</span>')
        stage = stages[min(3, int(c["evo"] * 4))] if stages else ""
        text = note.get("text") or (f'{c["label"]}. ' + (f'<span class="stage">{html.escape(stage)}</span>' if stage else ""))
        notes.append(f'<li><b>{n}</b> {text if note.get("text") is None else html.escape(text)}</li>')
    w = spec.get("width_mm", 114)
    return (f'<div class="mapnotes"><div class="mn-map" style="width:{w}mm"><img src="{src_prefix}/{spec["image"]}" alt="{html.escape(m.get("title", "A Wardley map"))}">'
            + "".join(markers) + f'</div><ol class="mn-notes">{"".join(notes)}</ol></div>')
