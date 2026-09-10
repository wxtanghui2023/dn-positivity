"""
ABD-0: Arithmetic Balance Defect -- canonical integer refinement + transfer rho(alpha).
Optimised version: heavy sums replaced by (a) closed form C(alpha)=B(1+a,1+a) and
(b) precomputed per-state roots for a bounded range.
NO zeta / Mellin / zeros / FE.  Offspring forced by a+b=c, ab.
"""
from math import log, exp, lgamma

def m_scale(a,b,c): return (a*b)/(c*c)
def C(alpha): return exp(2.0*lgamma(1.0+alpha)-lgamma(2.0+2.0*alpha))   # int_0^1 (r(1-r))^a dr

def bisect(f, lo=1e-12, hi=60.0, tol=1e-14, it=200):
    flo, fhi = f(lo), f(hi)
    if flo*fhi > 0: return None
    for _ in range(it):
        mid=0.5*(lo+hi); fm=f(mid)
        if flo*fm<=0: hi,fhi=mid,fm
        else: lo,flo=mid,fm
        if hi-lo<tol: break
    return 0.5*(lo+hi)

print("="*76); print("ABD-0 / PART 1 : arithmetic pin  m = ab/c^2 <= 1/4  (AM-GM, exact)"); print("="*76)
worst=(0.0,None); tie=0
for c in range(2,1501):
    for a in range(1,c):
        m=m_scale(a,c-a,c)
        if m>worst[0]+1e-18: worst=(m,(a,c-a,c))
        if abs(m-0.25)<1e-15: tie+=1
print(f"  m_max over c<=1500 : {worst[0]!r} at (a,b,c)={worst[1]}")
print(f"  #triples with m=1/4 exactly : {tie}  (all a=b, i.e. exact additive balance)")
print("  => exponent pinned from ABOVE by pure arithmetic; not inserted\n")

print("="*76); print("ABD-0 / PART 2 : choice-free refinement (ALL splits) -- root alpha_*(c)"); print("="*76)
def rho_full(c,al): return sum((x*(c-x)/(c*c))**al for x in range(1,c))
print("     c        alpha_*(c)        rho(1/2)      c*C(alpha_*)")
for c in (10,50,100,200,400,800):
    r=bisect(lambda al: rho_full(c,al)-1.0)
    print(f"  {c:>5}   {r:>13.9f}   {rho_full(c,0.5):>13.4e}   {c*C(r):>10.4f}")
print("  => root exists BY ITSELF but alpha_*(c) DIVERGES like (1/2)*log2(c) : NO stable")
print("     neutral constant.  (branching # ~ c grows linearly while every child scale")
print("     is <= 1/4 < 1, so alpha must be pushed up to bring the sum down to 1)\n")

print("="*76); print("ABD-0 / PART 3 : closed-form cross-check for large c :  c*C(alpha)=1"); print("="*76)
for c in (100,1000,10000,100000,10**6):
    r=bisect(lambda al: c*C(al)-1.0)
    print(f"   c={c:>8}   alpha_* = {r:.9f}   (1/c-correction ~ {2*(1-log(2))/c:.2e})")
print("  => confirms DIVERGENCE: C(0)=1 and C decreasing => root of c*C(a)=1 grows with c")
print("  ratio alpha_*/log2(c) -> 1/2 SLOWLY (0.454 at c=1e6); the 1/2 is again 1/arity,")
print("  since the maximal child scale is 1/4 = 2^-2:")
for c in (100,1000,10000,100000,10**6):
    r=bisect(lambda al: c*C(al)-1.0)
    print(f"   c={c:>8}   alpha_*/log2(c) = {r/log(c,2):.6f}")
print()

print("="*76); print("ABD-0 / PART 4 : where is the root exactly 1/2 ?  (uniform k-child)"); print("="*76)
print("  uniform k children, common scale m :  root of k*m^a=1  <=>  a = log k / log(1/m)")
for k in (2,3,4):
    for m in (0.25, 0.125, 0.1, 1.0/(k*k)):
        a=log(k)/log(1.0/m); f="   <== =1/2" if abs(a-0.5)<1e-12 else ""
        print(f"   k={k}  m={m:<9} alpha_*={a:.12f}{f}")
print("  per-factor form: both factors = q  => m=q^2 => a = log k /(2 log(1/q)); a=1/2 <=> q=1/k")
print("  the '2' is the ARITY of ab (two factors) = arithmetic, not inserted\n")

print("="*76); print("ABD-0 / PART 5 : asymmetric canonical 2-child refinement (split larger part)"); print("="*76)
def a_split(a,b,c):
    m1=m_scale(1,c-1,c); m2=m_scale(a-1,b+1,c)
    return bisect(lambda al: m1**al+m2**al-1.0), m1, m2
print("     c      a      b         m1            m2         alpha_*")
for c in (20,60,120,400,1000):
    for a in (c//2, c//3, c//10, c//50):
        if a<2: continue
        b=c-a; r,m1,m2=a_split(a,b,c)
        print(f"  {c:>5} {a:>6} {b:>6}  {m1:>12.7f}  {m2:>12.7f}   {r:>10.7f}")
print("  => asymmetric instances: alpha_* < 1/2 STRICTLY, -> 1/2 as a/b -> 1")
print("     so 1/2 = SUPREMUM of achievable exponents, attained only at exact balance a=b\n")

print("="*76); print("ABD-0 / PART 6 : cross-scale stability of the neutral point"); print("="*76)
print("  aggregate pressure T_X(alpha) = mean_{c<=X} rho_full(c,alpha), root of T_X=1")
cs=list(range(2,401))
def T_X(al): return sum(rho_full(c,al) for c in cs)/len(cs)
for X in (10,50,100,200,400):
    sub=cs[:X-1] if X<=400 else cs
    def TX(al,sub=sub): return sum(rho_full(c,al) for c in sub)/len(sub)
    r=bisect(lambda al: TX(al)-1.0)
    print(f"   X={X:>4}   T_X(0)={TX(0.0):>10.2f}   alpha_*(X)={r:.9f}")
big=[10**3,10**4,10**5,10**6]
def T_inf(X,al): return (sum(range(2,X+1))/(X-1))*C(al)   # mean(c) ~ X/2
for X in big:
    r=bisect(lambda al: T_inf(X,al)-1.0)
    print(f"   X={X:>8} (closed form)  alpha_*(X)={r:.9f}")
print("  => neutral point DIVERGES UPWARD with scale: no scale-stable root exists;")
print("     the choice-free refinement FAILS the cross-scale stability requirement\n")

print("="*76); print("ABD-0 / PART 7 : the balance-defect functional B_X(alpha)"); print("="*76)
Tri=[(a,c-a,c) for c in range(3,301) for a in range(1,c)]
def B(al):
    s=0.0
    for a,b,c in Tri:
        m=m_scale(a,b,c); s+=m**al-m**(1.0-al)
    return s
for al in (0.2,0.35,0.5,0.65,0.8):
    l,r=B(al),B(1.0-al)
    print(f"   alpha={al:<5} B={l:>18.10f}  B(1-a)={r:>18.10f}  sum={l+r:>9.2e}")
print("  => B(a) = -B(1-a) exactly by construction; B(1/2)=0 trivially.")
print("     This antisymmetry is IMPORTED, not generated => N3 danger (as anticipated)\n")

print("="*76); print("ABD-0 VERDICT"); print("="*76)
print("""  (i)   rho(a)=1 has an internally generated root -- but AUTOMATIC for >=2 children
        (rho decreasing, rho(0+)=k, rho(inf)=0).  Existence is not the discriminating test.
  (ii)  the unique CHOICE-FREE refinement (all splits) => alpha_*(c) DIVERGES ~ (1/2)log2(c):
        no stable neutral constant, not 1/2.  (branch # ~ c, all child scales <= 1/4)
  (iii) alpha_* = 1/2 <=> uniform k-child with m = 1/k^2 (both factors 1/k); exponent = 1/arity,
        arity = 2 for the product ab.
  (iv)  asymmetric canonical refinements: alpha_* < 1/2 strictly, -> 1/2 as a/b -> 1
        => 1/2 is the SUPREMUM, pinned from above by AM-GM (ab <= c^2/4), NOT inserted.
  (v)   BUT the extremal locus a=b destroys the additive asymmetry => attained by symmetrisation
        => C_NI (non-insertability) at risk: the 1/2 arrives with the symmetry, not from dynamics.
  (vi)  the antisymmetry B(a)=-B(1-a) is trivially imported; not the mechanism.
""")
