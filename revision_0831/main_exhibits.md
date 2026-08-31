# Main-paper exhibits, rebuilt to the 0831 review memo (5 tables + 2 figures)

### Table 1. Sample construction and characteristics of the matched population

**Panel A. Sample construction**

|  | Events |
|---|---|
| Private equity investment events identified | 752 |
| &nbsp;&nbsp;unable to link to NPS records | −168 |
| &nbsp;&nbsp;insufficient pre-investment history | −120 |
| &nbsp;&nbsp;fewer than five insured employees at transaction | −75 |
| &nbsp;&nbsp;no eligible baseline control cell | −10 |
| **Baseline matched universe** | **379** |
| Average-effect sample (≥6 observed months per window, target and a control) | 367 |
| Conventional heterogeneity matching, without state balance | 301 |
| **Primary state-balanced gradient sample** | **286** |
| &nbsp;&nbsp;&nbsp;&nbsp;state window (months −24 to −13) not fully observed | −53 |
| &nbsp;&nbsp;&nbsp;&nbsp;employment below five within the state window | −1 |
| &nbsp;&nbsp;&nbsp;&nbsp;no state-balanced control cell | −17 |
| &nbsp;&nbsp;&nbsp;&nbsp;outcome windows incomplete | −22 |
| Complete transaction-characteristic sample | 180 |
| Audited financial-statement sample used in the one-year analysis | 147 |

**Panel B. Target characteristics and sample scope**

| Characteristic | Matched targets | Identified targets not entering the matched design |
|---|---|---|
| Median insured employment | 79.8 | 135.6 |
| Mean insured employment | 218.2 | — |
| Median deal year | 2021 | — |
| Two-digit industries represented | 44 | — |

**Panel C. Covariate and state balance in the primary 286-event sample**

| Variable | Treated | State-balanced controls | Normalised difference |
|---|---|---|---|
| Log insured employment | 4.442 | 4.380 | +0.0538 |
| Pre-deal employment growth | +0.095 | +0.080 | +0.0651 |
| Firm age (years) | 16.524 | 18.099 | −0.1676 |
| Pre-deal hiring state S | −0.352 | −0.343 | −0.0390 |
| Prior hiring rate (12 months) | 0.436 | 0.415 | +0.0624 |
| Prior separation rate (12 months) | 0.352 | 0.350 | +0.0075 |

*Notes.* Panel A: the 367-event average-effect sample and the 286-event primary gradient sample are parallel branches of the 379-event baseline universe, not successive stages; the indented rows decompose 379 → 286 (I63 attrition, code-verified labels). Panel C: balance is computed on the primary 286-event sample against its state-balanced controls (covariates as in the baseline design; normalised difference = (m̄_T − m̄_C)/√((s²_T + s²_C)/2)). The baseline-design and unmatched-pool comparisons move to the appendix.

### Table 2. Average post-investment changes relative to matched controls

| Outcome | Matched change | 95% CI | Events |
|---|---|---|---|
| Log employment at +12 months | 0.0878 | [0.0462, 0.1300] | 367 |
| Hiring rate, post 12 months − pre 12 months | 0.0485 | [0.0163, 0.0814] | 367 |
| Separation rate, post 12 months − pre 12 months | 0.0007 | [−0.0353, 0.0398] | 367 |

*Notes.* Employment is measured at month +12 relative to the mean of months −12 to −1 (log difference), treated minus matched controls; rates are 12-month sums of flows over mean insured employment. [AUTHOR: keep the baseline wording aligned with code — the +12-month log-employment baseline is the pre-deal 12-month mean.]

### Table 3. Hiring responses across pre-deal hiring states

**Panel A. Primary state gradient**

| Quantity | Estimate |
|---|---|
| State gradient | 0.7101 [0.3187, 1.1254] |
| Effect of an interquartile move | 0.2005 [0.0900, 0.3177] |
| Untreated reference mean (SD) | 0.1010 (0.1538) |
| Excess over untreated mean | 0.6091 |
| Standardized distance | 3.96 |
| Empirical two-sided p | 0.0010 |

**Panel B. Effect of balancing the pre-deal hiring state** — preferred 5/95-winsorised specification, common 286-event sample

| Matching design | Matched gradient |
|---|---|
| Conventional matching, state not balanced | 0.4698 |
| State-balanced matching | 0.7101 |

**Panel C. Control-path diagnostic** — unwinsorised decomposition, common 286-event sample

| Component slope | Conventional | State-balanced |
|---|---|---|
| Treated-side slope | 0.8425 | 0.8425 |
| Control-side slope with respect to treated state | 0.2950 | 0.0056 |

*Notes.* Panel A: the confidence interval clusters on treated firms (2,000 bootstrap draws); the reference distribution is the empirical distribution of 2,000 untreated pseudo-sample gradients (Figure 1(b)); the two-sided p is 2·min(upper, lower) empirical tail shares — the upper-tail p is 0.0005. Panel C is unwinsorised and is reported as a decomposition diagnostic; its component differences therefore do not numerically equal the winsorised gradients in Panel B.

### Table 4. Worker-flow and employment gradients across pre-deal hiring states

**Panel A. Worker-inflow measures**

| Outcome | Gradient | Untreated reference mean | Empirical two-sided p | Events |
|---|---|---|---|---|
| Log hiring rate | 0.7101 | 0.1012 | 0.001 | 286 |
| Log worker-entry count | 0.6315 | 0.1795 | 0.014 | 286 |
| Log worker-entry count, controlling for Δ log employment | 0.6957 | 0.0363 | 0.002 | 286 |

**Panel B. Worker flows and employment**

| Outcome | Gradient | Standardized distance | Empirical two-sided p | Events |
|---|---|---|---|---|
| Log churn rate | 0.3816 | 3.08 | 0.002 | 288 |
| Log separation rate | 0.1788 | 1.17 | 0.2349 | 281 |
| Log employment | −0.0580 | −2.60 | 0.007 | 289 |

**Panel C. Within-event outcome contrasts**

| Contrast | Estimate | Reference mean / standardized distance | Empirical two-sided p | Events |
|---|---|---|---|---|
| Hiring − employment | 0.7536 | 0.0232 / 4.56 | 0.001 | 286 |
| Churn − employment | 0.4539 | −0.0750 / 4.19 | 0.001 | 288 |

*Notes.* Standardized distance = (observed − untreated reference mean)/reference SD, from the outcome-specific pseudo-event distribution; two-sided p = 2·min(upper, lower) empirical tail shares. Panel A holds the design fixed and varies only the outcome (denominator check); the reference distributions in Panel A are re-estimated per outcome (I59). Event counts differ across outcomes because outcome windows must be non-degenerate; the Panel C contrasts are computed within the same events.

### Table 5. Pre-deal diagnostics for the hiring-state gradient

| Diagnostic | Estimate | 95% CI | Events |
|---|---|---|---|
| Pre-deal excess gradient, non-overlapping earlier state | −0.1770 | [−0.4394, 0.0854] | 250 |
| Pre-deal gradient, primary-state specification | 0.1068 | [−0.1955, 0.4351] | 283 |
| Post-deal gradient, same events | 0.7250 | [0.3259, 1.1081] | 283 |

*Notes.* The first row avoids overlap between the state and the earlier outcome by moving the state window from months −24 to −13 to months −36 to −25; this produces a mechanically cleaner comparison but changes the moderator relative to the primary specification. The second row retains the usual state definition but shares observations between the state and the earlier outcome. The third row reports the post-investment gradient on the same events as the second row. These specifications are complementary diagnostics rather than formal tests of the identifying assumption. Relative-magnitude sensitivity calculations are reported in Online Appendix D.

