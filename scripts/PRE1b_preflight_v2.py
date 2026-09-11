
"""
PRE1b (v2): pre-flight filter, repaired.
  v1 flaw (self-reference): R1 killed our OWN findings, because findings are recorded in
  the corpus.  Fix: distinguish claim_type.
     claim_type = "explore"  -> proposing a NEW mechanism to pursue: R1 applies
     claim_type = "finding"  -> reporting an elimination/result:  R1 EXEMPT (it is ours)
  Also R1 requires an explicit `difference` declaration when registry hits exist.
"""
import os, glob
ROOTS=["/home/node/.openclaw/workspace/dn-project/docs",
       "/home/node/.openclaw/workspace/memory",
       "/home/node/.openclaw/workspace"]
files=[]
for r in ROOTS: files += glob.glob(os.path.join(r,"*.md"))
files=[f for f in files if os.path.isfile(f)]
corpus={f:open(f,encoding="utf-8",errors="ignore").read().lower() for f in files}
CLOSING=["判死","closed","no-go","nogo","dead","已排除","已否决","stall","停滞"]
def hits(keywords):
    d={}
    for f,t in corpus.items():
        n=sum(t.count(k.lower()) for k in keywords)
        if n>0: d[f]=n
    return d
def closed_hits(keywords):
    """hits where the doc ALSO carries closing markers => the object was already closed"""
    out={}
    for f,n in hits(keywords).items():
        t=corpus[f]
        if any(c in t for c in CLOSING): out[f]=n
    return out
def check(name, keywords, claim_type, target=None, falsifier=None, difference=None):
    reasons=[]
    if claim_type=="explore":
        ch=closed_hits(keywords)
        if ch and not difference:
            worst=max(ch,key=ch.get)
            reasons.append(f"R1 core object already CLOSED in {len(ch)} doc(s) e.g. {os.path.basename(worst)}")
        if not difference and not ch:
            pass
    if target=="" or target is None: reasons.append("R4 no eliminated class / proved statement named")
    if falsifier=="" or falsifier is None: reasons.append("R5 no falsification criterion")
    if claim_type=="necessary": reasons.append("R2 necessary-only => zero leverage")
    v="KILL" if reasons else "PASS"
    print(f"  [{v}] {name}")
    for r in reasons: print(f"          - {r}")
    return v
print("="*92); print("V2 BACKTEST on this session's own proposals"); print("="*92)
check("① Arakelov/Faltings-Hriljac as positivity source",["arakelov","faltings"],"explore")
check("② Selberg spectral realisation",["selberg"],"explore")
check("③ Connes scaling site",["connes","scaling site"],"explore")
check("④ Deninger cohomology",["deninger"],"explore")
check("⑤ no-common-carrier formulation",["common carrier"],"necessary",target=None,falsifier=None)
check("⑥ Newton baseline + excess",["newton","turan"],"necessary",target=None,falsifier="one n with r_n<(n+1)/n")
check("⑦ Guinand phase-locking sensitivity (OUR finding)",["guinand","phase lock"],"finding",
      target="kills 'statistical uniformity' as the mechanism; keeps exact phase alignment",
      falsifier="reproduce the O(1) suppression with randomised phases")
check("⑧ Phi kernel TP5 failure (OUR finding)",["total positivity","polya frequency"],"finding",
      target="eliminates the positive-kernel/TP family of sufficient conditions",
      falsifier="exhibit a TP5-repair or a reparametrisation restoring all-order positivity")
print()
print("="*92); print("READ-OFF"); print("="*92)
print("""  * ①②③④ KILL: they are closed and I re-proposed them => the exact spinning.
  * ⑤⑥ KILL: necessary-condition artifacts => zero leverage (the error class I repeated 3x).
  * ⑦⑧ PASS: they are OUR findings, each naming an eliminated class + a falsifier.
  * => Institutional rule from now on: NOTHING is explored unless it PASSES this filter.""")

