#!/usr/bin/env python3
"""
ADVERSARIAL SELF-AUDIT of the epsilon_m bound.

Chain: sum_eps = E + interior/n
  E = -f(gamma1)S(gamma1)
  interior/n = (1/(n+1/2)) * [boundary + integral]

AUDIT POINTS:
A. Exact relation: E vs phi-coord boundary term phi_max sin(phi_max) S(gamma1)/(n+1/2)
   f(gamma1) = 2 sin(phi_max) sin(theta1/2). Claim: f(gamma1) ~ phi_max sin(phi_max)/(n+1/2)
   => phi_max sin(phi_max) S(gamma1)/(n+1/2) ~ E. Verify EXACTLY how close.
B. sin(theta/2) -> theta/2 error: relative error bound on [pi, phi_max]
C. cos(theta/2) -> 1 error
D. theta_RS' Stirling remainder: |theta_RS'(t) - (1/2)log(t/2pi)| <= 1/(12t^2) + C/t^4 ?
E. theta(t) ~ 1/t error: |theta(t) - 1/t| <= 1/(12t^3)?
F. Half-wave lemma |J| <= 2g(pi): verify for the EXACT integrand with all corrections
G. Total: |sum_eps| <= 0.04 + log(n/2pi^2)/pi^2 + corrections? Measure actual vs bound.
"""
import numpy as np, math

z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
def theta(t): return math.pi - 2*np.arctan(2*np.asarray(t, dtype=float))
def theta_RS(t):
    import mpmath as mp
    mp.mp.dps = 15
    return float(mp.im(mp.loggamma(mp.mpc(0.25, t/2))) - (t/2)*mp.log(mp.pi))
def dtheta_RS(t):
    import mpmath as mp
    mp.mp.dps = 15
    return float(mp.re(mp.digamma(mp.mpc(0.25, t/2)))/2 - mp.log(mp.pi)/2)
def S_of_t(t):
    return np.searchsorted(z, t, side='right') - theta_RS(t)/math.pi - 1

print("=== AUDIT A: E vs boundary term ===")
for n in [1000, 5000, 10000]:
    g1 = z[0]; phi_max = (n+0.5)*theta(g1)
    E = 2*math.sin(phi_max)*math.sin(theta(g1)/2)*S_of_t(g1)
    bdry_n = phi_max*math.sin(phi_max)*S_of_t(g1)/(n+0.5)
    print(f"  n={n}: E={E:+.6f}, bdry/n={bdry_n:+.6f}, 差={E-bdry_n:+.6f}")
    # 精确关系: f(gamma1) = 2 sin(phi) sin(theta/2), phi_max sin(phi)/(n+1/2) = ? 
    # 2 sin(phi) sin(th/2) vs phi sin(phi)/(n+1/2): ratio = 2(n+1/2)sin(th/2)/phi
    r = 2*(n+0.5)*math.sin(theta(g1)/2)/phi_max
    print(f"    比值 f/bdry = {r:.6f} (应≈1: 2(n+½)sin(θ/2)/φ = {2*(n+0.5)*math.sin(theta(g1)/2)/phi_max:.6f})")

print("\n=== AUDIT B/C: sin(θ/2)≈θ/2, cos(θ/2)≈1 误差 (θ=φ/(n+½), φ∈[π,φ_max]) ===")
for n in [1000, 10000]:
    phis = np.linspace(math.pi, 0.0707*(n+0.5), 10000)
    th = phis/(n+0.5)
    err_sin = np.abs(np.sin(th/2) - th/2)/(th/2)
    err_cos = np.abs(np.cos(th/2) - 1)
    print(f"  n={n}: max|sin(θ/2)-θ/2|/(θ/2) = {err_sin.max():.2e}, max|cos(θ/2)-1| = {err_cos.max():.2e}")

print("\n=== AUDIT D: θ_RS' Stirling 余项 ===")
for t in [14.13, 50, 100, 318, 1000]:
    appr = 0.5*math.log(t/(2*math.pi)) - 1/(12*t*t)
    real = dtheta_RS(t)
    print(f"  t={t:8.1f}: θ_RS'={real:+.6f}, Stirling={appr:+.6f}, 差={real-appr:+.2e}")

print("\n=== AUDIT E: θ(t)≈1/t 误差 ===")
for t in [14.13, 50, 100, 318, 1000]:
    th = theta(t); inv = 1/t
    print(f"  t={t:8.1f}: θ={th:.6f}, 1/t={inv:.6f}, 差={abs(th-inv):.2e}, 1/(12t³)={1/(12*t**3):.2e}")

print("\n=== AUDIT G: 实际 |Σε| vs 界 0.04 + log(n/2π²)/π² ===")
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
for n in [1000, 5000, 10000, 20000]:
    eps = blocks_eps(n)
    s = abs(eps.sum())
    bd = 0.04 + math.log((n+0.5)/(2*math.pi**2))/math.pi**2
    print(f"  n={n}: |Σε|={s:.5f}  界={bd:.5f}  裕量={bd-s:.5f}")
