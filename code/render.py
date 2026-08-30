# -*- coding: utf-8 -*-
"""Spec-driven table renderer + checker.

A table spec lists, for every cell of every table in the submitted manuscript, the numeric tokens it contains and
where each token comes from (a CLAIMS_LEDGER claim field or a JSON path inside an aggregate artifact). render()
rebuilds the cell text by formatting each source value exactly as the manuscript prints it; check() compares the
rebuilt tables with the tables extracted from the submitted .docx, cell by cell. A mismatch is a defect.
"""
import json, os, re, csv
from decimal import Decimal, ROUND_HALF_UP
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
ART = os.environ.get("P014_ARTIFACTS", os.path.join(ROOT, "artifacts"))
_cache = {}
def artifact(name):
    if name not in _cache: _cache[name] = json.load(open(os.path.join(ART, name + ".json"), encoding="utf-8"))
    return _cache[name]
def ledger():
    if "__ledger" not in _cache:
        _cache["__ledger"] = {r["claim_id"]: r for r in csv.DictReader(open(os.path.join(ART, "CLAIMS_LEDGER.csv"), encoding="utf-8-sig"))}
    return _cache["__ledger"]
def resolve(o, path):
    for k in [k for k in path.split(".") if k]: o = o[int(k)] if isinstance(o, list) else o[k]
    return o
def value(src):
    """src: {'kind':'ledger','claim':'E01','field':'value'|'n'|'ci0'|'ci1'} | {'kind':'artifact','file':'I60','path':'estimates...'} | {'kind':'const','value':..}"""
    k = src["kind"]
    if k == "const": return float(src["value"])
    if k == "literal": return None
    if k == "ledger":
        r = ledger()[src["claim"]]; f = src["field"]
        if f in ("value", "n"): return float(r[f])
        ci = re.findall(r"-?\d+(?:\.\d+)?", r["ci95"]); return float(ci[0 if f == "ci0" else 1])
    return float(resolve(artifact(src["file"]), src["path"]))
def fmt(x, nd, pct=False, plus=False, comma=True):
    x = x * 100 if pct else x
    q = Decimal(repr(x)).quantize(Decimal(1).scaleb(-nd), ROUND_HALF_UP) if nd > 0 else Decimal(repr(x)).quantize(Decimal(1), ROUND_HALF_UP)
    s = f"{q:,.{nd}f}" if comma and abs(q) >= 1000 and nd == 0 else f"{q:.{nd}f}"
    if plus and q > 0: s = "+" + s
    return s.replace("-", "−")
def render_cell(cell):
    """cell: {'text': '0.7101 [0.3187, 1.1254]', 'tokens': [{'span':[0,6],'nd':4,'src':{...},'pct':False,'plus':False}, ...]}"""
    t = cell["text"]; out = []; pos = 0
    for tok in sorted(cell.get("tokens", []), key=lambda z: z["span"][0]):
        a, b = tok["span"]; out.append(t[pos:a]); v = value(tok["src"])
        out.append(t[a:b] if v is None else fmt(v, tok["nd"], tok.get("pct", False), tok.get("plus", False), comma="," in t[a:b] or tok["nd"] > 0)); pos = b
    out.append(t[pos:]); return "".join(out)
def render_table(tab):
    rows = [[render_cell(c) for c in row] for row in tab["rows"]]
    md = [f"**{tab['caption']}**" + (f" — {tab['panel']}" if tab.get("panel") else ""), ""]
    md.append("| " + " | ".join(rows[0]) + " |"); md.append("|" + "---|" * len(rows[0]))
    for r in rows[1:]: md.append("| " + " | ".join(r) + " |")
    return "\n".join(md), rows
def norm(s): return re.sub(r"\s+", " ", s.replace("-", "−").replace("+", "").strip())
def check(spec):
    """Compare rendered cells with the manuscript cells stored in the spec. Returns (n_cells, mismatches)."""
    n = 0; bad = []
    for tab in spec:
        _, rows = render_table(tab)
        for ri, row in enumerate(tab["rows"]):
            for ci, cell in enumerate(row):
                if not cell.get("tokens"): continue
                n += 1
                if norm(rows[ri][ci]) != norm(cell["text"]): bad.append((tab["caption"], tab.get("panel", ""), cell["text"], rows[ri][ci]))
    return n, bad
