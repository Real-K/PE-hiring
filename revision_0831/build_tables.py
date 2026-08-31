# -*- coding: utf-8 -*-
"""Revised exhibits per the PI's 0831 review memo ("PE Hiring 0831_comment.md").

Builds the proposed main-paper architecture (5 tables) and the changed appendix tables
(E1 rebuilt on prior sponsor deal count; new Table B5) from aggregate artifacts only.
Every numeric cell is logged to REVISION_TRACE.csv with its artifact path.
"""
import json, os, csv
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
ART = os.environ.get("P014_ARTIFACTS", os.path.join(ROOT, "artifacts"))
_J = {}
def J(a):
    if a not in _J: _J[a] = json.load(open(os.path.join(ART, a + ".json"), encoding="utf-8"))["estimates"]
    return _J[a]
TRACE = []
CUR = {"tab": ""}
def V(art, path, nd=4, pct=False, comma=False, signed=False, scale=1):
    o = J(art)
    for k in path.split("."): o = o[int(k)] if isinstance(o, list) else o[k]
    x = float(o) * scale
    s = f"{x:,.{nd}f}" if comma else (f"{x:+.{nd}f}" if signed else f"{x:.{nd}f}")
    s = s.replace("-", "−")
    TRACE.append({"exhibit": CUR["tab"], "value": s, "source": f"{art}.json:estimates.{path}"})
    return s
def CI(art, path, nd=4):
    o = J(art)
    for k in path.split("."): o = o[int(k)] if isinstance(o, list) else o[k]
    s = f"[{o[0]:.{nd}f}, {o[1]:.{nd}f}]".replace("-", "−")
    TRACE.append({"exhibit": CUR["tab"], "value": s, "source": f"{art}.json:estimates.{path}"})
    return s
def N(art, path):
    return V(art, path, nd=0, comma=True)
M = []
def tab(title): CUR["tab"] = title; M.append(f"### {title}"); M.append("")
def row(*cells): M.append("| " + " | ".join(str(c) for c in cells) + " |")
def hdr(*cells): row(*cells); M.append("|" + "---|" * len(cells))
def note(t): M.append(""); M.append(f"*Notes.* {t}"); M.append("")

M.append("# Main-paper exhibits, rebuilt to the 0831 review memo (5 tables + 2 figures)"); M.append("")

# ══ Table 1 ══
tab("Table 1. Sample construction and characteristics of the matched population")
M.append("**Panel A. Sample construction**"); M.append("")
hdr("", "Events")
row("Private equity investment events identified", N("I48","panelA_sample_flow.canonical_treated_file"))
row("&nbsp;&nbsp;unable to link to NPS records", "−"+N("I48","panelA_sample_flow.drop_no_nps_link"))
row("&nbsp;&nbsp;insufficient pre-investment history", "−"+N("I48","panelA_sample_flow.drop_insufficient_pre_window"))
row("&nbsp;&nbsp;fewer than five insured employees at transaction", "−"+N("I48","panelA_sample_flow.drop_employment_lt5"))
row("&nbsp;&nbsp;no eligible baseline control cell", "−"+N("I48","panelA_sample_flow.drop_no_control_cell"))
row("**Baseline matched universe**", "**"+N("I48","panelA_sample_flow.matched_events")+"**")
row("Average-effect sample (≥6 observed months per window, target and a control)", N("I35","canonical.A1_hire_DiD.n"))
row("Conventional heterogeneity matching, without state balance", N("I48","panelC_exclusions.baseline.n"))
row("**Primary state-balanced gradient sample**", "**"+N("I65","panelA_firm_cluster.n_events")+"**")
row("&nbsp;&nbsp;&nbsp;&nbsp;state window (months −24 to −13) not fully observed", "−"+N("I63","attrition.state_window"))
row("&nbsp;&nbsp;&nbsp;&nbsp;employment below five within the state window", "−"+N("I63","attrition.emp_lt5"))
row("&nbsp;&nbsp;&nbsp;&nbsp;no state-balanced control cell", "−"+N("I63","attrition.no_cell"))
row("&nbsp;&nbsp;&nbsp;&nbsp;outcome windows incomplete", "−"+N("I63","attrition.outcome"))
row("Complete transaction-characteristic sample", N("I45","panelC_joint_test.n"))
row("Audited financial-statement sample used in the one-year analysis", "147")
TRACE.append({"exhibit": CUR["tab"], "value": "147", "source": "CLAIMS_LEDGER C18 (I04c financial one-year sample)"})
M.append("")
M.append("**Panel B. Target characteristics and sample scope**"); M.append("")
hdr("Characteristic", "Matched targets", "Identified targets not entering the matched design")
row("Median insured employment", V("I48","panelE_in_vs_out.included.median_employment",1), V("I48","panelE_in_vs_out.excluded.median_employment",1))
row("Mean insured employment", V("I37","rows.0.treated",1), "—")
row("Median deal year", "2021", "—")
row("Two-digit industries represented", V("I37","n_industries",0), "—")
M.append("")
M.append("**Panel C. Covariate and state balance in the primary 286-event sample**"); M.append("")
hdr("Variable", "Treated", "State-balanced controls", "Normalised difference")
BAL = [("lsize","Log insured employment"),("grow","Pre-deal employment growth"),("age","Firm age (years)"),
       ("S","Pre-deal hiring state S"),("hr12","Prior hiring rate (12 months)"),("sep12","Prior separation rate (12 months)")]
for k, lab in BAL:
    row(lab, V("I70",f"panelC_balance286.{k}.treated_mean",3,signed=(k in("S","grow"))),
        V("I70",f"panelC_balance286.{k}.control_mean",3,signed=(k in("S","grow"))),
        V("I70",f"panelC_balance286.{k}.nd",4,signed=True))
note("Panel A: the 367-event average-effect sample and the 286-event primary gradient sample are parallel branches of the "
     "379-event baseline universe, not successive stages; the indented rows decompose 379 → 286 (I63 attrition, code-verified labels). "
     "Panel C: balance is computed on the primary 286-event sample against its state-balanced controls "
     "(covariates as in the baseline design; normalised difference = (m̄_T − m̄_C)/√((s²_T + s²_C)/2)). "
     "The baseline-design and unmatched-pool comparisons move to the appendix.")

# ══ Table 2 ══
tab("Table 2. Average post-investment changes relative to matched controls")
hdr("Outcome", "Matched change", "95% CI", "Events")
row("Log employment at +12 months", V("I35","canonical.A2_rel12.est"), CI("I35","canonical.A2_rel12.ci"), N("I35","canonical.A2_rel12.n"))
row("Hiring rate, post 12 months − pre 12 months", V("I35","canonical.A1_hire_DiD.est"), CI("I35","canonical.A1_hire_DiD.ci"), N("I35","canonical.A1_hire_DiD.n"))
row("Separation rate, post 12 months − pre 12 months", V("I35","canonical.A5_separation.est"), CI("I35","canonical.A5_separation.ci"), N("I35","canonical.A5_separation.n"))
note("Employment is measured at month +12 relative to the mean of months −12 to −1 (log difference), treated minus matched controls; "
     "rates are 12-month sums of flows over mean insured employment. [AUTHOR: keep the baseline wording aligned with code — "
     "the +12-month log-employment baseline is the pre-deal 12-month mean.]")

# ══ Table 3 ══
tab("Table 3. Hiring responses across pre-deal hiring states")
M.append("**Panel A. Primary state gradient**"); M.append("")
hdr("Quantity", "Estimate")
row("State gradient", V("I65","panelA_firm_cluster.observed") + " " + CI("I65","panelA_firm_cluster.ci95"))
row("Effect of an interquartile move", V("I65","panelF_magnitude.effect_iqr") + " " + CI("I65","panelF_magnitude.ci95_iqr"))
row("Untreated reference mean (SD)", V("I70","panelA_gradient.null_mean") + " (" + V("I70","panelA_gradient.null_sd") + ")")
row("Excess over untreated mean", V("I60","specs.winsor_5_95.excess"))
row("Standardized distance", V("I70","panelA_gradient.z",2))
row("Empirical two-sided p", V("I70","panelA_gradient.RI_p_two_sided_2min",4))
M.append("")
M.append("**Panel B. Effect of balancing the pre-deal hiring state** — preferred 5/95-winsorised specification, common 286-event sample"); M.append("")
hdr("Matching design", "Matched gradient")
row("Conventional matching, state not balanced", V("I58","panelD_decomposition.current.eff"))
row("State-balanced matching", V("I58","panelD_decomposition.balanced.eff"))
M.append("")
M.append("**Panel C. Control-path diagnostic** — unwinsorised decomposition, common 286-event sample"); M.append("")
hdr("Component slope", "Conventional", "State-balanced")
row("Treated-side slope", V("I58","panelD_decomposition.current.own"), V("I58","panelD_decomposition.balanced.own"))
row("Control-side slope with respect to treated state", V("I58","panelD_decomposition.current.control_mean"), V("I58","panelD_decomposition.balanced.control_mean"))
note("Panel A: the confidence interval clusters on treated firms (2,000 bootstrap draws); the reference distribution is the "
     "empirical distribution of 2,000 untreated pseudo-sample gradients (Figure 1(b)); the two-sided p is 2·min(upper, lower) "
     "empirical tail shares — the upper-tail p is 0.0005. Panel C is unwinsorised and is reported as a decomposition diagnostic; "
     "its component differences therefore do not numerically equal the winsorised gradients in Panel B.")

# ══ Table 4 ══
tab("Table 4. Worker-flow and employment gradients across pre-deal hiring states")
M.append("**Panel A. Worker-inflow measures**"); M.append("")
hdr("Outcome", "Gradient", "Untreated reference mean", "Empirical two-sided p", "Events")
row("Log hiring rate", V("I59","lrate.observed"), V("I59","lrate.null_mean"), V("I59","lrate.p_two",3), N("I59","lrate.n"))
row("Log worker-entry count", V("I59","lN.observed"), V("I59","lN.null_mean"), V("I59","lN.p_two",3), N("I59","lN.n"))
row("Log worker-entry count, controlling for Δ log employment", V("I59","lN_ctrlE.observed"), V("I59","lN_ctrlE.null_mean"), V("I59","lN_ctrlE.p_two",3), N("I59","lN_ctrlE.n"))
M.append("")
M.append("**Panel B. Worker flows and employment**"); M.append("")
hdr("Outcome", "Gradient", "Standardized distance", "Empirical two-sided p", "Events")
row("Log churn rate", V("I57","panelB_outcomes.churn.observed"), V("I57","panelB_outcomes.churn.z",2), V("I57","panelB_outcomes.churn.RI_p_two_sided",3), N("I57","panelB_outcomes.churn.n"))
row("Log separation rate", V("I57","panelB_outcomes.sep.observed"), V("I57","panelB_outcomes.sep.z",2), V("I57","panelB_outcomes.sep.RI_p_two_sided",4), N("I57","panelB_outcomes.sep.n"))
row("Log employment", V("I57","panelB_outcomes.emp.observed",4,signed=True), V("I57","panelB_outcomes.emp.z",2,signed=True), V("I57","panelB_outcomes.emp.RI_p_two_sided",3), N("I57","panelB_outcomes.emp.n"))
M.append("")
M.append("**Panel C. Within-event outcome contrasts**"); M.append("")
hdr("Contrast", "Estimate", "Reference mean / standardized distance", "Empirical two-sided p", "Events")
row("Hiring − employment", V("I57","panelC_paired.채용 − 고용.observed"),
    V("I57","panelC_paired.채용 − 고용.null_mean") + " / " + V("I57","panelC_paired.채용 − 고용.z",2), V("I57","panelC_paired.채용 − 고용.RI_p_two_sided",3), N("I57","panelC_paired.채용 − 고용.n"))
row("Churn − employment", V("I57","panelC_paired.churn − 고용.observed"),
    V("I57","panelC_paired.churn − 고용.null_mean",4,signed=True) + " / " + V("I57","panelC_paired.churn − 고용.z",2), V("I57","panelC_paired.churn − 고용.RI_p_two_sided",3), N("I57","panelC_paired.churn − 고용.n"))
note("Standardized distance = (observed − untreated reference mean)/reference SD, from the outcome-specific pseudo-event "
     "distribution; two-sided p = 2·min(upper, lower) empirical tail shares. Panel A holds the design fixed and varies only "
     "the outcome (denominator check); the reference distributions in Panel A are re-estimated per outcome (I59). "
     "Event counts differ across outcomes because outcome windows must be non-degenerate; the Panel C contrasts are computed "
     "within the same events.")

# ══ Table 5 ══
tab("Table 5. Pre-deal diagnostics for the hiring-state gradient")
hdr("Diagnostic", "Estimate", "95% CI", "Events")
row("Pre-deal excess gradient, non-overlapping earlier state", V("I66","panelA_pretrend_early_state.excess",4,signed=True), CI("I66","panelA_pretrend_early_state.excess_ci"), N("I66","panelA_pretrend_early_state.n"))
row("Pre-deal gradient, primary-state specification", V("I64","pre_12m.observed"), CI("I64","pre_12m.boot_ci"), N("I64","pre_12m.n"))
row("Post-deal gradient, same events", V("I64","post_12m.observed"), CI("I64","post_12m.boot_ci"), N("I64","post_12m.n"))
note("The first row avoids overlap between the state and the earlier outcome by moving the state window from months −24 to −13 "
     "to months −36 to −25; this produces a mechanically cleaner comparison but changes the moderator relative to the primary "
     "specification. The second row retains the usual state definition but shares observations between the state and the earlier "
     "outcome. The third row reports the post-investment gradient on the same events as the second row. These specifications are "
     "complementary diagnostics rather than formal tests of the identifying assumption. Relative-magnitude sensitivity "
     "calculations are reported in Online Appendix D.")

open(os.path.join(HERE, "main_exhibits.md"), "w", encoding="utf-8").write("\n".join(M) + "\n")
nmain = len(TRACE)

# ══════════ Appendix ══════════
M.clear(); M.append("# Appendix exhibits changed by the 0831 review memo"); M.append("")
tab("Table E1 (revised). Sponsor experience at the transaction date and the hiring response")
hdr("Prior sponsor deal count (before the focal transaction)", "Mean response", "95% CI", "Events")
row("First observed deal (0 prior)", V("I71","panelB_groups.first_time.mean",4,signed=True), CI("I71","panelB_groups.first_time.ci"), N("I71","panelB_groups.first_time.n"))
row("1–3 prior deals", V("I71","panelB_groups.prior_1_3.mean",4,signed=True), CI("I71","panelB_groups.prior_1_3.ci"), N("I71","panelB_groups.prior_1_3.n"))
row("4 or more prior deals", V("I71","panelB_groups.prior_ge4.mean",4,signed=True), CI("I71","panelB_groups.prior_ge4.ci"), N("I71","panelB_groups.prior_ge4.n"))
row("≥4 − first-deal contrast", V("I71","panelB_groups.ge4_minus_first.diff",4,signed=True), CI("I71","panelB_groups.ge4_minus_first.ci"), "—")
row("Repeat (≥1) − first-deal contrast", V("I71","panelB_groups.repeat_minus_first.diff",4,signed=True), CI("I71","panelB_groups.repeat_minus_first.ci"), "—")
note("Experience is the number of observed private equity deals by the same sponsor strictly before the focal transaction month, "
     "counted within the 379-event treated universe (no look-ahead). Share of first-observed deals: "
     + V("I71","panelA_dist.share_first_time",2) + "; correlation with the full-sample deal count: "
     + V("I71","panelA_dist.corr_with_fullcount",2) + ". Terciles are degenerate at zero, so fixed groups 0 / 1–3 / ≥4 are used.")

tab("Tables E2–E3 (revised inputs). Joint and held-out comparisons with the rebuilt experience variable")
hdr("Quantity", "Deal characteristics", "Pre-deal state", "Both")
row("In-sample R²", V("I71","panelC_joint.r2_deal"), V("I71","panelC_joint.r2_state"), V("I71","panelC_joint.r2_both"))
row("Permutation p", V("I71","panelC_joint.perm_p_deal",3), V("I71","panelC_joint.perm_p_state",4), "—")
row("Held-out-event R² (5-fold)", V("I71","panelD_oos.oos_r2_deal",4,signed=True), V("I71","panelD_oos.oos_r2_state",4,signed=True), V("I71","panelD_oos.oos_r2_both",4,signed=True))
row("State − deal, held-out difference", V("I71","panelD_oos.state_minus_deal",4,signed=True) + " " + CI("I71","panelD_oos.ci"), "", "")
note("Deal characteristics: buyout indicator, acquired stake, log(1 + prior sponsor deal count) — the experience variable now uses "
     "only information available at the transaction date. Sample: " + N("I71","panelC_joint.n") + " events with all deal "
     "characteristics observed. This is held-out-event fit within the observed sample, not forecasting of future transactions.")

tab("Table B5 (new). Pre-deal financial condition and hiring-response heterogeneity")
hdr("Pre-deal measure (standardised)", "Coefficient per SD", "95% CI", "Events")
for k, lab in [("cash_assets","Cash / assets"),("leverage","Leverage (liabilities / assets)"),
               ("coverage","Interest coverage (operating income / interest expense)"),("roa","Profitability (ROA)")]:
    row(lab, V("I72",f"panelA_slopes.{k}.slope",4,signed=True), CI("I72",f"panelA_slopes.{k}.ci"), N("I72",f"panelA_slopes.{k}.n"))
row("Pre-deal hiring state, same audited sample", V("I72","panelA_slopes.state_common.slope",4,signed=True), CI("I72","panelA_slopes.state_common.ci"), N("I72","panelA_slopes.state_common.n"))
row("*Memo: pre-deal hiring state, full sample*", V("I72","panelA_slopes.state_full.slope",4,signed=True), CI("I72","panelA_slopes.state_full.ci"), N("I72","panelA_slopes.state_full.n"))
note("The outcome is the event-level treated-minus-control change in the log hiring rate (unwinsorised). Financial measures are "
     "taken from the audited statement of the fiscal year before the deal year, clipped at the within-sample 1st/99th percentiles "
     "and standardised; coefficients are per one standard deviation, with treated-firm bootstrap intervals. The final row "
     "re-estimates the hiring-state slope on the same audited sample, separating the sample effect from the variable effect.")

open(os.path.join(HERE, "appendix_exhibits.md"), "w", encoding="utf-8").write("\n".join(M) + "\n")
with open(os.path.join(HERE, "REVISION_TRACE.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["exhibit", "value", "source"]); w.writeheader(); w.writerows(TRACE)
print(f"main cells traced {nmain} · appendix {len(TRACE)-nmain} · total {len(TRACE)} → main_exhibits.md, appendix_exhibits.md, REVISION_TRACE.csv")
