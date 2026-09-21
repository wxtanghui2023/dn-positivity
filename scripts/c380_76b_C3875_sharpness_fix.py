# c380_76b: corrected eta_1 LP  (u = up - um, no spurious up=um)
import numpy as np, mpmath as mp
from scipy.optimize import linprog
mp.mp.dps=40
SIG=[mp.mpf(-1),mp.mpf(1),mp.mpf(1),mp.mpf(-1),mp.mpf(1)]; AEV=[3,4,7,9]
PHI0=[p*mp.pi for p in [mp.mpf('0.14721317'),mp.mpf('0.23048868'),mp.mpf('0.18365067'),mp.mpf('0.2094225'),mp.mpf('0.11795883')]]
def newton(F,x0,maxit=80):
    x=mp.matrix(x0); n=len(x)
    for _ in range(maxit):
        r=F(x); J=mp.matrix(len(r),n); h=mp.mpf('1e-30')
        for j in range(n):
            xp=mp.matrix(x); xp[j]=xp[j]+h; rp=F(xp)
            for i in range(len(r)): J[i,j]=(rp[i]-r[i])/h
        dx=mp.lu_solve(J,mp.matrix([-t for t in r])); x=x+dx
        if max(abs(t) for t in dx)<mp.mpf('1e-40'): break
    return x
Occ=lambda p,k: mp.fsum([SIG[j]*mp.cos(k*p[j]) for j in range(5)])
Ev=lambda p,q: mp.fsum([mp.cos(4*q*p[j]) for j in range(5)])
dOcc=lambda p,k: [-k*SIG[j]*mp.sin(k*p[j]) for j in range(5)]
dEv=lambda p,q: [-4*q*mp.sin(4*q*p[j]) for j in range(5)]
phi=newton(lambda x: mp.matrix([Ev(x,q)-mp.mpf(1)/2 for q in AEV]+[Occ(x,13)+Occ(x,19)]), PHI0)
rows=[[-t for t in dOcc(phi,13)], list(dOcc(phi,19))]+[dEv(phi,q) for q in AEV]
G=np.array([[float(t) for t in r] for r in rows])
print("=== CORRECTED eta_1 LP ===", flush=True)
A=[];b=[]
for i in range(6):
    row=np.zeros(11); row[:5]=G[i]; row[5:10]=-G[i]; row[10]=-1.0; A.append(row); b.append(0.0)
row=np.zeros(11); row[:10]=1.0; A.append(row); b.append(1.0)
r=linprog(np.array([0]*10+[1.0]),A_ub=np.array(A),b_ub=np.array(b),bounds=[(0,None)]*10+[(None,None)],method='highs')
eta1=float(r.x[10]); u=r.x[:5]-r.x[5:10]
print("   status=%d ; eta_1 = %.12f"%(r.status,eta1), flush=True)
print("   u* = %s ; ||u*||_1 = %.12f ; max_i(Gu*)_i = %.12f"%(np.round(u,8),np.abs(u).sum(),max(G@u)), flush=True)
print("   consistency (max_i(Gu*) == eta_1*||u*||_1) : %s"%(abs(max(G@u)-eta1*np.abs(u).sum())<1e-9), flush=True)
print("   => eta_1 > 0 : %s"%(eta1>1e-12), flush=True)
# sanity: random directions never give max_i (Gu)_i <= 0
worst=(1e9,None)
for _ in range(200000):
    w=np.random.randn(5); w/=np.linalg.norm(w,1)
    v=max(G@w)
    if v<worst[0]: worst=(v,w)
print("   random-direction minimum of max_i(Gu)_i over the L1-sphere = %.6f (should be > 0)"%worst[0], flush=True)
K=648.0; rcert=eta1/K
print("\n=== sharpness closure ===", flush=True)
print("   eta_1 = %.9f ; K = %.1f ; r_cert = eta_1/K = %.6e"%(eta1,K,rcert), flush=True)
print("   per-coordinate phi halfwidth (sin(2phi)*r_cert, tightest) = %.3e"%min(abs(np.sin(2*float(phi[j])))*rcert for j in range(5)), flush=True)
print("   => LOCAL-SHARP-CLOSED on a nonempty (but small) box : %s"%(eta1>1e-12), flush=True)
print("DONE", flush=True)
