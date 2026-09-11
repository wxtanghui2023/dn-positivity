import numpy as np
from mpmath import mp, mpf, euler, log as mlog, pi as mpi
mp.dps=30
g=np.load('/tmp/zeros_odlyzko_2M.npy').astype(float).ravel(); g=np.sort(g)
T=float(g[-1]); N=g.size
th=np.arctan2(g, g**2-0.25)
def A(n): return float(np.sum(1.0-np.cos(n*th)))
T=float(g[-1]); N=g.size
th=np.arctan2(g, g**2-0.25)
def A(n): return float(np.sum(1.0-np.cos(n*th)))
lam1_true=mpf('0.5')*euler + 1 - mlog(4*mpi)/2
print("="*92); print("TRACKA2: calibrate against the known lambda_1"); print("="*92)
print("  known  lambda_1 = 0.5*gamma_E + 1 - 0.5*log(4pi) = %s" % mp.nstr(lam1_true,18))
for n in (1,2,3,5):
    a=A(n)
    print("  n=%d : A(n) = %.10f   2*A(n) = %.10f   ratio 2A/lam1_true = %.6f" % (n,a,2*a,2*a/float(lam1_true)))
print()
print("  (if n=1 matches to ~1e-3, the factor 2 is confirmed and the whole conversion is calibrated)")
# tail check: the discarded positive tail contribution to lambda_1
# sum over gamma>T of the on-line Re(1/rho) = (1/2)sum_{gamma>T} 1/(1/4+gamma^2) * 2 (pairs)
Bt=0.5*float(np.sum(1.0/np.maximum(g,1)**2))  # not the tail; do it analytically:
# sum_{gamma>T} gamma^{-2} ~ (log T + 1)/(2 pi T)
St=(np.log(T)+1)/(2*np.pi*T)
print()
print("  analytic tail  sum_{gamma>T} gamma^{-2} ~ (logT+1)/(2 pi T) = %.6e" % St)
print("  its contribution to lambda_1 (pairs, Re(1/rho)~(1/2)/gamma^2) = %.6e" % (St,))
print("  => 2*A(1) + tail = %.10f  vs known %.10f" % (2*A(1)+St, float(lam1_true)))
print()
print("="*92); print("CONSEQUENCE"); print("="*92)
print("""  * lambda_n >= 2*A(n) - n*B_T   (B_T = (1/2)sum_{gamma>T} gamma^{-2} ~ (logT+1)/(4 pi T))
  * the factor 2 doubles every margin and doubles the achievable range.""")
