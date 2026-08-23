#!/usr/bin/env python3
"""攻击离轴差：假设离轴零点的贡献——结构分析
离轴差 = Σ_离轴[2−2r^n cos(nφ) − 4sin²(nθ₁)]
r = |1−1/ρ| > 1（β<½）——物理指引：刚性/BKT 是否约束？
分析：单离轴零点的贡献（n 依赖）——慢燃（γ 大时）
"""
import numpy as np
import gc
from math import log, pi, sqrt

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

z = load_zeros(100000)
g1 = z[0]

def th1(t):
    return np.arctan(1/(2*t))

# 单离轴零点的离轴差贡献：2−2r^n cos(nφ) − 4sin²(nθ₁(γ))
def off_axis_contrib(beta, gamma, n):
    """β<½ 离轴零点（β+iγ）的 λ_n 贡献与 sin² 核的差"""
    rho = beta + 1j*gamma
    omr = 1 - 1/rho  # 1−1/ρ
    r = abs(omr)
    phi = np.angle(omr)
    real_contrib = 2 - 2*r**n*np.cos(n*phi)  # 上下对（ρ, ρ̄）
    # sin² 核的"假设贡献"（如果该零点在临界线）
    sin2 = 4*np.sin(n*th1(gamma))**2
    return real_contrib - sin2, r

print("单离轴零点的离轴差贡献（β<½——n 依赖）：")
print(f"{'β':>6} {'γ':>8} {'r':>8} {'n=10':>10} {'n=100':>10} {'n=500':>10} {'n=2000':>10}")
for beta, gamma in [(0.49, 100), (0.45, 100), (0.40, 100), (0.49, 1000), (0.45, 1000)]:
    row = []
    rs = []
    for n in [10, 100, 500, 2000]:
        c, r = off_axis_contrib(beta, gamma, n)
        row.append(c)
        rs.append(r)
    print(f"{beta:6.2f} {gamma:8d} {rs[0]:8.4f} {row[0]:+10.2f} {row[1]:+10.2f} {row[2]:+10.2f} {row[3]:+10.2f}")

# 关键：离轴差的"慢燃"——r^n 的量级 vs n
print("\n离轴差的慢燃（r^n 何时超过 nlogn）：")
for beta, gamma in [(0.49, 100), (0.45, 100), (0.49, 1000), (0.49, 10000)]:
    rho = beta + 1j*gamma
    r = abs(1 - 1/rho)
    # r^n = nlogn 的 n
    n_break = 0
    for n in [10, 100, 1000, 10000, 100000, 1000000]:
        if r**n > n*log(n):
            n_break = n
            break
    print(f"  β={beta}, γ={gamma}: r = {r:.6f}——r^n > nlogn 在 n ≈ {n_break}")

# 物理指引检验：如果离轴零点存在——刚性（Σδ=O(1)）是否"感觉"到？
# 离轴零点的虚部 γ 参与 δ（虚部间距）——但 β 不参与
print("\n物理指引检验（刚性是否约束 β）：")
print("  δ_k = Δγ_k·N₀' − 1——只含虚部——不含 β")
print("  ⟹ 刚性（Σδ=O(1)）不知道零点实部——不直接约束离轴")
print("  ⟹ 物理指引需要别的机制（BBH 伪自伴/排斥势）约束 β")

# 关键：反证法的检测阈值（数值能排除的离轴）
print("\n数值检测阈值（λ_n = O(1)——n≤3000 能排除什么）：")
for beta in [0.49, 0.45, 0.40]:
    for gamma in [100, 1000, 10000]:
        rho = beta + 1j*gamma
        r = abs(1 - 1/rho)
        n_break = int(2*gamma*gamma/(1-2*beta))  # r^n ~ exp(n(1-2β)/2γ²) > 1 的阈值
        detected = n_break < 3000
        print(f"  β={beta}, γ={gamma}: n_break ≈ {n_break}——{'可检测（n≤3000）' if detected else '不可检测（慢燃）'}")

del z
gc.collect()
print("内存已释放")
