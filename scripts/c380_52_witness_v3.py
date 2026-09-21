# c380_52_witness_v3.py -- 3+2 cancellation normalised (b2=1): 4 eqs / 4 unknowns, streaming output
import numpy as np
from scipy.optimize import least_squares

def res(v):
    a1, a2, a3, b = v
    return [a1**n + a2**n + a3**n - (b**n + 1.0) for n in (1, 3, 5, 7)]

rng = np.random.default_rng(52)
hits = []
print("start scanning (800 starts)...", flush=True)
for t in range(800):
    v0 = np.abs(rng.uniform(0.01, 2.0, 4)) * rng.choice([-1, 1], 4)
    try:
        r = least_squares(res, v0, xtol=1e-13, ftol=1e-13, max_nfev=600)
    except Exception:
        continue
    if np.linalg.norm(res(r.x), np.inf) < 1e-10:
        v = r.x
        dup = any(np.allclose(np.sort(v), np.sort(u), atol=1e-6) for u in hits)
        if not dup:
            hits.append(v)
            print("  HIT %d: (a1,a2,a3,beta) = %s   min=%.6f  all-pos=%s"
                  % (len(hits), np.round(v, 8), v.min(), bool(v.min() > 0)), flush=True)
print("total distinct solutions: %d" % len(hits), flush=True)
pos = [v for v in hits if v.min() > 0]
print("all-positive solutions: %d" % len(pos), flush=True)
if pos:
    v = pos[0]; a = v[:3]; b = v[3]
    x = np.array([a[0]**2, a[1]**2, a[2]**2, b**2, 1.0]); s = np.array([1., 1., 1., -1., -1.])
    c = np.sqrt(x)
    G = np.array([np.sum(s * np.cos((2*r+1) * np.arccos(np.clip(c, -1, 1)))) for r in range(4)])
    print("witness x = %s  distinct=%d  ||G||_inf = %.3e" % (np.round(x, 6), len(set(np.round(x, 9))), np.abs(G).max()), flush=True)
print("DONE", flush=True)
