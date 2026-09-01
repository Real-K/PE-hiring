# -*- coding: utf-8 -*-
"""I-75 stacked matched panel DiD / event-study (comment/did.md 반영).

주 설계(상태균형 매칭, 286 이벤트)의 매칭 세트를 그대로 쌓아(firm-month 패널)
  (1) Y_it = firmFE + calendarFE + Post + β1·Treat×Post                          [평균]
  (2)      + Post×S + β2·Treat×Post×S                                            [이질성 — 관심계수]
  (3) 분기 event-study: Treat×q_k (기준 q−1), 그리고 Treat×q_k×S
를 추정한다. Y = 월별 채용률(H/E). S 는 처치 target 의 연속 상태를 매칭 세트 전체에 부여(hazard 삼중교호와
동일 관행). unit = event×firm (재사용 대조는 stack 별 별도 유닛 — 표준 stacked DiD). SE 는 이벤트 클러스터.
firm·calendar FE 는 교대투영(반복 demeaning, FWL)으로 흡수 — 수렴 후 정확.
"""
import os
import numpy as np
from h30_common import emit

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "i58_design_audit.py"), encoding="utf-8").read()
i = src.find("[구축]")
ns = {"__name__": "i75_reuse"}
exec(compile(src[:src.rfind("\n", 0, i)], "i58_design_audit.py(head)", "exec"), ns)
G, EV0 = ns["G"], ns["EV0"]
build_set, match = ns["build_set"], ns["match"]
Hv, Ev = G["Hv"], G["Ev"]
mset = G["mset"]

print("[I-75] 상태균형 매칭 세트 재구축...")
T1, _, _ = build_set(True)
rows = []                      # (event, unitid, treated, k, y, calmonth)
uid = 0
for r in T1:
    e = EV0[r["g"]]; m0 = e["m0"]
    ct = match(e["ti"], m0, True)
    S_e = r["S"]
    for f, tr in [(e["ti"], 1)] + [(int(c), 0) for c in (ct if ct is not None else [])]:
        uid += 1
        for k in list(range(-12, 0)) + list(range(1, 13)):
            j = mset.get(m0 + k)
            if j is None: continue
            h, emp = Hv[f, j], Ev[f, j]
            if not (np.isfinite(h) and np.isfinite(emp)) or emp < 5: continue
            sp = G["Sv"][f, j]
            rows.append((r["g"], uid, tr, k, float(h) / float(emp), m0 + k, S_e,
                         (float(sp) / float(emp)) if np.isfinite(sp) else np.nan, f, j))
ev = np.array([x[0] for x in rows]); unit = np.array([x[1] for x in rows])
tr = np.array([x[2] for x in rows], float); kk = np.array([x[3] for x in rows])
y = np.array([x[4] for x in rows]); cal = np.array([x[5] for x in rows]); S = np.array([x[6] for x in rows])
sepv = np.array([x[7] for x in rows]); u_f = np.array([x[8] for x in rows]); u_j = np.array([x[9] for x in rows])
post = (kk > 0).astype(float)
S_bar = float(np.mean([r["S"] for r in T1]))   # 이벤트 평균으로 중심화 — 교호모형의 β1 = 평균상태에서의 효과
S = S - S_bar
print(f"  rows {len(y):,} · units {len(set(unit)):,} · events {len(set(ev))} · calendar months {len(set(cal))}")

def demean_two_way(M, g1, g2, iters=200, tol=1e-11):
    M = M.copy()
    for _ in range(iters):
        prev = M.copy()
        for g in (g1, g2):
            order = np.argsort(g, kind="stable"); gs = g[order]
            cuts = np.flatnonzero(np.r_[True, gs[1:] != gs[:-1]])
            for c in range(M.shape[1]):
                v = M[order, c]
                sums = np.add.reduceat(v, cuts); cnts = np.diff(np.r_[cuts, len(v)])
                means = np.repeat(sums / cnts, cnts)
                v -= means; M[order, c] = v
        if np.max(np.abs(M - prev)) < tol: break
    return M

def cluster_ols(X, yv, cl):
    XtX = X.T @ X; b = np.linalg.solve(XtX, X.T @ yv)
    e = yv - X @ b; inv = np.linalg.inv(XtX)
    meat = np.zeros((X.shape[1], X.shape[1]))
    for g in np.unique(cl):
        m = cl == g; Xg = X[m]; eg = e[m]
        s = Xg.T @ eg; meat += np.outer(s, s)
    Gn = len(np.unique(cl)); n, p = X.shape
    adj = (Gn / (Gn - 1)) * ((n - 1) / (n - p))
    V = adj * inv @ meat @ inv
    se = np.sqrt(np.diag(V))
    return b, se

def pack(b, se, lab):
    return {"coef": round(float(b), 6), "se": round(float(se), 6),
            "ci": [round(float(b - 1.96 * se), 6), round(float(b + 1.96 * se), 6)],
            "t": round(float(b / se), 2), "label": lab}

# ── Panel A: DiD (평균 + 상태 삼중교호) ──
X1 = np.column_stack([post, tr * post])
M = demean_two_way(np.column_stack([y[:, None], X1]), unit, cal)
b, se = cluster_ols(M[:, 1:], M[:, 0], ev)
PA = {"treat_post": pack(b[1], se[1], "β1 Treat×Post (월별 채용률)")}
X2 = np.column_stack([post, tr * post, post * S, tr * post * S])
M2 = demean_two_way(np.column_stack([y[:, None], X2]), unit, cal)
b2, se2 = cluster_ols(M2[:, 1:], M2[:, 0], ev)
PA["treat_post_S"] = pack(b2[3], se2[3], "β2 Treat×Post×S (관심계수)")
PA["treat_post_in_S_model"] = pack(b2[1], se2[1], "β1 (S 모형 내)")
print(f"  [A] β1 {PA['treat_post']['coef']:+.5f} (SE {PA['treat_post']['se']:.5f}, t {PA['treat_post']['t']})")
print(f"      β2 {PA['treat_post_S']['coef']:+.5f} (SE {PA['treat_post_S']['se']:.5f}, t {PA['treat_post_S']['t']}) {PA['treat_post_S']['ci']}")

# ── Panel B/C: 분기 event-study (기준 q−1) ──
q = np.where(kk > 0, (kk + 2) // 3, -(((-kk) + 2) // 3))
QS = [-4, -3, -2, 1, 2, 3, 4]          # q−1 기준(제외)
Dq = np.column_stack([(q == qq).astype(float) for qq in QS])
Xb = np.column_stack([Dq, Dq * tr[:, None]])
Mb = demean_two_way(np.column_stack([y[:, None], Xb]), unit, cal)
bb, sb = cluster_ols(Mb[:, 1:], Mb[:, 0], ev)
PB = {f"q{qq}": pack(bb[len(QS) + i2], sb[len(QS) + i2], f"Treat×q{qq}") for i2, qq in enumerate(QS)}
Xc = np.column_stack([Dq, Dq * tr[:, None], Dq * S[:, None], Dq * (tr * S)[:, None]])
Mc = demean_two_way(np.column_stack([y[:, None], Xc]), unit, cal)
bc, sc = cluster_ols(Mc[:, 1:], Mc[:, 0], ev)
PC = {f"q{qq}": pack(bc[3 * len(QS) + i2], sc[3 * len(QS) + i2], f"Treat×q{qq}×S") for i2, qq in enumerate(QS)}
for lab, P in (("[B] Treat×q_k", PB), ("[C] Treat×q_k×S", PC)):
    print(f"  {lab}: " + " · ".join(f"q{qq} {P[f'q{qq}']['coef']:+.5f}({P[f'q{qq}']['t']})" for qq in QS))

# ═══ 0831 확장: 다각도 통계량 (전부 결정적 — rng 없음) ═══
from scipy import stats as sps

def run_fe(yv, X, g1, g2, cl):
    M = demean_two_way(np.column_stack([yv[:, None], X]), g1, g2)
    return cluster_ols(M[:, 1:], M[:, 0], cl)

def did_pair(yv, g1=None, g2=None, cl=None, msk=None):
    """β1·β2 (S 모형) 한 번에."""
    m = np.ones(len(yv), bool) if msk is None else msk
    X = np.column_stack([post[m], (tr * post)[m], (post * S)[m], (tr * post * S)[m]])
    b, se = run_fe(yv[m], X, (unit if g1 is None else g1)[m], (cal if g2 is None else g2)[m], (ev if cl is None else cl)[m])
    return {"beta1": pack(b[1], se[1], "Treat×Post"), "beta2": pack(b[3], se[3], "Treat×Post×S")}

# ── Panel D: 결과변수 변형 ──
h_raw = np.array([Hv[u_f[i], u_j[i]] for i in range(len(y))], float)
OUTS2 = {"rate": y,
         "log1p_rate": np.log1p(y),
         "any_entry": (h_raw > 0).astype(float),
         "sep_rate": sepv,
         "churn_rate": y + sepv}
PD_ = {}
for k, yv in OUTS2.items():
    ok = np.isfinite(yv)
    PD_[k] = did_pair(yv, msk=ok); PD_[k]["n_rows"] = int(ok.sum())
    print(f"  [D] {k:<12} β1 {PD_[k]['beta1']['coef']:+.5f}(t {PD_[k]['beta1']['t']}) · β2 {PD_[k]['beta2']['coef']:+.5f}(t {PD_[k]['beta2']['t']})")

# ── Panel E: 상태 정의 변형 (연속·표준화·삼분위·중앙값) ──
S_sd = float(np.std([r["S"] for r in T1])); S_iqr = float(np.subtract(*np.percentile([r["S"] for r in T1], [75, 25])) * -1)
q1S, q2S = np.percentile([r["S"] - S_bar for r in T1], [33.33, 66.67])
S_t3 = (S > q2S).astype(float); S_t1 = (S <= q1S).astype(float)
PE_ = {"continuous": PA["treat_post_S"],
       "per_sd": pack(PA["treat_post_S"]["coef"] * S_sd, PA["treat_post_S"]["se"] * S_sd, "β2×SD(S)"),
       "per_iqr": pack(PA["treat_post_S"]["coef"] * S_iqr, PA["treat_post_S"]["se"] * S_iqr, "β2×IQR(S)"),
       "S_sd": round(S_sd, 4), "S_iqr": round(S_iqr, 4)}
Xt = np.column_stack([post, tr * post, post * S_t3, tr * post * S_t3])
bt, st_ = run_fe(y, Xt, unit, cal, ev)
PE_["tercile_T3_vs_rest"] = pack(bt[3], st_[3], "Treat×Post×1(T3)")
med = np.median([r["S"] - S_bar for r in T1]); S_med = (S > med).astype(float)
Xm = np.column_stack([post, tr * post, post * S_med, tr * post * S_med])
bm, sm_ = run_fe(y, Xm, unit, cal, ev)
PE_["median_split"] = pack(bm[3], sm_[3], "Treat×Post×1(S>med)")
print(f"  [E] per-SD {PE_['per_sd']['coef']:+.5f} · T3 {PE_['tercile_T3_vs_rest']['coef']:+.5f}(t {PE_['tercile_T3_vs_rest']['t']}) · median {PE_['median_split']['coef']:+.5f}(t {PE_['median_split']['t']})")

# ── Panel F: 설계 비교 — 통상 매칭(301) vs 상태균형(286) ──
T0, _, _ = build_set(False)
rows0 = []; uid0 = 0
for r in T0:
    e = EV0[r["g"]]; m0 = e["m0"]; ct = match(e["ti"], m0, False)
    for f2, tr2 in [(e["ti"], 1)] + [(int(c), 0) for c in (ct if ct is not None else [])]:
        uid0 += 1
        for k2 in list(range(-12, 0)) + list(range(1, 13)):
            j2 = mset.get(m0 + k2)
            if j2 is None: continue
            h2, e2 = Hv[f2, j2], Ev[f2, j2]
            if not (np.isfinite(h2) and np.isfinite(e2)) or e2 < 5: continue
            rows0.append((r["g"], uid0, tr2, k2, float(h2) / float(e2), m0 + k2, r["S"]))
ev0 = np.array([x[0] for x in rows0]); un0 = np.array([x[1] for x in rows0]); tr0 = np.array([x[2] for x in rows0], float)
kk0 = np.array([x[3] for x in rows0]); y0 = np.array([x[4] for x in rows0]); cal0 = np.array([x[5] for x in rows0]); S0 = np.array([x[6] for x in rows0]) - S_bar
p0 = (kk0 > 0).astype(float)
X0 = np.column_stack([p0, tr0 * p0, p0 * S0, tr0 * p0 * S0])
b0, se0 = run_fe(y0, X0, un0, cal0, ev0)
PF_ = {"conventional_301": {"beta1": pack(b0[1], se0[1], "β1"), "beta2": pack(b0[3], se0[3], "β2"),
                            "n_rows": len(y0), "n_events": int(len(set(ev0)))},
       "balanced_286": {"beta1": PA["treat_post_in_S_model"], "beta2": PA["treat_post_S"]}}
print(f"  [F] 통상(301) β2 {PF_['conventional_301']['beta2']['coef']:+.5f}(t {PF_['conventional_301']['beta2']['t']}) vs 균형(286) {PA['treat_post_S']['coef']:+.5f}(t {PA['treat_post_S']['t']})")

# ── Panel G: FE·클러스터·가중 변형 (β2) ──
etime = kk  # event-time FE
Xg = np.column_stack([post, tr * post, post * S, tr * post * S])
bg, sg = run_fe(y, Xg, unit, etime, ev)
PG_ = {"fe_unit_eventtime": pack(bg[3], sg[3], "unit+event-time FE")}
Mg = demean_two_way(np.column_stack([y[:, None], Xg]), unit, cal)
bu, su = cluster_ols(Mg[:, 1:], Mg[:, 0], unit)
PG_["cluster_unit"] = pack(bu[3], su[3], "unit 클러스터")
wts = np.zeros(len(y))
for g in np.unique(ev):
    m = ev == g; wts[m] = 1.0 / m.sum()
wts *= len(y) / wts.sum()
sw = np.sqrt(wts)
Mw = demean_two_way(np.column_stack([(y * 1.0)[:, None], Xg]), unit, cal)  # FE 후 가중 (근사: 가중 demeaning 생략 명시)
bw, sww = cluster_ols(Mw[:, 1:] * sw[:, None], Mw[:, 0] * sw, ev)
PG_["event_equal_weight"] = pack(bw[3], sww[3], "이벤트 동일가중(사후 FE 가중)")
print(f"  [G] event-time FE {PG_['fe_unit_eventtime']['coef']:+.5f}(t {PG_['fe_unit_eventtime']['t']}) · unit-cl {PG_['cluster_unit']['t']} · eq-wt {PG_['event_equal_weight']['coef']:+.5f}(t {PG_['event_equal_weight']['t']})")

# ── Panel H: 크기 환산 + 결합 사전추세 Wald ──
pre_mean_tr = float(np.mean(y[(tr == 1) & (post == 0)]))
PH_ = {"pre_mean_treated_rate": round(pre_mean_tr, 5),
       "annualised_beta1": round(12 * PA["treat_post"]["coef"], 4),
       "beta1_pct_of_pre_mean": round(PA["treat_post"]["coef"] / pre_mean_tr * 100, 1),
       "beta2_iqr_annualised": round(12 * PE_["per_iqr"]["coef"], 4),
       "beta2_iqr_pct_of_pre_mean": round(PE_["per_iqr"]["coef"] / pre_mean_tr * 100, 1)}
def wald_pre(Mx, bx, sx, cl, X, yv, idxs):
    Md = demean_two_way(np.column_stack([yv[:, None], X]), unit, cal)
    Xd, yd = Md[:, 1:], Md[:, 0]
    XtX = Xd.T @ Xd; b = np.linalg.solve(XtX, Xd.T @ yd); e = yd - Xd @ b
    inv = np.linalg.inv(XtX); meat = np.zeros((Xd.shape[1],) * 2)
    for g in np.unique(cl):
        m = cl == g; sv = Xd[m].T @ e[m]; meat += np.outer(sv, sv)
    Gn = len(np.unique(cl)); n, p = Xd.shape
    V = (Gn / (Gn - 1)) * ((n - 1) / (n - p)) * inv @ meat @ inv
    bb = b[idxs]; VV = V[np.ix_(idxs, idxs)]
    w = float(bb @ np.linalg.solve(VV, bb))
    return round(w, 3), round(float(1 - sps.chi2.cdf(w, len(idxs))), 4)
w1, p1 = wald_pre(None, None, None, ev, Xb, y, [len(QS) + i2 for i2, qq in enumerate(QS) if qq < 0])
w2, p2 = wald_pre(None, None, None, ev, Xc, y, [3 * len(QS) + i2 for i2, qq in enumerate(QS) if qq < 0])
PH_["pretrend_wald_level"] = {"chi2_3": w1, "p": p1}
PH_["pretrend_wald_state"] = {"chi2_3": w2, "p": p2}
print(f"  [H] 사전 Wald: level χ²={w1} p={p1} · state χ²={w2} p={p2} · 12×β1 {PH_['annualised_beta1']} ({PH_['beta1_pct_of_pre_mean']}%)")

# ── Panel I: 상태군별 event-study (T3 vs T1) ──
PI_ = {}
for lab, mgrp in (("T3_low_hiring", S > q2S), ("T1_high_hiring", S <= q1S)):
    mm = mgrp
    Dqm = np.column_stack([(q[mm] == qq).astype(float) for qq in QS])
    Xi = np.column_stack([Dqm, Dqm * tr[mm][:, None]])
    Mi = demean_two_way(np.column_stack([y[mm][:, None], Xi]), unit[mm], cal[mm])
    bi, si = cluster_ols(Mi[:, 1:], Mi[:, 0], ev[mm])
    PI_[lab] = {f"q{qq}": pack(bi[len(QS) + i2], si[len(QS) + i2], f"{lab} q{qq}") for i2, qq in enumerate(QS)}
    PI_[lab]["n_events"] = int(len(set(ev[mm])))
print("  [I] T3 q1..q4:", " ".join(f"{PI_['T3_low_hiring'][f'q{qq}']['coef']:+.5f}" for qq in (1,2,3,4)),
      "| T1:", " ".join(f"{PI_['T1_high_hiring'][f'q{qq}']['coef']:+.5f}" for qq in (1,2,3,4)))

pre_ok_B = all(abs(PB[f"q{qq}"]["t"]) < 1.96 for qq in (-4, -3, -2))
pre_ok_C = all(abs(PC[f"q{qq}"]["t"]) < 1.96 for qq in (-4, -3, -2))
emit("I-75", "stacked matched panel DiD / event-study (comment did.md)", "GO",
     {"panelA_did": PA, "panelB_es_level": PB, "panelC_es_state": PC,
      "panelD_outcomes": PD_, "panelE_state_forms": PE_, "panelF_design_compare": PF_,
      "panelG_variants": PG_, "panelH_magnitudes": PH_, "panelI_es_bystate": PI_,
      "design": {"S_centering": round(S_bar, 4), "outcome": "월별 채용률 H/E (비변환)", "fe": "unit(event×firm) + calendar month (교대투영)",
                 "S": "처치 target 의 연속 상태를 매칭 세트 전체에 부여", "cluster": "event",
                 "ref": "q−1 기준", "n_rows": int(len(y)), "n_units": int(len(set(unit))),
                 "n_events": int(len(set(ev))), "n_cal_months": int(len(set(cal)))}},
     "동일 매칭 구조의 패널 DiD/event-study 에서도 상태 이질성(β2>0)과 무사전추세가 보이는가",
     f"β1 {PA['treat_post']['coef']:+.5f} (t {PA['treat_post']['t']}) · β2 {PA['treat_post_S']['coef']:+.5f} "
     f"(t {PA['treat_post_S']['t']}) · 사전 분기 |t|<1.96: level {pre_ok_B} · state {pre_ok_C}",
     kill_met=False, n=int(len(set(ev))),
     extra={"date": "2026-09-02", "comment_ref": "paper_v4/submission/comment/did.md"})
