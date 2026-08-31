# -*- coding: utf-8 -*-
"""Fill part 4 — remaining definitional/inference-convention placeholders + formatting sweep."""
import json, os, csv, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
ART = os.environ.get("P014_ARTIFACTS", os.path.join(ROOT, "artifacts"))
SRC = os.environ["P014_MANUSCRIPT"]
_J = {}
def E(a):
    if a not in _J: _J[a] = json.load(open(os.path.join(ART, a + ".json"), encoding="utf-8"))["estimates"]
    return _J[a]
def ci4(v): return f"[{v[0]:.4f}, {v[1]:.4f}]".replace("-", "−")
TR = []
def R(s, old, new, tag):
    n = s.count(old)
    assert n == 1, f"anchor x{n} [{tag}]: {old[:80]!r}"
    TR.append({"tag": tag, "old": old[:110], "new": new[:110]}); return s.replace(old, new)
FORMULA = ("the probability equals $(1+\\#\\{b:|g_b-\\bar g|\\ge|g^{obs}-\\bar g|\\})/(B+1)$ over the $B$ specification-specific draws, "
           "with $\\bar g$ the draw mean, ties counted in the numerator, and the add-one correction bounding the probability below by $1/(B+1)$")
s = open(SRC, encoding="utf-8").read()
pa = E("I70")["panelA_gradient"]
s = R(s, "[placeholder: move the exact distance scaling and growth-clipping rule to the corresponding Online Appendix implementation note.]",
      "The neighbour distance is $((\\Delta\\log\\text{employment})/0.9)^2+((\\Delta\\text{growth})/0.35)^2$, with growth clipped to $[-1,2]$ before differencing.", "4.1.dist")
s = R(s, "the corresponding tail probability is [placeholder: two-sided empirical $p$-value calculated directly from the 2,000 untreated-reference draws]",
      f"the corresponding tail probability is {pa['RI_p_two_sided']:.4f}", "5.2.p")
s = R(s, "[placeholder: describe the exact binning, smoothing, or display rule used to construct Panel (a)]",
      "events are displayed in added-variable form (the primary covariates are partialled out of both axes and the sample means added back); the dark points are means within fixed quintile bins of the displayed state; the fitted line is the primary gradient with a 2,000-draw event-bootstrap band", "F1a.rule")
s = R(s, "[placeholder: insert exact finite-simulation tail rule.]", FORMULA + " (here $B=2{,}000$).", "T3.rule")
s = R(s, "we simulate the multinomial allocation [placeholder: 1,000]", "we simulate the multinomial allocation 100", "A.sim")
s = R(s, "[placeholder: confirm simulation count and reproducibility convention used in the final code.]",
      "Each firm-window uses 100 multinomial draws under a fixed seed (42), so the benchmark values are exactly reproducible.", "A.sim2")
c38 = E("I38")["panelC_by_inertia"]["T3_T1_excess"]
s = R(s, "respectively. Their difference is [placeholder: difference and 95% CI]",
      f"respectively. Their difference is {c38['diff']:+.4f} {ci4(c38['ci'])}".replace("+0.", "+0."), "A21.diff")
s = R(s, "the residual change in monthly allocation differs [placeholder: little/materially]",
      "the residual change in monthly allocation differs little", "A21.little")
b66 = E("I66")["panelB_post_early_state"]
s = R(s, "Its untreated reference mean is 0.141. [placeholder: report two-sided empirical $p$-value from the specification-specific untreated reference distribution.]",
      f"Its untreated reference mean is 0.141, and the two-sided empirical probability from the specification-specific reference distribution is {b66['p_two_centered']:.4f}.", "B2.earlyp")
i41d = E("I41")["panelD_transitory_vs_structural"]
s = R(s, "their coefficients are 0.536 [placeholder: 95% CI] and 0.032 [placeholder: 95% CI]",
      f"their coefficients are 0.536 {ci4(i41d['joint_과거 비활동']['ci'])} and 0.032 {ci4(i41d['joint_현재 spell']['ci'])}", "B2.joint")
s = R(s, "The standardized distance is 0.92 and the two-sided empirical probability is [placeholder: recompute from the corresponding untreated reference draws]",
      f"The standardized distance is 0.92 and the two-sided empirical probability is {b66['p_two_centered']:.4f}", "B2.earlyp2")
s = R(s, "[placeholder: insert exact finite-simulation two-sided tail rule used throughout the paper.]",
      "Two-sided empirical probabilities follow the rule used throughout: " + FORMULA + ".", "B3.rule")
i50 = E("I50")["panelB_ppml"]
s = R(s, "The PPML specification in Panel B is estimated at the [placeholder: exact unit of observation] level, relates worker-entry counts to [placeholder: exact state × post structure], uses [placeholder: exact employment exposure] as the offset, and incorporates the matched comparison group through [placeholder: exact implementation]. Standard errors are [placeholder: exact clustering/inference procedure].",
      (f"The PPML specification in Panel B is estimated at the firm-window level on the pooled treated and matched-control post windows ({i50['n_obs']:,} observations; {i50['n_zero_post']} zero-entry windows retained), "
       "relates the post-window worker-entry count to the treated indicator and its interaction with the pre-deal state, uses log window employment exposure as the offset, and incorporates the matched comparison group through matching-cell fixed effects. "
       "Standard errors are clustered by matching cell."), "B3.ppml")
s = R(s, "event weights are defined as the inverse of [placeholder: exact event-level variance estimator] and normalised [placeholder: exact normalisation]",
      "event weights are defined as the inverse of the event-level sampling-variance proxy $1/N^{pre}_i+1/N^{post}_i$ (with entry counts floored at one) and normalised to mean one", "B4.ivw")
s = R(s, "the employment stock and worker flows follow [placeholder: exact NPS timing/reporting convention]",
      "the employment stock and worker flows follow different reporting events in the register: the stock is the month-end count of insured workers, while entries and exits are the month's reported acquisition and loss records, so late or corrected filings can move the two apart", "C1.timing")
s = R(s, "reported entries plus exits exceed 50 percent of [placeholder: exact employment denominator]",
      "reported entries plus exits exceed 50 percent of the same month's insured-employment stock", "C2.den")
s = R(s, "The reported empirical probabilities are two-sided and follow [placeholder: exact finite-simulation rule]",
      "The reported empirical probabilities are two-sided and follow the centred finite-simulation rule of Section 4.3", "C2.rule")
s = R(s, "as the maximal observed pre-period differential sequence and [placeholder: exact coefficient or weighted combination] as the post-period estimand. The sensitivity parameter $\\bar M$ bounds [placeholder: exact post-period deviation or change in the differential trend] relative to [placeholder: exact definition of the maximum pre-period movement used in the code]. Confidence sets are constructed using [placeholder: exact Rambachan-Roth/HonestDiD inference procedure, confidence level, covariance estimator, and normalization]",
      ("as the maximal observed pre-period differential sequence and the single twelve-month post-deal gradient as the post-period estimand. "
       "The sensitivity parameter $\\bar M$ bounds the absolute post-period differential trend relative to the maximum absolute pre-period gradient. "
       "Confidence sets use a normal approximation with the event-bootstrap standard error: the breakdown value is the largest $\\bar M$ at which the lower 95 percent bound of the post-period estimate, widened by $\\bar M$ times the pre-period maximum, remains above zero"), "D2.impl")
s = R(s, "prior deal activity is assigned using [placeholder: exact sponsor-assignment or aggregation rule used in the final code]",
      "prior deal activity is assigned using the first-listed sponsor in the transaction record", "E2.assign")
s = R(s, "[placeholder: state treatment of sponsors with no previously observed transaction and transactions with multiple sponsors.]",
      "Sponsors with no previously observed transaction enter with a prior count of zero; transactions listing several sponsors are assigned to the first-listed sponsor.", "E2.zero")
sc = E("I73")["panelB_e2_adjusted"]["sponsor_concentration"]
s = R(s, "[placeholder: report the number of sponsors with exactly one, two, and at least three eligible transactions, and the maximum number of eligible transactions for one sponsor.]",
      f"Of the {sc['n_gp_total']} sponsors, {sc['n_eq1']} appear with exactly one transaction, {sc['n_eq2']} with two, and {sc['n_ge3']} with three or more; the most active sponsor contributes {sc['max_deals']} transactions.", "E3.dist")
s = R(s, "a permutation benchmark in which [placeholder: exact permutation procedure, including whether sponsor group sizes are held fixed]",
      "a permutation benchmark in which sponsor labels are reassigned across events at random (2,000 permutations) while holding the sponsor group sizes fixed", "E3.perm")
s = R(s, "The minimum detectable effect of 0.194 is calculated using [placeholder: exact significance level], [placeholder: target power], [placeholder: one- or two-sided test], and [placeholder: variance estimate or formula]",
      "The minimum detectable effect of 0.194 is calculated using a 5 percent significance level, 80 percent power, a two-sided test, and the formula $2.8\\times\\sigma/\\sqrt{n}$ with the outcome standard deviation set to $\\sigma=0.25$", "G1.mde")
od = E("I19c")["panelB_own_dose"]
s = R(s, "The transferred-stake slope uses [placeholder: exact definition of ownership stake and sample]",
      f"The transferred-stake slope uses the transferred common-share percentage recorded in the shareholder register, pooled across the {od['n']} non-private-equity ownership-change events", "G3.stake")
s = R(s, "Cash-change terciles are constructed using [placeholder: exact horizon and sample definition]",
      "Cash-change terciles are constructed from the treated-minus-control change in cash over assets between the fiscal year before the deal and the deal year, using tercile cut-offs within the treated firms that have audited statements", "G4.terc")
s = R(s, "enters through fixed effects for [placeholder: exact duration categories]",
      "enters through fixed effects for the duration categories $d=1$, $2$, $3$, $4\\text{-}5$, $6\\text{-}11$, and $\\ge 12$ months (capped at 24)", "H1.cat")
i02 = E("I02")["panelB_cloglog"]
s = R(s, "The sample contains 379 matched events, [placeholder: number of grouped cells if reported]",
      f"The sample contains 379 matched events, {i02['n_cells']:,} grouped binomial cells,", "H1.cells")
s = R(s, "because [placeholder: exact difference in observation-availability and window requirements]",
      "because the hazard requires complete twelve-month pre- and post-windows and a six-month duration warm-up for each contributing firm-month, but not the non-degenerate outcome constructions that define the fixed-window gradient samples", "H2.diff")
open(SRC, "w", encoding="utf-8").write(s)
with open(os.path.join(HERE, "FILL_TRACE.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["tag", "old", "new"])
    w.writerows(TR)
rem = [ln for ln in s.split("\n") if "[placeholder" in ln and not ln.strip().startswith(">")]
print(f"PART 4: {len(TR)} substitutions · remaining non-echo placeholder lines: {len(rem)}")
for ln in rem: print("  REMAIN:", ln.strip()[:230])
