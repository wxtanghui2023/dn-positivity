#!/usr/bin/env python3
"""
Rigorous check of the van der Corput / alternating-half-wave argument for
J = int_{pi}^{phi_max} sin(phi) g(phi) dphi,  g(phi) = log(A/phi)/phi, A = n/2pi.

Claim: |J| <= 2 g(pi) if g decreasing and phi_max is a half-integer multiple of pi,
with a correction for the partial last wave. Check numerically:
1. g decreasing on [pi, phi_max]?
2. |J| vs 2 g(pi) vs true value
3. Partial-wave correction size
"""
import numpy as np, math

def g(phi, n):
    A = n/(2*math.pi)
    return np.log(A/np.maximum(phi,1e-12))/np.maximum(phi,1e-12)

print("=== g(phi) 单调性检查 ===")
for n in [1000, 10000]:
    phi_max = (n+0.5)*0.070718
    phis = np.linspace(math.pi, phi_max, 1000)
    gv = g(phis, n)
    mono = np.all(np.diff(gv) < 0)
    print(f"n={n}: g 单调递减? {mono}  (g(pi)={gv[0]:.4f}, g(phi_max)={gv[-1]:.6f})")

print("\n=== |J| vs 2g(pi) vs 真值 ===")
for n in [1000, 5000, 10000, 20000]:
    phi_max = (n+0.5)*0.070718
    phis = np.linspace(math.pi, phi_max, 400000)
    J = np.trapz(np.sin(phis)*g(phis, n), phis)
    bound2 = 2*g(math.pi, n)
    print(f"n={n}: J={J:+.4f}, |J|={abs(J):.4f}, 2g(pi)={bound2:.4f}, |J|<=2g(pi)? {abs(J)<=bound2}")
    # 实际: J 应该 ~ -2.2 (之前看到收敛到常数), 而 2g(pi) ~ 2*log(n/2pi^2)/pi 很大
    print(f"     J/(logn) = {J/math.log(n):+.4f}")
