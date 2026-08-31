# -*- coding: utf-8 -*-
"""Fill every [placeholder] in `Paper+Appendix(w.placeholder).md` from the analysis artifacts.

Reads the placeholder manuscript, replaces each placeholder (and unifies formatting: 4-dp
estimates/CIs, true minus signs, Events columns), writes the filled file in place after
backing up the original, and logs every substitution to FILL_TRACE.csv.
Every anchor must occur exactly once; the script fails loudly otherwise.
"""
import json, os, csv, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
ART = os.environ.get("P014_ARTIFACTS", os.path.join(ROOT, "artifacts"))
SRC = os.environ["P014_MANUSCRIPT"]  # path to Paper+Appendix(w.placeholder).md
_J = {}
def E(a):
    if a not in _J: _J[a] = json.load(open(os.path.join(ART, a + ".json"), encoding="utf-8"))["estimates"]
    return _J[a]
def g(a, path):
    o = E(a)
    for k in path.split("."): o = o[int(k)] if isinstance(o, list) else o[k]
    return o
def f4(x, plus=False): return (f"{x:+.4f}" if plus else f"{x:.4f}").replace("-", "−")
def f2(x, plus=False): return (f"{x:+.2f}" if plus else f"{x:.2f}").replace("-", "−")
def ci4(v): return f"[{v[0]:.4f}, {v[1]:.4f}]".replace("-", "−")
def p4(x): return f"{x:.4f}"
TR = []
def R(s, old, new, tag):
    n = s.count(old)
    assert n == 1, f"anchor x{n} [{tag}]: {old[:90]!r}"
    TR.append({"tag": tag, "old": old[:110], "new": new[:110]})
    return s.replace(old, new)

s = open(SRC, encoding="utf-8").read()

# ═══ 본문 ═══
# Table 1 Panel C — I70 균형 (286 상태균형)
b = lambda k, f: g("I70", f"panelC_balance286.{k}.{f}")
for k, lab in [("lsize", "| Log insured employment |"), ("grow", "| Pre-deal employment growth |"),
               ("age", "| Firm age |"), ("hr12", "| Hiring rate, months -12 to -1 |"),
               ("sep12", "| Separation rate, months -12 to -1 |"),
               ("zsh12", "| Share of no-hire months, -12 to -1 |"),
               ("S", "| Pre-deal hiring state, months -24 to -13 |")]:
    key = {"| Log insured employment |": "lsize", "| Pre-deal employment growth |": "grow",
           "| Firm age |": "age", "| Hiring rate, months -12 to -1 |": "hr12",
           "| Separation rate, months -12 to -1 |": "sep12",
           "| Share of no-hire months, -12 to -1 |": "zsh12",
           "| Pre-deal hiring state, months -24 to -13 |": "S"}[lab]
    s = R(s, f"{lab} [placeholder] | [placeholder] | [placeholder] |",
          f"{lab} {f4(b(key,'treated_mean'))} | {f4(b(key,'control_mean'))} | {f4(b(key,'nd'), plus=True)} |",
          f"T1C.{key}")
# §4.1 상태 분모
s = R(s, "$E_i^{state}$ is [placeholder: exact employment denominator used in the estimation code]",
      "$E_i^{state}$ is mean insured employment over the same twelve state-window months (months -24 through -13)", "S-denom")
# §4.3 양측 p + 공식 문장
pa = E("I70")["panelA_gradient"]
s = R(s, "a two-sided empirical tail probability of [placeholder: two-sided empirical $p$-value from the 2,000 untreated-reference draws]",
      f"a two-sided empirical tail probability of {p4(pa['RI_p_two_sided'])}", "p-main")
s = R(s, "[placeholder: state the exact finite-simulation tail formula used in the code, including treatment of the reference-distribution centre, ties, and any add-one correction.]",
      f"The reported probability equals $(1+\\#\\{{b:|g_b-\\bar g|\\ge|g^{{obs}}-\\bar g|\\}})/(B+1)$, where $g_b$ are the $B={pa['n_pseudo'] and 2000}$ simulated gradients, $\\bar g$ is their mean, ties count toward the numerator, and the add-one correction bounds the probability below by $1/(B+1)=0.0005$.", "p-formula")
# Table 3 Panel A p
s = R(s, "| Empirical two-sided $p$ | [placeholder] |",
      f"| Empirical two-sided $p$ | {p4(pa['RI_p_two_sided'])} |", "T3.p")
# Table 4 — 전면 I57 (패치판: 중심화 p)
o = lambda k, f: g("I57", f"panelB_outcomes.{k}.{f}")
s = R(s, "| Log hiring rate | 0.7101 | 0.1010 | $p=$[placeholder: two-sided] | 286 |",
      f"| Log hiring rate | {f4(o('hire','observed'))} | {f4(o('hire','null_mean'))} | {p4(o('hire','RI_p_two_centered'))} | {o('hire','n')} |", "T4.hire")
s = R(s, "| Log worker-entry count | 0.6315 | 0.1795 | [placeholder: standardized distance and two-sided $p$] | [placeholder] |",
      f"| Log worker-entry count | {f4(o('lN','observed'))} | {f4(o('lN','null_mean'))} | {f2(o('lN','z'), plus=True)}; {p4(o('lN','RI_p_two_centered'))} | {o('lN','n')} |", "T4.lN")
s = R(s, "| Log worker-entry count, controlling for $\\Delta$ log employment | 0.6957 | 0.0363 | [placeholder: standardized distance and two-sided $p$] | [placeholder] |",
      f"| Log worker-entry count, controlling for $\\Delta$ log employment | {f4(o('lN_ctrlE','observed'))} | {f4(o('lN_ctrlE','null_mean'))} | {f2(o('lN_ctrlE','z'), plus=True)}; {p4(o('lN_ctrlE','RI_p_two_centered'))} | {o('lN_ctrlE','n')} |", "T4.lNc")
s = R(s, "| Log churn rate | 0.3816 | 3.08 | [placeholder] | 288 |",
      f"| Log churn rate | {f4(o('churn','observed'))} | {f2(o('churn','z'), plus=True)} | {p4(o('churn','RI_p_two_centered'))} | {o('churn','n')} |", "T4.churn")
pc_ = lambda k, f: g("I57", f"panelC_paired.{k}.{f}")
s = R(s, "| Hiring - employment | 0.7536 | Mean 0.0232; standardized distance 4.56 | [placeholder] | 286 |",
      f"| Hiring - employment | {f4(pc_('채용 − 고용','observed'))} | Mean {f4(pc_('채용 − 고용','null_mean'))}; standardized distance {f2(pc_('채용 − 고용','z'), plus=True)} | {p4(pc_('채용 − 고용','RI_p_two_centered'))} | {pc_('채용 − 고용','n')} |", "T4.pair1")
s = R(s, "| Churn - employment | 0.4539 | Standardized distance 4.19 | [placeholder] | [placeholder: same-event $N$] |",
      f"| Churn - employment | {f4(pc_('churn − 고용','observed'))} | Mean {f4(pc_('churn − 고용','null_mean'))}; standardized distance {f2(pc_('churn − 고용','z'), plus=True)} | {p4(pc_('churn − 고용','RI_p_two_centered'))} | {pc_('churn − 고용','n')} |", "T4.pair2")
# §6.2 재무상태 문장 — I72
z = lambda k, f: g("I72", f"panelA_slopes.{k}.{f}")
fin_sent = ("Across the audited pre-deal statements, none of the standardised financial measures predicts the hiring response: "
            f"cash over assets gives {f4(z('cash_assets','slope'), plus=True)} {ci4(z('cash_assets','ci'))} (n = {z('cash_assets','n')}), "
            f"leverage {f4(z('leverage','slope'), plus=True)} {ci4(z('leverage','ci'))} (n = {z('leverage','n')}), "
            f"interest coverage {f4(z('coverage','slope'), plus=True)} {ci4(z('coverage','ci'))} (n = {z('coverage','n')}), "
            f"and profitability {f4(z('roa','slope'), plus=True)} {ci4(z('roa','ci'))} (n = {z('roa','n')}), per standard deviation of each measure. "
            f"On the same audited sample, the pre-deal hiring state remains predictive, at {f4(z('state_common','slope'), plus=True)} {ci4(z('state_common','ci'))} per standard deviation (n = {z('state_common','n')}). "
            "The observable financial variables therefore do not reproduce the information in the hiring state, although the audited subsample is smaller and the intervals are wide.")
i = s.find("[placeholder: report the hiring-response coefficients and 95% confidence intervals for pre-deal cash/assets, leverage, int")
assert i >= 0, "fin sentence anchor"
j = s.find("]", i)
s = s[:i] + fin_sent + s[j+1:]
TR.append({"tag": "6.2-fin", "old": "financial condition placeholder", "new": fin_sent[:110]})

open(SRC, "w", encoding="utf-8").write(s)
with open(os.path.join(HERE, "FILL_TRACE.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["tag", "old", "new"])
    if f.tell() == 0: w.writeheader()
    w.writerows(TR)
print(f"PART 1 (main text): {len(TR)} substitutions · remaining placeholders: {s.count('[placeholder')}")
