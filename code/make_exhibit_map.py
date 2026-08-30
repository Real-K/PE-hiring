# -*- coding: utf-8 -*-
"""EXHIBIT_MAP.csv (every numeric table token → source → pipeline script) and ARTIFACT_MANIFEST.md."""
import json, csv, os, hashlib
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")); ART = os.path.join(ROOT, "artifacts")
led = {r["claim_id"]: r for r in csv.DictReader(open(os.path.join(ART, "CLAIMS_LEDGER.csv"), encoding="utf-8-sig"))}
def code_of(f):
    try: return os.path.basename(json.load(open(os.path.join(ART, f + ".json"), encoding="utf-8")).get("code", "") or "")
    except Exception: return ""
rows = []
for doc, spec in [("main", "main_tables"), ("appendix", "appendix_tables")]:
    for T in json.load(open(os.path.join(ROOT, "spec", spec + ".json"), encoding="utf-8")):
        for row in T["rows"]:
            for ci, c in enumerate(row):
                for tok in c.get("tokens", []):
                    s = tok["src"]; k = s["kind"]; claim = ""
                    if k == "ledger":
                        r = led[s["claim"]]; claim = s["claim"]; src = f"{r['source_json'].split('/')[-1]}:{r['json_path']}" + ("" if s["field"] == "value" else f" ({s['field']})"); script = os.path.basename(r["code"]) or code_of(r["source_json"].split("/")[-1][:-5])
                    elif k == "artifact": src = f"{s['file']}.json:{s['path']}"; script = code_of(s["file"])
                    elif k == "const": src, script = "constant (sample fact)", ""
                    else: src, script = "UNTRACEABLE", ""
                    rows.append({"document": doc, "table": T["caption"], "panel": T["panel"], "row": row[0]["text"][:80], "col": ci, "token": c["text"][tok["span"][0]:tok["span"][1]], "claim_id": claim, "source": src, "pipeline_script": script, "docx_edit_required": tok.get("docx_current", "")})
with open(os.path.join(ROOT, "EXHIBIT_MAP.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
use = {}
for r in rows:
    if ":" in r["source"]: use.setdefault(r["source"].split(":")[0].replace(".json", ""), set()).add(("Main " if r["document"] == "main" else "OA ") + r["table"].split(".")[0])
lines = ["# Artifact manifest", "", "Aggregate result files in `artifacts/`; `Feeds` lists the submitted-manuscript tables whose cells read from the file (from `EXHIBIT_MAP.csv`). `I05.json` is a public copy with firm identifiers removed. `I45_rerun_check.json` records the 2026-08-31 confirmatory re-run behind the Table E4 correction.", "", "| Artifact | sha256₁₆ | Bytes | Pipeline script | Feeds |", "|---|---|---:|---|---|"]
for fn in sorted(os.listdir(ART)):
    if not fn.endswith(".json"): continue
    p = os.path.join(ART, fn); h = hashlib.sha256(open(p, "rb").read()).hexdigest()[:16]
    try: j = json.load(open(p, encoding="utf-8")); code = os.path.basename(j.get("code", "") or j.get("script", "") or "")
    except Exception: code = ""
    lines.append(f"| `{fn}` | `{h}` | {os.path.getsize(p):,} | `{code}` | {', '.join(sorted(use.get(fn[:-5], []))) or '—'} |")
open(os.path.join(ROOT, "ARTIFACT_MANIFEST.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
print(f"EXHIBIT_MAP rows {len(rows)} · untraceable {sum(r['source']=='UNTRACEABLE' for r in rows)} · docx edits {sum(bool(r['docx_edit_required']) for r in rows)} · manifest {sum(f.endswith('.json') for f in os.listdir(ART))} files")
