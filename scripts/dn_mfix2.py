#!/usr/bin/env python3
# FIXED M(T): Simpson factor /12. Vectorized theta (mpmath only for t<50).
import numpy as np
import mpmath as mp
mp.mp.dps = 20

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gmax = float(zeros[-1])

def theta_asy(t):
    t = np.maximum(t, 1e-9)
    return 0.5*t*np.log(t/(2*np.pi)) - 0.5*t - np.pi/8 + 1/(48*t) + 7/(5760*t**3) + 31/(80640*t**5)

def theta_scalar(t):
    if t < 50:
        z = mp.mpf('0.25') + 1j*mp.mpf(t)/2
        return float(mp.im(mp.loggamma(z)) - mp.mpf(t)/2*mp.log(mp.pi))
    return float(theta_asy(t))

def theta_vec(t):
    t = np.asarray(t, float)
    if t.ndim == 0:
        return theta_scalar(float(t))
    out = theta_asy(t)
    small = t < 50
    for i in np.nonzero(small)[0]:
        z = mp.mpf('0.25') + 1j*mp.mpf(t[i])/2
        out[i] = float(mp.im(mp.loggamma(z)) - mp.mpf(t[i])/2*mp.log(mp.pi))
    return out

def simp(f, a, b):
    x = np.linspace(a, b, 5)
    return (b-a)/12.0*(f(x[0])+4*f(x[1])+2*f(x[2])+4*f(x[3])+f(x[4]))

Tgrid = np.concatenate([[0.0], zeros])
Mcum = np.zeros(len(zeros)+1)
for j in range(1, len(zeros)+1):
    a, b = Tgrid[j-1], Tgrid[j]
    Mcum[j] = Mcum[j-1] + (j-2)*(b-a) - simp(theta_vec, a, b)/np.pi

print("M(T) = ∫₀^T S(u)du  (corrected Simpson /12):")
print(f"{'T':>9} {'M(T)':>12} {'max|M|≤T':>12}")
for idx in [1, 10, 100, 1000, 5000, 10000, 50000, 100000]:
    T = Tgrid[idx]
    mm = np.max(np.abs(Mcum[:idx+1]))
    print(f"{T:9.1f} {Mcum[idx]:+12.4f} {mm:12.4f}")

print("\ngrowth comparison:")
for idx in [100, 1000, 10000, 50000, 100000]:
    T = Tgrid[idx]
    mm = np.max(np.abs(Mcum[:idx+1]))
    print(f"  T={T:9.1f}:  max|M|={mm:10.4f}   (T={T:.0f}, T^0.5={T**0.5:.1f}, T·logT={T*np.log(T):.1f}, logT={np.log(T):.2f})")

# S(T) sanity
print("\nS(T) sanity (should be O(log T)):")
for idx in [100, 1000, 10000, 100000]:
    T = Tgrid[idx]
    z = mp.mpf('0.25') + 1j*mp.mpf(T)/2
    th = float(mp.im(mp.loggamma(z)) - mp.mpf(T)/2*mp.log(mp.pi))
    print(f"  T={T:9.1f}:  N={idx}, θ/π={th/np.pi:+.3f}, S={idx - th/np.pi - 1:+.4f}  (logT={np.log(T):.2f})")
