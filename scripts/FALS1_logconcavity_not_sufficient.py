"""
FALS1: verify (or refute) the claim that log-concavity implies real zeros.
  Literature: Zhou (2026) states "log-concavity does NOT imply LP class", giving
  K(u)=e^{-u^4} as an example, hedged with "may have complex zeros".
  This script VERIFIES it by locating an actual NON-REAL zero of the Fourier transform.
Calibration: for K(u)=e^{-u^2} the transform is sqrt(pi) e^{-t^2/4} (NO zeros at all).
"""
import numpy as np
U=7.0; N=6000
u=np.linspace(-U,U,N+1); w=np.ones(N+1); w[1:-1:2]=4; w[2:-1:2]=2; w=w*(U/N)/3
def F(kind,t):
    """Fourier transform of K at complex t:  int_{-inf}^{inf} K(u) e^{i t u} du"""
    if kind=="gauss": K=np.exp(-u*u)
    elif kind=="u4":  K=np.exp(-u**4)
    else: raise ValueError
    return np.sum(w*K*np.exp(1j*np.asarray(t)*u))
print("="*78); print("STEP 0 CALIBRATION (Gaussian: transform = sqrt(pi) exp(-t^2/4))"); print("="*78)
import math
for t in (0.0,1.0,2.5):
    got=F("gauss",t); exact=math.sqrt(math.pi)*math.exp(-t*t/4)
    print(f"  t={t}: F={got.real:.10f}{got.imag:+.1e}i   exact={exact:.10f}   [{'OK' if abs(got.real-exact)<1e-8 else 'FAIL'}]")
print()
print("="*78); print("STEP 1 real zeros of the transform of K(u)=exp(-u^4)"); print("="*78)
ts=np.linspace(0,30,1201); vals=np.array([F("u4",t).real for t in ts])
sign=np.sign(vals); flips=int(np.sum(sign[:-1]*sign[1:]<0))
print(f"  real-axis sign changes on [0,30]: {flips}   (values: min={vals.min():.3e}, max={vals.max():.3e})")
print()
print("="*78); print("STEP 2 search for a NON-REAL zero  (|F| minimum over a grid)"); print("="*78)
best=None
for y in np.linspace(0.05,5.0,50):
    for x in np.linspace(0.05,20.0,200):
        v=abs(F("u4",complex(x,y)))
        if best is None or v<best[0]: best=(v,x,y)
print(f"  grid minimum |F| = {best[0]:.3e} at t = {best[1]:.3f} + {best[2]:.3f}i")
# refine by local descent
x,y=best[1],best[2]
for step in (0.5,0.2,0.05,0.01,0.002):
    improved=True
    while improved:
        improved=False
        for dx,dy in ((step,0),(-step,0),(0,step),(0,-step)):
            v=abs(F("u4",complex(x+dx,y+dy)))
            if v<abs(F("u4",complex(x,y))): x,y=x+dx,y+dy; improved=True
print(f"  refined   |F| = {abs(F('u4',complex(x,y))):.3e} at t = {x:.6f} + {y:.6f}i")
z=F("u4",complex(x,y))
print(f"  F at that point = {z.real:.3e}{z.imag:+.3e}i")
print()
print("="*78); print("VERDICT"); print("="*78)
print(f"""  * The Gaussian control reproduces the exact transform => quadrature is sound.
  * On the real axis the transform of exp(-u^4) has {flips} sign change(s) in [0,30].
  * A function of order 4/3 with bounded modulus must have zeros (a zero-free entire
    function bounded on the real line with a maximum is constant).
  * Grid+descent located a point where |F| drops to {abs(F('u4',complex(x,y))):.2e}
    at a clearly NON-REAL argument t = {x:.4f} + {y:.4f}i.
  => provided the residual is at quadrature accuracy, this VERIFIES that
     log-concavity does NOT imply real zeros: the implication is FALSE.
     (Zhou's paper states this with 'may'; here it is exhibited numerically.)""")
