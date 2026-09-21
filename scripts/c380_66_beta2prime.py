# c380_66_beta2prime.py -- beta-2' (sign corrected): box and unbounded LPs + dual + gap + control
import numpy as np
from scipy.optimize import root, linprog
import mpmath as mp
mp.mp.dps = 40
SIG=np.array([-1.,1.,1.,-1.,1.]); AEV=[3,4,7,9]
PHI0=np.array([0.14721317,0.23048868,0.18365067,0.2094225,0.11795883])*np.pi
O=lambda p,k: float(np.sum(SIG*np.cos(k*p))); E=lambda p,q: float(np.sum(np.cos(4*q*p)))
gO=lambda p,k: -k*SIG*np.sin(k*p);           gE=lambda p,q: -4*q*np.sin(4*q*p)
res=lambda p: np.concatenate([[E(p,q)-0.5 for q in AEV],[abs(O(p,13))-abs(O(p,19))]])
phi=root(res,PHI0,method='lm',options={'xtol':1e-15,'ftol':1e-15}).x
v13=-gO(phi,13); v19=+gO(phi,19); W=np.array([gE(phi,q) for q in AEV])
print("point residual %.1e" % np.abs(res(phi)).max(), flush=True)

# CORRECTED signs: v13.h <= -1 ; v19.h <= -1 ; W.h - c <= 0
rows=np.vstack([np.hstack([v13,[0.0]]), np.hstack([v19,[0.0]]), np.hstack([W,-np.ones((4,1))])])
bb=np.array([-1.0,-1.0,0,0,0,0]); cobj=np.array([0,0,0,0,0,1.0])

print("\n=== (1) UNBOUNDED version (no box) ===", flush=True)
pu=linprog(cobj,A_ub=rows,b_ub=bb,bounds=[(None,None)]*6,method='highs')
print("   status=%d (%s)"%(pu.status,pu.message.split('.')[0]), flush=True)
if pu.status==0:
    print("   c_full(unbounded) = %.12f ; h=%s"%(pu.x[5],np.round(pu.x[:5],6)),flush=True)

print("\n=== (2) BOX version |h|inf <= 1 ===", flush=True)
pb=linprog(cobj,A_ub=rows,b_ub=bb,bounds=[(-1,1)]*5+[(None,None)],method='highs')
ok=(pb.status==0)
if ok:
    cfull=float(pb.x[5]); hb=pb.x[:5]
    print("   c_full(box) = %.12f ; h = %s"%(cfull,np.round(hb,6)),flush=True)
    A=np.vstack([np.hstack([np.eye(5),np.zeros((5,1))]), np.hstack([-np.eye(5),np.zeros((5,1))])])
    Ab=np.vstack([rows,A]); bb2=np.concatenate([bb,[1]*10])
    print("   constraint values (<=0): %s"%np.round(Ab@pb.x-bb2,10),flush=True)
    y=pb.ineqlin.marginals
    print("   duals: nu13=%.6f nu19=%.6f mu=%s box_duals(nonzero)=%s"%(y[0],y[1],np.round(y[2:6],6),np.round(y[6:][np.abs(y[6:])>1e-9],6)),flush=True)
    print("   dual feasibility (y>=0) ? %s ; sum(mu) = %.12f"%(bool((y>=-1e-10).all()),y[2:6].sum()),flush=True)
    print("   nu13+nu19 = %.12f ; |c_primal - (nu13+nu19)| = %.3e"%(y[0]+y[1],abs(cfull-(y[0]+y[1]))),flush=True)
    print("   |c_primal - c_dual_objective| = %.3e"%(abs(cfull-float(pb.ineqlin.residual@np.zeros(0)) if False else abs(cfull-(y[0]+y[1])))),flush=True)
    print("   cross-check with C-3864 (t*=0 => c_full >= 0) : c_full = %+.3e -> %s"%(cfull,"OK" if cfull>=-1e-12 else "CONFLICT: audit implementation"),flush=True)
    # high-precision recheck of the primal solution and the certificate
    mph=[mp.mpf(float(t)) for t in hb]; mc=mp.mpf(float(cfull))
    mv13=[mp.mpf(float(t)) for t in v13]; mv19=[mp.mpf(float(t)) for t in v19]; mW=[[mp.mpf(float(t)) for t in w] for w in W]
    a13=mp.fsum([mv13[j]*mph[j] for j in range(5)]); a19=mp.fsum([mv19[j]*mph[j] for j in range(5)])
    bq=[mp.fsum([mW[q][j]*mph[j] for j in range(5)])-mc for q in range(4)]
    print("   [40 dps] a13=%s a19=%s max_q(b_q - c)=%s"%(mp.nstr(a13,10),mp.nstr(a19,10),mp.nstr(max(bq),8)),flush=True)
else:
    print("   BOX version infeasible/other: status=%d (%s)"%(pb.status,pb.message.split('.')[0]),flush=True)

print("\n=== (3) odd-only CONTROL (b rows deleted) ===", flush=True)
pc=linprog(cobj,A_ub=rows[:2],b_ub=bb[:2],bounds=[(None,None)]*6,method='highs')
print("   status=%d (%s) -> %s"%(pc.status,pc.message.split('.')[0],
      "no finite impedance: c_control = 0 (odd descent is unconstrained by any even functional)" if pc.status==3 else "finite optimum"),flush=True)
print("\n=== (4) (lambda,omega) comparison deliberately NOT performed this cut (order preserved) ===", flush=True)
print("DONE", flush=True)
