"""verify the radical threshold: omega restricted to G[p^j] vanishes identically iff j <= k/2"""
def elems(n): return [(x,y) for x in range(n) for y in range(n)]
def symp(v,u,n): return (v[0]*u[1]-v[1]*u[0])%n
print("="*86); print("radical threshold: is omega|G[p^j] identically zero?"); print("="*86)
print(f"  {'p':>3}{'k':>3}{'n':>5} | {'j':>3} | {'omega==0 on G[p^j] ?':>22} | {'j <= k/2 ?':>11} | agree?")
for (p,k) in ((2,2),(2,3),(3,2),(2,4)):
    n=p**k; okall=True
    for j in range(1,k+1):
        m=p**j
        Gpj=[v for v in elems(n) if (m*v[0])%n==0 and (m*v[1])%n==0]
        zero=all(symp(v,u,n)==0 for v in Gpj for u in Gpj)
        pred=(j*2<=k)
        okall = okall and (zero==pred)
        print(f"  {p:>3}{k:>3}{n:>5} | {j:>3} | {str(zero):>22} | {str(pred):>11} | {zero==pred}")
    print(f"      => threshold rule holds for p={p},k={k}: {okall}")
print()
print("  consequence: for j <= k/2 the restricted form is totally degenerate, so 'self-complementary inside")
print("  G[p^j]' is VACUOUS there (every subgroup equals its own complement); the earlier cyclic=False /")
print("  non-cyclic=True verdicts at small j are ARTIFACTS of that degeneracy, not structure.")
print("  the meaningful, verification-grade statement about layers is about SIZE: |Lambda[p^j]| = p^j iff Lambda cyclic.")
