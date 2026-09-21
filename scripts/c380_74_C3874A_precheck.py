# c380_74_C3874A_precheck.py -- C3874-A: go/no-go pre-check for a global interval certificate
import numpy as np, sympy as sp
from scipy.optimize import minimize
np.random.seed(7474)

print("=== Q1a: is the system semi-algebraic in c_j = cos(phi_j) ? ===", flush=True)
c,t = sp.symbols('c t')
for k in [6,8,13,14,18,19,23,12,16,28,36]:
    ident=sp.simplify(sp.chebyshevt(k,c)-sp.cos(k*sp.acos(c)))
    print("   T_%d(c) == cos(%d*phi)  : %s"%(k,k,ident==0), flush=True)
print("   => F_k = sum_j gamma_j T_k(c_j): POLYNOMIAL in c for BOTH odd and even    [Q1a: YES]", flush=True)
print("   => x = c^2 works for even (deg 4q even) but adds sqrt(x) for odd; c is the natural algebraic variable", flush=True)

print("\n=== Q1b: naive interval-subdivision scale estimate ===", flush=True)
for eps in [1e-2,1e-3,1e-4]:
    boxes=(37.0*36.0*eps)**-5   # derivative bound ~ k^2 ~ 36^2=1296, resolve to eps
    print("   box side %g -> need ~ %.1f boxes in 5 dims (1296*eps resolution) = %.2e"%(eps,(1296*eps)**-1,boxes), flush=True)
print("   => naive uniform subdivision is hopeless (curse of dimensionality).", flush=True)

print("\n=== Q2: how many distinct candidate regions? (multi-start local descent, sigma=(-1,1,1,-1,1)) ===", flush=True)
SIG=np.array([-1.,1.,1.,-1.,1.]); KODD=np.arange(1,24,2)           # 13 odd frequencies 1..23
AEV=[3,4,7,9]
def Fodd(c,k):  return float(np.sum(SIG*np.cos(k*np.arccos(np.clip(c,0,1)))))
def Feven(c,q): return float(np.sum(np.cos(4*q*np.arccos(np.clip(c,0,1)))))
def maxodd(c):
    v=[abs(Fodd(c,k)) for k in KODD]; return max(v), int(KODD[int(np.argmax(v))])
def pen(c):
    m,idx=maxodd(c); e=max(Feven(c,q)-0.5 for q in AEV)
    return m + 500.0*max(0.0,e)**1 + 5.0*np.sum(np.clip(c-1,0,None)**2)+5.0*np.sum(np.clip(-c,0,None)**2), idx
def smooth(c,p=12.0):
    m,idx=maxodd(c); e=max(Feven(c,q)-0.5 for q in AEV)
    v=np.array([abs(Fodd(c,k)) for k in KODD])
    sm=np.log(np.sum(np.exp(p*v)))/p
    return sm + 500.0*max(0.0,e) + 5.0*np.sum(np.clip(c-1,0,None)**2)+5.0*np.sum(np.clip(-c,0,None)**2)
found=[]
for trial in range(80):
    c0=np.random.uniform(0.05,0.95,5)
    r=minimize(lambda c: smooth(c), c0, method='Nelder-Mead',
               options={'maxiter':400,'xatol':1e-8,'fatol':1e-10})
    v,idx=maxodd(r.x)
    if max(Feven(r.x,q)-0.5 for q in AEV) <= 1e-6:      # feasible
        found.append((round(v,6),idx,np.round(r.x,5)))
found.sort()
vals=[f[0] for f in found]
crit=[v for v in vals if v<1.5]
print("   feasible descents: %d ; distinct values < 1.5 : %s"%(len(found), sorted(set(crit))[:12]), flush=True)
print("   best found = %.9f (known V_sigma candidate 0.868850348)"%min(vals) if vals else "   none", flush=True)
idxset={}
for v,i,x in found: idxset.setdefault(i,[]).append(v)
print("   active odd FREQUENCY at each local min (frequency -> count, best value):", flush=True)
for i in sorted(idxset): print("      k=%2d : %d hits, best %.6f"%(i,len(idxset[i]),min(idxset[i])), flush=True)
print("   => number of distinct active-odd branches observed: %d"%len(idxset), flush=True)
print("DONE", flush=True)
