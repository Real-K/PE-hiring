# -*- coding: utf-8 -*-
"""I-74 not-yet-treated 민감도 — 최소 처치 간격 18개월 (0831 원고 §G.2).
i06 을 SPEC 정의 직후까지 실행해 동일 설계(nyt·summ·SPEC)를 재사용하고, 별도 seed 로 G18 만 산출한다.
I06 의 기존 G24/G36 산출(패널 C 부트 CI 포함)은 재실행으로 원상 보존한다 — 인쇄값 재현성."""
import os
import numpy as np
from h30_common import emit, SEED

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "i06_notyet_anatomy.py"), encoding="utf-8").read()
i = src.find('print("\\n[Panel A]')
ns = {"__name__": "i74_reuse"}
exec(compile(src[:src.rfind("\n", 0, i)], "i06_notyet_anatomy.py(head)", "exec"), ns)
nyt, summ, SPEC = ns["nyt"], ns["summ"], ns["SPEC"]
rng = np.random.default_rng(SEED + 18)
PA = {}
for lab, (tl, pl) in SPEC.items():
    r = nyt(tl, pl, 18)
    s = summ(r, rng)
    s["mean_ncand"] = round(float(np.mean([x["n_cand"] for x in r])), 1) if r else None
    PA[f"G18|{lab}"] = s
    print(f"  G18|{lab}: n {s.get('n')} · DiD {s.get('DiD')} {s.get('DiD_ci')} · P1 {s.get('P1')} {s.get('P1_ci')} · rel {s.get('rel')} {s.get('rel_ci')}")
emit("I-74", "not-yet-treated 최소간격 18개월 (0831 원고 G.2)", "GO",
     {"panelA_specs_G18": PA},
     "18개월 최소간격에서도 G24/G36 의 결론이 유지되는가",
     f"S1 DiD {PA['G18|S1 기존처치·기존풀']['DiD']} · S4 DiD {PA['G18|S4 확장처치·확장풀']['DiD']}",
     kill_met=False, n=PA["G18|S4 확장처치·확장풀"].get("n"),
     extra={"date": "2026-08-31", "comment_ref": "Paper+Appendix(w.placeholder)_0831_2200.md §G.2", "seed_note": "SEED+18 별도 스트림 — I06 rng 불간섭"})
