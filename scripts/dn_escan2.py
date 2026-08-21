#!/usr/bin/env python3
# E_S(n) = D_n - Main(n) with FAST grid-based Main (no per-n quad)
import numpy as np
import mpmath as mp
mp.mp.dps = 20
zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gmax = float(zeros[-1]); g1 = float(zeros[0])

def theta_doc(t):
    return np.pi - 2.0*np.arctan(2.0*t)
def g_n_doc(t, n):
    th = theta_doc(t)
    return (t*np.sin(n*th) + 0.5*np.cos(n*th))/(0.25+t*t)
def theta_RS_prime(t):
    z = mp.mpf('0.25') + 1j*mp.mpf(t)/2
    return float(mp.re(mp.psi(0, z))/2 - mp.log(mp.pi)/2)

# precompute θ_RS' on fine grid (mpmath below 50, asy above)
STEP = 0.25
tg = np.arange(g1, gmax, STEP)
tp = np.zeros_like(tg)
small = tg < 50
for i in np.nonzero(small)[0]:
    tp[i] = theta_RS_prime(float(tg[i]))
tp[~small] = 0.5*np.log(tg[~small]/(2*np.pi)) - 1/(48*tg[~small]**2) - 7/(1920*tg[~small]**4)

def Main_fast(n):
    # (1/π)∫_{γ1}^{gmax} g_n(γ)θ_RS'(γ)dγ + tail
    th = theta_doc(tg)
    g = (tg*np.sin(n*th) + 0.5*np.cos(n*th))/(0.25+tg*tg)
    I = np.trapz(g*tp, tg)
    tail = n*(np.log(gmax/(2*np.pi))+1)/(2*np.pi*gmax)
    return I/np.pi + tail

def D_fast(n):
    return np.sum(g_n_doc(zeros, n))

print(f"{'n':>6} {'D_n':>10} {'Main':>10} {'E_S':>10} {'E_S/Main':>9} {'Main+E_S':>10}", flush=True)
for n in [43, 50, 75, 100, 150, 200, 300, 500, 750, 1000, 1500, 2000, 3000, 5000, 7500, 10000]:
    D = D_fast(n); M = Main_fast(n); Es = D - M
    print(f"{n:6d} {D:+10.4f} {M:+10.4f} {Es:+10.4f} {Es/M:9.3f} {M+Es:+10.4f}", flush=True)

# dense scan n=43..3000 for max|E_S| and min(D_n)
print("\ndense scan n∈[43,3000]...", flush=True)
mx = 0; mx_n = 0; mnD = 1e9; mnD_n = 0
for n in range(43, 3001):
    D = D_fast(n); M = Main_fast(n)
    if abs(D-M) > mx: mx, mx_n = abs(D-M), n
    if D < mnD: mnD, mnD_n = D, n
print(f"max|E_S| = {mx:.4f} at n={mx_n};  min D_n = {mnD:.4f} at n={mnD_n}", flush=True)
print(f"all |E_S| < Main for n∈[43,3000]: check via margin", flush=True)
# margin check
worst = 1e9; worst_n = 0
for n in range(43, 3001):
    D = D_fast(n); M = Main_fast(n)
    m = M - abs(D-M)
    if m < worst: worst, worst_n = m, n
print(f"min (Main - |E_S|) = {worst:.4f} at n={worst_n}  (>0 ⟹ D_n>0 via Main+error)", flush=True)
