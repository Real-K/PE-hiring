# -*- coding: utf-8 -*-
"""I-72 사전 재무상태 × 채용반응 이질성 (표 B5) — PI 0831 코멘트 Part 5 §33.

거래 전 회계연도(딜연도−1)의 현금/자산·레버리지(부채/자산)·이자보상배율(영업이익/이자비용)·ROA 를
표준화해 이벤트 수준 반응(eff)에 대한 기울기를 추정하고, **같은 감사표본에서 상태 S 기울기**를 함께 보고한다
(표본효과와 변수효과의 분리 — 코멘트 §33 의 핵심 행).

규칙: 모든 재무 측정치는 표본 내 1/99 백분위로 일괄 클립 후 z-표준화(변수별 튜닝 없음).
결과 y 는 I-47 관행대로 비winsor. i47_state_final.py 를 Panel A 마커까지 실행해 U·slope_ci 재사용.
"""
import os, re, gc
import numpy as np, pandas as pd
from h30_common import emit, BASE

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "i47_state_final.py"), encoding="utf-8").read()
i = src.find("[Panel A] FWL")
ns = {"__name__": "i72_reuse"}
exec(compile(src[:src.rfind("\n", 0, i)], "i47_state_final.py(head)", "exec"), ns)
U, y, slope_ci, rng = ns["U"], ns["y"], ns["slope_ci"], ns["rng"]

FINPATH = BASE + re.search(r'f"\{BASE\}(/[^"]+_통합\.csv)"', open(os.path.join(HERE, "i21_cash_lead.py"), encoding="utf-8").read()).group(1)
NEED = ["사업자등록번호", "회계연도", "분기", "자산총계(천원)", "현금및현금성자산(천원)",
        "부채총계(천원)", "이자비용(천원)", "영업이익(천원)"]
BNS = {e["bn"] for e in U}
parts = []
for ch in pd.read_csv(FINPATH, usecols=NEED, dtype=str, chunksize=200_000):
    ch = ch[ch["분기"].astype(str).str.contains("결산", na=False)]
    ch["bn10"] = ch["사업자등록번호"].str.replace(r"\D", "", regex=True).str.zfill(10)
    parts.append(ch[ch.bn10.isin(BNS)])
F = pd.concat(parts, ignore_index=True); del parts; gc.collect()
F["yr"] = pd.to_numeric(F["회계연도"], errors="coerce")
for c, k in (("자산총계(천원)", "asset"), ("현금및현금성자산(천원)", "cash"), ("부채총계(천원)", "debt"),
             ("이자비용(천원)", "intexp"), ("영업이익(천원)", "op")):
    F[k] = pd.to_numeric(F[c], errors="coerce")
F = F[F.yr.notna()].drop_duplicates(["bn10", "yr"])
FIN = {(r.bn10, int(r.yr)): (r.asset, r.cash, r.debt, r.intexp, r.op) for r in F.itertuples()}
print(f"[I-72] 재무 {len(F):,}행 · 대상기업 {F.bn10.nunique():,}")

MEAS = {"cash_assets": "현금/자산", "leverage": "부채/자산", "coverage": "영업이익/이자비용", "roa": "ROA(영업이익/자산)"}
X = {k: np.full(len(U), np.nan) for k in MEAS}
for j, e in enumerate(U):
    yr0 = (e["m0"] - 1) // 12
    f = FIN.get((e["bn"], yr0 - 1))
    if not f: continue
    A_, C_, D_, I_, P_ = f
    if np.isfinite(A_) and A_ > 0:
        if np.isfinite(C_) and C_ >= 0: X["cash_assets"][j] = C_ / A_
        if np.isfinite(D_) and D_ >= 0: X["leverage"][j] = D_ / A_
        if np.isfinite(P_): X["roa"][j] = float(np.clip(P_ / A_, -1, 1))
    if np.isfinite(P_) and np.isfinite(I_) and I_ > 0: X["coverage"][j] = P_ / I_
S = -np.array([e["S"]["lr"] for e in U])

def zclip(v, m):
    lo, hi = np.percentile(v[m], [1, 99]); w = np.clip(v, lo, hi)
    return (w - w[m].mean()) / w[m].std()

EST = {}
for k, lab in MEAS.items():
    m = np.isfinite(X[k])
    EST[k] = dict(label=lab, **slope_ci(zclip(X[k], m)[m], y[m]))
    print(f"  {lab:<22} 기울기/SD {EST[k]['slope']:+.4f} {EST[k]['ci']} n={EST[k]['n']}")
m4 = np.isfinite(X["cash_assets"]) & np.isfinite(X["leverage"]) & np.isfinite(X["roa"])
mall = m4 & np.isfinite(X["coverage"])
mc = mall if mall.sum() >= 100 else m4
tag = "cash·lev·cov·roa 공통" if mall.sum() >= 100 else "cash·lev·roa 공통(coverage 표본 부족)"
EST["state_common"] = dict(label=f"사전 채용상태 S ({tag})", **slope_ci(zclip(S, mc)[mc], y[mc]))
EST["state_full"] = dict(label="사전 채용상태 S (전체 301)", **slope_ci(zclip(S, np.isfinite(S))[np.isfinite(S)], y))
EST["common_sample"] = {"rule": "all-4 교집합 n>=100 이면 all-4, 아니면 cash·lev·roa 교집합", "n_all4": int(mall.sum()), "n_3": int(m4.sum()), "used": tag}
for k2 in ("state_common", "state_full"):
    print(f"  {EST[k2]['label']:<34} {EST[k2]['slope']:+.4f} {EST[k2]['ci']} n={EST[k2]['n']}")

sig_fin = [k for k in MEAS if EST[k]["sig"]]
emit("I-72", "사전 재무상태 × 채용반응 이질성 (표 B5)", "GO",
     {"panelA_slopes": EST, "y_def": "이벤트 수준 처치−대조 Δlog 채용률 (비winsor, I-47 관행)",
      "x_rule": "1/99 일괄 클립 후 z-표준화 · 재무는 딜연도−1 결산"},
     "관측 재무상태가 상태 gradient 를 대체 설명하는가 — 같은 감사표본에서 상태와 직접 비교",
     f"유의한 재무 기울기 {len(sig_fin)}/4 ({', '.join(sig_fin) or '없음'}) · "
     f"동일표본 상태 기울기 {EST['state_common']['slope']:+.4f} {EST['state_common']['ci']} (n {EST['state_common']['n']})",
     kill_met=False, n=int(np.isfinite(X['cash_assets']).sum()),
     extra={"date": "2026-08-31", "comment_ref": "PE Hiring 0831_comment.md Part5 §33"})
