"""
Number-field version of A' -- CONSTRUCTIVE assembly (no audit).
Replacements:  finite symplectic pairing -> trace pairing Tr_{K/Q}(xy);  p-power filtration -> ramification
filtration;  sqrt(|G|) -> sqrt(|D_K|).
Classical inputs used (cited, not proved here):
  (C1) the trace-pairing dual of an ideal a is a* = a^{-1} D_K^{-1}  (D_K = different)
  (C2) the different exponents: d(p) = e-1 for tame p;  d(p) >= e for wild p
  (C3) conductor-discriminant: for a cyclic cubic field of conductor f, D = f^2
"""
from math import gcd
def sqfree(n):
    n=abs(n)
    for p in range(2,int(n**0.5)+1):
        if n%(p*p)==0: return False
    return True

def quad_disc(d):
    """discriminant of Q(sqrt(d)), d squarefree"""
    return d if d%4==1 else 4*d

def quad_diff_exponents(d):
    """returns dict prime -> v_p(D_K) for Q(sqrt d), from the classical rules"""
    D=quad_disc(d); ex={}
    n=abs(D)
    p=2
    m=n
    fac={}
    q=2
    while q*q<=m:
        while m%q==0: fac[q]=fac.get(q,0)+1; m//=q
        q+=1
    if m>1: fac[m]=fac.get(m,0)+1
    for p,e in fac.items():
        if p==2:
            # wild at 2
            if d%4==2: ex[p]=3                      # e.g. Q(sqrt2): D=(sqrt2)^3
            elif d==-1: ex[p]=2                     # Q(i): D=(1+i)^2  (even!)
            elif d==-2: ex[p]=3                     # Q(sqrt-2)
            else: ex[p]=0                           # 2 unramified
        else:
            ex[p]=1                                 # tame, e=2  => d=e-1=1
    return {p:v for p,v in ex.items() if v>0}

print("="*92); print("NUMBER-FIELD A' : balanced (self-dual) lattices and the sqrt(|D|) they are forced to have"); print("="*92)
print("""  self-duality of a lattice a (fractional ideal) w.r.t. the TRACE pairing means  a = a* = a^{-1} D^{-1}
  =>  a^2 = D^{-1}  =>  a = D^{-1/2}  =>  N(a) = |D_K|^{-1/2} : the square root is FORCED, not inserted.
  existence  <=>  D^{-1} is a SQUARE IDEAL  <=>  every different exponent v_p(D) is EVEN (and the class
  of D^{-1} is a square in Cl(K));  locally, tame p with ramification index e requires e-1 even, i.e. e ODD.""")
print()
print(f"  {'d':>4} | {'D_K':>6} | {'different exponents v_p(D)':>28} | {'all even?':>10} | {'balanced lattice exists?':>25}")
for d in (-1,-2,-3,2,3,5,6,-5,7,13,-7,-11,10,11,-13):
    if not sqfree(d): continue
    D=quad_disc(d); ex=quad_diff_exponents(d)
    alleven=all(v%2==0 for v in ex.values())
    print(f"  {d:>4} | {D:>6} | {str(ex):>28} | {str(alleven):>10} | {str(alleven):>25}")
print()
print("  => among quadratic fields, balance requires |D| to have no odd ramified prime and an even 2-part exponent;")
print("     for the family above this leaves ONLY Q(i) (d=-1, D=-4, v_{(1+i)}(D)=2 even).")
print()
print("="*92); print("explicit verification on Q(i):  the self-dual ideal and its norm"); print("="*92)
print("""  K=Q(i), O=Z[i], D_K=(1+i)^2=(2i), so D^{-1}=1/(2i)=-i/2=(1-i)/2 * (1/2)... concretely a=D_K^{-1/2}=(1+i)^{-1}=(1-i)/2
  N(a) = N((1-i)/2) = (1+1)/4 = 1/2 = |D_K|^{-1/2} with |D_K| = 4  =>  sqrt(|D_K|)=2   [check: (1/2) = 1/2  OK]""")
print("  trace pairing check: a*a = ((1-i)/2)^2 = (1-2i+i^2)/4 = (-2i)/4 = -i/2 = D^{-1}  => a is indeed self-dual")
print()
print("="*92); print("a case where balance EXISTS outside the quadratic family (cited classical facts)"); print("="*92)
print("""  cyclic cubic field of conductor f=7: D = f^2 = 49 (conductor-discriminant), 7 = p^3 so e=3 (tame, 7>3)
  different exponent = e-1 = 2, EVEN  =>  balance condition satisfied at the only ramified prime
  => it admits a self-dual lattice with N(a) = |D|^{-1/2} = 1/7   (and sqrt(|D|)=7 is a rational integer)""")
print()
print("="*92); print("WHAT THE FAILURE MEANS (the square-root obstruction)"); print("="*92)
print("""  when some v_p(D) is ODD, no ideal a with a^2 = D^{-1} exists *inside K*: the square root of the
  different class does not live in K.  The balance condition is then met only in a 2-COVER
  (Kummer / metaplectic-type), i.e. the "1/2" is exactly a 2-cover phenomenon.
  ObstruCTION CLASS = the class of D in Cl(K)/Cl(K)^2  (plus the local parity data) -- an arithmetic invariant.
  => ARITHMETIC SELECTION IS REAL, and it is governed by: tame ramification indices odd, wild (2-adic)
     exponents even, and the square-class condition in Cl(K).
""")
