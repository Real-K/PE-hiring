# -*- coding: utf-8 -*-
"""Build the six notebooks with stored outputs (run from anywhere): tables, figure, traceability — for main_paper/ and online_appendix/."""
import os, re, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_notebooks import build
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
COMMON = ["Every number is read from an aggregate result artifact in `../artifacts/` — the files the submitted manuscript's tables were generated from.",
          "No licensed microdata is used or required (see `../DATA_ACCESS.md`). Outputs are stored, so the notebook renders on GitHub without running.",
          "The last cell compares every regenerated cell with the cell text extracted from the submitted .docx and raises on any difference."]
SETUP = '''import os, sys, json
sys.path.insert(0, "../code"); import render          # spec-driven renderer (../code/render.py)
spec = json.load(open("../spec/%s.json", encoding="utf-8"))
print(f"tables in spec: {len(spec)} · artifacts: {len([f for f in os.listdir('../artifacts') if f.endswith('.json')])}")'''
for folder, specname, title, figpy, figpng, figtitle in [
    ("main_paper", "main_tables", "# Main text — Tables 1–6", "build_figure1.py", "figure1_event_study.png", "# Figure 1 — Hiring rises after the deal, and the response is concentrated in targets with low pre-deal hiring intensity"),
    ("online_appendix", "appendix_tables", "# Online Appendix — Tables A1–H2", "build_figureC1.py", "figure2_turnover.png", "# Figure C1 — State gradients and placebo distributions across worker-flow outcomes")]:
    os.chdir(os.path.join(ROOT, folder))
    spec = json.load(open(f"../spec/{specname}.json", encoding="utf-8"))
    cells = [(["## Setup"], SETUP % specname)]
    for i, T in enumerate(spec):
        cap = T["caption"] + (f" — {T['panel']}" if T["panel"] else "")
        cells.append(([f"## {cap}"], f'md, rows = render.render_table(spec[{i}]); _md = md\nprint("{cap[:70]}")'))
    cells.append((["## Check — every regenerated cell equals the submitted manuscript's cell"],
                  'n, bad = render.check(spec)\nlit = [(T["caption"], c["text"]) for T in spec for row in T["rows"] for c in row for t in c.get("tokens", []) if t["src"]["kind"] == "literal"]\nprint(f"cells checked {n} · mismatches {len(bad)} · untraceable literals {len(lit)}")\nfor l in lit: print("  LITERAL (flagged, see PLACEHOLDERS_RESOLVED.md):", l)\nassert not bad'))
    build("01_tables.ipynb", title, COMMON, cells)
    # figure notebook: header + block cut from the build script
    src = open(figpy, encoding="utf-8").read(); body = src.split("SAVE = lambda", 1)[1].split("\n", 1)[1]
    setup_f = '''import json, os, csv, io
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
ART, EX = "../artifacts", "."
J = lambda f: json.load(open(os.path.join(ART, f + ".json"), encoding="utf-8"))
L = {r["claim_id"]: r for r in csv.DictReader(open(os.path.join(ART, "CLAIMS_LEDGER.csv"), encoding="utf-8-sig"))}
c = lambda cid, w="value": L[cid][w]
_figs = []
def SAVE(fig, n):
    for e in ("png", "pdf"): fig.savefig(f"{EX}/{n}.{e}", dpi=200, bbox_inches="tight")
    b = io.BytesIO(); fig.savefig(b, format="png", dpi=110, bbox_inches="tight"); _figs.append(b.getvalue())'''
    check_f = f'''import hashlib
a = hashlib.sha256(open("{figpng}", "rb").read()).hexdigest()
b = hashlib.sha256(open("../paper_exhibits/{'figure1_event_study.png' if folder=='main_paper' else 'figureC1_worker_flows.png'}", "rb").read()).hexdigest()
print("regenerated PNG sha256 ==", "image embedded in the submitted .docx" if a == b else "DIFFERS", a[:16]); assert a == b'''
    build("02_figure.ipynb", figtitle, COMMON[:2] + ["The code below is cut verbatim from the paper's figure builder; the last cell checks the regenerated PNG against the image embedded in the submitted .docx."],
          [(["## Setup"], setup_f), (["## Build"], body), (["## Check"], check_f)])
    trace = '''import csv, json, os
from collections import Counter
doc = "%s"
em = [r for r in csv.DictReader(open("../EXHIBIT_MAP.csv", encoding="utf-8")) if r["document"] == doc]
tn = [r for r in csv.DictReader(open("../TEXT_NUMBERS.csv", encoding="utf-8")) if r["document"] == doc]
print(f"table cells mapped: {len(em)} · by source kind:", dict(Counter("ledger" if r["claim_id"] else ("constant" if "constant" in r["source"] else ("UNTRACEABLE" if r["source"]=="UNTRACEABLE" else "artifact")) for r in em)))
print(f"prose numbers: {len(tn)} · by kind:", dict(Counter(r["kind"] for r in tn)))
print("\\nartifacts feeding this document's tables:", sorted({r["source"].split(":")[0] for r in em if ":" in r["source"]}))
print("pipeline scripts:", sorted({r["pipeline_script"] for r in em if r["pipeline_script"]}))
un = [r for r in em if r["source"] == "UNTRACEABLE"] + [r for r in tn if r["kind"] == "UNMATCHED"]
for r in un: print("  UNTRACEABLE:", r)''' % ("main" if folder == "main_paper" else "appendix")
    ledg = '''rows = list(csv.DictReader(open("../artifacts/CLAIMS_LEDGER.csv", encoding="utf-8-sig")))
def resolve(o, path):
    for k in [k for k in path.split(".") if k]: o = o[int(k)] if isinstance(o, list) else o[k]
    return o
exact = derived = mismatch = missing = 0
for r in rows:
    f = os.path.join("../artifacts", os.path.basename(r["source_json"]))
    if not os.path.exists(f): missing += 1; continue
    try: o = resolve(json.load(open(f, encoding="utf-8")), r["json_path"])
    except Exception: mismatch += 1; continue
    if isinstance(o, (dict, list)): derived += 1; continue
    try: ok = abs(float(r["value"]) - float(o)) <= max(5e-5, abs(float(o)) * 1e-6)
    except Exception: ok = str(o) == r["value"]
    exact += ok; mismatch += (not ok)
print(f"claims ledger: {len(rows)} rows · exact {exact} · derived {derived} · mismatch {mismatch} · artifact missing {missing}"); assert mismatch == 0'''
    build("03_traceability.ipynb", "# Traceability — every number in the submitted manuscript → its artifact", COMMON[:2],
          [(["## Table cells and prose numbers → sources", "`EXHIBIT_MAP.csv` lists every numeric table cell; `TEXT_NUMBERS.csv` every number in the prose (References excluded)."], trace),
           (["## The claims ledger resolves against the artifacts"], ledg)])
print("notebooks built")
