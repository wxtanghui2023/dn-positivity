#!/usr/bin/env python3
# D_n = ∫ g_n dS = Σ_γ g_n(γ) - (1/π)∫ θ'(t) g_n(t) dt
# g_n(t) = sin(n θ(t))/t, θ = Riemann-Siegel theta (continuous branch via loggamma)
# Robust integral: u = θ(t) substitution -> Fourier integrals handled by quad(weight='sin')
# v2: checkpointed zeros at dps=20, incremental save, low memory
import mpmath as mp
import numpy as np
from scipy import integrate, optimize
import time, json, os, sys

mp.mp.dps = 20
N_ZEROS = 2000
CACHE = '/tmp/zeros_2000.npy'

# ---------- zeros (cached, checkpointed) ----------
t0 = time.time()
if os.path.exists(CACHE):
    zeros = np.load(CACHE)
    print(f"loaded {len(zeros)} cached zeros", flush=True)
else:
    zeros = np.zeros(N_ZEROS)
    done = 0
    # resume from partial save if exists
    tmp = CACHE + '.partial'
    if os.path.exists(tmp):
        zeros = np.load(tmp)
        done = len(zeros)
        print(f"resuming from {done} zeros", flush=True)
    else:
        zeros = np.zeros(N_ZEROS)
    for k in range(done, N_ZEROS):
        zeros[k] = float(mp.im(mp.zetazero(k + 1)))
        if (k + 1) % 200 == 0:
            np.save(tmp, zeros[:k + 1])
            print(f"  ...{k+1} zeros ({time.time()-t0:.0f}s)", flush=True)
    np.save(CACHE, zeros)
    if os.path.exists(tmp):
        os.remove(tmp)
    print(f"computed {N_ZEROS} zeros in {time.time()-t0:.0f}s", flush=True)
T_max = float(zeros[-1])
print(f"last zero gamma_2000 = {T_max:.2f}", flush=True)

# ---------- theta (continuous branch) & theta' ----------
def theta_cont(t):
    z = mp.mpf('0.25') + 1j * mp.mpf(t) / 2
    return float(mp.im(mp.loggamma(z)) - mp.mpf(t) / 2 * mp.log(mp.pi))

def theta_prime(t):
    z = mp.mpf('0.25') + 1j * mp.mpf(t) / 2
    return float(mp.re(mp.psi(0, z)) / 2 - mp.log(mp.pi) / 2)

g1 = float(zeros[0])
print(f"theta(γ1={g1:.4f}) = {theta_cont(g1):.4f}", flush=True)

# ---------- inverse branches ----------
t_star = optimize.brentq(theta_prime, 1.0, 20.0)
theta_min = theta_cont(t_star)
print(f"theta min: t*={t_star:.4f}, theta_min={theta_min:.4f}", flush=True)

def t1(u):
    if u > 0: u = 0.0
    if u < theta_min: u = theta_min
    return optimize.brentq(lambda t: theta_cont(t) - u, 0.0, t_star, xtol=1e-12)

def t2(u):
    if u < theta_min: u = theta_min
    return optimize.brentq(lambda t: theta_cont(t) - u, t_star, 4000.0, xtol=1e-12)

theta_Tmax = theta_cont(T_max)
print(f"theta(T_max={T_max:.1f}) = {theta_Tmax:.1f}", flush=True)

def f1(u):
    return 1.0 / t1(u)

def f2(u):
    return 1.0 / t2(u)

from scipy.special import sici
DELTA = 1e-4   # split for the removable 1/u singularity at u=0

def robust_integral(n):
    """∫_0^Tmax θ'(t) g_n(t) dt = ∫_0^{θmin} sin(nu)/t1(u) du + ∫_{θmin}^{θ(Tmax)} sin(nu)/t2(u) du"""
    # piece 1: u from 0 down to theta_min  ->  -∫_{theta_min}^0 sin(nu)/t1(u) du
    # near u=0: t1(u) ≈ u/θ'(0), so 1/t1(u) ≈ θ'(0)/u; split off removable singularity:
    # ∫_{theta_min}^{-δ} sin(nu)/t1(u) du + θ'(0)·∫_{-δ}^0 sin(nu)/u du = ... + θ'(0)·Si(nδ)
    I1a, e1a = integrate.quad(f1, theta_min, -DELTA, weight='sin', wvar=n, limit=2000)
    thp0 = theta_prime(0.0)
    Si = sici(n * DELTA)[0]
    I1 = -(I1a + thp0 * Si)
    # piece 2
    I2, e2 = integrate.quad(f2, theta_min, theta_Tmax, weight='sin', wvar=n, limit=2000)
    return I1 + I2, e1a + e2

def direct_integral(n, a=0.0, b=None, lim=500):
    if b is None: b = T_max
    return integrate.quad(lambda t: theta_prime(t) * np.sin(n * theta_cont(t)) / t, a, b, limit=lim)

# --- validation ---
# piece 1 (has the removable singularity): compare u-domain vs direct t-domain on [0, t*]
for n in [10, 20]:
    # robust piece 1 = -(I1a + θ'(0)Si(nδ))
    I1a, _ = integrate.quad(f1, theta_min, -DELTA, weight='sin', wvar=n, limit=2000)
    thp0 = theta_prime(0.0)
    I1_rob = -(I1a + thp0 * sici(n * DELTA)[0])
    I1_dir, _ = integrate.quad(lambda t: theta_prime(t) * np.sin(n * theta_cont(t)) / t, 0.0, t_star, limit=500)
    print(f"[check piece1 n={n}] robust={I1_rob:+.8f}  direct={I1_dir:+.8f}", flush=True)

# full-range check for n=10 with high limit
I_rob10, _ = robust_integral(10)
I_dir10, e_dir = direct_integral(10, lim=3000)
print(f"[check full n=10] robust={I_rob10:+.8f}  direct={I_dir10:+.8f}  (direct err est {e_dir:.1e})", flush=True)

g_n = lambda t, n: np.sin(n * theta_cont(t)) / t
ns = [10, 20, 30, 40, 50, 60, 80, 100, 200, 300, 500, 700, 1000, 1500, 2000]
results = []

for n in ns:
    gamma_sum = sum(g_n(float(z), n) for z in zeros)
    I, eI = robust_integral(n)
    theta_integral = I / np.pi
    D_n = gamma_sum - theta_integral
    results.append({'n': n, 'gamma_sum': gamma_sum, 'theta_integral': theta_integral,
                    'D_n': D_n, 'nD_n': n * D_n, 'int_err': eI})
    print(f"n={n:5d}:  Σg_n(γ)={gamma_sum:+.8f}  -(1/π)∫θ'g_n={-theta_integral:+.8f}  "
          f"D_n={D_n:+.8f}  n·D_n={n*D_n:+.6f}   (int err {eI:.1e})", flush=True)

with open('/tmp/dn_results.json', 'w') as f:
    json.dump(results, f, indent=1)
print("\nsaved /tmp/dn_results.json", flush=True)
