"""
MATERIAL A -- dual realisation (CONSTRUCTIVE, no audit).  v2: COMPLETE subgroup enumeration.
Object: subgroups of G = (Z/n)^2 (all of them: every subgroup of an abelian 2-generated group needs <=2 generators).
Natural operations:
   P = a symplectic isometry (e.g. Weyl w = [[0,-1],[1,0]])
   Q = symplectic complement Lambda -> Lambda^perp
Theorem (one line): for any isometry g of the form, (gL)^perp = g(L^perp), hence g o Q = Q o g.
This script verifies the theorem on the COMPLETE subgroup lattice and measures the balanced locus.
"""
def elems(n): return [(x,y) for x in range(n) for y in range(n)]
def symp(v,u,n): return (v[0]*u[1]-v[1]*u[0])%n

def closure(gens,n):
    S={(0,0)}; frontier=[(0,0)]
    while frontier:
        v=frontier.pop()
        for g in gens:
            u=((v[0]+g[0])%n,(v[1]+g[1])%n)
            if u not in S: S.add(u); frontier.append(u)
    return frozenset(S)

def all_subgroups(n):
    E=elems(n); subs=set()
    for g1 in E:
        for g2 in E:
            subs.add(closure([g1,g2],n))
    return subs

def complement(L,n):
    return frozenset(v for v in elems(n) if all(symp(l,v,n)==0 for l in L))
def weyl(L,n): return frozenset(((-v[1])%n, v[0]) for v in L)

print("="*94); print("COMPLETE subgroup lattice: P (Weyl isometry) vs Q (complement)"); print("="*94)
print(f"  {'n':>3} | {'#subgroups (complete)':>21} | {'#commuting':>11} | {'#Lagrangian':>12} | all commute? | Lagrangian orders | == sqrt(|G|)=n ?")
print("  "+"-"*92)
rows=[]
for n in (2,3,4,5,6,7,8,9,10,12):
    subs=all_subgroups(n)
    comm=sum(1 for L in subs if weyl(complement(L,n),n)==complement(weyl(L,n),n))
    lag=[L for L in subs if complement(L,n)==L]
    orders=sorted(set(len(L) for L in lag))
    rows.append((n,len(subs),comm,len(lag),orders))
    print(f"  {n:>3} | {len(subs):>21} | {comm:>11} | {len(lag):>12} | {str(comm==len(subs)):>12} | {orders} | {orders==[n]}")
print()
print("  checks against textbook counts of subgroups of (Z/p)^2 : 1 + (p+1) + 1 = p+3")
for p in (2,3,5,7):
    subs=all_subgroups(p)
    print(f"    p={p}: #subgroups = {len(subs)}   expected p+3 = {p+3}   match: {len(subs)==p+3}")
print()
print("="*94); print("the balance locus (Lagrangian = self-complementary) and its order"); print("="*94)
for n,c,cc,nl,orders in rows:
    print(f"  n={n:>3}: |G|={n*n:>4}  sqrt(|G|)={n:>3}  |Lagrangian|={nl:>3}  Lagrangian orders={orders}  "
          f"all == sqrt(|G|)? {orders==[n]}")
print()
print("  => on the COMPLETE lattice, every symplectic isometry commutes with the complement (as the one-line")
print("     theorem predicts), and the self-dual (balanced) subgroups have order exactly sqrt(|G|).")
print()
print("="*94); print("is there ANY non-commuting natural pair here? the isometry group cannot supply one:"); print("="*94)
print("""  proof: v in (gL)^perp  <=>  omega(v, g*l) = 0 for all l  <=>  omega(g^-1 v, l) = 0 for all l
          <=>  g^-1 v in L^perp  <=>  v in g(L^perp).        Hence g o Q = Q o g for EVERY isometry g.
  ==> a non-commutation defect requires a natural operation that is NOT an isometry of the form.
      natural non-isometric candidates: scaling L -> mL  (defect turns out to be exactly quadratic, m^2),
      or ideal inversion in a non-PID (material B). The isometry route is CLOSED BY THIS THEOREM, not by audit.""")
