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

## 2026-08-31 (2차) — placeholder 원고 채움에서 발생한 결과 변경·플래그

6. **양측 p 관행 통일**: 원고 §4.3의 선언(중심화·직접계산)에 맞춰 i57/i59/i60/i62/i63/i56/i66 산출물에 `RI_p_two_centered`를 추가(기존 수치·rng 순서 보존, 동일 seed 재실행). 표 3·4·B3·B4·C2의 p는 전부 중심화 값.
7. **F3(생존) 결론 변경**: 재계산한 Šidák(양측 부트스트랩 p, 4개 지평) 최소 p = **0.0394** — 이전 프로즈의 0.074와 다르며, +48개월 대비는 조정 후에도 검출됨. "does not survive" 문장을 교체했고 절차를 노트에 명시함(`I04c.json:panelD_survival.multiplicity`).
8. **표 4 Panel A 참조평균 갱신**: lN/lN_ctrlE를 I57 실행으로 통일(관측 0.6315/0.6957 동일, 참조 0.1858/0.0377) — I59와 4째 자리 차이는 위약 재추출 때문.
9. **B1 문장 교정**: "≥12건 표본, 물량 조건부" 값은 −0.3426(조건부)·+0.0101(무조건) — 기존 프로즈의 0.010은 무조건 값이었음. 두 값을 구분해 기재.
10. **D2/D6 구현 명시**: 12개월 RR(사전 최대 0.1068, 사후 0.7250 SE 0.1995, M̄ 3.126)·분기(0.1259/0.0711/0.0871, M̄ 0)·평균효과(I11 S4: 사전 최대 0.0154, θ 0.046 SE 0.0105, M̄ 0.658).
11. **E1–E3 재구축치**: prior-count 조정 기울기 +0.0622 [−0.0665, 0.1820], 상−하 +0.1139 [−0.0461, 0.2947]; 스폰서 분포: 총 206개 중 1건 144 · 2건 29 · ≥3건 33, 최다 14건 (I73).
12. 채움 전수 기록: `FILL_TRACE.csv` (157+ 치환), 검증: 채움 후 원고 소수 토큰 1,050개 전수 산출물 풀 추적(미매칭 = 6자리 지분 기울기 표기 2건·DOI 1건뿐).

## 2026-08-31 (3차) — 22:00 판 placeholder 채움

- 대상: `Paper+Appendix(w.placeholder)_0831_2200.md` (PI 대폭 재작성판, placeholder 151개) → **101건 치환, 잔여 0** (`FILL_TRACE_2200.csv`; 채움본 사본 `paper_exhibits/Paper+Appendix_2200_filled_2026-08-31.md`). 소수 토큰 1,196개 전수 풀 추적.
- 신규 분석: **I74** (`i74_g18_gap.py`) — not-yet-treated 최소간격 18개월(별도 seed, I06 인쇄값 재현성 보존: G18 삽입 시 부트 CI가 밀리는 것을 확인하고 i06을 원상복구); **I38 확장** — 상태별 초과 무채용을 고용가중 벤치마크로 재산출(T3 +0.0047 · T1 +0.0013 · 차 +0.0034, 원고의 균등 기반 수치와 병기).
- 서식 통일(3차): 표 1 Panel C·B3·B4·G3을 4dp로 재구성, p 셀 4dp(0.0020/0.0050/0.0010), 표 행 마이너스 68행 정규화, 3dp→4dp 자동 승격 9건(풀에서 4째 자리가 실재하는 유일 매칭만; 원천 3dp인 1.204·3.126은 유지).
- ⚠ PI 확인: **G3 'Employment level 0.002 [−0.017, 0.025]' 행은 현행 산출물에 없음**(구세대 I19 계열 잔재로 추정; 현행 I19은 무채용 결과만 산출). 재계산하거나 행 삭제 필요 — no-entry 행은 I19 정본으로 4dp 갱신 완료(0.0050 [−0.0066, 0.0176], n 1,191).
- 그림 1(b) 풀 표기를 1,246 → 1,205(I70 실행 풀)로 교정.
