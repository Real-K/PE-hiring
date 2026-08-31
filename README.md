# Private Equity and State-Dependent Hiring — code for the submitted manuscript

Analysis code and aggregate result artifacts behind the submitted manuscript (main paper, 6 tables + 1 figure; online appendix, 28 tables + 1 figure). The folder is organised **by document**: everything the main text reports is regenerated under `main_paper/`, everything the online appendix reports under `online_appendix/`.

## Start here — the notebooks render on GitHub

| | Main paper | Online appendix |
|---|---|---|
| Tables, regenerated and checked cell-by-cell against the submitted .docx | [`main_paper/01_tables.ipynb`](main_paper/01_tables.ipynb) | [`online_appendix/01_tables.ipynb`](online_appendix/01_tables.ipynb) |
| Figure, regenerated and checked by SHA-256 against the image in the .docx | [`main_paper/02_figure.ipynb`](main_paper/02_figure.ipynb) (Figure 1) | [`online_appendix/02_figure.ipynb`](online_appendix/02_figure.ipynb) (Figure C1) |
| Traceability: every table cell and every prose number → artifact | [`main_paper/03_traceability.ipynb`](main_paper/03_traceability.ipynb) | [`online_appendix/03_traceability.ipynb`](online_appendix/03_traceability.ipynb) |

Outputs are stored in the notebooks. Each reads only `artifacts/` (aggregate JSON + the claims ledger); no licensed microdata is used or required.

## Revised exhibits (0831 review memo) — `revision_0831/`

The PI's 2026-08-31 review memo restructures the main paper to 5 tables + 2 figures and asks for three new analyses.
`revision_0831/` builds all of it from artifacts: rebuilt Tables 1–5 (`main_exhibits.md`), the new two-panel Figure 1
(event-level state–response scatter + the **actual** 2,000 placebo draws), Figure 2 (quarterly dynamics), the rebuilt
sponsor-experience tables and the new Table B5 (`appendix_exhibits.md`). New pipeline runs: `i70_fig_balance.py`,
`i71_gp_prior.py`, `i72_fin_het.py` → `I70/I71/I72.json`. Start at
[`revision_0831/00_revised_exhibits.ipynb`](revision_0831/00_revised_exhibits.ipynb); the memo-to-exhibit mapping and
open decisions are in [`revision_0831/REVISION_MAP.md`](revision_0831/REVISION_MAP.md). Cell-level traceability:
`revision_0831/REVISION_TRACE.csv` (148 cells). `paper_exhibits/*_0831.md` are the extracted reference copies of the
0831 manuscript build (its 895 decimal tokens all trace to the artifact pool).

## How the check works

`spec/*.json` records, for every cell of every table in the submitted manuscript, the numeric tokens it contains and the artifact field (or claims-ledger claim) each token comes from. `code/render.py` rebuilds each cell by formatting the source value exactly as the manuscript prints it and compares the result with the cell text extracted from the .docx. Result at build time: **143 main-text and 331 appendix table tokens mapped; 393 numeric cells checked; 0 mismatches; 1 untraceable literal** (Table E4, see `PLACEHOLDERS_RESOLVED.md`). Both figures regenerate byte-identical to the images embedded in the .docx files.

## What is here

```
main_paper/        build_tables.py · build_figure1.py · tables.md · CHECK_REPORT.md · figure1_event_study.png/pdf · 3 notebooks
online_appendix/   build_tables.py · build_figureC1.py · tables.md · CHECK_REPORT.md · figure2_turnover.png/pdf · 3 notebooks
spec/              main_tables.json · appendix_tables.json — cell-level source map (the single source of truth for the tables)
code/              render.py (renderer + checker) · build_notebooks.py · make_notebooks.py
artifacts/         65 aggregate result files + CLAIMS_LEDGER.csv
pipeline/          the full analysis pipeline, i01 … i69 + shared loaders (requires licensed inputs; see DATA_ACCESS.md)
paper_exhibits/    tables and figures extracted from the submitted .docx — the reference the checks compare against
EXHIBIT_MAP.csv    table · panel · row · token → claim id · artifact path · generating pipeline script
TEXT_NUMBERS.csv   every number in the prose (References excluded) → source
PLACEHOLDERS_RESOLVED.md   values and definitions for the manuscript's [report N] / [confirm …] placeholders, and the one value to correct
ARTIFACT_MANIFEST.md · DATA_ACCESS.md · LICENSE
```

## Rebuilding

```bash
python3 main_paper/build_tables.py && python3 online_appendix/build_tables.py     # exit 1 on any cell mismatch
python3 main_paper/build_figure1.py && python3 online_appendix/build_figureC1.py
python3 code/make_exhibit_map.py && python3 code/make_notebooks.py                 # rebuild exhibit map, manifest, notebooks
```
Python 3.11+, numpy, matplotlib. Set `P014_ARTIFACTS` to point elsewhere if the artifacts are moved.

## Pipeline scripts feeding the reported tables

`i04_performance.py`, `i04c_valueadded.py`, `i05_exit_reversal.py`, `i06_notyet_anatomy.py`, `i11_honestdid.py`, `i14_shareholder_dose.py`, `i19_succession.py`, `i19c_dose_gradient.py`, `i22_wage_structure.py`, `i25_pre_inertia.py`, `i35_canonical.py`, `i36_regression_table.py`, `i37_balance.py`, `i38_excess_zeros.py`, `i39_spell_benchmark.py`, `i40_salvage.py`, `i41_moderator_defense.py`, `i44_state_variable.py`, `i45_power_invariance.py`, `i47_state_final.py`, `i48_construct_validity.py`, `i53_randomization.py`, `i56_efficiency.py`, `i57_reallocation2.py`, `i58_design_audit.py`, `i60_speccurve.py`, `i61_gradient_pretrend.py`, `i62_power3.py`, `i63_sample_expansion.py`, `i64_pretrend_honest.py`, `i65_bootci_reuse.py`, `i66_pretrend_zeros.py`, `i67_emp_horizons.py` — each writes one artifact in `artifacts/` (the `code` and `sha256_16` fields inside each file identify the script and its hash at run time). Scripts are numbered in the order they were written; `pipeline/CODE_INDEX.md` describes each.

## Licence
MIT. Citation details to be added on publication.
