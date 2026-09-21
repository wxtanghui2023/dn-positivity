# c380_78_C3876_precheck.py -- C3876-A/B: MAP ONLY (no certificate). far-region geometry of {M < c0}
import numpy as np
np.random.seed(7878)
SIG=np.array([-1.,1.,1.,-1.,1.]); KODD=np.arange(1,24,2); QALL=list(range(1,13))
c0=0.86885034832244940011
def ph(c): return np.arccos(np.clip(c,0,1))
def M(c):
    v=[abs(float(np.sum(SIG*np.cos(k*ph(c))))) for k in KODD]; return max(v), int(KODD[int(np.argmax(v))])
def evenok(c,tol=1e-9): return max(float(np.sum(np.cos(4*q*ph(c)))) for q in QALL)<=0.5+tol

print("=== A: map of M over E_even (random feasible sampling) ===", flush=True)
vals=[]; n=0
while n<4000 and n<200000:
    c=np.random.uniform(0.02,0.999,5); n+=1
    if evenok(c): vals.append(M(c)[0])
vals=np.array(vals)
print("   feasible samples: %d (from %d draws)"%(len(vals),n), flush=True)
print("   min M = %.6f ; median = %.6f ; max = %.6f"%(vals.min(),np.median(vals),vals.max()), flush=True)
print("   count(M < c0) = %d ; count(M < 1.5) = %d ; count(M < 1.0) = %d"%((vals<c0).sum(),(vals<1.5).sum(),(vals<1.0).sum()), flush=True)
print("   => {M < c0} appears %s in this random map"%("EMPTY" if (vals<c0).sum()==0 else "NONEMPTY"), flush=True)

print("\n=== A2: the pairing locus (c1=c3, c2=c4) -- where even-blind M=0 lived ===", flush=True)
print("   on that locus F_k = sigma5*T_k(c5) -> M = max_k |T_k(c5)| :", flush=True)
best=(9,None)
for c5 in np.linspace(0.0,0.999,400):
    mv=max(abs(np.cos(k*np.arccos(c5))) for k in KODD)
    if mv<best[0]: best=(mv,c5)
print("   min over c5 of max_odd|T_k(c5)| = %.6f at c5 = %.4f  (>= c0 ? %s)"%(best[0],best[1],best[0]>=c0), flush=True)
print("   (at c5=0 we get M=0 -- the excluded zero-atom point of C-3849)", flush=True)

print("\n=== B: does M < c0 force x into the tiny local box rho_cert=1.18278e-4 ? ===", flush=True)
print("   local sharpness (C3875'): for |phi-phi*|_2 < 1.18278e-4 we have M >= c0 + eta r - K r^2 > c0", flush=True)
print("   => inside the box the claim is CLOSED; the map above shows no sub-c0 feasible point OUTSIDE either", flush=True)
print("   but the Taylor extension to arbitrary h fails: max_i[(Gh)_i + delta_i] - K|h|^2 < 0 once |h| >~ eta/K", flush=True)
print("   => no local->global transfer; a genuine global argument is still missing", flush=True)

print("\n=== C: point-independent Gordan certificate? ===", flush=True)
print("   Even-blind witness (M=0, zero-atom layer) has a non-trivial cone {G h <= 0}, hence NO y>0 with G^T y = 0 there.", flush=True)
print("   => 'exists point-independent y>0 for all x' is FALSE in general; the Gordan route cannot be globalised.", flush=True)
print("DONE", flush=True)
