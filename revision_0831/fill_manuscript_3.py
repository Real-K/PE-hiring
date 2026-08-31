# -*- coding: utf-8 -*-
"""Fill part 3 — Online Appendix D–H, formatting unification, final sweep."""
import json, os, csv, re
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
    assert n == 1, f"anchor x{n} [{tag}]: {old[:90]!r}"
    TR.append({"tag": tag, "old": old[:110], "new": new[:110]}); return s.replace(old, new)
s = open(SRC, encoding="utf-8").read()

# ═══ D ═══
hd = E("I64")["honestdid"]; i11 = E("I11")["S4_quarterly_premean"]
s = R(s, "For the twelve-month implementation, we map [placeholder: exact sequence of pre- and post-investment state-gradient estimates] into the relative-magnitude restriction by treating [placeholder: exact coefficients] as the pre-p",
      f"For the twelve-month implementation, we map the pre- and post-investment state gradients estimated on the same 283 events (pre-deal gradient {hd['resolution_12m']['max_pre_abs']:.4f}; post-deal gradient {hd['resolution_12m']['post']:.4f}, SE {hd['resolution_12m']['post_se']:.4f}) into the relative-magnitude restriction by treating the absolute pre-deal gradient as the maximal observed pre-p", "D2.map")
s = R(s, "*Notes.* The twelve-month and quarterly calculations apply the same class of relative-magnitude restriction to estimates constructed at different temporal resolutions. [placeholder: insert exact coefficient sequences and implementation details for each row.]",
      ("*Notes.* The twelve-month and quarterly calculations apply the same class of relative-magnitude restriction to estimates constructed at different temporal resolutions. "
       f"Twelve-month row: post-deal gradient {hd['resolution_12m']['post']:.4f} (SE {hd['resolution_12m']['post_se']:.4f}), maximal absolute pre-deal gradient {hd['resolution_12m']['max_pre_abs']:.4f}; the confidence set for the post-deal parameter first contains zero when the permitted differential trend reaches $\\bar M={hd['resolution_12m']['Mbar']:.3f}$ times the pre-deal maximum. "
       f"Quarterly row: mean post-deal quarterly gradient {hd['resolution_quarterly']['post_mean']:.4f} (approximate SE {hd['resolution_quarterly']['post_se_approx']:.4f}), maximal absolute pre-deal quarterly gradient {hd['resolution_quarterly']['max_pre_abs']:.4f}."), "D2.note")
i65 = E("I65")
s = R(s, "*Notes.* The first row resamples [placeholder: exact matched-event/treated-cluster implementation used in the main analysis]. The second row uses [placeholder: exact control-firm resampling algorithm, including how a matched event with several controls is represented and how a control appearing in more than one event is handled]. The final specification assigns each control firm to at most one matched event and re-estimates the gradient on the 286 primary target events. [placeholder: state the rule used to choose the retained event when a control was originally used more than once.]",
      ("*Notes.* The first row resamples the 286 matched target-control sets with replacement, so each treated firm moves together with its assigned controls (2,000 draws; winsorisation cut-offs held fixed). "
       f"The second row resamples the {i65['panelC_reuse']['n_unique_controls']:,} distinct control firms with replacement; each event's control mean is recomputed using the multiplicity of its controls in the draw, events whose controls all drop out are omitted from that replication, and the gradient is re-estimated with the fixed cut-offs. "
       "The final specification assigns each control firm to at most one matched event and re-estimates the gradient on the 286 primary target events; when a control was originally used by more than one event, the event with the earliest transaction month retains it."), "D3.notes")
s = R(s, "| Each control assigned to at most one event | 0.7036 | [placeholder: interval if recomputed] |",
      "| Each control assigned to at most one event | 0.7036 | - (deterministic reassignment; interval not recomputed) |", "D3.one")
s = R(s, "the relevant pre- and post-investment sequence is [placeholder: exact coefficient sequence and outcome construction]. We apply [placeholder: exact relative-magnitude restriction and inference procedure], using the same definition of the breakdown value as in Section D.2.",
      (f"the relevant pre- and post-investment sequence is the quarterly treated-minus-control hiring-rate path (maximal pre-deal first difference {i11['pre_max_first_diff']:.4f}; twelve-month average effect {i11['theta']:.4f}, SE {i11['se']:.4f}). "
       f"We apply the relative-magnitude restriction that bounds the post-period differential trend per quarter by a multiple of the largest observed pre-period first difference (maximum tolerable drift {i11['max_tolerable_drift_per_quarter']:.4f} per quarter at the breakdown), using the same definition of the breakdown value as in Section D.2."), "D6.seq")

# ═══ E ═══
e2 = E("I73")["panelB_e2_adjusted"]; sc = e2["sponsor_concentration"]
s = R(s, "| $\\log(1+\\text{prior sponsor deal count})$, adjusted | [placeholder] | [placeholder] | [placeholder] |",
      f"| $\\log(1+\\text{{prior sponsor deal count}})$, adjusted | {f4(e2['slope_log1p_adj']['slope'], plus=True)} | {ci4(e2['slope_log1p_adj']['ci'])} | {e2['slope_log1p_adj']['n']} |", "E2.slope")
s = R(s, "| High - low prior sponsor activity, adjusted | [placeholder] | [placeholder] | [placeholder] |",
      f"| High - low prior sponsor activity, adjusted | {f4(e2['hi_lo_adj']['diff'], plus=True)} | {ci4(e2['hi_lo_adj']['ci'])} | {e2['hi_lo_adj']['n_hi']} / {e2['hi_lo_adj']['n_lo']} |", "E2.hilo")
s = R(s, "The high- and low-activity groups are defined using [placeholder: exact tercile cutoffs from the rerun].",
      "The high- and low-activity groups are defined using the tercile cut-offs of the prior-deal-count distribution, which fall at 0 and 1: the low group contains first-observed deals (no prior deal) and the high group contains sponsors with two or more prior deals.", "E2.cuts")
s = R(s, "The association between prior sponsor activity and the worker-inflow response is [placeholder: estimate-based description]. The confidence interval for the continuous measure is [placeholder], while the high-minus-low comparison is [placeholder].",
      f"The association between prior sponsor activity and the worker-inflow response is {desc(e2['slope_log1p_adj']['ci'])}. The confidence interval for the continuous measure is {ci4(e2['slope_log1p_adj']['ci'])}, while the high-minus-low comparison is {f4(e2['hi_lo_adj']['diff'], plus=True)} {ci4(e2['hi_lo_adj']['ci'])}.", "E2.prose")
i = s.find("[placeholder: report the number o")
assert i >= 0
j = s.find("]", i)
s = s[:i] + (f"Of the {sc['n_gp_total']} sponsor identifiers in the treated universe, {sc['n_gp_ge2']} are associated with two or more observed deals, accounting for {100*sc['share_events_gp_ge2']:.1f} percent of events with an identified sponsor.") + s[j+1:]
TR.append({"tag": "E3.conc", "old": "sponsor concentration ph", "new": "counts"})

# ═══ F ═══
s = R(s, "AE_i\n=\n[\\text{placeholder: exact formula used in the estimation code}].",
      "AE_i\n=\n\\frac{(A_i^{post}-A_i^{pre})/\\Delta E_i}{A_i^{pre}/E_i^{pre}},", "F1.formula")
s = R(s, "The construction uses [placeholder: exact payroll window], [placeholder: exact employment-change window], and [placeholder: exact incumbent-earnings denominator]. Observations for which $\\Delta Employment_i\\leq 0$ are handled as follows: [placeholder: exact sample or coding rule]. [placeholder: state any treatment of very small employment changes, zero denominators, winsorisation, or other restrictions.]",
      ("The construction uses total reported NPS contribution-base payroll summed over months -12 through -1 ($A^{pre}$) and months +1 through +12 ($A^{post}$), the change in window-mean insured employment between the same two windows ($\\Delta E$), and pre-window average earnings per insured worker ($A^{pre}/E^{pre}$) as the incumbent-earnings denominator. "
       "Observations with $\\Delta E_i<2$ (including all non-positive changes) are excluded, which prevents denominator explosion; the resulting ratio is truncated to $[-3,5]$. No other winsorisation is applied."), "F1.windows")
s = R(s, "The payroll-based added-employment earnings measure is defined as [placeholder: exact formula].",
      "The payroll-based added-employment earnings measure is defined as the change in window-total payroll divided by the change in window-mean insured employment, normalised by pre-window average earnings per worker (computed only when employment rises by at least two insured workers, truncated to $[-3,5]$).", "F1.note")
sv = E("I04c")["panelD_survival"]
for h, old in [(1, "| +12 months | [placeholder] | [placeholder] | [placeholder] |"),
               (2, "| +24 months | [placeholder] | [placeholder] | [placeholder] |"),
               (3, "| +36 months | [placeholder] | [placeholder] | [placeholder] |")]:
    d = sv[f"T3-T1|h{h}"]
    s = R(s, old, f"| +{12*h} months | {f4(d['diff'], plus=True)} | {ci4(d['ci'])} | {d['n_T1']+d['n_T3']} |", f"F3.h{h}")
d4 = sv["T3-T1|h4"]
s = R(s, "| +48 months | -0.1360 | [-0.2563, -0.0289] | [placeholder] |",
      f"| +48 months | {f4(d4['diff'], plus=True)} | {ci4(d4['ci'])} | {d4['n_T1']+d4['n_T3']} |", "F3.h4")
s = R(s, "*Notes.* Positive values indicate [placeholder: exact direction of the state coding in this analysis];",
      "*Notes.* Positive values indicate that low-hiring (top-tercile state) targets show a larger treated-minus-control retention contrast than high-hiring (bottom-tercile) targets;", "F3.dir")
mul = sv["multiplicity"]
s = R(s, "[placeholder: report the multiplicity-adjustment procedure and adjusted $p$-values for all four horizons.]",
      ("Adjustment: " + mul["procedure"] + "; adjusted $p$-values are "
       + ", ".join(f"{sv[f'T3-T1|h{h}']['sidak_p']:.3f} (+{12*h}m)" for h in (1, 2, 3, 4)) + "."), "F3.mult")
s = R(s, "The corresponding contrasts at the earlier horizons are [placeholder: insert estimates and intervals] and are not separately detected under the reported inference procedure.",
      ("The corresponding contrasts at the earlier horizons are "
       + ", ".join(f"{f4(sv[f'T3-T1|h{h}']['diff'], plus=True)} {ci4(sv[f'T3-T1|h{h}']['ci'])} (+{12*h} months)" for h in (1, 2, 3))
       + " and are not separately detected under the reported inference procedure."), "F3.earlier")
s = R(s, "the minimum multiplicity-adjusted $p$-value across the four horizons is 0.074. The pattern therefore does not survive the reported adjustment for the family of horizon comparisons.",
      f"the minimum multiplicity-adjusted $p$-value across the four horizons is {mul['min_sidak_p']:.3f} (two-sided bootstrap p, Šidák-adjusted). Under this adjustment the four-year contrast remains detected while the earlier horizons are not; given the retention caveats above, we still treat the pattern as an exploratory retention diagnostic.", "F3.minp")

# ═══ G ═══
a06 = E("I06")["panelA_specs"]; c06 = E("I06")["panelC_collapse_test"]["G24"]
S1, S4 = a06["G24|S1 기존처치·기존풀"], a06["G24|S4 확장처치·확장풀"]
s = R(s, "| Original treated sample and future-treated pool | [placeholder] | [placeholder] | 186 |",
      f"| Original treated sample and future-treated pool | {f4(S1['DiD'], plus=True)} | {ci4(S1['DiD_ci'])} | 186 |", "G2.a1")
s = R(s, "| Expanded treated sample and future-treated pool | [placeholder] | [placeholder] | 256 |",
      f"| Expanded treated sample and future-treated pool | {f4(S4['DiD'], plus=True)} | {ci4(S4['DiD_ci'])} | 256 |", "G2.a2")
s = R(s, "| Difference | [placeholder] | [placeholder] | - |\n\n**Panel B. Continuous change in $\\log(1+\\text{worker-entry rate})$**",
      f"| Difference | {f4(c06['DiD_diff'], plus=True)} | {ci4(c06['DiD_ci'])} | - |\n\n**Panel B. Continuous change in $\\log(1+\\text{{worker-entry rate}})$**", "G2.adiff")
s = R(s, "| Original treated sample and future-treated pool | [placeholder] | [placeholder] | [placeholder] |",
      f"| Original treated sample and future-treated pool | {f4(S1['rel'], plus=True)} | {ci4(S1['rel_ci'])} | 186 |", "G2.b1")
s = R(s, "| Expanded treated sample and future-treated pool | [placeholder] | [placeholder] | [placeholder] |",
      f"| Expanded treated sample and future-treated pool | {f4(S4['rel'], plus=True)} | {ci4(S4['rel_ci'])} | 256 |", "G2.b2")
s = R(s, "| Difference | [placeholder] | [placeholder] | - |",
      f"| Difference | {f4(S1['rel']-S4['rel'], plus=True)} | - (not separately bootstrapped) | - |", "G2.bdiff")
s = R(s, "The original and expanded samples differ according to [placeholder: exact sample-expansion rule].",
      "The original sample uses treated events linked to the NPS register by business registration number; the expanded sample adds events recovered through the reviewed firm-name matching described in Section 3.2.", "G2.rule")
G36S1, G36S4 = a06["G36|S1 기존처치·기존풀"], a06["G36|S4 확장처치·확장풀"]
s = R(s, "[placeholder: if rerun, report corresponding 18- and 36-month treatment-gap sensitivity estimates here or in a separate panel.]",
      f"With a 36-month minimum treatment gap, the corresponding $P1$ estimates are {f4(G36S1['P1'], plus=True)} {ci4(G36S1['P1_ci'])} (original, $n={G36S1['n']}$) and {f4(G36S4['P1'], plus=True)} {ci4(G36S4['P1_ci'])} (expanded, $n={G36S4['n']}$).", "G2.g36")
s = R(s, "The continuous no-entry-share comparison is [placeholder: estimate-based interpretation after rerun]. The $\\log(1+\\text{worker-entry rate})$ comparison is [placeholder: estimate-based interpretation after rerun].",
      f"The continuous no-entry-share comparison is {desc(S4['DiD_ci'])} in the expanded sample ({f4(S4['DiD'], plus=True)} {ci4(S4['DiD_ci'])}). The $\\log(1+\\text{{worker-entry rate}})$ comparison is {desc(S4['rel_ci'])} ({f4(S4['rel'], plus=True)} {ci4(S4['rel_ci'])}).", "G2.prose")
od = E("I19c")["panelB_own_dose"]
s = R(s, "The slope with transferred ownership stake is -0.000008 per percentage point [placeholder: 95% CI].",
      f"The slope with transferred ownership stake is -0.000008 per percentage point [{od['ci'][0]:.4f}, {od['ci'][1]:.4f}] ($n={od['n']}$).".replace("-0.000008", "−0.000008"), "G3.ci")
s = R(s, "| Slope with transferred ownership stake | -0.000008 per percentage point | [placeholder: 95% CI if available] |",
      f"| Slope with transferred ownership stake | −0.000008 per percentage point | [{od['ci'][0]:.4f}, {od['ci'][1]:.4f}] |".replace("-0", "−0"), "G3.row")
sg = E("I19c")["panelA_sidak"]
sub_rows = "\n".join(
    f"| {name.replace('①','(1) ').replace('②','(2) ').replace('③','(3) ').replace('④','(4) ').replace('⑤','(5) ')} | {f4(v['DiD'], plus=True)} | {v['p']:.4f} | {v['sidak_p']:.4f} |"
    for name, v in sg.items())
i = s.find("[placeholder: If the six exploratory ownership-transfer subgroups are retained")
assert i >= 0
j = s.find("]", i)
s = s[:i] + ("The exploratory subgroup estimates are reported below; none survives the Šidák adjustment across the family of subgroup comparisons.\n\n"
             "**Supplementary panel. Exploratory ownership-transfer subgroups (no-entry-share change)**\n\n"
             "| Subgroup | Estimate | Unadjusted $p$ | Šidák-adjusted $p$ |\n|---|---:|---:|---:|\n" + sub_rows + "\n\n"
             "*Notes.* Subgroups follow the shareholder-register classification: (1) majority acquisitions (stake moving from below to at least 50 percent), (2) corporate acquirers, (3) individual acquirers with a different surname, (4) individual acquirers with the same surname (family succession), (5) top tercile of transferred stake. The adjustment applies the Šidák correction across the subgroup family.") + s[j+1:]
TR.append({"tag": "G3.sub", "old": "subgroup ph", "new": "supplementary panel"})
cash = E("I21")["panelA_cash_path"]
s = R(s, "| +1 year | 0.0215 | [-0.0024, 0.0483] | [placeholder] |", f"| +1 year | 0.0215 | [−0.0024, 0.0483] | {cash['Y0+1']['n']} |", "G4.n1")
s = R(s, "| +2 years | 0.0179 | [-0.0108, 0.0494] | [placeholder] |", f"| +2 years | 0.0179 | [−0.0108, 0.0494] | {cash['Y0+2']['n']} |", "G4.n2")

# ═══ H ═══
s = R(s, "Duration categories are [placeholder: exact duration-bucket cutoffs used in the code]. The duration clock resets to [placeholder] when a positive-entry month occurs. Observations at the beginning of the NPS panel are handled as [placeholder: exact left-censoring rule], and the transaction month is [placeholder: excluded/included and exact coding].",
      ("Duration categories are $d=1$, $d=2$, $d=3$, $d=4\\text{-}5$, $d=6\\text{-}11$, and $d\\ge 12$ months since the last positive-entry month, with durations capped at 24 months. "
       "The duration clock resets to one in the month after a positive-entry month. Observations at the beginning of the NPS panel (or after gaps in observation) are excluded until six consecutive observed months have accumulated, and the transaction month itself is excluded; contributing months are event months -12 through -1 and +1 through +12."), "H1.dur")
h57 = E("I57")["panelA_hazard_triple"]["연속 S"]
s = R(s, "This specification uses [placeholder: number of events], 1,199 grouped cells, and [placeholder: number of firm-month observations].",
      f"This specification uses {h57['n_ev']} events, 1,199 grouped cells, and {h57['n_firm_months']:,} firm-month observations.", "H2.meta")
s = R(s, "| State-balanced matching, continuous state | 1.507 | [0.8710, 2.6087] | [placeholder] | 1,199 | [placeholder] |",
      f"| State-balanced matching, continuous state | 1.507 | [0.8710, 2.6087] | {h57['n_ev']} | 1,199 | {h57['n_firm_months']:,} |", "H2.row2")
s = R(s, "| State-balanced matching, state tercile | - | - | [placeholder] | - | - |",
      f"| State-balanced matching, state tercile | - | - | {h57['n_ev']} | - | - |", "H2.row3")
s = R(s, "The state variable attached to each firm-month in the hazard specification is [placeholder: state whether this is the treated target’s state assigned to all firms in the matched set, each firm’s own pre-deal state, or another exact construction].",
      "The state variable attached to each firm-month in the hazard specification is the treated target's pre-deal state, assigned to every firm in that event's matched set (treated target and controls alike).", "H2.coding")
s = R(s, "because [placeholder: exact state-tercile variable] is collinear with the event fixed effects.",
      "because the event-level state-tercile indicator, which is constant within a matched event, is collinear with the event fixed effects.", "H2.terc")
s = R(s, "The hazard-state variable is [placeholder: exact coding].",
      "The hazard-state variable is the treated target's continuous pre-deal state, common to all firm-months within a matched event.", "H2.note")

open(SRC, "w", encoding="utf-8").write(s)
with open(os.path.join(HERE, "FILL_TRACE.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["tag", "old", "new"])
    if f.tell() == 0: w.writeheader()
    w.writerows(TR)
rem = [ln for ln in s.split("\n") if "[placeholder" in ln]
print(f"PART 3 (D–H): {len(TR)} substitutions · remaining placeholder lines: {len(rem)}")
for ln in rem: print("  REMAIN:", ln.strip()[:200])
