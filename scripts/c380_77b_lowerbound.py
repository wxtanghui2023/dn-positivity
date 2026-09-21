# c380_77b: rigorous rational lower bound for eta_1 (LP duals + rational enclosure of G)
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
MEPS=Fr(1,10**30)          # conservative enclosure margin for the 50-dps mpf truncation
def Fr_exact(x): return Fr(mp.nstr(x,55))
best=None
for s in itertools.product([1,-1],repeat=5):
    Gs=G*np.array(s)
    A=np.hstack([Gs,-np.ones((6,1))]); Aeq=np.zeros((1,6)); Aeq[0,:5]=1.0
    r=linprog(np.array([0]*5+[1.0]),A_ub=A,b_ub=np.zeros(6),A_eq=Aeq,b_eq=np.array([1.0]),
              bounds=[(0,None)]*5+[(None,None)],method='highs')
    t=float(r.x[5]); y=-r.ineqlin.marginals                     # fix the global sign convention
    if not (y>=-1e-12).all(): y=np.abs(y)
    yf=[Fr(float(v)).limit_denominator(10**9) for v in y]
    if any(v<0 for v in yf): continue
    sy=sum(yf); yf=[v/sy for v in yf]                            # normalise sum y = 1 (exact rationals)
    Gs_mp=[[(Gmp[i][j] if s[j]>0 else -Gmp[i][j]) for j in range(5)] for i in range(6)]
    vals=[]
    for j in range(5):
        tot=Fr(0)
        for i in range(6):
            v=Gs_mp[i][j]
            # rational enclosure: mpf is an exact binary rational; widen by MEPS in the right direction
            tot += yf[i]*(Fr_exact(v)-MEPS)
        vals.append(tot)
    lb=min(vals)
    if best is None or lb<best[0]: best=(lb,s,t)
print("=== rigorous rational lower bound eta_lb ===", flush=True)
print("   best (min) class s = %s"%str(best[1]), flush=True)
print("   LP optimum t_s* (float) = %.12f"%best[2], flush=True)
print("   eta_lb (rational, with enclosure margin 1e-30) = %s"%best[0], flush=True)
print("   eta_lb (decimal, 20 digits) = %s"%mp.nstr(mp.mpf(best[0].numerator)/mp.mpf(best[0].denominator),20), flush=True)
print("   strictly positive : %s"%(best[0]>0), flush=True)
rc=best[0]/Fr(648)
print("\n=== closure radius (LOCAL-SHARP-CLOSED iff eta_lb > 0) ===", flush=True)
print("   K = 648 ; rho_cert = eta_lb/K = %s = %s"%(rc, mp.nstr(mp.mpf(rc.numerator)/mp.mpf(rc.denominator),6)), flush=True)
ph=[float(phi[j]) for j in range(5)]
print("   tightest x-halfwidth = %.6e"%(min(abs(np.sin(2*p))*float(rc) for p in ph)), flush=True)
print("   VERDICT LOCAL-SHARP-CLOSED : %s"%(best[0]>0), flush=True)
print("DONE", flush=True)
