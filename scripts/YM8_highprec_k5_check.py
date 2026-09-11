"""
YM8: HIGH-PRECISION re-check of the order-5 violations found in YM7.
  YM7 (float64) found k=5 violations with min ~ -2.5e-9 while Phi spans 1e-197,
  so catastrophic cancellation is a serious candidate.  Recompute in mpmath at
  60/120 digits.  Discipline: verify before claiming.
"""
from mpmath import mp, mpf, exp, pi, matrix, det as mdet
import itertools

def setprec(d): mp.dps=d
def Phi(u):
    u=mpf(u); s=mpf(0)
    for n in range(1,16):
        a=2*pi**2*mpf(n)**4*exp(mpf('4.5')*u) - 3*pi*mpf(n)**2*exp(mpf('2.5')*u)
        s+= a*exp(-pi*mpf(n)**2*exp(2*u))
    return s
# the float64 cases that produced the most negative k=5 minors (from YM7's uniform grid h=0.1)
pts=[mpf('0.0')+mpf(k)*mpf('0.1') for k in range(0,11)]
def det_mp(M): return mdet(matrix(M))
print("="*84); print("ORDER 5, uniform grid h=0.1 : recompute ALL minors in high precision"); print("="*84)
for dps in (30,60,120):
    setprec(dps)
    neg=0; mn=None; mnidx=None; total=0
    for idx in itertools.combinations(range(len(pts)),5):
        M=[[Phi(abs(pts[a]-pts[b])) for b in idx] for a in idx]
        d=det_mp(M); total+=1
        if mn is None or d<mn: mn=d; mnidx=idx
        if d<0: neg+=1
    print(f"  dps={dps:<4} minors={total}  negative={neg}   min={mp.nstr(mn,10)}")
    if neg: print(f"        most negative at indices {mnidx}  -> points {[mp.nstr(pts[i],6) for i in mnidx]}")
print()
print("="*84); print("CONTROL: a known-positive kernel (Gaussian) must show 0 negatives"); print("="*84)
def G(u): return exp(-mpf('0.5')*u*u)
for dps in (60,):
    setprec(dps)
    neg=0
    for idx in itertools.combinations(range(11),5):
        M=[[G(abs(pts[a]-pts[b])) for b in idx] for a in idx]
        if det_mp(M)<0: neg+=1
    print(f"  Gaussian kernel, dps={dps}: negatives = {neg}  (expect 0) ")
print()
print("="*84); print("VERDICT LOGIC"); print("="*84)
print("""  * If the negative minors PERSIST at 60-120 digits => the TP5 failure is REAL
    (a genuine structural fact about Phi's kernel).
  * If they FLIP/ vanish => the float64 result was cancellation noise, TP5 may hold.
  * Either way the decisive test is this high-precision run.""")
