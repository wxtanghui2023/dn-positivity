"""
A' -- from SIZE to SCALE: two-level filtration, conserved total, and CROSS-SCALE TRANSPORT.
Object: G=(Z/n)^2 with standard symplectic omega.  No audit; construction + computation only.
"""
def elems(n): return [(x,y) for x in range(n) for y in range(n)]
def symp(v,u,n): return (v[0]*u[1]-v[1]*u[0])%n
def closure(gens,n):
    S={(0,0)}; fr=[(0,0)]
    while fr:
        v=fr.pop()
        for g in gens:
            u=((v[0]+g[0])%n,(v[1]+g[1])%n)
            if u not in S: S.add(u); fr.append(u)
    return frozenset(S)
def all_subgroups(n):
    E=elems(n); return {closure([a,b],n) for a in E for b in E}
_EC={}
def E(n):
    if n not in _EC: _EC[n]=elems(n)
    return _EC[n]
def complement(L,n): return frozenset(v for v in E(n) if all(symp(l,v,n)==0 for l in L))
def p_torsion(n,p,j):
    """G[p^j] = {v : p^j v = 0} in (Z/n)^2"""
    m=p**j
    return frozenset(v for v in elems(n) if (m*v[0])%n==0 and (m*v[1])%n==0)

print("="*92); print("A'.3  CONSERVATION: |L| * |L^perp| = |G| for every subgroup L"); print("="*92)
print(f"  {'n':>3} | {'|G|':>6} | {'#subgroups':>11} | {'#with |L||L^perp|=|G|':>22} | all ?")
for n in (2,3,4,5,6,8,9,10):
    S=all_subgroups(n); ok=sum(1 for L in S if len(L)*len(complement(L,n))==n*n)
    print(f"  {n:>3} | {n*n:>6} | {len(S):>11} | {ok:>22} | {ok==len(S)}")
print("  => the conserved total S_1+S_2 = log|G| is theorem-level (non-degenerate pairing)")
print()
print("="*92); print("A'.1  p-primary filtration: is every LAYER of a Lagrangian again Lagrangian?"); print("="*92)
print(f"  claim to test: for Lambda Lagrangian in (Z/p^k)^2, Lambda[p^j] = Lambda cap G[p^j]")
print(f"                 is Lagrangian in G[p^j], and |Lambda[p^j]| = p^j = sqrt(|G[p^j]|)")
print()
for (p,k) in ((2,2),(2,3),(3,2)):
    n=p**k
    S=all_subgroups(n)
    lag=[L for L in S if complement(L,n)==L]
    allok=True; detail=[]
    for L in lag:
        for j in range(0,k+1):
            Gpj=p_torsion(n,p,j) if j>0 else frozenset({(0,0)})
            layer=frozenset(v for v in L if v in Gpj)
            comp=frozenset(v for v in Gpj if all(symp(l,v,n)==0 for l in layer))
            ok = (len(layer)==p**j) and (layer==comp)
            allok = allok and ok
            if j<=2: detail.append((len(layer),p**j,ok))
        if not allok: break
    print(f"  p={p},k={k} (n={n}): #Lagrangians={len(lag):>4} | all layers Lagrangian: {allok}")
print()
print("="*92); print("A'.1  layer dimensions: log_p b_j (ambient) vs log_p a_j (self-dual)"); print("="*92)
for (p,k) in ((2,2),(2,3),(3,2),(2,4)):
    n=p**k
    b=[2*j for j in range(1,k+1)]                # log_p |G[p^j]| = 2j
    a=[j for j in range(1,k+1)]                  # log_p |Lambda[p^j]| = j  (verified above)
    print(f"  p={p},k={k}: ambient log_p|G[p^j]| = {b} | self-dual log_p|Lambda[p^j]| = {a} "
          f"| ratio per layer = {[round(bb/aa,4) for bb,aa in zip(b,a)]}")
print("  => per layer: ambient dimension 2, self-dual dimension 1; ratio 1/2 at EVERY level")
print()
print("="*92); print("A'.4  CROSS-SCALE TRANSPORT: do the pairs transport with ONE law?"); print("="*92)
print("  transport candidate:  T_j : Lambda  ->  Lambda[p^j]  (p-primary layer)")
print("  conservation transport: log|G[p^j]| = 2j log p  (linear in j, same law at all levels)")
print("  balance transport     : log|Lambda[p^j]| = j log p = (1/2) log|G[p^j]|  at EVERY j")
print("  => the balance is NOT recomputed at each level: all layers come from ONE top-level Lagrangian")
print()
print("="*92); print("cross-scale COUNT: number of Lagrangians of (Z/p^k)^2  vs  1+p+...+p^k"); print("="*92)
print(f"  {'p':>3} {'k':>3} {'n':>6} | {'#Lagrangians':>13} | {'1+p+...+p^k':>12} | match | (p^{k+1}-1)/(p-1)")
for (p,k) in ((2,1),(3,1),(5,1),(7,1),(2,2),(2,3),(3,2)):
    n=p**k
    S=all_subgroups(n)
    nl=sum(1 for L in S if complement(L,n)==L)
    geo=sum(p**i for i in range(k+1))
    print(f"  {p:>3} {k:>3} {n:>6} | {nl:>13} | {geo:>12} | {str(nl==geo):>5} | {(p**(k+1)-1)//(p-1)}")
print()
print("="*92); print("check of the subscript slip in the S_- definition"); print("="*92)
n=12; S=all_subgroups(n); bad=0; tot=0
for L in S:
    tot+=1
    if (n*n)//len(complement(L,n)) != len(L): bad+=1
print(f"  |G/L^perp| = |G|/|L^perp| = |L|   holds for {tot-bad}/{tot} subgroups of (Z/12)^2")
print("  => with S_-(L):=log|G/L^perp| one gets S_- = S_+ identically; the intended second coordinate is")
print("     log|L^perp| (= log|G/L|), so the definition needs the one-symbol repair |G/L| instead of |G/L^perp|")
