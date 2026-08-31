# -*- coding: utf-8 -*-
"""New Figure 2 per the 0831 review memo (Part 6 §3): the former Figure 1(a) quarterly path as a standalone figure,
with significance markers removed (point estimates and 95% CIs only)."""
import json, os
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
ART = os.environ.get("P014_ARTIFACTS", os.path.join(ROOT, "artifacts"))
i68 = json.load(open(os.path.join(ART, "I68.json"), encoding="utf-8"))["estimates"]
B = i68["beta"]
QL = [f"q{k}" for k in range(-4, 0)] + [f"q{k}" for k in range(1, 13)]
xs = list(range(-4, 0)) + list(range(1, 13))
b = [B[q]["b"] for q in QL]; lo = [B[q]["ci"][0] for q in QL]; hi = [B[q]["ci"][1] for q in QL]
fig, a0 = plt.subplots(figsize=(7.4, 4.1))
a0.axhline(0, color="0.4", lw=.8); a0.axvline(0, color="0.45", lw=.9, ls=":")
a0.axvspan(-4.6, -0.4, color="0.5", alpha=.05, lw=0, zorder=0)
a0.errorbar(xs, b, yerr=[np.array(b) - np.array(lo), np.array(hi) - np.array(b)], fmt="o", ms=4.5,
            lw=1, capsize=2.5, color="#1b4a8a", ecolor="0.6", zorder=3)
a0.annotate("pre-deal quarters flat\n(all within ±0.004)", xy=(-2.5, max(hi[:4]) * 1.9 + 0.004),
            fontsize=8, color="0.4", ha="center")
a0.set_ylabel("Treated − control, hires per worker per quarter\n(normalized to quarters −4 to −1)", fontsize=9)
a0.set_xlabel("Quarter relative to deal")
a0.text(.985, .045, f"n = {i68['n_ev']} matched events (baseline design)",
        transform=a0.transAxes, ha="right", fontsize=8, color="0.45")
a0.spines[["top", "right"]].set_visible(False)
a0.set_title("Figure 2. Quarterly hiring differences relative to matched controls", fontsize=10.6, loc="left")
fig.text(.01, -0.06, "Notes. Point estimates with 95% event-bootstrap intervals; no per-quarter significance markers. "
         f"Contributing events decline with horizon, from {B['q1']['n']} at quarter 1 to {B['q12']['n']} at quarter 12.",
         fontsize=7.6, color="0.4", ha="left")
fig.tight_layout()
for e in ("png", "pdf"): fig.savefig(os.path.join(HERE, f"figure2_quarterly.{e}"), dpi=200, bbox_inches="tight")
print("saved figure2_quarterly.png/.pdf")
