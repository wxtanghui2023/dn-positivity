# c380_75_C3874B_audit.py -- C3874-B: (i) even-blind counterexample, (ii) point-independence audit
import numpy as np
from scipy.optimize import minimize
np.random.seed(7575)
SIG=np.array([-1.,1.,1.,-1.,1.]); KODD=np.arange(1,24,2); c0=0.86885034832244940011
AEV=[3,4,7,9]; QALL=list(range(1,13))
def ph(c): return np.arccos(np.clip(c,0,1))
def Fk(c,k,gam=SIG): return float(np.sum(gam*np.cos(k*ph(c))))
def Fe(c,q): return float(np.sum(np.cos(4*q*ph(c))))
def M(c): 
    v=[abs(Fk(c,k)) for k in KODD]; return max(v)
def smoothM(c,p=25.0):
    v=np.array([Fk(c,k) for k in KODD]); return float(np.log(np.sum(np.exp(p*np.abs(v))))/p)
def pen_all(c):
    e=max(Fe(c,q)-0.5 for q in QALL); return smoothM(c)+200.0*max(0.0,e)+10*np.sum(np.clip(c-1,0,None))+10*np.sum(np.clip(-c,0,None))

print("=== (i) EVEN-BLIND test: is there a point with M(x) < c0 when even constraints are DROPPED? ===")
best=(9,None)
for t in range(60):
    c0v=np.random.uniform(0.05,0.95,5)
    r=minimize(smoothM,c0v,method='Nelder-Mead',options={'maxiter':600,'xatol':1e-9,'fatol':1e-11})
    m=M(r.x)
    if m<best[0]: best=(m,r.x.copy())
print("   unconstrained min of M found = %.9f  (c0 = %.9f)"%(best[0],c0))
print("   => M < c0 WITHOUT even constraints: %s"%(best[0]<c0-1e-6))
print("   dropped-constraint point c = %s"%np.round(best[1],6))
print("   its even values F_2..F_24 - 1/2: max = %+.6f (i.e. VIOLATES some even constraint)"%max(Fe(best[1],q)-0.5 for q in QALL))

print("\n=== (ii) with ALL 12 even constraints enforced (correct feasible set) ===")
feas=[]
for t in range(120):
    c0v=np.random.uniform(0.05,0.95,5)
    r=minimize(pen_all,c0v,method='Nelder-Mead',options={'maxiter':700,'xatol':1e-9,'fatol':1e-11})
    if max(Fe(r.x,q)-0.5 for q in QALL)<=1e-7: feas.append((M(r.x),r.x.copy()))
feas.sort(key=lambda t:t[0])
print("   truly feasible descents: %d"%len(feas))
if feas:
    print("   best feasible M = %.9f (known candidate %.9f)"%(feas[0][0],c0))
    print("   values < 1.5 : %s"%sorted(set(round(v,6) for v,_ in feas if v<1.5))[:10])
print("\n=== (iii) B1 linear-functional ceiling (archive, C-3813/C-3814) ===")
print("   positive trig-dual route closed sharp: sum_k a_k <= 6 c0 (see C-3814) => linear functional cannot reach c0")
print("DONE")
