# Online Appendix. Private Equity and State-Dependent Hiring

Unless otherwise stated, confidence intervals follow the procedures described in the main text. Placebo tests for specifications of the hiring-state gradient use the upper tail corresponding to the directional prediction; tests of other outcomes are two-sided. An equivalence statement is made only when the entire confidence interval lies within the stated practical-equivalence range.

### Appendix A. Hiring-volume benchmark and monthly measures

The main text shows that private equity targets hire in a broader set of months after investment. Because the probability of observing positive hiring in a month rises mechanically with the total number of workers hired, this appendix compares the observed monthly pattern with a benchmark that preserves realised hiring volume. It also reports the extensive- and intensive-margin decomposition omitted from Table 2.

### A.1 Construction of the volume benchmark

For each firm-window, let  denote the realised number of hires and let  denote month ’s share of total employment exposure over the window. We hold , the observed months, and the employment weights fixed and allocate the  hires across months according to the probabilities .

Under this allocation, the expected number of months with no hiring is

With equal monthly weights, the corresponding expression is

For measures without a closed-form expectation—the longest spell without hiring, the Herfindahl index of hires across months, and the share of hires occurring in the two busiest months—we simulate the same multinomial allocation 60 times for each firm-window. The excess is the observed measure minus its volume-preserving benchmark. Changes in the excess therefore capture monthly allocation patterns beyond those implied by the change in realised hiring volume.

The benchmark is intentionally narrow. It preserves realised hiring volume and monthly employment exposure but does not reproduce firm-specific seasonality, month-specific demand conditions, or a firm’s pre-existing tendency to cluster hiring. The exercise therefore asks whether the observed monthly changes contain a component comparable in magnitude to the extensive-margin movement itself after accounting for volume; it is not a structural model of hiring timing.

Before the transaction, treated firms average 91.9 hires per twelve-month window. They have 3.23 months without hiring, compared with 2.58 under the volume benchmark, and a longest no-hire spell of 1.97 months, compared with 1.53. The Herfindahl index of monthly hires is 0.203 in the data and 0.163 under the benchmark; the corresponding shares of hires in the two busiest months are 0.468 and 0.378. Hiring is therefore more clustered before the transaction than a simple volume-preserving random allocation would imply.

### A.2 Monthly hiring patterns relative to realised volume

### Table A1. Monthly hiring measures and the volume benchmark

### Panel A. Twelve-month window

[TABLE #1]
| Measure | Observed change | Volume-only benchmark | Excess | 95% CI for excess | Equivalence range | Equivalent? |
|---|---|---|---|---|---|---|
| Share of no-hire months | −0.0466 | −0.0518 | +0.0052 | [−0.0082, +0.0189] | ±0.046 | Yes |
| Share of no-hire months, employment-weighted benchmark | −0.0466 | −0.0508 | +0.0042 | [−0.0088, +0.0180] | ±0.046 | Yes |
| Number of no-hire months | −0.5594 | −0.6182 | +0.0587 | [−0.1097, +0.2086] | ±0.55 | Yes |
| Longest no-hire spell, months | −0.3566 | −0.3688 | +0.0122 | [−0.1330, +0.1608] | ±0.36 | Yes |
| Herfindahl index of hires across months | −0.0248 | −0.0309 | +0.0061 | [−0.0064, +0.0190] | ±0.025 | Yes |
| Share of hires in the two busiest months | −0.0249 | −0.0335 | +0.0086 | [−0.0082, +0.0250] | ±0.025 | No |

### Panel B. Thirty-six-month window

[TABLE #2]
| Measure | Observed change | 95% CI | Excess | 95% CI for excess | Equivalence range |
|---|---|---|---|---|---|
| Share of no-hire months | −0.055 | [−0.086, −0.025] | +0.0088 | [−0.0058, +0.0220] | ±0.046 |
| Longest no-hire spell, months | −0.756 | [−1.335, −0.161] | +0.297 | [−0.117, +0.727] | ±1.0 |

Notes. The observed change is the treated-minus-control change in the corresponding monthly measure. The volume-only benchmark holds each firm-window’s realised number of hires fixed and reallocates those hires across the same months in proportion to monthly employment. The excess is the observed measure minus this benchmark. Equivalence is recorded only when the entire confidence interval for the excess lies inside the stated range. The thirty-six-month results use 180 events.

The volume benchmark accounts for most of the observed movement in the twelve-month measures. For the main no-hire-share outcome, the observed decline is 0.0466 while the benchmark predicts a decline of 0.0518. The excess is only 0.0052 [−0.0082, 0.0189], with its full interval inside the ±0.046 equivalence range used in the main text. Longest no-hire spells and monthly hiring concentration yield similar comparisons.

The one exception is the share of hires occurring in the two busiest months. Its excess is 0.0086 [−0.0082, 0.0250]. The upper endpoint coincides with the ±0.025 equivalence boundary to the reported precision, so we do not classify this measure as establishing equivalence. This knife-edge result does not change the broader pattern, but it prevents a blanket statement that every monthly allocation measure falls strictly inside its equivalence range.

Over thirty-six months, the same conclusion is visible in the two measures for which the longer window is available. The observed no-hire share falls by 0.055, while the excess over the volume benchmark is 0.0088 [−0.0058, 0.0220]. The observed longest spell falls by 0.756 months and the excess is 0.297 [−0.117, 0.727]. Both excess intervals lie inside their stated equivalence ranges.

Total hires increase by 8.5 workers per twelve-month window in the corresponding level comparison, although the estimate is imprecise [−17.3, 47.5]. We therefore use the realised volume of each firm-window as the conditioning object in the benchmark rather than interpreting this level estimate as a separate result.

### Hiring-state split

The raw extensive-margin change is larger among firms that entered the transaction with lower hiring intensity. Their share of no-hire months falls by 0.1076 [−0.1551, −0.0613], compared with 0.0182 [−0.0452, 0.0131] among more active targets. Once each group is benchmarked against its own realised hiring volume, however, the corresponding excesses are 0.0058 [−0.0249, 0.0350] and 0.0027 [−0.0159, 0.0203]. The difference between these excesses is 0.0032 [−0.0321, 0.0365]. The state split therefore reinforces the interpretation in the main text: firms with lower pre-deal hiring intensity hire more after investment, but the monthly allocation of those additional hires contributes little additional variation once realised volume is held fixed.

### A.3 Extensive- and intensive-margin decomposition

The twelve-month hiring rate can be written as

where  is the share of months with positive hiring and  is mean hiring intensity in active months, measured as hires relative to employment. The factor 12 reflects the length of the measurement window; it does not annualise the primary hiring-rate outcome.

### Table A2. Decomposition of the average increase in hiring

[TABLE #3]
| Component | Estimate | 95% CI |
|---|---|---|
| Change in active-month share, | +0.0443 | [+0.0247, +0.0645] |
| Change in active-month hiring intensity, | +0.0048 | [−0.0001, +0.0102] |
| Change in log active-month share, | +0.1011 | [+0.0544, +0.1496] |
| Change in log active-month intensity, | +0.0652 | [+0.0074, +0.1242] |

Notes. The pre-deal means are  and . In logs, the two components are additive; the change in  accounts for 0.608 of the summed log change. We do not report a ratio based on aggregate level changes because the denominator is unstable when positive and negative firm-level changes offset one another.

Both components rise in the log decomposition. The increase in the active-month share accounts for 60.8 percent of the summed log change. This decomposition describes how the increase in hiring appears in monthly data, but it should not be interpreted as identifying a separate extensive-margin choice. As Table A1 shows, the probability of observing an active hiring month rises mechanically with realised hiring volume. The volume benchmark is therefore the relevant comparison when using monthly participation measures to make claims about the timing or frequency of labour adjustment.

### Appendix B. State construction and alternative specifications

The primary analysis measures the target’s pre-deal hiring state using its hiring rate over months −24 to −13, with the index oriented so that higher values correspond to lower hiring intensity. This appendix examines the construction of that state and reports selected alternative specifications of the main hiring gradient. We focus on alternatives that address the interpretation of the state, the treatment of zero-hiring observations and outliers, and the construction of the matched comparison. Measurement checks for the administrative hiring variable itself are reported separately in Appendix C.

### B.1 Alternative measures of the pre-deal hiring state

Pre-deal hiring activity can be summarized using the hiring rate, total hiring volume, or the frequency of months with any hiring. These measures describe related aspects of the same underlying activity state but need not contain the same information after conditioning on firm characteristics.

All measures in Table B1 are constructed over months −24 to −13. Signs are oriented so that a positive coefficient corresponds to a larger post-deal hiring response among less active firms. The adjusted specifications partial out log pre-deal employment, pre-deal employment growth, firm age, and one-digit industry from both the outcome and the state.

### Table B1. Alternative measures of pre-deal hiring activity

[TABLE #4]
| State measure | Unadjusted slope | Adjusted slope, 95% CI |
|---|---|---|
| Hiring rate | 0.4964 | 0.5650 [0.210, 0.968] |
| Hiring volume | 0.1275 | 0.1578 [0.020, 0.291] |
| Share of months with no hiring | 0.5259 | 0.3522 [−0.079, 0.829] |

Notes. All state measures use months −24 to −13. The scales differ across the three indices, so coefficient magnitudes should not be compared directly. Positive coefficients indicate larger subsequent hiring responses among firms with lower pre-deal activity. The adjusted specification removes the same pre-deal covariates used in the main analysis from both the state and the outcome.

The hiring-rate measure is the most stable of the three once the pre-deal covariates are included. Grouping firms by the adjusted hiring-rate state gives a low- versus high-activity contrast of 0.215 [0.026, 0.392] using terciles, 0.215 [0.030, 0.425] using quartiles, and 0.188 [0.031, 0.332] using a median split. The corresponding continuous hiring-rate slope also increases rather than decreases after adjustment.

The share of no-hire months is more closely tied to total hiring volume. Over the same pre-deal window, the correlation between the no-hire share and log hiring volume is −0.854. We therefore also construct a volume-adjusted frequency measure by subtracting the no-hire share implied by allocating each firm’s realised pre-deal hires across months using the volume benchmark in Appendix A. This adjustment reduces the correlation with hiring volume to −0.013. The tercile contrast in the volume-adjusted frequency measure is 0.0031 [−0.176, 0.190]. Within quintiles of pre-deal hiring volume, the pooled frequency slope is −0.066; residualising frequency on volume and size gives 0.063; and restricting the sample to firms with at least twelve pre-deal hires gives 0.010 conditional on volume.

These comparisons motivate the interpretation of the primary state as pre-deal hiring intensity rather than as the frequency of hiring months itself. The different indices remain related descriptions of firm activity, but the frequency component has little separate association with the post-deal response once realised hiring volume is removed.

### B.2 Persistent hiring history and the firm’s position at closing

The main text distinguishes a broader low-hiring condition from a short-lived pause immediately before the transaction. Table B2 collects the corresponding checks.

### Table B2. What component of the pre-deal state carries the gradient?

[TABLE #5]
| Specification | Estimate | 95% CI |
|---|---|---|
| Hiring state, controlling for pre-deal employment growth | 0.410 | [0.078, 0.753] |
| Historical share of no-hire months | 0.559 | [0.241, 0.885] |
| Length of hiring pause in progress at closing | 0.040 | [−0.016, 0.107] |
| Residualised hiring state | 0.243 | [−0.221, 0.723] |
| Earlier hiring state, months −36 to −25 | 0.268 | — |

Notes. The residualised state removes size, industry, pre-deal growth, age, and seasonality, which jointly account for 63.9 percent of its variance. The earlier-state specification redefines the matching state using months −36 to −25 and reconstructs the state-balanced comparison accordingly. Its untreated placebo mean is 0.141, giving an excess of 0.127 and an upper-tail placebo .

When the historical no-hire share and the pause in progress at closing enter together, their point estimates are 0.536 and 0.032, respectively. The larger response among low-hiring targets is therefore more closely associated with their broader recent hiring history than with the duration of a pause already underway at the transaction date.

The residualised-state result provides a separate qualification. Size, industry, growth, age, and seasonality together explain 63.9 percent of the variation in the state. Removing that component leaves the same positive sign, 0.243, but a considerably wider interval [−0.221, 0.723]. The data therefore support the broader observed hiring state more clearly than a residual state stripped of most observable variation.

Moving the state window further into the past weakens the relationship more sharply. Using months −36 to −25 produces a gradient of 0.268 against a specification-specific placebo mean of 0.141. The standardized distance is 0.92 and the upper-tail placebo -value is 0.1789. This is the main adverse state-timing result: the association is considerably weaker for hiring activity measured two to three years before the transaction, which is more consistent with a relatively recent pre-deal condition than with a permanent firm type.

### B.3 Outcome transformations and winsorisation

The primary outcome is the change in the log hiring rate and therefore requires positive hiring in both twelve-month windows. This restriction removes three treated firm-windows. We examine transformations that retain zero-hiring windows and alternative treatments of the tails of the outcome distribution.

### Table B3. Alternative transformations of the hiring outcome

[TABLE #6]
| Specification | Gradient | Placebo mean (SD) | Standardized distance | Upper-tail placebo |
|---|---|---|---|---|
| Winsorised 5/95, primary | 0.710 | 0.101 (0.154) | 3.96 | 0.0005 |
| Unwinsorised | 0.837 | 0.122 (0.181) | 3.96 | 0.0005 |
| Winsorised 1/99 | 0.816 | 0.114 (0.171) | 4.10 | 0.0010 |
| Winsorised 10/90 | 0.634 | 0.096 (0.136) | 3.96 | 0.0005 |
| Inverse hyperbolic sine of hiring rate | 0.206 | 0.026 (0.059) | 3.08 | 0.0010 |
| ​ | 0.162 | 0.017 (0.045) | 3.24 | 0.0020 |

Notes. Winsorisation cut-offs are calculated from the treated sample and the same absolute values are applied to the placebo observations. The inverse-hyperbolic-sine and  transformations retain zero-hiring windows. Their coefficients are on different scales from the primary log-rate outcome and should not be compared numerically with the headline gradient. Each row has its own placebo distribution generated using the same transformation and estimation procedure.

The gradient remains positive across the principal winsorisation choices. The unwinsorised estimate is 0.837, compared with 0.710 under the primary 5/95 specification; more aggressive 10/90 winsorisation lowers the estimate to 0.634. The primary estimate therefore does not arise from an unusually favourable treatment of the tails and lies toward the lower end of the specifications using the reported hiring measure.

The transformations that retain zero-hiring windows also preserve the directional result. Because these transformations behave more like the level of the hiring rate at the magnitudes observed in the sample, their coefficients cannot be compared directly with the 0.710 log-rate gradient. Their role is narrower: they show that the exclusion of the three zero-hiring treated windows is not responsible for the state-dependent pattern.

A Poisson pseudo-maximum-likelihood specification provides a less supportive check. Applied to hire counts with log employment as an offset, the coefficient is 0.104 [−0.319, 0.526]. The point estimate has the same sign as the primary result but is too imprecise to establish a corresponding count-model relationship. We report this result because it changes the functional form and avoids the log transformation rather than because it strengthens the main specification.

### B.4 Selected matching and estimation alternatives

We also examine whether the gradient depends on particular choices in the construction of the matched sample. Rather than report every specification considered during development, Table B4 presents alternatives that change a distinct element of the design: the number of controls, the role of the state in neighbour selection, the state-window completeness requirement, the coarseness of matching cells, the state horizon, weighting, and deal-year adjustment.

### Table B4. Selected alternatives to the primary matching and estimation design

[TABLE #7]
| Specification | Events | Gradient | Standardized distance | Upper-tail placebo |
|---|---|---|---|---|
| Primary: exact state tercile, 5 controls | 286 | 0.710 | 3.96 | 0.0005 |
| Exact state tercile, 20 controls | 286 | 0.678 | 4.12 | 0.0005 |
| State included in neighbour distance, 5 controls | 299 | 0.640 | 3.54 | 0.0010 |
| At least 6 of 12 state months observed | 310 | 0.655 | 4.57 | 0.0005 |
| Two state bins rather than three | 292 | 0.610 | 3.65 | 0.0005 |
| One-digit rather than two-digit industry cell | 299 | 0.636 | 3.69 | 0.0005 |
| State measured over months −36 to −13 | 244 | 0.388 | 2.33 | 0.0115 |
| Inverse-variance weighting | 286 | 0.346 | 2.28 | 0.0155 |
| Add deal-year fixed effects | 286 | 0.678 | 3.50 | 0.0010 |

Notes. Every specification reconstructs the untreated placebo distribution using the corresponding matching and estimation procedure. The primary design requires an exact tercile of the twelve-month hiring state and five controls. The state-in-distance specification does not exact-match on the state tercile but instead includes the state when selecting nearest neighbours within the remaining matching structure. Relaxing state-window completeness increases the usable sample; the primary analysis retains the complete twelve-month requirement to keep the state definition constant across events.

Several patterns are worth noting. Increasing the number of controls from five to twenty changes the gradient little. Including the state in the neighbour-distance calculation rather than imposing the primary exact-tercile restriction also produces a similar positive gradient, although adding more distant neighbours progressively weakens the estimate in specifications not shown here. Likewise, using two state bins or broader one-digit industry cells increases the sample but leaves the qualitative result unchanged.

Relaxing the requirement that all twelve state months be observed adds twenty-four events and gives a gradient of 0.655. We nevertheless retain complete state windows in the primary specification because incomplete windows change the measurement of the moderator across events. Extending the state over a longer twenty-four-month period, months −36 to −13, reduces the usable sample to 244 events and the gradient to 0.388. Together with the earlier-state result in Table B2, this reinforces the importance of the relatively recent pre-deal hiring history.

The inverse-variance-weighted specification produces a smaller gradient of 0.346 and a different placebo distribution; its standardized distance falls to 2.28. Adding deal-year fixed effects, by contrast, leaves the estimate close to the primary specification at 0.678. The alternatives therefore show meaningful variation in precision and magnitude but do not turn the specification exercise into evidence that every reasonable estimator produces the same number.

### B.5 Summary

The appendix results support three narrower conclusions about the construction of the main state gradient.

First, the hiring-rate index is the most stable summary of pre-deal hiring activity after adjustment for observable firm characteristics. The frequency of hiring months contains much less separate information once realised hiring volume is accounted for.

Second, the state is most informative when measured over the relatively recent pre-deal period. The gradient weakens when the state is pushed further into the past, and a state stripped of most observable firm-level variation is estimated too imprecisely to support a stronger interpretation.

Third, the positive gradient is present under alternative winsorisation choices, zero-retaining transformations, and several matching constructions. The Poisson specification and some weighting or longer-window alternatives are substantially less precise. These results support the stability of the broad state-dependent pattern while leaving the primary specification as the estimand and implementation used for the paper’s headline result.

### Appendix C. Measurement of worker entries and flow outcomes

The main analysis treats monthly National Pension entries as worker inflows and uses them to construct the hiring rate. Two measurement issues warrant additional checks. First, an administrative entry need not always represent an external hire: payroll consolidation or employee re-registration around a transaction could generate entries without corresponding recruitment. Second, both hiring and separation rates divide worker flows by employment, which is itself an outcome. This appendix examines the accounting consistency of the pension records, reconstructs hiring without using the reported entry field, and reports additional worker-flow and employment diagnostics.

### C.1 Accounting consistency of worker entries and exits

The pension records contain monthly insured employment, worker entries, and worker exits. These variables should approximately satisfy the employment-flow accounting relation: changes in insured employment should correspond to entries less exits, subject to administrative timing and reporting discrepancies.

Across 227,339 firm-month observations, the accounting relation holds closely. The median absolute discrepancy is one worker, and 24.3 percent of firm-months reconcile exactly. Scaled by employment, the median absolute discrepancy is 1.4 percent and the 90th percentile is 7.1 percent.

### Table C1. Accounting consistency of pension worker flows

[TABLE #8]
| Measure | Value |
|---|---|
| Firm-month observations | 227,339 |
| Median absolute discrepancy | 1 worker |
| Share reconciling exactly | 24.3% |
| Median discrepancy relative to employment | 1.4% |
| 90th percentile, relative discrepancy | 7.1% |
| Treated firms, year before transaction | 2.8% |
| Treated firms, transaction month | 3.6% |
| Treated firms, post-transaction period | 3.1% |

Notes. The discrepancy compares the observed change in insured employment with the net worker flow implied by reported entries and exits. Relative discrepancies scale the absolute difference by employment. The treated-firm figures report the corresponding relative discrepancy around the transaction.

The discrepancy rises around the transaction, from 2.8 percent in the preceding year to 3.6 percent in the deal month, before falling to 3.1 percent afterward. The temporary increase is consistent with some transaction-related administrative adjustment. Its size, however, is modest relative to employment and does not persist into the post-deal period. We therefore retain the qualification that individual entry records need not always be external hires rather than assuming exact accounting identity at every firm-month.

### C.2 Alternative filters and reconstructed hiring

We next ask whether the state gradient depends on firm-months in which the accounting discrepancy is relatively large. Tightening discrepancy filters leaves positive point estimates but reduces the usable sample and, in some cases, substantially widens uncertainty.

### Table C2. Hiring-state gradient under worker-flow measurement checks

[TABLE #9]
| Specification | Gradient | 95% interval / inference |
|---|---|---|
| Primary hiring measure | 0.7101 | [0.3187, 1.1254] |
| Exclude months with relative discrepancy above 10% | 0.312 | not separately detected |
| Exclude months with relative discrepancy above 5% | 0.544 | not separately detected |
| Exclude months with total turnover above 50% of employment | 0.488 | [0.102, 0.850] |
| Exclude treated firms that change the number of registered workplaces | 0.557 | [0.160, 0.930] |
| Hiring reconstructed from employment change and recorded exits | 0.365 | upper-tail placebo |

Notes. The first two discrepancy filters discard firm-months according to the absolute accounting discrepancy relative to employment. The turnover filter excludes months in which entries plus exits exceed half of employment. Only three of the 379 treated firms change their number of registered workplaces around the transaction. The reconstructed-hiring specification infers worker entries from the employment-flow identity rather than using the reported entry field.

Two features of these results are useful. The point estimates remain positive under each measurement restriction, but the strict discrepancy filters lose statistical precision. We report that loss rather than treating sign stability alone as robustness.

The workplace-registration check addresses a related concern. If a transaction created large numbers of administrative entries by reorganising establishments or payroll units, the number of registered workplaces might change at the same time. Only three of the 379 treated firms experience such a change; excluding them yields a gradient of 0.557 [0.160, 0.930].

The reconstructed-hiring measure is the strongest check because it does not use the reported entry count as its hiring variable. Its gradient is smaller than the primary estimate, at 0.365, but remains positive relative to its own untreated placebo distribution (upper-tail ). Taken together, the accounting, workplace, and reconstructed-flow checks support treating NPS entries primarily as worker inflows, while preserving the qualification that the administrative measure is not a direct record of external recruitment.

### C.3 Hiring rates, employment denominators, and level flows

The primary hiring outcome scales entries by employment. Because employment can itself change after a private equity investment, a firm with falling employment can display a higher flow rate even without a proportionate increase in worker entries.

The main text addresses this issue directly. The gradient in the raw log count of hires is 0.6315 against a placebo mean of 0.1795, and the estimate is 0.6957 after controlling for the change in log employment, against a placebo mean of 0.0363. The corresponding log-employment gradient is −0.0580 against a placebo mean of 0.0796. The primary state gradient is therefore driven mainly by variation in worker entries themselves rather than by employment appearing in the denominator.

Level flow rates provide an additional accounting check but illustrate why log employment is the preferred measure of net employment adjustment. The state gradients in the level hiring rate, separation rate, and net inflow rate are +0.263, +0.094, and +0.172, respectively; the accounting relation among these gradients holds to within 0.003.

The positive level net-inflow gradient differs in sign from the negative gradient in log employment. This is not an inconsistency in the worker-flow accounting. The level net-inflow rate also divides by employment, so changes in its denominator can move the rate in the opposite direction from log employment itself. We therefore use log employment—whose outcome is not scaled by contemporaneous employment—as the primary measure of differential net employment growth.

### Table C3. Flow-rate accounting and employment

[TABLE #10]
| Outcome | State gradient |
|---|---|
| Level hiring rate | +0.263 |
| Level separation rate | +0.094 |
| Level net inflow rate | +0.172 |
| Log employment | −0.0580 |

Notes. The first three rows are level worker-flow rates and therefore scale flows by employment. Their accounting identity holds to within 0.003 in the estimated gradients. Log employment does not contain employment in its own denominator and is the measure used in the main text to characterise net employment adjustment.

### C.4 Employment horizons and additional worker-flow contrasts

The main text reports the twelve-month log-employment gradient and the principal hiring- and churn-versus-employment contrasts. Longer horizons produce the same broad ordering.

### Table C4. Additional employment horizons and worker-flow contrasts

### Panel A. Relative employment at longer horizons

[TABLE #11]
| Horizon | Gradient | Standardized distance | Events |
|---|---|---|---|
| +12 months | −0.0316 | −1.92 | 291 |
| +24 months | −0.1616 | −1.63 | 245 |
| +36 months | −0.2092 | −2.29 | 203 |

### Panel B. Additional within-event contrast

[TABLE #12]
| Contrast | Estimate | Inference |
|---|---|---|
| Hiring − separations | 0.5746 | two-sided |

Notes. Relative employment measures log employment at the stated horizon relative to the mean of months −6 to −1 and difference that change against matched controls. The twenty-four-month estimate is not individually detected. The hiring-minus-separations contrast is formed within the same events and is tested against a two-sided placebo distribution.

The relative-employment gradients are negative at all three horizons. The magnitude becomes more negative with the horizon, although precision falls as fewer events have complete longer post-deal windows. These estimates support the distinction in the main text between the average increase in employment across targets and the negative cross-target employment gradient with respect to the pre-deal hiring state.

The hiring-minus-separations contrast is positive at 0.5746 and reaches a two-sided -value of 0.043. We do not use this result to claim that the separation channel is identified. The separation gradient on its own is 0.1788 with  and , so the composition of gross worker flows remains too imprecise to assign the state-dependent response to worker exits specifically.

### C.5 Joint worker-flow pattern

Hiring, churn, and employment are correlated outcomes. Evaluating them one at a time therefore discards information about their joint configuration. We compute the vector of the three state gradients on each untreated placebo draw and compare the observed vector with the resulting multivariate placebo distribution.

The observed  vector has a Mahalanobis distance of 28.4 from the placebo mean. The 95th percentile of the corresponding placebo distribution is 7.6. Under the null, the hiring and churn gradients have a correlation of approximately 0.71, so the joint calculation accounts for substantial covariance between the two gross-flow outcomes.

The joint comparison reinforces the interpretation of the individual estimates. What is unusual among private equity targets is the configuration of a large positive hiring gradient, a positive churn gradient, and a negative employment gradient across the same pre-deal state. The joint result supports a gross worker-flow pattern, but it does not resolve the separation margin or identify an internal organisational mechanism.

### Figure C1. State gradients and placebo distributions across worker-flow outcomes

[IMAGE #1]
Notes. State gradients and placebo distributions across worker-flow outcomes. Panel (a) plots the state gradient for hiring, churn, separations, and log employment under the primary specification. Grey bands show the central 95 percent of the specification-specific untreated placebo distribution and tick marks show its mean; these null distributions need not be centred at zero. Panel (b) plots within-event outcome contrasts. The hiring row reproduces the Table 3 estimate, while the separation gradient is positive but not separately detected. The gross-flow interpretation therefore rests on hiring, churn, and their paired contrasts with employment rather than on an identified separation response.

### C.6 Summary

The measurement checks support three conclusions.

First, worker entries, exits, and employment satisfy the monthly accounting relation closely for most observations. Accounting discrepancies rise modestly at the transaction month but fall afterward, and changes in registered workplaces are rare.

Second, the hiring-state gradient remains positive when hiring is reconstructed without the reported entry field and under several filters designed to remove firm-months with unusually large flow discrepancies. The stricter filters reduce precision, so these checks support the interpretation of pension entries as worker inflows without establishing that every entry is an external hire.

Third, the distinction between gross worker flows and net employment is robust to several ways of examining the outcomes. Hiring and churn gradients are positive relative to employment, longer-horizon employment gradients remain negative, and the joint outcome vector is far from its untreated placebo distribution. The separation gradient itself remains imprecise, leaving the worker-exit margin unresolved.

### Appendix D. Additional validity and sensitivity checks

The main text evaluates the hiring-state gradient using a non-overlapping pre-deal comparison and a relative-magnitude sensitivity analysis at the same twelve-month resolution as the primary estimand. This appendix reports supplementary checks at finer temporal resolution and examines three additional concerns: selection on sponsor timing, measurement error in the transaction date, and dependence created by the limited reuse of control firms. We also report the corresponding relative-magnitude sensitivity calculation for the separate average-effect estimand.

### D.1 Quarterly state-gradient dynamics

The twelve-month pre-deal comparison in Table 5 is the primary pre-trend diagnostic because it matches the resolution of the headline estimand. A quarterly version of the same exercise is considerably noisier.

The treated state gradient over the four pre-deal quarters is , , , and , in chronological order. The corresponding four post-deal gradients are , , , and . None of the individual quarterly estimates is separately detected. The mean pre-deal gradient is  with an interval of [−0.163, 0.131], while the mean of the four post-deal coefficients is 0.126.

### Table D1. State gradients at quarterly resolution

[TABLE #13]
| Period | Quarter 1 | Quarter 2 | Quarter 3 | Quarter 4 |
|---|---|---|---|---|
| Treated, pre-deal | +0.087 | −0.042 | −0.038 | −0.056 |
| Treated, post-deal | +0.147 | +0.240 | +0.108 | +0.010 |
| Untreated pseudo-events, pre-deal | −0.073 | −0.031 | −0.003 | +0.045 |
| Untreated pseudo-events, post-deal | −0.024 | +0.088 | −0.040 | −0.000 |

Notes. Entries are state gradients estimated at quarterly resolution, with quarters shown in chronological order within the pre- and post-deal periods. The treated pre-deal mean is −0.012 [−0.163, 0.131]. A single pre-deal drift over the four quarters is −0.038 [−0.600, 0.473]. No individual treated pre- or post-deal quarter is separately detected.

Estimating a single drift over the four pre-deal quarters does not materially improve precision: the cumulative drift is −0.038 [−0.600, 0.473]. At this finer resolution, the relative-magnitude breakdown value falls to zero because the denominator of the sensitivity calculation is dominated by sampling noise in the quarterly pre-trend estimates. We therefore do not use the quarterly exercise to calibrate the identifying assumption. The twelve-month result in the main text is the more informative diagnostic because it is measured at the same resolution as the primary gradient.

The untreated pseudo-event path is also noisy. Its four pre-deal gradients are −0.073, −0.031, −0.003, and +0.045; the corresponding post-deal values are −0.024, +0.088, −0.040, and approximately zero. Two of the eight placebo-quarter estimates are individually detected. The quarterly exercise therefore adds little precision beyond the twelve-month comparison and is reported here mainly to show the behaviour of the gradient at a finer temporal resolution.

### D.2 Sponsor deployment pressure

A difficult alternative to the matched comparison is selection on information observed by the sponsor but absent from the researcher’s data. A sponsor may invest in a low-hiring target when it privately anticipates future expansion. The pre-deal diagnostics in the main text cannot eliminate this possibility.

We examine one implication using a sponsor deployment-pressure proxy based on the age of the sponsor’s most recent fund. The economic intuition is that a sponsor operating an older fund may face greater pressure to deploy remaining capital and therefore have less scope to wait for particularly favourable targets or timing. In the monthly hazard specification, the interaction between treatment, the post-deal period, and this pressure measure has a hazard ratio of 1.2881 [1.0535, 1.5750] across 379 events.

### Table D2. Supplementary validity checks

[TABLE #14]
| Check | Estimate | 95% interval | Events |
|---|---|---|---|
| Sponsor deployment pressure, hazard ratio | 1.2881 | [1.0535, 1.5750] | 379 |
| Independently date-confirmed subsample, no-hire share | −0.0645 | [−0.1145, −0.0163] | 62 |
| Primary gradient, one event per control firm | 0.7036 | — | 286 |

Notes. The deployment-pressure row reports the treated-post interaction with the manuscript’s proxy based on the age of the sponsor’s most recent fund. [Confirm the exact coding and scale of the pressure variable from the analysis code before submission.] The date-confirmed row uses the shareholder-register subsample for which the transaction year is independently observed. The final row restricts each control firm to a single matched event.

The deployment-pressure result runs against the simplest version of the private-information selection account: the post-deal response is larger in the setting where the sponsor is interpreted as having less flexibility to wait for an especially favourable target or transaction date. The comparison remains suggestive rather than decisive. Older-fund deals may differ from other transactions in target composition, fund strategy, sponsor circumstances, or other unobserved dimensions. We therefore do not treat this interaction as an instrument or as evidence that private-information selection has been removed.

The inspected manuscript material does not specify the exact scaling or coding of the deployment-pressure variable. That construction should be inserted from the analysis code before the appendix is finalised; the hazard ratio itself is locked at 1.2881 [1.0535, 1.5750].

### D.3 Independent confirmation of transaction timing

PitchBook provides the transaction dates used throughout the main analysis. Annual shareholder records offer an independent check on timing for a subset of events by identifying the year in which the sponsor stake first appears.

The shareholder-register date can be confirmed independently for 62 events. In this subsample, the treated-minus-control share of no-hire months falls by 0.0645 [−0.1145, −0.0163], compared with approximately 0.047 in absolute magnitude in the full sample.

This comparison is deliberately qualitative. The confirmed-date sample is small, and the outcome is the no-hire share rather than the primary log hiring-rate gradient. The result nevertheless provides some evidence against moderate transaction-date error as the main explanation for the post-deal hiring pattern: the independently confirmed subsample moves in the same direction and, on this secondary outcome, by a somewhat larger amount.

Because the shareholder records are annual, this exercise validates the deal year rather than the exact transaction month. It therefore cannot rule out within-year timing error.

## D.4 Shared controls and uncertainty

The primary gradient uses five controls per target, and a control firm can in principle appear in more than one matched set. Repeated use of the same controls could induce dependence across event-level outcomes.

In practice, overlap is limited. The 286 primary target events use 1,144 distinct control firms. Of these controls, 95.02 percent appear in only one event, and no control firm is used in more than three events.

### Table D3. Sensitivity to shared control firms

[TABLE #15]
| Specification | Gradient | 95% interval |
|---|---|---|
| Bootstrap clustered on treated firms | 0.7101 | [0.3187, 1.1254] |
| Bootstrap clustered on control firms | 0.7101 | [0.4595, 0.8771] |
| Each control assigned to at most one event | 0.7036 | — |

Notes. The primary paper reports the treated-firm-clustered interval because it is wider than the interval obtained when the bootstrap is clustered on control firms. The one-event-per-control specification removes repeated control use and re-estimates the state gradient on the 286 primary events.

Clustering on control firms produces a narrower interval than clustering on treated firms. Restricting each control firm to a single event also leaves the point estimate close to the primary value, at 0.7036. These comparisons indicate that the main uncertainty is not being generated by repeated use of a small set of control firms. We retain the wider treated-firm-clustered interval in the main text.

### D.5 Relative-magnitude sensitivity of the average effect

The main paper reports two different estimands: the average post-deal effect and the state gradient. Their sensitivity calculations should therefore be kept separate.

For the average-effect estimand, the relative-magnitude breakdown value following Rambachan and Roth (2023) is 0.658. At the resolution of that estimand, the estimate remains distinguishable from zero while post-treatment differential trends are allowed to reach 0.658 times the largest observed pre-period quarterly movement.

Rambachan and Roth’s relative-magnitude framework bounds possible post-treatment violations of parallel trends relative to the largest pre-treatment violation. A breakdown value records the magnitude of permitted post-treatment deviation at which the relevant confidence set first includes the null.

The 0.658 value should not be compared mechanically with the 3.126 breakdown value reported for the state gradient in Table 5. The two calculations concern different estimands, use different outcome constructions, and are calibrated at their respective temporal resolutions. For the average effect, a breakdown value below one means that the conclusion becomes indistinguishable from zero before permitted post-treatment differential trends reach the size of the largest observed pre-period movement. We therefore regard the average-effect result as more sensitive to departures from parallel trends than the primary state-gradient comparison.

### Table D4. Relative-magnitude sensitivity

[TABLE #16]
| Estimand | Breakdown value |
|---|---|
| State gradient, twelve-month resolution | 3.126 |
| Average post-deal effect | 0.658 |

Notes. The state-gradient value is reproduced from main Table 5 for comparison only. The average-effect value is a separate sensitivity calculation. A larger value means that the corresponding estimate remains distinguishable from zero under a larger permitted relative deviation from the observed pre-treatment trend. The two rows should not be read as estimates of the same parameter.

### D.6 Interpretation

These checks provide supplementary information rather than an independent identification strategy. Quarterly estimates of the state gradient are too noisy to improve on the twelve-month pre-deal diagnostic. The independently confirmed-date sample moves in the same direction as the full sample, and limited reuse of control firms has little effect on the point estimate. The deployment-pressure interaction is also directionally inconsistent with the simplest private-information timing story, although it is not a clean test of selection.

The average-effect sensitivity result is less reassuring than the corresponding state-gradient calibration and should be reported as such. None of these checks eliminates the principal limitation identified in the main text: sponsors may possess information about future firm conditions that is not observed in the administrative or transaction data.

### Appendix E. Transaction and sponsor characteristics

The main analysis organises variation in post-deal hiring around the target’s pre-deal hiring state. This appendix reports the underlying comparisons with transaction structure and sponsor characteristics. The outcome throughout is the event-level treated-minus-control change in the log hiring rate used in the main analysis.

Individual comparisons use the largest sample available for each characteristic. A second set of analyses restricts the sample to the 180 events for which all transaction variables used in the joint comparison are observed. Because the available samples differ across characteristics, the individual coefficients should not be interpreted as a common-sample ranking.

### E.1 Individual transaction and sponsor comparisons

We consider whether the hiring response varies with transaction type, the sponsor’s recorded ownership stake, majority ownership, and sponsor experience. Covariate-adjusted estimates residualise the event-level response on the pre-deal hiring state, log firm size, pre-deal employment growth, firm age, industry, and deal year.

The distinction between control transactions and growth investments illustrates why this adjustment matters. The unadjusted response difference is 0.1218 log points [−0.0494, 0.2776]. Targets in control transactions also enter the deal with lower prior hiring activity: their pre-deal share of no-hire months is 0.0948 higher than that of growth-investment targets. After adjusting for the hiring state and the other pre-deal characteristics, the estimated difference falls to 0.0475 [−0.1062, 0.1958].

### Table E1. Hiring responses across transaction and sponsor characteristics

[TABLE #17]
| Characteristic | Estimate | 95% CI | Events |
|---|---|---|---|
| Control transaction − growth investment, unadjusted | 0.1218 | [−0.0494, 0.2776] | 301 |
| Control transaction − growth investment, adjusted | 0.0475 | [−0.1062, 0.1958] | 301 |
| Acquired ownership stake, per percentage point, adjusted | 0.0007 | [−0.0015, 0.0027] | 181 |
| Majority (≥50%) − minority investment, adjusted | 0.0397 | [−0.1761, 0.2674] | 181 |
| Sponsor experience, top − bottom tercile, adjusted | 0.0692 | [−0.1278, 0.2609] | 301 |
| Sponsor identity, leave-one-out prediction | −0.2675 | — | 189 |

Notes. The outcome is the event-level change in the log hiring rate. Adjusted estimates partial out the pre-deal hiring state, firm size, pre-deal employment growth, age, industry, and deal year. The ownership stake is the sum of private equity holders’ common-share stakes reported in the shareholder register for the entry year. The transaction-level percentage-acquired field is not used because its distribution is heavily concentrated at 100 percent and does not support a useful tercile comparison. Sponsor experience is based on sponsor deal activity; [confirm the exact deal-count window and construction from the analysis code before submission].

The point estimates for ownership stake, majority ownership, and sponsor experience are positive, but their intervals are wide. For example, the majority–minority interval spans from −0.1761 to 0.2674 log points. The data therefore remain compatible with economically meaningful differences along these dimensions even though the individual comparisons are estimated imprecisely.

The acquired-stake and sponsor-experience variables are only weakly correlated with the pre-deal hiring state in the available data: the corresponding correlations are 0.0099 and 0.0919. Covariate adjustment therefore matters most visibly for transaction type, where target composition differs before the transaction.

### E.2 Common-sample explanatory content

The individual comparisons above use different samples and are not well suited to a direct comparison of explanatory content. We therefore restrict the analysis to the 180 events for which control status, acquired stake, and sponsor deal count are all observed.

On this sample, the transaction-characteristic model contains an indicator for a control transaction, acquired ownership stake, and log sponsor deal count. The comparison model contains the pre-deal hiring state alone. Permutation tests randomly relabel the relevant regressors 2,000 times and recompute model fit.

### Table E2. In-sample explanatory content on the common sample

[TABLE #18]
| Model or incremental contribution | ​ | Permutation |
|---|---|---|
| Transaction characteristics jointly | 0.0092 | 0.6425 |
| Pre-deal hiring state alone | 0.0286 | 0.0250 |
| Transaction characteristics added to the state | 0.0068 | — |
| State added to transaction characteristics | 0.0261 | — |

Notes. The sample contains 180 events with complete transaction information. The transaction-characteristic model includes control status, acquired ownership stake, and log sponsor deal count. Permutation -values are based on 2,000 relabellings. The 95th percentile of the permutation distribution for the transaction-characteristic model is 0.0433. Incremental  reports the change in fit when one set of variables is added to a model containing the other.

The observed transaction characteristics jointly explain 0.92 percent of the variation in event-level hiring responses. This fit lies well within the permutation distribution (). The hiring state alone explains 2.86 percent, with a permutation . Adding the state to the transaction-characteristic model raises  by 2.61 percentage points, while adding the transaction characteristics to the state raises it by 0.68 percentage points.

These estimates support the narrower comparison made in the main text: on the common sample, the target’s pre-deal hiring condition has clearer within-sample explanatory content than the observed transaction characteristics. They do not establish that transaction structure is economically unimportant, nor do the  values measure causal importance.

The broader covariate set used for adjustment explains 12.8 percent of the variation in the event-level response, reducing its residual standard deviation from 0.6871 to 0.6415. This comparison is useful mainly for understanding why covariate-adjusted transaction estimates can differ from simple group contrasts; it is not part of the state-versus-transaction  comparison in Table E2.

### E.3 Out-of-sample comparison

In-sample explanatory content need not translate into forecasting performance. We therefore repeat the state-versus-transaction comparison using five-fold cross-fitting on the same 180 events.

### Table E3. Five-fold out-of-sample comparison

[TABLE #19]
| Model | Out-of-sample | 95% CI |
|---|---|---|
| Transaction characteristics | −0.0269 | — |
| Pre-deal hiring state | −0.0168 | — |
| Difference: state − transaction characteristics | 0.0101 | [−0.0349, 0.1173] |

Notes. Models are estimated using five-fold cross-fitting on the 180-event common sample. A negative out-of-sample  indicates prediction that is worse, on average, than assigning held-out observations the sample mean response. The reported interval applies to the difference between the two models. Folds are assigned at the event level rather than being grouped by sponsor.

Both out-of-sample  values are negative. The state model performs somewhat less poorly than the transaction-characteristic model, but the difference of 0.0101 is estimated imprecisely [−0.0349, 0.1173]. The common-sample result therefore does not establish that the hiring state is a better forecasting variable for held-out transactions.

This distinction is important for the interpretation of Section 7.2. The evidence separates the two models in terms of within-sample explanatory content, but not in terms of validated out-of-sample prediction. We therefore avoid using the state as a proposed target-selection or forecasting rule.

### E.4 Sponsor identity and persistence across deals

The sponsor-identity exercise asks a different question: whether a sponsor’s response in its other transactions predicts the response in a held-out transaction by the same sponsor. For each eligible event, we construct the mean response across the sponsor’s other observed deals and use that leave-one-out mean to predict the held-out event.

The resulting coefficient is −0.2675 across 189 leave-one-out observations. Repeat-deal information is sparse: 164 sponsors contribute to the exercise, and the typical sponsor contributes very little information beyond the held-out observation. The negative sign is therefore difficult to interpret as a substantive sponsor effect.

### Table E4. Sponsor-identity diagnostics

[TABLE #20]
| Specification | Leave-one-out coefficient |
|---|---|
| Baseline sponsor leave-one-out | −0.2675 |
| Outcome winsorised at 1/99 | −0.2659 |
| Outcome winsorised at 5/95 | −0.2387 |
| Drop five most influential events | −0.1751 |
| Covariate-adjusted response | −0.2261 |

Notes. Each specification predicts an event using the mean response in the same sponsor’s other observed transactions. The influence check removes the five events with the greatest effect on the baseline coefficient. In the full event dataset, business registration numbers are unique across the 379 matched events, so repeated observation of the same target does not generate the sponsor-level relationship.

The coefficient remains negative under the alternative winsorisation and covariate-adjustment choices, although removing the five most influential observations attenuates it by roughly one-third. We do not assign an economic interpretation to the negative sign.

A complementary variance-decomposition exercise provides a more conventional test of persistent sponsor-level variation. Sponsor fixed effects account for 28.8 percent of the variance in event-level responses, compared with a permutation median of 25.7 percent; the permutation -value is 0.26.

The two exercises therefore provide little support for a stable positive sponsor-specific component in hiring responses. This conclusion is more limited than saying that sponsors do not matter. Sponsor identity may affect outcomes through dimensions that are not stable across deals or cannot be estimated precisely in a sample with little repeat-deal information.

### E.5 Summary

The transaction and sponsor results provide context for the main state gradient rather than a competing explanation of comparable precision.

First, part of the simple control-transaction versus growth-investment difference reflects differences in the pre-deal condition of the targets entering those transactions.

Second, on the common 180-event sample, the observed transaction characteristics have less in-sample explanatory content than the pre-deal hiring state. The corresponding out-of-sample exercise, however, does not distinguish the two models reliably.

Third, the sponsor-identity exercises do not reveal a stable positive sponsor-level response component. The leave-one-out coefficient is negative and sensitive to influential observations, while the sponsor fixed-effect variance share is not unusual relative to its permutation benchmark.

These results are therefore consistent with the paper’s narrower conclusion: among the observable dimensions examined here, the target’s prior hiring condition is the clearest within-sample correlate of variation in the post-deal hiring response. The evidence does not rank that condition as the dominant economic determinant of private equity outcomes.

### Appendix F. Worker earnings and firm outcomes

The main text uses worker earnings and audited financial outcomes to provide economic context for the post-deal expansion in employment and hiring. These outcomes are secondary to the hiring-state analysis. They are also observed on different subsets of the matched sample: pension-based earnings are available relatively broadly, whereas audited financial statements select a smaller and generally larger set of firms.

This appendix first reports the worker-earnings measures moved from the former main-text table and then extends the audited firm outcomes over longer horizons. The financial results describe changes in scale and measured average outcomes; they do not identify the marginal productivity or profitability of additional workers.

### F.1 Worker earnings

The National Pension records report the contribution base used to calculate pension contributions. We use this measure to examine changes in assessed income per worker. Because the contribution base is subject to a statutory ceiling, it measures pensionable earnings rather than total compensation.

Across 346 events, average assessed income per worker rises by 0.0096 log points relative to matched controls [0.0039, 0.0154]. Employment expansion is therefore accompanied by a modest increase in measured earnings per worker rather than a comparable decline in the pension-recorded earnings measure.

A second measure asks what earnings are associated with newly added employment. The construction relates the change in payroll to the change in employment and normalises the resulting quantity by incumbent earnings. Because changes in incumbent wages also affect the numerator, the level of this constructed measure does not have a clean marginal-wage interpretation. We therefore interpret only its treated-control difference.

Across 182 events, the treated-control difference in the implied wage measure is 0.0086 [−0.1383, 0.1585]. The interval excludes a 20 percent discount relative to incumbent earnings, while smaller discounts—approximately 6.6 percent or less under the manuscript’s calibration—remain compatible with the estimates.

### Table F1. Worker earnings and one-year firm outcomes

### Panel A. Worker earnings

[TABLE #21]
| Outcome | Estimate | 95% CI | Events |
|---|---|---|---|
| Assessed income per worker, log | 0.0096 | [0.0039, 0.0154] | 346 |
| Implied wage measure for newly added employment | 0.0086 | [−0.1383, 0.1585] | 182 |

Panel B. Firm outcomes one year after the transaction

[TABLE #22]
| Outcome | Estimate | 95% CI | Events |
|---|---|---|---|
| Value added, log | 0.0778 | [0.0296, 0.1294] | 147 |
| Value added per worker, log | −0.0052 | [−0.0333, 0.0261] | 147 |
| Value added per unit of assets, log | −0.099 | [−0.177, −0.020] | [report N] |
| Return on assets | −0.008 | [−0.037, 0.024] | [report N] |

Notes. Assessed income is the National Pension contribution base and is top-coded at the statutory ceiling. The implied wage measure relates the change in payroll to the change in employment relative to incumbent earnings; only its treated-control difference is interpreted. Value added is defined as operating income plus payroll observed in the pension records. The ±0.10-log-point practical-equivalence range for value added per worker is specified in the main analysis. Exact event counts for value added per assets and return on assets should be inserted from the analysis output before submission.

### F.2 Value added and firm scale

Value added is constructed as operating income plus payroll observed in the pension records. One year after the transaction, value added is 0.0778 log points higher relative to matched controls [0.0296, 0.1294]. Value added per worker changes by −0.0052 log points [−0.0333, 0.0261], and the entire interval lies within the ±0.10-log-point practical-equivalence range used for this outcome.

The combination of these estimates describes an expansion in firm scale. Employment rises in the matched sample, and audited targets also record higher value added, while value added per worker remains close to its matched-control benchmark.

The existing appendix extends these outcomes to three years. The surviving source records the following point estimates:

### Table F2. Firm outcomes over three post-deal years

[TABLE #23]
| Outcome | +1 year | +2 years | +3 years |
|---|---|---|---|
| Log value added | +0.078 | +0.080 | +0.052 |
| Log value added per worker | −0.005 | −0.003 | +0.006 |
| Log assets | +0.227 | +0.180 | +0.240 |
| Survival | +0.006 | +0.009 | +0.007 |
| Events | 147 | [report N] | [report N] |

Notes. These are treated-minus-control estimates at the corresponding horizons. The archived appendix records the year-2 and year-3 point estimates but does not preserve their exact confidence intervals or event counts in the material inspected here. Those quantities should be restored from the analysis output before the table is finalised. The archived analysis records value added per worker as satisfying the specified equivalence criterion at all three horizons, but the exact year-2 and year-3 intervals should be reported rather than relying on that label alone.

Value added remains positive in point estimate through year three, although the archived results indicate less precise evidence by the third year. The value-added-per-worker point estimates remain close to zero throughout. Assets rise by 0.227, 0.180, and 0.240 log points at years one, two, and three, respectively.

This combination is more informative than describing value added alone. The audited firms expand both employment and their balance sheets, while measured value added per worker remains near its control benchmark. The evidence is consistent with an expansion in scale, but the outcomes do not provide a structural decomposition of why that expansion occurs.

### F.3 Value added relative to assets, revenue, and profitability

At the one-year horizon, value added per unit of assets falls by 0.099 log points [−0.177, −0.020]. The asset base therefore grows more rapidly than value added over this horizon.

This result should not be described as a decline in “productivity” without qualification. Assets and value added are accounting measures, and the analysis does not identify the marginal product of capital or separate physical productivity from changes in input composition, utilisation, accounting recognition, or other components of firm expansion. The safer interpretation is simply that measured assets expand faster than measured value added.

The existing appendix also reports that revenue remains close to the matched-control benchmark over the first three years. At the first two horizons, the revenue confidence intervals lie within a ±0.15-log-point practical-equivalence range. The exact point estimates and intervals are not available in the inspected source and should be restored before submission:

Revenue, +1 year: [report estimate and 95% CI]
Revenue, +2 years: [report estimate and 95% CI]
Revenue, +3 years: [report estimate and 95% CI]

Return on assets is estimated at −0.008 [−0.037, 0.024]. This interval contains zero and is too wide for the archived analysis to establish practical equivalence. The evidence therefore permits modest changes in profitability in either direction and does not support a precise zero-profitability-response interpretation.

These accounting outcomes also show why the main text should avoid language such as “the additional hires are profitable” or “labour productivity is unchanged” without qualification. The observed data support statements about measured value added, assets, earnings, and their ratios. They do not identify the return generated by an additional worker or unit of invested capital.

### F.4 Survival and longer-horizon sample composition

Survival outcomes require particular caution because disappearing from the panel need not mean economic failure. A private equity target may leave the observed sample following closure, acquisition, restructuring, or a successful sale. The pension data do not distinguish these events cleanly.

The archived three-year analysis reports treated-control survival differences of +0.006, +0.009, and +0.007 at years one, two, and three. Exact confidence intervals for these estimates should be restored from the analysis output before submission.

Extending the analysis to a fourth year changes the composition of the usable sample materially: approximately one-third of events are lost because they approach the end of the panel. At that horizon, the difference in survival between targets with lower and higher pre-deal hiring activity is −0.136 [−0.256, −0.029]. The corresponding state comparison is not separately detected at the other horizons, and adjustment for the four horizons examined gives a minimum multiplicity-adjusted -value of 0.074.

We therefore do not interpret the isolated fourth-year estimate as evidence that low-hiring targets are more likely to fail. It arises at the horizon with the greatest sample attrition, does not reproduce at the earlier horizons, and panel exit has no unique economic interpretation in this setting. The result is retained because it is an adverse longer-horizon diagnostic, not because it supports the main hiring-state claim.

### F.5 Sample selection and interpretation

The financial-statement analysis covers a different population from the primary hiring-state design. The one-year value-added analysis contains 147 events, compared with 286 events in the primary gradient sample. Firms with audited financial statements are generally larger, and we do not reweight the audited subsample to reproduce the distribution of the full matched population.

The worker-earnings results have broader coverage, but they also have measurement limits. Assessed income is top-coded, and the constructed marginal-wage measure is affected by incumbent wage changes. These outcomes therefore provide information about measured pensionable earnings rather than a complete measure of worker compensation or the wage received by a uniquely identifiable marginal hire.

Taken together, the secondary outcomes describe three features of post-deal expansion. Measured pensionable earnings per worker rise modestly. Among audited firms, value added and assets also rise, while value added per worker remains close to its control benchmark. Value added grows more slowly than assets at the one-year horizon. These patterns provide economic context for the employment and hiring results but do not distinguish financing, demand, governance, recruiting capacity, or other internal channels.

### Appendix G. Exploratory alternative designs

The analyses in this appendix use alternative comparison groups or post-treatment classifications that differ materially from the primary matched design. They were not assigned primary or secondary status and are not used to strengthen the causal interpretation of the main hiring-state gradient. Their role is to show what several intuitively useful alternative designs can and cannot resolve with the available data.

### G.1 Sponsor exits and reversibility

If the post-investment hiring response reflects a change associated with private equity ownership, one natural question is whether the response reverses when the sponsor exits. The shareholder records allow us to identify sponsor departures by tracking the holder that entered around the original transaction, after normalising shareholder names and grouping name variants within firms.

Only thirteen exits satisfy both requirements for this exercise: a verified sponsor departure and at least twelve months of post-exit pension data. For these events, the archived analysis reports an entry-period estimate of −0.0715 [−0.133, −0.009], an exit-period estimate of −0.008 [−0.119, 0.086], and a combined entry-plus-exit estimate of −0.079 [−0.212, 0.034].

### Table G1. Sponsor exits and reversibility

[TABLE #24]
| Estimate | Value | 95% CI |
|---|---|---|
| Entry-period effect | −0.0715 | [−0.133, −0.009] |
| Exit-period effect | −0.008 | [−0.119, 0.086] |
| Entry + exit | −0.079 | [−0.212, 0.034] |
| Minimum detectable effect | 0.194 | — |
| Usable sponsor exits | 13 | — |

Notes. Sponsor exits are identified from annual shareholder records by following the private equity holder that entered around the original transaction. An event must have a verified sponsor departure and at least twelve months of post-exit data. [Confirm the exact outcome represented by the entry and exit coefficients from the analysis output before submission.] The minimum detectable effect was calculated for the available exit sample.

The confidence interval for the combined entry-plus-exit estimate contains both zero and the original entry estimate. In economic terms, the data are therefore compatible both with a response that reverses after sponsor exit and with one that persists. The minimum detectable effect is 0.194, more than four times the magnitude of the entry estimate, making the thirteen-event sample too small to distinguish these alternatives.

We consequently use the exit analysis as a statement about lack of identifying power, rather than as evidence for either persistence or reversibility.

### G.2 Not-yet-treated firms as controls

The primary analysis uses never-treated firms as controls. An alternative is to compare a treated target with firms that eventually receive private equity investment but only sufficiently far in the future. Such firms may resemble current targets along dimensions that are difficult to observe, although the design requires enough temporal separation to avoid contamination by anticipation or impending treatment.

We implement this comparison using firms treated at least  months later, a size calliper, and five nearest neighbours. At , the archived probability statistic is −0.086 [−0.165, −0.007] in the original sample and −0.058 [−0.126, 0.008] in an expanded sample. Their difference is −0.029 [−0.130, 0.071]. The corresponding difference-in-differences estimate is not separately detected in either sample.

### Table G2. Not-yet-treated comparison at a 24-month treatment gap

[TABLE #25]
| Specification | Estimate | 95% CI |
|---|---|---|
| Original sample | −0.086 | [−0.165, −0.007] |
| Expanded sample | −0.058 | [−0.126, 0.008] |
| Difference between samples | −0.029 | [−0.130, 0.071] |

Notes. Controls are firms whose private equity treatment occurs at least 24 months after the focal event, selected using a size calliper and five nearest neighbours. [Confirm the exact definition and label of the “probability statistic” from the analysis output before submission.] The corresponding difference-in-differences estimates are not separately detected in either sample.

The exercise does not provide a sufficiently precise alternative estimate of the main treatment comparison. The result is sensitive to the available sample, and the difference-in-differences specification does not distinguish the treated and not-yet-treated groups with useful precision. We therefore do not use the not-yet-treated design either to support or to contradict the main never-treated comparison.

This limitation is worth reporting because the alternative comparison group is conceptually attractive. The problem is empirical support rather than the absence of a plausible motivation for the design.

### G.3 Non-private-equity ownership changes

A second alternative comparison asks whether similar labour-market changes occur around ownership transitions that do not involve private equity. We identify changes in the largest shareholder among firms never observed as private equity targets and exclude incoming holders whose names indicate a financial sponsor. The private equity and non-private-equity groups are processed using annual event timing and a common control pool that excludes firms experiencing any ownership change.

The non-private-equity ownership-change group exhibits little movement in the labour outcomes. Its estimated change in the no-hire outcome is 0.0050 [−0.007, 0.018], while the corresponding employment-level estimate is 0.002 [−0.017, 0.025].

### Table G3. Labour outcomes around non-private-equity ownership changes

[TABLE #26]
| Outcome | Estimate | 95% CI |
|---|---|---|
| No-hire outcome | 0.0050 | [−0.007, 0.018] |
| Employment level | 0.002 | [−0.017, 0.025] |
| Slope with transferred ownership stake | −0.000008 per pp | — |

Notes. Ownership changes are identified from annual shareholder records among firms never observed as private equity targets. Incoming holders whose names indicate a financial sponsor are excluded. The comparison uses annual event timing and a common control pool purged of firms with any ownership change.

The near-zero estimates make this comparison less informative than it first appears. A useful ownership-change benchmark would ideally generate economically meaningful organisational change while differing from private equity in the dimension of interest. Here, the comparison group shows little movement even in employment itself. The data therefore cannot establish whether these events represent consequential changes in effective control comparable with the private equity transactions.

Additional classifications do not resolve the problem. Estimates for six subgroups intended to isolate clearer transfers do not survive adjustment for the multiple subgroup comparisons. The outcome also shows essentially no relationship with the size of the transferred stake: the slope is −0.000008 per percentage point. Family successions, defined in the archived analysis by a common surname between outgoing and incoming holders, are not separately detected.

We therefore do not use the non-private-equity comparison to make a claim about which component of the observed labour response is unique to private equity.

### G.4 Post-deal cash and financial slack

The final exploratory exercise considers whether the hiring response is associated with changes in financial slack after investment. Cash as a share of assets rises by 0.033 in the deal year [0.010, 0.056] and does not show a corresponding increase afterward in the archived analysis. The cash increase also does not precede the hiring response.

We additionally split targets according to their post-deal change in cash. Firms in the bottom tercile of this cash-change distribution have an estimated response of −0.063 [−0.104, −0.019] on the archived outcome, which is not distinguishable from the corresponding estimate for the top tercile.

This comparison has a more fundamental limitation than sampling precision. Post-deal cash is itself potentially affected by the private equity transaction. Conditioning on its realised change therefore groups firms using a post-treatment variable and can induce selection through a collider. The resulting tercile comparison cannot be interpreted as estimating whether a capital injection causes the larger hiring response.

For that reason, we report the exercise only as a descriptive post-treatment association. It does not replace the pre-deal financial-variable comparisons discussed in the paper, and it is not used to infer that financial slack is or is not the internal mechanism behind the hiring response.

The exact top-tercile estimate and the precise outcome definition for the −0.063 estimate are not preserved in the inspected appendix text and should be restored from the analysis output rather than reconstructed.

### G.5 Interpretation

These alternative designs are useful mainly because their limitations are different from those of the primary analysis.

The exit analysis asks about reversibility but has only thirteen usable events and cannot distinguish persistence from reversal. The not-yet-treated design uses a potentially more comparable treatment population but lacks sufficient precision. The non-private-equity ownership-change group provides a conceptually appealing benchmark but exhibits almost no movement in the labour outcomes, making the economic content of the comparison uncertain. The cash split conditions on a post-treatment variable and therefore cannot support a causal mechanism interpretation.

None of these exercises provides a stronger counterfactual than the primary matched design. We retain them because they address natural alternative interpretations and because their weak or unresolved results define the limits of what the present data can establish.

### Appendix H. Supplementary monthly hiring hazard specifications

The main analysis measures hiring over twelve-month windows. As a supplementary specification, we also use the monthly panel to examine whether a target is more likely to record hiring after the private equity transaction, conditional on the time elapsed since its previous hire.

The hazard specification serves a descriptive purpose. Duration since the previous hire evolves as firms change their hiring behaviour after the transaction and is therefore itself potentially affected by treatment. Conditioning on that duration changes the estimand relative to the twelve-month matched comparisons in the main analysis. We consequently use the hazard model to describe monthly hiring activity rather than as an alternative estimate of the paper’s primary effect.

### H.1 Post-deal hiring hazard

The hazard sample contains 48,853 firm-month observations associated with the 379 baseline matched events. The specification includes event fixed effects and reports standard errors clustered by event. The archived analysis conditions on the number of months since the previous hire. [Before submission, insert the exact link function and the full coding of the duration controls from the analysis code.]

### Table H1. Supplementary monthly hiring hazard estimates

[TABLE #27]
| Specification | Hazard ratio | 95% CI |
|---|---|---|
| Post-deal hiring, treated relative to matched controls | 1.159 | [1.083, 1.241] |

Sample: 379 matched events; 48,853 firm-month observations.
Event fixed effects: Yes
Standard errors clustered by event: Yes
Conditions on months since previous hire: Yes

Notes. The outcome is the monthly hiring hazard. The reported hazard ratio compares the post-deal change for treated firms with the corresponding change among matched controls, conditional on the duration since the previous hire. The model includes 379 event fixed effects, and standard errors are clustered by event. The hazard sample contains 48,853 firm-month observations. Because duration since the previous hire evolves with post-transaction hiring, this is a conditional descriptive estimand and is not directly comparable with the twelve-month matched-difference estimates reported in Table 2. [Verify the exact model link, event-time controls, and duration-bin coding from the analysis output before finalising this note.]

The estimate implies a 15.9 percent higher conditional monthly hiring hazard after the transaction. This result is consistent with the average hiring-rate increase reported in the main text, but the two estimates answer different questions. The twelve-month hiring-rate estimate aggregates worker entries over fixed pre- and post-deal windows. The hazard model instead conditions on a variable—the time since the last hire—that changes as hiring occurs.

For this reason, we do not use the hazard ratio to quantify the magnitude of the primary hiring response or to compare effect sizes across pre-deal hiring states.

### H.2 The hiring-state interaction in the hazard model

The corrected matching design creates a particular limitation for using the hazard model to estimate the state-dependent response. In the primary design, the pre-deal hiring-state tercile enters the exact matching cell. As a result, state variation within a matched event is intentionally reduced. An estimator that identifies a treatment-by-state interaction primarily from within-event variation therefore loses information when applied to the corrected sample.

The archived discrete-time hazard analysis illustrates this trade-off. Under the earlier matching procedure, which did not exact-match on the hiring state, the treated-by-post-by-state interaction has a hazard ratio of 1.204 [1.021, 1.421]. Under the corrected state-balanced design, the corresponding continuous-state interaction is 1.507 [0.871, 2.609] across 1,199 grouped cells. The point estimate remains in the same direction but becomes much less precise. A tercile-based interaction cannot be separately estimated in the state-balanced specification because the state-tercile indicator is collinear with the event fixed effects.

### Table H2. State interaction in the monthly hazard specification

[TABLE #28]
| Matching design | State interaction, hazard ratio | 95% CI | Interpretation |
|---|---|---|---|
| Previous matching, state not exact-matched | 1.204 | [1.021, 1.421] | Positive interaction |
| State-balanced matching, continuous state | 1.507 | [0.871, 2.609] | Same direction, imprecise |
| State-balanced matching, state tercile | — | — | Not separately estimable with event fixed effects |

Notes. Entries report the treated-by-post-by-state interaction in the archived discrete-time hazard analysis. Under the primary matching design, state tercile is part of the exact matching cell and is therefore collinear with event fixed effects in a tercile-interaction specification. The corrected continuous-state interaction is estimated over 1,199 grouped cells. The monthly hazard interaction is not used as the paper’s primary state-gradient estimator.

This loss of precision is a consequence of the design correction rather than evidence against the state gradient. The primary matched-difference estimator was chosen precisely because it compares event-level responses across the target’s pre-deal state while allowing controls to be balanced on that same state. By contrast, the fixed-effect hazard specification places more weight on within-event variation that the state-balanced design intentionally removes.

The hazard results therefore play two limited roles. The average post-deal hazard ratio shows that hiring becomes more likely at monthly frequency, consistent with the average twelve-month hiring result. The interaction specification shows that the state-dependent direction is similar in the monthly model but is estimated too imprecisely under the corrected matching design to provide an independent test of the primary gradient.

### H.3 Interpretation

The monthly hazard analysis complements, rather than replaces, the main window-based estimands. Targets display a higher conditional probability of hiring after private equity investment, with a hazard ratio of 1.159 [1.083, 1.241]. The state interaction points in the same direction as the main state-gradient result, but the corrected design leaves insufficient within-event state variation for a precise hazard-based interaction estimate.

We therefore base the paper’s substantive conclusions on the matched twelve-month hiring-rate comparisons and use the hazard analysis only as supplementary evidence on monthly hiring activity.

