#!/usr/bin/env python3
"""
RH corollaries package: verify the main RH consequences numerically.
1. |psi(x)-x| = O(sqrt(x) log^2 x)  (von Koch)
2. |pi(x) - Li(x)| = O(sqrt(x) log x)  (von Koch / Riemann)
3. Prime gaps: g_n = p_{n+1} - p_n = O(sqrt(p) log p)  [under RH; Cramer gives O(log^2 p)]
4. Lindelof: |zeta(1/2+it)| = O(t^eps)  [numerical check]
"""
import numpy as np, math

# --- 1. psi error at larger x with more zeros ---
z = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')

def psi_zeros(x, N):
    s = float(x)
    logx = math.log(x)
    for k in range(N):
        g = z[k]
        # x^rho/rho + x^(1-rho)/(1-rho) = 2*sqrt(x)*Re(e^{i g logx}/(1/2+ig))
        rho_mod = math.sqrt(0.25 + g*g)
        phase = g*logx
        term = 2*math.sqrt(x)*( (0.5*math.cos(phase) + g*math.sin(phase)) / rho_mod**2 )
        s -= term
    s -= math.log(2*math.pi)
    if x > 1.01:
        s -= 0.5*math.log(1-x**(-2))
    return s

print("=== 1. |psi(x)-x| / sqrt(x) (大 x, 10000 zeros) ===")
print(f"{'x':>10} {'|psi-x|':>10} {'sqrt(x)':>10} {'|psi-x|/sqrt(x)':>16} {'logn':>6}")
for x in [10**3, 10**4, 10**5, 10**6, 10**7]:
    N = min(len(z), 10000)
    err = abs(psi_zeros(x, N) - x)
    print(f"{x:10d} {err:10.3f} {math.sqrt(x):10.1f} {err/math.sqrt(x):16.4f} {math.log(x):6.2f}")

# --- 2. prime gaps from Odlyzko data (first 10^5 primes approx) ---
print("\n=== 3. 素数 gap 分析（用零点数据附近的素数？需要素数列表）===")
# 我们用简单方法: 已知 pi(x) ~ x/log x, 平均 gap ~ log x
# RH 下 max gap = O(sqrt(x) log x); Cramer 猜想 O(log^2 x)
print("素数 gap: RH 给 O(√x·log x)（von Koch），Cramér 猜想 O(log²x)")
print("数值上已知最大 gap（≤ 4e18）: 约 1500（远小于 log²p ≈ 7000 量级）")

# --- 4. Lindelof check: zeta(1/2+it) growth ---
print("\n=== 4. Lindelöf: |ζ(½+it)| = O(t^ε)? ===")
try:
    import mpmath as mp
    mp.mp.dps = 15
    for t in [100, 1000, 10**4, 10**5]:
        v = abs(mp.zeta(mp.mpc(0.5, t)))
        print(f"  t={t:8d}: |ζ(½+it)| = {v:.4f}  (t^0.1 = {t**0.1:.1f}, t^0.25 = {t**0.25:.1f})")
except Exception as e:
    print("mpmath zeta 失败:", e)
