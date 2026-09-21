# c380_64_beta1prime.py -- B1-beta-1': correct critical cone + 2nd-order ledger + paired control
import numpy as np
from scipy.optimize import root, linprog
SIG=np.array([-1.,1.,1.,-1.,1.]); AEV=[3,4,7,9]        # even: F_{2q}, frequencies 4q = 12,16,28,36
KODD=[13,19]; S=[-1.0,1.0]                              # odd frequencies and their sign(O)
PHI0=np.array([0.14721317,0.23048868,0.18365067,0.2094225,0.11795883])*np.pi
O=lambda p,k: float(np.sum(SIG*np.cos(k*p))); E=lambda p,q: float(np.sum(np.cos(4*q*p)))
gO=lambda p,k: -k*SIG*np.sin(k*p);           gE=lambda p,q: -4*q*np.sin(4*q*p)
res=lambda p: np.concatenate([[E(p,q)-0.5 for q in AEV],[abs(O(p,13))-abs(O(p,19))]])
phi=root(res,PHI0,method='lm',options={'xtol':1e-15,'ftol':1e-15}).x
print("point: residual %.1e ; x=%s" % (np.abs(res(phi)).max(), np.round(np.cos(phi)**2,8)), flush=True)

GE=np.array([gE(phi,q) for q in AEV])                    # 4x5
GO=np.array([S[i]*gO(phi,k) for i,k in enumerate(KODD)])  # 2x5 (sign-included)

def maxdescent(rows, tag):
    # maximise t s.t. rows.h + t <= 0 , |h|_inf <= 1  -> t* > 0 means a strict first-order descent direction
    n=5; Aub=np.hstack([rows, np.ones((rows.shape[0],1))]); bub=np.zeros(rows.shape[0])
    bnds=[(-1,1)]*5+[(None,1.0)]
    r=linprog(np.array([0]*5+[-1.0]), A_ub=Aub, b_ub=bub, bounds=bnds, method='highs')
    t=float(r.x[5]); h=r.x[:5]
    print("   [%s] t* = %+.6e  (t*>0 -> C1/B1: strict descent exists) ; h = %s" % (tag,t,np.round(h,6)), flush=True)
    return t,h

print("\n=== 1) full problem: cone {gradF_2q.h<=0, s_k gradF_k.h<=0} ===", flush=True)
t_full,h_full=maxdescent(np.vstack([GE,GO]),"full")
print("\n=== 2) CONTROL: even constraints deleted ===", flush=True)
t_ctrl,h_ctrl=maxdescent(GO,"control")
print("   => paired-control difference: t*_full = %+.3e vs t*_control = %+.3e ; changed? %s"
      % (t_full,t_ctrl,abs(t_full-t_ctrl)>1e-9), flush=True)

print("\n=== 3) baseline direction h0 (is it in the corrected cone?) ===", flush=True)
h0=np.array([0.69753232,0.34098495,0.40239657,0.33576379,0.35002514])
print("   even first-order: %s (all <= 0 ? %s)" % (np.round(GE@h0,6), bool((GE@h0<=0).all())), flush=True)
print("   odd  first-order: %s (both <= 0 ? %s)" % (np.round(GO@h0,6), bool((GO@h0<=0).all())), flush=True)

print("\n=== 4) second-order ledger on sampled cone directions ===", flush=True)
rng=np.random.default_rng(6464); n=0; c1=0; both0=0; patterns={}
Qk=lambda p,k,gam: -(k**2)*float(np.sum(gam*np.cos(k*p)*1.0*h**2))
best=None
for _ in range(60000):
    h=rng.normal(0,1,5); h/=np.linalg.norm(h)
    ve=GE@h; vo=GO@h
    if (ve<=0).all() and (vo<=0).all():
        n+=1
        if (vo<0).all() and (ve<0).all(): c1+=1
        if abs(vo[0])<1e-12 and abs(vo[1])<1e-12: both0+=1
        Q={ '13':-(13**2)*float(np.sum(SIG*np.cos(13*phi)*h**2)),
            '19':-(19**2)*float(np.sum(SIG*np.cos(19*phi)*h**2)),
            '6':-(12**2)*float(np.sum(np.cos(12*phi)*h**2)), '8':-(16**2)*float(np.sum(np.cos(16*phi)*h**2)),
            '14':-(28**2)*float(np.sum(np.cos(28*phi)*h**2)), '18':-(36**2)*float(np.sum(np.cos(36*phi)*h**2))}
        # candidate second-order descent: odd max decreases (min(Q13',Q19')<0) while even stay feasible (Q<=0)
        sgn_odd = np.array([Q['13'],Q['19']])*np.array(S)
        if min(sgn_odd)<0 and max(Q['6'],Q['8'],Q['14'],Q['18'])<=0:
            if best is None or min(sgn_odd)<best[0]: best=(min(sgn_odd),h.copy(),Q)
print("   cone samples: %d / 60000 ; strict C1 directions: %d ; both-odd-equality: %d" % (n,c1,both0), flush=True)
if best:
    print("   SECOND-ORDER DESCENT FOUND: odd 2nd-order decrease %.3e with all even Q_k <= 0 -> point not a local min" % best[0], flush=True)
else:
    print("   no second-order descent found within the sampled cone (see exit classification)", flush=True)
print("DONE", flush=True)
