"""
CVS2: total-positivity check of the Connes-van Suijlekom matrix family
  q_ij = (f'(lambda_i) - f'(lambda_j))/(lambda_i - lambda_j)   (i != j)
  q_ii = f''(lambda_i)                                          (diagonal)
  lambda_i = i, the spectrum of the circle Dirac operator.
Classical criterion to test:
  * PSD  <=> f convex                     (Loewner 1934)
  * TOTAL positivity (all minors >= 0) <=> f' ABSOLUTELY MONOTONE (all derivatives >= 0)
We test: (a) f' = e^x  (absolutely monotone)  -> expect TP
         (b) f' = x^2  (convex, not abs.monotone) -> expect PSD but NOT TP
         (c) f' = 1/(1+e^{-x}) (logistic, abs.monotone) -> expect TP
         (d) f' = log(1+e^x) (convex, not abs.monotone) -> expect not TP
Method: random index subsets, orders k=2..6, count negative minors; also min eigenvalue.
"""
import numpy as np, itertools
rng=np.random.default_rng(7)
def loewner(fp, fpp, xs):
    n=len(xs); Q=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            Q[i,j]=fpp(xs[i]) if i==j else (fp(xs[i])-fp(xs[j]))/(xs[i]-xs[j])
    return Q
def tp_test(Q, orders, trials=400):
    n=Q.shape[0]; out={}
    for k in orders:
        worst=0.0; neg=0
        for _ in range(trials):
            idx=sorted(rng.choice(n,k,replace=False))
            m=np.linalg.det(Q[np.ix_(idx,idx)])
            if m<0: neg+=1
            worst=min(worst,m) if neg else worst if worst else m
            worst=min(worst,m)
        out[k]=(worst,neg)
    return out
xs=np.arange(-6,7).astype(float)          # lambda_i = i, i=-6..6  (13 points)
cases={
 "a) f'=e^x        (abs.monotone)":(lambda x:np.exp(x),      lambda x:np.exp(x)),
 "b) f'=x^2        (convex only) ":((lambda x:x**2),         (lambda x:2.0+0*x)),
 "c) f'=logistic   (abs.monotone)":((lambda x:1/(1+np.exp(-x))),(lambda x:np.exp(-x)/(1+np.exp(-x))**2)),
 "d) f'=log(1+e^x) (convex only) ":((lambda x:np.log(1+np.exp(x))),(lambda x:np.exp(x)/(1+np.exp(x)))),
}
print("="*92); print("Loewner/spectral-action matrices: positivity vs total positivity"); print("="*92)
print(f"  {'case':>32} | {'min eig':>10} | {'k=2':>14} | {'k=3':>14} | {'k=4':>14} | {'k=5':>14}")
for name,(fp,fpp) in cases.items():
    Q=loewner(fp,fpp,xs)
    ev=np.linalg.eigvalsh(Q).min()
    cells=[]
    for k in (2,3,4,5):
        worst,neg=tp_test(Q,[k])[k]
        cells.append(f"{'OK' if neg==0 else 'NEG'}:{worst:>8.1e}")
    print(f"  {name:>32} | {ev:>10.2e} | " + " | ".join(f"{c:>14}" for c in cells))
print()
print("="*92); print("READ-OFF"); print("="*92)
print("""  * If (a),(c) [absolutely monotone] show no negative minors while (b),(d) [merely convex]
    do show them, then the classical criterion is confirmed: POSITIVITY needs only convexity,
    but TOTAL POSITIVITY needs absolute monotonicity of f' -- a strictly stronger condition.
  * Consequence for the Connes-van Suijlekom mechanism: what their proof uses is
    POSITIVITY PLUS RANK DEFICIENCY (verified separately in CVS1c), NOT total positivity.""")
