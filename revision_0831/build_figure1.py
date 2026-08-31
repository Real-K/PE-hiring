# -*- coding: utf-8 -*-
"""New Figure 1 per the 0831 review memo (Part 4 §6–7, §26–27): (a) event-level state–response relationship,
(b) the ACTUAL empirical distribution of the 2,000 untreated pseudo-sample gradients (no normal approximation)."""
import json, os
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
ART = os.environ.get("P014_ARTIFACTS", os.path.join(ROOT, "artifacts"))
E = json.load(open(os.path.join(ART, "I70.json"), encoding="utf-8"))["estimates"]
PA, PB = E["panelA_gradient"], E["panelB_scatter"]
fig, ax = plt.subplots(1, 2, figsize=(11.2, 4.3))

a0 = ax[0]
xy = np.array(PB["pairs_display"])
a0.scatter(xy[:, 0], xy[:, 1], s=13, color="0.72", alpha=.75, lw=0, zorder=2)
g = np.array(PB["band"]["grid"]); lo = np.array(PB["band"]["lo"]); hi = np.array(PB["band"]["hi"])
a0.fill_between(g, lo, hi, color="#1b4a8a", alpha=.13, lw=0, zorder=3)
f = PB["fit"]
a0.plot(g, f["ybar"] + f["slope"] * (g - f["xbar"]), color="#1b4a8a", lw=2, zorder=5)
bm = PB["quintile_bin_means"]
a0.scatter([b["x"] for b in bm], [b["y"] for b in bm], s=52, color="#1b4a8a", edgecolor="white", lw=1.1, zorder=6)
a0.axhline(0, color="0.55", lw=.7, zorder=1)
a0.set_xlabel("Pre-deal hiring state $S_i$  (higher = lower prior hiring)")
a0.set_ylabel("Adjusted treated − control change\nin the log hiring rate")
a0.set_title("(a) Matched hiring responses across the pre-deal state", fontsize=10.5, loc="left")
a0.text(.985, .04, f"n = {PA['n']} events · dark points: fixed quintile-bin means\nslope {f['slope']:+.4f} · 95% band: event bootstrap",
        transform=a0.transAxes, ha="right", fontsize=7.8, color="0.42")

a1 = ax[1]
d = np.array(PA["draws"])
a1.hist(d, bins=42, density=True, color="0.62", alpha=.55, edgecolor="white", lw=.4, zorder=1)
for q, lab in ((PA["pct_2_5"], None), (PA["pct_97_5"], None)):
    a1.axvline(q, color="0.35", lw=1.0, ls=":", zorder=3)
a1.axvline(PA["null_mean"], color="0.35", lw=1.1, ls="--", zorder=3, ymax=.86)
a1.axvline(PA["observed"], color="#8a1b2e", lw=2.3, zorder=5)
ytop = a1.get_ylim()[1]; a1.set_ylim(0, ytop * 1.22)
a1.annotate(f"observed {PA['observed']:+.3f}", xy=(PA["observed"], ytop * .48), xytext=(-9, 0),
            textcoords="offset points", fontsize=9.4, color="#8a1b2e", weight="bold", va="center", ha="right", rotation=90)
a1.annotate(f"untreated mean {PA['null_mean']:+.3f}", xy=(PA["null_mean"], ytop * 1.06), xytext=(3, 0),
            textcoords="offset points", fontsize=7.8, color="0.3", ha="left", va="center")
a1.annotate(f"empirical central 95%\n[{PA['pct_2_5']:+.3f}, {PA['pct_97_5']:+.3f}]",
            xy=(PA["pct_97_5"], ytop * .55), xytext=(-5, 0), textcoords="offset points",
            fontsize=7.8, color="0.35", ha="right", va="center")
a1.text(.02, .88, f"standardized distance = {PA['z']}\ntwo-sided $p$ = {PA['RI_p_two_sided']:.4f}\n(upper-tail $p$ = {PA['RI_p_upper']:.4f})",
        transform=a1.transAxes, ha="left", va="top", fontsize=8.6, color="#8a1b2e")
a1.text(.02, .60, f"{len(d):,} pseudo-sample gradients\nfrom {PA['n_pseudo']:,} untreated pseudo-events",
        transform=a1.transAxes, ha="left", va="top", fontsize=7.6, color="0.42")
a1.set_yticks([]); a1.set_xlabel("State gradient in the log hiring rate")
a1.set_title("(b) Observed gradient relative to untreated pseudo-events", fontsize=10.5, loc="left")

for a in ax: a.spines[["top", "right"]].set_visible(False)
fig.suptitle("Figure 1. Hiring responses across pre-deal hiring states",
             fontsize=10.6, y=1.005, x=.008, ha="left")
fig.text(.008, -0.075,
         "Notes. Panel (a) plots the event-level treated-minus-control change in the log hiring rate against the target's pre-deal hiring state in the 286-event primary sample;\n"
         "higher state values indicate lower pre-deal hiring intensity. The display follows the primary specification (5/95 winsorisation; covariates partialled out of both axes,\n"
         "added-variable form); dark points are fixed quintile-bin means of the displayed values. Panel (b) plots the empirical distribution of the 2,000 untreated pseudo-sample\n"
         "gradients described in Section 4.3 — not a fitted normal approximation; vertical markers show the empirical mean and central 95 percent interval.",
         fontsize=7.4, color="0.4", ha="left")
fig.tight_layout()
for e in ("png", "pdf"): fig.savefig(os.path.join(HERE, f"figure1_state_gradient.{e}"), dpi=200, bbox_inches="tight")
print("saved figure1_state_gradient.png/.pdf")
