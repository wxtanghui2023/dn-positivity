#!/usr/bin/env python3
# Answer the boundary-term question rigorously:
# 1. g_n(0) = 2(-1)^n? (user's claim)
# 2. Document θ: (1/π)∫θ'_doc g_n ≡ 0  ->  D_n = Σg_n(γ) EXACT (no "other terms" needed)
# 3. RS θ: (1/π)∫θ'_RS g_n = ?  (≠0 presumably - shows doc θ ≠ RS θ, different framework)
# 4. min of Σg_n(γ) over n=1..2000 (is it always > 0?)
import numpy as np
from scipy.integrate import quad
import mpmath as mp
mp.mp.dps = 20

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gmax = float(zeros[-1])

# --- definitions ---
def theta_doc(t):
    return np.pi - 2.0*np.arctan(2.0*t)
def theta_doc_prime(t):
    return -4.0/(1.0+4.0*t*t)
def g_n_doc(t, n):
    th = theta_doc(t)
    return (t*np.sin(n*th) + 0.5*np.cos(n*th))/(0.25+t*t)

# RS theta (standard, for comparison)
def theta_RS(t):
    z = mp.mpf('0.25') + 1j*mp.mpf(t)/2
    return float(mp.im(mp.loggamma(z)) - mp.mpf(t)/2*mp.log(mp.pi))
def theta_RS_prime(t):
    z = mp.mpf('0.25') + 1j*mp.mpf(t)/2
    return float(mp.re(mp.psi(0, z))/2 - mp.log(mp.pi)/2)

# --- 1. g_n(0) ---
print("=== 1. g_n(0) ===")
for n in [1, 2, 3, 4, 10]:
    # limit t->0: [t sin(nπ) + 0.5 cos(nπ)]/(1/4) = 0 + 0.5(-1)^n * 4 = 2(-1)^n
    print(f"  n={n}: g_n(0) = 2·(-1)^{n} = {2*(-1)**n:+.1f}  (analytic)")

# --- 2. document θ integral ≡ 0 ---
print("\n=== 2. doc θ: (1/π)∫θ'_doc·g_n dt ===")
for n in [1, 2, 10, 20]:
    I1, _ = quad(lambda t: theta_doc_prime(t)*g_n_doc(t, n), 0, 100, limit=1000)
    I2, _ = quad(lambda t: theta_doc_prime(t)*g_n_doc(t, n), 100, gmax, limit=2000)
    print(f"  n={n}: {(I1+I2)/np.pi:+.8f}  (≡0, exact)")

# --- 3. RS θ integral (comparison) ---
print("\n=== 3. RS θ: (1/π)∫θ'_RS·g_n dt (≠0? doc θ ≠ RS θ) ===")
def tp_rs_fast(t):
    t = float(t)
    if t < 50:
        return theta_RS_prime(t)
    return 0.5*np.log(t/(2*np.pi)) - 1/(48*t*t) - 7/(1920*t**4)
for n in [1, 2, 10, 20]:
    I1, _ = quad(lambda t: tp_rs_fast(t)*g_n_doc(t, n), 0, 100, limit=1000)
    I2, _ = quad(lambda t: tp_rs_fast(t)*g_n_doc(t, n), 100, gmax, limit=2000)
    print(f"  n={n}: (1/π)∫θ'_RS g_n = {(I1+I2)/np.pi:+.6f}")

# --- 4. min of D_n = Σg_n(γ) over n ---
print("\n=== 4. D_n = Σg_n(γ) positivity scan ===")
mins = []
for n in list(range(1, 101)) + list(range(100, 1001, 25)) + list(range(1000, 3001, 100)):
    s = np.sum(g_n_doc(zeros, n))
    mins.append((s, n))
mins.sort()
print(f"  min over n∈[1,3000] ({len(mins)} pts): D_n = {mins[0][0]:+.6f} at n={mins[0][1]}")
print(f"  D_n > 0 for all tested n: {mins[0][0] > 0}")
# check growth: is D_n converging or growing like log?
for n in [3000, 5000, 8000, 12000]:
    s = np.sum(g_n_doc(zeros, n))
    print(f"  n={n}: D_n = {s:+.6f}  (log n = {np.log(n):.2f})")
