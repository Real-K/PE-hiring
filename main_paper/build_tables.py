# -*- coding: utf-8 -*-
"""Main text, Tables 1–6 — rebuild every table of the submitted manuscript from aggregate artifacts and check it cell by cell.

Each table is defined in ../spec/main_tables.json: for every cell, the numeric tokens and the artifact/ledger field
they come from. This script (1) renders all tables to tables.md, (2) compares every rendered cell with the cell text
extracted from the submitted .docx (stored in the spec), (3) writes CHECK_REPORT.md. Exit 1 if any cell differs.
"""
import os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code"))
import render
HERE = os.path.dirname(os.path.abspath(__file__))
spec = json.load(open(os.path.join(HERE, "..", "spec", "main_tables.json"), encoding="utf-8"))
md = ["# Main text, Tables 1–6 — regenerated from artifacts", ""]
for tab in spec:
    t, _ = render.render_table(tab); md.append(t); md.append("")
open(os.path.join(HERE, "tables.md"), "w", encoding="utf-8").write("\n".join(md))
n, bad = render.check(spec)
lit = [(T["caption"], c["text"], tok["src"]["note"]) for T in spec for row in T["rows"] for c in row for tok in c.get("tokens", []) if tok["src"]["kind"] == "literal"]
rep = [f"# Check report — Main text, Tables 1–6", "", f"- tables: {len(spec)}", f"- numeric cells checked against the submitted manuscript: {n}", f"- mismatches: {len(bad)}", f"- untraceable literals (rendered as-is, flagged): {len(lit)}", ""]
for cap, pan, want, got in bad: rep.append(f"- MISMATCH {cap} / {pan}: manuscript '{want}' vs rebuilt '{got}'")
for cap, txt, note in lit: rep.append(f"- LITERAL {cap}: '{txt}' — {note}")
open(os.path.join(HERE, "CHECK_REPORT.md"), "w", encoding="utf-8").write("\n".join(rep) + "\n")
print(f"Main text, Tables 1–6: {len(spec)} tables · {n} cells checked · {len(bad)} mismatches · {len(lit)} untraceable literal(s)")
sys.exit(1 if bad else 0)
