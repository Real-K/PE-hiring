# -*- coding: utf-8 -*-
"""Fill the 0831_2200 manuscript, part B — Appendices C–H + final sweep."""
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
def ci4(v): return f"[{v[0]:.4f}, {v[1]:.4f}]".replace("-", "−")
def desc(ci): return ("positive but not detected" if ci[0] <= 0 <= ci[1] and (ci[0]+ci[1]) > 0
                      else "negative but not detected" if ci[0] <= 0 <= ci[1]
                      else "detected as positive" if ci[0] > 0 else "detected as negative")
TR = []
def R(s, old, new, tag):
    n = s.count(old)
    assert n == 1, f"anchor x{n} [{tag}]: {old[:80]!r}"
    TR.append({"tag": tag, "old": old[:100], "new": new[:100]}); return s.replace(old, new)
s = open(SRC, encoding="utf-8").read()

# ═══ C ═══
s = R(s, "discrepancies can arise because [placeholder: exact NPS stock and flow reporting convention and timing]",
      "discrepancies can arise because the stock is the month-end count of insured workers while entries and exits are the month's reported acquisition and loss records, so late or corrected filings can move the two apart", "C1.arise")
s = R(s, "{[\\text{placeholder: exact employment denominator used in the code}]}",
      "{E_{i,t-1}}", "C1.rden")
s = R(s, "Relative discrepancies divide $|d_{it}|$ by [placeholder: exact denominator]. Employment is measured according to [placeholder: exact NPS stock-timing convention]. The final three rows report [placeholder: exact statistic-mean or median] relative discrepancies over the stated periods for treated firms.",
      "Relative discrepancies divide $|d_{it}|$ by the prior-month insured-employment stock $E_{i,t-1}$ (months with $E_{i,t-1}=0$ are excluded). Employment is the month-end insured-employment stock in the NPS register. The final three rows report mean relative discrepancies over the stated periods for treated firms.", "C1.note")
s = R(s, "[\\text{placeholder: exact code definition}],",
      "\\max\\{0,\\,(E_{it}-E_{i,t-1})+Exit_{it}\\},", "C2.formula")
s = R(s, "with negative implied flows treated as [placeholder], missing or non-consecutive months treated as [placeholder], and the transaction month treated as [placeholder]. Pre- and post-investment reconstructed flows are aggregated using [placeholder: exact window and denominator rule].",
      "with negative implied flows set to zero, missing or non-consecutive months invalidating the window, and the transaction month excluded because the windows are months $-12$ through $-1$ and $+1$ through $+12$. Pre- and post-investment reconstructed flows are summed within each window and divided by window-mean insured employment, entering the same gradient pipeline as the primary measure.", "C2.rules")
i48c = E("I48")["panelC_exclusions"]; sc48 = E("I48")["panelD_site_change"]["excluded"]; imp = E("I60")["specs"]["implied_hires"]
s = R(s, "| Exclude relative discrepancy $>10\\%$ | [placeholder] | 0.312 | [placeholder] | [placeholder] |",
      f"| Exclude relative discrepancy $>10\\%$ | {i48c['exclude_rel_gt_10pct']['n']} | {f4(i48c['exclude_rel_gt_10pct']['slope_adj'])} | {ci4(i48c['exclude_rel_gt_10pct']['ci'])} | - |", "C2.r2")
s = R(s, "| Exclude relative discrepancy $>5\\%$ | [placeholder] | 0.544 | [placeholder] | [placeholder] |",
      f"| Exclude relative discrepancy $>5\\%$ | {i48c['exclude_rel_gt_5pct']['n']} | {f4(i48c['exclude_rel_gt_5pct']['slope_adj'])} | {ci4(i48c['exclude_rel_gt_5pct']['ci'])} | - |", "C2.r3")
s = R(s, "| Exclude total turnover $>50\\%$ of employment | [placeholder] | 0.488 | [0.102, 0.850] | [placeholder] |",
      f"| Exclude total turnover $>50\\%$ of employment | {i48c['exclude_churn_gt_50pct']['n']} | {f4(i48c['exclude_churn_gt_50pct']['slope_adj'])} | {ci4(i48c['exclude_churn_gt_50pct']['ci'])} | - |", "C2.r4")
s = R(s, "| Exclude treated firms with workplace-count changes | [placeholder] | 0.557 | [0.160, 0.930] | [placeholder] |",
      f"| Exclude treated firms with workplace-count changes | {sc48['n']} | {f4(sc48['slope_adj'])} | {ci4(sc48['ci'])} | - |", "C2.r5")
s = R(s, "| Reconstructed worker inflows | [placeholder] | 0.365 | [placeholder] | [placeholder] |",
      f"| Reconstructed worker inflows | {imp['n']} | {f4(imp['observed'])} | - | {imp['RI_p_two_centered']:.4f} |", "C2.r6")
s = R(s, "exceed 50 percent of [placeholder: exact denominator]. The workplace-count specification removes treated firms whose number of registered NPS workplaces changes over [placeholder: exact event window].",
      "exceed 50 percent of the same month's insured-employment stock. The workplace-count specification removes treated firms whose number of registered NPS workplaces takes more than one value at any point in the observed panel (not restricted to an event window).", "C2.notes")
s = R(s, "Event counts and intervals for the discrepancy and reconstructed-flow specifications should be populated from the final rerun.",
      "The discrepancy and workplace rows use the conventional matched sample with regression adjustment and report bootstrap intervals; the reconstructed-flow row uses the state-balanced design with its own untreated reference distribution, so its inference is the empirical probability rather than a bootstrap interval.", "C2.note2")
s = R(s, "The reconstructed-flow gradient is 0.365 [placeholder: 95% CI].",
      f"The reconstructed-flow gradient is 0.365 (two-sided empirical $p$ = {imp['RI_p_two_centered']:.4f} against its own untreated reference distribution).", "C2.prose")
pc57 = E("I57")["panelC_paired"]["채용 − 이직"]
s = R(s, "| Worker-entry gradient - separation gradient | 0.5746 | 0.043 | [placeholder] |",
      f"| Worker-entry gradient - separation gradient | {f4(pc57['observed'])} | {pc57['RI_p_two_centered']:.4f} | {pc57['n']} |", "C4.row")
s = R(s, "which uses [placeholder: exact primary baseline and post-period construction]",
      "which uses the change in the log of window-mean insured employment between months $-12$ through $-1$ and months $+1$ through $+12$", "C4.note")

# ═══ D ═══
hd = E("I64")["honestdid"]
s = R(s, "we map [placeholder: exact coefficient sequence] into the relative-magnitude restriction. The pre-period differential sequence is [placeholder: exact coefficients and normalisation], and the post-period estimand is [placeholder: exact coefficient or linear combination]. Confidence sets are constructed using [placeholder: exact HonestDiD/Rambachan-Roth procedure, covariance matrix, confidence level, and any restrictions beyond relative magnitude].",
      (f"we map the pre- and post-investment state gradients estimated on the same 283 events into the relative-magnitude restriction. The pre-period differential sequence is the twelve-month pre-deal gradient ({hd['resolution_12m']['max_pre_abs']:.4f} in absolute value, unnormalised), and the post-period estimand is the single twelve-month post-deal gradient ({hd['resolution_12m']['post']:.4f}, SE {hd['resolution_12m']['post_se']:.4f}). "
       "Confidence sets use a normal approximation with the event-bootstrap standard error at the 95 percent level and impose only the relative-magnitude restriction: the breakdown value is the largest $\\bar M$ at which the lower 95 percent bound of the post-period estimate, widened by $\\bar M$ times the maximum absolute pre-period gradient, remains above zero."), "D2.impl")
s = R(s, "[placeholder: provide the exact event-time coefficient sequence and implementation details for each row.]",
      (f"Twelve-month row: pre-period maximum {hd['resolution_12m']['max_pre_abs']:.4f}, post-period estimate {hd['resolution_12m']['post']:.4f} (SE {hd['resolution_12m']['post_se']:.4f}). "
       f"Quarterly row: mean post-deal quarterly gradient {hd['resolution_quarterly']['post_mean']:.4f} (approximate SE {hd['resolution_quarterly']['post_se_approx']:.4f}), pre-period maximum {hd['resolution_quarterly']['max_pre_abs']:.4f}."), "D2.note")
s = R(s, "when an exact close month is unavailable, [placeholder: confirm the rule assigning timing within the vintage year]",
      "when an exact close month is unavailable, the mid-year of the fund's vintage year is used as the closing month", "D3.vintage")
i65 = E("I65")
s = R(s, "| Each control assigned to at most one event | 0.7036 | [placeholder] |",
      "| Each control assigned to at most one event | 0.7036 | - (deterministic reassignment; interval not recomputed) |", "D3.one")
s = R(s, "The primary bootstrap resamples [placeholder: exact treated-event and matched-set implementation]. The alternative control-based procedure resamples [placeholder: exact algorithm, including how events with several controls and controls reused across events are represented]. In the final row, controls appearing in more than one original event are retained for [placeholder: exact assignment rule] and removed from their other matched sets.",
      ("The primary bootstrap resamples the 286 matched target-control sets with replacement, so each treated event moves together with its assigned controls (2,000 draws; winsorisation cut-offs held fixed). "
       f"The alternative control-based procedure resamples the {i65['panelC_reuse']['n_unique_controls']:,} distinct control firms with replacement; each event's control mean is recomputed using the multiplicity of its controls in the draw, and events whose controls all drop out are omitted from that replication. "
       "In the final row, controls appearing in more than one original event are retained for the event with the earliest transaction month and removed from their other matched sets."), "D3.note")
i11 = E("I11")["S4_quarterly_premean"]
s = R(s, "the event-time outcome sequence is [placeholder: exact construction]. We implement the Rambachan-Roth relative-magnitude restriction using [placeholder: exact pre-period coefficients, post-period estimand, covariance estimator, and confidence-set procedure].",
      (f"the event-time outcome sequence is the quarterly treated-minus-control hiring-rate path (pre-period maximum first difference {i11['pre_max_first_diff']:.4f}; twelve-month average effect {i11['theta']:.4f}, SE {i11['se']:.4f}). "
       "We implement the Rambachan-Roth relative-magnitude restriction by bounding the post-period differential trend per quarter by a multiple of the largest observed pre-period first difference, with a normal-approximation confidence set at the 95 percent level based on the event-bootstrap standard error."), "D6.seq")

# ═══ E ═══
s = R(s, "The permutation probabilities in Panel A are based on [placeholder: exact number and implementation of relabellings]",
      "The permutation probabilities in Panel A are based on 2,000 random permutations of the transaction-characteristic vectors across events, holding the state column fixed", "E2.perm")
lu = g("I73", "panelB_e2_adjusted.sponsor_concentration.loo_universe")
s = R(s, "The baseline leave-one-out coefficient is -0.2675 across 189 event observations. [placeholder: report the number of distinct repeat sponsors represented among these 189 event observations.]",
      f"The baseline leave-one-out coefficient is -0.2675 across 189 event observations, which represent {lu['n_repeat_gp_301sample']} distinct repeat sponsors.", "E3.rep")
s = R(s, "[placeholder: report the number of distinct sponsor identifiers represented in this repeat-deal subset.]",
      f"The repeat-deal subset spans {lu['n_repeat_gp_301sample']} distinct sponsor identifiers.", "E3.rep2")
s = R(s, "Panel B is estimated on [placeholder: exact event and sponsor sample used for the fixed-effect variance-share calculation]. Its permutation benchmark is generated by [placeholder: exact permutation procedure and whether sponsor-group sizes are held fixed].",
      "Panel B is estimated on the 213 events with an attached sponsor identifier and at least one same-sponsor peer (56 sponsors). Its permutation benchmark is generated by 2,000 random reassignments of sponsor labels across events, holding the sponsor group sizes fixed.", "E3.panelB")

# ═══ F ═══
s = R(s, "[\\text{placeholder: exact formula used in the estimation code}].",
      "\\frac{(A_i^{post}-A_i^{pre})/\\Delta E_i}{A_i^{pre}/E_i^{pre}}.", "F1.formula")
s = R(s, "The construction uses [placeholder: exact payroll window], [placeholder: exact employment-change window], and [placeholder: exact incumbent-earnings normalisation]. Observations with non-positive or very small employment changes are treated according to [placeholder: exact coding and sample restriction].",
      ("The construction uses total reported NPS contribution-base payroll summed over months $-12$ through $-1$ ($A^{pre}$) and months $+1$ through $+12$ ($A^{post}$), the change in window-mean insured employment between the same windows ($\\Delta E$), and pre-window average earnings per insured worker ($A^{pre}/E^{pre}$) as the incumbent-earnings normalisation. "
       "Observations with $\\Delta E_i<2$, including all non-positive changes, are excluded, and the resulting ratio is truncated to $[-3,5]$."), "F1.windows")
s = R(s, "The payroll-based added-employment measure is defined as [placeholder: exact formula].",
      "The payroll-based added-employment measure is the change in window-total payroll divided by the change in window-mean insured employment, normalised by pre-window average earnings per worker (computed only when employment rises by at least two insured workers; truncated to $[-3,5]$).", "F1.note")
sv = E("I04c")["panelD_survival"]
for h, old in [(1, "| +12 months | [placeholder] | [placeholder] | [placeholder] | [placeholder] |"),
               (2, "| +24 months | [placeholder] | [placeholder] | [placeholder] | [placeholder] |"),
               (3, "| +36 months | [placeholder] | [placeholder] | [placeholder] | [placeholder] |")]:
    dd = sv[f"T3-T1|h{h}"]
    s = R(s, old, f"| +{12*h} months | {f4(dd['diff'], plus=True)} | {ci4(dd['ci'])} | {dd['sidak_p']:.4f} | {dd['n_T1']+dd['n_T3']} |", f"F3.h{h}")
d4 = sv["T3-T1|h4"]
s = R(s, "| +48 months | -0.1360 | [-0.2563, -0.0289] | **0.0394** | [placeholder] |",
      f"| +48 months | {f4(d4['diff'], plus=True)} | {ci4(d4['ci'])} | **{d4['sidak_p']:.4f}** | {d4['n_T1']+d4['n_T3']} |", "F3.h4")
s = R(s, "The state is oriented so that [placeholder: state the exact scaling or group contrast used in this panel-presence analysis].",
      "The contrast compares top-tercile (lowest pre-deal hiring) with bottom-tercile targets in their treated-minus-control continued-observation rates at each horizon.", "F3.orient")
s = R(s, "account for the four horizon comparisons using [placeholder: exact multiplicity-adjustment procedure]",
      "account for the four horizon comparisons using the Šidák correction applied to two-sided bootstrap probabilities", "F3.mult")
s = R(s, "The earlier-horizon contrasts are [placeholder: report the +12-, +24-, and +36-month estimates, confidence intervals, adjusted $p$-values, and event counts].",
      ("The earlier-horizon contrasts are "
       + ", ".join(f"{f4(sv[f'T3-T1|h{h}']['diff'], plus=True)} {ci4(sv[f'T3-T1|h{h}']['ci'])} (adjusted $p$ = {sv[f'T3-T1|h{h}']['sidak_p']:.3f}, $n={sv[f'T3-T1|h{h}']['n_T1']+sv[f'T3-T1|h{h}']['n_T3']}$) at +{12*h} months" for h in (1, 2, 3)) + "."), "F3.earlier")

# ═══ G ═══
a06 = E("I06")["panelA_specs"]; c06 = E("I06")["panelC_collapse_test"]["G24"]
S1, S4 = a06["G24|S1 기존처치·기존풀"], a06["G24|S4 확장처치·확장풀"]
s = R(s, "| Original treated sample and future-treated controls | [placeholder] | [placeholder] | 186 |\n| Expanded treated sample and future-treated controls | [placeholder] | [placeholder] | 256 |\n| Difference | [placeholder] | [placeholder] | - |",
      f"| Original treated sample and future-treated controls | {f4(S1['DiD'], plus=True)} | {ci4(S1['DiD_ci'])} | 186 |\n| Expanded treated sample and future-treated controls | {f4(S4['DiD'], plus=True)} | {ci4(S4['DiD_ci'])} | 256 |\n| Difference | {f4(c06['DiD_diff'], plus=True)} | {ci4(c06['DiD_ci'])} | - |", "G2.panelA")
s = R(s, "| Original treated sample and future-treated controls | [placeholder] | [placeholder] | [placeholder] |\n| Expanded treated sample and future-treated controls | [placeholder] | [placeholder] | [placeholder] |\n| Difference | [placeholder] | [placeholder] | - |",
      f"| Original treated sample and future-treated controls | {f4(S1['rel'], plus=True)} | {ci4(S1['rel_ci'])} | 186 |\n| Expanded treated sample and future-treated controls | {f4(S4['rel'], plus=True)} | {ci4(S4['rel_ci'])} | 256 |\n| Difference | {f4(S1['rel']-S4['rel'], plus=True)} | - (not separately bootstrapped) | - |", "G2.panelB")
s = R(s, "The original and expanded samples differ according to [placeholder: exact expansion rule].",
      "The original sample uses treated events linked to the NPS register by business registration number; the expanded sample adds events recovered through the reviewed firm-name matching described in Section 3.2.", "G2.rule")
i74 = E("I74")["panelA_specs_G18"]; G18S1, G18S4 = i74["G18|S1 기존처치·기존풀"], i74["G18|S4 확장처치·확장풀"]
G36S1, G36S4 = a06["G36|S1 기존처치·기존풀"], a06["G36|S4 확장처치·확장풀"]
s = R(s, "[placeholder: report the 18-, 24-, and 36-month minimum-future-treatment-gap sensitivity analyses if retained.]",
      (f"Gap sensitivity ($P1$, expanded sample): {f4(G18S4['P1'], plus=True)} {ci4(G18S4['P1_ci'])} with an 18-month gap ($n={G18S4['n']}$), {f4(S4['P1'], plus=True)} {ci4(S4['P1_ci'])} with the 24-month gap ($n=256$), and {f4(G36S4['P1'], plus=True)} {ci4(G36S4['P1_ci'])} with a 36-month gap ($n={G36S4['n']}$)."), "G2.gaps")
s = R(s, "the corresponding comparison is [placeholder: estimate, confidence interval, and interpretation]. For $\\log(1+\\text{worker-entry rate})$, the estimate is [placeholder: estimate, confidence interval, and interpretation].",
      (f"the corresponding comparison is {desc(S4['DiD_ci'])} in the expanded sample, at {f4(S4['DiD'], plus=True)} {ci4(S4['DiD_ci'])}. "
       f"For $\\log(1+\\text{{worker-entry rate}})$, the estimate is {f4(S4['rel'], plus=True)} {ci4(S4['rel_ci'])}, likewise {desc(S4['rel_ci'])}."), "G2.prose")
od = E("I19c")["panelB_own_dose"]
s = R(s, "| Slope with transferred ownership stake | -0.000008 per percentage point | [placeholder] |",
      f"| Slope with transferred ownership stake | −0.000008 per percentage point | {ci4(od['ci'])} |", "G3.row")
s = R(s, "The transferred-stake slope uses [placeholder: exact transferred-ownership definition and eligible sample].",
      f"The transferred-stake slope uses the transferred common-share percentage recorded in the shareholder register, pooled across the {od['n']} non-private-equity ownership-change events.", "G3.def")
s = R(s, "close to zero at $-0.000008$ per percentage point [placeholder: 95% CI]",
      f"close to zero at $-0.000008$ per percentage point {ci4(od['ci'])} ($n={od['n']}$)", "G3.prose")
sg = E("I19c")["panelA_sidak"]
sub_rows = "\n".join(
    f"| {name.replace('①','(1) ').replace('②','(2) ').replace('③','(3) ').replace('④','(4) ').replace('⑤','(5) ')} | {f4(v['DiD'], plus=True)} | {v['p']:.4f} | {v['sidak_p']:.4f} |"
    for name, v in sg.items())
i = s.find("[placeholder: If the six exploratory ownership-transfer subgroup analyses are retained")
assert i >= 0
j = s.find("]", i)
s = s[:i] + ("The exploratory subgroup estimates are reported below; none survives the Šidák adjustment across the subgroup family.\n\n"
             "**Supplementary panel. Exploratory ownership-transfer subgroups (no-entry-share change)**\n\n"
             "| Subgroup | Estimate | Unadjusted $p$ | Šidák-adjusted $p$ |\n|---|---:|---:|---:|\n" + sub_rows + "\n\n"
             "*Notes.* Subgroups follow the shareholder-register classification: (1) majority acquisitions (stake moving from below to at least 50 percent), (2) corporate acquirers, (3) individual acquirers with a different surname, (4) individual acquirers with the same surname, (5) top tercile of transferred stake. The adjustment applies the Šidák correction across the subgroup family.") + s[j+1:]
TR.append({"tag": "G3.sub", "old": "subgroup ph", "new": "supplementary panel"})
cash = E("I21")["panelA_cash_path"]
s = R(s, "| +1 year | 0.0215 | [-0.0024, 0.0483] | [placeholder] |", f"| +1 year | 0.0215 | [−0.0024, 0.0483] | {cash['Y0+1']['n']} |", "G4.n1")
s = R(s, "| +2 years | 0.0179 | [-0.0108, 0.0494] | [placeholder] |", f"| +2 years | 0.0179 | [−0.0108, 0.0494] | {cash['Y0+2']['n']} |", "G4.n2")
s = R(s, "Cash-change terciles use [placeholder: exact post-deal horizon and construction].",
      "Cash-change terciles use the treated-minus-control change in cash over assets between the fiscal year before the deal and the deal year, with tercile cut-offs computed within the treated firms that have audited statements.", "G4.terc")

# ═══ H ═══
s = R(s, "The duration categories are [placeholder: exact duration-bucket cutoffs]. A positive-entry month resets the duration clock according to [placeholder: exact reset rule]. At the beginning of the NPS panel, duration is treated according to [placeholder: exact left-censoring convention]. The transaction month is [placeholder: exact inclusion/exclusion and post indicator rule].",
      ("The duration categories are $d=1$, $2$, $3$, $4\\text{-}5$, $6\\text{-}11$, and $\\ge 12$ months, with durations capped at 24. "
       "A positive-entry month resets the duration clock to one in the following month. At the beginning of the NPS panel, and after any gap in observation, months are excluded until six consecutive observed months have accumulated. "
       "The transaction month is excluded: contributing months are event months $-12$ through $-1$ and $+1$ through $+12$, with the post indicator equal to one for the latter."), "H1.dur")
s = R(s, "enters through fixed effects for [placeholder: exact duration categories]",
      "enters through fixed effects for the categories $d=1$, $2$, $3$, $4\\text{-}5$, $6\\text{-}11$, and $\\ge 12$ months", "H1.cat")
s = R(s, "The state variable used in the hazard analysis is [placeholder: state whether the target’s state is assigned to all observations within its matched event, whether each firm carries its own state, and the exact scaling].",
      "The state variable used in the hazard analysis is the treated target's continuous pre-deal state, assigned to every firm-month within that event's matched set (controls carry the target's state, not their own), entered without rescaling.", "H2.assign")
h57 = E("I57")["panelA_hazard_triple"]["연속 S"]
s = R(s, "The state-balanced continuous specification uses 1,199 grouped cells. [placeholder: report its event and firm-month counts if retained in the final table.]",
      f"The state-balanced continuous specification uses {h57['n_ev']} events, 1,199 grouped cells, and {h57['n_firm_months']:,} firm-month observations.", "H2.meta")
s = R(s, "The state variable used in the continuous interaction is [placeholder: exact definition and scaling].",
      "The state variable used in the continuous interaction is the treated target's pre-deal state $S_i=-\\log(1+N_i^{state}/E_i^{state})$ over months $-24$ through $-13$, unscaled and common to all firm-months within the matched event.", "H2.def")
open(SRC, "w", encoding="utf-8").write(s)
with open(os.path.join(HERE, "FILL_TRACE_2200.csv"), "a", encoding="utf-8", newline="") as f:
    csv.DictWriter(f, fieldnames=["tag", "old", "new"]).writerows(TR)
rem = [ln for ln in s.split("\n") if "[placeholder" in ln and not ln.strip().startswith(">")]
print(f"2200-B: {len(TR)} substitutions · remaining non-echo lines: {len(rem)}")
for ln in rem: print("  REMAIN:", ln.strip()[:220])
