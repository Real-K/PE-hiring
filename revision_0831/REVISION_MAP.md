# Exhibit revision map — 0831 review memo → rebuilt tables and figures

Source memo: `paper_v4/submission/PI Writing Version v0.2/PE Hiring 0831_comment.md`. Everything below is built by
`build_tables.py` / `build_figure1.py` / `build_figure2.py` in this folder from `../artifacts/` only; every numeric
cell is listed in `REVISION_TRACE.csv` with its artifact path. New analyses were run as pipeline scripts
`i70_fig_balance.py`, `i71_gp_prior.py`, `i72_fin_het.py` (in `../pipeline/`, artifacts `I70/I71/I72.json`,
claims V01–V10 in the ledger).

| Memo § | Directive | Delivered | Sources |
|---|---|---|---|
| Part 3 §9 | Table 1 re-tabulation: funnel + parallel branches + **balance on the primary 286 sample** | `main_exhibits.md` Table 1 (Panel C newly computed) | I48, I35, I63, I65, I45, I37, **I70** |
| Part 4 §4 | Table 2 simplified, "changes relative to matched controls" | Table 2 | I35 |
| Part 4 §6–7, §26–27 | Figure 1 split; panel (b) must show the **actual 2,000 draws**, not a normal density | `figure1_state_gradient.png/.pdf` | **I70** (draws stored in the artifact) |
| Part 4 §10 | Table 3: Panel A + winsorised design comparison + unwinsorised control-path diagnostic, clearly separated; two-sided empirical p | Table 3 | I65, I70, I60, I58 |
| Part 4 §11, §18–19 | Old Table 3 Panel C moves to Table 4; Table 4 rebuilt with denominator check first, real p columns | Table 4 | I59, I57 |
| Part 5 §8–10 | Table 5 simplified to three pre/post diagnostics; Rambachan–Roth row removed from the main table (detail stays in Appendix D) | Table 5 | I66, I64 |
| Part 6 §4, §27 | Table 6 deleted from the main paper (content remains Appendix Table A1) | — (no build needed) | — |
| Part 6 §3 | Old Figure 1(a) becomes Figure 2; per-quarter significance markers removed | `figure2_quarterly.png/.pdf` | I68 |
| Part 6 §10–11, §33 | Sponsor experience rebuilt as **prior deal count at the transaction date**; E1–E3 re-estimated; "forecasting" framing dropped | `appendix_exhibits.md` E1/E2–E3 (revised) | **I71** |
| Part 5 §33 | New Table B5: pre-deal financial condition vs the hiring-response heterogeneity, with the state on the same audited sample | `appendix_exhibits.md` Table B5 | **I72** |

## Results of the new analyses (summary)

- **I70**: primary gradient reproduced exactly (0.7101); the 2,000 actual pseudo-sample gradients have mean 0.1010, SD 0.1538,
  empirical central 95% [−0.1835, 0.4082] — identical moments to the Table 3 source run (I60); upper-tail p 0.0005, two-sided p 0.001.
  Balance on the 286 sample: largest |normalised difference| = 0.168 (firm age); state ND −0.039.
- **I71**: 52.8% of events are the sponsor's first observed deal; ≥4-prior − first-deal contrast −0.0118 [−0.2193, 0.2195] — still no
  experience gradient. Joint deal-characteristic R² falls to 0.0054 (permutation p 0.814) vs state 0.0286 (p 0.022); held-out
  state − deal difference +0.0287 [−0.028, 0.115]. All prior conclusions survive the look-ahead fix.
- **I72**: none of cash/assets, leverage, interest coverage, ROA predicts the response (0/4 significant), while the hiring state on the
  **same audited sample** remains predictive: +0.1087 [0.0229, 0.1964] per SD (n 169) — the sample-vs-variable separation the memo asked for.

## Flags for the PI (decide before pasting into the manuscript)

1. **Pseudo-event pool size wording.** The pool differs slightly across placebo implementations: 1,205 (I70/I58 design, used by Figure 1(b)
   and Table 3), 1,246 (I57), 1,244 (I66). The manuscript prose currently says "1,246". Either cite the per-run count next to each exhibit
   or write "approximately 1,200". The null moments used in Table 3/Figure 1 are the I70 run (= I60 exactly).
2. **State-balance ND convention.** Rebuilt Table 1 Panel C reports the pooled-controls normalised difference (state ND −0.039), consistent
   with the covariate rows. The current manuscript's −0.0078 is the paired (event-mean) convention from I58. Both are correct; pick one and
   say which in the note.
3. **Reference means differ in the 4th decimal across per-outcome placebo runs** (Table 4 Panel A ref 0.1012 from I59 vs Table 3's 0.1010
   from I70/I60). The Table 4 note states that reference distributions are re-estimated per outcome.
4. **Adopting the rebuilt experience variable changes Appendix E numbers** (in-sample R² 0.0092→0.0054, permutation p 0.642→0.814; held-out
   difference +0.0101→+0.0287). Conclusions are unchanged; swap the E2/E3 cells when the variable is adopted.
5. Previous round's pending docx edits remain: Table E4 −0.2261 → −0.2496; §3.2 "gradienct".
