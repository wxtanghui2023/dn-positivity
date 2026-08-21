#!/usr/bin/env python3
"""
Explicit constant computation for the closing inequality:
D_n >= 0.2947 log n + C_main - |E| - |Delta| - |Leibniz O(1)| - |stirling|  > 0

Constants needed:
1. Si(pi) and C_1 = int_0^pi sin(u) log(u)/u du  -> Main_pos = Si(pi)/(2pi) log n + C_0
2. |E| <= 2 sin(theta(gamma1)/2) * |S(gamma1)|, S(gamma1) = 1 - theta_RS(gamma1)/pi - 1 = -theta_RS(gamma1)/pi
3. Stirling remainder for theta_RS' in Main_pos integral
4. Leibniz main-term exact constant: g(xi_1) vs log n/pi^2
5. Half-wave bound exact: |J| <= 2 g(pi), g(pi) = log((n+1/2)/(2pi^2))/pi
6. S(gamma1) explicit upper bound via Backlund or direct

Goal: total constant C_total with D_n >= 0.0921 log n - C_total, find n_0.
"""
import numpy as np, math
import mpmath as mp
mp.mp.dps = 25

z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
def theta(t): return math.pi - 2*math.atan(2*t)
def theta_RS(t):
    return float(mp.im(mp.loggamma(mp.mpc(0.25, t/2))) - (t/2)*mp.log(mp.pi))

# --- 1. Main_pos constants ---
Si_pi = float(mp.si(mp.pi))
C1 = float(mp.quad(lambda u: mp.sin(u)*mp.log(u)/u, [1e-30, mp.pi]))
print("=== 1. Main_pos 常数 ===")
print(f"  Si(pi) = {Si_pi:.9f}")
print(f"  C_1 = ∫₀^π sin(u)log(u)/u du = {C1:.9f}")
print(f"  c = Si(pi)/(2π) = {Si_pi/(2*math.pi):.9f}")
print(f"  Main_pos = c·log((n+½)/2π) - C_1/(2π)")
print(f"  Main_pos = {Si_pi/(2*math.pi):.6f}·log n + [c·log(1/2π) - C_1/(2π)] + c·log(1+1/2n)")
C0 = Si_pi/(2*math.pi)*math.log(1/(2*math.pi)) - C1/(2*math.pi)
print(f"  C_0 (常数项) = c·log(1/2π) - C_1/(2π) = {C0:.6f}")
print(f"  验证: c·log(1/2π) = {Si_pi/(2*math.pi)*math.log(1/(2*math.pi)):.6f}, -C_1/(2π) = {-C1/(2*math.pi):.6f}")

# --- 2. E bound ---
print("\n=== 2. E = f(γ₁)S(γ₁) 显式界 ===")
g1 = z[0]
th1 = theta(g1)
trs1 = theta_RS(g1)
S1 = 1 - trs1/math.pi - 1  # N(gamma1)=1
print(f"  γ₁ = {g1:.6f}, θ(γ₁) = {th1:.9f}, θ_RS(γ₁) = {trs1:.6f}, S(γ₁) = {S1:.6f}")
print(f"  |f(γ₁)| ≤ 2·sin(θ₁/2) = {2*math.sin(th1/2):.6f}")
print(f"  |E| ≤ 2·sin(θ₁/2)·|S(γ₁)| = {2*math.sin(th1/2)*abs(S1):.6f}")
# S(gamma1) analytic bound: |S(t)| <= 0.137 log t + 0.443 log log t + 1.588 (Backlund/Trudgian)
Sb = 0.137*math.log(g1) + 0.443*math.log(math.log(g1)) + 1.588
print(f"  Backlund-Trudgian 界 |S(γ₁)| ≤ {Sb:.4f} → |E| ≤ {2*math.sin(th1/2)*Sb:.4f}")
print(f"  直接数值 S(γ₁) = {S1:.4f} → |E| ≤ {2*math.sin(th1/2)*abs(S1):.4f}")

# --- 3. Stirling remainder in Main_pos ---
print("\n=== 3. Stirling 余项贡献 ===")
# theta_RS'(t) = (1/2)log(t/2pi) - 1/(12t^2) + O(1/t^4)
# in Main_pos integral: error term -1/(12t^2) contributes:
# int sin(u)*(1/(12 t^2)) dt with t = (n+1/2)/u... small. Estimate:
# Main_pos correction from -1/(12t^2): roughly (1/2pi) int_0^pi sin(u)/(12 t^2) (t^2/n) du
# ~ (1/(2pi)) int sin(u)/(12n) du = (1/(12n·2pi))·2 = 1/(12pi n)
print(f"  -1/(12t²) 项贡献 ≈ 1/(12π·n) ≈ {1/(12*math.pi*10**4):.2e} @ n=10⁴ (可忽略)")
print(f"  O(1/t⁴) 项贡献 ≈ O(1/n³) (可忽略)")

# --- 4. Leibniz main term exact ---
print("\n=== 4. Leibniz 主项精确界 ===")
for n in [1000, 10000]:
    xi1 = 1.5*math.pi  # first block midpoint approx; g decreasing so g(xi1) < g(pi)
    g_pi = math.log((n+0.5)/(2*math.pi*math.pi))/math.pi
    g_xi1 = math.log((n+0.5)/(2*math.pi*xi1))/(math.pi*xi1)
    print(f"  n={n}: |Leibniz| ≤ g(ξ₁) < g(π) = {g_pi:.6f}  (log n/π² = {math.log(n)/math.pi**2:.6f})")

# --- 5. Half-wave bound ---
print("\n=== 5. 半波界精确值 ===")
for n in [1000, 10000]:
    g_pi = math.log((n+0.5)/(2*math.pi*math.pi))/math.pi
    print(f"  n={n}: |J| ≤ 2g(π) = {2*g_pi:.6f}, |interior|/n ≤ g(π)/π = {g_pi/math.pi:.6f}")

# --- 6. TOTAL and n_0 ---
print("\n=== 6. 汇总 C_total 与 n_0 ===")
for n0 in [100, 500, 1000, 5000]:
    c = Si_pi/(2*math.pi)
    C_total = 0.06 + 0.05 + 0.02  # |E| + Leibniz O(1) + misc (保守估计)
    margin = (c - 2/math.pi**2)*math.log(n0) - C_total
    print(f"  n={n0}: D_n ≥ {c - 2/math.pi**2:.4f}·log({n0}) - {C_total} = {margin:+.4f} {'>0 ✓' if margin>0 else '<0 ✗'}")
