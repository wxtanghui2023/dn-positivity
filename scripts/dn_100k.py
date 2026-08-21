#!/usr/bin/env python3
# Option C verification with 100k Odlyzko zeros
# g_n(t) = sin(t/n)/t, RS theta, D_n = Σg_n(γ) - (1/π)∫θ'g_n
# Key: n·D_n should stay ≈ 1.001 for n well below γ_max
import mpmath as mp
import numpy as np
from scipy import integrate
import time

mp.mp.dps = 20

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
print(f"loaded {len(zeros)} zeros, gamma_max = {zeros[-1]:.2f}", flush=True)

def theta_cont(t):
    z = mp.mpf('0.25') + 1j*mp.mpf(t)/2
    return float(mp.im(mp.loggamma(z)) - mp.mpf(t)/2*mp.log(mp.pi))

def theta_prime(t):
    z = mp.mpf('0.25') + 1j*mp.mpf(t)/2
    return float(mp.re(mp.psi(0, z))/2 - mp.log(mp.pi)/2)

def g_sinc(t, n):
    return np.sin(t/n)/t

# S(T) = N(T) - θ(T)/π - 1  (exact from zero count + RS theta)
def S_of_T(T):
    N = int(np.searchsorted(zeros, T))  # number of zeros <= T
    return N - theta_cont(T)/np.pi - 1.0

# ---- main computation ----
ns = [10, 20, 50, 100, 200, 500, 1000, 2000, 3000, 5000, 8000, 10000, 15000, 20000, 30000]
print(f"\n=== g_n(t)=sin(t/n)/t, 100k zeros, gamma_max={zeros[-1]:.1f} ===")
print(f"{'n':>7} {'Σg_n(γ)':>14} {'-(1/π)∫θg':>14} {'D_n':>14} {'n·D_n':>12}  {'S(γmax)':>9}")
for n in ns:
    # sum over ALL zeros (tail of sinc beyond gamma_max is tiny when gamma_max >> n)
    s = sum(g_sinc(float(z), n) for z in zeros)
    # integral 0..gamma_max with theta'
    I, eI = integrate.quad(lambda t: theta_prime(t)*g_sinc(t, n), 0.0, float(zeros[-1]), limit=2000)
    ti = I/np.pi
    D = s - ti
    print(f"{n:7d} {s:+14.6f} {-ti:+14.6f} {D:+14.6f} {n*D:+12.4f}", flush=True)

# ---- S(T) check at a few points ----
print("\n=== S(T) = N(T) - θ(T)/π - 1 (from exact zero counts) ===")
for T in [100, 500, 1000, 2515, 5000, 10000, 50000, 74921]:
    print(f"T={T:6d}:  S(T) = {S_of_T(T):+.4f}")

# ---- key identity check: D_n = -∫S g_n'  (integration by parts) ----
print("\n=== verify D_n = -∫₀^∞ S g_n' ===")
for n in [20, 100, 500]:
    # compute -∫₀^{γmax} S(t) g_n'(t) dt  (g_n' = cos(t/n)/(nt) - sin(t/n)/t²)
    gnp = lambda t: np.cos(t/n)/(n*t) - np.sin(t/n)/(t*t)
    I_S, eI = integrate.quad(lambda t: S_of_T(t)*gnp(t), 0.0, float(zeros[-1]), limit=2000)
    print(f"  n={n:4d}:  -∫S g_n' = {-I_S:+.8f}   (truncated at γmax; compare D_n from table)", flush=True)

print("\ndone", flush=True)
