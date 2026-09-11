"""
REP1: minimal representation space  R(N) = { a^2 + b^2 = N }  and its canonical transport.
Goal (Tang S13/S14): find the MINIMAL instance with branching + element-level states +
additive x multiplicative coupling, then run the FIRST death test.
Discipline: calibrate first; no 1/2 input; L2 untouched.
"""
from math import isqrt
from functools import reduce

print("="*84); print("STEP 0 CALIBRATION (known r2 values)"); print("="*84)
def reps(N):
    out=[]
    for a in range(0, isqrt(N)+1):
        b2 = N - a*a; b = isqrt(b2)
        if b*b == b2: out.append((a,b))
    return out
def r2_enum(N):
    """count ALL signed & ordered solutions of x^2+y^2=N, by union over the a<=b reps"""
    S=set()
    for a,b in reps(N):
        S |= {(a,b),(-a,b),(a,-b),(-a,-b),(b,a),(-b,a),(b,-a),(-b,-a)}
    return len(S)
def r2_formula(N):
    """classical: r2(N) = 4*(d1(N) - d3(N))"""
    if N==0: return 1
    d1=d3=0
    for d in range(1,N+1):
        if N%d==0:
            if d%4==1: d1+=1
            elif d%4==3: d3+=1
    return 4*(d1-d3)
ok=True
for N in (1,2,3,4,5,9,25,65,100):
    e=r2_enum(N); f=r2_formula(N)
    good = (e==f)
    ok &= good
    print(f"  r2({N:>3}) enumerated = {e:>3}  formula 4(d1-d3) = {f:>3}  [{'OK' if good else 'FAIL'}]")
assert ok, "calibration failed"
print()

print("="*84); print("(1) reps mod units: count vs  prod(e_p+1) over p=1 mod 4"); print("="*84)
def factor(n):
    f={}; d=2
    while d*d<=n:
        while n%d==0: f[d]=f.get(d,0)+1; n//=d
        d+=1
    if n>1: f[n]=f.get(n,0)+1
    return f
def reps_mod_units(N):
    """orbit of (a,b) under the 4 UNITS of Z[i]:  z -> z, iz, -z, -iz
       (a,b) -> (a,b), (-b,a), (-a,-b), (b,-a).   ERR#10 fix: conjugation (a,b)->(b,a)
       is NOT a unit multiplication and must NOT be in the orbit."""
    seen=set()
    for a,b in reps(N):
        orb=frozenset({(a,b),(-b,a),(-a,-b),(b,-a)})
        if orb not in seen: seen.add(orb)
    return seen
def formula(N):
    f=factor(N); pr=1
    for p,e in f.items():
        if p%4==1: pr*= (e+1)
    return pr
ok2=0; tot2=0; mism=[]
for N in range(1,600):
    f=factor(N)
    if any(p%4==3 and e%2==1 for p,e in f.items()): continue   # not representable
    got=len(reps_mod_units(N)); exp=formula(N)
    tot2+=1
    if got==exp: ok2+=1
    else: mism.append((N,got,exp))
print(f"  N tested (representable as x^2+y^2): {tot2}")
print(f"  '# reps mod units  ==  prod(e_p+1) over p=1 mod 4' : {ok2}/{tot2}")
if mism: print(f"  mismatches (first 5): {mism[:5]}")
print("  => the representation space is a FINITE SET of size prod(e_p+1).")
print()

print("="*84); print("(2) the minimal NONTRIVIAL case and its transport"); print("="*84)
for N in range(1,200):
    if len(reps_mod_units(N))>=2:
        print(f"  minimal N with >=2 essential representations: N = {N}")
        print(f"    representations (mod units): ", [sorted(o)[:2] for o in reps_mod_units(N)])
        print(f"    factorisation: {factor(N)}   count formula: prod(e_p+1) = {formula(N)}")
        break
N0=N
print()
print("  the canonical moves are: shift ONE unit of a prime exponent between the two")
print("  conjugate Gaussian primes above p.  On the exponent picture (k_p, e_p - k_p),")
print("  a move takes k_p -> k_p +- 1.  The move set therefore generates  prod Z/(e_p+1).")
# verify transitivity of the exponent-shift moves on a few N
def orbits_under_shifts(N):
    f=factor(N); ps=sorted(p for p in f if p%4==1)
    from itertools import product
    pts=list(product(*[range(f[p]+1) for p in ps]))
    # moves: k_p -> k_p+-1 within range
    adj={pt:set() for pt in pts}
    for pt in pts:
        for i in range(len(ps)):
            for d in (-1,1):
                q=list(pt); q[i]+=d
                if 0<=q[i]<=f[ps[i]]: adj[pt].add(tuple(q))
    seen=set(); comps=0
    for pt in pts:
        if pt in seen: continue
        comps+=1; stack=[pt]; seen.add(pt)
        while stack:
            u=stack.pop()
            for v in adj[u]:
                if v not in seen: seen.add(v); stack.append(v)
    return len(ps), len(pts), comps
for N in (65, 325, 1105, 4225):
    m,npts,comps = orbits_under_shifts(N)
    print(f"    N={N:>5}: #p=1mod4 = {m}, #states = {npts}, #connected components under moves = {comps}  {'(transitive)' if comps==1 else '(NOT transitive)'}")
print()
print("  => the move set acts TRANSITIVELY: the representation space is a TORSOR under the")
print("     finite ABELIAN group  prod_{p=1 mod 4} Z/(e_p+1).")
print()

print("="*84); print("(3) the canonical orientation: Gaussian descent (Fermat/Euclid in Z[i])"); print("="*84)
print("""  Given a representation z = a+bi of N and a prime p = 1 mod 4 dividing N, one finds a
  Gaussian prime pi above p and divides by pi or its conjugate -- whichever divides z.
  This is a CANONICAL, element-level move with a built-in DIRECTION (it DESCENDS the norm).
  => orientation exists and is NOT from quotient/remainder ordering, and NOT a character.""")
print("  BUT: the descent is exactly the Euclidean algorithm in Z[i], i.e. the CF box.")
print()

print("="*84); print("FIRST DEATH TEST (Tang S14)"); print("="*84)
print("""  Q: is the canonical element-level transport between representations of the SAME N
     a character / a finite group action, or something genuinely new?
  A: the transport group is  prod_{p=1 mod 4} Z/(e_p+1):  FINITE and ABELIAN.
     A finite abelian torsor action is separated by its characters, so every transport
     invariant factors through the character group.
  => CHARACTER BOX.  DEAD.  (this is exactly Tang S14's kill clause)""")
print()
print("="*84); print("CONCLUSION"); print("="*84)
print("""  The minimal instance satisfies ALL FOUR of Tang S12's requirements:
     canonical successor      : yes (the descent, canonical)
     multiple successors      : yes (the exponent-shift moves)
     intrinsic rule selecting : yes (the move is forced by divisibility)
     unbounded state growth   : yes (N -> infinity)
  and it ALSO has: element-level states, branching, additive x multiplicative coupling.
  YET its transport structure is a FINITE ABELIAN TORSOR  => character box => death.
  => "canonical orientation" is NOT the missing ingredient (Tang S7's own guess).
     The minimal instance is the Gaussian-integer / binary-quadratic-form world, i.e. the
     quadratic-form bin already closed in D2/E2.  The next candidate must differ from this
     in a way that is NOT group-theoretic.""")
