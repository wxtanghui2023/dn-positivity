"""
TUR1: push OUR OWN observable (the Turan-type log-concavity margin of Xi's coefficients)
      from n<=9 to n<=20, in high precision, using only the classical kernel Phi.
  Motivation: the frontier paradigm (e.g. the 2/3 zero-proportion program) is
    (i) use ONLY the positivity available unconditionally, (ii) optimize over it,
    (iii) push the constant.  We apply that paradigm to our own asset.
  Xi(t) = 2 int_0^inf Phi(u) cos(ut) du = 2 sum_n (-1)^n M_n t^{2n}/(2n)!,  M_n = int Phi u^{2n} du
  a_n = 2(-1)^n M_n/(2n)! ;  r_n = a_n^2/(a_{n-1} a_{n+1})
Discipline: calibrate against the earlier r_1..r_9 values; no 1/2 input; L2 untouched.
"""
from mpmath import mp, mpf, exp, pi, factorial, nstr, sqrt
mp.dps=60
def Phi(u):
    u=mpf(u); s=mpf(0)
    for n in range(1,16):
        a=2*pi**2*mpf(n)**4*exp(mpf('4.5')*u) - 3*pi*mpf(n)**2*exp(mpf('2.5')*u)
        s+= a*exp(-pi*mpf(n)**2*exp(2*u))
    return s
print("="*94); print("MOMENTS  M_n = int_0^inf Phi(u) u^{2n} du   (dps=60, Simpson on [0,1.6])"); print("="*94)
N=6000; U=mpf('1.6'); h=U/N
base=[Phi(i*h) for i in range(N+1)]
def moment(k):
    s=mpf(0)
    for i in range(N+1):
        w=mpf(1) if i in (0,N) else (mpf(4) if i%2 else mpf(2))
        if k==0: s+= w*base[i]
        else: s+= w*base[i]*(mpf(i)*h)**(2*k)
    return s*h/3
Ms=[moment(k) for k in range(0,21)]
print(f"  M_0 = {nstr(Ms[0],15)}   (Xi(0)/2 = 0.2485603891)")
a=[2*((-1)**n)*Ms[n]/factorial(2*n) for n in range(0,21)]
print()
print("="*94); print("CALIBRATION: r_1..r_9 must match the earlier run"); print("="*94)
prev={1:'2.149687885',2:'1.59411549941',3:'1.40573777485',4:'1.31006309864',5:'1.25185500715',
      6:'1.21256928725',7:'1.18419917977',8:'1.16271177935',9:'1.14585060676'}
ok=True
for n in range(1,10):
    r=(a[n]**2)/(a[n-1]*a[n+1])
    good=abs(r-mpf(prev[n]))<mpf('1e-9'); ok&=good
    print(f"  r_{n} = {nstr(r,12)}   earlier {prev[n]}   [{'OK' if good else 'DIFF'}]")
print(f"  => pipeline {'VALIDATED' if ok else 'DISCREPANT'}")
print()
print("="*94); print("EXTENDED: r_n and the margin law  (r_n - 1)*n"); print("="*94)
print(f"  {'n':>3} | {'r_n':>16} | {'(r_n-1)*n':>12} | {'(r_n-1)*n/log n':>15}")
for n in range(1,20):
    r=(a[n]**2)/(a[n-1]*a[n+1])
    m=(r-1)*n
    import math
    lg=mpf(str(math.log(n))) if n>1 else mpf(1)
    print(f"  {n:>3} | {nstr(r,16)} | {nstr(m,12)} | {nstr(m/lg,15)}")
print()
print("="*94); print("READ-OFF"); print("="*94)
print("""  If (r_n-1)*n is not constant but drifts, the margin law is not c/n and the
  sub-leading term is an observable.  That law is OUR quantity, computable without
  waiting for anyone.  §RH-predicted asymptotics (Csordas-Norfolk-Varga type) would
  give the reference; if the drift matches the predicted next order, our pipeline is
  producing a genuine quantitative check rather than a restatement.""")
