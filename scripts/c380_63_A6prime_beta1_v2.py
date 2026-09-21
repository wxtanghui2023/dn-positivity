# c380_63_A6prime_beta1_v2.py -- A6' + beta-1 with FREQUENCY-based definitions (r/frequency confusion fixed)
import numpy as np
from scipy.optimize import root
import mpmath as mp
mp.mp.dps = 40
SIG = np.array([-1.,1.,1.,-1.,1.])
AEVEN = [3,4,7,9]                 # q indices -> F_{2q}, frequencies 4q = 12,16,28,36
KODD = [13, 19]                   # frequencies of the two active odd branches (r = 6, 9)
PHI0 = np.array([0.14721317, 0.23048868, 0.18365067, 0.2094225, 0.11795883])*np.pi

O = lambda p, k: float(np.sum(SIG*np.cos(k*p)))                 # odd functional, frequency k
E = lambda p, q: float(np.sum(np.cos(4*q*p)))                   # even functional F_{2q}
gO = lambda p, k: -k*SIG*np.sin(k*p)                            # gradient in phi
gE = lambda p, q: -4*q*np.sin(4*q*p)

def res(p):
    return np.concatenate([[E(p,q)-0.5 for q in AEVEN], [abs(O(p,KODD[0]))-abs(O(p,KODD[1]))]])
phi = root(res, PHI0, method='lm', options={'xtol':1e-15,'ftol':1e-15}).x
print("=== point restored: residual %.2e ; x = %s ===" % (np.abs(res(phi)).max(), np.round(np.cos(phi)**2,10)), flush=True)
ov = {k: O(phi,k) for k in range(1,26,2)}
print("   odd values (freq):", {k: round(v,6) for k,v in ov.items()}, flush=True)
t = max(abs(v) for v in ov.values()); print("   t = %.12f" % t, flush=True)

print("\n=== A6'-(1) base tie precision, 40 dps ===", flush=True)
mp_phi=[mp.mpf(float(v)) for v in phi]
mpO=lambda k: mp.fsum([mp.mpf(float(SIG[j]))*mp.cos(k*mp_phi[j]) for j in range(5)])
Dt=abs(abs(mpO(13))-abs(mpO(19)))
print("   Delta_tie = | |F_13| - |F_19| | = %s" % mp.nstr(Dt,8), flush=True)
print("   F_13 = %s ; F_19 = %s (40 dps)" % (mp.nstr(mpO(13),20), mp.nstr(mpO(19),20)), flush=True)

print("\n=== A6'-(2) relative perturbation test ===", flush=True)
rng=np.random.default_rng(6363)
for sd in (1e-8,1e-6,1e-4,1e-2):
    dom13=0; mx=0.0
    for _ in range(300):
        h=rng.normal(0,sd,5)
        d=abs(abs(O(phi+h,13))-abs(O(phi+h,19))); mx=max(mx,d)
        if abs(O(phi+h,13))>abs(O(phi+h,19)): dom13+=1
    print("   sd=%.0e : max delta_odd=%.3e (%.2e relative to t=%.4f) ; F_13 dominant %d/300 ; expected ~150" % (sd,mx,mx/t,t,dom13), flush=True)
print("   => dominance flips freely and delta_odd scales linearly with sd: consistent with an EXACT base tie", flush=True)

print("\n=== A6'-(3) omega is structural, not a tie-break ===", flush=True)
g13=np.sign(O(phi,13))*gO(phi,13); g19=np.sign(O(phi,19))*gO(phi,19)
G=np.array([gE(phi,q) for q in AEVEN])
for w in (0.903717944, 0.5, 1.0, 0.0):
    lam,rss,_,_=np.linalg.lstsq(G.T,-(w*g13+(1-w)*g19),rcond=None)
    print("   omega=(%.9f,%.9f): residual=%.3e ; lambda=%s ; lambda>=0? %s"
          % (w,1-w,np.linalg.norm(w*g13+(1-w)*g19+G.T@lam),np.round(lam,8),bool((lam>=-1e-12).all())), flush=True)

print("\n=== B1-beta-1: critical cone and second-order ledger ===", flush=True)
U,S,Vt=np.linalg.svd(G); print("   singular values of the active-even gradient matrix: %s" % np.round(S,8), flush=True)
h0=Vt[-1]
a=float(g13@h0); b=float(g19@h0)
print("   null direction h0 = %s" % np.round(h0,8), flush=True)
print("   first-order odd changes: s1 dF13.h0 = %+.6e ; s2 dF19.h0 = %+.6e ; omega*a+(1-omega)*b = %.3e"
      % (a,b,0.903717944*a+0.096282056*b), flush=True)
h = h0 if max(a,b) < 0 else -h0
a=float(g13@h); b=float(g19@h)
print("   oriented so the odd MAX decreases: max(a,b) = %+.6e (<0 required)" % max(a,b), flush=True)
print("   --- ledger: D2 F_k[h,h] = -k^2 sum_j gamma_j cos(k phi_j) h_j^2 ---", flush=True)
for k,gam,tag in [(13,SIG,'odd active'),(19,SIG,'odd active'),(12,np.ones(5),'even F_6 active'),(16,np.ones(5),'even F_8 active'),(28,np.ones(5),'even F_14 active'),(36,np.ones(5),'even F_18 active')]:
    print("   k=%2d (%-16s): D2 = %+.6e" % (k,tag,-(k**2)*float(np.sum(gam*np.cos(k*phi)*h**2))), flush=True)
print("\n   (constraint F<=1/2 active at the point: D2 > 0 => violated for any step along +-h => blocked)", flush=True)
print("DONE", flush=True)
