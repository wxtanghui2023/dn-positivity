"""
YM5: the decisive test of the transferred criterion.
  Classical chain:  measure mu >= 0  and  its cosine/Laplace transform has only real zeros
                    <=>  the kernel is a Polya frequency (PF) object
                    <=>  (Toeplitz form) the sampled sequence is LOG-CONCAVE:  a_k^2 >= a_{k-1} a_{k+1}
  Our object: Xi(t) = 2 int_0^inf Phi(u) cos(ut) du   (Phi from the classical theta series)
  ERR#14/#15 recorded: (i) used a 'reciprocal form' for u>0; (ii) then used evenness.  BOTH wrong:
  Phi is defined by the theta series with e^{+9u/2} and is positive on the INTEGRATION DOMAIN u>=0,
  and it decays doubly-exponentially.  The sign change I first reported lives at u<0, i.e. OUTSIDE
  the integration domain, hence irrelevant.
"""
import math
PI=math.pi
def Phi(u):
    s=0.0
    for n in range(1,16):
        a=2*PI*PI*n**4*math.exp(4.5*u) - 3*PI*n*n*math.exp(2.5*u)
        s+= a*math.exp(-PI*n*n*math.exp(2*u))
    return s
print("="*82); print("STEP 0 CALIBRATION"); print("="*82)
def Xi(t,U=7.0,N=2800):
    h=U/N; s=0.0
    for k in range(N+1):
        u=k*h; w=1.0 if k in (0,N) else (4.0 if k%2 else 2.0)
        s+= w*Phi(u)*math.cos(u*t)
    return 2*s*h/3
x0=Xi(0.0); print(f"  Xi(0)/2 = {x0:.10f}   (0.4971207782/2 = 0.2485603891)  [{'OK' if abs(x0-0.2485603891)<1e-5 else 'FAIL'}]")
lo,hi=10.0,20.0
for _ in range(60):
    mid=(lo+hi)/2
    if Xi(lo)*Xi(mid)<=0: hi=mid
    else: lo=mid
t1=(lo+hi)/2
print(f"  first zero = {t1:.9f}   (known 14.1347251417)  [{'OK' if abs(t1-14.1347251417)<1e-4 else 'FAIL'}]")
print()
print("="*82); print("STEP 1  is Phi positive on the integration domain u>=0 ?"); print("="*82)
us=[0,0.1,0.2,0.3,0.4,0.5,0.7,1.0,1.3,1.5,1.8,2.0,2.5]
for u in us: print(f"  Phi({u:>4}) = {Phi(u): .6e}   {'+' if Phi(u)>0 else '-'}")
print()
print("="*82); print("STEP 2  PF2 test: log-concavity  a_k^2 >= a_{k-1} a_{k+1}"); print("="*82)
for h in (0.05, 0.1, 0.2):
    a=[Phi(k*h) for k in range(0,int(2.0/h)+1)]
    bad=[]
    for k in range(1,len(a)-1):
        lhs=a[k]**2; rhs=a[k-1]*a[k+1]
        if lhs<rhs*(1-1e-12): bad.append((k*h,a[k-1],a[k],a[k+1]))
    print(f"  h={h:<5} samples={len(a):<4} log-concavity violations: {len(bad)}")
    for b in bad[:4]: print(f"      u={b[0]:.2f}: a_prev={b[1]:.4e} a={b[2]:.4e} a_next={b[3]:.4e}")
print()
print("="*82); print("VERDICT"); print("="*82)
print("""  If violations = 0 for the sampled range, the sampled kernel satisfies the PF2/log-concavity
  condition on that range -> the classical route is OPEN on that range, and the remaining question
  becomes uniformity in u (which is exactly this project's 'uniformity' gap).
  If violations occur, their LOCATIONS tell us where the sign structure of Phi obstructs PF2.""")
