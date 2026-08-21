#!/usr/bin/env python3
# Dense scan: empirical envelope of C(n) and n·D_n, precision C∞, closed-form candidates
# Key: precompute θ' on ONE fine grid, reuse for all n (fast)
import numpy as np
from scipy import integrate
import mpmath as mp
import time
mp.mp.dps = 20

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gmax = float(zeros[-1])
g1 = float(zeros[0])

def theta_prime_asy(t):
    return 0.5*np.log(t/(2*np.pi)) - 1/(48*t*t) - 7/(1920*t**4) - 31/(16128*t**6)

def theta_prime_mp(t):
    z = mp.mpf('0.25') + 1j*mp.mpf(t)/2
    return float(mp.re(mp.psi(0, z))/2 - mp.log(mp.pi)/2)

def sinc(x):
    return np.where(x==0, 1.0, np.sin(x)/x)

# ---- precompute θ' on fine grid once ----
STEP = 0.25
tg = np.arange(0.0, gmax, STEP)
tp = np.zeros_like(tg)
small = tg < 50
for i in np.nonzero(small)[0]:
    tp[i] = theta_prime_mp(float(tg[i]))
tp[~small] = theta_prime_asy(tg[~small])
print(f"grid: {len(tg)} points, step {STEP}", flush=True)

def ndn_fast(n):
    s = np.sum(sinc(zeros/n))
    I = np.trapz(tp*sinc(tg/n), tg)
    return s - I/np.pi

def C_of_n_fast(n):
    # C(n) = n·D_n - A - B, A = -(1/π)∫₀^{γ1}θ'sinc, B = -sinc(γ1/n)
    m = tg < g1
    A = -np.trapz(tp[m]*sinc(tg[m]/n), tg[m])/np.pi
    B = -sinc(g1/n)
    return ndn_fast(n) - A - B

# ---- dense scan ----
t0 = time.time()
ns = list(range(1, 11)) + list(range(10, 101, 2)) + list(range(100, 1001, 10)) + list(range(1000, 8001, 100))
vals = {}
print("scanning...", flush=True)
for n in ns:
    vals[n] = (ndn_fast(n), C_of_n_fast(n))
print(f"scan done in {time.time()-t0:.0f}s", flush=True)

ndn_arr = np.array([vals[n][0] for n in ns])
C_arr = np.array([vals[n][1] for n in ns])
n_arr = np.array(ns)

print(f"\n=== ENVELOPE (n ∈ [{ns[0]}, {ns[-1]}], {len(ns)} values) ===")
print(f"min n·D_n = {ndn_arr.min():.6f}  at n={ns[int(np.argmin(ndn_arr))]}")
print(f"max n·D_n = {ndn_arr.max():.6f}")
print(f"min C(n)  = {C_arr.min():.6f}  at n={ns[int(np.argmin(C_arr))]}")
print(f"max C(n)  = {C_arr.max():.6f}")
print(f"threshold for D_n>0: 1+θ(γ₁)/π = {1 + (theta_prime_mp(0.0)*0 + 0):.4f}... (need C > 0.4497)")

# large-n plateau: average n·D_n over n in [3000, 7000] (truncation-safe since γmax/n ≥ 10)
mask = (n_arr >= 3000) & (n_arr <= 7000)
print(f"\nplateau: mean n·D_n over n∈[3000,7000] = {ndn_arr[mask].mean():.6f} ± {ndn_arr[mask].std():.6f}")
maskC = (n_arr >= 1000) & (n_arr <= 7000)
print(f"plateau: mean C(n) over n∈[1000,7000] = {C_arr[maskC].mean():.6f} ± {C_arr[maskC].std():.6f}")

Cinf = C_arr[maskC].mean()
print(f"\nC∞ estimate ≈ {Cinf:.6f}")

# ---- closed-form candidates for C∞ ≈ 1.4452 ----
import math
print(f"\n=== C∞ closed-form candidates (target {Cinf:.6f}) ===")
cands = {
    "π/2 - 1/8": math.pi/2 - 1/8,
    "log(2π) - 7/16": math.log(2*math.pi) - 7/16,
    "log(2π) - 3/8": math.log(2*math.pi) - 3/8,
    "log(2π) - 0.3927": math.log(2*math.pi) - 0.3927,
    "1 + γ/2": 1 + mp.euler/2,
    "γ + 7/8": mp.euler + 7/8,
    "π/2 - γ/2": math.pi/2 - mp.euler/2,
    "π/2 - 1/8 - γ/16": math.pi/2 - 1/8 - mp.euler/16,
    "log(π) + 3/10": math.log(math.pi) + 0.3,
    "4/π + 1/10": 4/math.pi + 0.1,
    "3/2 - 1/20": 1.5 - 0.05,
}
for name, v in cands.items():
    print(f"  {name:28s} = {v:.6f}   diff={v-Cinf:+.6f}")

# also: check if C∞ = 1 + θ(γ₁)/π + c with c clean?
th1 = float(mp.im(mp.loggamma(mp.mpf('0.25') + 1j*mp.mpf(g1)/2)) - mp.mpf(g1)/2*mp.log(mp.pi))
c = ndn_arr[mask].mean()
print(f"\nc = lim n·D_n ≈ {c:.6f};  -θ(γ₁)/π = {-th1/math.pi:.6f}")
print(f"check: C∞ = c + θ(γ₁)/π + 1 = {c + th1/math.pi + 1:.6f} (should equal C∞ estimate {Cinf:.6f})")

# small n detail (1..9)
print(f"\n=== small n ===")
for n in range(1, 10):
    print(f"  n={n}:  n·D_n = {vals[n][0]:+.6f}  C(n) = {vals[n][1]:+.6f}")
