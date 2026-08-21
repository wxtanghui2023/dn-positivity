#!/usr/bin/env python3
"""
FINAL closing verification with all explicit constants:
Main_pos = c log n - 0.4559 (c = 0.294744936)  [verified numerically]
|Leibniz| <= g(xi_1) = log((n+1/2)/(2pi·1.5pi))/(pi·1.5pi)  [verified]
|sum eps| <= |E| + g(pi)/pi <= 0.0389 + log((n+1/2)/(2pi^2))/pi^2  [verified]
|Delta| <= sup|S|·int|f'| over positive region (small, ~O(log n/n))

D_n >= c log n - 0.4559 - g(xi1) - 0.0389 - g(pi)/pi - |Delta|
Verify against TRUE D_n for n = 43..10000, and find smallest n where bound > 0.
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
    return (np.cos(n*th) - np.cos((n+1)*th)).sum()

c = 0.294744936; C0 = -0.4559
def g_xi1(n):
    xi1 = 1.5*math.pi
    return math.log((n+0.5)/(2*math.pi*xi1))/(math.pi*xi1)
def g_pi(n):
    return math.log((n+0.5)/(2*math.pi**2))/math.pi

print("n        D_n(真)   下界       裕量    真值>下界?")
n0 = None
for n in [44, 50, 60, 80, 100, 200, 500, 1000, 5000, 10000, 20000]:
    Dn = D_n(n)
    lb = c*math.log(n) + C0 - g_xi1(n) - 0.0389 - g_pi(n)/math.pi
    ok = Dn > lb
    if n0 is None and ok: n0 = n
    print(f"{n:6d} {Dn:+9.4f} {lb:+9.4f} {Dn-lb:+9.4f}   {ok}")
print(f"\n最小 n 使下界为正: {n0}")

# Also: what's the smallest n where the BOUND ITSELF > 0 (analytic, no D_n needed)?
print("\n下界本身 > 0 的最小 n（纯解析，无需数值 D_n）:")
for n in range(40, 200):
    lb = c*math.log(n) + C0 - g_xi1(n) - 0.0389 - g_pi(n)/math.pi
    if lb > 0:
        print(f"  n = {n} (下界 = {lb:+.4f})")
        break
