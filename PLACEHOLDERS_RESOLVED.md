# Placeholders in the submitted manuscript — resolved from the analysis artifacts

Every `[report N]`, `[confirm …]`, `[insert …]` in *Main Paper(PE Hiring).docx* / *Online Appendix.docx*, with the value or definition taken from the artifact that generated the surrounding numbers. Paths are `artifact.json:estimates.…`. One value in the manuscript is stale and must be corrected; see the end.

## Table F1, Panel B — event counts

- Value added per unit of assets, log: n = **146** (`I04c.json:estimates.panelA_value_added.va_pa|h1.n`); estimate -0.0990 [-0.1774, -0.0203] (n = 146)
- Return on assets: n = **155** (`…roa|h1.n`); estimate -0.0079 [-0.0373, 0.0236] (n = 155) — the manuscript's −0.008 [−0.037, 0.024] is this at 3 dp

## Table F2 — three post-deal years (estimates, 95% CIs, event counts)

| Outcome | +1 year | +2 years | +3 years |
|---|---|---|---|
| Log value added | +0.0778 [0.0296, 0.1294] (n = 147) | +0.0795 [0.0022, 0.1491] (n = 117) | +0.0519 [-0.0323, 0.1385] (n = 90) |
| Log value added per worker | -0.0052 [-0.0333, 0.0261] (n = 147) | -0.0030 [-0.0409, 0.0308] (n = 117) | +0.0060 [-0.0448, 0.0483] (n = 90) |
| Log assets | +0.2265 [0.1241, 0.3522] (n = 155) | +0.1796 [0.0643, 0.3032] (n = 123) | +0.2396 [0.0974, 0.3811] (n = 95) |
| Log revenue | -0.0191 [-0.1169, 0.0707] (n = 152) | +0.0009 [-0.1153, 0.1174] (n = 121) | +0.0622 [-0.0761, 0.2034] (n = 93) |
| Return on assets | -0.0079 [-0.0373, 0.0236] (n = 155) | -0.0131 [-0.0482, 0.0217] (n = 122) | +0.0265 [-0.0107, 0.0684] (n = 93) |
| Log value added per assets | -0.0990 [-0.1774, -0.0203] (n = 146) | -0.0811 [-0.1990, 0.0357] (n = 116) | -0.2046 [-0.3299, -0.0713] (n = 89) |

Source: `I04c.json:estimates.panelA_value_added.<outcome>|h<k>.{DiD,ci,n}`. Revenue rows fill the three `[report estimate and 95% CI]` lines in F.3; the ±0.15 equivalence statement holds at +1 and +2 (intervals inside ±0.15) and not at +3 ([-0.0761, 0.2034]).

### Survival rows (F2 / F.4)

- `I04c.json:estimates.panelD_survival.T3-T1|h4.ci` = [-0.2563, -0.0289]
- `I04c.json:estimates.panelD_survival.T3-T1|h4.diff` = -0.136
- `I04c.json:estimates.panelD_survival.T3-T1|h4.sig` = True

- State contrast at +4 years (F.4): `panelD_survival.T3-T1|h4` = -0.136 [-0.2563, -0.0289]

## Table D2 / D.2 — deployment-pressure variable (from `i36_regression_table.py`)

- Fund data: PitchBook fund file (Investor, Vintage, Close Date, Fund Strategy); PE funds = strategy matching Buyout|Growth|Mezzanine|Special|Turnaround|PE.
- Fund age at the deal = (deal month − most recent fund close month of the sponsor)/12; close month = Close Date, or vintage-year mid-year when Close Date is missing.
- **Pressure = indicator for the top tercile of that age; cut = 2.42 years** (`I36.json:estimates.pressure_cut_years`). Inaction tercile cut for the state interaction = 0.3333.
- Model: discrete-time complementary log-log on grouped binomial cells; event fixed effects (True), duration-bucket fixed effects (True: buckets of consecutive no-hire months before the observation), SE clustered by event; clusters 379, cells 4,686, firm-months 48,853, McFadden pseudo-R² 0.5059.
- Terms in specification (4): treated, post, treated x post, treated x pressure, post x pressure, treated x post x pressure. Triple interaction HR = 1.2881 [1.0535, 1.575].

## Table E1 — sponsor experience (from `i43_*.py`, Panel D)

- Experience = number of deals by the same sponsor in the treated universe (count per GP); terciles with cuts at [1.0, 4.0] deals → E1 (≤1) n=130, E2 n=99, E3 (>4) n=111; the table reports E3 − E1. No time window: the count is over all deals of that sponsor observed in the sample.

## Table H1 — hazard link and duration coding

- Link: complementary log-log (discrete-time hazard), grouped-binomial likelihood (likelihood-equivalent to the firm-month fit); duration = consecutive no-hire months preceding the observation, entered as bucket fixed effects; event FE; SE clustered by event (`I36.json:estimates.specs.(2)`).

## Table G1 — exit coefficients (from `i05_exit_reversal.py`)

- Outcome: twelve-month share of no-hire months (the paper's 'inaction' outcome), treated − matched controls. Exit events are re-matched at the exit month with the same never-treated cell + 5-NN procedure; the entry-period coefficient is the same outcome around the original entry for the same 13 firms; 'entry + exit' is their sum per firm.
- `I05.json:estimates.panelB_entry_exit_pairs`: entry {'mean': -0.0715, 'ci': [-0.1328, -0.0093], 'sig': True}, exit {'mean': -0.0077, 'ci': [-0.1192, 0.0859], 'sig': False}, sum {'mean': -0.0792, 'ci': [-0.2122, 0.0338], 'sig': False}; MDE at n=13: 0.194. (Public copy of I05.json has firm identifiers removed.)

## Table G2 — the 'probability statistic' P1 (from `h39_common.summ` via `i06_notyet_anatomy.py`)

- P1 = Pr(Δ outcome < 0 | treated) − Pr(Δ outcome < 0 | matched not-yet-treated controls), i.e. the treated–control difference in the share of events whose no-hire-month share falls from the pre- to the post-window. DiD is the mean difference in the same outcome.
- `I06.json:estimates.panelA_specs`: S1 (original treated, original pool) P1 = -0.0863 [-0.1653, -0.0069] (n 186); S4 (expanded, expanded) P1 = -0.0577 [-0.1257, 0.0081] (n 256); difference `panelC_collapse_test.G24.P1_diff` = -0.0287 [-0.1295, 0.0713].

## G.4 — cash split (from `i21_cash_lead.py`)

- Outcome: twelve-month no-hire-share DiD. Bottom tercile of post-deal cash change (C1): -0.0631 [-0.1038, -0.0194] (n 61); top tercile (C3): -0.0553 [-0.1019, -0.0092] (n 60); difference 0.0079 [-0.0551, 0.0671].
- Cash/assets rise in the deal year: 0.0327 [0.0104, 0.0562] (n 194); +1: 0.0215 [-0.0024, 0.0483]; +2: 0.0179 [-0.0108, 0.0494].

## Table H2 — state interaction under the two designs

- Previous matching (state not in the exact-matching cell): `I25.json:estimates.panelD_hazard_triple.tp_hi` HR 1.204 [1.0205, 1.4205]. I25 was run on 2026-08-24 on the expanded treated sample (752/379); the hazard panel uses the 308 events with a pre-pre state measurement, 3,919 grouped cells, 41,303 firm-months (`panelD_hazard_triple.{n_ev_fe,n_cells,n_firm_months}`). 'Previous' refers to the matching procedure, not to an earlier sample — the row is correctly traceable and needs no change; consider adding the 308-event count to the table note.
- State-balanced, continuous state: `I57.json:estimates.panelA_hazard_triple.연속 S` HR 1.5074 [0.871, 2.6087], grouped cells 1199.

## Table E4 — variance decomposition

- `I17.json:estimates.panelB_variance`: sponsor fixed-effect share 0.2875 (manuscript 28.8%), permutation median 0.2571 (25.7%), permutation p 0.2605 (0.26).

## Value that must be corrected in the .docx

1. **Table E4 'Covariate-adjusted response −0.2261' → −0.2496.** The covariate-adjusted leave-one-out coefficient in the artifact is `I45.json:estimates.panelE_gp_loo_robustness.loo_on_adjusted_residual` = −0.2496 (run 2026-08-25, final covariate set: pre-deal hiring state S, log size, pre-deal growth, age, one-digit industry, deal year — the same set as Table E3's 'adjusted' rows). The −0.2261 in the manuscript is the value from an earlier run with the pre-I47 covariate set, carried over from internal ledger prose; no artifact contains it. The other four E4 rows (−0.2675, −0.2659, −0.2387, −0.1751) match the artifact. The E.4 prose sentence 'computing it on the covariate-adjusted residual gives −0.2261' must change likewise. The confirmatory re-run of `i45_power_invariance.py` is recorded in `artifacts/I45_rerun_check.json`.
2. **Table H2** — no change (see above; my earlier flag that I25 was a pre-expansion artifact was wrong).

## Editorial

- §3.2: 'primary gradienct sample' → 'gradient'.
- Table 1, Panel C header lost its formula in the .docx→text extraction used here; the .docx itself is unaffected.
