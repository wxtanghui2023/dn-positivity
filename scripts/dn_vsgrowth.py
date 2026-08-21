#!/usr/bin/env python3
"""
Measure V(S) growth and |sum eps| bounds accurately over a range of n.
Key question: does V(S) grow like O(log n)? O(sqrt(n))? O(n^alpha)?
And: is |sum eps| bounded by a constant (independent of n)?
"""
import numpy as np, math

z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
def theta(t): return math.pi - 2*np.arctan(2*np.asarray(t, dtype=float))
def theta_RS(t):
    import mpmath as mp
    mp.mp.dps = 18
    return float(mp.im(mp.loggamma(mp.mpc(0.25, t/2))) - (t/2)*mp.log(mp.pi))
def S_of_t(t):
    return np.searchsorted(z, t, side='right') - theta_RS(t)/math.pi - 1

# V(S) over [gamma_1, T] for various T (in t-coordinate) -- independent of n
print("=== V(S) 增长 vs T ===")
for T in [100, 318, 1591, 3183, 6366, 15915, 31830, 74921]:
    ts = np.linspace(z[0], T, 2000)
    Ss = np.array([S_of_t(t) for t in ts])
    V = np.abs(np.diff(Ss)).sum()
    N = np.searchsorted(z, T, side='right')
    print(f"  T={T:7d}: N(T)={N:6d}  V(S)={V:8.1f}  V/N={V/N:.4f}  V/logT={V/math.log(T):.1f}")
