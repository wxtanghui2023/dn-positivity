"""FALS2: corrected.  Calibration fix: h = 2U/N (I had U/N, giving half the integral)."""
import numpy as np, math
U=8.0; N=8000
u=np.linspace(-U,U,N+1); w=np.ones(N+1); w[1:-1:2]=4; w[2:-1:2]=2; w=w*(2*U/N)/3
def F(kind,t):
    K={"gauss":np.exp(-u*u),"u4":np.exp(-u**4),"u3":np.exp(-np.abs(u)**3),"u6":np.exp(-u**6)}[kind]
    return np.sum(w*K*np.exp(1j*complex(t)*u))
print("="*80); print("STEP 0 CALIBRATION  (Gaussian control: F = sqrt(pi) exp(-t^2/4))"); print("="*80)
ok=True
for t in (0.0,1.0,2.5,4.0):
    got=F("gauss",t).real; ex=math.sqrt(math.pi)*math.exp(-t*t/4)
    good=abs(got-ex)<1e-8; ok&=good
    print(f"  t={t}: F={got:.10f}  exact={ex:.10f}  [{'OK' if good else 'FAIL'}]")
assert ok, "calibration failed"
print("  -> quadrature is sound")
print()
print("="*80); print("STEP 1 real zeros (sign changes) of the cosine transform"); print("="*80)
for kind in ("gauss","u3","u4","u6"):
    ts=np.linspace(0,40,4001); v=np.array([F(kind,t).real for t in ts])
    fl=int(np.sum(np.sign(v[:-1])*np.sign(v[1:])<0))
    print(f"  {kind:>6}: sign changes on [0,40] = {fl:<3}  (min={v.min():.3e}, max={v.max():.3e})")
print()
print("="*80); print("STEP 2 NON-REAL zero search: min |F| at FIXED heights y>0"); print("="*80)
xs=np.linspace(0.02,25.0,250)
for kind in ("u3","u4"):
    print(f"  --- {kind} ---")
    for y in (0.2,0.5,1.0,2.0,3.0):
        vals=[abs(F(kind,complex(x,y))) for x in xs]
        i=int(np.argmin(vals))
        print(f"    y={y:<5} min|F| = {vals[i]:.3e} at x={xs[i]:.3f}")
print()
print("="*80); print("READ-OFF (honest)"); print("="*80)
print("""  * If for some fixed y>0 the minimum of |F| is at quadrature accuracy (~1e-9 or less),
    then a genuine NON-REAL zero exists => log-concavity does not imply real zeros.
  * If the minimum stays bounded away from zero at all tested heights, then no evidence
    for a non-real zero was found => the example does NOT establish the counterexample,
    and the literature's claim (Zhou: 'may have complex zeros'; Gershon: e^{-t^4}) is
    UNVERIFIED in this test.""")
