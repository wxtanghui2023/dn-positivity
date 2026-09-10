"""diagnose: WHY do some Lagrangians fail the per-layer claim of A'.1 ?"""
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
def complement(L,n): return frozenset(v for v in elems(n) if all(symp(l,v,n)==0 for l in L))
def order_of(v,n):
    o=1; x=v
    while x!=(0,0):
        x=((x[0]+v[0])%n,(x[1]+v[1])%n); o+=1
    return o
def is_cyclic(L,n):
    return any(order_of(v,n)==len(L) for v in L)

print("="*94); print("WHY some Lagrangians fail A'.1 : cyclic vs non-cyclic maximal isotropic subgroups"); print("="*94)
for (p,k) in ((2,2),(2,3),(3,2)):
    n=p**k
    S=all_subgroups(n); lag=[L for L in S if complement(L,n)==L]
    cyc=[L for L in lag if is_cyclic(L,n)]; ncyc=[L for L in lag if not is_cyclic(L,n)]
    print(f"\n  p={p},k={k} (n={n}): #Lagrangians={len(lag)}  cyclic={len(cyc)}  non-cyclic={len(ncyc)}")
    for tag,group in (('cyclic   ',cyc[:2]),('non-cyclic',ncyc[:2])):
        for L in group:
            sizes=[]
            for j in range(0,k+1):
                m=p**j
                Gpj={v for v in elems(n) if (m*v[0])%n==0 and (m*v[1])%n==0}
                layer={v for v in L if v in Gpj}
                sizes.append(len(layer))
            print(f"    {tag} |L|={len(L):>4}  layer sizes |L[p^j]| j=0..k = {sizes}   "
                  f"expected p^j = {[p**j for j in range(k+1)]}   match: {sizes==[p**j for j in range(k+1)]}")
    # claim: layer sizes == p^j  iff  L cyclic
    ok = all(( [len({v for v in L if (p**j*v[0])%n==0 and (p**j*v[1])%n==0}) for j in range(k+1)]
               == [p**j2 for j2 in range(k+1)]) == is_cyclic(L,n) for L in lag)
    print(f"    => 'layers are exactly p^0..p^k'  <=>  'L is cyclic'   :  {ok}")
print()
print("="*94); print("counts: total / cyclic / non-cyclic Lagrangians of (Z/p^k)^2"); print("="*94)
print(f"  {'p':>3}{'k':>3}{'n':>5} | {'#Lagrangians':>13} | {'1+p+..+p^k':>11} | {'#cyclic':>8} | {'#non-cyclic':>12} | {'phi(p^k)=p^k-p^{k-1}':>21}")
for (p,k) in ((2,1),(3,1),(5,1),(2,2),(2,3),(3,2)):
    n=p**k; S=all_subgroups(n); lag=[L for L in S if complement(L,n)==L]
    cyc=sum(1 for L in lag if is_cyclic(L,n))
    print(f"  {p:>3}{k:>3}{n:>5} | {len(lag):>13} | {sum(p**i for i in range(k+1)):>11} | {cyc:>8} | {len(lag)-cyc:>12} | {p**k-p**(k-1):>21}")
print()
print("="*94); print("does the BALANCE LAW transport along the filtration for cyclic Lagrangians?"); print("="*94)
print("  for cyclic Lambda:  log_p|Lambda[p^j]| = j ,  log_p|G[p^j]| = 2j  => ratio 1/2 at EVERY j  (transported, not recomputed)")
print("  for non-cyclic Lambda: the layers are NOT one-dimensional, so the 1/2 ratio is not per-layer")

print()
print("="*94); print("FINAL CHECK: for CYCLIC Lambda, is the layer Lambda[p^j] self-complementary inside G[p^j]?"); print("="*94)
for (p,k) in ((2,2),(2,3),(3,2)):
    n=p**k
    E=elems(n)
    def Gpj(j):
        m=p**j
        return {v for v in E if (m*v[0])%n==0 and (m*v[1])%n==0}
    def iscyc(L):
        return any(order_of(v,n)==len(L) for v in L)
    S=all_subgroups(n); lag=[L for L in S if complement(L,n)==L]
    cyc=[L for L in lag if iscyc(L)]; ncyc=[L for L in lag if not iscyc(L)]
    def layer_comp_ok(L,j):
        Gj=Gpj(j); layer={v for v in L if v in Gj}
        comp={v for v in Gj if all(symp(l,v,n)==0 for l in layer)}
        return layer==comp, len(layer), len(comp)
    okc=all(layer_comp_ok(L,j)[0] for L in cyc for j in range(0,k+1))
    okn=all(layer_comp_ok(L,j)[0] for L in ncyc for j in range(0,k+1)) if ncyc else True
    print(f"  p={p},k={k}: cyclic Lagrangians: all layers self-complementary in G[p^j] = {okc}  "
          f"| non-cyclic: {okn}  (ncyc={len(ncyc)})")
    if ncyc:
        L=ncyc[0]
        for j in range(0,k+1):
            ok,l,c=layer_comp_ok(L,j)
            print(f"      non-cyclic example at j={j}: |layer|={l}  |complement in G[p^j]|={c}  equal={ok}")
