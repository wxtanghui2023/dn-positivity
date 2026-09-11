import math, numpy as np
PI=math.pi
U=1.6; N=6000
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
print("="*78); print("CALIBRATION"); print("="*78)
lo,hi=13.0,15.0
for _ in range(90):
    m=(lo+hi)/2
    if Xi(lo)*Xi(m)<=0: hi=m
    else: lo=m
g1=(lo+hi)/2
print(f"  first zero = {g1:.9f}   (known 14.134725142) [{'OK' if abs(g1-14.134725142)<1e-6 else 'CHECK'}]")
print(f"  Xi'(gamma_1) = {Xip(g1):+.8f}")
print()
print("="*78); print("zeros below 120 (bisection on the exact kernel, fine grid)"); print("="*78)
seeds=[]; prev=Xi(12.0); t=12.0; h=0.01
while t<120.0:
    t+=h; v=Xi(t)
    if prev*v<0:
        a,b=t-h,t
        for _ in range(60):
            m=(a+b)/2
            if Xi(a)*Xi(m)<=0: b=m
            else: a=m
        seeds.append((a+b)/2)
    prev=v
def newton(t0):
    t=t0
    for _ in range(80):
        d=Xip(t)
        if abs(d)<1e-15: break
        st=Xi(t)/d; t-=st
        if abs(st)<1e-13: break
    return t
zs=[newton(s) for s in seeds]
gs=[Xip(z) for z in zs]
print(f"  found {len(zs)} zeros; first 6 = {[round(z,7) for z in zs[:6]]}")
print(f"  signs of Xi'(gamma_k), first 16: {''.join('+' if g>0 else '-' for g in gs[:16])}  (alternation expected)")
print()
print("="*78); print("DECISIVE: sum_{k<=K} 1/Xi'(gamma_k) over POSITIVE zeros"); print("="*78)
inv=[1.0/g for g in gs]
print(f"  {'K':>4} | {'partial sum':>24} | {'-sum (=Lambda(0) if it holds)':>30}")
for K in [5,10,15,20,25,len(inv)]:
    s=math.fsum(inv[:K])
    print(f"  {K:>4} | {s:>24.12e} | {-s:>30.12e}")
tot=math.fsum(inv)
print(f"  (total over all {len(inv)} zeros: {tot:.12e})")
print()
print("="*78); print("IMPLICATION"); print("="*78)
print("""  Xi'(-g) = -Xi'(g) by evenness  =>  the sum of 1/Xi' over ALL zeros is 0.
  If the positive-zero partial sums DECAY toward 0 with K, then Lambda(0)=0, hence
  2x2 minor = Lambda(0)^2 - Lambda(d)Lambda(-d) = -Lambda(d)^2 < 0 for every d != 0
  => the two-sided object is NOT totally positive for structural reasons (no configuration
  can fix it), i.e. the naive TP test on this object is structurally void.
  If instead the partial sums converge to a NON-ZERO constant, Lambda(0) != 0 and the
  TP test is meaningful and can be run as specified.""")
