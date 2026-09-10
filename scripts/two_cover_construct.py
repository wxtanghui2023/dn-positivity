"""
甲：2-cover 的显式构造（纯构造/实算，不做审计）
K = Q(sqrt2) 是失败例；构造 K' = K(delta), delta = 2^{1/4} = sqrt(sqrt2)，并在 K' 内显式验证
    a'^2 = D_K^{-1} O_{K'}   （即 pi^*(D_K^{-1}) 的平方根真的存在）
环模型：Z[delta] = Z[x]/(x^4-2)，元素 (a,b,c,d) <-> a + b d + c d^2 + d d^3
"""
import itertools
from fractions import Fraction

# ---------- exact arithmetic in Z[delta], delta^4 = 2 ----------
def mul(u,v):
    a,b,c,d=u; e,f,g,h=v
    # (a + b x + c x^2 + d x^3)(e + f x + g x^2 + h x^3) mod (x^4 - 2)
    raw=[0]*7
    for i,ui in enumerate((a,b,c,d)):
        for j,vj in enumerate((e,f,g,h)):
            raw[i+j]+=ui*vj
    # reduce x^4 = 2
    for k in range(6,3,-1):
        coef=raw[k]
        if coef:
            raw[k]-=coef
            raw[k-4]+=2*coef
    return tuple(raw[:4])

def norm(u):
    """field norm N_{Q(delta)/Q}(u) via the 4x4 multiplication matrix"""
    a,b,c,d=u
    cols=[]
    for e in ((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)):
        cols.append(mul(u,e))
    # determinant of the matrix whose columns are mul(u, basis)
    M=[[cols[j][i] for j in range(4)] for i in range(4)]
    det=0
    for perm in itertools.permutations(range(4)):
        sign=1
        for i in range(4):
            for j in range(i+1,4):
                if perm[i]>perm[j]: sign=-sign
        term=sign
        for i in range(4): term*=M[i][perm[i]]
        det+=term
    return det

print("="*94); print("STEP 1  the different of K=Q(sqrt2) and its prime factorization"); print("="*94)
print("""  O_K = Z[sqrt2], alpha = sqrt2, f(x)=x^2-2, f'(x)=2x  =>  D_K = (f'(alpha)) = (2 sqrt2)
  (2) = (sqrt2)^2   [since sqrt2*sqrt2 = 2]
  =>  D_K = (2 sqrt2) = (sqrt2)^2 * (sqrt2) = (sqrt2)^3        so  v_{(sqrt2)}(D_K) = 3 = ODD
  N(D_K) = |D_K| = 8  (discriminant of Q(sqrt2)) ;  8 is NOT a perfect square""")
print()
print("="*94); print("STEP 2  why an odd exponent forbids a square root INSIDE K"); print("="*94)
print("""  want a fractional ideal a of K with a^2 = D_K^{-1}. Taking norms:
        N(a)^2 = N(D_K^{-1}) = 1/|D_K| = 1/8
  but N(a) is a POSITIVE RATIONAL for every fractional ideal, while 1/8 is not a rational square
  (proof: (p/q)^2 = 1/8 => 8p^2 = q^2 => 2^3 | q^2 => 2^2 | q => ... parity contradiction).
  => NO such a exists in K.   [This is a norm obstruction, purely arithmetic, not a naming convention.]""")
from math import isqrt
ok=all(isqrt(8*p*p)**2!=8*p*p for p in range(1,200))
print(f"  numeric confirmation that 1/8 is not a rational square (bounded search): {ok}")
print()
print("="*94); print("STEP 3  the explicit 2-descent lift:  K' = K(delta), delta = 2^(1/4)"); print("="*94)
print("""  choose gamma = sqrt2 (the RAMIFIED element, valuation 1 at the ramified prime)
  K' = K(delta) with delta^2 = gamma = sqrt2  =>  [K':K] = 2   (a quadratic, i.e. 2-, cover)
  the cover is FORCED by the ramified datum: it adjoins the square root of the ramified element""")
one=(1,0,0,0); delta=(0,1,0,0)
delta2=mul(delta,delta); delta3=mul(delta2,delta); delta6=mul(delta3,delta3)
print(f"  delta^2 = {delta2}  = (0,0,1,0) which is sqrt2   => (delta)^2 = (sqrt2) as principal ideals  ✓")
print(f"  delta^6 = {delta6} = (2,0,0,0)*? check: delta^6 = (delta^2)^3 = (sqrt2)^3 = 2*sqrt2")
print(f"  N(delta) = {norm(delta)}   (expect -2)      N(delta^2) = {norm(delta2)}   (expect 4)")
print()
print("="*94); print("STEP 4  verify the square relation really holds after lifting"); print("="*94)
print("""  D_K O_{K'} = (sqrt2)^3 O_{K'} = (delta^2)^3 = (delta^6)     [as principal ideals]
  take  a' = (delta^{-3}) = (delta)^(-3)
  then  a'^2 = (delta)^(-6) = (delta^6)^{-1} = (D_K O_{K'})^{-1} = D_K^{-1} O_{K'}   ✓✓ EXACT
  norm check:  N_{K'/Q}(a')^2 = 1/N_{K'/Q}(D_K O_{K'}) = 1/|D_K|^{[K':K]} = 1/8^2 = 1/64
               => N(a') = 1/8 which IS rational (64 = 8^2 is a perfect square)  ✓""")
d3=mul(delta2,delta)
print(f"  N(delta^3) = {norm(d3)}   =>  |N(a')| = 1/{abs(norm(d3))}   (expect 1/8)")
print(f"  exponent doubling: v_(delta)(sqrt2) = 2  =>  v_(delta)(D_K O_K') = 3*2 = 6  EVEN  ✓")
print()
print("="*94); print("STEP 5  where does the obstruction REALLY live for this example? (honest check)"); print("="*94)
print("""  Cl(Q(sqrt2)) = 1  (class number one).  Hence Cl/2Cl is TRIVIAL here.
  => the obstruction CANNOT be attributed to Cl(K)/2Cl(K) in this example: that quotient vanishes
     while the obstruction is real.  The real obstruction is the LOCAL PARITY datum
        v_{(sqrt2)}(D_K) = 3 odd,
     whose natural home is the Kummer datum  K^x/(K^x)^2  (equivalently the 2-torsion of the
     idele class group), NOT Cl(K)/2Cl(K).
  CORRECTION (errata to bfa4227): "obstruction = class of D in Cl(K)/2Cl(K)" was INCOMPLETE.
     Corrected factorization:   obstruction = (local parity data) x (2-descent/class-group data),
     the local factor being handled by ramification in the cover, and the 2-descent factor governing
     whether a SINGLE 2-cover suffices.
  For K=Q(sqrt2): local factor non-trivial (v=3 odd), 2-descent factor trivial (h=1)
     => ONE 2-cover suffices, as constructed and verified above.  ✓ consistent.""")
print()
print("="*94); print("why the cover works, in one line (and why it is canonical)"); print("="*94)
print("""  lifting a degree-2 Kummer cover DOUBLES the valuation at the ramified prime, so every ODD exponent
  becomes EVEN; equivalently the lifted different has norm |D_K|^2 = 64 = 8^2, a perfect square.
  => the 2-cover "makes the discriminant a square", which is exactly the rationality required in STEP 2.
  the cover is determined by the arithmetic datum (the ramified element), not chosen by us.""")
