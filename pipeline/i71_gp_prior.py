# -*- coding: utf-8 -*-
"""I-71 스폰서 경험 재구축 — 거래시점 **이전** 딜 수 (PI 0831 코멘트 Part 6 §10–11·§33).

현행 E1 의 'sponsor experience' 는 표본 전기간 딜 수(gpexp)라 look-ahead 가 섞인다.
  Panel A  사전 딜 수(prior count) 분포 — 첫 딜 비중, 절단값, full-count 와의 상관
  Panel B  경험 그룹별 반응 — 첫 딜(0) / 1–3 / ≥4, repeat−first 대비 (E1 대체)
  Panel C  결합 R² 순열검정 — 거래특성(딜유형·지분·log1p(사전 딜 수)) vs 상태 (I-45 Panel C 재실행)
  Panel D  5-fold 교차적합 — 동일 재실행 ('forecasting' 아님: held-out-event fit)

i45_power_invariance.py 를 Panel A 마커까지 실행해 U(301)·부트스트랩 도구를 그대로 재사용한다.
"""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "i45_power_invariance.py"), encoding="utf-8").read()
i = src.find("Panel A 구성 진단")
ns = {"__name__": "i71_reuse"}
exec(compile(src[:src.rfind("\n", 0, i)], "i45_power_invariance.py(head)", "exec"), ns)
from h30_common import emit, qci
U, EV, y, rng, rng_fig = ns["U"], ns["EV"], ns["y"], ns["rng"], ns["rng_fig"]
gdiff, qb, NPERM, NB = ns["gdiff"], ns["qb"], ns["NPERM"], ns["NB"]

print("[I-71] 사전 딜 수 구축 (처치 유니버스 전체 기준)...")
evgp = [(e["gp"], e["m0"]) for e in EV if e.get("gp")]
for e in EV:
    e["gp_prior"] = (float(sum(1 for g2, m2 in evgp if g2 == e["gp"] and m2 < e["m0"]))
                     if e.get("gp") else np.nan)
for e in U: e["gp_prior"] = e.get("gp_prior", np.nan)
pr = np.array([e["gp_prior"] for e in U], float); m = np.isfinite(pr)
full = np.array([e.get("gpexp", np.nan) for e in U], float)
mm = m & np.isfinite(full)
ties = sum(1 for e in EV if e.get("gp") and any(g2 == e["gp"] and m2 == e["m0"] for g2, m2 in evgp) and
           sum(1 for g2, m2 in evgp if g2 == e["gp"] and m2 == e["m0"]) > 1)
PA = {"n_with_gp": int(m.sum()), "share_first_time": round(float((pr[m] == 0).mean()), 4),
      "quantiles": {q: round(float(np.percentile(pr[m], q)), 2) for q in (25, 50, 75, 90)},
      "max": float(np.nanmax(pr)), "tercile_cuts": [round(float(c), 2) for c in np.percentile(pr[m], [33.33, 66.67])],
      "corr_with_fullcount": round(float(np.corrcoef(pr[mm], full[mm])[0, 1]), 4),
      "same_month_ties": int(ties),
      "def": "같은 스폰서(첫 기재 투자자)가 처치 유니버스(379)에서 초점 거래월보다 엄격히 이전에 실행한 딜 수"}
print(f"  gp 있는 이벤트 {PA['n_with_gp']} · 첫 딜 비중 {PA['share_first_time']:.2%} · "
      f"삼분위 절단 {PA['tercile_cuts']} · full-count 상관 {PA['corr_with_fullcount']}")

g0 = y[m & (pr == 0)]; g1 = y[m & (pr >= 1) & (pr <= 3)]; g2 = y[m & (pr >= 4)]
rep = y[m & (pr >= 1)]
PB = {"first_time": {"n": len(g0), "mean": round(float(g0.mean()), 4), "ci": qci(np.array([g0[rng.integers(0, len(g0), len(g0))].mean() for _ in range(NB)]))},
      "prior_1_3": {"n": len(g1), "mean": round(float(g1.mean()), 4), "ci": qci(np.array([g1[rng.integers(0, len(g1), len(g1))].mean() for _ in range(NB)]))},
      "prior_ge4": {"n": len(g2), "mean": round(float(g2.mean()), 4), "ci": qci(np.array([g2[rng.integers(0, len(g2), len(g2))].mean() for _ in range(NB)]))},
      "ge4_minus_first": gdiff(g2, g0), "repeat_minus_first": gdiff(rep, g0),
      "grouping_note": "삼분위 절단이 0 에서 퇴화하므로(첫 딜 과반) 0 / 1–3 / ≥4 고정 구간을 쓴다"}
print(f"  첫 딜 {PB['first_time']['mean']:+.4f}(n{len(g0)}) · 1–3 {PB['prior_1_3']['mean']:+.4f}(n{len(g1)}) · "
      f"≥4 {PB['prior_ge4']['mean']:+.4f}(n{len(g2)}) · ≥4−첫 {PB['ge4_minus_first']['diff']:+.4f} {PB['ge4_minus_first']['ci']}")

# ── Panel C/D: i45 재실행 (gpexp → gp_prior) ──
allidx = list(range(len(U)))
di = [i2 for i2 in allidx if np.isfinite(U[i2]["buy"]) and np.isfinite(U[i2]["stake"]) and np.isfinite(U[i2]["gp_prior"])]
yj = y[di]
Dl = np.column_stack([np.ones(len(di)), np.array([U[i2]["buy"] for i2 in di]),
                      np.array([U[i2]["stake"] for i2 in di]) / 100.0,
                      np.log1p(np.array([U[i2]["gp_prior"] for i2 in di]))])
Sl = np.column_stack([np.ones(len(di)), np.array([U[i2]["S"] for i2 in di])])
def r2(X, yy):
    r_ = yy - X @ np.linalg.lstsq(X, yy, rcond=None)[0]
    return 1 - r_.var() / yy.var()
r2d, r2s = r2(Dl, yj), r2(Sl, yj); Both = np.column_stack([Dl, Sl[:, 1:]]); r2b = r2(Both, yj)
perm_d = np.array([r2(np.column_stack([np.ones(len(di)), Dl[rng.permutation(len(di)), 1:]]), yj) for _ in range(NPERM)])
perm_s = np.array([r2(np.column_stack([np.ones(len(di)), Sl[rng.permutation(len(di)), 1:]]), yj) for _ in range(NPERM)])
PC = {"n": len(di), "r2_deal": round(float(r2d), 4), "perm_p_deal": round(float((perm_d >= r2d).mean()), 4),
      "r2_state": round(float(r2s), 4), "perm_p_state": round(float((perm_s >= r2s).mean()), 4),
      "r2_both": round(float(r2b), 4), "incremental_deal_over_state": round(float(r2b - r2s), 4),
      "incremental_state_over_deal": round(float(r2b - r2d), 4), "n_perm": NPERM,
      "deal_vars": ["buyout", "stake/100", "log1p(prior sponsor deals)"]}
print(f"  [C] n={len(di)} 거래특성 R² {r2d:.4f}(p {PC['perm_p_deal']:.3f}) · 상태 R² {r2s:.4f}(p {PC['perm_p_state']:.4f}) · 결합 {r2b:.4f}")
K = 5; fold = rng_fig.permutation(len(di)) % K
def oos_r2(X):
    pred = np.zeros(len(di))
    for k in range(K):
        trn, te = fold != k, fold == k
        pred[te] = X[te] @ np.linalg.lstsq(X[trn], yj[trn], rcond=None)[0]
    return 1 - ((yj - pred) ** 2).sum() / ((yj - yj.mean()) ** 2).sum()
o_d, o_s, o_b = oos_r2(Dl), oos_r2(Sl), oos_r2(Both)
bo = []
for _ in range(NB):
    p = rng.integers(0, len(di), len(di)); yb = yj[p]
    def oos_b(X):
        Xb = X[p]; prd = np.zeros(len(di))
        for k in range(K):
            trn, te = fold != k, fold == k
            try: prd[te] = Xb[te] @ np.linalg.lstsq(Xb[trn], yb[trn], rcond=None)[0]
            except np.linalg.LinAlgError: return np.nan
        return 1 - ((yb - prd) ** 2).sum() / ((yb - yb.mean()) ** 2).sum()
    a_, b_ = oos_b(Sl), oos_b(Dl)
    if np.isfinite(a_) and np.isfinite(b_): bo.append(a_ - b_)
dci = qb(np.array(bo))
PD = {"oos_r2_deal": round(float(o_d), 4), "oos_r2_state": round(float(o_s), 4), "oos_r2_both": round(float(o_b), 4),
      "state_minus_deal": round(float(o_s - o_d), 4), "ci": dci, "sig": bool(dci[0] > 0 or dci[1] < 0),
      "k_folds": K, "n": len(di), "framing": "held-out-event fit within the observed sample (not forecasting)"}
print(f"  [D] OOS R² 거래 {o_d:+.4f} · 상태 {o_s:+.4f} · 차이 {PD['state_minus_deal']:+.4f} {dci}")

emit("I-71", "스폰서 경험 재구축 — 거래시점 이전 딜 수", "GO",
     {"panelA_dist": PA, "panelB_groups": PB, "panelC_joint": PC, "panelD_oos": PD},
     "look-ahead 없는 경험 변수로도 E1/E2/E3 의 결론(경험 gradient 부재, 상태 우위)이 유지되는가",
     f"첫 딜 {PB['first_time']['mean']:+.4f} vs ≥4 {PB['prior_ge4']['mean']:+.4f}, 차이 {PB['ge4_minus_first']['diff']:+.4f} "
     f"{PB['ge4_minus_first']['ci']} · 거래특성 R² {r2d:.4f}(순열 p {PC['perm_p_deal']:.3f}) vs 상태 {r2s:.4f} · "
     f"OOS 차이 {PD['state_minus_deal']:+.4f} {dci}",
     kill_met=False, n=int(m.sum()), extra={"date": "2026-08-31", "comment_ref": "PE Hiring 0831_comment.md Part6 §10–11·§33"})
