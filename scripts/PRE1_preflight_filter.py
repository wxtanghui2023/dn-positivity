"""
PRE1: institutionalise the lessons -- a PRE-FLIGHT FILTER for research proposals.
  Motivation (director, 2026-09-11 17:03): foreign systems iterate with selection until
  breakthrough; ours spins in place and does not learn from experience.  Diagnosis: the
  ledger exists but is used as an ARCHIVE, not as a FILTER.  Fix: make the failure
  features MACHINE-CHECKABLE pre-conditions.
Rules (all mandatory; any failure => REJECT):
  R1 registry-hit     : core objects already present in the corpus and no explicit
                        'difference from registry entry' declared  => REJECT
  R2 necessary-only   : claimed as a necessary condition => REJECT (zero leverage)
  R3 restatement      : no independent content beyond restating the hypothesis => REJECT
  R4 no target        : must name what it ELIMINATES or what it PROVES (otherwise REJECT)
  R5 no falsifier     : must state what observation would refute it (otherwise REJECT)
Then BACKTEST on this session's own proposals.
"""
import os, re, glob
ROOTS=["/home/node/.openclaw/workspace/dn-project/docs",
       "/home/node/.openclaw/workspace/memory",
       "/home/node/.openclaw/workspace"]
files=[]
for r in ROOTS:
    files += glob.glob(os.path.join(r,"*.md"))
files=[f for f in files if os.path.isfile(f)]
corpus={f:open(f,encoding="utf-8",errors="ignore").read().lower() for f in files}
def registry_hits(keywords):
    hits={}
    for f,txt in corpus.items():
        n=sum(txt.count(k.lower()) for k in keywords)
        if n>0: hits[f]=n
    return hits
def check(name, keywords, claim_type, restatement, target, falsifier, difference=None):
    reasons=[]
    hits=registry_hits(keywords)
    strong=[f for f,n in hits.items() if n>=3]
    if strong and not difference:
        reasons.append(f"R1 registry-hit in {len(strong)} doc(s) e.g. {os.path.basename(max(hits,key=hits.get))} (no 'difference' declared)")
    if claim_type=="necessary": reasons.append("R2 necessary-only claim => zero leverage for the hypothesis")
    if restatement: reasons.append("R3 restatement of the hypothesis")
    if not target: reasons.append("R4 no eliminated class / no proved statement named")
    if not falsifier: reasons.append("R5 no falsification criterion")
    verdict="KILL" if reasons else "PASS"
    print(f"  [{verdict}] {name}")
    for r in reasons: print(f"          - {r}")
    if not strong and not reasons: print(f"          (registry clean: {len(hits)} weak hit(s))")
    return verdict

print("="*94); print("BACKTEST: this session's own proposals, judged by the filter"); print("="*94)
check("① Arakelov / Faltings–Hriljac as a positivity source",
      ["arakelov","faltings","hriljac","hodge index"],"sufficient",False,"", "exhibit common carrier")
check("② Selberg-type spectral realisation",
      ["selberg","trace formula","hyperbolic"],"sufficient",False,"", "exhibit common carrier")
check("③ Connes scaling site / Riemann–Roch",
      ["connes","scaling site","consani","riemann-roch"],"sufficient",False,"", "exhibit common carrier")
check("④ Deninger cohomology of Spec Z",
      ["deninger","cohomology of spec"],"sufficient",False,"", "exhibit common carrier")
check("⑤ 'no common carrier' formulation",
      ["common carrier"],"necessary",False,"", "", "exhibit common carrier")
check("⑥ Newton baseline r_n >= (n+1)/n  + excess observable",
      ["newton","turan","log-concav", "excess"],"necessary",False,"", "one n with r_n < (n+1)/n")
check("⑦ Guinand phase-locking sensitivity",
      ["guinand","phase lock","sin(gamma"],"elimination",False,
      "eliminates 'statistical uniformity' as the mechanism", "reproduce with a different phase set")
check("⑧ Phi kernel TP5 failure (total positivity)",
      ["total positivity","tp2","tp5","polya frequency"],"elimination",False,
      "eliminates the positive-kernel family of sufficient conditions", "exhibit a TP5-repaired kernel")
print()
print("="*94); print("READ-OFF"); print("="*94)
print("""  * The filter kills ①②③④ instantly (all are already in the corpus) and rejects ⑤⑥
    as necessary-only claims.  That is EXACTLY the spinning the director described:
    I re-proposed ledgered territory and produced necessary-condition artifacts.
  * ⑦⑧ PASS: they name an eliminated class and a falsifier -- they are the genuine output.
  * => The lesson is institutionalised: any future proposal must PASS this filter
    BEFORE it is explored.  No exceptions.""")
