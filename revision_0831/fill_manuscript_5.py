# -*- coding: utf-8 -*-
"""Fill part 5 — formatting unification: Table D1 to 4 dp from I61; true minus signs in all table cells."""
import json, os, csv, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
ART = os.environ.get("P014_ARTIFACTS", os.path.join(ROOT, "artifacts"))
SRC = os.environ["P014_MANUSCRIPT"]
E = lambda a: json.load(open(os.path.join(ART, a + ".json"), encoding="utf-8"))["estimates"]
def f4p(x): return f"{x:+.4f}".replace("-", "−")
TR = []
def R(s, old, new, tag):
    n = s.count(old)
    assert n == 1, f"anchor x{n} [{tag}]: {old[:80]!r}"
    TR.append({"tag": tag, "old": old[:110], "new": new[:110]}); return s.replace(old, new)
s = open(SRC, encoding="utf-8").read()
tp, pp = E("I61")["panelA_treated_path"], E("I61")["panelC_placebo_path"]
def qrow(d, pre):
    ks = [f"q{k}" for k in ((-4, -3, -2, -1) if pre else (1, 2, 3, 4))]
    return " | ".join(f4p(d[k]["grad"] if "grad" in d[k] else d[k].get("mean", d[k])) for k in ks)
s = R(s, "| Treated, pre-deal | +0.087 | -0.042 | -0.038 | -0.056 |", f"| Treated, pre-deal | {qrow(tp, True)} |", "D1.r1")
s = R(s, "| Treated, post-deal | +0.147 | +0.240 | +0.108 | +0.010 |", f"| Treated, post-deal | {qrow(tp, False)} |", "D1.r2")
s = R(s, "| Untreated pseudo-events, pre-deal | -0.073 | -0.031 | -0.003 | +0.045 |", f"| Untreated pseudo-events, pre-deal | {qrow(pp, True)} |", "D1.r3")
s = R(s, "| Untreated pseudo-events, post-deal | -0.024 | +0.088 | -0.040 | -0.000 |", f"| Untreated pseudo-events, post-deal | {qrow(pp, False)} |", "D1.r4")
# 표 셀 내 마이너스 통일 (표 행에서만)
lines = s.split("\n"); nfix = 0
for i, ln in enumerate(lines):
    if ln.startswith("|"):
        new = re.sub(r"(?<=[\s\[(|=])-(?=\d)", "−", ln)
        if new != ln: nfix += 1; lines[i] = new
s = "\n".join(lines)
TR.append({"tag": "minus", "old": f"{nfix} table lines", "new": "true minus"})
open(SRC, "w", encoding="utf-8").write(s)
with open(os.path.join(HERE, "FILL_TRACE.csv"), "a", encoding="utf-8", newline="") as f:
    csv.DictWriter(f, fieldnames=["tag", "old", "new"]).writerows(TR)
print(f"PART 5: D1 rebuilt at 4 dp · minus normalised in {nfix} table lines")
