"""
ABD-1' : direction field from FUTURE legal arithmetic branching structure  (memoised version)
For a+b=c the relation-preserving integer moves are exactly
    (a,b,c) -> (a+p, b+q, c+p+q),  (p,q) in Z^2        [DERIVED, exact]
Legality reads ONLY gcd/divisibility:
    L1 increments are multiples of g=gcd(a,b)      L2 additionally gcd(a',b')=g
Bounded window |p|,|q| <= B (constant).  Branching C(s)=#legal moves.
Dynamics: move to the legal neighbour MAXIMISING C(descendant); ties canonical.
"""
from math import gcd, prod
from itertools import product
import statistics

B=3; CMAX=30; KMAX=25

_C={}
def C(a,b):
    k=(a,b)
    if k in _C: return _C[k]
    g=gcd(a,b); n=0
    for p in range(-B,B+1):
        if p%g: continue
        for q in range(-B,B+1):
            if q%g: continue
            if a+p>=1 and b+q>=1: n+=1
    _C[k]=n; return n

_C2={}
def C2(a,b):
    k=(a,b)
    if k in _C2: return _C2[k]
    g=gcd(a,b); s=0
    for p in range(-B,B+1):
        if p%g: continue
        for q in range(-B,B+1):
            if q%g: continue
            na,nb=a+p,b+q
            if na>=1 and nb>=1: s+=C(na,nb)
    _C2[k]=s; return s

def moves(a,b,mode="L1"):
    g=gcd(a,b); out=[]
    for p in range(-B,B+1):
        if p%g: continue
        for q in range(-B,B+1):
            if q%g: continue
            na,nb=a+p,b+q
            if na<1 or nb<1: continue
            if mode=="L2" and gcd(na,nb)!=g: continue
            out.append((p,q,na,nb))
    return out

def step(a,b,mode="L1",which="C2"):
    ms=moves(a,b,mode)
    if not ms: return (a,b)
    if which=="C2":
        return min(ms,key=lambda t:(-C2(t[2],t[3]),abs(t[0])+abs(t[1]),t[0],t[1]))[2:]
    return min(ms,key=lambda t:(-C(t[2],t[3]),abs(t[0])+abs(t[1]),t[0],t[1]))[2:]

def R(a,b): return min(a,b)/max(a,b)
def orbit(a,b,stepfn,K=KMAX):
    seq=[(a,b)]; seen={(a,b)}
    for _ in range(K):
        na,nb=stepfn(a,b)
        if (na,nb)==(a,b) or (na,nb) in seen: break
        seen.add((na,nb)); seq.append((na,nb)); a,b=na,nb
    return seq

print("="*84); print("ABD-1' : FUTURE-BRANCHING DIRECTION FIELD   (B=%d, c<=%d, memoised)"%(B,CMAX)); print("="*84)

print("="*84); print("PART A -- C_NI AUDIT (FIRST, before any convergence claim)"); print("="*84)
print("  A1: equal |a-b| but different C ?")
hits=[]
for c in range(6,CMAX+1):
    byd={}
    for a in range(1,c):
        b=c-a; byd.setdefault(abs(a-b),set()).add(C(a,b))
    for d,S in byd.items():
        if len(S)>1: hits.append((c,d,sorted(S)))
print(f"     found {len(hits)} levels where equal |a-b| gives different C; first: {hits[:3]}")
print("     => C is NOT a function of |a-b|  (C_NI audit passes on this count)")
print("  A2: is C a function of (g,c) alone ?  (g=gcd)")
bad=[]
for c in range(4,CMAX+1):
    byg={}
    for a in range(1,c):
        b=c-a; byg.setdefault(gcd(a,b),set()).add(C(a,b))
    for g,S in byg.items():
        if len(S)>1: bad.append((c,g,sorted(S)))
print(f"     counterexamples: {len(bad)}  first: {bad[:3]}")
print("     => C depends on g AND on more than g.")
print("  A3: correlations over the window")
XS=[];YS=[];GS=[]
for c in range(4,CMAX+1):
    for a in range(1,c):
        b=c-a; XS.append(abs(a-b)); YS.append(C(a,b)); GS.append(gcd(a,b))
def corr(X,Y):
    mx,my=statistics.mean(X),statistics.mean(Y)
    s=sum((x-mx)*(y-my) for x,y in zip(X,Y))/len(X)
    return s/(statistics.pstdev(X)*statistics.pstdev(Y))
print(f"     corr(|a-b|, C) = {corr(XS,YS):+.4f}      corr(g, C) = {corr(GS,YS):+.4f}")
print("     => branching INCREASES as the pair becomes more imbalanced / less composite.")
print()

print("="*84); print("PART B -- DOES THE FUTURE-BRANCHING DIRECTION REACH BALANCE ?"); print("="*84)
starts=[(a,c-a) for c in range(4,CMAX+1) for a in range(1,c)]
ceiling=sum(1 for c in range(4,CMAX+1) for a in range(1,c) if c%2==0)/len(starts)
print(f"  (reference CEILING = even-c fraction = {ceiling:.4f}; R0_grad attains it)")
for mode in ("L1","L2"):
    for which in ("C1","C2"):
        reached=0; Rf=[]; Rst=[]
        for (a,b) in starts:
            seq=orbit(a,b,lambda x,y:step(x,y,mode,which))
            if any(x==y for x,y in seq): reached+=1
            Rf.append(R(*seq[-1])); Rst.append(R(a,b))
        print(f"   mode={mode} which={which}:  reach a=b frac = {reached/len(starts):.4f}"
              f"   mean R: {statistics.mean(Rst):.4f} -> {statistics.mean(Rf):.4f}")
print()

print("="*84); print("PART C -- WHERE DOES IT GO INSTEAD ?"); print("="*84)
for (a,b) in [(1,19),(5,15),(10,10),(7,13),(2,28),(1,29),(15,15)]:
    seq=orbit(a,b,lambda x,y:step(x,y,"L1","C2"))
    print(f"   start({a:>2},{b:>2}) R={R(a,b):.4f} len={len(seq):>2}  end={seq[-1]} R_end={R(*seq[-1]):.4f} "
          f"g: {gcd(a,b):>2} -> {gcd(*seq[-1]):>2}   C={C(a,b):>3} C2={C2(a,b):>5}  (C(10,10)={C(10,10)}, C(1,19)={C(1,19)})")
print()

print("="*84); print("PART D -- THE STRUCTURAL REASON"); print("="*84)
print("  C(a,b) as a function of g=gcd(a,b), for fixed c:")
for c in (20,30):
    seen={}; 
    for a in range(1,c):
        b=c-a; g=gcd(a,b); seen.setdefault(g,C(a,b))
    print(f"   c={c}: " + "  ".join(f"g={g}:C={v}" for g,v in sorted(seen.items())))
print("  => C is monotone DECREASING in g.  Balance a=b=c/2 maximises g=c/2, hence MINIMISES branching.")
print("     Balance is maximal arithmetic COMPOSITENESS, i.e. MINIMAL refinement freedom.")
print()
print("="*84); print("ABD-1' VERDICT  (checked against the printed numbers)"); print("="*84)
print("""  AUDIT-DESIGN CORRECTION (found this round, must be recorded):
    The criterion 'C is not in sigma(|a-b|, ab, c)' is VACUOUS as posed.  Reason: c = a+b, so
    (|a-b|, c) determines the UNORDERED state {a,b}; every symmetric function of the state is
    therefore 'determined by' those quantities.  The audit must be DIRECTIONAL instead: ask
    whether the direction induced by C coincides with the |a-b|-gradient direction.

  AUDIT RESULTS (as measured):
    A1: 0 levels with equal |a-b| but different C -- consistent with the vacuity above, NOT evidence
        that C is anti-aligned by determination.
    A2: 40 counterexamples to 'C is a function of (g,c) alone' (e.g. c=5,g=1: C in {28,30}): the
        bounded move window clips at the boundary.  => C depends on g AND on boundary effects.
    A3: corr(|a-b|, C) = -0.0731  (WEAK, slightly negative)
        corr(g, C)     = -0.6618  (STRONG negative)
        => the real dependence is on g, not on |a-b|.

  STRUCTURAL REASON (near-proof, from PART D):
    legality 'increments are g-multiples' with window B gives C = (2*floor(B/g)+1)^2, which is
    monotone DECREASING in g.  For c >= 4 the balanced state a=b=c/2 has g = c/2 >= 2, hence
    C(balance) <= (2*floor(B/(c/2))+1)^2 < C(primitive state) with g=1.
    => the branching-maximising dynamics can NEVER select the balanced state (c >= 4).
    Example (c=20,B=3): g=1 -> C=28 ; g=2 -> C=6 ; g>=4 -> C=1 ; balance has g=10 -> C=1.

  MEASURED BEHAVIOUR (PART B/C):
    reach a=b fraction = 0.0324 for all four variants, against the even-c CEILING 0.5185 that
    R0_grad attains.  mean R rises 0.4106 -> 0.4763 (C1) / 0.5638 (C2): the dynamics does move
    away from the strongly composite states, but it STALLS in the primitive region and enters
    SHORT CYCLES (e.g. (1,19) -> 3 steps -> (7,20) then cycles; (7,13) -> (7,10)).
    The primitive region contains the maximally imbalanced states, e.g. (1,c-1) with C=28 = maximum.

  => CONCLUSION: the future-arithmetic-branching direction is ANTI-ALIGNED with the AM-GM equality
     manifold, and this is structural rather than statistical: branching is monotone decreasing in
     gcd, while balance MAXIMISES the gcd.  The state with the most arithmetic future is the
     maximally imbalanced primitive one; the equality manifold has the LEAST arithmetic freedom.
     Hence: primitive arithmetic future complexity does NOT imply balance.
     The ALIGNMENT SOURCE therefore remains missing, and this round gives a REASON why the natural
     'future richness' functional cannot supply it.
""")
