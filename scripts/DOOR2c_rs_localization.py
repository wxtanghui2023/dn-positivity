"""DOOR2c: proper tool = Riemann-Siegel Z-function (standard).  Calibrate on known zeros."""
import numpy as np, math
def theta(t):
    # Riemann-Siegel theta, asymptotic (accurate for t >= 10)
    return (t/2)*math.log(t/(2*math.pi)) - t/2 - math.pi/8 + 1/(48*t) + 7/(5760*t**3)
def Z(t):
    if t < 6.0:  # below the RS range: use the theta-series-free direct sum is unsafe; skip
        return float('nan')
    N=int(math.floor(math.sqrt(t/(2*math.pi))))
    s=0.0
    for n in range(1,N+1):
        s+= math.cos(theta(t)-t*math.log(n))/math.sqrt(n)
    s*=2.0
    # first RS correction
    p=math.sqrt(t/(2*math.pi))-N
    C0=math.cos(2*math.pi*(p*p-p-1/16))/math.cos(2*math.pi*p)
    s+= ((-1)**(N-1))*(t/(2*math.pi))**(-0.25)*C0
    return s
print("="*80); print("CALIBRATION on known zeros"); print("="*80)
known=[14.134725,21.022040,25.010858,30.424876,32.935062,37.586178,40.918719,43.327073,48.005151,49.773832]
zeros=[]
prev_t=10.0; prev=Z(prev_t); Tmax=520.0; dt=0.05
t=prev_t
while t<Tmax:
    t+=dt; v=Z(t)
    if v==v and prev==prev and prev*v<0:
        a,b=t-dt,t
        for _ in range(60):
            m=(a+b)/2
            if Z(a)*Z(m)<=0: b=m
            else: a=m
        zeros.append((a+b)/2)
    prev=v
print(f"  found {len(zeros)} zeros up to {Tmax}:")
print(f"    first 10 = {[round(z,6) for z in zeros[:10]]}")
err=[abs(zeros[i]-known[i]) for i in range(min(10,len(zeros)))]
print(f"    max |error| on first 10 = {max(err):.2e}   [{'OK' if max(err)<1e-4 else 'CHECK'}]")
print()
print("="*80); print("PARTIAL SUMS  S(T)=sum_{gamma<=T} 2Re[2^{i gamma}/(1/2+i gamma)]"); print("="*80)
zs=np.array(zeros); x=math.log(2.0)
term=2*np.real(np.exp(1j*zs*x)/(0.5+1j*zs))
print(f"  {'T':>7} | {'S(T)':>13} | {'|S(T)|':>10} | {'#zeros':>7} | {'chunk':>12}")
prevS=0.0; edges=[50,100,150,200,250,300,350,400,450,520]
for T in edges:
    m=zs<=T; S=float(term[m].sum())
    print(f"  {T:>7} | {S:>13.6f} | {abs(S):>10.6f} | {int(m.sum()):>7} | {S-prevS:>+12.6f}")
    prevS=S
print()
print("="*80); print("READ-OFF"); print("="*80)
print("""  Look at the "chunk" column: does it DECAY with T (decay-type localisation => a
  conversion is possible once a rate is known) or stay O(1) with no trend (=> no localisation,
  door 2 has no door) ?""")
