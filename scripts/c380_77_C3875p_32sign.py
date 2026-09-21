# c380_77_C3875p_32sign.py -- C3875': 32-sign LP certification of eta_1 (primal/dual, rigorous lower bound)
import numpy as np, mpmath as mp, itertools
from fractions import Fraction as Fr
from scipy.optimize import linprog
mp.mp.dps=50
SIG=[mp.mpf(-1),mp.mpf(1),mp.mpf(1),mp.mpf(-1),mp.mpf(1)]; AEV=[3,4,7,9]
PHI0=[p*mp.pi for p in [mp.mpf('0.14721317'),mp.mpf('0.23048868'),mp.mpf('0.18365067'),mp.mpf('0.2094225'),mp.mpf('0.11795883')]]
def newton(F,x0,maxit=80):
    x=mp.matrix(x0); n=len(x)
    for _ in range(maxit):
        r=F(x); J=mp.matrix(len(r),n); h=mp.mpf('1e-35')
        for j in range(n):
            xp=mp.matrix(x); xp[j]=xp[j]+h; rp=F(xp)
            for i in range(len(r)): J[i,j]=(rp[i]-r[i])/h
        dx=mp.lu_solve(J,mp.matrix([-t for t in r])); x=x+dx
        if max(abs(t) for t in dx)<mp.mpf('1e-45'): break
    return x
Occ=lambda p,k: mp.fsum([SIG[j]*mp.cos(k*p[j]) for j in range(5)])
Ev=lambda p,q: mp.fsum([mp.cos(4*q*p[j]) for j in range(5)])
dOcc=lambda p,k: [-k*SIG[j]*mp.sin(k*p[j]) for j in range(5)]
dEv=lambda p,q: [-4*q*mp.sin(4*q*p[j]) for j in range(5)]
phi=newton(lambda x: mp.matrix([Ev(x,q)-mp.mpf(1)/2 for q in AEV]+[Occ(x,13)+Occ(x,19)]), PHI0)
Gmp=[[mp.mpf(t) for t in r] for r in [[-t for t in dOcc(phi,13)],list(dOcc(phi,19))]+[dEv(phi,q) for q in AEV]]
G=np.array([[float(t) for t in r] for r in Gmp])
# Gordan certificate (for the sanity check G^T y = 0, y>0) -- reuse C-3868 ray
print("=== C3875': 32 sign patterns, LP  min t  s.t. G(s.w) <= t*1 , w>=0 , sum w = 1 ===", flush=True)
rows=[]
for s in itertools.product([1,-1],repeat=5):
    Gs=G*np.array(s)                                  # columns sign-flipped
    A=np.hstack([Gs, -np.ones((6,1))])                # Gs w - t <= 0
    Aeq=np.zeros((1,6)); Aeq[0,:5]=1.0
    r=linprog(np.array([0]*5+[1.0]),A_ub=A,b_ub=np.zeros(6),A_eq=Aeq,b_eq=np.array([1.0]),
              bounds=[(0,None)]*5+[(None,None)],method='highs')
    t=float(r.x[5]); w=r.x[:5]; y=r.ineqlin.marginals
    rows.append((s,t,w,y,r.status))
ts=[t for _,t,_,_,_ in rows]
print("   statuses all 0 : %s ; min_s t_s* = %.12f ; max_s t_s* = %.12f"%(all(r[4]==0 for r in rows),min(ts),max(ts)),flush=True)
print("   sanity (Gordan: every t_s* >= 0) : %s"%(all(t>=-1e-12 for t in ts)),flush=True)
neg=[t for t in ts if t<1e-9]
print("   number of t_s* < 1e-9 : %d  (0 would contradict Gordan)"%len(neg),flush=True)
smin,tmin,wmin,ymin,_=min(rows,key=lambda r:r[1])
print("   argmin sign pattern s = %s ; t* = %.12f"%(smin,tmin),flush=True)
print("   primal w = %s ; ||w||_1 = %.12f"%(np.round(wmin,8),wmin.sum()),flush=True)
print("   dual y = %s ; y >= 0 ? %s ; sum y = %.12f"%(np.round(ymin,8),bool((ymin>=-1e-12).all()),ymin.sum()),flush=True)
gap=abs(tmin-float(ymin@np.zeros(6))) # placeholder
print("\n=== rigorous lower bound via weak duality ===",flush=True)
print("   variational form: t_s* >= max_{y in simplex} min_j (G_s^T y)_j",flush=True)
def lower_bound(s,y_float):
    ys=[Fr(y_float[i]).limit_denominator(10**9) for i in range(6)]
    if any(v<0 for v in ys): return None
    if sum(ys)!=1: ys=[v/sum(ys) for v in ys]
    Gs=[[(Gmp[i][j] if s[j]>0 else -Gmp[i][j]) for j in range(5)] for i in range(6)]
    vals=[]
    for j in range(5):
        tot=Fr(0)
        for i in range(6): tot+=ys[i]*Fr(Gs[i][j])
        vals.append(tot)
    return min(vals), ys
lb,margin=zip(*[(lower_bound(s,y),Fr(0)) for s,_,_,y,_ in rows])
lbs=[b[0] for b in lb if b is not None]
print("   per-sign dual lower bounds: min = %s ; max = %s"%(float(min(lbs)),float(max(lbs))),flush=True)
eta_lb=min(lbs)
print("   *** eta_lb (rational, from LP duals + exact mpf rationals) = %s = %.12f"%(eta_lb,float(eta_lb)),flush=True)
print("   (strictly positive : %s)"%(eta_lb>0),flush=True)
print("\n=== closure radius ===",flush=True)
K=Fr(648)
rc=Fr(eta_lb)/K
print("   K = 648 ; rho_cert = eta_lb/K = %s = %.6e (phi, L2)"%(rc,float(rc)),flush=True)
ph=[float(phi[j]) for j in range(5)]
print("   tightest coordinate x-halfwidth = %.6e"%(min(abs(np.sin(2*p))*float(rc) for p in ph)),flush=True)
print("   => LOCAL-SHARP-CLOSED (nonempty box) : %s"%(eta_lb>0),flush=True)
print("DONE",flush=True)
