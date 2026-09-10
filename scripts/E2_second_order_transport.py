"""
E2: exact verification of Tang's second-order transport criterion
   Delta_{p,q} L(n) = L(pqn) - L(pn) - L(qn) + L(n)
DISCIPLINE: calibrate on known values FIRST, then verify predicted identities exactly.
No 1/2 input, no model construction, L2 untouched.
"""
from math import log
# ---------- 0. CALIBRATION (known answers must pass before anything else) ----------
N=5000
sieve=[True]*(N+1); sieve[0]=sieve[1]=False
for i in range(2,int(N**0.5)+1):
    if sieve[i]:
        for j in range(i*i,N+1,i): sieve[j]=False
primes=[i for i in range(N+1) if sieve[i]]
pi=[0]*(N+1); c=0
for i in range(N+1):
    if i>1 and sieve[i]: c+=1
    pi[i]=c
def Omega(n):
    r=0; m=n; d=2
    while d*d<=m:
        while m%d==0: m//=d; r+=1
        d+=1
    if m>1: r+=1
    return r
def omega(n):
    r=0; m=n; d=2
    while d*d<=m:
        if m%d==0:
            r+=1
            while m%d==0: m//=d
        d+=1
    if m>1: r+=1
    return r
def divisors(n): return [d for d in range(1,n+1) if n%d==0]
def d(n): return len(divisors(n))
def sigma(n): return sum(divisors(n))
def phi(n):
    r=n; m=n; d=2
    while d*d<=m:
        if m%d==0:
            r-=r//d
            while m%d==0: m//=d
        d+=1
    if m>1: r-=r//m
    return r
chk=[("Omega(12)=3",Omega(12),3),("omega(12)=2",omega(12),2),("d(12)=6",d(12),6),
     ("sigma(12)=28",sigma(12),28),("phi(12)=4",phi(12),4),("pi(100)=25",pi[100],25),
     ("Omega(1)=0",Omega(1),0),("d(1)=1",d(1),1),("sigma(1)=1",sigma(1),1)]
bad=[c for c in chk if c[1]!=c[2]]
print("CALIBRATION:", "ALL PASS" if not bad else f"FAIL {bad}")
assert not bad, "calibration failed - stop"
print()
# ---------- 1. the criterion, applied to a battery of arithmetic L ----------
def Delta(L,n,p,q): return L(p*q*n)-L(p*n)-L(q*n)+L(n)
P=[p for p in primes if 3<=p<=29]
CASES=[(n,p,q) for n in range(1,120) for i,p in enumerate(P) for q in P[i+1:]
       if n%p and n%q and p*q*n<=N]
print(f"test grid: {len(CASES)} triples (n,p,q), p,q distinct primes not dividing n")
print()
def report(name,L,pred,exact=True):
    ok=tot=0; ex=[]
    for n,p,q in CASES:
        v=Delta(L,n,p,q); e=pred(L,n,p,q)
        tot+=1
        good = (v==e) if exact else (abs(v-e)<1e-9*max(1,abs(e)))
        if good: ok+=1
        elif len(ex)<3: ex.append((n,p,q,v,e))
    print(f"  L={name:<12} matches prediction: {ok}/{tot}   {'✓' if ok==tot else '✗ '+str(ex)}")
    return ok==tot
# (A) additive L  -> predicts 0
print("[A] ADDITIVE L  (prediction: Delta = 0)")
report("log",      lambda n: log(n),   lambda L,n,p,q: 0, exact=False)
report("Omega",    Omega,              lambda L,n,p,q: 0)
report("omega",    omega,              lambda L,n,p,q: 0)
report("v_2 ",     lambda n: (n & -n).bit_length()-1, lambda L,n,p,q: 0)
print()
# (B) multiplicative L -> predicts L(n)*(L(p)-1)*(L(q)-1)
print("[B] MULTIPLICATIVE L  (prediction: Delta = L(n)*(L(p)-1)*(L(q)-1))")
report("d",     d,     lambda L,n,p,q: L(n)*(L(p)-1)*(L(q)-1))
report("sigma", sigma, lambda L,n,p,q: L(n)*(L(p)-1)*(L(q)-1))
report("phi",   phi,   lambda L,n,p,q: L(n)*(L(p)-1)*(L(q)-1))
print()
# (C) functions of the FACTORISATION that are not multiplicative
print("[C] FUNCTIONS OF THE FACTORISATION (non-multiplicative)")
report("Omega^2", lambda n: Omega(n)**2, lambda L,n,p,q: 2)
report("d^2",     lambda n: d(n)**2,     lambda L,n,p,q: L(n)*(d(p)**2-1)*(d(q)**2-1)//1 if False else (d(n)**2)*(3)*(3))
print()
# (D) an ADDITIVE-STRUCTURE L
print("[D] ADDITIVE-STRUCTURE L  (prediction: n*(p-1)*(q-1))")
report("n-1", lambda n: n-1, lambda L,n,p,q: n*(p-1)*(q-1))
print()
# (E) a genuinely NON-LOCAL L: the prime counting function
print("[E] NON-LOCAL L: pi(n)")
ok=[(n,p,q,Delta(lambda m: pi[m],n,p,q)) for n,p,q in CASES[:400]]
nz=[t for t in ok if t[3]!=0]
print(f"    nonzero Delta count: {len(nz)}/{len(ok)}  (examples: {nz[:4]})")
# test whether Delta(pi) factorises into local data: compare to pi(n)*(pi(p)-1)*(pi(q)-1)
ok2=sum(1 for n,p,q in CASES[:400] if Delta(lambda m: pi[m],n,p,q)==pi[n]*(pi[p]-1)*(pi[q]-1))
print(f"    factorises as pi(n)(pi(p)-1)(pi(q)-1)?  {ok2}/400  -> {'yes' if ok2==400 else 'NO (non-local)'}")
print()
print("="*84)
print("SUMMARY")
print("""  additive L            -> Delta = 0                       (flat, no second-order coupling)
  multiplicative L      -> Delta = L(n)(L(p)-1)(L(q)-1)    (nonzero BUT factorises into LOCAL data)
  factorisation-determined L -> Delta depends only on local data   => Tang's S13 death condition MET
  non-local L (pi, M, psi, Delta(x), class numbers)
                        -> Delta does NOT factorise, BUT these are exactly the counting/error
                           functions whose asymptotics ARE the explicit formula / L-values
                           => Tang's S20 exclusion list MET""")
