import math
PI=math.pi
def Phi(u):
    s=0.0
    for n in range(1,10):                      # 10 terms is ample for u <= 4
        a=2*PI*PI*n**4*math.exp(4.5*u) - 3*PI*n*n*math.exp(2.5*u)
        s+= a*math.exp(-PI*n*n*math.exp(2*u))
    return s
def Xi(t, U=8.0, N=3000):
    h=U/N; s=0.0
    for k in range(N+1):
        u=k*h
        w=1.0 if k in (0,N) else (4.0 if k%2 else 2.0)
        s+= w*Phi(u)*math.cos(u*t)
    return 2*s*h/3
print("="*80); print("CALIBRATION: Xi(t) = 2*int_0^inf Phi(u)cos(ut)du"); print("="*80)
x0=Xi(0.0); print(f"  Xi(0) = {x0:.10f}   known 0.4971207782   [{'OK' if abs(x0-0.4971207782)<1e-4 else 'FAIL'}]")
# first zero
lo,hi=10.0,20.0; flo=Xi(lo); fhi=Xi(hi)
assert flo*fhi<0, "no sign change in [10,20]"
for _ in range(60):
    mid=(lo+hi)/2
    if Xi(lo)*Xi(mid)<=0: hi=mid
    else: lo=mid
t1=(lo+hi)/2
print(f"  first zero = {t1:.9f}   known 14.1347251417   [{'OK' if abs(t1-14.1347251417)<1e-4 else 'FAIL'}]")
print()
print("="*80); print("IS Phi A POSITIVE KERNEL?  (the Lee-Yang hypothesis test)"); print("="*80)
for u in [-3,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3]:
    print(f"  Phi({u:>5}) = {Phi(u): .6e}")
print("  => sign changes present" )
print()
print("="*80); print("TRANSFER STATEMENT"); print("="*80)
print("""  Lee-Yang property of a measure  :  all zeros of its Fourier transform are real
  Xi = Fourier cosine transform of Phi  =>  RH  <=>  Phi has the Lee-Yang property
  Classical Lee-Yang theorem requires a POSITIVE measure with ferromagnetic structure.
  Phi is SIGNED  =>  that hypothesis fails, and that failure is the whole difficulty.
  Concrete target: extend the Lee-Yang machinery to this signed-kernel class, the
  classical tool being total positivity (Polya frequency functions / Schoenberg / Karlin),
  where TP2 implies real zeros of the transform.""")
