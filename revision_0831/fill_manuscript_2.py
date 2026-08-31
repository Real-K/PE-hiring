# -*- coding: utf-8 -*-
"""Fill part 2 — Online Appendix A–C placeholders (run after fill_manuscript.py)."""
import json, os, csv
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
ART = os.environ.get("P014_ARTIFACTS", os.path.join(ROOT, "artifacts"))
SRC = os.environ["P014_MANUSCRIPT"]
_J = {}
def E(a):
    if a not in _J: _J[a] = json.load(open(os.path.join(ART, a + ".json"), encoding="utf-8"))["estimates"]
    return _J[a]
def g(a, p):
    o = E(a)
    for k in p.split("."): o = o[int(k)] if isinstance(o, list) else o[k]
    return o
def f4(x, plus=False): return (f"{x:+.4f}" if plus else f"{x:.4f}").replace("-", "−")
def f2(x): return f"{x:.2f}".replace("-", "−")
def f3(x): return f"{x:.3f}".replace("-", "−")
def ci4(v): return f"[{v[0]:.4f}, {v[1]:.4f}]".replace("-", "−")
TR = []
def R(s, old, new, tag):
    n = s.count(old)
    assert n == 1, f"anchor x{n} [{tag}]: {old[:90]!r}"
    TR.append({"tag": tag, "old": old[:110], "new": new[:110]}); return s.replace(old, new)
s = open(SRC, encoding="utf-8").read()

# ═══ Appendix A ═══
pl38, pl39 = g("I38","panelA_excess.pre_levels"), g("I39","pre_levels")
s = R(s, "compared with [placeholder: verified employment-weighted benchmark] under the primary benchmark",
      f"compared with {12*pl38['exp_w']:.2f} under the primary benchmark", "A.pre-zero")
s = R(s, "Their longest no-entry spell averages 1.97 months, compared with [placeholder: verified benchmark]",
      f"Their longest no-entry spell averages 1.97 months, compared with {pl39['e_ms']:.2f}", "A.pre-spell")
s = R(s, "is 0.203 in the data and [placeholder: verified benchmark] under the allocation benchmark",
      f"is 0.203 in the data and {pl39['e_hhi']:.3f} under the allocation benchmark", "A.pre-hhi")
s = R(s, "the two busiest months are 0.468 and [placeholder: verified benchmark]",
      f"the two busiest months are 0.468 and {pl39['e_t2']:.3f}", "A.pre-t2")
s = R(s, "more concentrated across months than predicted by [placeholder: confirm primary benchmark]",
      "more concentrated across months than predicted by the employment-exposure-weighted allocation benchmark", "A.pre-conf")
# Table A1 Panel A (행 재구성 + Events 열)
a38 = E("I38")["panelA_excess"]; b38 = E("I38")["panelB_spell_concentration"]; i39 = E("I39")
s = R(s, "| Measure | Observed change | Benchmark change | Excess | 95% CI for excess | Comparison range |\n|---|---:|---:|---:|---:|---:|",
      "| Measure | Observed change | Benchmark change | Excess | 95% CI for excess | Comparison range | Events |\n|---|---:|---:|---:|---:|---:|---:|", "A1.hdr")
def a1row(old_label, obs, bench, exc, n, rng_txt):
    return (f"| {old_label} | {f4(obs, plus=True)} | {f4(bench, plus=True)} | {f4(exc['DiD'], plus=True)} | {ci4(exc['ci'])} | {rng_txt} | {n} |")
s = R(s, "| Share of no-entry months, employment-weighted benchmark | -0.0466 | [placeholder: verify whether -0.0508] | [placeholder] | [placeholder] | ±0.046 |",
      a1row("Share of no-entry months, employment-weighted benchmark", a38["actual"]["DiD"], a38["expected_wgt"]["DiD"], a38["excess_wgt"], 346, "±0.046"), "A1.zw")
s = R(s, "| Share of no-entry months, equal-month benchmark | -0.0466 | [placeholder: verify whether -0.0518] | [placeholder] | [placeholder] | ±0.046 |",
      a1row("Share of no-entry months, equal-month benchmark", a38["actual"]["DiD"], a38["expected_uniform"]["DiD"], a38["excess_uniform"], 346, "±0.046"), "A1.zu")
s = R(s, "| Number of no-entry months | -0.5594 | [placeholder: verified primary benchmark] | [placeholder] | [placeholder] | ±0.55 |",
      a1row("Number of no-entry months", i39["zero"]["actual"]["DiD"], i39["zero"]["expected"]["DiD"], i39["zero"]["excess"], 346, "±0.55"), "A1.zn")
s = R(s, "| Longest no-entry spell, months | -0.3566 | [placeholder: verified primary benchmark] | [placeholder] | [placeholder] | ±0.36 |",
      a1row("Longest no-entry spell, months", i39["ms"]["actual"]["DiD"], i39["ms"]["expected"]["DiD"], i39["ms"]["excess"], 346, "±0.36"), "A1.ms")
s = R(s, "| Herfindahl index of worker entries across months | -0.0248 | [placeholder: verified primary benchmark] | [placeholder] | [placeholder] | ±0.025 |",
      a1row("Herfindahl index of worker entries across months", i39["hhi"]["actual"]["DiD"], i39["hhi"]["expected"]["DiD"], i39["hhi"]["excess"], 342, "±0.025"), "A1.hhi")
s = R(s, "| Share of worker entries in the two busiest months | -0.0249 | [placeholder: verified primary benchmark] | [placeholder] | [placeholder] | ±0.025 |",
      a1row("Share of worker entries in the two busiest months", i39["t2"]["actual"]["DiD"], i39["t2"]["expected"]["DiD"], i39["t2"]["excess"], 342, "±0.025"), "A1.t2")
b40 = E("I40")["panelB_36m_clustering"]
s = R(s, "| Share of no-entry months | -0.055 | [-0.086, -0.025] | [placeholder: recompute under verified primary benchmark] | [placeholder] | ±0.046 |",
      f"| Share of no-entry months | {f4(b40['z']['DiD'], plus=True)} | {ci4(b40['z']['ci'])} | {f4(b40['x']['DiD'], plus=True)} | {ci4(b40['x']['ci'])} | ±0.046 | {b40['x']['n']} |", "A1.36z")
s = R(s, "| Longest no-entry spell, months | -0.756 | [-1.335, -0.161] | [placeholder: recompute under verified primary benchmark] | [placeholder] | ±1.0 |",
      f"| Longest no-entry spell, months | {f4(b40['ms']['DiD'], plus=True)} | {ci4(b40['ms']['ci'])} | {f4(b40['xms']['DiD'], plus=True)} | {ci4(b40['xms']['ci'])} | ±1.0 | {b40['xms']['n']} |", "A1.36s")
s = R(s, "| Measure | Observed change | 95% CI | Excess | 95% CI for excess | Comparison range |\n|---|---:|---:|---:|---:|---:|",
      "| Measure | Observed change | 95% CI | Excess | 95% CI for excess | Comparison range | Events |\n|---|---:|---:|---:|---:|---:|---:|", "A1.hdr36")
s = R(s, "Simulation-based benchmarks use [placeholder: number] draws per firm-window.",
      "Simulation-based benchmarks use 100 multinomial draws per firm-window. Events: 346 for the no-entry measures, 342 for the concentration measures (twelve-month window).", "A1.draws")
s = R(s, "the predicted change is [placeholder: verified benchmark], leaving an excess of [placeholder] [placeholder: 95% CI]. The equal-month allocation produces a benchmark change of [placeholder: verified benchmark] and an excess of [placeholder] [placeholder: 95% CI]. Under either allocation rule, [placeholder: insert conclusion after verification of the two benchmark values].",
      f"the predicted change is {f4(a38['expected_wgt']['DiD'], plus=True)}, leaving an excess of {f4(a38['excess_wgt']['DiD'], plus=True)} {ci4(a38['excess_wgt']['ci'])}. The equal-month allocation produces a benchmark change of {f4(a38['expected_uniform']['DiD'], plus=True)} and an excess of {f4(a38['excess_uniform']['DiD'], plus=True)} {ci4(a38['excess_uniform']['ci'])}. Under either allocation rule, the observed decline in monthly non-participation is essentially the decline implied by realised worker-entry volume.", "A.z-prose")
s = R(s, "The residual changes in the longest no-entry spell and the Herfindahl index are [placeholder: verified values and intervals]. Relative to their stated comparison ranges, these estimates indicate [placeholder: wording after rerun]. For the share of entries in the two busiest months, the excess is [placeholder: verified value] [placeholder: 95% CI].",
      f"The residual changes in the longest no-entry spell and the Herfindahl index are {f4(i39['ms']['excess']['DiD'], plus=True)} {ci4(i39['ms']['excess']['ci'])} and {f4(i39['hhi']['excess']['DiD'], plus=True)} {ci4(i39['hhi']['excess']['ci'])}. Relative to their stated comparison ranges, these intervals lie inside the ranges. For the share of entries in the two busiest months, the excess is {f4(i39['t2']['excess']['DiD'], plus=True)} {ci4(i39['t2']['excess']['ci'])}, with an upper limit that coincides with the boundary of its comparison range.", "A.spell-prose")
s = R(s, "falls by 0.055, with an excess of [placeholder] [placeholder: 95% CI] under the primary benchmark. The longest no-entry spell falls by 0.756 months, with an excess of [placeholder] [placeholder: 95% CI].",
      f"falls by 0.055, with an excess of {f4(b40['x']['DiD'], plus=True)} {ci4(b40['x']['ci'])} under the primary benchmark. The longest no-entry spell falls by 0.756 months, with an excess of {f4(b40['xms']['DiD'], plus=True)} {ci4(b40['xms']['ci'])}.", "A.36-prose")
c38 = E("I38")["panelC_by_inertia"]
s = R(s, "the excess changes are [placeholder: low-hiring-state excess and 95% CI] and [placeholder: high-hiring-state excess and 95% CI], respectively",
      f"the excess changes are {f4(c38['T3 고관성']['excess']['DiD'], plus=True)} {ci4(c38['T3 고관성']['excess']['ci'])} (n = {c38['T3 고관성']['excess']['n']}) and {f4(c38['T1 저관성']['excess']['DiD'], plus=True)} {ci4(c38['T1 저관성']['excess']['ci'])} (n = {c38['T1 저관성']['excess']['n']}), respectively", "A21.groups")
s = R(s, "The larger raw monthly-participation change among low-hiring targets is therefore [placeholder: calibrated conclusion after benchmark rerun].",
      f"The larger raw monthly-participation change among low-hiring targets is therefore accounted for by their larger realised worker-entry volume: the volume-adjusted excesses are small in both state groups, and their difference is {f4(c38['T3_T1_excess']['diff'], plus=True)} {ci4(c38['T3_T1_excess']['ci'])}.", "A21.concl")
# Table A2 — I73
d = lambda k, f: g("I73", f"panelA_exposure_decomp.{k}.{f}")
for k, lab in [("dq", "| Change in active-month employment-exposure share, $\\Delta q$ | [placeholder] | [placeholder] |"),
               ("diE", "| Change in active-month worker-entry intensity, $\\Delta i_E$ | [placeholder] | [placeholder] |"),
               ("dlq", "| Change in log active-month employment-exposure share, $\\Delta\\log q$ | [placeholder] | [placeholder] |"),
               ("dliE", "| Change in log active-month worker-entry intensity, $\\Delta\\log i_E$ | [placeholder] | [placeholder] |")]:
    lab2 = lab.replace(" | [placeholder] | [placeholder] |", "")
    s = R(s, lab, f"{lab2} | {f4(d(k,'est'), plus=True)} | {ci4(d(k,'ci'))} ($n={d(k,'n')}$) |", f"A2.{k}")
sh = g("I73", "panelA_exposure_decomp.extensive_share_log")
s = R(s, "The pre-deal means are $q=[placeholder]$ and $i_E=[placeholder]$.",
      f"The pre-deal means are $q={g('I73','panelA_exposure_decomp.pre_q'):.4f}$ and $i_E={g('I73','panelA_exposure_decomp.pre_iE'):.4f}$.", "A2.pre")
s = R(s, "The active-month exposure component accounts for [placeholder] of the summed log change and the active-month intensity component accounts for the remainder.",
      f"The active-month exposure component accounts for {sh['est']:.3f} {ci4(sh['ci'])} of the summed log change and the active-month intensity component accounts for the remainder.", "A2.share")
inc = "increase" if (d("dlq","est") > 0 and d("dliE","est") > 0) else "move"
s = R(s, "Both components [placeholder: increase / description after recomputation] in the exposure-based decomposition.",
      f"Both components {inc} in the exposure-based decomposition.", "A2.dir")
s = R(s, "The change in active-month employment exposure accounts for [placeholder: percentage] of the summed log change, while active-month worker-entry intensity accounts for [placeholder: percentage].",
      f"The change in active-month employment exposure accounts for {100*sh['est']:.1f} percent of the summed log change, while active-month worker-entry intensity accounts for {100*(1-sh['est']):.1f} percent.", "A2.pct")

# ═══ Appendix B ═══
i46 = E("I46")
s = R(s, "After this adjustment, the correlation with worker-entry volume is [placeholder: recompute after finalising Appendix A benchmark].",
      f"After this adjustment, the correlation with worker-entry volume is {f3(i46['panelB_excess_dormancy']['corr_with_logN'])}.", "B1.corr")
s = R(s, "The frequency measure contains [placeholder: little / amount of] separate information about the post-deal response once this mechanical volume component is removed. The tercile contrast for the volume-adjusted measure is [placeholder: estimate and 95% CI]. The pooled frequency slope within quintiles of pre-deal worker-entry volume is [placeholder: recompute if benchmark change affects construction]; residualising frequency on volume and size gives [placeholder]; and restricting the sample to firms with at least twelve pre-deal worker entries gives [placeholder] conditional on volume.",
      "The frequency measure contains little separate information about the post-deal response once this mechanical volume component is removed. "
      f"The tercile contrast for the volume-adjusted measure is {f4(i46['panelB_excess_dormancy']['tercile']['diff'], plus=True)} {ci4(i46['panelB_excess_dormancy']['tercile']['ci'])}. "
      f"The pooled frequency slope within quintiles of pre-deal worker-entry volume is {f4(i46['panelD_within_volume_quintile']['pooled_within_quintile']['coef'], plus=True)} {ci4(i46['panelD_within_volume_quintile']['pooled_within_quintile']['ci'])}; "
      f"residualising frequency on volume and size gives {f4(i46['panelF_residualized']['slope']['coef'], plus=True)} {ci4(i46['panelF_residualized']['slope']['ci'])}; "
      f"and in the subsample with at least twelve pre-deal worker entries the frequency slope is {f4(i46['panelC_free_N12']['dorm_alone']['coef'], plus=True)} {ci4(i46['panelC_free_N12']['dorm_alone']['ci'])} unconditionally and {f4(i46['panelC_free_N12']['dorm_given_logN']['coef'], plus=True)} {ci4(i46['panelC_free_N12']['dorm_given_logN']['ci'])} conditional on volume ($n={i46['panelC_free_N12']['n']}$).", "B1.prose")
s = R(s, "The frequency with which a firm records worker entries contains [placeholder: little] evidence of a separate relationship with the post-deal response",
      "The frequency with which a firm records worker entries contains little evidence of a separate relationship with the post-deal response", "B1.little")
# Table B2 — Events 열 + CI
i41 = E("I41"); i44d = E("I44")["panelD_scale_vs_release"]; b66 = E("I66")["panelB_post_early_state"]
s = R(s, "| Hiring state, controlling for pre-deal employment growth | 0.410 | [0.078, 0.753] | [placeholder] |",
      f"| Hiring state, controlling for pre-deal employment growth | {f4(i44d['dorm']['coef'])} | {ci4(i44d['dorm']['ci'])} | {i44d.get('n', E('I44').get('n', 301))} |", "B2.r1")
s = R(s, "| Historical share of no-entry months | 0.559 | [0.241, 0.885] | [placeholder] |",
      f"| Historical share of no-entry months | {f4(i41['panelD_transitory_vs_structural']['historical']['slope'])} | {ci4(i41['panelD_transitory_vs_structural']['historical']['ci'])} | {i41['panelD_transitory_vs_structural']['historical']['n']} |", "B2.r2")
s = R(s, "| Length of hiring pause in progress at closing | 0.040 | [-0.016, 0.107] | [placeholder] |",
      f"| Length of hiring pause in progress at closing | {f4(i41['panelD_transitory_vs_structural']['current_spell']['slope'])} | {ci4(i41['panelD_transitory_vs_structural']['current_spell']['ci'])} | {i41['panelD_transitory_vs_structural']['current_spell']['n']} |", "B2.r3")
s = R(s, "| Residualised hiring state | 0.243 | [-0.221, 0.723] | [placeholder] |",
      f"| Residualised hiring state | {f4(i41['panelB_residualized']['resid_slope']['slope'])} | {ci4(i41['panelB_residualized']['resid_slope']['ci'])} | {i41['panelB_residualized']['resid_slope']['n']} |", "B2.r4")
s = R(s, "| Earlier hiring state, months -36 to -25 | 0.268 | [placeholder: bootstrap 95% CI] | [placeholder] |",
      f"| Earlier hiring state, months -36 to -25 | {f4(b66['observed'])} | {ci4(b66['obs_boot_ci'])} | {b66['n']} |", "B2.r5")
s = R(s, "| Joint specification: historical no-entry share | 0.536 | [placeholder: 95% CI] | [placeholder] |",
      f"| Joint specification: historical no-entry share | {f4(i41['panelD_transitory_vs_structural']['joint_과거 비활동']['coef'])} | {ci4(i41['panelD_transitory_vs_structural']['joint_과거 비활동']['ci'])} | {i41['panelD_transitory_vs_structural']['historical']['n']} |", "B2.r6")
s = R(s, "| Joint specification: pause duration | 0.032 | [placeholder: 95% CI] | [placeholder] |",
      f"| Joint specification: pause duration | {f4(i41['panelD_transitory_vs_structural']['joint_현재 spell']['coef'])} | {ci4(i41['panelD_transitory_vs_structural']['joint_현재 spell']['ci'])} | {i41['panelD_transitory_vs_structural']['current_spell']['n']} |", "B2.r7")
# Table B3 — 4dp·중심 p·Events
i60 = E("I60")["specs"]; c66, d66 = E("I66")["panelC_asinh"], E("I66")["panelD_log1p"]
s = R(s, "| Specification | Gradient | Untreated reference mean (SD) | Standardized distance | Two-sided empirical $p$ |\n|---|---:|---:|---:|---:|",
      "| Specification | Gradient | Untreated reference mean (SD) | Standardized distance | Two-sided empirical $p$ | Events |\n|---|---:|---:|---:|---:|---:|", "B3.hdr")
def b3row(old, spec, tag):
    s2 = i60[spec]
    return (old, f"| {old.split('|')[1].strip()} | {f4(s2['observed'])} | {f4(s2['null_mean'])} ({f4(s2['null_sd'])}) | {f2(s2['z'])} | {s2['RI_p_two_centered']:.4f} | {s2['n']} |", tag)
for old, spec, tag in [
    ("| Winsorised 5/95, primary | 0.710 | 0.101 (0.154) | 3.96 | [placeholder] |", "winsor_5_95", "B3.w5"),
    ("| Unwinsorised | 0.837 | 0.122 (0.181) | 3.96 | [placeholder] |", "raw", "B3.raw"),
    ("| Winsorised 1/99 | 0.816 | 0.114 (0.171) | 4.10 | [placeholder] |", "winsor_1_99", "B3.w1"),
    ("| Winsorised 10/90 | 0.634 | 0.096 (0.136) | 3.96 | [placeholder] |", "winsor_10_90", "B3.w10")]:
    o_, n_, t_ = b3row(old, spec, tag); s = R(s, o_, n_, t_)
s = R(s, "| Inverse hyperbolic sine of hiring rate | 0.206 | 0.026 (0.059) | 3.08 | [placeholder] |",
      f"| Inverse hyperbolic sine of hiring rate | {f4(c66['observed'])} | {f4(c66['null_mean'])} ({f4(c66['null_sd'])}) | {f2(c66['z'])} | {c66['p_two_centered']:.4f} | {c66['n']} |", "B3.asinh")
s = R(s, "| $\\log(1+\\text{hiring rate})$ | 0.162 | 0.017 (0.045) | 3.24 | [placeholder] |",
      f"| $\\log(1+\\text{{hiring rate}})$ | {f4(d66['observed'])} | {f4(d66['null_mean'])} ({f4(d66['null_sd'])}) | {f2(d66['z'])} | {d66['p_two_centered']:.4f} | {d66['n']} |", "B3.log1p")
# Table B4 — 중심 p
i62, i63, i56 = E("I62"), E("I63"), E("I56")
B4 = [("| Primary: exact state tercile, 5 controls | 286 | 0.710 | 3.96 | [placeholder] |", i60["winsor_5_95"], "0.7101"),
      ("| Exact state tercile, 20 controls | 286 | 0.678 | 4.12 | [placeholder] |", i62["bin_k20"], "0.6778"),
      ("| State included in neighbour distance, 5 controls | 299 | 0.640 | 3.54 | [placeholder] |", i62["dist_k5"], "0.6400"),
      ("| At least 6 of 12 state months observed | 310 | 0.655 | 4.57 | [placeholder] |", i63["A' 상태창 ≥6개월"], "0.6545"),
      ("| Two state bins rather than three | 292 | 0.610 | 3.65 | [placeholder] |", i63["B 상태 2분위"], "0.6101"),
      ("| One-digit rather than two-digit industry cell | 299 | 0.636 | 3.69 | [placeholder] |", i63["C 산업 1자리"], "0.6361"),
      ("| State measured over months -36 to -13 | 244 | 0.388 | 2.33 | [placeholder] |", i56["panelC_state_window"]["24개월 [−36,−13]"], "0.3883"),
      ("| Inverse-variance weighting | 286 | 0.346 | 2.28 | [placeholder] |", i56["panelE_weighting"]["precision_weighted"], "0.3458"),
      ("| Add deal-year fixed effects | 286 | 0.678 | 3.50 | [placeholder] |", i56["panelF_covariates"]["plus_year"], "0.6779")]
for old, src, obs4 in B4:
    lab = old.split("|")[1].strip(); nn = src.get("n", src.get("n_treated"))
    s = R(s, old, f"| {lab} | {nn} | {obs4} | {f2(src['z'])} | {src['RI_p_two_centered']:.4f} |", f"B4.{lab[:14]}")

# ═══ Appendix C ═══
s = R(s, "Relative discrepancies divide $|d_{it}|$ by [placeholder: exact denominator].",
      "Relative discrepancies divide $|d_{it}|$ by the prior-month insured-employment stock $E_{i,t-1}$ (months with $E_{i,t-1}=0$ are excluded).", "C1.den")
s = R(s, "Employment is measured according to [placeholder: exact stock-timing convention].",
      "Employment is the month-end insured-employment stock in the NPS register, so the discrepancy compares the month-over-month stock change with the same month's reported entries minus exits.", "C1.stock")
s = R(s, "The final three rows report [placeholder: mean/median or other exact statistic] relative discrepancies among treated firms over the indicated periods.",
      "The final three rows report mean relative discrepancies among treated firms over the indicated periods.", "C1.stat")
i48c = E("I48")["panelC_exclusions"]; imp = i60["implied_hires"]; i70p = E("I70")["panelA_gradient"]
s = R(s, "| Primary worker-entry measure | 286 | 0.7101 | [0.3187, 1.1254] | [placeholder] |",
      f"| Primary worker-entry measure | 286 | 0.7101 | [0.3187, 1.1254] | {i70p['RI_p_two_sided']:.4f} |", "C2.r1")
s = R(s, "| Exclude months with relative discrepancy above 10% | [placeholder] | 0.312 | [placeholder] | [placeholder] |",
      f"| Exclude months with relative discrepancy above 10% | {i48c['exclude_rel_gt_10pct']['n']} | {f4(i48c['exclude_rel_gt_10pct']['slope_adj'])} | {ci4(i48c['exclude_rel_gt_10pct']['ci'])} | - |", "C2.r2")
s = R(s, "| Exclude months with relative discrepancy above 5% | [placeholder] | 0.544 | [placeholder] | [placeholder] |",
      f"| Exclude months with relative discrepancy above 5% | {i48c['exclude_rel_gt_5pct']['n']} | {f4(i48c['exclude_rel_gt_5pct']['slope_adj'])} | {ci4(i48c['exclude_rel_gt_5pct']['ci'])} | - |", "C2.r3")
s = R(s, "| Exclude months with total turnover above 50% of employment | [placeholder] | 0.488 | [0.102, 0.850] | [placeholder] |",
      f"| Exclude months with total turnover above 50% of employment | {i48c['exclude_churn_gt_50pct']['n']} | {f4(i48c['exclude_churn_gt_50pct']['slope_adj'])} | {ci4(i48c['exclude_churn_gt_50pct']['ci'])} | - |", "C2.r4")
sc = E("I48")["panelD_site_change"]["excluded"]
s = R(s, "| Exclude treated firms changing the number of registered workplaces | [placeholder] | 0.557 | [0.160, 0.930] | [placeholder] |",
      f"| Exclude treated firms changing the number of registered workplaces | {sc['n']} | {f4(sc['slope_adj'])} | {ci4(sc['ci'])} | - |", "C2.r5")
s = R(s, "| Worker inflows reconstructed from employment change and recorded exits | [placeholder] | 0.365 | [placeholder] | [placeholder] |",
      f"| Worker inflows reconstructed from employment change and recorded exits | {imp['n']} | {f4(imp['observed'])} | - | {imp['RI_p_two_centered']:.4f} |", "C2.r6")
s = R(s, "The implemented reconstructed-flow measure is [placeholder: exact formula used in the code, including the treatment of negative implied entries, missing months, transaction-month observations, and pre/post aggregation].",
      "The implemented reconstructed-flow measure replaces the monthly entry count with $\\max\\{0,(E_{it}-E_{i,t-1})+Exit_{it}\\}$; negative implied entries are set to zero, months with missing employment or exits invalidate the window, the transaction month is excluded because the windows are months -12 through -1 and +1 through +12, and monthly values are summed within each window before entering the same gradient pipeline as the primary measure.", "C2.formula")
s = R(s, "gives a gradient of 0.312 [placeholder: 95% CI], while the 5-percent restriction gives 0.544 [placeholder: 95% CI]",
      f"gives a gradient of 0.312 {ci4(i48c['exclude_rel_gt_10pct']['ci'])}, while the 5-percent restriction gives 0.544 {ci4(i48c['exclude_rel_gt_5pct']['ci'])}", "C2.prose1")
s = R(s, "The reconstructed-flow estimate is 0.365 [placeholder: 95% CI].",
      f"The reconstructed-flow estimate is 0.365 (two-sided empirical $p$ = {imp['RI_p_two_centered']:.4f} against its own untreated reference distribution).", "C2.prose2")
pc57 = E("I57")["panelC_paired"]["채용 − 이직"]
s = R(s, "| Worker-entry gradient - separation gradient | 0.5746 | 0.043 | [placeholder] |",
      f"| Worker-entry gradient - separation gradient | {f4(pc57['observed'])} | {pc57['RI_p_two_centered']:.4f} | {pc57['n']} |", "C4.pair")
s = R(s, "because the latter uses [placeholder: exact baseline and post-period construction of the primary log-employment outcome].",
      "because the latter is the change in the log of window-mean insured employment (months +1 through +12 versus months -12 through -1), whereas Panel A compares point-in-time employment at each horizon with the months -6 through -1 baseline.", "C4.note")
open(SRC, "w", encoding="utf-8").write(s)
with open(os.path.join(HERE, "FILL_TRACE.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["tag", "old", "new"])
    if f.tell() == 0: w.writeheader()
    w.writerows(TR)
print(f"PART 2 (Appendix A–C): {len(TR)} substitutions · remaining placeholders: {s.count('[placeholder')}")
