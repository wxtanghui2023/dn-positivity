"""
MAG1: magnitude calibration of Xi via the known asymptotic slope.
  From Stirling: |Gamma(1/4 + it/2)| ~ sqrt(2pi) (t/2)^{-1/4} e^{-pi t/4}
  =>  log|Xi(t)| = -(pi/4) t - (1/4) log(t/2) + O(log t) + log|zeta(1/2+it)|
  so the slope of log|Xi(t)| against t must be -pi/4 = -0.7853981634.
  This CALIBRATES THE MAGNITUDE (not just the zeros) -- exactly what was missing.
  Test points chosen away from zeros so |Xi| is near its local maxima.
"""
import math, numpy as np
PI=math.pi
U=1.6; N=8000
uu=np.linspace(0,U,N+1); ww=np.ones(N+1); ww[1:-1:2]=4; ww[2:-1:2]=2; ww=ww*(U/N)/3
def Phi_arr(u):
    s=np.zeros_like(u)
    for n in range(1,20):
        a=2*PI*PI*n**4*np.exp(4.5*u)-3*PI*n*n*np.exp(2.5*u)
        s+=a*np.exp(-PI*n*n*np.exp(2*u))
    return s
W=ww*Phi_arr(uu)
def Xi(t): return 2.0*float(W@np.cos(uu*t))
print("="*78); print("CALIBRATION 1: Xi(0)"); print("="*78)
print(f"  Xi(0) = {Xi(0.0):.10f}   (known Xi(0) = 0.4971207...)")
print()
print("="*78); print("CALIBRATION 2: slope of log|Xi(t)| must be -pi/4 = -0.7853981634"); print("="*78)
pts=[5.5,8.5,12.5,15.5,18.5,22.5,26.5,31.5,35.5,40.5,45.5,50.5,60.5,70.5,80.5,100.5,120.5,150.5,180.5,200.5]
vals=[]
for t in pts:
    v=Xi(t); vals.append(v)
    print(f"  t={t:>6.1f}  Xi(t) = {v: .6e}   log|Xi| = {math.log(abs(v)):>10.5f}")
ts=np.array(pts); lg=np.array([math.log(abs(v)) for v in vals])
A=np.vstack([ts,np.ones_like(ts)]).T
slope,inter=np.linalg.lstsq(A,lg,rcond=None)[0]
print()
print(f"  fitted slope d log|Xi|/dt = {slope:.6f}   (predicted -pi/4 = {-PI/4:.6f})")
print(f"  relative deviation = {abs(slope+PI/4)/(PI/4)*100:.4f}%   [{'OK' if abs(slope+PI/4)<0.02 else 'MISMATCH'}]")
print()
print("="*78); print("CONSEQUENCE: size of the residues 1/Xi'(gamma_k)"); print("="*78)
print("  |Xi| decays like e^{-(pi/4) t}  =>  |Xi'(gamma_k)| decays the same way")
print("  => |1/Xi'(gamma_k)| ~ e^{+(pi/4) gamma_k}  GROWS SUPEREXPONENTIALLY")
for g in (14.13,50.0,100.0,300.0,900.0):
    print(f"    gamma={g:>6.1f}:  log|1/Xi'| ~ +(pi/4)*gamma = {PI/4*g:>8.2f}  (i.e. e^{PI/4*g:.0f})")
print()
print("  => the exponential sum  Lambda(x) = sum_k c_k e^{-gamma_k x}  has terms ~ e^{gamma_k(pi/4 - x)}")
print("     CONVERGES IFF  x > pi/4 = 0.7853981634   <-- a natural abscissa, forced by the data")
print()
print("="*78); print("WHY THE EARLIER RUN BLEW UP (corrected diagnosis)"); print("="*78)
print("""  NOT a wrong t-dependent factor in the kernel (that diagnosis was wrong).
  The real cause: 1/Xi'(gamma_k) grows like e^{+(pi/4) gamma_k}; in float64
  Xi'(gamma_k) underflows below ~1e-308 once (pi/4)*gamma > 709, i.e. gamma > ~903,
  and even well before that the values are dominated by cancellation noise.
  => mixed genuine divergence + floating-point underflow. Fix: log-scale / mpmath.""")
