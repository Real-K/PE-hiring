# -*- coding: utf-8 -*-
"""I-73 (a) 고용노출 가중 분해 (표 A2, HR = 12·q·i_E) — PI 0831 원고 §A.3 정의 그대로.
       q = 활동월 고용노출 비중, i_E = 활동월 노출당 채용. Δlog HR = Δlog q + Δlog i_E (항등식).
   (b) E2 — 사전 딜 수 경험의 조정(FWL) 연속 기울기와 삼분위 대비 (0831 원고 §E.2).
i35_canonical.py / i45_power_invariance.py 를 마커까지 실행해 표본·매칭을 그대로 재사용한다.
"""
import os, gc
import numpy as np
from h30_common import emit, qci, NB, widx, boot_did_ci, SEED

HERE = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(SEED)

# ── (a) 표 A2: 고용노출 가중 분해 ──
src = open(os.path.join(HERE, "i35_canonical.py"), encoding="utf-8").read()
i = src.find("def did(")
ns = {"__name__": "i73_reuse"}
exec(compile(src[:src.rfind("\n", 0, i)], "i35_canonical.py(head)", "exec"), ns)
G, EV = ns["G"], ns["EV"]; Hv, Ev = G["Hv"], G["Ev"]

def qi(row, m0, a, b):
    c = widx(G, m0, a, b)
    if len(c) != (b - a + 1): return None
    h, e = Hv[row, c].astype(float), Ev[row, c].astype(float)
    if not (np.isfinite(h).all() and np.isfinite(e).all()) or np.mean(e) < 5: return None
    A = h > 0; Et = float(e.sum())
    if Et <= 0: return None
    qv = float(e[A].sum() / Et)
    iE = float(h.sum() / e[A].sum()) if A.any() else np.nan
    return qv, iE

for e in EV:
    pr, po = qi(e["ti"], e["m0"], -12, -1), qi(e["ti"], e["m0"], 1, 12)
    e["x"] = {}
    if pr and po:
        (q0, i0), (q1, i1) = pr, po
        e["x"] = {"dq": q1 - q0,
                  "diE": (i1 - i0) if (np.isfinite(i0) and np.isfinite(i1)) else np.nan,
                  "dlq": np.log(q1 / q0) if (q0 > 0 and q1 > 0) else np.nan,
                  "dliE": (np.log(i1 / i0) if (np.isfinite(i0) and np.isfinite(i1)
                                               and i0 > 0 and i1 > 0) else np.nan),
                  "q0": q0, "i0": i0}
    acc = {}
    for k in e["ctrls"]:
        a2, b2 = qi(k, e["m0"], -12, -1), qi(k, e["m0"], 1, 12)
        if not (a2 and b2): continue
        (q0, i0), (q1, i1) = a2, b2
        acc.setdefault("dq", []).append(q1 - q0)
        if np.isfinite(i0) and np.isfinite(i1): acc.setdefault("diE", []).append(i1 - i0)
        if q0 > 0 and q1 > 0: acc.setdefault("dlq", []).append(np.log(q1 / q0))
        if np.isfinite(i0) and np.isfinite(i1) and i0 > 0 and i1 > 0:
            acc.setdefault("dliE", []).append(np.log(i1 / i0))
    e["xc"] = {k2: float(np.mean(v)) for k2, v in acc.items() if v}

PA = {}
LAB = {"dq": "Δq 노출비중 (수준)", "diE": "Δi_E 노출당 채용 (수준)",
       "dlq": "Δlog q", "dliE": "Δlog i_E"}
for k, lab in LAB.items():
    t = [e["x"].get(k) for e in EV if e["x"].get(k) is not None and k in e["xc"]]
    c = [e["xc"][k] for e in EV if e["x"].get(k) is not None and k in e["xc"]]
    ok = [j for j, v in enumerate(t) if np.isfinite(v)]
    p_, ci, n = boot_did_ci(np.array([t[j] for j in ok]), np.array([c[j] for j in ok]), rng)
    PA[k] = {"est": p_, "ci": ci, "n": n}
    print(f"  {lab:<28} {p_:+.4f} {ci} (n={n})")
q0s = [e["x"]["q0"] for e in EV if e["x"].get("q0") is not None]
i0s = [e["x"]["i0"] for e in EV if np.isfinite(e["x"].get("i0", np.nan))]
PA["pre_q"] = round(float(np.mean(q0s)), 4); PA["pre_iE"] = round(float(np.mean(i0s)), 4)
# 로그 분해 비중 + 이벤트 부트스트랩 CI (dlq·dliE 둘 다 있는 이벤트만, 페어 재표본)
pair = [(e["x"]["dlq"] - e["xc"]["dlq"], e["x"]["dliE"] - e["xc"]["dliE"]) for e in EV
        if np.isfinite(e["x"].get("dlq", np.nan)) and "dlq" in e.get("xc", {})
        and np.isfinite(e["x"].get("dliE", np.nan)) and "dliE" in e.get("xc", {})]
arr = np.array(pair)
sh = float(arr[:, 0].mean() / (arr[:, 0].mean() + arr[:, 1].mean()))
bo = []
for _ in range(NB):
    ii = rng.integers(0, len(arr), len(arr)); a_, b_ = arr[ii, 0].mean(), arr[ii, 1].mean()
    if abs(a_ + b_) > 1e-9: bo.append(a_ / (a_ + b_))
PA["extensive_share_log"] = {"est": round(sh, 4), "ci": qci(np.array(bo)), "n": len(arr)}
print(f"  노출비중 성분의 log 기여 비중 {sh:.4f} {PA['extensive_share_log']['ci']} (n={len(arr)})")
del ns; gc.collect()

# ── (b) E2: 사전 딜 수 — 조정 연속 기울기·삼분위 대비 ──
src = open(os.path.join(HERE, "i45_power_invariance.py"), encoding="utf-8").read()
i = src.find("Panel A 구성 진단")
ns2 = {"__name__": "i73_reuse2"}
exec(compile(src[:src.rfind("\n", 0, i)], "i45_power_invariance.py(head)", "exec"), ns2)
U, EV2, y = ns2["U"], ns2["EV"], ns2["y"]
evgp = [(e["gp"], e["m0"]) for e in EV2 if e.get("gp")]
for e in U:
    e["gp_prior"] = (float(sum(1 for g2, m2 in evgp if g2 == e["gp"] and m2 < e["m0"]))
                     if e.get("gp") else np.nan)
pr = np.array([e["gp_prior"] for e in U], float); m = np.isfinite(pr)
x = np.log1p(pr)
def design(idx):
    cols = [np.ones(len(idx))]
    for k in ("S", "lsize", "grow", "age"):
        v = np.array([U[i2][k] for i2 in idx], float)
        v = np.where(np.isfinite(v), v, np.nanmedian(v[np.isfinite(v)]))
        cols.append(v)
    for s_ in sorted({U[i2]["ind1"] for i2 in idx})[1:]:
        cols.append(np.array([1.0 if U[i2]["ind1"] == s_ else 0.0 for i2 in idx]))
    for v_ in sorted({U[i2]["yr"] for i2 in idx})[1:]:
        cols.append(np.array([1.0 if U[i2]["yr"] == v_ else 0.0 for i2 in idx]))
    return np.column_stack(cols)
idxm = [i2 for i2 in range(len(U)) if m[i2]]
def fwl_slope(sel):
    C = design(sel); yv = y[sel]; xv = x[sel]
    r_ = lambda v: v - C @ np.linalg.lstsq(C, v, rcond=None)[0]
    yr, xr = r_(yv), r_(xv); d = float(np.sum(xr * xr))
    return (float(np.sum(xr * yr) / d) if d > 0 else np.nan), yr
b0, yres = fwl_slope(idxm)
bo = []
for _ in range(NB):
    sel = [idxm[j] for j in rng.integers(0, len(idxm), len(idxm))]
    v_, _ = fwl_slope(sel)
    if np.isfinite(v_): bo.append(v_)
cuts = [float(np.percentile(pr[m], 33.33)), float(np.percentile(pr[m], 66.67))]
prm = pr[idxm]
lo_m = prm <= cuts[0]                      # 첫 딜(0)
hi_m = prm > cuts[1]                       # 2건 이상
hi, lo = yres[hi_m], yres[lo_m]
d0 = float(hi.mean() - lo.mean())
bo2 = np.array([hi[rng.integers(0, len(hi), len(hi))].mean()
                - lo[rng.integers(0, len(lo), len(lo))].mean() for _ in range(NB)])
from collections import Counter
cnt_gp = Counter(g2 for g2, _ in evgp)
ge2 = {g2 for g2, c2 in cnt_gp.items() if c2 >= 2}
PB2_extra = {"n_gp_total": len(cnt_gp), "n_gp_ge2": len(ge2),
             "n_eq1": sum(1 for c2 in cnt_gp.values() if c2 == 1),
             "n_eq2": sum(1 for c2 in cnt_gp.values() if c2 == 2),
             "n_ge3": sum(1 for c2 in cnt_gp.values() if c2 >= 3),
             "max_deals": max(cnt_gp.values()),
             "share_events_gp_ge2": round(sum(1 for g2, _ in evgp if g2 in ge2) / len(evgp), 4)}
cnt_U = Counter(e["gp"] for e in U if e.get("gp"))
geU = {g2 for g2, c2 in cnt_U.items() if c2 >= 2}
PB2_extra["loo_universe"] = {"n_gp_301sample": len(cnt_U),
                             "n_repeat_gp_301sample": len(geU),
                             "n_events_repeat_301sample": int(sum(c2 for g2, c2 in cnt_U.items() if g2 in geU))}
PB2 = {"sponsor_concentration": PB2_extra, "slope_log1p_adj": {"slope": round(b0, 4), "ci": qci(np.array(bo)), "n": len(idxm)},
       "tercile_cuts": cuts,
       "hi_lo_adj": {"diff": round(d0, 4), "ci": qci(bo2), "n_hi": int(hi_m.sum()),
                     "n_lo": int(lo_m.sum())},
       "adjust_set": "사전 상태 S·log 규모·사전 성장·업력·1자리 산업·딜연도 (FWL, x·y 양측 잔차화)",
       "sponsor_rule": "복수 스폰서는 첫 기재 투자자(gplist 첫 항목)로 귀속"}
print(f"  E2 조정 연속 기울기 {b0:+.4f} {PB2['slope_log1p_adj']['ci']} (n={len(idxm)}) · "
      f"삼분위 절단 {cuts} · 상−하(조정) {d0:+.4f} {PB2['hi_lo_adj']['ci']}")

emit("I-73", "노출가중 분해(표 A2) + E2 조정 경험기울기 (0831 원고)", "GO",
     {"panelA_exposure_decomp": PA, "panelB_e2_adjusted": PB2},
     "0831 원고의 노출가중 분해 항등식과 E2 조정 사양을 정본 표본에서 산출",
     f"Δlog q {PA['dlq']['est']:+.4f} + Δlog i_E {PA['dliE']['est']:+.4f}, 노출비중 기여 "
     f"{PA['extensive_share_log']['est']:.3f} {PA['extensive_share_log']['ci']} · "
     f"E2 조정기울기 {b0:+.4f} {PB2['slope_log1p_adj']['ci']}",
     kill_met=False, n=PA["dlq"]["n"],
     extra={"date": "2026-08-31", "comment_ref": "Paper+Appendix(w.placeholder).md §A.3·§E.2"})
