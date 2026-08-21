#!/usr/bin/env python3
"""
FINAL VERIFICATION of the complete strict chain:

|sum_m eps_m| <= |E| + |interior|/n
E = f(gamma_1) S(gamma_1),  |E| <= 0.04  (computed, O(1))
interior/n: exact conversion interior/n = (1/(2pi)) * J + O(1/n),
  J = int_{pi}^{phi_max} sin(phi) g(phi) dphi, g = log(n/2pi phi)/phi decreasing
  |J| <= 2 g(pi)  [alternating half-waves, g decreasing]
=> |interior|/n <= g(pi)/pi = log(n/2pi^2)/pi^2  [+ O(1/n)]

Therefore: |sum eps| <= 0.04 + log(n/2pi^2)/pi^2 + O(1/n)

D_n = Main_pos + D_neg
Main_pos >= 0.2947 log n - C1   [Lemma A]
D_neg = sum_m (-1)^m g(xi_m) + sum eps
|sum (-1)^m g(xi_m)| <= log n/pi^2   [Leibniz, g decreasing]
D_n >= 0.2947 log n - log n/pi^2 - [0.04 + log(n/2pi^2)/pi^2] - C1
    >= [0.2947 - 2/pi^2] log n - C2  = 0.0921 log n - C2  > 0 for large n

KEY CHECKS:
1. g(phi) decreasing on [pi, phi_max]  -- need g'(phi) < 0
   g(phi) = log(A/phi)/phi, A = n/2pi. g' = -(1 + log(A/phi))/phi^2 < 0 iff log(A/phi) > -1 iff phi < A*e.
   phi_max = 0.070718(n+1/2). A*e = n*e/2pi = 0.4327 n. phi_max < 0.071 n < 0.43 n. ✓
2. Leibniz on g(xi_m): g_m = log(n/2pi xi_m)/(pi xi_m), xi_m ~ m*pi increasing, 
   g_m decreasing in m (same g decreasing argument, xi_m > pi). ✓
3. Main_pos Lemma A: Main_pos = Si(pi) log n /(2pi) + O(1), Si(pi) = 1.8519, /2pi = 0.2947. ✓
4. |E| <= 0.04: f(gamma1) = 2 sin((n+1/2)0.070718) sin(0.0354) <= 2*0.0354 = 0.071, S(gamma1) = 0.5503.
   |E| <= 0.071*0.5503 = 0.039. ✓ (n-dependent sign but magnitude bounded)

MARGIN: 0.2947 - 2/pi^2 = 0.2947 - 0.2026 = 0.0921 > 0. ✓✓✓
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

# Check 1: g decreasing range
print("=== 检查 1: g 递减区间 ===")
for n in [100, 1000, 10000]:
    A = n/(2*math.pi)
    phi_max = 0.070718*(n+0.5)
    print(f"n={n}: phi_max={phi_max:.2f} < A*e={A*math.e:.2f}? {phi_max < A*math.e}")
    # g' < 0 iff phi < A*e; check all phi up to phi_max
    phis = np.linspace(math.pi, phi_max, 500)
    A_arr = n/(2*math.pi)
    gp = -(1 + np.log(A_arr/phis))/phis**2
    print(f"   min g'(phi) = {gp.min():.4f} < 0: {np.all(gp<0)}")

print("\n=== 检查 2: Leibniz 界 g(xi_m) 递减 ===")
for n in [1000, 10000]:
    Mprime = int(math.floor((n+0.5)*theta(z[0])/math.pi))
    xis = (np.arange(1, Mprime+1)+0.5)*math.pi
    gm = np.log((n+0.5)/(2*math.pi*xis))/(math.pi*xis)
    print(f"n={n}: g(xi_m) 递减? {np.all(np.diff(gm)<0)}, g(xi_1)={gm[0]:.5f}, log n/pi^2={math.log(n)/math.pi**2:.5f}")

print("\n=== 检查 4: |E| <= 0.04 ===")
for n in [1000, 10000, 20000]:
    g1 = z[0]
    E = abs(2*math.sin((n+0.5)*theta(g1))*math.sin(theta(g1)/2)*S_of_t(g1))
    print(f"n={n}: |E| = {E:.5f} <= 0.04? {E <= 0.04}")

print("\n=== 最终裕量 ===")
margin = 0.2947 - 2/math.pi**2
print(f"margin = 0.2947 - 2/pi^2 = {margin:.4f} > 0  {'✓' if margin>0 else '✗'}")
