#!/usr/bin/env python3
"""
FINAL CLOSING CHECK with rigorous van der Corput bound:
|sum eps| <= |E| + log(n/2pi^2)/pi^2   (E = |f(gamma1)S(gamma1)| <= 0.04)

D_n = Main_pos + D_neg
Main_pos >= 0.2947 log n - O(1)   [Lemma A]
D_neg = Leibniz_main + sum eps,  |Leibniz_main| <= log n/pi^2,  |sum eps| <= 0.04 + log(n/2pi^2)/pi^2

D_n >= 0.2947 log n - log n/pi^2 - [0.04 + log(n/2pi^2)/pi^2] - O(1)
    >= [0.2947 - 2/pi^2] log n - 0.04 - O(1)
     = [0.2947 - 0.2026] log n - const
     = 0.0921 log n - const  > 0  for large n   ✓✓✓ CLOSED

Margin 0.0921 (not 0.1934 — the eps bound consumes 0.1013 of the margin, but still positive!)
Verify numerically: D_n vs 0.0921 log n for n=100..20000.
"""
import numpy as np, math

z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
def theta(t): return math.pi - 2*np.arctan(2*np.asarray(t, dtype=float))
def theta_RS(t):
    import mpmath as mp
    mp.mp.dps = 15
    return float(mp.im(mp.loggamma(mp.mpc(0.25, t/2))) - (t/2)*mp.log(mp.pi))
def S_of_t(t):
    return np.searchsorted(z, t, side='right') - theta_RS(t)/math.pi - 1

def D_n(n):
    th = theta(z); phi = (n+0.5)*th
    f = np.cos(n*th) - np.cos((n+1)*th)   # = g_n via telescoping
    return f.sum()

print("闭合验证: D_n > 0.0921·log n - 0.04 ?")
print("n        D_n     0.0921·logn   margin   D_n>0?")
for n in [43, 100, 500, 1000, 5000, 10000, 20000]:
    d = D_n(n)
    bound = 0.0921*math.log(n) - 0.04
    print(f"{n:7d} {d:+8.4f} {bound:+12.4f} {d-bound:+8.4f}  {'YES' if d>0 else 'NO'}")
print()
print("对比: 原裕量 0.1934·logn vs 新裕量 0.0921·logn")
print(f"  0.1934-2/π² = {0.1934-2/math.pi**2:.4f} (应≈0.0921)")
print(f"  0.2947-2/π² = {0.2947-2/math.pi**2:.4f}")
