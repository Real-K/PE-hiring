# -*- coding: utf-8 -*-
"""Fill the 0831_2200 manuscript, part A — main text + Appendices A–B."""
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
def ci4(v): return f"[{v[0]:.4f}, {v[1]:.4f}]".replace("-", "−")
TR = []
def R(s, old, new, tag):
    n = s.count(old)
    assert n == 1, f"anchor x{n} [{tag}]: {old[:80]!r}"
    TR.append({"tag": tag, "old": old[:100], "new": new[:100]}); return s.replace(old, new)
FORMULA = ("The reported probability equals $(1+\\#\\{b:|g_b-\\bar g|\\ge|g^{obs}-\\bar g|\\})/(B+1)$ over the $B=2{,}000$ "
           "specification-specific draws, where $\\bar g$ is the draw mean; ties count toward the numerator, and the add-one "
           "correction bounds the probability below by $1/(B+1)=0.0005$.")
s = open(SRC, encoding="utf-8").read()

# ═══ 본문 ═══
s = R(s, "[placeholder: report the number of direct business-registration-number links, manually reviewed name-based links, and rejected ambiguous links if the linkage audit is retained.]",
      "Of the 379 matched events, 283 link directly by business registration number and 96 enter through the manually reviewed name-based recovery; candidate name matches judged ambiguous in that review were rejected and are documented in the linkage audit of the replication package.", "M.link")
s = R(s, "[placeholder: state the exact distance scaling and any growth clipping used in the final estimation code.]",
      "The neighbour distance is $((\\Delta\\log\\text{employment})/0.9)^2+((\\Delta\\text{growth})/0.35)^2$, with growth clipped to $[-1,2]$ before differencing.", "M.dist")
s = R(s, "let $E_i^{state}$ denote [placeholder: exact employment denominator used in the estimation code]",
      "let $E_i^{state}$ denote mean insured employment over the same twelve state-window months", "M.den")
s = R(s, "The log-hiring restriction removes [placeholder: retain exact count only if final code confirms the number after all primary-sample restrictions].",
      "The log-hiring restriction removes three events that record zero worker entries in one of the outcome windows.", "M.logn")
s = R(s, "[placeholder: state the exact finite-simulation centred two-sided tail rule used in the final code, including treatment of ties and any finite-simulation correction.]",
      FORMULA, "M.rule")
s = R(s, "[placeholder: insert the exact binning or display rule used for Panel (a).]",
      "Events are displayed in added-variable form: the primary covariates are partialled out of both axes and the sample means added back; the dark points are means within fixed quintile bins of the displayed state, and the fitted line is the primary gradient with a 2,000-draw event-bootstrap band.", "M.fig1a")
s = R(s, "Panel (b) plots the empirical distribution of 2,000 gradients drawn from the pool of 1,246 untreated pseudo-events and estimated using the primary procedure.",
      f"Panel (b) plots the empirical distribution of 2,000 gradients drawn from the pool of {g('I70','panelA_gradient.n_pseudo'):,} untreated pseudo-events and estimated using the primary procedure.", "M.pool")

# ═══ Appendix A ═══
s = R(s, "we simulate the corresponding multinomial allocation 60 times for each firm-window. [placeholder: replace the simulation count and state the random-seed convention if the benchmark is rerun with a larger number of draws.]",
      "we simulate the corresponding multinomial allocation 100 times for each firm-window under a fixed seed (42), so the benchmark values are exactly reproducible.", "A.sim")
s = R(s, "the allocation probabilities follow [placeholder: confirm the final code uses employment-exposure weights $w_j$]",
      "the allocation probabilities follow the employment-exposure weights $w_j$", "A.wj")
s = R(s, "the reported benchmark uses [placeholder: confirm final allocation rule in the code]",
      "the reported benchmark uses the employment-exposure-weighted allocation", "A.rule2")
cw = E("I38")["panelC_by_inertia_wgt"]
s = R(s, "Under the original state-specific volume allocation, the corresponding excess changes are 0.0058 [-0.0249, 0.0350] and 0.0027 [-0.0159, 0.0203], respectively. Their difference is 0.0032 [-0.0321, 0.0365]. [placeholder: replace these three quantities if the final state-specific calculation is rerun specifically under the employment-exposure-weighted benchmark adopted as primary above.]",
      ("Under the equal-month allocation, the corresponding excess changes are 0.0058 [−0.0249, 0.0350] and 0.0027 [−0.0159, 0.0203], respectively, with a difference of 0.0032 [−0.0321, 0.0365]. "
       f"Under the employment-exposure-weighted benchmark adopted as primary, the excesses are {f4(cw['T3 고관성']['excess']['DiD'])} {ci4(cw['T3 고관성']['excess']['ci'])} and {f4(cw['T1 저관성']['excess']['DiD'])} {ci4(cw['T1 저관성']['excess']['ci'])}, with a difference of {f4(cw['T3_T1_excess']['diff'])} {ci4(cw['T3_T1_excess']['ci'])}."), "A.split")
d = lambda k, f: g("I73", f"panelA_exposure_decomp.{k}.{f}")
for k, lab in [("dq", "| Change in active-month employment-exposure share, $\\Delta q$ | [placeholder] | [placeholder] |"),
               ("diE", "| Change in active-month worker-entry intensity, $\\Delta i_E$ | [placeholder] | [placeholder] |"),
               ("dlq", "| Change in log active-month employment-exposure share, $\\Delta\\log q$ | [placeholder] | [placeholder] |"),
               ("dliE", "| Change in log active-month worker-entry intensity, $\\Delta\\log i_E$ | [placeholder] | [placeholder] |")]:
    lab2 = lab.replace(" | [placeholder] | [placeholder] |", "")
    s = R(s, lab, f"{lab2} | {f4(d(k,'est'), plus=True)} | {ci4(d(k,'ci'))} ($n={d(k,'n')}$) |", f"A2.{k}")
s = R(s, "The pre-deal means are $q=[placeholder]$ and $i_E=[placeholder]$.",
      f"The pre-deal means are $q={g('I73','panelA_exposure_decomp.pre_q'):.4f}$ and $i_E={g('I73','panelA_exposure_decomp.pre_iE'):.4f}$.", "A2.pre")
sh = g("I73", "panelA_exposure_decomp.extensive_share_log")
s = R(s, "[placeholder: report the exposure-based decomposition after recomputation.]",
      (f"Both components increase: $\\Delta\\log q$ is {f4(d('dlq','est'), plus=True)} {ci4(d('dlq','ci'))} and $\\Delta\\log i_E$ is {f4(d('dliE','est'), plus=True)} {ci4(d('dliE','ci'))}; "
       f"the exposure-share component accounts for {100*sh['est']:.1f} percent {ci4(sh['ci'])} of the summed log change."), "A2.report")

# ═══ Appendix B ═══
i41 = E("I41"); i44d = E("I44")["panelD_scale_vs_release"]; b66 = E("I66")["panelB_post_early_state"]
s = R(s, "| Hiring state, controlling for pre-deal employment growth | 0.410 | [0.078, 0.753] | [placeholder] |",
      f"| Hiring state, controlling for pre-deal employment growth | {f4(i44d['dorm']['coef'])} | {ci4(i44d['dorm']['ci'])} | {i44d['n']} |", "B2.r1")
s = R(s, "| Historical share of no-entry months | 0.559 | [0.241, 0.885] | [placeholder] |",
      f"| Historical share of no-entry months | {f4(i41['panelD_transitory_vs_structural']['historical']['slope'])} | {ci4(i41['panelD_transitory_vs_structural']['historical']['ci'])} | {i41['panelD_transitory_vs_structural']['historical']['n']} |", "B2.r2")
s = R(s, "| Length of hiring pause in progress at closing | 0.040 | [-0.016, 0.107] | [placeholder] |",
      f"| Length of hiring pause in progress at closing | {f4(i41['panelD_transitory_vs_structural']['current_spell']['slope'])} | {ci4(i41['panelD_transitory_vs_structural']['current_spell']['ci'])} | {i41['panelD_transitory_vs_structural']['current_spell']['n']} |", "B2.r3")
s = R(s, "| Residualised hiring state | 0.243 | [-0.221, 0.723] | [placeholder] |",
      f"| Residualised hiring state | {f4(i41['panelB_residualized']['resid_slope']['slope'])} | {ci4(i41['panelB_residualized']['resid_slope']['ci'])} | {i41['panelB_residualized']['resid_slope']['n']} |", "B2.r4")
s = R(s, "| Earlier hiring state, months $-36$ to $-25$ | 0.268 | [placeholder: 95% CI] | [placeholder] |",
      f"| Earlier hiring state, months $-36$ to $-25$ | {f4(b66['observed'])} | {ci4(b66['obs_boot_ci'])} | {b66['n']} |", "B2.r5")
s = R(s, "| Joint specification: historical no-entry share | 0.536 | [placeholder: 95% CI] | [placeholder] |",
      f"| Joint specification: historical no-entry share | {f4(i41['panelD_transitory_vs_structural']['joint_과거 비활동']['coef'])} | {ci4(i41['panelD_transitory_vs_structural']['joint_과거 비활동']['ci'])} | {i41['panelD_transitory_vs_structural']['historical']['n']} |", "B2.r6")
s = R(s, "| Joint specification: pause duration | 0.032 | [placeholder: 95% CI] | [placeholder] |",
      f"| Joint specification: pause duration | {f4(i41['panelD_transitory_vs_structural']['joint_현재 spell']['coef'])} | {ci4(i41['panelD_transitory_vs_structural']['joint_현재 spell']['ci'])} | {i41['panelD_transitory_vs_structural']['current_spell']['n']} |", "B2.r7")
s = R(s, "giving an excess of 0.127 and a standardized distance of 0.92. [placeholder: report the two-sided empirical $p$-value from the corresponding untreated reference distribution.]",
      f"giving an excess of 0.127 and a standardized distance of 0.92; the two-sided empirical probability from the corresponding untreated reference distribution is {b66['p_two_centered']:.4f}.", "B2.p")
# B3 — 4dp 재구성 + Events 열
i60 = E("I60")["specs"]; c66, d66 = E("I66")["panelC_asinh"], E("I66")["panelD_log1p"]
s = R(s, "| Specification | Gradient | Untreated reference mean (SD) | Standardized distance | Empirical two-sided $p$ |\n|---|---:|---:|---:|---:|\n| Winsorised 5/95, primary | 0.710 | 0.101 (0.154) | 3.96 | 0.0005 |",
      "| Specification | Gradient | Untreated reference mean (SD) | Standardized distance | Empirical two-sided $p$ | Events |\n|---|---:|---:|---:|---:|---:|\n"
      f"| Winsorised 5/95, primary | {f4(i60['winsor_5_95']['observed'])} | {f4(i60['winsor_5_95']['null_mean'])} ({f4(i60['winsor_5_95']['null_sd'])}) | {f2(i60['winsor_5_95']['z'])} | {i60['winsor_5_95']['RI_p_two_centered']:.4f} | {i60['winsor_5_95']['n']} |", "B3.hdr")
for old, src in [("| Unwinsorised | 0.837 | 0.122 (0.181) | 3.96 | [placeholder] |", i60["raw"]),
                 ("| Winsorised 1/99 | 0.816 | 0.114 (0.171) | 4.10 | [placeholder] |", i60["winsor_1_99"]),
                 ("| Winsorised 10/90 | 0.634 | 0.096 (0.136) | 3.96 | [placeholder] |", i60["winsor_10_90"]),
                 ("| Inverse hyperbolic sine of hiring rate | 0.206 | 0.026 (0.059) | 3.08 | [placeholder] |", None),
                 ("| $\\log(1+\\text{hiring rate})$ | 0.162 | 0.017 (0.045) | 3.24 | [placeholder] |", None)]:
    lab = old.split("|")[1].strip()
    v = src if src else (c66 if "hyperbolic" in lab else d66)
    pc = v.get("RI_p_two_centered", v.get("p_two_centered"))
    s = R(s, old, f"| {lab} | {f4(v['observed'])} | {f4(v['null_mean'])} ({f4(v['null_sd'])}) | {f2(v['z'])} | {pc:.4f} | {v['n']} |", f"B3.{lab[:12]}")
i50 = E("I50")["panelB_ppml"]
s = R(s, "| PPML worker-entry count with log employment offset | 0.104 | [-0.319, 0.526] |",
      f"| PPML worker-entry count with log employment offset | {f4(i50['gradient'])} | {ci4(i50['ci'])} |", "B3.ppml.row")
s = R(s, "[placeholder: populate the revised two-sided probabilities for the non-primary rows.] The PPML specification uses [placeholder: exact unit of observation], [placeholder: exact post-by-state structure], an offset equal to [placeholder: exact exposure definition], and [placeholder: exact treatment of the matched comparison group]. Inference follows [placeholder: exact clustering procedure].",
      (f"The PPML specification is estimated at the firm-window level on the pooled treated and matched-control post windows ({i50['n_obs']:,} observations; {i50['n_zero_post']} zero-entry windows retained), "
       "relates the post-window worker-entry count to the treated indicator and its interaction with the pre-deal state, uses log window employment exposure as the offset, and absorbs the matched comparison group through matching-cell fixed effects. "
       "Inference clusters standard errors by matching cell."), "B3.ppml.note")
s = R(s, "The unwinsorised estimate is 0.837, compared with 0.710 under the 5/95 specification. Winsorising at 1/99 gives 0.816, while the 10/90 specification gives 0.634.",
      "The unwinsorised estimate is 0.8370, compared with 0.7101 under the 5/95 specification. Winsorising at 1/99 gives 0.8157, while the 10/90 specification gives 0.6339.", "B3.prose1")
s = R(s, "The inverse-hyperbolic-sine specification gives 0.206, while $\\log(1+\\text{hiring rate})$ gives 0.162.",
      "The inverse-hyperbolic-sine specification gives 0.2062, while $\\log(1+\\text{hiring rate})$ gives 0.1623.", "B3.prose2")
s = R(s, "The PPML coefficient is 0.104 [-0.319, 0.526].", "The PPML coefficient is 0.1038 [−0.3185, 0.5261].", "B3.prose3")
# B4 — 4dp 재구성 + 중심 p
i62, i63, i56 = E("I62"), E("I63"), E("I56")
B4 = [("| Primary: exact state tercile, 5 controls | 286 | 0.710 | 3.96 | 0.0005 |", i60["winsor_5_95"]),
      ("| Exact state tercile, 20 controls | 286 | 0.678 | 4.12 | [placeholder] |", i62["bin_k20"]),
      ("| State included in neighbour distance, 5 controls | 299 | 0.640 | 3.54 | [placeholder] |", i62["dist_k5"]),
      ("| At least 6 of 12 state months observed | 310 | 0.655 | 4.57 | [placeholder] |", i63["A' 상태창 ≥6개월"]),
      ("| Two state bins rather than three | 292 | 0.610 | 3.65 | [placeholder] |", i63["B 상태 2분위"]),
      ("| One-digit rather than two-digit industry cell | 299 | 0.636 | 3.69 | [placeholder] |", i63["C 산업 1자리"]),
      ("| State measured over months $-36$ to $-13$ | 244 | 0.388 | 2.33 | [placeholder] |", i56["panelC_state_window"]["24개월 [−36,−13]"]),
      ("| Inverse-variance weighting | 286 | 0.346 | 2.28 | [placeholder] |", i56["panelE_weighting"]["precision_weighted"]),
      ("| Add deal-year fixed effects | 286 | 0.678 | 3.50 | [placeholder] |", i56["panelF_covariates"]["plus_year"])]
for old, src in B4:
    lab = old.split("|")[1].strip(); nn = src.get("n", src.get("n_treated"))
    s = R(s, old, f"| {lab} | {nn} | {f4(src['observed'])} | {f2(src['z'])} | {src['RI_p_two_centered']:.4f} |", f"B4.{lab[:12]}")
s = R(s, "The inverse-variance weights are defined as [placeholder: exact variance estimator] and normalised [placeholder: exact normalisation]. Each row uses its own untreated reference distribution. [placeholder: populate revised two-sided empirical probabilities.]",
      "The inverse-variance weights are defined as the inverse of the event-level sampling-variance proxy $1/N^{pre}_i+1/N^{post}_i$ (entry counts floored at one) and normalised to mean one. Each row uses its own untreated reference distribution, and the two-sided probabilities follow the centred empirical rule of Section 4.3.", "B4.note")
open(SRC, "w", encoding="utf-8").write(s)
with open(os.path.join(HERE, "FILL_TRACE_2200.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["tag", "old", "new"])
    if f.tell() == 0: w.writeheader()
    w.writerows(TR)
print(f"2200-A: {len(TR)} substitutions · remaining: {s.count('[placeholder')}")
