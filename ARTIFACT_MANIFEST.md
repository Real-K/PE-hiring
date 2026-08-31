# Artifact manifest

Aggregate result files in `artifacts/`; `Feeds` lists the submitted-manuscript tables whose cells read from the file (from `EXHIBIT_MAP.csv`). `I05.json` is a public copy with firm identifiers removed. `I45_rerun_check.json` records the 2026-08-31 confirmatory re-run behind the Table E4 correction.

| Artifact | sha256₁₆ | Bytes | Pipeline script | Feeds |
|---|---|---:|---|---|
| `I01.json` | `5780c45ca931b2b9` | 3,538 | `i01_timeagg.py` | — |
| `I02.json` | `582b04b1e3a78e04` | 6,518 | `i02_hazard.py` | — |
| `I03.json` | `db70361a6d437c6f` | 3,985 | `i03_ss_band.py` | — |
| `I04.json` | `7f87b84efb4972a2` | 11,468 | `i04_performance.py` | Main Table 1 |
| `I04b.json` | `94f17e7e266ef4b9` | 14,402 | `i04b_performance_v2.py` | — |
| `I04c.json` | `3da40abb54aabe7a` | 14,694 | `i04c_valueadded.py` | Main Table 1, OA Table F1, OA Table F2 |
| `I05.json` | `d2fefac444fa5209` | 3,918 | `i05_exit_reversal.py` | OA Table G1 |
| `I05a.json` | `55fced24357fb7c3` | 1,500 | `i05a_exit_refine.py` | — |
| `I06.json` | `27038f2628daacaa` | 6,699 | `i06_notyet_anatomy.py` | OA Table G2 |
| `I11.json` | `93e2d0fb8ebfb26c` | 3,999 | `i11_honestdid.py` | OA Table D4 |
| `I14.json` | `6b8f8f3cba88c4ac` | 7,095 | `i14_shareholder_dose.py` | OA Table D2 |
| `I15.json` | `0d9f102eb6cafa73` | 3,862 | `i15_fund_pressure.py` | — |
| `I16.json` | `521afc447557117e` | 6,782 | `i16_dealtype.py` | — |
| `I17.json` | `3b988ff9a3a8c37c` | 2,686 | `i17_gp_style.py` | — |
| `I19.json` | `cb16a708ea98533e` | 5,261 | `i19_succession.py` | OA Table G3 |
| `I19b.json` | `e217efd628db4388` | 4,433 | `i19b_own_subtypes.py` | — |
| `I19c.json` | `48fd8d451913ed48` | 3,005 | `i19c_dose_gradient.py` | OA Table G3 |
| `I21.json` | `6b3c72ab246e5e67` | 3,006 | `i21_cash_lead.py` | — |
| `I22.json` | `dc45a7e680142d59` | 4,115 | `i22_wage_structure.py` | OA Table F1 |
| `I25.json` | `0f8c5b0461ccfac8` | 6,732 | `i25_pre_inertia.py` | OA Table H2 |
| `I31.json` | `0a9d85b94070b291` | 6,178 | `i31_inertia_placebo.py` | — |
| `I32.json` | `90c4b64dbca095f2` | 6,628 | `i32_decay.py` | — |
| `I33.json` | `603470c6b778cad1` | 4,231 | `i33_linchpin.py` | — |
| `I34.json` | `af60923e4af98d4f` | 2,656 | `i34_margin_decomp.py` | — |
| `I35.json` | `c9f1c40df4def371` | 4,747 | `i35_canonical.py` | Main Table 1, Main Table 2, OA Table A2 |
| `I36.json` | `9d23770592a7a7de` | 6,579 | `i36_regression_table.py` | Main Table 1, OA Table D2, OA Table H1 |
| `I37.json` | `951d1151ed939593` | 2,685 | `i37_balance.py` | Main Table 1 |
| `I38.json` | `424a138113200850` | 4,321 | `i38_excess_zeros.py` | Main Table 6, OA Table A1 |
| `I39.json` | `23d61216468e66e1` | 4,206 | `i39_spell_benchmark.py` | OA Table A1, OA Table G3 |
| `I40.json` | `cf1157fa0119ef38` | 4,085 | `i40_salvage.py` | Main Table 1, OA Table A1 |
| `I41.json` | `b06cc9df9d81cea7` | 3,307 | `i41_moderator_defense.py` | OA Table B2 |
| `I41_RECLASS.json` | `810417eed5ad035d` | 3,704 | `` | — |
| `I42.json` | `931e5464a2641c0d` | 1,841 | `i42_placebo_lograte.py` | — |
| `I43.json` | `05e25cfb4ea2f29c` | 4,900 | `i43_invariance_lograte.py` | — |
| `I44.json` | `7e893dccc627d316` | 5,795 | `i44_state_variable.py` | OA Table B2 |
| `I45.json` | `ca7e0e559cd38c48` | 6,598 | `i45_power_invariance.py` | OA Table E1, OA Table E2, OA Table E3, OA Table E4, OA Table G3 |
| `I45_rerun_check.json` | `fe1e0f02a44a4143` | 1,106 | `i45_power_invariance.py` | — |
| `I46.json` | `0c3065edbfbadd7b` | 9,936 | `i46_state_vs_volume.py` | — |
| `I47.json` | `f772a3eba5697770` | 10,732 | `i47_state_final.py` | OA Table B1 |
| `I48.json` | `30cab17b5d6b8f25` | 3,782 | `i48_construct_validity.py` | Main Table 1, OA Table C1, OA Table C2 |
| `I49.json` | `5f41571a977336b3` | 5,083 | `i49_reuse_and_finance.py` | — |
| `I50.json` | `9ae2ca62aea4bc0c` | 5,738 | `i50_power.py` | — |
| `I50_panelH.json` | `17ee8c96eb8ea26e` | 349 | `` | — |
| `I51.json` | `3f331e65e54ffe1a` | 2,391 | `i51_spec_adjudication.py` | — |
| `I52.json` | `83b5474d8bb49853` | 4,655 | `i52_headline_final.py` | — |
| `I53.json` | `1f8ed3bf680363e8` | 2,938 | `i53_randomization.py` | Main Table 1 |
| `I54.json` | `5c94d61cfabeeca3` | 3,319 | `i54_limits.py` | — |
| `I55.json` | `338ac07afe0df07f` | 3,550 | `i55_reallocation.py` | — |
| `I55_employment_horizons.json` | `6fa4b2cab9e6b5d0` | 943 | `(inline, 원장 §41-3)` | — |
| `I56.json` | `26af115be7ce9d4a` | 5,626 | `i56_efficiency.py` | OA Table B4 |
| `I57.json` | `d8fc51f6ea86fbe8` | 5,275 | `i57_reallocation2.py` | Main Table 3, Main Table 4, OA Table C4, OA Table H2 |
| `I57_levels.json` | `5d1968ab781ff148` | 932 | `` | OA Table C3 |
| `I58.json` | `8e2e54ce180fab92` | 2,509 | `i58_design_audit.py` | Main Table 1, Main Table 3 |
| `I58_control_contamination.json` | `01d679757aa751c7` | 659 | `` | Main Table 1 |
| `I59.json` | `530a4c2d2a1c8af5` | 1,126 | `` | Main Table 3 |
| `I60.json` | `9ce11e1e40eabe79` | 2,598 | `i60_speccurve.py` | Main Table 3, OA Table B3, OA Table B4, OA Table C2 |
| `I61.json` | `fbd921816ffd5a02` | 3,720 | `i61_gradient_pretrend.py` | OA Table D1 |
| `I62.json` | `99790e69bc872ae3` | 3,580 | `i62_power3.py` | OA Table B4 |
| `I63.json` | `8e51349f0c9d1294` | 3,575 | `i63_sample_expansion.py` | OA Table B4 |
| `I64.json` | `ed1df01b02ecb3f4` | 1,914 | `i64_pretrend_honest.py` | Main Table 5, OA Table D4 |
| `I65.json` | `3da372c82a53ce5d` | 2,832 | `i65_bootci_reuse.py` | Main Table 3, OA Table C2, OA Table D2, OA Table D3 |
| `I66.json` | `f0ffd76d7dd90f5d` | 3,429 | `i66_pretrend_zeros.py` | Main Table 5, OA Table B2, OA Table B3 |
| `I67.json` | `67e86ce7fe5489c8` | 1,963 | `i67_emp_horizons.py` | OA Table C4 |
| `I68.json` | `3b75315a55917528` | 3,316 | `i68_hiring_rate_es.py` | — |
| `I69.json` | `9eea16a0120a0bda` | 2,230 | `i69_sample_flow.py` | — |
| `I70.json` | `076f13d9cdd89fea` | 72,159 | `i70_fig_balance.py` | — |
| `I71.json` | `87b7c4243d38e410` | 3,337 | `i71_gp_prior.py` | — |
| `I72.json` | `92a98304ef2c0539` | 2,338 | `i72_fin_het.py` | — |
| `I73.json` | `5130e3209ece8556` | 2,285 | `i73_decomp_e2.py` | — |
| `h41_causal_gap.json` | `31b201a9dd5b8680` | 13,913 | `` | — |
