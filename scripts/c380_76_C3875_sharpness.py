# c380_76_C3875_sharpness.py -- C3875: first-order local sharpness closure (no Hessian matrix)
import numpy as np, mpmath as mp
from scipy.optimize import linprog
mp.mp.dps=40
SIG=[mp.mpf(-1),mp.mpf(1),mp.mpf(1),mp.mpf(-1),mp.mpf(1)]
PHI0=[p*mp.pi for p in [mp.mpf('0.14721317'),mp.mpf('0.23048868'),mp.mpf('0.18365067'),mp.mpf('0.2094225'),mp.mpf('0.11795883')]]
AEV=[3,4,7,9]
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
print("x* rebuilt (40 dps): x =", [mp.nstr(mp.cos(phi[j])**2,22) for j in range(5)], flush=True)
print("  phi/pi =", [mp.nstr(phi[j]/mp.pi,20) for j in range(5)], flush=True)

# G rows = gradients of g_13 = -F_13, g_19 = +F_19, g_q = F_2q - 1/2  (all at x*)
rows=[[-t for t in dOcc(phi,13)], list(dOcc(phi,19))]+[dEv(phi,q) for q in AEV]
G=np.array([[float(t) for t in r] for r in rows])
print("\n=== eta_1 = min over the L1-sphere of max_i (G u)_i  (LP) ===", flush=True)
# min t  s.t.  G u <= t*1 ,  u = up-um ,  sum(up+um)=1 , up,um>=0
A=[]; b=[]
for i in range(6):
    row=np.zeros(11); row[:5]=G[i]; row[10]=-1.0; A.append(row); b.append(0.0)
for j in range(5):
    row=np.zeros(11); row[j]=1.0; row[5+j]=-1.0; A.append(row); b.append(0.0)   # u = up-um
row=np.zeros(11); row[:10]=1.0; A.append(row); b.append(1.0)                     # sum(up+um)=1
A=np.array(A); b=np.array(b)
res=linprog(np.array([0,0,0,0,0,0,0,0,0,0,1.0]),A_ub=A,b_ub=b,bounds=[(0,None)]*10+[(None,None)],method='highs')
eta1=float(res.x[10]); u=res.x[:5]-res.x[5:10]
print("   status=%d ; eta_1 = %.12f"%(res.status,eta1), flush=True)
print("   minimising direction u* = %s ; ||u*||_1 = %.12f"%(np.round(u,8),np.abs(u).sum()), flush=True)
print("   max_i (G u*)_i = %.12f  (= eta_1 * |u*|_1)"%max(G@u), flush=True)
print("   => Gordan implies eta_1 > 0 : %s"%(eta1>0), flush=True)

print("\n=== K : explicit diagonal-Hessian bound (phi coordinates) ===", flush=True)
print("   F_2q = sum_j cos(4q phi_j) -> |d^2/dphi_j^2| = (4q)^2 <= 36^2 = 1296", flush=True)
print("   F_13,F_19 -> |d^2| <= 23^2 = 529", flush=True)
K=0.5*1296.0
print("   K := 0.5 * 1296 = %.1f   (|R_i(h)| <= K ||h||_2^2)"%K, flush=True)

print("\n=== sharpness closure: eta_1*r - K*r^2 > 0  <=>  0 < r < eta_1/K ===", flush=True)
rcert=eta1/K
print("   certified radius in ||.||_2 (phi units): r_cert = %.9e"%rcert, flush=True)
print("   (eta_1/K = %.9f / %.1f)"%(eta1,K), flush=True)
ph=[float(phi[j]) for j in range(5)]
print("   per-coordinate phi-halfwidth that is certified: min_j sin(2phi_j)*r_cert = %.3e"%min(abs(np.sin(2*p))*rcert for p in ph), flush=True)
print("   corresponding x-halfwidth (dx = sin(2phi) dphi): rho_j = %.3e for the tightest coordinate"%min(abs(np.sin(2*p))*rcert for p in ph), flush=True)
print("\n=== verdict inputs ===", flush=True)
print("   eta_1 > 0 : %s   (so the first-order closure EXISTS in a nonempty box)"%(eta1>0), flush=True)
print("   box radius certified: %.3e (phi, L2) -- very small => global part still needed" % rcert, flush=True)
print("DONE", flush=True)
