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
            rows.append((r["g"], uid, tr, k, float(h) / float(emp), m0 + k, S_e))
ev = np.array([x[0] for x in rows]); unit = np.array([x[1] for x in rows])
tr = np.array([x[2] for x in rows], float); kk = np.array([x[3] for x in rows])
y = np.array([x[4] for x in rows]); cal = np.array([x[5] for x in rows]); S = np.array([x[6] for x in rows])
post = (kk > 0).astype(float)
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

pre_ok_B = all(abs(PB[f"q{qq}"]["t"]) < 1.96 for qq in (-4, -3, -2))
pre_ok_C = all(abs(PC[f"q{qq}"]["t"]) < 1.96 for qq in (-4, -3, -2))
emit("I-75", "stacked matched panel DiD / event-study (comment did.md)", "GO",
     {"panelA_did": PA, "panelB_es_level": PB, "panelC_es_state": PC,
      "design": {"outcome": "월별 채용률 H/E (비변환)", "fe": "unit(event×firm) + calendar month (교대투영)",
                 "S": "처치 target 의 연속 상태를 매칭 세트 전체에 부여", "cluster": "event",
                 "ref": "q−1 기준", "n_rows": int(len(y)), "n_units": int(len(set(unit))),
                 "n_events": int(len(set(ev))), "n_cal_months": int(len(set(cal)))}},
     "동일 매칭 구조의 패널 DiD/event-study 에서도 상태 이질성(β2>0)과 무사전추세가 보이는가",
     f"β1 {PA['treat_post']['coef']:+.5f} (t {PA['treat_post']['t']}) · β2 {PA['treat_post_S']['coef']:+.5f} "
     f"(t {PA['treat_post_S']['t']}) · 사전 분기 |t|<1.96: level {pre_ok_B} · state {pre_ok_C}",
     kill_met=False, n=int(len(set(ev))),
     extra={"date": "2026-09-02", "comment_ref": "paper_v4/submission/comment/did.md"})
