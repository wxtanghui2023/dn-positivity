# c380_56_B1_local_coupling.py -- B1: local first/second-order audit at candidate interior extrema
import numpy as np, itertools
np.set_printoptions(precision=6, suppress=True)

S = np.array([list(b) + [1] for b in itertools.product([-1, 1], repeat=4)], dtype=float)

def phi_of(x):                       # x_j = c_j^2, c_j = cos phi_j
    return np.arccos(np.sqrt(np.clip(x, 0, 1)))

# exact values and derivatives (in phi coordinates); F_k = sum_j gamma_j cos(k phi_j), gamma=1 even, sigma odd
def evens(phi):
    return np.array([np.sum(np.cos(4 * r * phi)) for r in range(1, 13)])          # F_{2r}, r=1..12

def odds(phi):
    return np.array([[np.sum(s * np.cos((2 * r + 1) * phi)) for r in range(13)] for s in S])  # (16,13)

def grad_even(phi, r):
    k = 2 * r
    return -k * np.sin(k * phi)                                                    # per atom

def grad_odd(phi, s, r):
    k = 2 * r + 1
    return -k * s * np.sin(k * phi)

def audit(x, tag):
    phi = phi_of(x)
    E = evens(phi); margins = 0.5 - E
    O = odds(phi)
    flat = np.abs(O)
    idx = np.unravel_index(np.argmin(np.abs(O).max(1) if False else np.array([np.abs(o).max() for o in O])), (16,))
    # choose (sigma*, r*) minimising over sigma of the max over r
    per_sigma_max = np.abs(O).max(1)
    si = int(np.argmin(per_sigma_max))
    rstar = int(np.argmax(np.abs(O[si])))
    gval = float(np.abs(O[si]).max())
    print("=== %s ===" % tag, flush=True)
    print("   g = %.6f  at sigma* = %s , active odd index r* = %d (frequency %d)" % (gval, S[si].astype(int), rstar, 2 * rstar + 1), flush=True)
    print("   even margins 1/2 - F_2r :", margins, flush=True)
    act = [r for r in range(12) if margins[r] < 0.02]
    print("   near-binding even indices (margin < 0.02) :", [(r + 1, float(margins[r])) for r in act], flush=True)
    print("   min margin = %.6f at r = %d" % (margins.min(), int(np.argmin(margins)) + 1), flush=True)
    go = grad_odd(phi, S[si], rstar)
    print("   grad F_odd (phi-coords) =", go, " ||grad|| = %.6f" % np.linalg.norm(go), flush=True)
    print("   -> all margins > 0 ? %s ; if yes and ||grad|| > 0 then a first-order improving FEASIBLE direction exists"
          % bool(margins.min() > 0), flush=True)
    if act:
        A = np.array([grad_even(phi, r) for r in [a + 1 for a in act]])
        lam, res, rk, _ = np.linalg.lstsq(A.T, -go, rcond=None)
        print("   KKT attempt with near-binding even gradients: lambda = %s (>=0 ? %s), residual = %.6f"
              % (lam, bool(np.all(lam >= -1e-12)), float(np.linalg.norm(A.T @ lam + go))), flush=True)
    return gval

# candidate 1: the best value found so far (C-3850)
x1 = np.array([0.801874, 0.561119, 0.703473, 0.627211, 0.869546])
audit(x1, "candidate from C-3850 (g = 0.876069)")

# candidate 2: the refined point of knife A (g = 0.9878)
x2 = np.array([0.702989, 0.873806, 0.797976, 0.551115, 0.628434])
audit(x2, "candidate from knife A phase 3 (g = 0.9878)")

# candidate 3: the same point with smallest margin (phase-3-like) for comparison
print()
print("=== exact second-order identities (for the record) ===", flush=True)
print("   F_k(phi+h) = F_k - k sum_j g_j sin(k phi_j) h_j - (k^2/2) sum_j g_j cos(k phi_j) h_j^2 + O(|h|^3)", flush=True)
print("   Hessian of every F_k is DIAGONAL in phi-coordinates (separable).", flush=True)
print("DONE", flush=True)
