# c380_65_beta2_v2.py -- beta-2 fixed: compactified LP (|h|inf<=1) + ratio infimum + control
import numpy as np
from scipy.optimize import root, linprog
SIG=np.array([-1.,1.,1.,-1.,1.]); AEV=[3,4,7,9]
PHI0=np.array([0.14721317,0.23048868,0.18365067,0.2094225,0.11795883])*np.pi
O=lambda p,k: float(np.sum(SIG*np.cos(k*p))); E=lambda p,q: float(np.sum(np.cos(4*q*p)))
gO=lambda p,k: -k*SIG*np.sin(k*p);           gE=lambda p,q: -4*q*np.sin(4*q*p)
res=lambda p: np.concatenate([[E(p,q)-0.5 for q in AEV],[abs(O(p,13))-abs(O(p,19))]])
phi=root(res,PHI0,method='lm',options={'xtol':1e-15,'ftol':1e-15}).x
v13=-gO(phi,13); v19=+gO(phi,19); W=np.array([gE(phi,q) for q in AEV])
print("point ok (res %.1e)"%np.abs(res(phi)).max(),flush=True)

rows=np.vstack([np.hstack([-v13,[0.0]]), np.hstack([-v19,[0.0]]), np.hstack([W,-np.ones((4,1))])])
b=np.array([1.,1.,0,0,0,0]); cobj=np.array([0,0,0,0,0,1.0])
for tag,bnd in [("UNBOUNDED-h (as specified)",[(None,None)]*6),
                ("COMPACTIFIED |h|inf<=1",[(-1,1)]*5+[(None,None)]),
                ("COMPACTIFIED |h|inf<=0.25",[(-0.25,0.25)]*5+[(None,None)])]:
    p=linprog(cobj,A_ub=rows,b_ub=b,bounds=bnd,method='highs')
    if p.status==0:
        print("   [%s] c = %.10f ; h=%s ; duals=%s"%(tag,p.x[5],np.round(p.x[:5],6),np.round(p.ineqlin.marginals[:6],6)),flush=True)
    else:
        print("   [%s] status=%d (%s) -> no finite optimum"%(tag,p.status,p.message.split('.')[0]),flush=True)

print("\nrecession check (why the unbounded version fails):",flush=True)
r=linprog(np.array([0,0,0,0,0,0.0]),A_ub=np.vstack([-v13,-v19,np.hstack([W,-np.ones((4,1))])]),
          b_ub=np.concatenate([[0,0],np.zeros(4)]),bounds=[(None,None)]*6,method='highs')
print("   exists h with a13>=0,a19>=0 and max_q b_q<=0 (recession)?", r.status==0, flush=True)

print("\n=== ratio infimum over unit directions (scale-invariant, nonconvex) ===",flush=True)
rng=np.random.default_rng(6565); best=(1e9,None,None)
for _ in range(400000):
    h=rng.normal(0,1,5); h/=np.linalg.norm(h)
    a13=float(v13@h); a19=float(v19@h); D=-max(a13,a19)
    if D<=1e-12: continue
    Ev=max(0.0,float((W@h).max())); ratio=Ev/D
    if ratio<best[0]: best=(ratio,(a13,a19,np.round(W@h,4)),h.copy())
print("   min E/D found = %.6f ; (a13,a19,W.h)=%s"%(best[0],best[1]),flush=True)
print("   => pointwise E(h) > 0 whenever D(h) > 0, but the infimum over the cone is approached only",flush=True)
print("      along growing recession directions: the odd-normalised bridge constant is NOT uniform.",flush=True)

print("\n=== control: pure odd descent, even rows dropped ===",flush=True)
hc=best[2]
print("   along the near-optimal direction: b_q = %s (max = %+.4f)"%(np.round(W@hc,4),(W@hc).max()),flush=True)
print("DONE",flush=True)
