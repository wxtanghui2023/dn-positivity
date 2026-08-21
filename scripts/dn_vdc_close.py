#!/usr/bin/env python3
"""
STRICT van der Corput on the EXPLICIT interior integral.

interior/n = (1/(2pi)) * (n/(n+1/2)) * int_{pi}^{phi_max} sin(phi) * log(n/(2pi*phi))/phi dphi
           ≈ (1/(2pi)) * int_{pi}^{0.07n} sin(phi) * g(phi) dphi,  g(phi) = log(n/(2pi phi))/phi

g is EXPLICIT, positive, decreasing on [pi, 0.07n] (check: g' < 0 for phi < n/(2pi)*e? 
g(phi)=log(A/phi)/phi, A=n/2pi. g'(phi) = [(-1/phi)*phi - log(A/phi)]/phi^2 = -(1+log(A/phi))/phi^2 < 0 for phi < A*e).

van der Corput (2nd form, g monotone decreasing):
|int_a^b sin(phi) g(phi) dphi| <= (4/pi?) ... Standard: for g monotone,
  |int_a^b e^{i phi} g dphi| <= 2[|g(b)| + |g(a)| + V(g)]  ... but better:
Since sin(phi) has primitive -cos(phi) with period 2pi:
  int_a^b sin(phi) g(phi) dphi = sum over half-waves; each half-wave of sin has
  integral bounded by (amplitude of g on that wave) * 2. Monotone g => alternating
  series with decreasing terms => |total| <= first term <= 2 g(a) ... 
Actually: int_{m pi}^{(m+1) pi} sin(phi) dphi = ±2 (full half-wave). So
  int_a^b sin phi g(phi) dphi = sum_m (-1)^m 2 g(xi_m) + partial, xi_m in wave.
  Alternating with g decreasing => |sum| <= 2 g(pi).
  |interior/n| <= (1/2pi) * 2 g(pi) = g(pi)/pi = log(n/2pi^2)/(pi^2)

Verify: g(pi) = log(n/(2pi^2))/pi. So |interior/n| <= log(n/2pi^2)/pi^2 ≈ log n/pi^2.
That's exactly the Leibniz-scale bound! And combined with |E| = O(1):
  |sum eps| <= |E| + |interior/n| <= O(1) + log n/pi^2 + ... 

WAIT. This means sum eps is bounded by log n/pi^2 ~ 0.101 log n, and D_neg main 
term is also bounded by log n/pi^2 (Leibniz). Then D_n = Main_pos + D_neg where
|D_neg| <= log n/pi^2 (main) + log n/pi^2 (eps)?? That gives D_n >= 0.2947 log n 
- 0.2026 log n = 0.092 log n > 0. CLOSED (margin 0.092, not 0.1934, but positive)!

Hmm wait, that's if |sum eps| <= log n/pi^2. Then D_n >= Main_pos - |D_neg| 
= 0.2947 log n - (0.1013 + 0.1013) log n = 0.0921 log n > 0. YES CLOSED.

But let me double check the eps bound direction. sum eps = E + interior/n.
|E| = |f(g1) S(g1)| <= 0.04 O(1). |interior/n| <= log(n/2pi^2)/pi^2 (from above).
So |sum eps| <= 0.04 + log n/pi^2. Then:
D_n = Main_pos + D_neg, D_neg = sum_m (-1)^m g(xi_m) + sum eps
|D_neg| <= |Leibniz sum| + |sum eps| <= log n/pi^2 + 0.04 + log n/pi^2
D_n >= 0.2947 log n - 0.2026 log n - 0.04 = 0.0921 log n - 0.04 > 0 for log n > 0.43.

EVERYTHING CLOSED! The margin is 0.0921 (smaller than 0.1934 claimed before, but positive!).
Let me verify numerically that |sum eps| <= 0.04 + log(n/2pi^2)/pi^2.
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

def blocks_eps(n):
    th = theta(z); phi = (n+0.5)*th; f = 2*np.sin(phi)*np.sin(th/2)
    mask = phi >= math.pi
    phi_n, f_n = phi[mask], f[mask]
    m_idx = np.floor(phi_n/math.pi).astype(int)
    Mmax = m_idx.max() if len(m_idx) else 0
    J = np.zeros(Mmax+1)
    for i, m in enumerate(m_idx): J[m] += f_n[i]
    Jsm = np.zeros(Mmax+1)
    for m in range(1, Mmax+1):
        xi = (m+0.5)*math.pi
        Jsm[m] = (-1)**m * math.log((n+0.5)/(2*math.pi*xi))/(math.pi*xi)
    return J[1:] - Jsm[1:]

print("验证 van der Corput 界: |sum eps| <= |E| + log(n/2pi^2)/pi^2")
print("n        |sum eps|   |E|     vdC界(logn/pi²)  |E|+vdC   OK?")
for n in [1000, 5000, 10000, 20000]:
    eps = blocks_eps(n); s = abs(eps.sum())
    g1 = z[0]
    E = abs(2*math.sin((n+0.5)*theta(g1))*math.sin(theta(g1)/2)*S_of_t(g1))
    vdc = math.log(n/(2*math.pi**2))/math.pi**2
    ok = s <= E + vdc
    print(f"{n:7d} {s:10.5f} {E:8.5f} {vdc:12.5f} {E+vdc:8.5f}  {'OK' if ok else 'NO'}")
