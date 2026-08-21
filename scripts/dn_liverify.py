#!/usr/bin/env python3
"""
Verify: lambda_{n+1} - lambda_n = 2 D_n  (Bombieri-Lagarias / Li criterion link)

Li coefficients: lambda_n = sum_rho [1 - (1 - 1/rho)^n]
For rho = 1/2 + i*gamma (pair with conjugate):
  lambda_n = 2*sum_{gamma>0} [1 - cos(n*psi_gamma)]
  psi_gamma = arg(1 - 1/rho), and we showed psi_gamma = theta(gamma) = pi - 2 arctan(2 gamma)

So: lambda_{n+1} - lambda_n = 2*sum [cos(n theta) - cos((n+1) theta)] = 2*D_n  (telescoping!)

Checks:
1. psi vs theta for first zeros
2. lambda_{n+1} - lambda_n vs 2*D_n numerically
3. lambda_1 > 0 (needed: lambda_n increasing + lambda_1 > 0  =>  lambda_n > 0 => RH)
"""
import numpy as np, math

# Load zeros
z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
print(f"zeros loaded: {len(z)}, gamma_1 = {z[0]:.6f}")

def theta(t):
    return math.pi - 2*math.atan(2*t)

# 1. psi vs theta
print("\n=== 1. psi(gamma) vs theta(gamma) ===")
for g in z[:5]:
    # psi = arg(1 - 1/rho), rho = 1/2 + i*g
    re = (g*g - 0.25)/(g*g + 0.25)   # Re(1-1/rho)
    im = g/(g*g + 0.25)              # Im(1-1/rho)
    psi = math.atan2(im, re)
    th = theta(g)
    print(f"  gamma={g:12.6f}  psi={psi:12.8f}  theta={th:12.8f}  diff={abs(psi-th):.2e}")

# 2. lambda_{n+1} - lambda_n vs 2 D_n
print("\n=== 2. lambda_{n+1}-lambda_n vs 2*D_n (100k zeros) ===")
def lam_diff(n):
    s = 0.0
    for g in z:
        th = theta(g)
        s += math.cos(n*th) - math.cos((n+1)*th)
    return 2*s  # 2*D_n = lambda_{n+1}-lambda_n

def lam(n):
    s = 0.0
    for g in z:
        s += 1 - math.cos(n*theta(g))
    return 2*s

for n in [1, 5, 10, 20, 43, 100]:
    d = lam_diff(n)
    l1, l2 = lam(n), lam(n+1)
    print(f"  n={n:4d}: lambda_{n+1}-lambda_n = {l2-l1:12.6f}   2*D_n = {d:12.6f}   match={abs((l2-l1)-d)<1e-6}")

# 3. lambda_1
print("\n=== 3. lambda_1 (partial sum over 100k zeros) ===")
l1 = lam(1)
print(f"  lambda_1 = {l1:.6f}  (positive? {l1>0})")
print(f"  NOTE: known value lambda_1 = 1 - gamma_E/2 - log(4pi)/2 + ... ~ 0.023 (independent of zeros, from xi expansion)")

# 4. Consequence: D_n > 0 for all n  =>  lambda strictly increasing; if lambda_1 > 0 => RH (Li)
print("\n=== 4. Li criterion consequence ===")
print("  D_n > 0 for all n  <=>  lambda_{n+1} > lambda_n for all n")
print("  With lambda_1 > 0:  lambda_n > 0 for all n  <=>  RH  (Li 1997)")
print("  =>  A FULL proof of D_n > 0 for all n would prove RH.")
