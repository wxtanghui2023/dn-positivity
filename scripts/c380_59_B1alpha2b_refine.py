# c380_59_B1alpha2b_refine.py -- B1-alpha-2b: constrained local refinement + subdifferential LP audit
import numpy as np, itertools
from scipy.optimize import minimize, linprog
rng = np.random.default_rng(59271)
SIG = [np.array(list(b)+[1], dtype=float) for b in itertools.product([-1,1], repeat=4)]
X0 = np.array([0.801874, 0.561119, 0.703473, 0.627211, 0.869546])   # C-3850 point
PHI0 = np.arccos(np.sqrt(X0))

def F_odd(phi, s, r): return float(np.sum(s*np.cos((2*r+1)*phi)))
def F_even(phi, r):   return float(np.sum(np.cos(4*r*phi)))
def g_odd(phi, s, r): return -(2*r+1)*s*np.sin((2*r+1)*phi)
def g_even(phi, r):   return -4*r*np.sin(4*r*phi)

def solve_one(s, start, maxit=200):
    def obj(z): return z[5]
    def cons(z):
        phi, t = z[:5], z[5]
        c = [abs(F_odd(phi, s, r)) - t for r in range(13)]
        c += [F_even(phi, r) - 0.5 for r in range(1, 13)]
        return np.array(c)
    z0 = np.concatenate([start, [max(abs(F_odd(start, s, r)) for r in range(13))]])
    try:
        r = minimize(obj, z0, method='SLSQP', constraints={'type':'ineq','fun':cons},
                     bounds=[(1e-6, np.pi/2-1e-6)]*5 + [(0, None)], options={'maxiter':maxit,'ftol':1e-12})
    except Exception:
        return None
    phi = r.x[:5]
    marg = np.array([0.5 - F_even(phi, r_) for r_ in range(1,13)])
    if marg.min() < -1e-9: return None
    g = max(abs(F_odd(phi, s, r_)) for r_ in range(13))
    return g, phi, marg

print("=== B1-alpha-2b: SLSQP refinement from the C-3850 point (multi-start per sigma) ===", flush=True)
best = None
for si, s in enumerate(SIG):
    loc = None
    for t in range(120):
        start = PHI0 + (rng.normal(0, 0.08, 5) if t else 0.0)
        start = np.clip(start, 1e-3, np.pi/2-1e-3)
        out = solve_one(s, start)
        if out and (loc is None or out[0] < loc[0]): loc = out
    if loc:
        marg = loc[2]
        A = [q for q in range(1,13) if marg[q-1] <= 1e-6]
        ties = [r for r in range(13) if abs(abs(F_odd(loc[1], s, r)) - loc[0]) <= 1e-7]
        print("  sigma=%s : g=%.9f | active even A=%s | tied odd r=%s | min margin=%.2e"
              % (s.astype(int), loc[0], A, ties, marg.min()), flush=True)
        if best is None or loc[0] < best[0]: best = (loc[0], loc[1], loc[2], s, A, ties)

print("\n=== checks on the overall best point ===", flush=True)
g, phi, marg, s, A, ties = best
print("   g = %.9f  (< 0.876069 + eps ? %s)" % (g, g < 0.876069 + 1e-6), flush=True)
print("   all even constraints satisfied ? %s (min margin %.3e)" % (marg.min() >= -1e-9, marg.min()), flush=True)
print("   active even set A = %s ; tied odd indices = %s" % (A, ties), flush=True)
print("   phi/pi = %s ; x = %s" % (np.round(phi/np.pi, 6), np.round(np.cos(phi)**2, 6)), flush=True)

print("\n=== subdifferential LP audit (only meaningful if the above is a genuine local min) ===", flush=True)
for tol in (1e-7, 1e-6, 1e-5):
    I = [r for r in range(13) if abs(abs(F_odd(phi, s, r)) - g) <= tol]
    Aq = [q for q in range(1,13) if marg[q-1] <= tol]
    W = np.array([np.sign(F_odd(phi, s, r))*g_odd(phi, s, r) for r in I])
    G = np.array([g_even(phi, q) for q in Aq]) if Aq else np.zeros((0,5))
    m, n = len(I), len(Aq)
    Aeq = np.vstack([np.hstack([W.T, G.T]), np.hstack([np.ones(m), np.zeros(n)])])
    beq = np.concatenate([np.zeros(5), [1.0]])
    res = linprog(np.zeros(m+n), A_eq=Aeq, b_eq=beq, bounds=[(0,None)]*(m+n), method='highs')
    ok = res.status == 0
    resid = float(np.linalg.norm(W.T@res.x[:m] + (G.T@res.x[m:] if n else 0))) if ok else float('nan')
    print("   tol=%.0e : |I|=%d A=%s -> subdiff-KKT=%s residual=%.2e" % (tol, m, Aq, ok, resid), flush=True)
    if ok:
        print("        omega = %s ; lambda = %s" % (np.round(res.x[:m],5), np.round(res.x[m:],5)), flush=True)
print("DONE", flush=True)
