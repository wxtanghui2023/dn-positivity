"""
TPX3: decisive check.  Two-sided object Lambda(x) = -sum_k e^{-gamma_k|x|}/Xi'(gamma_k).
  If sum_k 1/Xi'(gamma_k) = 0 (forced by evenness: Xi'(-g) = -Xi'(g)), then Lambda(0)=0 and
  the 2x2 minor  Lambda(0)^2 - Lambda(d)Lambda(-d) = -Lambda(d)^2 < 0  => TP FAILS at order 2,
  for EVERY configuration.  That would mean the naive TP test on this object is structurally void.
Exact Xi and Xi' from the kernel:  Xi(t)=2 int Phi(u)cos(tu)du,  Xi'(t) = -2 int Phi(u) u sin(tu) du.
Calibration: first zero 14.134725142; Xi'(gamma_1) sign & magnitude.
"""
import math, numpy as np, mpmath as mp
mp.mp.dps=40
PI=mp.pi
U=1.6; N=4000
uu=np.linspace(0,U,N+1); ww=np.ones(N+1); ww[1:-1:2]=4; ww[2:-1:2]=2; ww=ww*(U/N)/3
def Phi_arr(u):
    s=np.zeros_like(u)
    for n in range(1,20):
        a=2*PI*PI*n**4*np.exp(4.5*u)-3*PI*n*n*np.exp(2.5*u)
        s+=a*np.exp(-PI*n*n*np.exp(2*u))
    return s
W=ww*Phi_arr(uu)
def Xi(t):  return 2.0*float(W@np.cos(uu*t))
def Xip(t): return -2.0*float(W@(uu*np.sin(uu*t)))
print("="*78); print("CALIBRATION (exact kernel route)"); print("="*78)
lo,hi=13.0,15.0
for _ in range(80):
    m=(lo+hi)/2
    if Xi(lo)*Xi(m)<=0: hi=m
    else: lo=m
g1=(lo+hi)/2
print(f"  first zero = {g1:.9f}   (known 14.134725142)  [{'OK' if abs(g1-14.134725142)<1e-6 else 'CHECK'}]")
print(f"  Xi'(gamma_1) = {Xip(g1):.8f}   (nonzero for a simple zero)")
print()
print("="*78); print("first 26 zeros via Newton from coarse seeds"); print("="*78)
def newton(t0):
    t=t0
    for _ in range(60):
        v=Xi(t); d=Xip(t)
        if abs(d)<1e-14: break
        step=v/d; t-=step
        if abs(step)<1e-12: break
    return t
seeds=[]; prev=Xi(12.0); t=12.0; h=0.02
while t<120.0:
    t+=h; v=Xi(t)
    if prev*v<0:
        a,b=t-h,t
        for _ in range(50):
            m=(a+b)/2
            if Xi(a)*Xi(m)<=0: b=m
            else: a=m
        seeds.append((a+b)/2)
    prev=v
zs=[newton(s) for s in seeds]
print(f"  found {len(zs)} zeros below 120;  first 5: {[round(z,6) for z in zs[:5]]}")
gs=[Xip(z) for z in zs]
print(f"  signs of Xi'(gamma_k): {['+' if g>0 else '-' for g in gs[:14]]}   (alternation expected)")
print()
print("="*78); print("DECISIVE: partial sums of 1/Xi'(gamma_k) over the POSITIVE zeros"); print("="*78)
inv=1.0/np.array(gs)
print(f"  {'K':>4} | {'sum_{k<=K} 1/Xi(gamma_k)':>26} | {'Lambda(0) = -sum':>18}")
for K in (5,10,15,20,25,26):
    s=float(inv[:K].sum())
    print(f"  {K:>4} | {s:>26.10e} | {-s:>18.10e}")
print()
print("="*78); print("IMPLICATION"); print("="*78)
print("""  * By evenness of Xi, Xi'(-g) = -Xi'(g), so the sum of 1/Xi' over ALL zeros is 0.
    If the positive-zero partial sum tends to 0 as K grows, then Lambda(0) = 0, and then
    the 2x2 minor Lambda(0)^2 - Lambda(d)Lambda(-d) = -Lambda(d)^2 < 0 for every d != 0.
    => the two-sided object is NOT totally positive, structure-independently.
  * A non-zero limit instead would mean Lambda(0) != 0 and the test is meaningful.""")
