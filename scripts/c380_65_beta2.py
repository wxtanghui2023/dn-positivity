# c380_65_beta2.py -- B1-beta-2: quantitative first-order odd->even bridge constant
import numpy as np
from scipy.optimize import root, linprog
import mpmath as mp
mp.mp.dps = 40
SIG=np.array([-1.,1.,1.,-1.,1.])
AEV=[3,4,7,9]; KODD=[13,19]; SK=[-1.0,1.0]
PHI0=np.array([0.14721317,0.23048868,0.18365067,0.2094225,0.11795883])*np.pi
O=lambda p,k: float(np.sum(SIG*np.cos(k*p))); E=lambda p,q: float(np.sum(np.cos(4*q*p)))
gO=lambda p,k: -k*SIG*np.sin(k*p);           gE=lambda p,q: -4*q*np.sin(4*q*p)
res=lambda p: np.concatenate([[E(p,q)-0.5 for q in AEV],[abs(O(p,13))-abs(O(p,19))]])
phi=root(res,PHI0,method='lm',options={'xtol':1e-15,'ftol':1e-15}).x
print("point residual %.1e ; x=%s"%(np.abs(res(phi)).max(),np.round(np.cos(phi)**2,8)),flush=True)

v13=SK[0]*gO(phi,13); v19=SK[1]*gO(phi,19)            # rows: a13(h)=v13.h etc
W=np.array([gE(phi,q) for q in AEV])                  # rows: b_q(h)=w_q.h  (F_6,F_8,F_14,F_18)
print("a13 row=%s\na19 row=%s"%(np.round(v13,6),np.round(v19,6)),flush=True)

# ---- primal LP: min c s.t. a13 <= -1, a19 <= -1, b_q <= c   (h,c free)
A_ub=np.vstack([np.hstack([-v13,[0.0]]), np.hstack([-v19,[0.0]]), np.hstack([W,-np.ones((4,1))])])
b_ub=np.array([1.0,1.0,0,0,0,0]); cobj=np.array([0,0,0,0,0,1.0])
p=linprog(cobj,A_ub=A_ub,b_ub=b_ub,bounds=[(None,None)]*6,method='highs')
print("\n=== beta-2b primal LP ===",flush=True)
print("   success=%s status=%d ; c_full = %.12f"%(p.success,p.status,p.x[5]),flush=True)
print("   primal h = %s"%np.round(p.x[:5],6),flush=True)
print("   constraint residuals (<=0): %s"%np.round(A_ub@p.x-b_ub,10),flush=True)
mu=p.ineqlin.marginals
print("   LP duals y = %s (dual feasibility y>=0 ? %s)"%(np.round(mu,8),bool((mu>=-1e-12).all())),flush=True)
print("   dual objective (nu13+nu19) = %.12f ; primal-dual gap = %.3e"%(mu[0]+mu[1],abs(mu[0]+mu[1]-p.x[5])),flush=True)
print("   dual check: sum(mu_q)=%.12f (should be 1) ; balance || -v13*y0 -v19*y1 + sum mu_q w_q || = %.3e"
      %(mu[2:].sum(), np.linalg.norm(-mu[0]*v13-mu[1]*v19+mu[2:]@W)),flush=True)

print("\n=== beta-2c comparison with the original KKT multipliers (only now) ===",flush=True)
lam=np.array([0.83791706,0.98971406,0.04185319,0.12728511]); om=np.array([0.903717944,0.096282056])
print("   KKT: lambda(4)=%s ; omega=(%.9f,%.9f)"%(np.round(lam,8),om[0],om[1]),flush=True)
print("   LP dual (overline-normalised): mu/sum_mu = %s ; nu/nu_sum = %s"%(np.round(mu[2:]/mu[2:].sum(),6),np.round(mu[:2]/max(mu[0]+mu[1],1e-30),6)),flush=True)
print("   KKT normalised: lambda/sum_lambda = %s ; omega = %s"%(np.round(lam/lam.sum(),6),np.round(om,6)),flush=True)
print("   ratio mu_q/lambda_q = %s"%(np.round(np.where(lam>0,mu[2:]/np.maximum(lam,1e-30),np.nan),6)),flush=True)

print("\n=== beta-2d odd-only control ===",flush=True)
h_ctrl=np.array([-1.,-1.,-1.,1.,1.])
print("   pure odd-descent direction h_ctrl=%s : a13=%+.4f a19=%+.4f ; b_q=%s ; max_q b_q=%+.4f"
      %(h_ctrl, v13@h_ctrl, v19@h_ctrl, np.round(W@h_ctrl,4), (W@h_ctrl).max()),flush=True)
pc=linprog(np.array([0,0,0,0,0,1.0]),A_ub=np.vstack([np.hstack([-v13,[0.0]]),np.hstack([-v19,[0.0]])]),
           b_ub=np.array([1.0,1.0]),bounds=[(None,None)]*6,method='highs')
print("   control LP (no b rows): status=%d -> c unbounded below (as expected, no even constraints)"%pc.status,flush=True)
print("   => control cost constant c_control = 0 (odd descent is free; no even constraint can be violated)",flush=True)

print("\n=== high-precision (40 dps) certification of the primal/dual certificates ===",flush=True)
mph=[mp.mpf(float(t)) for t in p.x[:5]]; y=[mp.mpf(float(t)) for t in mu]
def mpvec(g): return [mp.mpf(float(t)) for t in g]
mv13, mv19 = mpvec(v13), mpvec(v19); mW=[mpvec(w) for w in W]
b1=mp.fsum([mv13[j]*mph[j] for j in range(5)]); b2=mp.fsum([mv19[j]*mph[j] for j in range(5)])
bs=[mp.fsum([mW[q][j]*mph[j] for j in range(5)]) for q in range(4)]
print("   primal: a13=%s a19=%s (both <= -1 ? %s, accuracy %s)"%(mp.nstr(b1,10),mp.nstr(b2,10),b1<=-1 and b2<=-1,mp.nstr(max(b1+1,b2+1),5)),flush=True)
print("   primal: max_q b_q - c = %s (<=0 ?)"%(mp.nstr(max(bs)-mp.mpf(float(p.x[5])),8)),flush=True)
bal=[mp.fsum([y[0]*mv13[j], y[1]*mv19[j]]+[-y[2+q]*mW[q][j] for q in range(4)]) for j in range(5)]
print("   dual balance max|.| = %s ; sum mu = %s"%(mp.nstr(max(abs(t) for t in bal),8), mp.nstr(mp.fsum(y[2:]),8)),flush=True)
print("DONE",flush=True)
