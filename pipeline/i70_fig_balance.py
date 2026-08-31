# -*- coding: utf-8 -*-
"""I-70 그림 1 재작성 자료 + 주표본(286) 균형 — PI 0831 코멘트 Part 4 §6–7·§26–27, Part 3 §9(Panel C).

코멘트 요구사항:
  (a) Figure 1(a): 286 이벤트 수준 (사전 상태 S, 주사양 처리 결과) 산점 + 고정 오분위 bin 평균
      + 선형적합 + 95% 밴드. 표시 관계는 주사양의 공변량 조정(FWL)·5/95 winsor 를 따른다(added-variable).
  (b) Figure 1(b): 위약 gradient 의 **실제 2,000 draws** 경험분포(정규근사 금지) + 경험 2.5/97.5 백분위.
  (c) Table 1 Panel C: 286 처치 vs 상태균형 대조군의 공변량·상태 균형(정규화 차이).

설계 코드는 i58_design_audit.py 를 마커까지 그대로 실행해 재사용한다(전사 없음).
관측 기울기 = 0.7101 재현을 assert 한다. 산점 좌표는 S 정렬로 저장해 이벤트 순서 연결을 끊는다.
"""
import os
import numpy as np
from h30_common import emit, widx

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "i58_design_audit.py"), encoding="utf-8").read()
i = src.find("[구축]")
ns = {"__name__": "i70_reuse"}
exec(compile(src[:src.rfind("\n", 0, i)], "i58_design_audit.py(head)", "exec"), ns)
G, EV0, rng = ns["G"], ns["EV0"], ns["rng"]
build_set, sl, design, match, blk, Sall = (ns[k] for k in ("build_set", "sl", "design", "match", "blk", "Sall"))
Hv, Ev, Sv, adpt = G["Hv"], G["Ev"], G["Sv"], G["adpt_arr"]
NDRAW = 2000

print("[I-70] 상태균형 설계 구축...")
T1, P1, K1 = build_set(True)
cuts = tuple(np.percentile([r["eff"] for r in T1], [5, 95]))
obs = sl(T1, "eff", cuts)
print(f"  처치 {len(T1)} · 위약 {len(P1)} · 관측 기울기 {obs:+.4f}")
assert abs(obs - 0.7101) < 5e-4, f"주계수 재현 실패: {obs}"

# ── Panel A: 실제 위약 draws (i58.ri 와 동일 로직, draw 를 저장) ──
cells = sorted({r["g"] for r in P1}); byg = {c: [r for r in P1 if r["g"] == c] for c in cells}
draws = []
for _ in range(NDRAW):
    d_ = []
    for j in rng.permutation(len(cells)):
        d_ += byg[cells[j]]
        if len(d_) >= len(T1): break
    v = sl(d_[:len(T1)], "eff", cuts)
    if v is not None: draws.append(v)
draws = np.array(draws)
mu, sd = float(draws.mean()), float(draws.std())
p_up = (int((draws >= obs).sum()) + 1) / (len(draws) + 1)
p_two = (int((np.abs(draws - mu) >= abs(obs - mu)).sum()) + 1) / (len(draws) + 1)
p_lo = (int((draws <= obs).sum()) + 1) / (len(draws) + 1)
p_two_2min = min(1.0, 2 * min(p_up, p_lo))
q025, q975 = np.percentile(draws, [2.5, 97.5])
print(f"  null 평균 {mu:+.4f} (SD {sd:.4f}) · 경험 95% [{q025:+.4f}, {q975:+.4f}] · "
      f"p_upper {p_up:.4f} · p_two {p_two:.4f}")
PA = {"observed": round(obs, 4), "n": len(T1), "n_pseudo": len(P1),
      "null_mean": round(mu, 4), "null_sd": round(sd, 4),
      "pct_2_5": round(float(q025), 4), "pct_97_5": round(float(q975), 4),
      "RI_p_upper": round(p_up, 4), "RI_p_two_sided": round(p_two, 4),
      "RI_p_two_sided_2min": round(p_two_2min, 4),
      "p_conventions": "two_sided = 중심화 |d-μ|>=|obs-μ| 경험비율; 2min = 2·min(상단,하단) — I-57/I-59 관행",
      "z": round((obs - mu) / sd, 2), "winsor_cuts": [round(c, 4) for c in cuts],
      "draws": [round(float(v), 4) for v in draws]}

# ── Panel B: added-variable 산점 · 고정 오분위 bin · 적합선 · 부트스트랩 밴드 ──
S = np.array([r["S"] for r in T1]); yw = np.clip(np.array([r["eff"] for r in T1]), *cuts)
C = design(T1)
rz = lambda v: v - C @ np.linalg.lstsq(C, v, rcond=None)[0]
xr, yr = rz(S), rz(yw)
b_fwl = float(np.sum(xr * yr) / np.sum(xr * xr))
assert abs(b_fwl - obs) < 5e-4
xd, yd = xr + S.mean(), yr + yw.mean()
qs = np.percentile(xd, [20, 40, 60, 80]); bins = np.digitize(xd, qs)
bin_means = [{"x": round(float(xd[bins == k].mean()), 4), "y": round(float(yd[bins == k].mean()), 4),
              "n": int((bins == k).sum())} for k in range(5)]
grid = np.linspace(float(xd.min()), float(xd.max()), 60)
n = len(xd); lines = np.empty((NDRAW, len(grid)))
for b in range(NDRAW):
    ii = rng.integers(0, n, n)
    xb, yb = xd[ii], yd[ii]
    vx = xb - xb.mean()
    bb = float(np.sum(vx * (yb - yb.mean())) / np.sum(vx * vx))
    lines[b] = yb.mean() + bb * (grid - xb.mean())
lo_b, hi_b = np.percentile(lines, [2.5, 97.5], axis=0)
o_srt = np.argsort(xd); o_raw = np.argsort(S)
PB = {"display": "added-variable: 주사양 공변량(로그규모·사전성장·업력·산업)을 S 와 winsor 결과 양쪽에서 잔차화 후 각 평균을 더해 표시",
      "pairs_display": [[round(float(xd[i]), 4), round(float(yd[i]), 4)] for i in o_srt],
      "pairs_raw": [[round(float(S[i]), 4), round(float(yw[i]), 4)] for i in o_raw],
      "quintile_bin_means": bin_means,
      "fit": {"xbar": round(float(xd.mean()), 4), "ybar": round(float(yd.mean()), 4), "slope": round(b_fwl, 4)},
      "band": {"grid": [round(float(g), 4) for g in grid],
               "lo": [round(float(v), 4) for v in lo_b], "hi": [round(float(v), 4) for v in hi_b],
               "note": "이벤트 재표본 2000회, added-variable 좌표의 OLS 적합선 2.5/97.5 백분위"}}

# ── Panel C: 286 처치 vs 상태균형 대조군 균형 ──
def cov12(row, m0):
    b12 = blk(row, m0, -12, -1); st = blk(row, m0, -24, -13); w36 = blk(row, m0, -36, -25)
    if b12 is None or st is None: return None
    c = widx(G, m0, -12, -1)
    sv = Sv[row, c].astype(float)
    sep = float(np.nansum(sv) / b12[1]) if np.isfinite(sv).all() else np.nan
    S_, _ = Sall(m0)
    c12ok = len(c) == 12 and np.isfinite(Hv[row, c].astype(float)).all()
    zsh12 = float((Hv[row, c].astype(float) == 0).mean()) if c12ok else np.nan
    return dict(zsh12=zsh12, lsize=float(np.log(b12[1])), grow=(float(np.log(st[1] / w36[1])) if (w36 and w36[1] > 0) else np.nan),
                age=(float((m0 - adpt[row]) / 12.0) if np.isfinite(adpt[row]) else np.nan),
                hr12=float(b12[0] / b12[1]), sep12=sep,
                S=(float(S_[row]) if (S_ is not None and np.isfinite(S_[row])) else np.nan))

tr, cn = [], []
for r in T1:
    e = EV0[r["g"]]; m0 = e["m0"]
    u = cov12(e["ti"], m0)
    if u: tr.append(u)
    ct = match(e["ti"], m0, True)
    for k in ([] if ct is None else ct):
        v = cov12(int(k), m0)
        if v: cn.append(v)
LBL = {"zsh12": "무채용월 비중(−12~−1)", "lsize": "log 고용(−12~−1 평균)", "grow": "사전 고용성장(−24~−13 / −36~−25)",
       "age": "업력(년)", "hr12": "사전 12개월 채용률", "sep12": "사전 12개월 이직률", "S": "사전 채용상태 S"}
PC = {}
for k, lab in LBL.items():
    a = np.array([u[k] for u in tr], float); b = np.array([u[k] for u in cn], float)
    a, b = a[np.isfinite(a)], b[np.isfinite(b)]
    nd = float((a.mean() - b.mean()) / np.sqrt((a.var() + b.var()) / 2))
    PC[k] = {"label": lab, "treated_mean": round(float(a.mean()), 4), "control_mean": round(float(b.mean()), 4),
             "nd": round(nd, 4), "n_treated": len(a), "n_controls": len(b)}
    print(f"  {lab:<28} 처치 {PC[k]['treated_mean']:>+8.4f} · 대조 {PC[k]['control_mean']:>+8.4f} · ND {nd:+.4f}")

emit("I-70", "그림1 재작성 자료 + 주표본 균형 (0831 코멘트)", "GO",
     {"panelA_gradient": PA, "panelB_scatter": PB, "panelC_balance286": PC},
     "주사양 관계가 소수 극단값이 아니라 상태 분포 전반의 관계인가; 위약분포를 경험분포로 직접 보여준다",
     f"기울기 {obs:+.4f} 재현 · 실제 {len(draws)} draws 경험 95% [{q025:+.4f},{q975:+.4f}] · "
     f"p_two {p_two:.4f} · 286 균형 |ND| 최대 {max(abs(v['nd']) for v in PC.values()):.4f}",
     kill_met=False, n=len(T1), extra={"date": "2026-08-31", "comment_ref": "PE Hiring 0831_comment.md Part4 §6–7, Part3 §9"})
